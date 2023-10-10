# coding: utf-8

## eMASS API v3.12 Specification

The emass_client_api is a Python client that implements the [Enterprise Mission Assurance Support Service (eMASS)](https://disa.mil/~/media/Files/DISA/Fact-Sheets/eMASS.pdf)
Representational State Transfer (REST) Application Programming Interface (API) specifications.


This Python package was generated from the eMASS API specification:

- API version: v3.12
- Package version: 3.11.1
- Build date: 2023-10-10T02:05:20.537795Z[Etc/UTC]

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
from typing import Dict, Any
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class DashboardMockResponsePagination(BaseModel):
    """
    DashboardMockResponsePagination
    """
    total_count: Optional[StrictInt] = Field(default=None, alias="totalCount")
    total_pages: Optional[StrictInt] = Field(default=None, alias="totalPages")
    page_index: Optional[StrictInt] = Field(default=None, alias="pageIndex")
    page_size: Optional[StrictInt] = Field(default=None, alias="pageSize")
    prev_page_url: Optional[StrictStr] = Field(default=None, alias="prevPageUrl")
    next_page_url: Optional[StrictStr] = Field(default=None, alias="nextPageUrl")
    __properties: ClassVar[List[str]] = ["totalCount", "totalPages", "pageIndex", "pageSize", "prevPageUrl", "nextPageUrl"]

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
        """Create an instance of DashboardMockResponsePagination from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        """Create an instance of DashboardMockResponsePagination from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "totalCount": obj.get("totalCount"),
            "totalPages": obj.get("totalPages"),
            "pageIndex": obj.get("pageIndex"),
            "pageSize": obj.get("pageSize"),
            "prevPageUrl": obj.get("prevPageUrl"),
            "nextPageUrl": obj.get("nextPageUrl")
        })
        return _obj


