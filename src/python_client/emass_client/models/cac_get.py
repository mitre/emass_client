# coding: utf-8

## eMASS API v3.9 Specification

The emass_client_api is a Python client that implements the [Enterprise Mission Assurance Support Service (eMASS)](https://disa.mil/~/media/Files/DISA/Fact-Sheets/eMASS.pdf)
Representational State Transfer (REST) Application Programming Interface (API) specifications.


This Python package was generated from the eMASS API specification:

- API version: v3.9
- Package version: 3.9.1
- Build date: 2023-05-23T01:07:18.461999Z[Etc/UTC]

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
from pydantic import BaseModel, Field, StrictInt, StrictStr, conint

class CacGet(BaseModel):
    """
    CacGet
    """
    system_id: Optional[StrictInt] = Field(None, alias="systemId", description="[Required] Unique eMASS system identifier.")
    control_acronym: Optional[StrictStr] = Field(None, alias="controlAcronym", description="[Required] System acronym name.")
    compliance_status: Optional[StrictStr] = Field(None, alias="complianceStatus", description="[Read-only] Compliance status of the control.")
    current_stage_name: Optional[StrictStr] = Field(None, alias="currentStageName", description="[Read-Only] Role in current stage.")
    current_stage: Optional[conint(strict=True, le=50, ge=1)] = Field(None, alias="currentStage", description="[Read-Only] Current step in the Control Approval Chain.")
    total_stages: Optional[conint(strict=True, le=50, ge=1)] = Field(None, alias="totalStages", description="[Read-Only] Total number of steps in Control Approval Chain.")
    comments: Optional[StrictStr] = Field(None, description="[Conditional] Control Approval Chain comments - 2000 Characters.")
    __properties = ["systemId", "controlAcronym", "complianceStatus", "currentStageName", "currentStage", "totalStages", "comments"]

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
    def from_json(cls, json_str: str) -> CacGet:
        """Create an instance of CacGet from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if compliance_status (nullable) is None
        # and __fields_set__ contains the field
        if self.compliance_status is None and "compliance_status" in self.__fields_set__:
            _dict['complianceStatus'] = None

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

        # set to None if comments (nullable) is None
        # and __fields_set__ contains the field
        if self.comments is None and "comments" in self.__fields_set__:
            _dict['comments'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CacGet:
        """Create an instance of CacGet from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CacGet.parse_obj(obj)

        _obj = CacGet.parse_obj({
            "system_id": obj.get("systemId"),
            "control_acronym": obj.get("controlAcronym"),
            "compliance_status": obj.get("complianceStatus"),
            "current_stage_name": obj.get("currentStageName"),
            "current_stage": obj.get("currentStage"),
            "total_stages": obj.get("totalStages"),
            "comments": obj.get("comments")
        })
        return _obj

