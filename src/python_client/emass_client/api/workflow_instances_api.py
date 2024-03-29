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

import re  # noqa: F401
import io
import warnings

from pydantic import validate_call, ValidationError
from typing import Dict, List, Optional, Tuple

from pydantic import Field
from typing_extensions import Annotated
from pydantic import StrictBool, StrictInt, StrictStr, field_validator

from typing import Optional

from emass_client.models.workflow_instance_response_get import WorkflowInstanceResponseGet
from emass_client.models.workflow_instances_response_get import WorkflowInstancesResponseGet

from emass_client.api_client import ApiClient
from emass_client.api_response import ApiResponse
from emass_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class WorkflowInstancesApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_call
    def get_system_workflow_instances(
        self,
        include_comments: Annotated[Optional[StrictBool], Field(description="**Include Comments**: If no value is specified, the default returns true to not include transition comments.  Note: Corresponds to the Comments textbox that is required at most workflow transitions. Does not include other text input fields such as Terms / Conditions for Authorization. ")] = None,
        include_decommission_systems: Annotated[Optional[StrictBool], Field(description="**Include Decommission Systems**: If no value is specified, the default returns false to exclude decommissioned systems. ")] = None,
        page_index: Annotated[Optional[StrictInt], Field(description="**Page Index**: If no value is specified, the default returns results from the first page with an index of 0.  **Note:** Pages contain 1000 workflow instances. ")] = None,
        since_date: Annotated[Optional[StrictStr], Field(description="**Date**: Filter on authorization/assessment date (Unix date format).  Note: Filters off the lastEditedDate field.  Note: The authorization/assessment decisions on completed workflows  can be edited for up to 30 days after the initial decision is made. ")] = None,
        status: Annotated[Optional[StrictStr], Field(description="**Status**: Filter by status.  If no value is specified, the default returns all to include both active and inactive workflows.  Note: Any workflows at a current stage of Complete or Cancelled are inactive. Ongoing workflows currently at other stages are active. ")] = None,
        **kwargs,
    ) -> WorkflowInstancesResponseGet:
        """Get workflow instances in a site  # noqa: E501

        View detailed information on all active and historical workflows filtered by provided parameters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_system_workflow_instances(include_comments, include_decommission_systems, page_index, since_date, status, async_req=True)
        >>> result = thread.get()

        :param include_comments: **Include Comments**: If no value is specified, the default returns true to not include transition comments.  Note: Corresponds to the Comments textbox that is required at most workflow transitions. Does not include other text input fields such as Terms / Conditions for Authorization. 
        :type include_comments: bool
        :param include_decommission_systems: **Include Decommission Systems**: If no value is specified, the default returns false to exclude decommissioned systems. 
        :type include_decommission_systems: bool
        :param page_index: **Page Index**: If no value is specified, the default returns results from the first page with an index of 0.  **Note:** Pages contain 1000 workflow instances. 
        :type page_index: int
        :param since_date: **Date**: Filter on authorization/assessment date (Unix date format).  Note: Filters off the lastEditedDate field.  Note: The authorization/assessment decisions on completed workflows  can be edited for up to 30 days after the initial decision is made. 
        :type since_date: str
        :param status: **Status**: Filter by status.  If no value is specified, the default returns all to include both active and inactive workflows.  Note: Any workflows at a current stage of Complete or Cancelled are inactive. Ongoing workflows currently at other stages are active. 
        :type status: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: WorkflowInstancesResponseGet
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_system_workflow_instances_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_system_workflow_instances_with_http_info(include_comments, include_decommission_systems, page_index, since_date, status, **kwargs)  # noqa: E501

    @validate_call
    def get_system_workflow_instances_with_http_info(
        self,
        include_comments: Annotated[Optional[StrictBool], Field(description="**Include Comments**: If no value is specified, the default returns true to not include transition comments.  Note: Corresponds to the Comments textbox that is required at most workflow transitions. Does not include other text input fields such as Terms / Conditions for Authorization. ")] = None,
        include_decommission_systems: Annotated[Optional[StrictBool], Field(description="**Include Decommission Systems**: If no value is specified, the default returns false to exclude decommissioned systems. ")] = None,
        page_index: Annotated[Optional[StrictInt], Field(description="**Page Index**: If no value is specified, the default returns results from the first page with an index of 0.  **Note:** Pages contain 1000 workflow instances. ")] = None,
        since_date: Annotated[Optional[StrictStr], Field(description="**Date**: Filter on authorization/assessment date (Unix date format).  Note: Filters off the lastEditedDate field.  Note: The authorization/assessment decisions on completed workflows  can be edited for up to 30 days after the initial decision is made. ")] = None,
        status: Annotated[Optional[StrictStr], Field(description="**Status**: Filter by status.  If no value is specified, the default returns all to include both active and inactive workflows.  Note: Any workflows at a current stage of Complete or Cancelled are inactive. Ongoing workflows currently at other stages are active. ")] = None,
        **kwargs,
    ) -> ApiResponse:
        """Get workflow instances in a site  # noqa: E501

        View detailed information on all active and historical workflows filtered by provided parameters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_system_workflow_instances_with_http_info(include_comments, include_decommission_systems, page_index, since_date, status, async_req=True)
        >>> result = thread.get()

        :param include_comments: **Include Comments**: If no value is specified, the default returns true to not include transition comments.  Note: Corresponds to the Comments textbox that is required at most workflow transitions. Does not include other text input fields such as Terms / Conditions for Authorization. 
        :type include_comments: bool
        :param include_decommission_systems: **Include Decommission Systems**: If no value is specified, the default returns false to exclude decommissioned systems. 
        :type include_decommission_systems: bool
        :param page_index: **Page Index**: If no value is specified, the default returns results from the first page with an index of 0.  **Note:** Pages contain 1000 workflow instances. 
        :type page_index: int
        :param since_date: **Date**: Filter on authorization/assessment date (Unix date format).  Note: Filters off the lastEditedDate field.  Note: The authorization/assessment decisions on completed workflows  can be edited for up to 30 days after the initial decision is made. 
        :type since_date: str
        :param status: **Status**: Filter by status.  If no value is specified, the default returns all to include both active and inactive workflows.  Note: Any workflows at a current stage of Complete or Cancelled are inactive. Ongoing workflows currently at other stages are active. 
        :type status: str
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
        :rtype: tuple(WorkflowInstancesResponseGet, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'include_comments',
            'include_decommission_systems',
            'page_index',
            'since_date',
            'status'
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
                    " to method get_system_workflow_instances" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats: Dict[str, str] = {}

        # process the path parameters
        _path_params: Dict[str, str] = {}

        # process the query parameters
        _query_params: List[Tuple[str, str]] = []
        if _params.get('include_comments') is not None:  # noqa: E501
            _query_params.append(('includeComments', _params['include_comments']))

        if _params.get('include_decommission_systems') is not None:  # noqa: E501
            _query_params.append(('includeDecommissionSystems', _params['include_decommission_systems']))

        if _params.get('page_index') is not None:  # noqa: E501
            _query_params.append(('pageIndex', _params['page_index']))

        if _params.get('since_date') is not None:  # noqa: E501
            _query_params.append(('sinceDate', _params['since_date']))

        if _params.get('status') is not None:  # noqa: E501
            _query_params.append(('status', _params['status']))

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
            '200': "WorkflowInstancesResponseGet",
            '400': "Response400",
            '401': "Response401",
            '403': "Response403",
            '404': "Response404",
            '405': "Response405",
            '490': "Response490",
            '500': "Response500",
        }

        return self.api_client.call_api(
            '/api/workflows/instances', 'GET',
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
    def get_system_workflow_instances_by_workflow_instance_id(
        self,
        workflow_instance_id: Annotated[StrictInt, Field(description="**Workflow Instance Id**: The unique workflow definition identifier.")],
        **kwargs,
    ) -> WorkflowInstanceResponseGet:
        """Get workflow instance by ID  # noqa: E501

        View detailed historical workflow information for `workflowInstanceId`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_system_workflow_instances_by_workflow_instance_id(workflow_instance_id, async_req=True)
        >>> result = thread.get()

        :param workflow_instance_id: **Workflow Instance Id**: The unique workflow definition identifier. (required)
        :type workflow_instance_id: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: WorkflowInstanceResponseGet
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_system_workflow_instances_by_workflow_instance_id_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_system_workflow_instances_by_workflow_instance_id_with_http_info(workflow_instance_id, **kwargs)  # noqa: E501

    @validate_call
    def get_system_workflow_instances_by_workflow_instance_id_with_http_info(
        self,
        workflow_instance_id: Annotated[StrictInt, Field(description="**Workflow Instance Id**: The unique workflow definition identifier.")],
        **kwargs,
    ) -> ApiResponse:
        """Get workflow instance by ID  # noqa: E501

        View detailed historical workflow information for `workflowInstanceId`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_system_workflow_instances_by_workflow_instance_id_with_http_info(workflow_instance_id, async_req=True)
        >>> result = thread.get()

        :param workflow_instance_id: **Workflow Instance Id**: The unique workflow definition identifier. (required)
        :type workflow_instance_id: int
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
        :rtype: tuple(WorkflowInstanceResponseGet, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'workflow_instance_id'
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
                    " to method get_system_workflow_instances_by_workflow_instance_id" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats: Dict[str, str] = {}

        # process the path parameters
        _path_params: Dict[str, str] = {}
        if _params['workflow_instance_id'] is not None:
            _path_params['workflowInstanceId'] = _params['workflow_instance_id']


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
            '200': "WorkflowInstanceResponseGet",
            '400': "Response400",
            '401': "Response401",
            '403': "Response403",
            '404': "Response404",
            '405': "Response405",
            '490': "Response490",
            '500': "Response500",
        }

        return self.api_client.call_api(
            '/api/workflows/instances/{workflowInstanceId}', 'GET',
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
