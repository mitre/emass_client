# emass_client.CoastGuardSystemFISMAMetricsDashboardApi

All URIs are relative to *http://localhost:4010*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_coast_guard_system_fisma_metrics**](CoastGuardSystemFISMAMetricsDashboardApi.md#get_coast_guard_system_fisma_metrics) | **GET** /api/dashboards/coastguard-system-fisma-metrics | Coast Guard System FISMA Metrics


# **get_coast_guard_system_fisma_metrics**
> GetSystemStatusDetails200Response get_coast_guard_system_fisma_metrics(org_id, excludeinherited=excludeinherited, page_index=page_index, page_size=page_size)

Coast Guard System FISMA Metrics

Get Coast Guard system FISMA metrics dashboard information.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (mockType):
* Api Key Authentication (userId):

```python
import emass_client
from emass_client.models.get_system_status_details200_response import GetSystemStatusDetails200Response
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
    api_instance = emass_client.CoastGuardSystemFISMAMetricsDashboardApi(api_client)
    org_id = 1 # int | **Organization Id**: The unique organization identifier.
    excludeinherited = False # bool | **Exclude Inherited**: If no value is specified, the default returns false to include inherited data.  (optional) (default to False)
    page_index = 0 # int | **Page Index**: If no value is specified, the default returns results from the first page with an index of 0.  (optional) (default to 0)
    page_size = 20000 # int | **Page Size**: If no value is specified, the default returns 20000 per page.  (optional) (default to 20000)

    try:
        # Coast Guard System FISMA Metrics
        api_response = api_instance.get_coast_guard_system_fisma_metrics(org_id, excludeinherited=excludeinherited, page_index=page_index, page_size=page_size)
        print("The response of CoastGuardSystemFISMAMetricsDashboardApi->get_coast_guard_system_fisma_metrics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoastGuardSystemFISMAMetricsDashboardApi->get_coast_guard_system_fisma_metrics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**| **Organization Id**: The unique organization identifier. | 
 **excludeinherited** | **bool**| **Exclude Inherited**: If no value is specified, the default returns false to include inherited data.  | [optional] [default to False]
 **page_index** | **int**| **Page Index**: If no value is specified, the default returns results from the first page with an index of 0.  | [optional] [default to 0]
 **page_size** | **int**| **Page Size**: If no value is specified, the default returns 20000 per page.  | [optional] [default to 20000]

### Return type

[**GetSystemStatusDetails200Response**](GetSystemStatusDetails200Response.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Pagination response schema |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**405** | Method Not Allowed |  -  |
**490** | API Rule Failed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

