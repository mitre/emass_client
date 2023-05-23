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


from typing import Any, List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conlist

class ContainersResourcesPost(BaseModel):
    """
    ContainersResourcesPost
    """
    container_id: Optional[StrictStr] = Field(None, alias="containerId", description="[Required] Unique identifier of the container")
    success: Optional[StrictBool] = None
    system_id: Optional[StrictInt] = Field(None, alias="systemId")
    errors: Optional[conlist(Any, max_items=5)] = None
    __properties = ["containerId", "success", "systemId", "errors"]

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
    def from_json(cls, json_str: str) -> ContainersResourcesPost:
        """Create an instance of ContainersResourcesPost from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if errors (nullable) is None
        # and __fields_set__ contains the field
        if self.errors is None and "errors" in self.__fields_set__:
            _dict['errors'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ContainersResourcesPost:
        """Create an instance of ContainersResourcesPost from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ContainersResourcesPost.parse_obj(obj)

        _obj = ContainersResourcesPost.parse_obj({
            "container_id": obj.get("containerId"),
            "success": obj.get("success"),
            "system_id": obj.get("systemId"),
            "errors": obj.get("errors")
        })
        return _obj

