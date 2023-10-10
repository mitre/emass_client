# emass_client.TestResultsApi

All URIs are relative to *http://localhost:4010*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_test_results_by_system_id**](TestResultsApi.md#add_test_results_by_system_id) | **POST** /api/systems/{systemId}/test-results | Add one or many test results in a system
[**get_system_test_results**](TestResultsApi.md#get_system_test_results) | **GET** /api/systems/{systemId}/test-results | Get one or many test results in a system


# **add_test_results_by_system_id**
> TestResultsResponsePost add_test_results_by_system_id(system_id, request_body)

Add one or many test results in a system

Adds test results for given `systemId`  **Request Body Required Fields** - `testedBy` - `testDate` - `description` - `complianceStatus` - `assessmentProcedure`       

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (mockType):
* Api Key Authentication (userId):
```python
import time
import os
import emass_client
from emass_client.models.test_results_response_post import TestResultsResponsePost
from emass_client.models.object import object
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
    api_instance = emass_client.TestResultsApi(api_client)
    system_id = 35 # int | **System Id**: The unique system record identifier.
    request_body = None # List[object] | Add test results to a system (systemId)

    try:
        # Add one or many test results in a system
        api_response = api_instance.add_test_results_by_system_id(system_id, request_body)
        print("The response of TestResultsApi->add_test_results_by_system_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestResultsApi->add_test_results_by_system_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **int**| **System Id**: The unique system record identifier. | 
 **request_body** | [**List[object]**](object.md)| Add test results to a system (systemId) | 

### Return type

[**TestResultsResponsePost**](TestResultsResponsePost.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**405** | Method Not Allowed |  -  |
**411** | Length Required |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_test_results**
> TestResultsResponseGet get_system_test_results(system_id, control_acronyms=control_acronyms, assessment_procedures=assessment_procedures, ccis=ccis, latest_only=latest_only)

Get one or many test results in a system

Returns system test results information for matching parameters.<br>

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (mockType):
* Api Key Authentication (userId):
```python
import time
import os
import emass_client
from emass_client.models.test_results_response_get import TestResultsResponseGet
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
    api_instance = emass_client.TestResultsApi(api_client)
    system_id = 35 # int | **System Id**: The unique system record identifier.
    control_acronyms = 'control_acronyms_example' # str | **Control Acronym**: Filter query by given system acronym (single value or comma separated). (optional)
    assessment_procedures = 'assessment_procedures_example' # str | **Assessment Procedure**: Filter query by given Security Control Assessment Procedure (single value or comma separated). (optional)
    ccis = 'ccis_example' # str | **CCI System**: Filter query by Control Correlation Identifiers (CCIs) (single value or comma separated). (optional)
    latest_only = True # bool | **Latest Results Only**: Indicates that only the latest test resultes are retrieved. (optional) (default to True)

    try:
        # Get one or many test results in a system
        api_response = api_instance.get_system_test_results(system_id, control_acronyms=control_acronyms, assessment_procedures=assessment_procedures, ccis=ccis, latest_only=latest_only)
        print("The response of TestResultsApi->get_system_test_results:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestResultsApi->get_system_test_results: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **int**| **System Id**: The unique system record identifier. | 
 **control_acronyms** | **str**| **Control Acronym**: Filter query by given system acronym (single value or comma separated). | [optional] 
 **assessment_procedures** | **str**| **Assessment Procedure**: Filter query by given Security Control Assessment Procedure (single value or comma separated). | [optional] 
 **ccis** | **str**| **CCI System**: Filter query by Control Correlation Identifiers (CCIs) (single value or comma separated). | [optional] 
 **latest_only** | **bool**| **Latest Results Only**: Indicates that only the latest test resultes are retrieved. | [optional] [default to True]

### Return type

[**TestResultsResponseGet**](TestResultsResponseGet.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**405** | Method Not Allowed |  -  |
**490** | API Rule Failed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

