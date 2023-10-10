# coding: utf-8

## eMASS API v3.12 Specification

The emass_client_api is a Python client that implements the [Enterprise Mission Assurance Support Service (eMASS)](https://disa.mil/~/media/Files/DISA/Fact-Sheets/eMASS.pdf)
Representational State Transfer (REST) Application Programming Interface (API) specifications.


This Python package was generated from the eMASS API specification:

- API version: v3.12
- Package version: 3.11.0
- Build date: 2023-10-10T00:19:35.596959Z[Etc/UTC]

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


from typing import Optional
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from pydantic import Field
from typing import Dict, Any
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class MockObject(BaseModel):
    """
    MockObject
    """
    poc_organization: Optional[StrictStr] = Field(default=None, description="[Required] Organization/Office represented. 100 Characters.", alias="pocOrganization")
    resources: Optional[StrictStr] = Field(default=None, description="[Required] List of resources used. 250 Characters.")
    owning_organization: Optional[StrictStr] = Field(default=None, description="[Read-Only] Owning organization of the system record. Values match the eMASS instance Organizational Hierarchy.", alias="owningOrganization")
    secondary_organization: Optional[StrictStr] = Field(default=None, description="[Read-only] Secondary organization that owns the system record (i.e. Sub-Organization-level.", alias="secondaryOrganization")
    poc_first_name: Optional[StrictStr] = Field(default=None, description="[Conditional] First name of POC. 100 Characters.", alias="pocFirstName")
    poc_last_name: Optional[StrictStr] = Field(default=None, description="[Conditional] Last name of POC. 100 Characters.", alias="pocLastName")
    poc_email: Optional[StrictStr] = Field(default=None, description="[Conditional] Email address of POC. 100 Characters.", alias="pocEmail")
    poc_phone_number: Optional[StrictStr] = Field(default=None, description="[Conditional] Phone number of POC (area code) ***-**** format. 100 Characters.", alias="pocPhoneNumber")
    severity: Optional[StrictStr] = Field(default=None, description="[Conditional] Required for approved items. Values include the following options: (Very Low, Low, Moderate,High,Very High)")
    scheduled_completion_date: Optional[StrictInt] = Field(default=None, description="[Conditional] Required for ongoing and completed POA&M items. Unix time format.", alias="scheduledCompletionDate")
    completion_date: Optional[StrictInt] = Field(default=None, description="[Conditional] Field is required for completed POA&M items. Unix time format.", alias="completionDate")
    comments: Optional[StrictStr] = Field(default=None, description="[Conditional] Field is required for completed and risk accepted POA&M items. 2000 Characters")
    is_active: Optional[StrictBool] = Field(default=None, description="[Conditional] Optionally used in PUT to delete milestones when updating a POA&M.", alias="isActive")
    __properties: ClassVar[List[str]] = ["pocOrganization", "resources", "owningOrganization", "secondaryOrganization", "pocFirstName", "pocLastName", "pocEmail", "pocPhoneNumber", "severity", "scheduledCompletionDate", "completionDate", "comments", "isActive"]

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
        """Create an instance of MockObject from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if owning_organization (nullable) is None
        # and model_fields_set contains the field
        if self.owning_organization is None and "owning_organization" in self.model_fields_set:
            _dict['owningOrganization'] = None

        # set to None if secondary_organization (nullable) is None
        # and model_fields_set contains the field
        if self.secondary_organization is None and "secondary_organization" in self.model_fields_set:
            _dict['secondaryOrganization'] = None

        # set to None if scheduled_completion_date (nullable) is None
        # and model_fields_set contains the field
        if self.scheduled_completion_date is None and "scheduled_completion_date" in self.model_fields_set:
            _dict['scheduledCompletionDate'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        """Create an instance of MockObject from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pocOrganization": obj.get("pocOrganization"),
            "resources": obj.get("resources"),
            "owningOrganization": obj.get("owningOrganization"),
            "secondaryOrganization": obj.get("secondaryOrganization"),
            "pocFirstName": obj.get("pocFirstName"),
            "pocLastName": obj.get("pocLastName"),
            "pocEmail": obj.get("pocEmail"),
            "pocPhoneNumber": obj.get("pocPhoneNumber"),
            "severity": obj.get("severity"),
            "scheduledCompletionDate": obj.get("scheduledCompletionDate"),
            "completionDate": obj.get("completionDate"),
            "comments": obj.get("comments"),
            "isActive": obj.get("isActive")
        })
        return _obj


