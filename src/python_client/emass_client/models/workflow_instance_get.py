# coding: utf-8

### eMASS API v3.12 Specification
#The emass_client_api is a Python client that implements the [Enterprise Mission Assurance Support Service (eMASS)](https://disa.mil/~/media/Files/DISA/Fact-Sheets/eMASS.pdf)Representational State Transfer (REST) Application Programming Interface (API) specifications.


#This Python package was generated from the eMASS API specification:
#- API version: v3.12- Package version: 3.12.0
#- Build date: 2023-10-10T14:36:02.975730Z[Etc/UTC]
### Requirements.
#Python 
### Installation & Usage### pip install

#If the python package is hosted on a repository, you can install directly using:
#```shpip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
#```(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

#Then import the package:```python
#import emass_client#```
#### Setuptools
#Install via [Setuptools](http://pypi.python.org/pypi/setuptools).
#```shpython setup.py install --user
#```(or `sudo python setup.py install` to install the package for all users)

#Then import the package:```python
#import emass_client#```
#### Tests
#Execute `pytest` to run the tests.
from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, StrictInt, StrictStr
from pydantic import Field
from emass_client.models.instances_transitions import InstancesTransitions
from typing import Dict, Any
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class WorkflowInstanceGet(BaseModel):
    """
    WorkflowInstanceGet
    """
    workflow_uid: Optional[StrictStr] = Field(default=None, description="[Read-Only] Unique workflow definition identifier.", alias="workflowUid")
    system_name: Optional[StrictStr] = Field(default=None, description="[Read-Only] The system name.", alias="systemName")
    workflow_instance_id: Optional[StrictInt] = Field(default=None, description="[Read-Only] Unique workflow instance identifier.", alias="workflowInstanceId")
    package_name: Optional[StrictStr] = Field(default=None, description="[Read-Only] The package name.", alias="packageName")
    created_date: Optional[StrictInt] = Field(default=None, description="[Read-Only] Date the workflow instance or the workflow transition was created.", alias="createdDate")
    last_edited_date: Optional[StrictInt] = Field(default=None, description="[Read-Only] Date the workflow was last acted on.", alias="lastEditedDate")
    last_edited_by: Optional[StrictStr] = Field(default=None, description="[Read-Only] User that last acted on the workflow.", alias="lastEditedBy")
    workflow: Optional[StrictStr] = Field(default=None, description="[Read-Only] The workflow type.")
    version: Optional[StrictStr] = Field(default=None, description="[Read-Only] Version of the workflow definition.")
    current_stage: Optional[StrictStr] = Field(default=None, description="[Read-Only] Name of the current stage.", alias="currentStage")
    transitions: Optional[List[InstancesTransitions]] = None
    __properties: ClassVar[List[str]] = ["workflowUid", "systemName", "workflowInstanceId", "packageName", "createdDate", "lastEditedDate", "lastEditedBy", "workflow", "version", "currentStage", "transitions"]

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
        """Create an instance of WorkflowInstanceGet from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True,
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
        # and model_fields_set contains the field
        if self.workflow_uid is None and "workflow_uid" in self.model_fields_set:
            _dict['workflowUid'] = None

        # set to None if system_name (nullable) is None
        # and model_fields_set contains the field
        if self.system_name is None and "system_name" in self.model_fields_set:
            _dict['systemName'] = None

        # set to None if workflow_instance_id (nullable) is None
        # and model_fields_set contains the field
        if self.workflow_instance_id is None and "workflow_instance_id" in self.model_fields_set:
            _dict['workflowInstanceId'] = None

        # set to None if package_name (nullable) is None
        # and model_fields_set contains the field
        if self.package_name is None and "package_name" in self.model_fields_set:
            _dict['packageName'] = None

        # set to None if created_date (nullable) is None
        # and model_fields_set contains the field
        if self.created_date is None and "created_date" in self.model_fields_set:
            _dict['createdDate'] = None

        # set to None if last_edited_date (nullable) is None
        # and model_fields_set contains the field
        if self.last_edited_date is None and "last_edited_date" in self.model_fields_set:
            _dict['lastEditedDate'] = None

        # set to None if last_edited_by (nullable) is None
        # and model_fields_set contains the field
        if self.last_edited_by is None and "last_edited_by" in self.model_fields_set:
            _dict['lastEditedBy'] = None

        # set to None if workflow (nullable) is None
        # and model_fields_set contains the field
        if self.workflow is None and "workflow" in self.model_fields_set:
            _dict['workflow'] = None

        # set to None if version (nullable) is None
        # and model_fields_set contains the field
        if self.version is None and "version" in self.model_fields_set:
            _dict['version'] = None

        # set to None if current_stage (nullable) is None
        # and model_fields_set contains the field
        if self.current_stage is None and "current_stage" in self.model_fields_set:
            _dict['currentStage'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        """Create an instance of WorkflowInstanceGet from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "workflowUid": obj.get("workflowUid"),
            "systemName": obj.get("systemName"),
            "workflowInstanceId": obj.get("workflowInstanceId"),
            "packageName": obj.get("packageName"),
            "createdDate": obj.get("createdDate"),
            "lastEditedDate": obj.get("lastEditedDate"),
            "lastEditedBy": obj.get("lastEditedBy"),
            "workflow": obj.get("workflow"),
            "version": obj.get("version"),
            "currentStage": obj.get("currentStage"),
            "transitions": [InstancesTransitions.from_dict(_item) for _item in obj.get("transitions")] if obj.get("transitions") is not None else None
        })
        return _obj


