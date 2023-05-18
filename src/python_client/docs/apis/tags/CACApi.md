<a id="__pageTop"></a>
# emass_client.apis.tags.cac_api.CACApi

All URIs are relative to *http://localhost:4010*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_system_cac**](#add_system_cac) | **post** /api/systems/{systemId}/approval/cac | Submit control to second role of CAC
[**get_system_cac**](#get_system_cac) | **get** /api/systems/{systemId}/approval/cac | Get location of one or many controls in CAC

# **add_system_cac**
<a id="add_system_cac"></a>
> CacResponsePost add_system_cac(system_idcac_request_post_body)

Submit control to second role of CAC

Adds a Control Approval Chain (CAC) for given `systemId` path parameter<br><br> POST requests will only yield successful results if the control is currently sitting at the first role of the CAC. If the control is not currently sitting at the first role, then an error will be returned.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (mockType):
* Api Key Authentication (userId):
```python
import emass_client
from emass_client.apis.tags import cac_api
from emass_client.model.response400 import Response400
from emass_client.model.response401 import Response401
from emass_client.model.cac_response_post import CacResponsePost
from emass_client.model.response201 import Response201
from emass_client.model.response500 import Response500
from emass_client.model.response403 import Response403
from emass_client.model.response405 import Response405
from emass_client.model.cac_request_post_body import CacRequestPostBody
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
    api_instance = cac_api.CACApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'systemId': 35,
    }
    body = CacRequestPostBody([
        None
    ])
    try:
        # Submit control to second role of CAC
        api_response = api_instance.add_system_cac(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except emass_client.ApiException as e:
        print("Exception when calling CACApi->add_system_cac: %s\n" % e)
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
[**CacRequestPostBody**](../../models/CacRequestPostBody.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
systemId | SystemIdSchema | | 

# SystemIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#add_system_cac.ApiResponseFor200) | Successful response
201 | [ApiResponseFor201](#add_system_cac.ApiResponseFor201) | Created
400 | [ApiResponseFor400](#add_system_cac.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#add_system_cac.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#add_system_cac.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#add_system_cac.ApiResponseFor404) | Not Found
405 | [ApiResponseFor405](#add_system_cac.ApiResponseFor405) | Method Not Allowed
411 | [ApiResponseFor411](#add_system_cac.ApiResponseFor411) | Length Required
500 | [ApiResponseFor500](#add_system_cac.ApiResponseFor500) | Internal Server Error

#### add_system_cac.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CacResponsePost**](../../models/CacResponsePost.md) |  | 


#### add_system_cac.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Response201**](../../models/Response201.md) |  | 


#### add_system_cac.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Response400**](../../models/Response400.md) |  | 


#### add_system_cac.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Response401**](../../models/Response401.md) |  | 


#### add_system_cac.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Response403**](../../models/Response403.md) |  | 


#### add_system_cac.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Response404**](../../models/Response404.md) |  | 


#### add_system_cac.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor405ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor405ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Response405**](../../models/Response405.md) |  | 


#### add_system_cac.ApiResponseFor411
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor411ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor411ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Response411**](../../models/Response411.md) |  | 


#### add_system_cac.ApiResponseFor500
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

# **get_system_cac**
<a id="get_system_cac"></a>
> CacResponseGet get_system_cac(system_id)

Get location of one or many controls in CAC

Returns the location of a system's package in the Control Approval Chain (CAC) for matching `systemId` path parameter

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (mockType):
* Api Key Authentication (userId):
```python
import emass_client
from emass_client.apis.tags import cac_api
from emass_client.model.response490 import Response490
from emass_client.model.response400 import Response400
from emass_client.model.response401 import Response401
from emass_client.model.response500 import Response500
from emass_client.model.response403 import Response403
from emass_client.model.response405 import Response405
from emass_client.model.response404 import Response404
from emass_client.model.cac_response_get import CacResponseGet
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
    api_instance = cac_api.CACApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'systemId': 35,
    }
    query_params = {
    }
    try:
        # Get location of one or many controls in CAC
        api_response = api_instance.get_system_cac(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except emass_client.ApiException as e:
        print("Exception when calling CACApi->get_system_cac: %s\n" % e)

    # example passing only optional values
    path_params = {
        'systemId': 35,
    }
    query_params = {
        'controlAcronyms': "controlAcronyms_example",
    }
    try:
        # Get location of one or many controls in CAC
        api_response = api_instance.get_system_cac(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except emass_client.ApiException as e:
        print("Exception when calling CACApi->get_system_cac: %s\n" % e)
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
controlAcronyms | ControlAcronymsSchema | | optional


# ControlAcronymsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
systemId | SystemIdSchema | | 

# SystemIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_system_cac.ApiResponseFor200) | Successful response
400 | [ApiResponseFor400](#get_system_cac.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#get_system_cac.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#get_system_cac.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_system_cac.ApiResponseFor404) | Not Found
405 | [ApiResponseFor405](#get_system_cac.ApiResponseFor405) | Method Not Allowed
490 | [ApiResponseFor490](#get_system_cac.ApiResponseFor490) | API Rule Failed
500 | [ApiResponseFor500](#get_system_cac.ApiResponseFor500) | Internal Server Error

#### get_system_cac.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CacResponseGet**](../../models/CacResponseGet.md) |  | 


#### get_system_cac.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Response400**](../../models/Response400.md) |  | 


#### get_system_cac.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Response401**](../../models/Response401.md) |  | 


#### get_system_cac.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Response403**](../../models/Response403.md) |  | 


#### get_system_cac.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Response404**](../../models/Response404.md) |  | 


#### get_system_cac.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor405ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor405ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Response405**](../../models/Response405.md) |  | 


#### get_system_cac.ApiResponseFor490
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor490ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor490ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Response490**](../../models/Response490.md) |  | 


#### get_system_cac.ApiResponseFor500
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

