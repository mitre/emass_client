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

class Ssps(BaseModel):
    """
    Ssps
    """
    ssp_name: Optional[StrictStr] = Field(None, alias="sspName", description="[Read-Only] Name of the System Security Plan.")
    ssp_version: Optional[StrictStr] = Field(None, alias="sspVersion", description="[Read-Only] Version of the System Security Plan.")
    ssp_date: Optional[StrictInt] = Field(None, alias="sspDate", description="[Read-Only] Date of the System Security Plan. Unix date format.")
    __properties = ["sspName", "sspVersion", "sspDate"]

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
    def from_json(cls, json_str: str) -> Ssps:
        """Create an instance of Ssps from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if ssp_name (nullable) is None
        # and __fields_set__ contains the field
        if self.ssp_name is None and "ssp_name" in self.__fields_set__:
            _dict['sspName'] = None

        # set to None if ssp_version (nullable) is None
        # and __fields_set__ contains the field
        if self.ssp_version is None and "ssp_version" in self.__fields_set__:
            _dict['sspVersion'] = None

        # set to None if ssp_date (nullable) is None
        # and __fields_set__ contains the field
        if self.ssp_date is None and "ssp_date" in self.__fields_set__:
            _dict['sspDate'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Ssps:
        """Create an instance of Ssps from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Ssps.parse_obj(obj)

        _obj = Ssps.parse_obj({
            "ssp_name": obj.get("sspName"),
            "ssp_version": obj.get("sspVersion"),
            "ssp_date": obj.get("sspDate")
        })
        return _obj

