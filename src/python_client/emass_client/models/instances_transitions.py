# coding: utf-8

## eMASS API v3.10 Specification

The emass_client_api is a Python client that implements the [Enterprise Mission Assurance Support Service (eMASS)](https://disa.mil/~/media/Files/DISA/Fact-Sheets/eMASS.pdf)
Representational State Transfer (REST) Application Programming Interface (API) specifications.


This Python package was generated from the eMASS API specification:

- API version: v3.10
- Package version: 3.10.1
- Build date: 2023-06-13T18:24:16.147147Z[Etc/UTC]

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
from pydantic import BaseModel, Field, StrictInt, StrictStr

class InstancesTransitions(BaseModel):
    """
    InstancesTransitions
    """
    comments: Optional[StrictStr] = Field(None, description="[Read-Only] Comments entered by the user when performing the transition.")
    created_by: Optional[StrictStr] = Field(None, alias="createdBy", description="[Read-Only] User that performed the workflow transition.")
    created_date: Optional[StrictInt] = Field(None, alias="createdDate", description="[Read-Only] Date the workflow instance or the workflow transition was created.")
    description: Optional[StrictStr] = Field(None, description="[Read-Only] Description of the stage transition. This matches the action dropdown that appears for PAC users.")
    end_stage: Optional[StrictStr] = Field(None, alias="endStage", description="[Read-Only] The landing stage that is active after performing a transition.")
    start_stage: Optional[StrictStr] = Field(None, alias="startStage", description="[Read-Only] The beginning stage that is active before performing a transition.")
    __properties = ["comments", "createdBy", "createdDate", "description", "endStage", "startStage"]

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
    def from_json(cls, json_str: str) -> InstancesTransitions:
        """Create an instance of InstancesTransitions from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if comments (nullable) is None
        # and __fields_set__ contains the field
        if self.comments is None and "comments" in self.__fields_set__:
            _dict['comments'] = None

        # set to None if created_by (nullable) is None
        # and __fields_set__ contains the field
        if self.created_by is None and "created_by" in self.__fields_set__:
            _dict['createdBy'] = None

        # set to None if created_date (nullable) is None
        # and __fields_set__ contains the field
        if self.created_date is None and "created_date" in self.__fields_set__:
            _dict['createdDate'] = None

        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        # set to None if end_stage (nullable) is None
        # and __fields_set__ contains the field
        if self.end_stage is None and "end_stage" in self.__fields_set__:
            _dict['endStage'] = None

        # set to None if start_stage (nullable) is None
        # and __fields_set__ contains the field
        if self.start_stage is None and "start_stage" in self.__fields_set__:
            _dict['startStage'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> InstancesTransitions:
        """Create an instance of InstancesTransitions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return InstancesTransitions.parse_obj(obj)

        _obj = InstancesTransitions.parse_obj({
            "comments": obj.get("comments"),
            "created_by": obj.get("createdBy"),
            "created_date": obj.get("createdDate"),
            "description": obj.get("description"),
            "end_stage": obj.get("endStage"),
            "start_stage": obj.get("startStage")
        })
        return _obj

