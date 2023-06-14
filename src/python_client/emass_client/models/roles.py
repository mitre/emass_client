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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist
from emass_client.models.users import Users

class Roles(BaseModel):
    """
    Roles
    """
    role_category: Optional[StrictStr] = Field(None, alias="roleCategory", description="[Required] System role categories")
    role: Optional[StrictStr] = Field(None, description="[Required] System role description")
    users: Optional[conlist(Users)] = None
    __properties = ["roleCategory", "role", "users"]

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
    def from_json(cls, json_str: str) -> Roles:
        """Create an instance of Roles from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in users (list)
        _items = []
        if self.users:
            for _item in self.users:
                if _item:
                    _items.append(_item.to_dict())
            _dict['users'] = _items
        # set to None if users (nullable) is None
        # and __fields_set__ contains the field
        if self.users is None and "users" in self.__fields_set__:
            _dict['users'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Roles:
        """Create an instance of Roles from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Roles.parse_obj(obj)

        _obj = Roles.parse_obj({
            "role_category": obj.get("roleCategory"),
            "role": obj.get("role"),
            "users": [Users.from_dict(_item) for _item in obj.get("users")] if obj.get("users") is not None else None
        })
        return _obj

