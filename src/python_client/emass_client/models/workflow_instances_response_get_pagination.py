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
from pydantic import BaseModel, Field, StrictInt, StrictStr

class WorkflowInstancesResponseGetPagination(BaseModel):
    """
    WorkflowInstancesResponseGetPagination
    """
    total_count: Optional[StrictInt] = Field(None, alias="totalCount")
    total_pages: Optional[StrictInt] = Field(None, alias="totalPages")
    prev_page_url: Optional[StrictStr] = Field(None, alias="prevPageUrl")
    next_page_url: Optional[StrictStr] = Field(None, alias="nextPageUrl")
    __properties = ["totalCount", "totalPages", "prevPageUrl", "nextPageUrl"]

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
    def from_json(cls, json_str: str) -> WorkflowInstancesResponseGetPagination:
        """Create an instance of WorkflowInstancesResponseGetPagination from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> WorkflowInstancesResponseGetPagination:
        """Create an instance of WorkflowInstancesResponseGetPagination from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return WorkflowInstancesResponseGetPagination.parse_obj(obj)

        _obj = WorkflowInstancesResponseGetPagination.parse_obj({
            "total_count": obj.get("totalCount"),
            "total_pages": obj.get("totalPages"),
            "prev_page_url": obj.get("prevPageUrl"),
            "next_page_url": obj.get("nextPageUrl")
        })
        return _obj
