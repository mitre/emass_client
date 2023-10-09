# emass_client.MilestonesApi

All URIs are relative to *http://localhost:4010*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_milestone_by_system_id_and_poam_id**](MilestonesApi.md#add_milestone_by_system_id_and_poam_id) | **POST** /api/systems/{systemId}/poams/{poamId}/milestones | Add milestones to one or many POA&amp;M items in a system
[**delete_milestone**](MilestonesApi.md#delete_milestone) | **DELETE** /api/systems/{systemId}/poams/{poamId}/milestones | Remove milestones in a system for one or many POA&amp;M items
[**get_system_milestones_by_poam_id**](MilestonesApi.md#get_system_milestones_by_poam_id) | **GET** /api/systems/{systemId}/poams/{poamId}/milestones | Get milestones in one or many POA&amp;M items in a system
[**get_system_milestones_by_poam_id_and_milestone_id**](MilestonesApi.md#get_system_milestones_by_poam_id_and_milestone_id) | **GET** /api/systems/{systemId}/poams/{poamId}/milestones/{milestoneId} | Get milestone by ID in POA&amp;M item in a system
[**update_milestone_by_system_id_and_poam_id**](MilestonesApi.md#update_milestone_by_system_id_and_poam_id) | **PUT** /api/systems/{systemId}/poams/{poamId}/milestones | Update one or many POA&amp;M items in a system


# **add_milestone_by_system_id_and_poam_id**
> MilestoneResponsePost add_milestone_by_system_id_and_poam_id(system_id, poam_id, request_body)

Add milestones to one or many POA&M items in a system

Adds a milestone for given `systemId` and `poamId` path parameters  **Request Body Required Fields** - `description` - `scheduledCompletionDate`

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (mockType):
* Api Key Authentication (userId):
```python
import time
import os
import emass_client
from emass_client.models.milestone_response_post import MilestoneResponsePost
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
    api_instance = emass_client.MilestonesApi(api_client)
    system_id = 35 # int | **System Id**: The unique system record identifier.
    poam_id = 45 # int | **POA&M Id**: The unique POA&M record identifier.
    request_body = None # List[object] | Add milestones to an existing system poam

    try:
        # Add milestones to one or many POA&M items in a system
        api_response = api_instance.add_milestone_by_system_id_and_poam_id(system_id, poam_id, request_body)
        print("The response of MilestonesApi->add_milestone_by_system_id_and_poam_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MilestonesApi->add_milestone_by_system_id_and_poam_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **int**| **System Id**: The unique system record identifier. | 
 **poam_id** | **int**| **POA&amp;M Id**: The unique POA&amp;M record identifier. | 
 **request_body** | [**List[object]**](object.md)| Add milestones to an existing system poam | 

### Return type

[**MilestoneResponsePost**](MilestoneResponsePost.md)

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

# **delete_milestone**
> MilestoneResponseDelete delete_milestone(system_id, poam_id, milestones_request_delete_body_inner)

Remove milestones in a system for one or many POA&M items

Remove the POA&M matching `systemId` and `poamId` for path parameters and `milstoneId` provide in the Requst Body  **Notes**<br> To delete a milestone the record must be inactive by having the field isActive set to false (`isActive=false`).

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (mockType):
* Api Key Authentication (userId):
```python
import time
import os
import emass_client
from emass_client.models.milestone_response_delete import MilestoneResponseDelete
from emass_client.models.milestones_request_delete_body_inner import MilestonesRequestDeleteBodyInner
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
    api_instance = emass_client.MilestonesApi(api_client)
    system_id = 35 # int | **System Id**: The unique system record identifier.
    poam_id = 45 # int | **POA&M Id**: The unique POA&M record identifier.
    milestones_request_delete_body_inner = [emass_client.MilestonesRequestDeleteBodyInner()] # List[MilestonesRequestDeleteBodyInner] | Delete the given Milestone Id

    try:
        # Remove milestones in a system for one or many POA&M items
        api_response = api_instance.delete_milestone(system_id, poam_id, milestones_request_delete_body_inner)
        print("The response of MilestonesApi->delete_milestone:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MilestonesApi->delete_milestone: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **int**| **System Id**: The unique system record identifier. | 
 **poam_id** | **int**| **POA&amp;M Id**: The unique POA&amp;M record identifier. | 
 **milestones_request_delete_body_inner** | [**List[MilestonesRequestDeleteBodyInner]**](MilestonesRequestDeleteBodyInner.md)| Delete the given Milestone Id | 

### Return type

[**MilestoneResponseDelete**](MilestoneResponseDelete.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_milestones_by_poam_id**
> MilestoneResponseGet get_system_milestones_by_poam_id(system_id, poam_id, scheduled_completion_date_start=scheduled_completion_date_start, scheduled_completion_date_end=scheduled_completion_date_end)

Get milestones in one or many POA&M items in a system

Returns system containing milestones for matching parameters.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (mockType):
* Api Key Authentication (userId):
```python
import time
import os
import emass_client
from emass_client.models.milestone_response_get import MilestoneResponseGet
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
    api_instance = emass_client.MilestonesApi(api_client)
    system_id = 35 # int | **System Id**: The unique system record identifier.
    poam_id = 45 # int | **POA&M Id**: The unique POA&M record identifier.
    scheduled_completion_date_start = 'scheduled_completion_date_start_example' # str | **Date Started**: Filter query by the scheduled completion start date (Unix date format). (optional)
    scheduled_completion_date_end = 'scheduled_completion_date_end_example' # str | **Date Ended**: Filter query by the scheduled completion start date (Unix date format). (optional)

    try:
        # Get milestones in one or many POA&M items in a system
        api_response = api_instance.get_system_milestones_by_poam_id(system_id, poam_id, scheduled_completion_date_start=scheduled_completion_date_start, scheduled_completion_date_end=scheduled_completion_date_end)
        print("The response of MilestonesApi->get_system_milestones_by_poam_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MilestonesApi->get_system_milestones_by_poam_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **int**| **System Id**: The unique system record identifier. | 
 **poam_id** | **int**| **POA&amp;M Id**: The unique POA&amp;M record identifier. | 
 **scheduled_completion_date_start** | **str**| **Date Started**: Filter query by the scheduled completion start date (Unix date format). | [optional] 
 **scheduled_completion_date_end** | **str**| **Date Ended**: Filter query by the scheduled completion start date (Unix date format). | [optional] 

### Return type

[**MilestoneResponseGet**](MilestoneResponseGet.md)

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

# **get_system_milestones_by_poam_id_and_milestone_id**
> MilestoneResponseGetMilestone get_system_milestones_by_poam_id_and_milestone_id(system_id, poam_id, milestone_id)

Get milestone by ID in POA&M item in a system

Returns systems containing milestones for matching parameters.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (mockType):
* Api Key Authentication (userId):
```python
import time
import os
import emass_client
from emass_client.models.milestone_response_get_milestone import MilestoneResponseGetMilestone
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
    api_instance = emass_client.MilestonesApi(api_client)
    system_id = 35 # int | **System Id**: The unique system record identifier.
    poam_id = 45 # int | **POA&M Id**: The unique POA&M record identifier.
    milestone_id = 77 # int | **Milestone Id**: The unique milestone record identifier.

    try:
        # Get milestone by ID in POA&M item in a system
        api_response = api_instance.get_system_milestones_by_poam_id_and_milestone_id(system_id, poam_id, milestone_id)
        print("The response of MilestonesApi->get_system_milestones_by_poam_id_and_milestone_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MilestonesApi->get_system_milestones_by_poam_id_and_milestone_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **int**| **System Id**: The unique system record identifier. | 
 **poam_id** | **int**| **POA&amp;M Id**: The unique POA&amp;M record identifier. | 
 **milestone_id** | **int**| **Milestone Id**: The unique milestone record identifier. | 

### Return type

[**MilestoneResponseGetMilestone**](MilestoneResponseGetMilestone.md)

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

# **update_milestone_by_system_id_and_poam_id**
> MilestoneResponsePut update_milestone_by_system_id_and_poam_id(system_id, poam_id, request_body)

Update one or many POA&M items in a system

Updates a milestone for given `systemId` and `poamId` path parameters  **Request Body Required Fields** - `milestoneId` - `description` - `scheduledCompletionDate`

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (mockType):
* Api Key Authentication (userId):
```python
import time
import os
import emass_client
from emass_client.models.milestone_response_put import MilestoneResponsePut
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
    api_instance = emass_client.MilestonesApi(api_client)
    system_id = 35 # int | **System Id**: The unique system record identifier.
    poam_id = 45 # int | **POA&M Id**: The unique POA&M record identifier.
    request_body = None # List[object] | Update milestones for an existing system poam

    try:
        # Update one or many POA&M items in a system
        api_response = api_instance.update_milestone_by_system_id_and_poam_id(system_id, poam_id, request_body)
        print("The response of MilestonesApi->update_milestone_by_system_id_and_poam_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MilestonesApi->update_milestone_by_system_id_and_poam_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **int**| **System Id**: The unique system record identifier. | 
 **poam_id** | **int**| **POA&amp;M Id**: The unique POA&amp;M record identifier. | 
 **request_body** | [**List[object]**](object.md)| Update milestones for an existing system poam | 

### Return type

[**MilestoneResponsePut**](MilestoneResponsePut.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

