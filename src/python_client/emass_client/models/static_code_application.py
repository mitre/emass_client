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
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, validator

class StaticCodeApplication(BaseModel):
    """
    StaticCodeApplication
    """
    raw_severity: Optional[StrictStr] = Field(None, alias="rawSeverity", description="[Optional] Scan vulnerability ratting")
    code_check_name: Optional[StrictStr] = Field(None, alias="codeCheckName", description="[Required] Name of the software vulnerability or weakness.")
    count: Optional[StrictInt] = Field(None, description="[Required] Number of instances observed for a specified finding.")
    scan_date: Optional[StrictInt] = Field(None, alias="scanDate", description="[Required] The date of the scan. Unix date format.")
    cwe_id: Optional[StrictStr] = Field(None, alias="cweId", description="[Required] The Common Weakness Enumerator (CWE) identifier.")
    clear_findings: Optional[StrictBool] = Field(None, alias="clearFindings", description="[Optional] When used by itself, can clear out all application findings for a single application/version pairing.")
    __properties = ["rawSeverity", "codeCheckName", "count", "scanDate", "cweId", "clearFindings"]

    @validator('raw_severity')
    def raw_severity_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Low', 'Medium', 'Moderate', 'High', 'Critical'):
            raise ValueError("must be one of enum values ('Low', 'Medium', 'Moderate', 'High', 'Critical')")
        return value

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
    def from_json(cls, json_str: str) -> StaticCodeApplication:
        """Create an instance of StaticCodeApplication from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> StaticCodeApplication:
        """Create an instance of StaticCodeApplication from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return StaticCodeApplication.parse_obj(obj)

        _obj = StaticCodeApplication.parse_obj({
            "raw_severity": obj.get("rawSeverity"),
            "code_check_name": obj.get("codeCheckName"),
            "count": obj.get("count"),
            "scan_date": obj.get("scanDate"),
            "cwe_id": obj.get("cweId"),
            "clear_findings": obj.get("clearFindings")
        })
        return _obj

