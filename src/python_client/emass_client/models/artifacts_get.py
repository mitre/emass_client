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
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from pydantic import Field
from typing import Dict, Any
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ArtifactsGet(BaseModel):
    """
    ArtifactsGet
    """
    system_id: Optional[StrictInt] = Field(default=None, description="[Required] Unique eMASS system identifier.", alias="systemId")
    filename: Optional[StrictStr] = Field(default=None, description="[Required] File name should match exactly one file within the provided zip file. 1000 Characters. or Application/zip file. Max 30MB per artifact. ")
    is_inherited: Optional[StrictBool] = Field(default=None, description="[Read-only] Indicates whether an artifact is inherited.", alias="isInherited")
    is_template: Optional[StrictBool] = Field(default=None, description="[Required] Indicates whether an artifact template.", alias="isTemplate")
    type: Optional[StrictStr] = Field(default=None, description="[Required] Artifact type options")
    category: Optional[StrictStr] = Field(default=None, description="[Required] Artifact category options")
    name: Optional[StrictStr] = Field(default=None, description="[Optional] Artifact name. Character Limit = 100.")
    description: Optional[StrictStr] = Field(default=None, description="[Optional] Artifact description. 10,000 Characters.")
    reference_page_number: Optional[StrictStr] = Field(default=None, description="[Optional] Artifact reference page number. 50 Characters.", alias="referencePageNumber")
    ccis: Optional[StrictStr] = Field(default=None, description="[Read-Only] CCI mapping for Assessment Procedures associated with the artifact.")
    controls: Optional[StrictStr] = Field(default=None, description="[Optional] Control acronym associated with the artifact. NIST SP 800-53 Revision 4 defined.")
    assessment_procedures: Optional[StrictStr] = Field(default=None, description="[Optional] The Security Control Assessment Procedure being associated with the artifact.", alias="assessmentProcedures")
    mime_content_type: Optional[StrictStr] = Field(default=None, description="[Read-Only] Standard MIME content type derived from file extension.", alias="mimeContentType")
    file_size: Optional[StrictStr] = Field(default=None, description="[Read-Only] File size of attached artifact.", alias="fileSize")
    expiration_date: Optional[StrictInt] = Field(default=None, description="[Optional] Date Artifact expires and requires review. In Unix Date format.", alias="expirationDate")
    last_reviewed_date: Optional[StrictInt] = Field(default=None, description="[Optional] Date Artifact was last reviewed. Unix time format.", alias="lastReviewedDate")
    signed_date: Optional[StrictInt] = Field(default=None, description="[Optional] Date artifact was signed. Unix time format.", alias="signedDate")
    __properties: ClassVar[List[str]] = ["systemId", "filename", "isInherited", "isTemplate", "type", "category", "name", "description", "referencePageNumber", "ccis", "controls", "assessmentProcedures", "mimeContentType", "fileSize", "expirationDate", "lastReviewedDate", "signedDate"]

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
        """Create an instance of ArtifactsGet from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if is_inherited (nullable) is None
        # and model_fields_set contains the field
        if self.is_inherited is None and "is_inherited" in self.model_fields_set:
            _dict['isInherited'] = None

        # set to None if is_template (nullable) is None
        # and model_fields_set contains the field
        if self.is_template is None and "is_template" in self.model_fields_set:
            _dict['isTemplate'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if reference_page_number (nullable) is None
        # and model_fields_set contains the field
        if self.reference_page_number is None and "reference_page_number" in self.model_fields_set:
            _dict['referencePageNumber'] = None

        # set to None if ccis (nullable) is None
        # and model_fields_set contains the field
        if self.ccis is None and "ccis" in self.model_fields_set:
            _dict['ccis'] = None

        # set to None if controls (nullable) is None
        # and model_fields_set contains the field
        if self.controls is None and "controls" in self.model_fields_set:
            _dict['controls'] = None

        # set to None if mime_content_type (nullable) is None
        # and model_fields_set contains the field
        if self.mime_content_type is None and "mime_content_type" in self.model_fields_set:
            _dict['mimeContentType'] = None

        # set to None if file_size (nullable) is None
        # and model_fields_set contains the field
        if self.file_size is None and "file_size" in self.model_fields_set:
            _dict['fileSize'] = None

        # set to None if expiration_date (nullable) is None
        # and model_fields_set contains the field
        if self.expiration_date is None and "expiration_date" in self.model_fields_set:
            _dict['expirationDate'] = None

        # set to None if last_reviewed_date (nullable) is None
        # and model_fields_set contains the field
        if self.last_reviewed_date is None and "last_reviewed_date" in self.model_fields_set:
            _dict['lastReviewedDate'] = None

        # set to None if signed_date (nullable) is None
        # and model_fields_set contains the field
        if self.signed_date is None and "signed_date" in self.model_fields_set:
            _dict['signedDate'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        """Create an instance of ArtifactsGet from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "systemId": obj.get("systemId"),
            "filename": obj.get("filename"),
            "isInherited": obj.get("isInherited"),
            "isTemplate": obj.get("isTemplate"),
            "type": obj.get("type"),
            "category": obj.get("category"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "referencePageNumber": obj.get("referencePageNumber"),
            "ccis": obj.get("ccis"),
            "controls": obj.get("controls"),
            "assessmentProcedures": obj.get("assessmentProcedures"),
            "mimeContentType": obj.get("mimeContentType"),
            "fileSize": obj.get("fileSize"),
            "expirationDate": obj.get("expirationDate"),
            "lastReviewedDate": obj.get("lastReviewedDate"),
            "signedDate": obj.get("signedDate")
        })
        return _obj


