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


from typing import Optional
from pydantic import BaseModel, Field, StrictStr, conint

class Response405Meta(BaseModel):
    """
    Response405Meta
    """
    code: Optional[conint(strict=True, le=405, ge=405)] = 405
    error_message: Optional[StrictStr] = Field('Request was made with a verb (GET, POST, etc.) that is not permitted for the endpoint', alias="errorMessage")
    __properties = ["code", "errorMessage"]

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
    def from_json(cls, json_str: str) -> Response405Meta:
        """Create an instance of Response405Meta from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Response405Meta:
        """Create an instance of Response405Meta from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Response405Meta.parse_obj(obj)

        _obj = Response405Meta.parse_obj({
            "code": obj.get("code") if obj.get("code") is not None else 405,
            "error_message": obj.get("errorMessage") if obj.get("errorMessage") is not None else 'Request was made with a verb (GET, POST, etc.) that is not permitted for the endpoint'
        })
        return _obj
