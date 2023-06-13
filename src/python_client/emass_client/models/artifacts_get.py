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
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr

class ArtifactsGet(BaseModel):
    """
    ArtifactsGet
    """
    system_id: Optional[StrictInt] = Field(None, alias="systemId", description="[Required] Unique eMASS system identifier.")
    filename: Optional[StrictStr] = Field(None, description="[Required] File name should match exactly one file within the provided zip file. 1000 Characters.")
    is_inherited: Optional[StrictBool] = Field(None, alias="isInherited", description="[Read-only] Indicates whether an artifact is inherited.")
    is_template: Optional[StrictBool] = Field(None, alias="isTemplate", description="[Required] Indicates whether an artifact template.")
    type: Optional[StrictStr] = Field(None, description="[Required] Artifact type options")
    category: Optional[StrictStr] = Field(None, description="[Required] Artifact category options")
    name: Optional[StrictStr] = Field(None, description="[Optional] Artifact name. Character Limit = 100.")
    description: Optional[StrictStr] = Field(None, description="[Optional] Artifact description. 10,000 Characters.")
    reference_page_number: Optional[StrictStr] = Field(None, alias="referencePageNumber", description="[Optional] Artifact reference page number. 50 Characters.")
    ccis: Optional[StrictStr] = Field(None, description="[Optional] CCI associated with test result.")
    controls: Optional[StrictStr] = Field(None, description="[Optional] Control acronym associated with the artifact. NIST SP 800-53 Revision 4 defined.")
    mime_content_type: Optional[StrictStr] = Field(None, alias="mimeContentType", description="[Read-Only] Standard MIME content type derived from file extension.")
    file_size: Optional[StrictStr] = Field(None, alias="fileSize", description="[Read-Only] File size of attached artifact.")
    expiration_date: Optional[StrictInt] = Field(None, alias="expirationDate", description="[Optional] Date Artifact expires and requires review. In Unix Date format.")
    last_reviewed_date: Optional[StrictInt] = Field(None, alias="lastReviewedDate", description="[Optional] Date Artifact was last reviewed. Unix time format.")
    signed_date: Optional[StrictInt] = Field(None, alias="signedDate", description="[Optional] Date artifact was signed. Unix time format.")
    __properties = ["systemId", "filename", "isInherited", "isTemplate", "type", "category", "name", "description", "referencePageNumber", "ccis", "controls", "mimeContentType", "fileSize", "expirationDate", "lastReviewedDate", "signedDate"]

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
    def from_json(cls, json_str: str) -> ArtifactsGet:
        """Create an instance of ArtifactsGet from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if is_inherited (nullable) is None
        # and __fields_set__ contains the field
        if self.is_inherited is None and "is_inherited" in self.__fields_set__:
            _dict['isInherited'] = None

        # set to None if is_template (nullable) is None
        # and __fields_set__ contains the field
        if self.is_template is None and "is_template" in self.__fields_set__:
            _dict['isTemplate'] = None

        # set to None if name (nullable) is None
        # and __fields_set__ contains the field
        if self.name is None and "name" in self.__fields_set__:
            _dict['name'] = None

        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        # set to None if reference_page_number (nullable) is None
        # and __fields_set__ contains the field
        if self.reference_page_number is None and "reference_page_number" in self.__fields_set__:
            _dict['referencePageNumber'] = None

        # set to None if ccis (nullable) is None
        # and __fields_set__ contains the field
        if self.ccis is None and "ccis" in self.__fields_set__:
            _dict['ccis'] = None

        # set to None if controls (nullable) is None
        # and __fields_set__ contains the field
        if self.controls is None and "controls" in self.__fields_set__:
            _dict['controls'] = None

        # set to None if mime_content_type (nullable) is None
        # and __fields_set__ contains the field
        if self.mime_content_type is None and "mime_content_type" in self.__fields_set__:
            _dict['mimeContentType'] = None

        # set to None if file_size (nullable) is None
        # and __fields_set__ contains the field
        if self.file_size is None and "file_size" in self.__fields_set__:
            _dict['fileSize'] = None

        # set to None if expiration_date (nullable) is None
        # and __fields_set__ contains the field
        if self.expiration_date is None and "expiration_date" in self.__fields_set__:
            _dict['expirationDate'] = None

        # set to None if last_reviewed_date (nullable) is None
        # and __fields_set__ contains the field
        if self.last_reviewed_date is None and "last_reviewed_date" in self.__fields_set__:
            _dict['lastReviewedDate'] = None

        # set to None if signed_date (nullable) is None
        # and __fields_set__ contains the field
        if self.signed_date is None and "signed_date" in self.__fields_set__:
            _dict['signedDate'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ArtifactsGet:
        """Create an instance of ArtifactsGet from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ArtifactsGet.parse_obj(obj)

        _obj = ArtifactsGet.parse_obj({
            "system_id": obj.get("systemId"),
            "filename": obj.get("filename"),
            "is_inherited": obj.get("isInherited"),
            "is_template": obj.get("isTemplate"),
            "type": obj.get("type"),
            "category": obj.get("category"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "reference_page_number": obj.get("referencePageNumber"),
            "ccis": obj.get("ccis"),
            "controls": obj.get("controls"),
            "mime_content_type": obj.get("mimeContentType"),
            "file_size": obj.get("fileSize"),
            "expiration_date": obj.get("expirationDate"),
            "last_reviewed_date": obj.get("lastReviewedDate"),
            "signed_date": obj.get("signedDate")
        })
        return _obj

