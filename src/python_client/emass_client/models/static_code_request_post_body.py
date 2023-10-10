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


from typing import List, Optional
from pydantic import BaseModel
from pydantic import Field
from emass_client.models.static_code_application_post import StaticCodeApplicationPost
from emass_client.models.static_code_request_post_body_application import StaticCodeRequestPostBodyApplication
from typing import Dict, Any
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class StaticCodeRequestPostBody(BaseModel):
    """
    StaticCodeRequestPostBody
    """
    application: Optional[StaticCodeRequestPostBodyApplication] = None
    application_findings: Optional[List[StaticCodeApplicationPost]] = Field(default=None, alias="applicationFindings")
    __properties: ClassVar[List[str]] = ["application", "applicationFindings"]

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
        """Create an instance of StaticCodeRequestPostBody from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of application
        if self.application:
            _dict['application'] = self.application.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in application_findings (list)
        _items = []
        if self.application_findings:
            for _item in self.application_findings:
                if _item:
                    _items.append(_item.to_dict())
            _dict['applicationFindings'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        """Create an instance of StaticCodeRequestPostBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "application": StaticCodeRequestPostBodyApplication.from_dict(obj.get("application")) if obj.get("application") is not None else None,
            "applicationFindings": [StaticCodeApplicationPost.from_dict(_item) for _item in obj.get("applicationFindings")] if obj.get("applicationFindings") is not None else None
        })
        return _obj


