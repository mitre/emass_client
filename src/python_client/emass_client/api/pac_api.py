# coding: utf-8

## eMASS API v3.12 Specification

The emass_client_api is a Python client that implements the [Enterprise Mission Assurance Support Service (eMASS)](https://disa.mil/~/media/Files/DISA/Fact-Sheets/eMASS.pdf)
Representational State Transfer (REST) Application Programming Interface (API) specifications.


This Python package was generated from the eMASS API specification:

- API version: v3.12
- Package version: 3.11.1
- Build date: 2023-10-10T02:05:20.537795Z[Etc/UTC]

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

import re  # noqa: F401
import io
import warnings

from pydantic import validate_call, ValidationError
from typing import Dict, List, Optional, Tuple

from pydantic import Field
from typing_extensions import Annotated
from pydantic import StrictInt

from typing import List

from emass_client.models.pac_response_get import PacResponseGet
from emass_client.models.pac_response_post import PacResponsePost
from emass_client.models.object import object

from emass_client.api_client import ApiClient
from emass_client.api_response import ApiResponse
from emass_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class PACApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_call
    def add_system_pac(self, system_id : Annotated[StrictInt, Field(description="**System Id**: The unique system record identifier.")], request_body : Annotated[List[object], Field(description="Add system package to PAC for review")], **kwargs) -> PacResponsePost:  # noqa: E501
        """Initiate system workflow for review  # noqa: E501

        Adds a Package Approval Chain (PAC) for given `systemId` path parameter  **Request Body Required Fields** - `workflow` - `name` - `comments`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.add_system_pac(system_id, request_body, async_req=True)
        >>> result = thread.get()

        :param system_id: **System Id**: The unique system record identifier. (required)
        :type system_id: int
        :param request_body: Add system package to PAC for review (required)
        :type request_body: List[object]
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: PacResponsePost
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the add_system_pac_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.add_system_pac_with_http_info(system_id, request_body, **kwargs)  # noqa: E501

    @validate_call
    def add_system_pac_with_http_info(self, system_id : Annotated[StrictInt, Field(description="**System Id**: The unique system record identifier.")], request_body : Annotated[List[object], Field(description="Add system package to PAC for review")], **kwargs) -> ApiResponse:  # noqa: E501
        """Initiate system workflow for review  # noqa: E501

        Adds a Package Approval Chain (PAC) for given `systemId` path parameter  **Request Body Required Fields** - `workflow` - `name` - `comments`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.add_system_pac_with_http_info(system_id, request_body, async_req=True)
        >>> result = thread.get()

        :param system_id: **System Id**: The unique system record identifier. (required)
        :type system_id: int
        :param request_body: Add system package to PAC for review (required)
        :type request_body: List[object]
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(PacResponsePost, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'system_id',
            'request_body'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_system_pac" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats: Dict[str, str] = {}

        # process the path parameters
        _path_params: Dict[str, str] = {}
        if _params['system_id'] is not None:
            _path_params['systemId'] = _params['system_id']


        # process the query parameters
        _query_params: List[Tuple[str, str]] = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, str] = {}
        # process the body parameter
        _body_params = None
        if _params['request_body'] is not None:
            _body_params = _params['request_body']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings: List[str] = ['apiKey', 'mockType', 'userId']  # noqa: E501

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "PacResponsePost",
            '201': "Response201",
            '400': "Response400",
            '401': "Response401",
            '403': "Response403",
            '404': "Response404",
            '405': "Response405",
            '411': "Response411",
            '500': "Response500",
        }

        return self.api_client.call_api(
            '/api/systems/{systemId}/approval/pac', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_call
    def get_system_pac(self, system_id : Annotated[StrictInt, Field(description="**System Id**: The unique system record identifier.")], **kwargs) -> PacResponseGet:  # noqa: E501
        """Get status of active workflows in a system  # noqa: E501

        Returns the location of a system's package in the Package Approval Chain (PAC) for matching `systemId` path parameter  **Notes:** - If the indicated system has any active workflows, the response will include information   such as the workflow type and the current stage of each workflow.  - If there are no active workflows, then a null data member will be returned.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_system_pac(system_id, async_req=True)
        >>> result = thread.get()

        :param system_id: **System Id**: The unique system record identifier. (required)
        :type system_id: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: PacResponseGet
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_system_pac_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_system_pac_with_http_info(system_id, **kwargs)  # noqa: E501

    @validate_call
    def get_system_pac_with_http_info(self, system_id : Annotated[StrictInt, Field(description="**System Id**: The unique system record identifier.")], **kwargs) -> ApiResponse:  # noqa: E501
        """Get status of active workflows in a system  # noqa: E501

        Returns the location of a system's package in the Package Approval Chain (PAC) for matching `systemId` path parameter  **Notes:** - If the indicated system has any active workflows, the response will include information   such as the workflow type and the current stage of each workflow.  - If there are no active workflows, then a null data member will be returned.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_system_pac_with_http_info(system_id, async_req=True)
        >>> result = thread.get()

        :param system_id: **System Id**: The unique system record identifier. (required)
        :type system_id: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(PacResponseGet, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'system_id'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_system_pac" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats: Dict[str, str] = {}

        # process the path parameters
        _path_params: Dict[str, str] = {}
        if _params['system_id'] is not None:
            _path_params['systemId'] = _params['system_id']


        # process the query parameters
        _query_params: List[Tuple[str, str]] = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, str] = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings: List[str] = ['apiKey', 'mockType', 'userId']  # noqa: E501

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "PacResponseGet",
            '400': "Response400",
            '401': "Response401",
            '403': "Response403",
            '404': "Response404",
            '405': "Response405",
            '490': "Response490",
            '500': "Response500",
        }

        return self.api_client.call_api(
            '/api/systems/{systemId}/approval/pac', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))