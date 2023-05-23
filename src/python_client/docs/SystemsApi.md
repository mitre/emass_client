# emass_client.SystemsApi

All URIs are relative to *http://localhost:4010*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_system**](SystemsApi.md#get_system) | **GET** /api/systems/{systemId} | Get system information for a specific system
[**get_systems**](SystemsApi.md#get_systems) | **GET** /api/systems | Get system information


# **get_system**
> SystemResponse get_system(system_id, include_package=include_package, policy=policy)

Get system information for a specific system

Returns the system matching provided parameters

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (mockType):
* Api Key Authentication (userId):
```python
import time
import os
import emass_client
from emass_client.models.system_response import SystemResponse
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
    api_instance = emass_client.SystemsApi(api_client)
    system_id = 35 # int | **System Id**: The unique system record identifier.
    include_package = True # bool | **Include Package**:  Indicates if additional packages information is retrieved for queried system. (optional) (default to True)
    policy = 'rmf' # str | **System Policy**: Filter query by system policy. If no value is specified and more than one policy is available, the default return is the RMF policy information. (optional) (default to 'rmf')

    try:
        # Get system information for a specific system
        api_response = api_instance.get_system(system_id, include_package=include_package, policy=policy)
        print("The response of SystemsApi->get_system:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemsApi->get_system: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **int**| **System Id**: The unique system record identifier. | 
 **include_package** | **bool**| **Include Package**:  Indicates if additional packages information is retrieved for queried system. | [optional] [default to True]
 **policy** | **str**| **System Policy**: Filter query by system policy. If no value is specified and more than one policy is available, the default return is the RMF policy information. | [optional] [default to &#39;rmf&#39;]

### Return type

[**SystemResponse**](SystemResponse.md)

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

# **get_systems**
> SystemsResponse get_systems(include_package=include_package, registration_type=registration_type, ditpr_id=ditpr_id, coams_id=coams_id, policy=policy, include_ditpr_metrics=include_ditpr_metrics, include_decommissioned=include_decommissioned, reports_for_scorecard=reports_for_scorecard)

Get system information

Returns all system(s) that match the query parameters

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (mockType):
* Api Key Authentication (userId):
```python
import time
import os
import emass_client
from emass_client.models.systems_response import SystemsResponse
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
    api_instance = emass_client.SystemsApi(api_client)
    include_package = True # bool | **Include Package**:  Indicates if additional packages information is retrieved for queried system. (optional) (default to True)
    registration_type = 'regular' # str | **Registration Type**: Filter record by selected registration type (single value or comma delimited values).  *Available values:* assessAndAuthorize, assessOnly, guest, regular, functional, cloudServiceProvider, commonControlProvider   (optional) (default to 'regular')
    ditpr_id = 'ditpr_id_example' # str | **DITPR ID**: Filter query by DoD Information Technology (IT) Portfolio Repository (DITPR). (optional)
    coams_id = 'coams_id_example' # str | **COAMS ID**: Filter query by Cyber Operational Attributes Management System (COAMS). (optional)
    policy = 'rmf' # str | **System Policy**: Filter query by system policy. If no value is specified and more than one policy is available, the default return is the RMF policy information. (optional) (default to 'rmf')
    include_ditpr_metrics = False # bool | **Include DITPR**: Indicates if DITPR metrics are retrieved. This query string parameter can only be used in conjunction with the following parameters:<br>   <ul>     <li>registrationType</li>     <li>policy</li>   </ul> (optional) (default to False)
    include_decommissioned = True # bool | **Include Decommissioned Systems**: Indicates if decommissioned systems are retrieved. If no value is specified, the default returns true to include decommissioned systems. (optional) (default to True)
    reports_for_scorecard = True # bool | **DoD Cyber Hygiene Scorecard**: Indicates if the system reports to the DoD Cyber Hygiene Scorecard. (optional) (default to True)

    try:
        # Get system information
        api_response = api_instance.get_systems(include_package=include_package, registration_type=registration_type, ditpr_id=ditpr_id, coams_id=coams_id, policy=policy, include_ditpr_metrics=include_ditpr_metrics, include_decommissioned=include_decommissioned, reports_for_scorecard=reports_for_scorecard)
        print("The response of SystemsApi->get_systems:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemsApi->get_systems: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_package** | **bool**| **Include Package**:  Indicates if additional packages information is retrieved for queried system. | [optional] [default to True]
 **registration_type** | **str**| **Registration Type**: Filter record by selected registration type (single value or comma delimited values).  *Available values:* assessAndAuthorize, assessOnly, guest, regular, functional, cloudServiceProvider, commonControlProvider   | [optional] [default to &#39;regular&#39;]
 **ditpr_id** | **str**| **DITPR ID**: Filter query by DoD Information Technology (IT) Portfolio Repository (DITPR). | [optional] 
 **coams_id** | **str**| **COAMS ID**: Filter query by Cyber Operational Attributes Management System (COAMS). | [optional] 
 **policy** | **str**| **System Policy**: Filter query by system policy. If no value is specified and more than one policy is available, the default return is the RMF policy information. | [optional] [default to &#39;rmf&#39;]
 **include_ditpr_metrics** | **bool**| **Include DITPR**: Indicates if DITPR metrics are retrieved. This query string parameter can only be used in conjunction with the following parameters:&lt;br&gt;   &lt;ul&gt;     &lt;li&gt;registrationType&lt;/li&gt;     &lt;li&gt;policy&lt;/li&gt;   &lt;/ul&gt; | [optional] [default to False]
 **include_decommissioned** | **bool**| **Include Decommissioned Systems**: Indicates if decommissioned systems are retrieved. If no value is specified, the default returns true to include decommissioned systems. | [optional] [default to True]
 **reports_for_scorecard** | **bool**| **DoD Cyber Hygiene Scorecard**: Indicates if the system reports to the DoD Cyber Hygiene Scorecard. | [optional] [default to True]

### Return type

[**SystemsResponse**](SystemsResponse.md)

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

