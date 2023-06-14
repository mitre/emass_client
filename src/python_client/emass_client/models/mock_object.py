# coding: utf-8

## eMASS API v3.10 Specification

The emass_client_api is a Python client that implements the [Enterprise Mission Assurance Support Service (eMASS)](https://disa.mil/~/media/Files/DISA/Fact-Sheets/eMASS.pdf)
Representational State Transfer (REST) Application Programming Interface (API) specifications.


This Python package was generated from the eMASS API specification:

- API version: v3.10
- Package version: 3.10.1
- Build date: 2023-06-14T17:42:15.829833Z[Etc/UTC]

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
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr

class MockObject(BaseModel):
    """
    MockObject
    """
    poc_organization: Optional[StrictStr] = Field(None, alias="pocOrganization", description="[Required] Organization/Office represented. 100 Characters.")
    resources: Optional[StrictStr] = Field(None, description="[Required] List of resources used. 250 Characters.")
    owning_organization: Optional[StrictStr] = Field(None, alias="owningOrganization", description="[Read-Only] Owning organization of the system record. Values match the eMASS instance Organizational Hierarchy.")
    secondary_organization: Optional[StrictStr] = Field(None, alias="secondaryOrganization", description="[Read-only] Secondary organization that owns the system record (i.e. Sub-Organization-level.")
    poc_first_name: Optional[StrictStr] = Field(None, alias="pocFirstName", description="[Conditional] First name of POC. 100 Characters.")
    poc_last_name: Optional[StrictStr] = Field(None, alias="pocLastName", description="[Conditional] Last name of POC. 100 Characters.")
    poc_email: Optional[StrictStr] = Field(None, alias="pocEmail", description="[Conditional] Email address of POC. 100 Characters.")
    poc_phone_number: Optional[StrictStr] = Field(None, alias="pocPhoneNumber", description="[Conditional] Phone number of POC (area code) ***-**** format. 100 Characters.")
    severity: Optional[StrictStr] = Field(None, description="[Conditional] Required for approved items. Values include the following options: (Very Low, Low, Moderate,High,Very High)")
    scheduled_completion_date: Optional[StrictInt] = Field(None, alias="scheduledCompletionDate", description="[Conditional] Required for ongoing and completed POA&M items. Unix time format.")
    completion_date: Optional[StrictInt] = Field(None, alias="completionDate", description="[Conditional] Field is required for completed POA&M items. Unix time format.")
    comments: Optional[StrictStr] = Field(None, description="[Conditional] Field is required for completed and risk accepted POA&M items. 2000 Characters")
    is_active: Optional[StrictBool] = Field(None, alias="isActive", description="[Conditional] Optionally used in PUT to delete milestones when updating a POA&M.")
    __properties = ["pocOrganization", "resources", "owningOrganization", "secondaryOrganization", "pocFirstName", "pocLastName", "pocEmail", "pocPhoneNumber", "severity", "scheduledCompletionDate", "completionDate", "comments", "isActive"]

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
    def from_json(cls, json_str: str) -> MockObject:
        """Create an instance of MockObject from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if owning_organization (nullable) is None
        # and __fields_set__ contains the field
        if self.owning_organization is None and "owning_organization" in self.__fields_set__:
            _dict['owningOrganization'] = None

        # set to None if secondary_organization (nullable) is None
        # and __fields_set__ contains the field
        if self.secondary_organization is None and "secondary_organization" in self.__fields_set__:
            _dict['secondaryOrganization'] = None

        # set to None if scheduled_completion_date (nullable) is None
        # and __fields_set__ contains the field
        if self.scheduled_completion_date is None and "scheduled_completion_date" in self.__fields_set__:
            _dict['scheduledCompletionDate'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MockObject:
        """Create an instance of MockObject from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MockObject.parse_obj(obj)

        _obj = MockObject.parse_obj({
            "poc_organization": obj.get("pocOrganization"),
            "resources": obj.get("resources"),
            "owning_organization": obj.get("owningOrganization"),
            "secondary_organization": obj.get("secondaryOrganization"),
            "poc_first_name": obj.get("pocFirstName"),
            "poc_last_name": obj.get("pocLastName"),
            "poc_email": obj.get("pocEmail"),
            "poc_phone_number": obj.get("pocPhoneNumber"),
            "severity": obj.get("severity"),
            "scheduled_completion_date": obj.get("scheduledCompletionDate"),
            "completion_date": obj.get("completionDate"),
            "comments": obj.get("comments"),
            "is_active": obj.get("isActive")
        })
        return _obj

