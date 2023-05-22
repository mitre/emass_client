# emass_client.WorkflowDefinitionsApi

All URIs are relative to *http://localhost:4010*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_workflow_definitions**](WorkflowDefinitionsApi.md#get_workflow_definitions) | **GET** /api/workflows/definitions | Get workflow definitions in a site


# **get_workflow_definitions**
> WorkflowDefinitionResponseGet get_workflow_definitions(include_inactive=include_inactive, registration_type=registration_type)

Get workflow definitions in a site

View all workflow schemas available on the eMASS instance filtered by  status `includeInactive` and registration type `registrationType`.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (mockType):
* Api Key Authentication (userId):
```python
import time
import os
import emass_client
from emass_client.models.workflow_definition_response_get import WorkflowDefinitionResponseGet
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
    api_instance = emass_client.WorkflowDefinitionsApi(api_client)
    include_inactive = True # bool | **Include Inactive**: If no value is specified, the default returns false to not include outdated workflow definitions. (optional) (default to True)
    registration_type = 'regular' # str | **Registration Type**: Filter record by selected registration type (single value or comma delimited values).  *Available values:* assessAndAuthorize, assessOnly, guest, regular, functional, cloudServiceProvider, commonControlProvider   (optional) (default to 'regular')

    try:
        # Get workflow definitions in a site
        api_response = api_instance.get_workflow_definitions(include_inactive=include_inactive, registration_type=registration_type)
        print("The response of WorkflowDefinitionsApi->get_workflow_definitions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowDefinitionsApi->get_workflow_definitions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_inactive** | **bool**| **Include Inactive**: If no value is specified, the default returns false to not include outdated workflow definitions. | [optional] [default to True]
 **registration_type** | **str**| **Registration Type**: Filter record by selected registration type (single value or comma delimited values).  *Available values:* assessAndAuthorize, assessOnly, guest, regular, functional, cloudServiceProvider, commonControlProvider   | [optional] [default to &#39;regular&#39;]

### Return type

[**WorkflowDefinitionResponseGet**](WorkflowDefinitionResponseGet.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**405** | Method Not Allowed |  -  |
**490** | API Rule Failed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

