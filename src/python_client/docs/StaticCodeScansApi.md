# emass_client.StaticCodeScansApi

All URIs are relative to *http://localhost:4010*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_static_code_scans_by_system_id**](StaticCodeScansApi.md#add_static_code_scans_by_system_id) | **POST** /api/systems/{systemId}/static-code-scans | Upload static code scans or Clear static code scans


# **add_static_code_scans_by_system_id**
> StaticCodeResponsePost add_static_code_scans_by_system_id(system_id, static_code_request_post_body)

Upload static code scans or Clear static code scans

Upload or clear application scan findings into a system's `systemId` assets module.

**Request Body Required Fields**
- `application` (Object)
  - `applicationName`
  - `version`
- `applicationFindings` (Object Array)
  - `codeCheckName`
  - `count`
  - `scanDate`
  - `cweId`

**NOTE:** To clear an application's findings, use only the field `clearFindings` as
the Request body and set it to true. Example:
```
[
  {
    "application": {
      "applicationName": "application name",
      "version": "application version"
    },
    "applicationFindings": [
      { "clearFindings": true }
    ]
  }
]
```

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (mockType):
* Api Key Authentication (userId):

```python
import emass_client
from emass_client.models.static_code_request_post_body import StaticCodeRequestPostBody
from emass_client.models.static_code_response_post import StaticCodeResponsePost
from emass_client.rest import ApiException
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
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: mockType
configuration.api_key['mockType'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['mockType'] = 'Bearer'

# Configure API key authorization: userId
configuration.api_key['userId'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userId'] = 'Bearer'

# Enter a context with an instance of the API client
with emass_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = emass_client.StaticCodeScansApi(api_client)
    system_id = 35 # int | **System Id**: The unique system record identifier.
    static_code_request_post_body = emass_client.StaticCodeRequestPostBody() # StaticCodeRequestPostBody | Example request body for adding static code scans or Clear static code scans

    try:
        # Upload static code scans or Clear static code scans
        api_response = api_instance.add_static_code_scans_by_system_id(system_id, static_code_request_post_body)
        print("The response of StaticCodeScansApi->add_static_code_scans_by_system_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StaticCodeScansApi->add_static_code_scans_by_system_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **int**| **System Id**: The unique system record identifier. | 
 **static_code_request_post_body** | [**StaticCodeRequestPostBody**](StaticCodeRequestPostBody.md)| Example request body for adding static code scans or Clear static code scans | 

### Return type

[**StaticCodeResponsePost**](StaticCodeResponsePost.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**405** | Method Not Allowed |  -  |
**411** | Length Required |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

