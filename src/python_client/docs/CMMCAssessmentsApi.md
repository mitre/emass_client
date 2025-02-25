# emass_client.CMMCAssessmentsApi

All URIs are relative to *http://localhost:4010*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_cmmc_assessments**](CMMCAssessmentsApi.md#get_cmmc_assessments) | **GET** /api/cmmc-assessments | Get CMMC assessment information


# **get_cmmc_assessments**
> CmmcResponseGet get_cmmc_assessments(since_date)

Get CMMC assessment information

Get all CMMC assessment after the given date `sinceDate` parameter. It is available
to CMMC eMASS only.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (mockType):
* Api Key Authentication (userId):

```python
import emass_client
from emass_client.models.cmmc_response_get import CmmcResponseGet
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
    api_instance = emass_client.CMMCAssessmentsApi(api_client)
    since_date = '1638764040' # str | **Date** CMMC date (Unix date format)

    try:
        # Get CMMC assessment information
        api_response = api_instance.get_cmmc_assessments(since_date)
        print("The response of CMMCAssessmentsApi->get_cmmc_assessments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CMMCAssessmentsApi->get_cmmc_assessments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **since_date** | **str**| **Date** CMMC date (Unix date format) | 

### Return type

[**CmmcResponseGet**](CmmcResponseGet.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**405** | Method Not Allowed |  -  |
**490** | API Rule Failed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

