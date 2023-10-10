# coding: utf-8

## eMASS API v3.12 Specification

The emass_client_api is a Python client that implements the [Enterprise Mission Assurance Support Service (eMASS)](https://disa.mil/~/media/Files/DISA/Fact-Sheets/eMASS.pdf)
Representational State Transfer (REST) Application Programming Interface (API) specifications.


This Python package was generated from the eMASS API specification:

- API version: v3.12
- Package version: 3.11.1
- Build date: 2023-10-10T00:32:11.514559Z[Etc/UTC]

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
from pydantic import BaseModel, StrictBool, StrictStr
from pydantic import Field
from emass_client.models.stage import Stage
from typing import Dict, Any
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class WorkflowDefinitionGet(BaseModel):
    """
    WorkflowDefinitionGet
    """
    workflow_uid: Optional[StrictStr] = Field(default=None, description="[Read-Only] Unique workflow definition identifier.", alias="workflowUid")
    workflow: Optional[StrictStr] = Field(default=None, description="[Read-Only] The workflow type.")
    version: Optional[StrictStr] = Field(default=None, description="[Read-Only] Version of the workflow definition.")
    description: Optional[StrictStr] = Field(default=None, description="[Read-Only] Description of the workflow or the stage transition.")
    is_active: Optional[StrictBool] = Field(default=None, description="[Read-Only] Returns true if the workflow is available to the site.", alias="isActive")
    stages: Optional[List[Stage]] = None
    __properties: ClassVar[List[str]] = ["workflowUid", "workflow", "version", "description", "isActive", "stages"]

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
        """Create an instance of WorkflowDefinitionGet from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in stages (list)
        _items = []
        if self.stages:
            for _item in self.stages:
                if _item:
                    _items.append(_item.to_dict())
            _dict['stages'] = _items
        # set to None if workflow_uid (nullable) is None
        # and model_fields_set contains the field
        if self.workflow_uid is None and "workflow_uid" in self.model_fields_set:
            _dict['workflowUid'] = None

        # set to None if workflow (nullable) is None
        # and model_fields_set contains the field
        if self.workflow is None and "workflow" in self.model_fields_set:
            _dict['workflow'] = None

        # set to None if version (nullable) is None
        # and model_fields_set contains the field
        if self.version is None and "version" in self.model_fields_set:
            _dict['version'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if is_active (nullable) is None
        # and model_fields_set contains the field
        if self.is_active is None and "is_active" in self.model_fields_set:
            _dict['isActive'] = None

        # set to None if stages (nullable) is None
        # and model_fields_set contains the field
        if self.stages is None and "stages" in self.model_fields_set:
            _dict['stages'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        """Create an instance of WorkflowDefinitionGet from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "workflowUid": obj.get("workflowUid"),
            "workflow": obj.get("workflow"),
            "version": obj.get("version"),
            "description": obj.get("description"),
            "isActive": obj.get("isActive"),
            "stages": [Stage.from_dict(_item) for _item in obj.get("stages")] if obj.get("stages") is not None else None
        })
        return _obj


