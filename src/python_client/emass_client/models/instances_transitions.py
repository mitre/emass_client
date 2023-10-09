# coding: utf-8

## eMASS API v3.12 Specification

The emass_client_api is a Python client that implements the [Enterprise Mission Assurance Support Service (eMASS)](https://disa.mil/~/media/Files/DISA/Fact-Sheets/eMASS.pdf)
Representational State Transfer (REST) Application Programming Interface (API) specifications.


This Python package was generated from the eMASS API specification:

- API version: v3.12
- Package version: 3.11.0
- Build date: 2023-10-09T21:35:37.766947Z[Etc/UTC]

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
from pydantic import BaseModel, StrictInt, StrictStr
from pydantic import Field
from typing import Dict, Any
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class InstancesTransitions(BaseModel):
    """
    InstancesTransitions
    """
    comments: Optional[StrictStr] = Field(default=None, description="[Read-Only] Comments entered by the user when performing the transition.")
    created_by: Optional[StrictStr] = Field(default=None, description="[Read-Only] User that performed the workflow transition.", alias="createdBy")
    created_date: Optional[StrictInt] = Field(default=None, description="[Read-Only] Date the workflow instance or the workflow transition was created.", alias="createdDate")
    description: Optional[StrictStr] = Field(default=None, description="[Read-Only] Description of the stage transition. This matches the action dropdown that appears for PAC users.")
    end_stage: Optional[StrictStr] = Field(default=None, description="[Read-Only] The landing stage that is active after performing a transition.", alias="endStage")
    start_stage: Optional[StrictStr] = Field(default=None, description="[Read-Only] The beginning stage that is active before performing a transition.", alias="startStage")
    __properties: ClassVar[List[str]] = ["comments", "createdBy", "createdDate", "description", "endStage", "startStage"]

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
        """Create an instance of InstancesTransitions from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if comments (nullable) is None
        # and model_fields_set contains the field
        if self.comments is None and "comments" in self.model_fields_set:
            _dict['comments'] = None

        # set to None if created_by (nullable) is None
        # and model_fields_set contains the field
        if self.created_by is None and "created_by" in self.model_fields_set:
            _dict['createdBy'] = None

        # set to None if created_date (nullable) is None
        # and model_fields_set contains the field
        if self.created_date is None and "created_date" in self.model_fields_set:
            _dict['createdDate'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if end_stage (nullable) is None
        # and model_fields_set contains the field
        if self.end_stage is None and "end_stage" in self.model_fields_set:
            _dict['endStage'] = None

        # set to None if start_stage (nullable) is None
        # and model_fields_set contains the field
        if self.start_stage is None and "start_stage" in self.model_fields_set:
            _dict['startStage'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        """Create an instance of InstancesTransitions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "comments": obj.get("comments"),
            "createdBy": obj.get("createdBy"),
            "createdDate": obj.get("createdDate"),
            "description": obj.get("description"),
            "endStage": obj.get("endStage"),
            "startStage": obj.get("startStage")
        })
        return _obj


