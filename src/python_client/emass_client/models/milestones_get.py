# coding: utf-8

## eMASS API v3.9 Specification

The emass_client_api is a Python client that implements the [Enterprise Mission Assurance Support Service (eMASS)](https://disa.mil/~/media/Files/DISA/Fact-Sheets/eMASS.pdf)
Representational State Transfer (REST) Application Programming Interface (API) specifications.


This Python package was generated from the eMASS API specification:

- API version: v3.9
- Package version: 3.9.1
- Build date: 2023-05-23T01:07:18.461999Z[Etc/UTC]

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
from pydantic import BaseModel, Field, StrictInt, StrictStr, validator

class MilestonesGet(BaseModel):
    """
    MilestonesGet
    """
    system_id: Optional[StrictInt] = Field(None, alias="systemId", description="[Required] Unique eMASS system identifier.")
    milestone_id: Optional[StrictInt] = Field(None, alias="milestoneId", description="[Required] Unique item identifier")
    poam_id: Optional[StrictInt] = Field(None, alias="poamId", description="[Required] Unique item identifier")
    description: Optional[StrictStr] = Field(None, description="[Required] Include milestone description.")
    scheduled_completion_date: Optional[StrictInt] = Field(None, alias="scheduledCompletionDate", description="[Required] Required for ongoing and completed POA&M items. Unix time format.")
    review_status: Optional[StrictStr] = Field(None, alias="reviewStatus", description="[Read-Only] Values include the following options: (Not Approved,Under Review,Approved)")
    __properties = ["systemId", "milestoneId", "poamId", "description", "scheduledCompletionDate", "reviewStatus"]

    @validator('review_status')
    def review_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Not Approved', 'Under Review', 'Approved'):
            raise ValueError("must be one of enum values ('Not Approved', 'Under Review', 'Approved')")
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
    def from_json(cls, json_str: str) -> MilestonesGet:
        """Create an instance of MilestonesGet from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MilestonesGet:
        """Create an instance of MilestonesGet from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MilestonesGet.parse_obj(obj)

        _obj = MilestonesGet.parse_obj({
            "system_id": obj.get("systemId"),
            "milestone_id": obj.get("milestoneId"),
            "poam_id": obj.get("poamId"),
            "description": obj.get("description"),
            "scheduled_completion_date": obj.get("scheduledCompletionDate"),
            "review_status": obj.get("reviewStatus")
        })
        return _obj

