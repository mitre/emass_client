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
from pydantic import BaseModel, StrictInt, StrictStr, field_validator
from pydantic import Field
from typing import Dict, Any
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class MilestonesGet(BaseModel):
    """
    MilestonesGet
    """
    system_id: Optional[StrictInt] = Field(default=None, description="[Required] Unique eMASS system identifier.", alias="systemId")
    milestone_id: Optional[StrictInt] = Field(default=None, description="[Required] Unique item identifier", alias="milestoneId")
    poam_id: Optional[StrictInt] = Field(default=None, description="[Required] Unique item identifier", alias="poamId")
    description: Optional[StrictStr] = Field(default=None, description="[Required] Include milestone description.")
    scheduled_completion_date: Optional[StrictInt] = Field(default=None, description="[Required] Required for ongoing and completed POA&M items. Unix time format.", alias="scheduledCompletionDate")
    review_status: Optional[StrictStr] = Field(default=None, description="[Read-Only] Values include the following options: (Not Approved,Under Review,Approved)", alias="reviewStatus")
    __properties: ClassVar[List[str]] = ["systemId", "milestoneId", "poamId", "description", "scheduledCompletionDate", "reviewStatus"]

    @field_validator('review_status')
    def review_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Not Approved', 'Under Review', 'Approved'):
            raise ValueError("must be one of enum values ('Not Approved', 'Under Review', 'Approved')")
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
        """Create an instance of MilestonesGet from a JSON string"""
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
        """Create an instance of MilestonesGet from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "systemId": obj.get("systemId"),
            "milestoneId": obj.get("milestoneId"),
            "poamId": obj.get("poamId"),
            "description": obj.get("description"),
            "scheduledCompletionDate": obj.get("scheduledCompletionDate"),
            "reviewStatus": obj.get("reviewStatus")
        })
        return _obj


