# coding: utf-8

"""
    Enterprise Mission Assurance Support Service (eMASS)

    The eMASS Representational State Transfer (REST) Application Programming Interface (API) enables users to perform assessments and complete actions associated with system records.  The eMASS API provides an interface for application to communicate eMASS Services. For information on how to register and use the eMASS API reference the [eMASS API Getting Started](eMASSGettingStarted.md).  Additional information about eMASS can be obtain by contacting the National Industrial Security Program (NISP). Points of Contact are: 

    The version of the OpenAPI document: v3.22
    Contact: disa.global.servicedesk.mbx.ma-ticket-request@mail.mil
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class ForbiddenMeta(BaseModel):
    """
    ForbiddenMeta
    """ # noqa: E501
    code: Optional[Annotated[int, Field(le=403, strict=True, ge=403)]] = 403
    error_message: Optional[StrictStr] = Field(default='Request was blocked by the application due to a lack of client permissions to the API or to a specific endpoint', alias="errorMessage")
    __properties: ClassVar[List[str]] = ["code", "errorMessage"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ForbiddenMeta from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ForbiddenMeta from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "code": obj.get("code") if obj.get("code") is not None else 403,
            "errorMessage": obj.get("errorMessage") if obj.get("errorMessage") is not None else 'Request was blocked by the application due to a lack of client permissions to the API or to a specific endpoint'
        })
        return _obj


