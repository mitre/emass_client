# coding: utf-8

## eMASS API  Specification

The  is a Python client that implements the [Enterprise Mission Assurance Support Service (eMASS)](https://disa.mil/~/media/Files/DISA/Fact-Sheets/eMASS.pdf)
Representational State Transfer (REST) Application Programming Interface (API) specifications.


This Python package was generated from the eMASS API specification:

- API version: 
- Package version: 
- Build date: 

## Requirements.

Python 

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https:////.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https:////.git`)

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

## Getting Started

In your own code, to use this library to connect and interact with ,
you can run the following:

```python

import time
import emass_client
from pprint import pprint
```
## Documentation For Authorization

Authentication information is documented in the [emass_client specification GitHub page](https://mitre.github.io/emass_client/docs/redoc/)

## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in emass_client.apis and emass_client.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from emass_client..default_api import DefaultApi`
- `from emass_client..pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import emass_client
from emass_client.apis import *
from emass_client.models import *
```
from dataclasses import dataclass
import typing_extensions
import urllib3
from urllib3._collections import HTTPHeaderDict

from emass_client import api_client, exceptions
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

from emass_client.model.response490 import Response490
from emass_client.model.response400 import Response400
from emass_client.model.response401 import Response401
from emass_client.model.response500 import Response500
from emass_client.model.response403 import Response403
from emass_client.model.response405 import Response405
from emass_client.model.response404 import Response404
from emass_client.model.systems_response import SystemsResponse

# Query params
IncludePackageSchema = schemas.BoolSchema
RegistrationTypeSchema = schemas.StrSchema
DitprIdSchema = schemas.StrSchema
CoamsIdSchema = schemas.StrSchema


class PolicySchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def DIACAP(cls):
        return cls("diacap")
    
    @schemas.classproperty
    def RMF(cls):
        return cls("rmf")
    
    @schemas.classproperty
    def REPORTING(cls):
        return cls("reporting")
IncludeDitprMetricsSchema = schemas.BoolSchema
IncludeDecommissionedSchema = schemas.BoolSchema
ReportsForScorecardSchema = schemas.BoolSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'includePackage': typing.Union[IncludePackageSchema, bool, ],
        'registrationType': typing.Union[RegistrationTypeSchema, str, ],
        'ditprId': typing.Union[DitprIdSchema, str, ],
        'coamsId': typing.Union[CoamsIdSchema, str, ],
        'policy': typing.Union[PolicySchema, str, ],
        'includeDitprMetrics': typing.Union[IncludeDitprMetricsSchema, bool, ],
        'includeDecommissioned': typing.Union[IncludeDecommissionedSchema, bool, ],
        'reportsForScorecard': typing.Union[ReportsForScorecardSchema, bool, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_include_package = api_client.QueryParameter(
    name="includePackage",
    style=api_client.ParameterStyle.FORM,
    schema=IncludePackageSchema,
    explode=True,
)
request_query_registration_type = api_client.QueryParameter(
    name="registrationType",
    style=api_client.ParameterStyle.FORM,
    schema=RegistrationTypeSchema,
    explode=True,
)
request_query_ditpr_id = api_client.QueryParameter(
    name="ditprId",
    style=api_client.ParameterStyle.FORM,
    schema=DitprIdSchema,
    explode=True,
)
request_query_coams_id = api_client.QueryParameter(
    name="coamsId",
    style=api_client.ParameterStyle.FORM,
    schema=CoamsIdSchema,
    explode=True,
)
request_query_policy = api_client.QueryParameter(
    name="policy",
    style=api_client.ParameterStyle.FORM,
    schema=PolicySchema,
    explode=True,
)
request_query_include_ditpr_metrics = api_client.QueryParameter(
    name="includeDitprMetrics",
    style=api_client.ParameterStyle.FORM,
    schema=IncludeDitprMetricsSchema,
    explode=True,
)
request_query_include_decommissioned = api_client.QueryParameter(
    name="includeDecommissioned",
    style=api_client.ParameterStyle.FORM,
    schema=IncludeDecommissionedSchema,
    explode=True,
)
request_query_reports_for_scorecard = api_client.QueryParameter(
    name="reportsForScorecard",
    style=api_client.ParameterStyle.FORM,
    schema=ReportsForScorecardSchema,
    explode=True,
)
SchemaFor200ResponseBodyApplicationJson = SystemsResponse


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor200ResponseBodyApplicationJson,
    ]
    headers: schemas.Unset = schemas.unset


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor400ResponseBodyApplicationJson = Response400


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor400ResponseBodyApplicationJson,
    ]
    headers: schemas.Unset = schemas.unset


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJson),
    },
)
SchemaFor401ResponseBodyApplicationJson = Response401


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor401ResponseBodyApplicationJson,
    ]
    headers: schemas.Unset = schemas.unset


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor401ResponseBodyApplicationJson),
    },
)
SchemaFor403ResponseBodyApplicationJson = Response403


@dataclass
class ApiResponseFor403(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor403ResponseBodyApplicationJson,
    ]
    headers: schemas.Unset = schemas.unset


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor403ResponseBodyApplicationJson),
    },
)
SchemaFor404ResponseBodyApplicationJson = Response404


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor404ResponseBodyApplicationJson,
    ]
    headers: schemas.Unset = schemas.unset


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor404ResponseBodyApplicationJson),
    },
)
SchemaFor405ResponseBodyApplicationJson = Response405


@dataclass
class ApiResponseFor405(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor405ResponseBodyApplicationJson,
    ]
    headers: schemas.Unset = schemas.unset


_response_for_405 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor405,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor405ResponseBodyApplicationJson),
    },
)
SchemaFor490ResponseBodyApplicationJson = Response490


@dataclass
class ApiResponseFor490(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor490ResponseBodyApplicationJson,
    ]
    headers: schemas.Unset = schemas.unset


_response_for_490 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor490,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor490ResponseBodyApplicationJson),
    },
)
SchemaFor500ResponseBodyApplicationJson = Response500


@dataclass
class ApiResponseFor500(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor500ResponseBodyApplicationJson,
    ]
    headers: schemas.Unset = schemas.unset


_response_for_500 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor500,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor500ResponseBodyApplicationJson),
    },
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):
    @typing.overload
    def _get_systems_oapg(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def _get_systems_oapg(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def _get_systems_oapg(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def _get_systems_oapg(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        """
        Get system information
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value

        prefix_separator_iterator = None
        for parameter in (
            request_query_include_package,
            request_query_registration_type,
            request_query_ditpr_id,
            request_query_coams_id,
            request_query_policy,
            request_query_include_ditpr_metrics,
            request_query_include_decommissioned,
            request_query_reports_for_scorecard,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value

        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)

        response = self.api_client.call_api(
            resource_path=used_path,
            method='get'.upper(),
            headers=_headers,
            auth_settings=_auth,
            stream=stream,
            timeout=timeout,
        )

        if skip_deserialization:
            api_response = api_client.ApiResponseWithoutDeserialization(response=response)
        else:
            response_for_status = _status_code_to_response.get(str(response.status))
            if response_for_status:
                api_response = response_for_status.deserialize(response, self.api_client.configuration)
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(response=response)

        if not 200 <= response.status <= 299:
            raise exceptions.ApiException(
                status=response.status,
                reason=response.reason,
                api_response=api_response
            )

        return api_response


class GetSystems(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    @typing.overload
    def get_systems(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def get_systems(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def get_systems(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def get_systems(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._get_systems_oapg(
            query_params=query_params,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    @typing.overload
    def get(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def get(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def get(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def get(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._get_systems_oapg(
            query_params=query_params,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


