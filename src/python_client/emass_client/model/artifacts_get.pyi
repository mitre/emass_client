# coding: utf-8

"""
    Enterprise Mission Assurance Support Service (eMASS)

    The Enterprise Mission Assurance Support Service (eMASS) Representational State Transfer (REST) Application Programming Interface (API) enables users to perform assessments and complete actions associated with system records.   <strong>Register External Application (that use the eMASS API)</strong></br> New users will need to [register](https://nisp.emass.apps.mil/Content/Help/jobaids/eMASS_OT_NewUser_Job_Aid.pdf) an API key with the eMASS development team prior to accessing the site for the first time. The eMASS REST API  requires a client certificate (SSL/TLS, DoD PKI only). Use the `Registration` endpoint to register the client certificate.</br></br>  Every call to the eMASS REST API will require the use of the agreed upon public key certificate and API key.  The API key must be provided in the request header for all endpoint calls (api-key). If the service receives an untrusted certificate or API key, a 401 error response code will be returned along with an error message.</br></br>  <strong>Available Request Headers</strong></br> <table>   <tr>     <th align=left>key</th>     <th align=left>Example Value</th>     <th align=left>Description</th>   </tr>   <tr>     <td>`api-key`</td>     <td>api-key-provided-by-emass</td>     <td>This API key must be provided in the request header for all endpoint calls</td>   </tr>   <tr>     <td>`user-uid`</td>     <td>USER.UID.KEY</td>     <td>This User unique identifier key must be provided in the request header for all PUT, POST, and DELETE endpoint calls</td>   </tr>   <tr>     <td></td><td></td>     <td>       Note: For DoD users this is the DoD ID Number (EIDIPI) on their DoD CAC     </td>   </tr> </table>  </br><strong>Approve API Client for Actionable Requests</strong></br> Users are required to log-in to eMASS and grant permissions for a client to update data within eMASS on their behalf. This is only required for actionable requests (PUT, POST, DELETE). The Registration Endpoint and all GET requests can be accessed without completing this process with the correct permissions. Please note that leaving a field parameter blank (for PUT/POST requests) has the potential to clear information in the active eMASS records.  To establish an account with eMASS and/or acquire an api-key/user-uid, contact one of the listed POC:   # noqa: E501

    The version of the OpenAPI document: v3.9
    Contact: disa.meade.id.mbx.emass-tier-iii-support@mail.mil
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from emass_client import schemas  # noqa: F401


class ArtifactsGet(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            systemId = schemas.Int64Schema
            filename = schemas.StrSchema
            
            
            class isInherited(
                schemas.BoolBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneBoolMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, bool, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'isInherited':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class isTemplate(
                schemas.BoolBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneBoolMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, bool, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'isTemplate':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            type = schemas.StrSchema
            category = schemas.StrSchema
            
            
            class name(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'name':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class description(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'description':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class referencePageNumber(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'referencePageNumber':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class ccis(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'ccis':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class controls(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'controls':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class mimeContentType(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'mimeContentType':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class fileSize(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'fileSize':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class expirationDate(
                schemas.Int64Base,
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                class MetaOapg:
                    format = 'int64'
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'expirationDate':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class lastReviewedDate(
                schemas.Int64Base,
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                class MetaOapg:
                    format = 'int64'
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'lastReviewedDate':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class signedDate(
                schemas.Int64Base,
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                class MetaOapg:
                    format = 'int64'
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'signedDate':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "systemId": systemId,
                "filename": filename,
                "isInherited": isInherited,
                "isTemplate": isTemplate,
                "type": type,
                "category": category,
                "name": name,
                "description": description,
                "referencePageNumber": referencePageNumber,
                "ccis": ccis,
                "controls": controls,
                "mimeContentType": mimeContentType,
                "fileSize": fileSize,
                "expirationDate": expirationDate,
                "lastReviewedDate": lastReviewedDate,
                "signedDate": signedDate,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["systemId"]) -> MetaOapg.properties.systemId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["filename"]) -> MetaOapg.properties.filename: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isInherited"]) -> MetaOapg.properties.isInherited: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isTemplate"]) -> MetaOapg.properties.isTemplate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["category"]) -> MetaOapg.properties.category: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["referencePageNumber"]) -> MetaOapg.properties.referencePageNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ccis"]) -> MetaOapg.properties.ccis: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["controls"]) -> MetaOapg.properties.controls: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mimeContentType"]) -> MetaOapg.properties.mimeContentType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fileSize"]) -> MetaOapg.properties.fileSize: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expirationDate"]) -> MetaOapg.properties.expirationDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastReviewedDate"]) -> MetaOapg.properties.lastReviewedDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["signedDate"]) -> MetaOapg.properties.signedDate: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["systemId"], typing_extensions.Literal["filename"], typing_extensions.Literal["isInherited"], typing_extensions.Literal["isTemplate"], typing_extensions.Literal["type"], typing_extensions.Literal["category"], typing_extensions.Literal["name"], typing_extensions.Literal["description"], typing_extensions.Literal["referencePageNumber"], typing_extensions.Literal["ccis"], typing_extensions.Literal["controls"], typing_extensions.Literal["mimeContentType"], typing_extensions.Literal["fileSize"], typing_extensions.Literal["expirationDate"], typing_extensions.Literal["lastReviewedDate"], typing_extensions.Literal["signedDate"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["systemId"]) -> typing.Union[MetaOapg.properties.systemId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["filename"]) -> typing.Union[MetaOapg.properties.filename, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isInherited"]) -> typing.Union[MetaOapg.properties.isInherited, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isTemplate"]) -> typing.Union[MetaOapg.properties.isTemplate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["category"]) -> typing.Union[MetaOapg.properties.category, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["referencePageNumber"]) -> typing.Union[MetaOapg.properties.referencePageNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ccis"]) -> typing.Union[MetaOapg.properties.ccis, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["controls"]) -> typing.Union[MetaOapg.properties.controls, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mimeContentType"]) -> typing.Union[MetaOapg.properties.mimeContentType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fileSize"]) -> typing.Union[MetaOapg.properties.fileSize, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expirationDate"]) -> typing.Union[MetaOapg.properties.expirationDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastReviewedDate"]) -> typing.Union[MetaOapg.properties.lastReviewedDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["signedDate"]) -> typing.Union[MetaOapg.properties.signedDate, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["systemId"], typing_extensions.Literal["filename"], typing_extensions.Literal["isInherited"], typing_extensions.Literal["isTemplate"], typing_extensions.Literal["type"], typing_extensions.Literal["category"], typing_extensions.Literal["name"], typing_extensions.Literal["description"], typing_extensions.Literal["referencePageNumber"], typing_extensions.Literal["ccis"], typing_extensions.Literal["controls"], typing_extensions.Literal["mimeContentType"], typing_extensions.Literal["fileSize"], typing_extensions.Literal["expirationDate"], typing_extensions.Literal["lastReviewedDate"], typing_extensions.Literal["signedDate"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        systemId: typing.Union[MetaOapg.properties.systemId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        filename: typing.Union[MetaOapg.properties.filename, str, schemas.Unset] = schemas.unset,
        isInherited: typing.Union[MetaOapg.properties.isInherited, None, bool, schemas.Unset] = schemas.unset,
        isTemplate: typing.Union[MetaOapg.properties.isTemplate, None, bool, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        category: typing.Union[MetaOapg.properties.category, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, None, str, schemas.Unset] = schemas.unset,
        description: typing.Union[MetaOapg.properties.description, None, str, schemas.Unset] = schemas.unset,
        referencePageNumber: typing.Union[MetaOapg.properties.referencePageNumber, None, str, schemas.Unset] = schemas.unset,
        ccis: typing.Union[MetaOapg.properties.ccis, None, str, schemas.Unset] = schemas.unset,
        controls: typing.Union[MetaOapg.properties.controls, None, str, schemas.Unset] = schemas.unset,
        mimeContentType: typing.Union[MetaOapg.properties.mimeContentType, None, str, schemas.Unset] = schemas.unset,
        fileSize: typing.Union[MetaOapg.properties.fileSize, None, str, schemas.Unset] = schemas.unset,
        expirationDate: typing.Union[MetaOapg.properties.expirationDate, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        lastReviewedDate: typing.Union[MetaOapg.properties.lastReviewedDate, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        signedDate: typing.Union[MetaOapg.properties.signedDate, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'ArtifactsGet':
        return super().__new__(
            cls,
            *_args,
            systemId=systemId,
            filename=filename,
            isInherited=isInherited,
            isTemplate=isTemplate,
            type=type,
            category=category,
            name=name,
            description=description,
            referencePageNumber=referencePageNumber,
            ccis=ccis,
            controls=controls,
            mimeContentType=mimeContentType,
            fileSize=fileSize,
            expirationDate=expirationDate,
            lastReviewedDate=lastReviewedDate,
            signedDate=signedDate,
            _configuration=_configuration,
        )