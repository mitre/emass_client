<a id="__pageTop"></a>
# emass_client.apis.tags.milestones_api.MilestonesApi

All URIs are relative to *http://localhost:4010*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_milestone_by_system_id_and_poam_id**](#add_milestone_by_system_id_and_poam_id) | **post** /api/systems/{systemId}/poams/{poamId}/milestones | Add milestones to one or many POA&amp;M items in a system
[**delete_milestone**](#delete_milestone) | **delete** /api/systems/{systemId}/poams/{poamId}/milestones | Remove milestones in a system for one or many POA&amp;M items
[**get_system_milestones_by_poam_id**](#get_system_milestones_by_poam_id) | **get** /api/systems/{systemId}/poams/{poamId}/milestones | Get milestones in one or many POA&amp;M items in a system
[**get_system_milestones_by_poam_id_and_milestone_id**](#get_system_milestones_by_poam_id_and_milestone_id) | **get** /api/systems/{systemId}/poams/{poamId}/milestones/{milestoneId} | Get milestone by ID in POA&amp;M item in a system
[**update_milestone_by_system_id_and_poam_id**](#update_milestone_by_system_id_and_poam_id) | **put** /api/systems/{systemId}/poams/{poamId}/milestones | Update one or many POA&amp;M items in a system

# **add_milestone_by_system_id_and_poam_id**
<a id="add_milestone_by_system_id_and_poam_id"></a>
> MilestoneResponsePost add_milestone_by_system_id_and_poam_id(system_idpoam_idmilestones_request_post_body)

Add milestones to one or many POA&M items in a system

Adds a milestone for given `systemId` and `poamId` path parameters  **Request Body Required Fields** - `description` - `scheduledCompletionDate`

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (mockType):
* Api Key Authentication (userId):
```python
import emass_client
from emass_client.apis.tags import milestones_api
from emass_client.model.response400 import Response400
from emass_client.model.milestone_response_post import MilestoneResponsePost
from emass_client.model.response401 import Response401
from emass_client.model.response201 import Response201
from emass_client.model.response500 import Response500
from emass_client.model.response403 import Response403
from emass_client.model.response405 import Response405
from emass_client.model.milestones_request_post_body import MilestonesRequestPostBody
from emass_client.model.response404 import Response404
from emass_client.model.response411 import Response411
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:4010
# See configuration.py for a list of all supported configuration parameters.
configuration = emass_client.Configuration(
    host = "http://localhost:4010"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: mockType
configuration.api_key['mockType'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['mockType'] = 'Bearer'

# Configure API key authorization: userId
configuration.api_key['userId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userId'] = 'Bearer'
# Enter a context with an instance of the API client
with emass_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = milestones_api.MilestonesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'systemId': 35,
        'poamId': 45,
    }
    body = MilestonesRequestPostBody([
        None
    ])
    try:
        # Add milestones to one or many POA&M items in a system
        api_response = api_instance.add_milestone_by_system_id_and_poam_id(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except emass_client.ApiException as e:
        print("Exception when calling MilestonesApi->add_milestone_by_system_id_and_poam_id: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**MilestonesRequestPostBody**](../../models/MilestonesRequestPostBody.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
systemId | SystemIdSchema | | 
poamId | PoamIdSchema | | 

# SystemIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# PoamIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#add_milestone_by_system_id_and_poam_id.ApiResponseFor200) | Successful response
201 | [ApiResponseFor201](#add_milestone_by_system_id_and_poam_id.ApiResponseFor201) | Created
400 | [ApiResponseFor400](#add_milestone_by_system_id_and_poam_id.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#add_milestone_by_system_id_and_poam_id.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#add_milestone_by_system_id_and_poam_id.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#add_milestone_by_system_id_and_poam_id.ApiResponseFor404) | Not Found
405 | [ApiResponseFor405](#add_milestone_by_system_id_and_poam_id.ApiResponseFor405) | Method Not Allowed
411 | [ApiResponseFor411](#add_milestone_by_system_id_and_poam_id.ApiResponseFor411) | Length Required
500 | [ApiResponseFor500](#add_milestone_by_system_id_and_poam_id.ApiResponseFor500) | Internal Server Error

#### add_milestone_by_system_id_and_poam_id.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**MilestoneResponsePost**](../../models/MilestoneResponsePost.md) |  | 


#### add_milestone_by_system_id_and_poam_id.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Response201**](../../models/Response201.md) |  | 


#### add_milestone_by_system_id_and_poam_id.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Response400**](../../models/Response400.md) |  | 


#### add_milestone_by_system_id_and_poam_id.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Response401**](../../models/Response401.md) |  | 


#### add_milestone_by_system_id_and_poam_id.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Response403**](../../models/Response403.md) |  | 


#### add_milestone_by_system_id_and_poam_id.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Response404**](../../models/Response404.md) |  | 


#### add_milestone_by_system_id_and_poam_id.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor405ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor405ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Response405**](../../models/Response405.md) |  | 


#### add_milestone_by_system_id_and_poam_id.ApiResponseFor411
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor411ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor411ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Response411**](../../models/Response411.md) |  | 


#### add_milestone_by_system_id_and_poam_id.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Response500**](../../models/Response500.md) |  | 


### Authorization

[apiKey](../../../README.md#apiKey), [mockType](../../../README.md#mockType), [userId](../../../README.md#userId)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_milestone**
<a id="delete_milestone"></a>
> MilestonesPutPostDelete delete_milestone(system_idpoam_idmilestones_request_delete_body)

Remove milestones in a system for one or many POA&M items

Remove the POA&M matching `systemId` and `poamId` for path parameters and `milstoneId` provide in the Requst Body  **Notes**<br> To delete a milestone the record must be inactive by having the field isActive set to false (`isActive=false`).

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (mockType):
* Api Key Authentication (userId):
```python
import emass_client
from emass_client.apis.tags import milestones_api
from emass_client.model.response400 import Response400
from emass_client.model.response401 import Response401
from emass_client.model.milestones_request_delete_body import MilestonesRequestDeleteBody
from emass_client.model.response500 import Response500
from emass_client.model.response403 import Response403
from emass_client.model.response404 import Response404
from emass_client.model.milestones_put_post_delete import MilestonesPutPostDelete
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:4010
# See configuration.py for a list of all supported configuration parameters.
configuration = emass_client.Configuration(
    host = "http://localhost:4010"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: mockType
configuration.api_key['mockType'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['mockType'] = 'Bearer'

# Configure API key authorization: userId
configuration.api_key['userId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userId'] = 'Bearer'
# Enter a context with an instance of the API client
with emass_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = milestones_api.MilestonesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'systemId': 35,
        'poamId': 45,
    }
    body = MilestonesRequestDeleteBody([
        dict(
            milestone_id=19,
        )
    ])
    try:
        # Remove milestones in a system for one or many POA&M items
        api_response = api_instance.delete_milestone(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except emass_client.ApiException as e:
        print("Exception when calling MilestonesApi->delete_milestone: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**MilestonesRequestDeleteBody**](../../models/MilestonesRequestDeleteBody.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
systemId | SystemIdSchema | | 
poamId | PoamIdSchema | | 

# SystemIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# PoamIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#delete_milestone.ApiResponseFor200) | Successful operation
400 | [ApiResponseFor400](#delete_milestone.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#delete_milestone.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#delete_milestone.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#delete_milestone.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#delete_milestone.ApiResponseFor500) | Internal Server Error

#### delete_milestone.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**MilestonesPutPostDelete**](../../models/MilestonesPutPostDelete.md) |  | 


#### delete_milestone.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Response400**](../../models/Response400.md) |  | 


#### delete_milestone.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Response401**](../../models/Response401.md) |  | 


#### delete_milestone.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Response403**](../../models/Response403.md) |  | 


#### delete_milestone.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Response404**](../../models/Response404.md) |  | 


#### delete_milestone.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Response500**](../../models/Response500.md) |  | 


### Authorization

[apiKey](../../../README.md#apiKey), [mockType](../../../README.md#mockType), [userId](../../../README.md#userId)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_system_milestones_by_poam_id**
<a id="get_system_milestones_by_poam_id"></a>
> MilestoneResponseGet get_system_milestones_by_poam_id(system_idpoam_id)

Get milestones in one or many POA&M items in a system

Returns system containing milestones for matching parameters.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (mockType):
* Api Key Authentication (userId):
```python
import emass_client
from emass_client.apis.tags import milestones_api
from emass_client.model.response490 import Response490
from emass_client.model.milestone_response_get import MilestoneResponseGet
from emass_client.model.response400 import Response400
from emass_client.model.response401 import Response401
from emass_client.model.response500 import Response500
from emass_client.model.response403 import Response403
from emass_client.model.response405 import Response405
from emass_client.model.response404 import Response404
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:4010
# See configuration.py for a list of all supported configuration parameters.
configuration = emass_client.Configuration(
    host = "http://localhost:4010"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: mockType
configuration.api_key['mockType'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['mockType'] = 'Bearer'

# Configure API key authorization: userId
configuration.api_key['userId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userId'] = 'Bearer'
# Enter a context with an instance of the API client
with emass_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = milestones_api.MilestonesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'systemId': 35,
        'poamId': 45,
    }
    query_params = {
    }
    try:
        # Get milestones in one or many POA&M items in a system
        api_response = api_instance.get_system_milestones_by_poam_id(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except emass_client.ApiException as e:
        print("Exception when calling MilestonesApi->get_system_milestones_by_poam_id: %s\n" % e)

    # example passing only optional values
    path_params = {
        'systemId': 35,
        'poamId': 45,
    }
    query_params = {
        'scheduledCompletionDateStart': "scheduledCompletionDateStart_example",
        'scheduledCompletionDateEnd': "scheduledCompletionDateEnd_example",
    }
    try:
        # Get milestones in one or many POA&M items in a system
        api_response = api_instance.get_system_milestones_by_poam_id(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except emass_client.ApiException as e:
        print("Exception when calling MilestonesApi->get_system_milestones_by_poam_id: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
scheduledCompletionDateStart | ScheduledCompletionDateStartSchema | | optional
scheduledCompletionDateEnd | ScheduledCompletionDateEndSchema | | optional


# ScheduledCompletionDateStartSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ScheduledCompletionDateEndSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
systemId | SystemIdSchema | | 
poamId | PoamIdSchema | | 

# SystemIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# PoamIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_system_milestones_by_poam_id.ApiResponseFor200) | Successful response
400 | [ApiResponseFor400](#get_system_milestones_by_poam_id.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#get_system_milestones_by_poam_id.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#get_system_milestones_by_poam_id.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_system_milestones_by_poam_id.ApiResponseFor404) | Not Found
405 | [ApiResponseFor405](#get_system_milestones_by_poam_id.ApiResponseFor405) | Method Not Allowed
490 | [ApiResponseFor490](#get_system_milestones_by_poam_id.ApiResponseFor490) | API Rule Failed
500 | [ApiResponseFor500](#get_system_milestones_by_poam_id.ApiResponseFor500) | Internal Server Error

#### get_system_milestones_by_poam_id.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**MilestoneResponseGet**](../../models/MilestoneResponseGet.md) |  | 


#### get_system_milestones_by_poam_id.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Response400**](../../models/Response400.md) |  | 


#### get_system_milestones_by_poam_id.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Response401**](../../models/Response401.md) |  | 


#### get_system_milestones_by_poam_id.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Response403**](../../models/Response403.md) |  | 


#### get_system_milestones_by_poam_id.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Response404**](../../models/Response404.md) |  | 


#### get_system_milestones_by_poam_id.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor405ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor405ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Response405**](../../models/Response405.md) |  | 


#### get_system_milestones_by_poam_id.ApiResponseFor490
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor490ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor490ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Response490**](../../models/Response490.md) |  | 


#### get_system_milestones_by_poam_id.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Response500**](../../models/Response500.md) |  | 


### Authorization

[apiKey](../../../README.md#apiKey), [mockType](../../../README.md#mockType), [userId](../../../README.md#userId)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_system_milestones_by_poam_id_and_milestone_id**
<a id="get_system_milestones_by_poam_id_and_milestone_id"></a>
> MilestoneResponseGetMilestone get_system_milestones_by_poam_id_and_milestone_id(system_idpoam_idmilestone_id)

Get milestone by ID in POA&M item in a system

Returns systems containing milestones for matching parameters.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (mockType):
* Api Key Authentication (userId):
```python
import emass_client
from emass_client.apis.tags import milestones_api
from emass_client.model.milestone_response_get_milestone import MilestoneResponseGetMilestone
from emass_client.model.response490 import Response490
from emass_client.model.response400 import Response400
from emass_client.model.response401 import Response401
from emass_client.model.response500 import Response500
from emass_client.model.response403 import Response403
from emass_client.model.response405 import Response405
from emass_client.model.response404 import Response404
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:4010
# See configuration.py for a list of all supported configuration parameters.
configuration = emass_client.Configuration(
    host = "http://localhost:4010"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: mockType
configuration.api_key['mockType'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['mockType'] = 'Bearer'

# Configure API key authorization: userId
configuration.api_key['userId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userId'] = 'Bearer'
# Enter a context with an instance of the API client
with emass_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = milestones_api.MilestonesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'systemId': 35,
        'poamId': 45,
        'milestoneId': 77,
    }
    try:
        # Get milestone by ID in POA&M item in a system
        api_response = api_instance.get_system_milestones_by_poam_id_and_milestone_id(
            path_params=path_params,
        )
        pprint(api_response)
    except emass_client.ApiException as e:
        print("Exception when calling MilestonesApi->get_system_milestones_by_poam_id_and_milestone_id: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
systemId | SystemIdSchema | | 
poamId | PoamIdSchema | | 
milestoneId | MilestoneIdSchema | | 

# SystemIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# PoamIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# MilestoneIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_system_milestones_by_poam_id_and_milestone_id.ApiResponseFor200) | Successful response
400 | [ApiResponseFor400](#get_system_milestones_by_poam_id_and_milestone_id.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#get_system_milestones_by_poam_id_and_milestone_id.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#get_system_milestones_by_poam_id_and_milestone_id.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_system_milestones_by_poam_id_and_milestone_id.ApiResponseFor404) | Not Found
405 | [ApiResponseFor405](#get_system_milestones_by_poam_id_and_milestone_id.ApiResponseFor405) | Method Not Allowed
490 | [ApiResponseFor490](#get_system_milestones_by_poam_id_and_milestone_id.ApiResponseFor490) | API Rule Failed
500 | [ApiResponseFor500](#get_system_milestones_by_poam_id_and_milestone_id.ApiResponseFor500) | Internal Server Error

#### get_system_milestones_by_poam_id_and_milestone_id.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**MilestoneResponseGetMilestone**](../../models/MilestoneResponseGetMilestone.md) |  | 


#### get_system_milestones_by_poam_id_and_milestone_id.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Response400**](../../models/Response400.md) |  | 


#### get_system_milestones_by_poam_id_and_milestone_id.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Response401**](../../models/Response401.md) |  | 


#### get_system_milestones_by_poam_id_and_milestone_id.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Response403**](../../models/Response403.md) |  | 


#### get_system_milestones_by_poam_id_and_milestone_id.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Response404**](../../models/Response404.md) |  | 


#### get_system_milestones_by_poam_id_and_milestone_id.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor405ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor405ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Response405**](../../models/Response405.md) |  | 


#### get_system_milestones_by_poam_id_and_milestone_id.ApiResponseFor490
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor490ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor490ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Response490**](../../models/Response490.md) |  | 


#### get_system_milestones_by_poam_id_and_milestone_id.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Response500**](../../models/Response500.md) |  | 


### Authorization

[apiKey](../../../README.md#apiKey), [mockType](../../../README.md#mockType), [userId](../../../README.md#userId)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_milestone_by_system_id_and_poam_id**
<a id="update_milestone_by_system_id_and_poam_id"></a>
> MilestoneResponsePut update_milestone_by_system_id_and_poam_id(system_idpoam_idmilestones_request_put_body)

Update one or many POA&M items in a system

Updates a milestone for given `systemId` and `poamId` path parameters  **Request Body Required Fields** - `milestoneId` - `description` - `scheduledCompletionDate`

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (mockType):
* Api Key Authentication (userId):
```python
import emass_client
from emass_client.apis.tags import milestones_api
from emass_client.model.response400 import Response400
from emass_client.model.milestones_request_put_body import MilestonesRequestPutBody
from emass_client.model.response401 import Response401
from emass_client.model.response500 import Response500
from emass_client.model.response403 import Response403
from emass_client.model.response404 import Response404
from emass_client.model.milestone_response_put import MilestoneResponsePut
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:4010
# See configuration.py for a list of all supported configuration parameters.
configuration = emass_client.Configuration(
    host = "http://localhost:4010"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: mockType
configuration.api_key['mockType'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['mockType'] = 'Bearer'

# Configure API key authorization: userId
configuration.api_key['userId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userId'] = 'Bearer'
# Enter a context with an instance of the API client
with emass_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = milestones_api.MilestonesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'systemId': 35,
        'poamId': 45,
    }
    body = MilestonesRequestPutBody([
        None
    ])
    try:
        # Update one or many POA&M items in a system
        api_response = api_instance.update_milestone_by_system_id_and_poam_id(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except emass_client.ApiException as e:
        print("Exception when calling MilestonesApi->update_milestone_by_system_id_and_poam_id: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**MilestonesRequestPutBody**](../../models/MilestonesRequestPutBody.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
systemId | SystemIdSchema | | 
poamId | PoamIdSchema | | 

# SystemIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# PoamIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_milestone_by_system_id_and_poam_id.ApiResponseFor200) | Successful operation
400 | [ApiResponseFor400](#update_milestone_by_system_id_and_poam_id.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#update_milestone_by_system_id_and_poam_id.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#update_milestone_by_system_id_and_poam_id.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#update_milestone_by_system_id_and_poam_id.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#update_milestone_by_system_id_and_poam_id.ApiResponseFor500) | Internal Server Error

#### update_milestone_by_system_id_and_poam_id.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**MilestoneResponsePut**](../../models/MilestoneResponsePut.md) |  | 


#### update_milestone_by_system_id_and_poam_id.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Response400**](../../models/Response400.md) |  | 


#### update_milestone_by_system_id_and_poam_id.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Response401**](../../models/Response401.md) |  | 


#### update_milestone_by_system_id_and_poam_id.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Response403**](../../models/Response403.md) |  | 


#### update_milestone_by_system_id_and_poam_id.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Response404**](../../models/Response404.md) |  | 


#### update_milestone_by_system_id_and_poam_id.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Response500**](../../models/Response500.md) |  | 


### Authorization

[apiKey](../../../README.md#apiKey), [mockType](../../../README.md#mockType), [userId](../../../README.md#userId)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

