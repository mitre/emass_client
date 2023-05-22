# coding: utf-8

## eMASS API v3.9 Specification

The emass_client_api is a Python client that implements the [Enterprise Mission Assurance Support Service (eMASS)](https://disa.mil/~/media/Files/DISA/Fact-Sheets/eMASS.pdf)
Representational State Transfer (REST) Application Programming Interface (API) specifications.


This Python package was generated from the eMASS API specification:

- API version: v3.9
- Package version: 3.8.3
- Build date: 2023-05-22T22:31:52.941872Z[Etc/UTC]

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
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conlist, validator
from emass_client.models.milestones_get import MilestonesGet

class PoamGet(BaseModel):
    """
    PoamGet
    """
    external_uid: Optional[StrictStr] = Field(None, alias="externalUid", description="[Optional] Unique identifier external to the eMASS application for use with associating POA&Ms. 100 Characters.")
    system_id: Optional[StrictInt] = Field(None, alias="systemId", description="[Required] Unique eMASS system identifier.")
    poam_id: Optional[StrictInt] = Field(None, alias="poamId", description="[Required] Unique item identifier")
    display_poam_id: Optional[StrictInt] = Field(None, alias="displayPoamId", description="[Required] Globally unique identifier for individual POA&M Items, seen on the front-end as “ID”.")
    is_inherited: Optional[StrictBool] = Field(None, alias="isInherited", description="[Read-only] Indicates whether a test result is inherited.")
    control_acronym: Optional[StrictStr] = Field(None, alias="controlAcronym", description="[Optional] System acronym name.")
    cci: Optional[StrictStr] = Field(None, description="[Optional] CCI associated with POA&M Item..")
    status: Optional[StrictStr] = Field(None, description="[Required] Values include the following: (Ongoing,Risk Accepted,Completed,Not Applicable")
    review_status: Optional[StrictStr] = Field(None, alias="reviewStatus", description="[Read-Only] Values include the following options: (Not Approved,Under Review,Approved)")
    vulnerability_description: Optional[StrictStr] = Field(None, alias="vulnerabilityDescription", description="[Required] Provide a description of the POA&M Item. 2000 Characters.")
    source_ident_vuln: Optional[StrictStr] = Field(None, alias="sourceIdentVuln", description="[Required] Include Source Identifying Vulnerability text. 2000 Characters.")
    security_checks: Optional[StrictStr] = Field(None, alias="securityChecks", description="[Optional] Security Checks that are associated with the POA&M.")
    milestones: Optional[conlist(MilestonesGet)] = None
    poc_organization: Optional[StrictStr] = Field(None, alias="pocOrganization", description="[Required] Organization/Office represented. 100 Characters.")
    poc_first_name: Optional[StrictStr] = Field(None, alias="pocFirstName", description="[Conditional] First name of POC. 100 Characters.")
    poc_last_name: Optional[StrictStr] = Field(None, alias="pocLastName", description="[Conditional] Last name of POC. 100 Characters.")
    poc_email: Optional[StrictStr] = Field(None, alias="pocEmail", description="[Conditional] Email address of POC. 100 Characters.")
    poc_phone_number: Optional[StrictStr] = Field(None, alias="pocPhoneNumber", description="[Conditional] Phone number of POC. 100 Characters.")
    severity: Optional[StrictStr] = Field(None, description="[Conditional] Required for approved items. Values include the following options (Very Low,Low,Moderate,High,Very High)")
    raw_severity: Optional[StrictStr] = Field(None, alias="rawSeverity", description="[Optional] Values include the following options (I,II,III)")
    relevance_of_threat: Optional[StrictStr] = Field(None, alias="relevanceOfThreat", description="[Optional] Values include the following options: (Very Low,Low,Moderate,High,Very High)")
    likelihood: Optional[StrictStr] = Field(None, description="[Optional] Values include the following options: (Very Low,Low,Moderate,High,Very High)")
    impact: Optional[StrictStr] = Field(None, description="[Optional] Values include the following options: (Very Low,Low,Moderate,High,Very High)")
    impact_description: Optional[StrictStr] = Field(None, alias="impactDescription", description="[Optional] Include description of Security Control’s impact.")
    residual_risk_level: Optional[StrictStr] = Field(None, alias="residualRiskLevel", description="[Optional] Values include the following options: (Very Low,Low,Moderate,High,Very High)")
    recommendations: Optional[StrictStr] = Field(None, description="[Optional] Include recommendations. Character Limit = 2,000.")
    resources: Optional[StrictStr] = Field(None, description="[Required] List of resources used. 250 Characters.")
    scheduled_completion_date: Optional[StrictInt] = Field(None, alias="scheduledCompletionDate", description="[Conditional] Required for ongoing and completed POA&M items. Unix time format.")
    completion_date: Optional[StrictInt] = Field(None, alias="completionDate", description="[Conditional] Field is required for completed POA&M items. Unix time format.")
    extension_date: Optional[StrictInt] = Field(None, alias="extensionDate", description="[Read-Only] Value returned for a POA&M Item with review status Approved” and has a milestone with a scheduled completion date that extends beyond the POA&M Item’s scheduled completion date. ")
    comments: Optional[StrictStr] = Field(None, description="[Conditional] Field is required for completed and risk accepted POA&M items. 2000 Characters")
    mitigation: Optional[StrictStr] = Field(None, description="[Optional] Include mitigation explanation. 2000 Characters.")
    is_active: Optional[StrictBool] = Field(None, alias="isActive", description="[Conditional] Optionally used in PUT to delete milestones when updating a POA&M.")
    __properties = ["externalUid", "systemId", "poamId", "displayPoamId", "isInherited", "controlAcronym", "cci", "status", "reviewStatus", "vulnerabilityDescription", "sourceIdentVuln", "securityChecks", "milestones", "pocOrganization", "pocFirstName", "pocLastName", "pocEmail", "pocPhoneNumber", "severity", "rawSeverity", "relevanceOfThreat", "likelihood", "impact", "impactDescription", "residualRiskLevel", "recommendations", "resources", "scheduledCompletionDate", "completionDate", "extensionDate", "comments", "mitigation", "isActive"]

    @validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Ongoing', 'Risk Accepted', 'Completed', 'Not Applicable', 'Archived'):
            raise ValueError("must be one of enum values ('Ongoing', 'Risk Accepted', 'Completed', 'Not Applicable', 'Archived')")
        return value

    @validator('review_status')
    def review_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Not Approved', 'Under Review', 'Approved'):
            raise ValueError("must be one of enum values ('Not Approved', 'Under Review', 'Approved')")
        return value

    @validator('severity')
    def severity_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Very Low', 'Low', 'Moderate', 'High', 'Very High'):
            raise ValueError("must be one of enum values ('Very Low', 'Low', 'Moderate', 'High', 'Very High')")
        return value

    @validator('raw_severity')
    def raw_severity_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('I', 'II', 'III'):
            raise ValueError("must be one of enum values ('I', 'II', 'III')")
        return value

    @validator('relevance_of_threat')
    def relevance_of_threat_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Very Low', 'Low', 'Moderate', 'High', 'Very High'):
            raise ValueError("must be one of enum values ('Very Low', 'Low', 'Moderate', 'High', 'Very High')")
        return value

    @validator('likelihood')
    def likelihood_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Very Low', 'Low', 'Moderate', 'High', 'Very High'):
            raise ValueError("must be one of enum values ('Very Low', 'Low', 'Moderate', 'High', 'Very High')")
        return value

    @validator('impact')
    def impact_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Very Low', 'Low', 'Moderate', 'High', 'Very High'):
            raise ValueError("must be one of enum values ('Very Low', 'Low', 'Moderate', 'High', 'Very High')")
        return value

    @validator('residual_risk_level')
    def residual_risk_level_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Very Low', 'Low', 'Moderate', 'High', 'Very High'):
            raise ValueError("must be one of enum values ('Very Low', 'Low', 'Moderate', 'High', 'Very High')")
        return value

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> PoamGet:
        """Create an instance of PoamGet from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in milestones (list)
        _items = []
        if self.milestones:
            for _item in self.milestones:
                if _item:
                    _items.append(_item.to_dict())
            _dict['milestones'] = _items
        # set to None if external_uid (nullable) is None
        # and __fields_set__ contains the field
        if self.external_uid is None and "external_uid" in self.__fields_set__:
            _dict['externalUid'] = None

        # set to None if is_inherited (nullable) is None
        # and __fields_set__ contains the field
        if self.is_inherited is None and "is_inherited" in self.__fields_set__:
            _dict['isInherited'] = None

        # set to None if control_acronym (nullable) is None
        # and __fields_set__ contains the field
        if self.control_acronym is None and "control_acronym" in self.__fields_set__:
            _dict['controlAcronym'] = None

        # set to None if cci (nullable) is None
        # and __fields_set__ contains the field
        if self.cci is None and "cci" in self.__fields_set__:
            _dict['cci'] = None

        # set to None if review_status (nullable) is None
        # and __fields_set__ contains the field
        if self.review_status is None and "review_status" in self.__fields_set__:
            _dict['reviewStatus'] = None

        # set to None if security_checks (nullable) is None
        # and __fields_set__ contains the field
        if self.security_checks is None and "security_checks" in self.__fields_set__:
            _dict['securityChecks'] = None

        # set to None if poc_first_name (nullable) is None
        # and __fields_set__ contains the field
        if self.poc_first_name is None and "poc_first_name" in self.__fields_set__:
            _dict['pocFirstName'] = None

        # set to None if poc_last_name (nullable) is None
        # and __fields_set__ contains the field
        if self.poc_last_name is None and "poc_last_name" in self.__fields_set__:
            _dict['pocLastName'] = None

        # set to None if poc_email (nullable) is None
        # and __fields_set__ contains the field
        if self.poc_email is None and "poc_email" in self.__fields_set__:
            _dict['pocEmail'] = None

        # set to None if poc_phone_number (nullable) is None
        # and __fields_set__ contains the field
        if self.poc_phone_number is None and "poc_phone_number" in self.__fields_set__:
            _dict['pocPhoneNumber'] = None

        # set to None if severity (nullable) is None
        # and __fields_set__ contains the field
        if self.severity is None and "severity" in self.__fields_set__:
            _dict['severity'] = None

        # set to None if raw_severity (nullable) is None
        # and __fields_set__ contains the field
        if self.raw_severity is None and "raw_severity" in self.__fields_set__:
            _dict['rawSeverity'] = None

        # set to None if relevance_of_threat (nullable) is None
        # and __fields_set__ contains the field
        if self.relevance_of_threat is None and "relevance_of_threat" in self.__fields_set__:
            _dict['relevanceOfThreat'] = None

        # set to None if likelihood (nullable) is None
        # and __fields_set__ contains the field
        if self.likelihood is None and "likelihood" in self.__fields_set__:
            _dict['likelihood'] = None

        # set to None if impact (nullable) is None
        # and __fields_set__ contains the field
        if self.impact is None and "impact" in self.__fields_set__:
            _dict['impact'] = None

        # set to None if impact_description (nullable) is None
        # and __fields_set__ contains the field
        if self.impact_description is None and "impact_description" in self.__fields_set__:
            _dict['impactDescription'] = None

        # set to None if residual_risk_level (nullable) is None
        # and __fields_set__ contains the field
        if self.residual_risk_level is None and "residual_risk_level" in self.__fields_set__:
            _dict['residualRiskLevel'] = None

        # set to None if recommendations (nullable) is None
        # and __fields_set__ contains the field
        if self.recommendations is None and "recommendations" in self.__fields_set__:
            _dict['recommendations'] = None

        # set to None if scheduled_completion_date (nullable) is None
        # and __fields_set__ contains the field
        if self.scheduled_completion_date is None and "scheduled_completion_date" in self.__fields_set__:
            _dict['scheduledCompletionDate'] = None

        # set to None if completion_date (nullable) is None
        # and __fields_set__ contains the field
        if self.completion_date is None and "completion_date" in self.__fields_set__:
            _dict['completionDate'] = None

        # set to None if extension_date (nullable) is None
        # and __fields_set__ contains the field
        if self.extension_date is None and "extension_date" in self.__fields_set__:
            _dict['extensionDate'] = None

        # set to None if comments (nullable) is None
        # and __fields_set__ contains the field
        if self.comments is None and "comments" in self.__fields_set__:
            _dict['comments'] = None

        # set to None if mitigation (nullable) is None
        # and __fields_set__ contains the field
        if self.mitigation is None and "mitigation" in self.__fields_set__:
            _dict['mitigation'] = None

        # set to None if is_active (nullable) is None
        # and __fields_set__ contains the field
        if self.is_active is None and "is_active" in self.__fields_set__:
            _dict['isActive'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PoamGet:
        """Create an instance of PoamGet from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PoamGet.parse_obj(obj)

        _obj = PoamGet.parse_obj({
            "external_uid": obj.get("externalUid"),
            "system_id": obj.get("systemId"),
            "poam_id": obj.get("poamId"),
            "display_poam_id": obj.get("displayPoamId"),
            "is_inherited": obj.get("isInherited"),
            "control_acronym": obj.get("controlAcronym"),
            "cci": obj.get("cci"),
            "status": obj.get("status"),
            "review_status": obj.get("reviewStatus"),
            "vulnerability_description": obj.get("vulnerabilityDescription"),
            "source_ident_vuln": obj.get("sourceIdentVuln"),
            "security_checks": obj.get("securityChecks"),
            "milestones": [MilestonesGet.from_dict(_item) for _item in obj.get("milestones")] if obj.get("milestones") is not None else None,
            "poc_organization": obj.get("pocOrganization"),
            "poc_first_name": obj.get("pocFirstName"),
            "poc_last_name": obj.get("pocLastName"),
            "poc_email": obj.get("pocEmail"),
            "poc_phone_number": obj.get("pocPhoneNumber"),
            "severity": obj.get("severity"),
            "raw_severity": obj.get("rawSeverity"),
            "relevance_of_threat": obj.get("relevanceOfThreat"),
            "likelihood": obj.get("likelihood"),
            "impact": obj.get("impact"),
            "impact_description": obj.get("impactDescription"),
            "residual_risk_level": obj.get("residualRiskLevel"),
            "recommendations": obj.get("recommendations"),
            "resources": obj.get("resources"),
            "scheduled_completion_date": obj.get("scheduledCompletionDate"),
            "completion_date": obj.get("completionDate"),
            "extension_date": obj.get("extensionDate"),
            "comments": obj.get("comments"),
            "mitigation": obj.get("mitigation"),
            "is_active": obj.get("isActive")
        })
        return _obj

