# emass_client.SystemA20SummaryDashboardApi

All URIs are relative to *http://localhost:4010*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_va_system_a2_summary**](SystemA20SummaryDashboardApi.md#get_va_system_a2_summary) | **GET** /api/dashboards/va-system-a2-summary | VA System A2.0 Summary


# **get_va_system_a2_summary**
> object get_va_system_a2_summary(org_id, excludeinherited=excludeinherited, page_index=page_index, page_size=page_size)

VA System A2.0 Summary

Get VA system A2.0 summary dashboard information.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (mockType):
* Api Key Authentication (userId):
```python
import time
import os
import emass_client
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
    api_instance = emass_client.SystemA20SummaryDashboardApi(api_client)
    org_id = 1 # int | **Organization Id**: The unique organization identifier.
    excludeinherited = False # bool | **Exclude Inherited**: If no value is specified, the default returns false to include inherited data.  (optional) (default to False)
    page_index = 0 # int | **Page Index**: If no value is specified, the default returns results from the first page with an index of 0.  (optional) (default to 0)
    page_size = 20000 # int | **Page Size**: If no value is specified, the default returns 20000 per page.  (optional) (default to 20000)

    try:
        # VA System A2.0 Summary
        api_response = api_instance.get_va_system_a2_summary(org_id, excludeinherited=excludeinherited, page_index=page_index, page_size=page_size)
        print("The response of SystemA20SummaryDashboardApi->get_va_system_a2_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemA20SummaryDashboardApi->get_va_system_a2_summary: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**| **Organization Id**: The unique organization identifier. | 
 **excludeinherited** | **bool**| **Exclude Inherited**: If no value is specified, the default returns false to include inherited data.  | [optional] [default to False]
 **page_index** | **int**| **Page Index**: If no value is specified, the default returns results from the first page with an index of 0.  | [optional] [default to 0]
 **page_size** | **int**| **Page Size**: If no value is specified, the default returns 20000 per page.  | [optional] [default to 20000]

### Return type

**object**

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

