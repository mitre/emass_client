<a id="__pageTop"></a>
# emass_client.apis.tags.workflow_definitions_api.WorkflowDefinitionsApi

All URIs are relative to *http://localhost:4010*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_workflow_definitions**](#get_workflow_definitions) | **get** /api/workflows/definitions | Get workflow definitions in a site

# **get_workflow_definitions**
<a id="get_workflow_definitions"></a>
> WorkflowDefinitionResponseGet get_workflow_definitions()

Get workflow definitions in a site

View all workflow schemas available on the eMASS instance filtered by  status `includeInactive` and registration type `registrationType`.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (mockType):
* Api Key Authentication (userId):
```python
import emass_client
from emass_client.apis.tags import workflow_definitions_api
from emass_client.model.response490 import Response490
from emass_client.model.workflow_definition_response_get import WorkflowDefinitionResponseGet
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
    api_instance = workflow_definitions_api.WorkflowDefinitionsApi(api_client)

    # example passing only optional values
    query_params = {
        'includeInactive': True,
        'registrationType': "regular",
    }
    try:
        # Get workflow definitions in a site
        api_response = api_instance.get_workflow_definitions(
            query_params=query_params,
        )
        pprint(api_response)
    except emass_client.ApiException as e:
        print("Exception when calling WorkflowDefinitionsApi->get_workflow_definitions: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
includeInactive | IncludeInactiveSchema | | optional
registrationType | RegistrationTypeSchema | | optional


# IncludeInactiveSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of True

# RegistrationTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | if omitted the server will use the default value of "regular"

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_workflow_definitions.ApiResponseFor200) | Successful response
400 | [ApiResponseFor400](#get_workflow_definitions.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#get_workflow_definitions.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#get_workflow_definitions.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_workflow_definitions.ApiResponseFor404) | Not Found
405 | [ApiResponseFor405](#get_workflow_definitions.ApiResponseFor405) | Method Not Allowed
490 | [ApiResponseFor490](#get_workflow_definitions.ApiResponseFor490) | API Rule Failed
500 | [ApiResponseFor500](#get_workflow_definitions.ApiResponseFor500) | Internal Server Error

#### get_workflow_definitions.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**WorkflowDefinitionResponseGet**](../../models/WorkflowDefinitionResponseGet.md) |  | 


#### get_workflow_definitions.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Response400**](../../models/Response400.md) |  | 


#### get_workflow_definitions.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Response401**](../../models/Response401.md) |  | 


#### get_workflow_definitions.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Response403**](../../models/Response403.md) |  | 


#### get_workflow_definitions.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Response404**](../../models/Response404.md) |  | 


#### get_workflow_definitions.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor405ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor405ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Response405**](../../models/Response405.md) |  | 


#### get_workflow_definitions.ApiResponseFor490
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor490ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor490ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Response490**](../../models/Response490.md) |  | 


#### get_workflow_definitions.ApiResponseFor500
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

