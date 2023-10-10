# coding: utf-8

## eMASS API v3.12 Specification

The emass_client_api is a Python client that implements the [Enterprise Mission Assurance Support Service (eMASS)](https://disa.mil/~/media/Files/DISA/Fact-Sheets/eMASS.pdf)
Representational State Transfer (REST) Application Programming Interface (API) specifications.


This Python package was generated from the eMASS API specification:

- API version: v3.12
- Package version: 3.11.0
- Build date: 2023-10-10T00:19:35.596959Z[Etc/UTC]

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

class TestResultsGet(BaseModel):
    """
    TestResultsGet
    """
    system_id: Optional[StrictInt] = Field(default=None, description="[Required] Unique eMASS identifier. Will need to provide correct number", alias="systemId")
    control: Optional[StrictStr] = Field(default=None, description="[Read-Only] Control acronym associated with the test result. NIST SP 800-53 Revision 4 defined.")
    cci: Optional[StrictStr] = Field(default=None, description="[Required] CCI associated with test result.")
    assessment_procedure: Optional[StrictStr] = Field(default=None, description="[Required] The Security Control Assessment Procedure being assessed.", alias="assessmentProcedure")
    is_inherited: Optional[StrictBool] = Field(default=None, description="[Read-only] Indicates whether a test result is inherited.", alias="isInherited")
    tested_by: Optional[StrictStr] = Field(default=None, description="[Required] Last Name, First Name. 100 Characters.", alias="testedBy")
    test_date: Optional[StrictInt] = Field(default=None, description="[Required] Unix time format.", alias="testDate")
    description: Optional[StrictStr] = Field(default=None, description="[Required] Include description of test result. 4000 Characters.")
    type: Optional[StrictStr] = Field(default=None, description="[Read-Only] Indicates the location in the Control Approval Chain when the test result is submitted.")
    compliance_status: Optional[StrictStr] = Field(default=None, description="[Required] Test result compliance status", alias="complianceStatus")
    __properties: ClassVar[List[str]] = ["systemId", "control", "cci", "assessmentProcedure", "isInherited", "testedBy", "testDate", "description", "type", "complianceStatus"]

    @field_validator('compliance_status')
    def compliance_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Compliant', 'Non-Compliant', 'Not Applicable'):
            raise ValueError("must be one of enum values ('Compliant', 'Non-Compliant', 'Not Applicable')")
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
        """Create an instance of TestResultsGet from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if control (nullable) is None
        # and model_fields_set contains the field
        if self.control is None and "control" in self.model_fields_set:
            _dict['control'] = None

        # set to None if is_inherited (nullable) is None
        # and model_fields_set contains the field
        if self.is_inherited is None and "is_inherited" in self.model_fields_set:
            _dict['isInherited'] = None

        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        """Create an instance of TestResultsGet from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "systemId": obj.get("systemId"),
            "control": obj.get("control"),
            "cci": obj.get("cci"),
            "assessmentProcedure": obj.get("assessmentProcedure"),
            "isInherited": obj.get("isInherited"),
            "testedBy": obj.get("testedBy"),
            "testDate": obj.get("testDate"),
            "description": obj.get("description"),
            "type": obj.get("type"),
            "complianceStatus": obj.get("complianceStatus")
        })
        return _obj


