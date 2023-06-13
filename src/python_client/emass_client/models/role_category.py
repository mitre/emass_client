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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist
from emass_client.models.roles import Roles

class RoleCategory(BaseModel):
    """
    RoleCategory
    """
    system_id: Optional[StrictInt] = Field(None, alias="systemId", description="[Read-only] Unique system record identifier.")
    system_name: Optional[StrictStr] = Field(None, alias="systemName", description="[Read-only] Name of the system record.")
    system_acronym: Optional[StrictStr] = Field(None, alias="systemAcronym", description="[Read-only] Acronym of the system record.")
    roles: Optional[conlist(Roles)] = None
    __properties = ["systemId", "systemName", "systemAcronym", "roles"]

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
    def from_json(cls, json_str: str) -> RoleCategory:
        """Create an instance of RoleCategory from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in roles (list)
        _items = []
        if self.roles:
            for _item in self.roles:
                if _item:
                    _items.append(_item.to_dict())
            _dict['roles'] = _items
        # set to None if system_name (nullable) is None
        # and __fields_set__ contains the field
        if self.system_name is None and "system_name" in self.__fields_set__:
            _dict['systemName'] = None

        # set to None if system_acronym (nullable) is None
        # and __fields_set__ contains the field
        if self.system_acronym is None and "system_acronym" in self.__fields_set__:
            _dict['systemAcronym'] = None

        # set to None if roles (nullable) is None
        # and __fields_set__ contains the field
        if self.roles is None and "roles" in self.__fields_set__:
            _dict['roles'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RoleCategory:
        """Create an instance of RoleCategory from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RoleCategory.parse_obj(obj)

        _obj = RoleCategory.parse_obj({
            "system_id": obj.get("systemId"),
            "system_name": obj.get("systemName"),
            "system_acronym": obj.get("systemAcronym"),
            "roles": [Roles.from_dict(_item) for _item in obj.get("roles")] if obj.get("roles") is not None else None
        })
        return _obj

