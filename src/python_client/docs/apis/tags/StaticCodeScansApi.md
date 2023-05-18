<a id="__pageTop"></a>
# emass_client.apis.tags.static_code_scans_api.StaticCodeScansApi

All URIs are relative to *http://localhost:4010*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_static_code_scans_by_system_id**](#add_static_code_scans_by_system_id) | **post** /api/systems/{systemId}/static-code-scans | Upload static code scans or Clear static code scans

# **add_static_code_scans_by_system_id**
<a id="add_static_code_scans_by_system_id"></a>
> StaticCodeResponsePost add_static_code_scans_by_system_id(system_idstatic_code_request_post_body)

Upload static code scans or Clear static code scans

Upload or clear application scan findings into a system's `systemId` assets module.  **Note:** To clear an application's findings, use only the field `clearFindings` as the Request body and set it to true. Example:  ``` [    {      \"application\": {        \"applicationName\": \"Artemis\",        \"version\": \"Version 5.0\"      },      \"applicationFindings\": [        { \"clearFindings\": true }      ]    }  ] ```

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (mockType):
* Api Key Authentication (userId):
```python
import emass_client
from emass_client.apis.tags import static_code_scans_api
from emass_client.model.response400 import Response400
from emass_client.model.response401 import Response401
from emass_client.model.static_code_response_post import StaticCodeResponsePost
from emass_client.model.response201 import Response201
from emass_client.model.response500 import Response500
from emass_client.model.response403 import Response403
from emass_client.model.response405 import Response405
from emass_client.model.response404 import Response404
from emass_client.model.response411 import Response411
from emass_client.model.static_code_request_post_body import StaticCodeRequestPostBody
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
    api_instance = static_code_scans_api.StaticCodeScansApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'systemId': 35,
    }
    body = StaticCodeRequestPostBody(
        application=dict(
            application_name="Artemis",
            version="Version 5.0",
        ),
        application_findings=[
            StaticCodeApplication(
                raw_severity="Moderate",
                code_check_name="Hidden Field",
                count=14,
                scan_date=1625070000,
                cwe_id="155",
                clear_findings=False,
            )
        ],
    )
    try:
        # Upload static code scans or Clear static code scans
        api_response = api_instance.add_static_code_scans_by_system_id(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except emass_client.ApiException as e:
        print("Exception when calling StaticCodeScansApi->add_static_code_scans_by_system_id: %s\n" % e)
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
[**StaticCodeRequestPostBody**](../../models/StaticCodeRequestPostBody.md) |  | 


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
200 | [ApiResponseFor200](#add_static_code_scans_by_system_id.ApiResponseFor200) | Successful response
201 | [ApiResponseFor201](#add_static_code_scans_by_system_id.ApiResponseFor201) | Created
400 | [ApiResponseFor400](#add_static_code_scans_by_system_id.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#add_static_code_scans_by_system_id.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#add_static_code_scans_by_system_id.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#add_static_code_scans_by_system_id.ApiResponseFor404) | Not Found
405 | [ApiResponseFor405](#add_static_code_scans_by_system_id.ApiResponseFor405) | Method Not Allowed
411 | [ApiResponseFor411](#add_static_code_scans_by_system_id.ApiResponseFor411) | Length Required
500 | [ApiResponseFor500](#add_static_code_scans_by_system_id.ApiResponseFor500) | Internal Server Error

#### add_static_code_scans_by_system_id.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**StaticCodeResponsePost**](../../models/StaticCodeResponsePost.md) |  | 


#### add_static_code_scans_by_system_id.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Response201**](../../models/Response201.md) |  | 


#### add_static_code_scans_by_system_id.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Response400**](../../models/Response400.md) |  | 


#### add_static_code_scans_by_system_id.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Response401**](../../models/Response401.md) |  | 


#### add_static_code_scans_by_system_id.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Response403**](../../models/Response403.md) |  | 


#### add_static_code_scans_by_system_id.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Response404**](../../models/Response404.md) |  | 


#### add_static_code_scans_by_system_id.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor405ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor405ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Response405**](../../models/Response405.md) |  | 


#### add_static_code_scans_by_system_id.ApiResponseFor411
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor411ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor411ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Response411**](../../models/Response411.md) |  | 


#### add_static_code_scans_by_system_id.ApiResponseFor500
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

