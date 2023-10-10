# coding: utf-8

## eMASS API v3.12 Specification

The emass_client_api is a Python client that implements the [Enterprise Mission Assurance Support Service (eMASS)](https://disa.mil/~/media/Files/DISA/Fact-Sheets/eMASS.pdf)
Representational State Transfer (REST) Application Programming Interface (API) specifications.


This Python package was generated from the eMASS API specification:

- API version: v3.12
- Package version: 3.12.0
- Build date: 2023-10-10T14:36:02.975730Z[Etc/UTC]

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
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr, field_validator
from pydantic import Field
from typing import Dict, Any
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class StaticCodeApplicationPost(BaseModel):
    """
    StaticCodeApplicationPost
    """
    raw_severity: Optional[StrictStr] = Field(default=None, description="[Optional] Scan vulnerability ratting", alias="rawSeverity")
    code_check_name: Optional[StrictStr] = Field(default=None, description="[Required] Name of the software vulnerability or weakness.", alias="codeCheckName")
    count: Optional[StrictInt] = Field(default=None, description="[Required] Number of instances observed for a specified finding.")
    scan_date: Optional[StrictInt] = Field(default=None, description="[Required] The date of the scan. Unix date format.", alias="scanDate")
    cwe_id: Optional[StrictStr] = Field(default=None, description="[Required] The Common Weakness Enumerator (CWE) identifier.", alias="cweId")
    clear_findings: Optional[StrictBool] = Field(default=None, description="[Optional] When used by itself, can clear out all application findings for a single application/version pairing.", alias="clearFindings")
    __properties: ClassVar[List[str]] = ["rawSeverity", "codeCheckName", "count", "scanDate", "cweId", "clearFindings"]

    @field_validator('raw_severity')
    def raw_severity_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Low', 'Medium', 'Moderate', 'High', 'Critical'):
            raise ValueError("must be one of enum values ('Low', 'Medium', 'Moderate', 'High', 'Critical')")
        return value

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
        """Create an instance of StaticCodeApplicationPost from a JSON string"""
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
        """Create an instance of StaticCodeApplicationPost from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "rawSeverity": obj.get("rawSeverity"),
            "codeCheckName": obj.get("codeCheckName"),
            "count": obj.get("count"),
            "scanDate": obj.get("scanDate"),
            "cweId": obj.get("cweId"),
            "clearFindings": obj.get("clearFindings")
        })
        return _obj


