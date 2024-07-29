# coding: utf-8

### eMASS API v3.12 Specification
#The emass_client_api is a Python client that implements the [Enterprise Mission Assurance Support Service (eMASS)](https://disa.mil/~/media/Files/DISA/Fact-Sheets/eMASS.pdf)Representational State Transfer (REST) Application Programming Interface (API) specifications.


#This Python package was generated from the eMASS API specification:
#- API version: v3.12- Package version: 3.12.0
#- Build date: 2023-10-10T14:36:02.975730Z[Etc/UTC]
### Requirements.
#Python 
### Installation & Usage### pip install

#If the python package is hosted on a repository, you can install directly using:
#```shpip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
#```(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

#Then import the package:```python
#import emass_client#```
#### Setuptools
#Install via [Setuptools](http://pypi.python.org/pypi/setuptools).
#```shpython setup.py install --user
#```(or `sudo python setup.py install` to install the package for all users)

#Then import the package:```python
#import emass_client#```
#### Tests
#Execute `pytest` to run the tests.
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

class Ssps(BaseModel):
    """
    Ssps
    """
    ssp_name: Optional[StrictStr] = Field(default=None, description="[Read-Only] Name of the System Security Plan.", alias="sspName")
    ssp_version: Optional[StrictStr] = Field(default=None, description="[Read-Only] Version of the System Security Plan.", alias="sspVersion")
    ssp_date: Optional[StrictInt] = Field(default=None, description="[Read-Only] Date of the System Security Plan. Unix date format.", alias="sspDate")
    __properties: ClassVar[List[str]] = ["sspName", "sspVersion", "sspDate"]

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
        """Create an instance of Ssps from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if ssp_name (nullable) is None
        # and model_fields_set contains the field
        if self.ssp_name is None and "ssp_name" in self.model_fields_set:
            _dict['sspName'] = None

        # set to None if ssp_version (nullable) is None
        # and model_fields_set contains the field
        if self.ssp_version is None and "ssp_version" in self.model_fields_set:
            _dict['sspVersion'] = None

        # set to None if ssp_date (nullable) is None
        # and model_fields_set contains the field
        if self.ssp_date is None and "ssp_date" in self.model_fields_set:
            _dict['sspDate'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        """Create an instance of Ssps from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "sspName": obj.get("sspName"),
            "sspVersion": obj.get("sspVersion"),
            "sspDate": obj.get("sspDate")
        })
        return _obj


