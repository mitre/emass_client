# coding: utf-8

## eMASS API v3.12 Specification

The emass_client_api is a Python client that implements the [Enterprise Mission Assurance Support Service (eMASS)](https://disa.mil/~/media/Files/DISA/Fact-Sheets/eMASS.pdf)
Representational State Transfer (REST) Application Programming Interface (API) specifications.


This Python package was generated from the eMASS API specification:

- API version: v3.12
- Package version: 3.12.0
- Build date: 2023-10-10T14:36:02.975730Z[Etc/UTC]

## Requirements.

Python 

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import emass_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import emass_client
```

### Tests

Execute `pytest` to run the tests.

from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr, field_validator
from pydantic import Field
from emass_client.models.ssps import Ssps
from typing import Dict, Any
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class CmmcGet(BaseModel):
    """
    CmmcGet
    """
    operation: Optional[StrictStr] = Field(default=None, description="[Read-Only] Indicates the action that should be taken on the assessment record since the provided sinceDate.")
    hq_organization_name: Optional[StrictStr] = Field(default=None, description="[Read-Only] The name of the DIB Company.", alias="hqOrganizationName")
    uei: Optional[StrictStr] = Field(default=None, description="[Read-Only] The Unique Entity Identifier assigned to the DIB Company.")
    cage_codes_in_scope: Optional[StrictStr] = Field(default=None, description="[Read-Only] The five position code(s) associated with the Organization Seeking Certification (OSC).", alias="cageCodesInScope")
    osc_name: Optional[StrictStr] = Field(default=None, description="[Read-Only] The name of the Organization Seeking Certification.", alias="oscName")
    scope: Optional[StrictStr] = Field(default=None, description="[Read-Only] The scope of the OSC assessment.")
    scope_description: Optional[StrictStr] = Field(default=None, description="[Read-Only] Brief description of the scope of the OSC assessment", alias="scopeDescription")
    awarded_cmmc_level: Optional[StrictStr] = Field(default=None, description="[Read-Only] The CMMC award level.", alias="awardedCMMCLevel")
    expiration_date: Optional[StrictInt] = Field(default=None, description="[Read-Only] Expiration date of the awarded CMMC certification.", alias="expirationDate")
    assessment_id: Optional[StrictStr] = Field(default=None, description="[Read-Only] Unique identifier for the assessment/certificate.", alias="assessmentId")
    model_version: Optional[StrictStr] = Field(default=None, description="[Read-Only] Version of the CMMC Model used as part of the assessment.", alias="modelVersion")
    highest_level_cage_code: Optional[StrictStr] = Field(default=None, description="[Read-Only] Identifies the highest-level CAGE Code associated with a given organization.", alias="highestLevelCageCode")
    certification_unique_id: Optional[StrictStr] = Field(default=None, description="[Read-Only] Identifies the unique ID that is associated with a given CMMC certification for an organization.", alias="certificationUniqueId")
    poam: Optional[StrictBool] = Field(default=None, description="[Read-Only] Identifies whether any security requirements received a POA&M during the assessment.")
    overall_score: Optional[StrictInt] = Field(default=None, description="[Read-Only] Identifies the overall calculated score for the assessment based on the assigned values to each applicable security requirement.", alias="overallScore")
    osc_assessment_official_last_name: Optional[StrictStr] = Field(default=None, description="[Read-Only] Last name of the company official contracting with the C3PAO for the assessment.", alias="oscAssessmentOfficialLastName")
    osc_assessment_official_first_name: Optional[StrictStr] = Field(default=None, description="[Read-Only] First name of the company official contracting with the C3PAO for the assessment.", alias="oscAssessmentOfficialFirstName")
    osc_assessment_official_email: Optional[StrictStr] = Field(default=None, description="[Read-Only] Email of the company official contracting with the C3PAO for the assessment.", alias="oscAssessmentOfficialEmail")
    osc_assessment_official_title: Optional[StrictStr] = Field(default=None, description="[Read-Only] Title of the company official contracting with the C3PAO for the assessment.", alias="oscAssessmentOfficialTitle")
    ssps: Optional[List[Ssps]] = None
    __properties: ClassVar[List[str]] = ["operation", "hqOrganizationName", "uei", "cageCodesInScope", "oscName", "scope", "scopeDescription", "awardedCMMCLevel", "expirationDate", "assessmentId", "modelVersion", "highestLevelCageCode", "certificationUniqueId", "poam", "overallScore", "oscAssessmentOfficialLastName", "oscAssessmentOfficialFirstName", "oscAssessmentOfficialEmail", "oscAssessmentOfficialTitle", "ssps"]

    @field_validator('operation')
    def operation_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('ADDED', 'UPDATED', 'DELETED'):
            raise ValueError("must be one of enum values ('ADDED', 'UPDATED', 'DELETED')")
        return value

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of CmmcGet from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in ssps (list)
        _items = []
        if self.ssps:
            for _item in self.ssps:
                if _item:
                    _items.append(_item.to_dict())
            _dict['ssps'] = _items
        # set to None if operation (nullable) is None
        # and model_fields_set contains the field
        if self.operation is None and "operation" in self.model_fields_set:
            _dict['operation'] = None

        # set to None if hq_organization_name (nullable) is None
        # and model_fields_set contains the field
        if self.hq_organization_name is None and "hq_organization_name" in self.model_fields_set:
            _dict['hqOrganizationName'] = None

        # set to None if uei (nullable) is None
        # and model_fields_set contains the field
        if self.uei is None and "uei" in self.model_fields_set:
            _dict['uei'] = None

        # set to None if cage_codes_in_scope (nullable) is None
        # and model_fields_set contains the field
        if self.cage_codes_in_scope is None and "cage_codes_in_scope" in self.model_fields_set:
            _dict['cageCodesInScope'] = None

        # set to None if osc_name (nullable) is None
        # and model_fields_set contains the field
        if self.osc_name is None and "osc_name" in self.model_fields_set:
            _dict['oscName'] = None

        # set to None if scope (nullable) is None
        # and model_fields_set contains the field
        if self.scope is None and "scope" in self.model_fields_set:
            _dict['scope'] = None

        # set to None if scope_description (nullable) is None
        # and model_fields_set contains the field
        if self.scope_description is None and "scope_description" in self.model_fields_set:
            _dict['scopeDescription'] = None

        # set to None if awarded_cmmc_level (nullable) is None
        # and model_fields_set contains the field
        if self.awarded_cmmc_level is None and "awarded_cmmc_level" in self.model_fields_set:
            _dict['awardedCMMCLevel'] = None

        # set to None if expiration_date (nullable) is None
        # and model_fields_set contains the field
        if self.expiration_date is None and "expiration_date" in self.model_fields_set:
            _dict['expirationDate'] = None

        # set to None if assessment_id (nullable) is None
        # and model_fields_set contains the field
        if self.assessment_id is None and "assessment_id" in self.model_fields_set:
            _dict['assessmentId'] = None

        # set to None if model_version (nullable) is None
        # and model_fields_set contains the field
        if self.model_version is None and "model_version" in self.model_fields_set:
            _dict['modelVersion'] = None

        # set to None if highest_level_cage_code (nullable) is None
        # and model_fields_set contains the field
        if self.highest_level_cage_code is None and "highest_level_cage_code" in self.model_fields_set:
            _dict['highestLevelCageCode'] = None

        # set to None if certification_unique_id (nullable) is None
        # and model_fields_set contains the field
        if self.certification_unique_id is None and "certification_unique_id" in self.model_fields_set:
            _dict['certificationUniqueId'] = None

        # set to None if poam (nullable) is None
        # and model_fields_set contains the field
        if self.poam is None and "poam" in self.model_fields_set:
            _dict['poam'] = None

        # set to None if osc_assessment_official_last_name (nullable) is None
        # and model_fields_set contains the field
        if self.osc_assessment_official_last_name is None and "osc_assessment_official_last_name" in self.model_fields_set:
            _dict['oscAssessmentOfficialLastName'] = None

        # set to None if osc_assessment_official_first_name (nullable) is None
        # and model_fields_set contains the field
        if self.osc_assessment_official_first_name is None and "osc_assessment_official_first_name" in self.model_fields_set:
            _dict['oscAssessmentOfficialFirstName'] = None

        # set to None if osc_assessment_official_email (nullable) is None
        # and model_fields_set contains the field
        if self.osc_assessment_official_email is None and "osc_assessment_official_email" in self.model_fields_set:
            _dict['oscAssessmentOfficialEmail'] = None

        # set to None if osc_assessment_official_title (nullable) is None
        # and model_fields_set contains the field
        if self.osc_assessment_official_title is None and "osc_assessment_official_title" in self.model_fields_set:
            _dict['oscAssessmentOfficialTitle'] = None

        # set to None if ssps (nullable) is None
        # and model_fields_set contains the field
        if self.ssps is None and "ssps" in self.model_fields_set:
            _dict['ssps'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        """Create an instance of CmmcGet from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "operation": obj.get("operation"),
            "hqOrganizationName": obj.get("hqOrganizationName"),
            "uei": obj.get("uei"),
            "cageCodesInScope": obj.get("cageCodesInScope"),
            "oscName": obj.get("oscName"),
            "scope": obj.get("scope"),
            "scopeDescription": obj.get("scopeDescription"),
            "awardedCMMCLevel": obj.get("awardedCMMCLevel"),
            "expirationDate": obj.get("expirationDate"),
            "assessmentId": obj.get("assessmentId"),
            "modelVersion": obj.get("modelVersion"),
            "highestLevelCageCode": obj.get("highestLevelCageCode"),
            "certificationUniqueId": obj.get("certificationUniqueId"),
            "poam": obj.get("poam"),
            "overallScore": obj.get("overallScore"),
            "oscAssessmentOfficialLastName": obj.get("oscAssessmentOfficialLastName"),
            "oscAssessmentOfficialFirstName": obj.get("oscAssessmentOfficialFirstName"),
            "oscAssessmentOfficialEmail": obj.get("oscAssessmentOfficialEmail"),
            "oscAssessmentOfficialTitle": obj.get("oscAssessmentOfficialTitle"),
            "ssps": [Ssps.from_dict(_item) for _item in obj.get("ssps")] if obj.get("ssps") is not None else None
        })
        return _obj


