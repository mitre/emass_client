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
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist
from emass_client.models.instances_transitions import InstancesTransitions

class WorkflowInstancesGet(BaseModel):
    """
    WorkflowInstancesGet
    """
    workflow_uid: Optional[StrictStr] = Field(None, alias="workflowUid", description="[Read-Only] Unique workflow definition identifier.")
    system_id: Optional[StrictInt] = Field(None, alias="systemId", description="[Read-only] Unique system record identifier.")
    system_name: Optional[StrictStr] = Field(None, alias="systemName", description="[Read-Only] The system name.")
    workflow_instance_id: Optional[StrictInt] = Field(None, alias="workflowInstanceId", description="[Read-Only] Unique workflow instance identifier.")
    package_name: Optional[StrictStr] = Field(None, alias="packageName", description="[Read-Only] The package name.")
    created_date: Optional[StrictInt] = Field(None, alias="createdDate", description="[Read-Only] Date the workflow instance or the workflow transition was created.")
    last_edited_date: Optional[StrictInt] = Field(None, alias="lastEditedDate", description="[Read-Only] Date the workflow was last acted on.")
    last_edited_by: Optional[StrictStr] = Field(None, alias="lastEditedBy", description="[Read-Only] User that last acted on the workflow.")
    workflow: Optional[StrictStr] = Field(None, description="[Read-Only] The workflow type.")
    version: Optional[StrictStr] = Field(None, description="[Read-Only] Version of the workflow definition.")
    current_stage: Optional[StrictStr] = Field(None, alias="currentStage", description="[Read-Only] Name of the current stage.")
    transitions: Optional[conlist(InstancesTransitions)] = None
    __properties = ["workflowUid", "systemId", "systemName", "workflowInstanceId", "packageName", "createdDate", "lastEditedDate", "lastEditedBy", "workflow", "version", "currentStage", "transitions"]

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
    def from_json(cls, json_str: str) -> WorkflowInstancesGet:
        """Create an instance of WorkflowInstancesGet from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in transitions (list)
        _items = []
        if self.transitions:
            for _item in self.transitions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['transitions'] = _items
        # set to None if workflow_uid (nullable) is None
        # and __fields_set__ contains the field
        if self.workflow_uid is None and "workflow_uid" in self.__fields_set__:
            _dict['workflowUid'] = None

        # set to None if system_id (nullable) is None
        # and __fields_set__ contains the field
        if self.system_id is None and "system_id" in self.__fields_set__:
            _dict['systemId'] = None

        # set to None if system_name (nullable) is None
        # and __fields_set__ contains the field
        if self.system_name is None and "system_name" in self.__fields_set__:
            _dict['systemName'] = None

        # set to None if workflow_instance_id (nullable) is None
        # and __fields_set__ contains the field
        if self.workflow_instance_id is None and "workflow_instance_id" in self.__fields_set__:
            _dict['workflowInstanceId'] = None

        # set to None if package_name (nullable) is None
        # and __fields_set__ contains the field
        if self.package_name is None and "package_name" in self.__fields_set__:
            _dict['packageName'] = None

        # set to None if created_date (nullable) is None
        # and __fields_set__ contains the field
        if self.created_date is None and "created_date" in self.__fields_set__:
            _dict['createdDate'] = None

        # set to None if last_edited_date (nullable) is None
        # and __fields_set__ contains the field
        if self.last_edited_date is None and "last_edited_date" in self.__fields_set__:
            _dict['lastEditedDate'] = None

        # set to None if last_edited_by (nullable) is None
        # and __fields_set__ contains the field
        if self.last_edited_by is None and "last_edited_by" in self.__fields_set__:
            _dict['lastEditedBy'] = None

        # set to None if workflow (nullable) is None
        # and __fields_set__ contains the field
        if self.workflow is None and "workflow" in self.__fields_set__:
            _dict['workflow'] = None

        # set to None if version (nullable) is None
        # and __fields_set__ contains the field
        if self.version is None and "version" in self.__fields_set__:
            _dict['version'] = None

        # set to None if current_stage (nullable) is None
        # and __fields_set__ contains the field
        if self.current_stage is None and "current_stage" in self.__fields_set__:
            _dict['currentStage'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> WorkflowInstancesGet:
        """Create an instance of WorkflowInstancesGet from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return WorkflowInstancesGet.parse_obj(obj)

        _obj = WorkflowInstancesGet.parse_obj({
            "workflow_uid": obj.get("workflowUid"),
            "system_id": obj.get("systemId"),
            "system_name": obj.get("systemName"),
            "workflow_instance_id": obj.get("workflowInstanceId"),
            "package_name": obj.get("packageName"),
            "created_date": obj.get("createdDate"),
            "last_edited_date": obj.get("lastEditedDate"),
            "last_edited_by": obj.get("lastEditedBy"),
            "workflow": obj.get("workflow"),
            "version": obj.get("version"),
            "current_stage": obj.get("currentStage"),
            "transitions": [InstancesTransitions.from_dict(_item) for _item in obj.get("transitions")] if obj.get("transitions") is not None else None
        })
        return _obj

