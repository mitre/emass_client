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


from typing import Optional
from pydantic import BaseModel, StrictInt, StrictStr
from pydantic import Field
from typing_extensions import Annotated
from typing import Dict, Any
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class CacGet(BaseModel):
    """
    CacGet
    """
    system_id: Optional[StrictInt] = Field(default=None, description="[Required] Unique eMASS system identifier.", alias="systemId")
    control_acronym: Optional[StrictStr] = Field(default=None, description="[Required] System acronym name.", alias="controlAcronym")
    compliance_status: Optional[StrictStr] = Field(default=None, description="[Read-only] Compliance status of the control.", alias="complianceStatus")
    current_stage_name: Optional[StrictStr] = Field(default=None, description="[Read-Only] Role in current stage.", alias="currentStageName")
    current_stage: Optional[Annotated[int, Field(le=50, strict=True, ge=1)]] = Field(default=None, description="[Read-Only] Current step in the Control Approval Chain.", alias="currentStage")
    total_stages: Optional[Annotated[int, Field(le=50, strict=True, ge=1)]] = Field(default=None, description="[Read-Only] Total number of steps in Control Approval Chain.", alias="totalStages")
    comments: Optional[StrictStr] = Field(default=None, description="[Conditional] Control Approval Chain comments - 2000 Characters.")
    __properties: ClassVar[List[str]] = ["systemId", "controlAcronym", "complianceStatus", "currentStageName", "currentStage", "totalStages", "comments"]

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
        """Create an instance of CacGet from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if compliance_status (nullable) is None
        # and model_fields_set contains the field
        if self.compliance_status is None and "compliance_status" in self.model_fields_set:
            _dict['complianceStatus'] = None

        # set to None if current_stage_name (nullable) is None
        # and model_fields_set contains the field
        if self.current_stage_name is None and "current_stage_name" in self.model_fields_set:
            _dict['currentStageName'] = None

        # set to None if current_stage (nullable) is None
        # and model_fields_set contains the field
        if self.current_stage is None and "current_stage" in self.model_fields_set:
            _dict['currentStage'] = None

        # set to None if total_stages (nullable) is None
        # and model_fields_set contains the field
        if self.total_stages is None and "total_stages" in self.model_fields_set:
            _dict['totalStages'] = None

        # set to None if comments (nullable) is None
        # and model_fields_set contains the field
        if self.comments is None and "comments" in self.model_fields_set:
            _dict['comments'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        """Create an instance of CacGet from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "systemId": obj.get("systemId"),
            "controlAcronym": obj.get("controlAcronym"),
            "complianceStatus": obj.get("complianceStatus"),
            "currentStageName": obj.get("currentStageName"),
            "currentStage": obj.get("currentStage"),
            "totalStages": obj.get("totalStages"),
            "comments": obj.get("comments")
        })
        return _obj


