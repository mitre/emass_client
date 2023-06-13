# coding: utf-8

## eMASS API v3.10 Specification

The emass_client_api is a Python client that implements the [Enterprise Mission Assurance Support Service (eMASS)](https://disa.mil/~/media/Files/DISA/Fact-Sheets/eMASS.pdf)
Representational State Transfer (REST) Application Programming Interface (API) specifications.


This Python package was generated from the eMASS API specification:

- API version: v3.10
- Package version: 3.10.0
- Build date: 2023-06-13T13:46:18.843637Z[Etc/UTC]

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
from pydantic import BaseModel, Field, StrictInt, StrictStr, validator

class PacGet(BaseModel):
    """
    PacGet
    """
    system_id: Optional[StrictInt] = Field(None, alias="systemId", description="[Required] Unique eMASS system identifier.")
    workflow: Optional[StrictStr] = Field(None, description="[Required] Values include the following:(Assess and Authorize, Assess Only, Security Plan Approval)")
    name: Optional[StrictStr] = Field(None, description="[Required] Package name. 100 Characters.")
    current_stage_name: Optional[StrictStr] = Field(None, alias="currentStageName", description="[Read-Only] Name of the current stage in the active workflow.")
    current_stage: Optional[StrictInt] = Field(None, alias="currentStage", description="[Read-Only] Number of the current stage in the active workflow.")
    total_stages: Optional[StrictInt] = Field(None, alias="totalStages", description="[Read-Only] Total number of stages in the active workflow.")
    days_at_current_stage: Optional[StrictInt] = Field(None, alias="daysAtCurrentStage", description="[Read-Only] Indicates the number of days at current workflow stage.")
    comments: Optional[StrictStr] = Field(None, description="[Required] Comments related to package approval chain. Character Limit = 4,000.")
    __properties = ["systemId", "workflow", "name", "currentStageName", "currentStage", "totalStages", "daysAtCurrentStage", "comments"]

    @validator('workflow')
    def workflow_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Assess and Authorize', 'Assess Only', 'Security Plan Approval'):
            raise ValueError("must be one of enum values ('Assess and Authorize', 'Assess Only', 'Security Plan Approval')")
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
    def from_json(cls, json_str: str) -> PacGet:
        """Create an instance of PacGet from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if current_stage_name (nullable) is None
        # and __fields_set__ contains the field
        if self.current_stage_name is None and "current_stage_name" in self.__fields_set__:
            _dict['currentStageName'] = None

        # set to None if current_stage (nullable) is None
        # and __fields_set__ contains the field
        if self.current_stage is None and "current_stage" in self.__fields_set__:
            _dict['currentStage'] = None

        # set to None if total_stages (nullable) is None
        # and __fields_set__ contains the field
        if self.total_stages is None and "total_stages" in self.__fields_set__:
            _dict['totalStages'] = None

        # set to None if days_at_current_stage (nullable) is None
        # and __fields_set__ contains the field
        if self.days_at_current_stage is None and "days_at_current_stage" in self.__fields_set__:
            _dict['daysAtCurrentStage'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PacGet:
        """Create an instance of PacGet from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PacGet.parse_obj(obj)

        _obj = PacGet.parse_obj({
            "system_id": obj.get("systemId"),
            "workflow": obj.get("workflow"),
            "name": obj.get("name"),
            "current_stage_name": obj.get("currentStageName"),
            "current_stage": obj.get("currentStage"),
            "total_stages": obj.get("totalStages"),
            "days_at_current_stage": obj.get("daysAtCurrentStage"),
            "comments": obj.get("comments")
        })
        return _obj

