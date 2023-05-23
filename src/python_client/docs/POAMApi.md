# emass_client.POAMApi

All URIs are relative to *http://localhost:4010*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_poam_by_system_id**](POAMApi.md#add_poam_by_system_id) | **POST** /api/systems/{systemId}/poams | Add one or many POA&amp;M items in a system
[**delete_poam**](POAMApi.md#delete_poam) | **DELETE** /api/systems/{systemId}/poams | Remove one or many POA&amp;M items in a system
[**get_system_poams**](POAMApi.md#get_system_poams) | **GET** /api/systems/{systemId}/poams | Get one or many POA&amp;M items in a system
[**get_system_poams_by_poam_id**](POAMApi.md#get_system_poams_by_poam_id) | **GET** /api/systems/{systemId}/poams/{poamId} | Get POA&amp;M item by ID in a system
[**update_poam_by_system_id**](POAMApi.md#update_poam_by_system_id) | **PUT** /api/systems/{systemId}/poams | Update one or many POA&amp;M items in a system


# **add_poam_by_system_id**
> PoamResponsePost add_poam_by_system_id(system_id, request_body)

Add one or many POA&M items in a system

Add a POA&M for given `systemId`<br>  **Request Body Required Fields** - `status` - `vulnerabilityDescription` - `sourceIdentVuln` - `pocOrganization` - `resources`  **Note**<br /> If a POC email is supplied, the application will attempt to locate a user already registered within the application and pre-populate any information not explicitly supplied in the request. If no such user is found, these fields are **required** within the request.<br> `pocFirstName`, `pocLastName`, `pocPhoneNumber`<br />

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (mockType):
* Api Key Authentication (userId):
```python
import time
import os
import emass_client
from emass_client.models.poam_response_post import PoamResponsePost
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
    api_instance = emass_client.POAMApi(api_client)
    system_id = 35 # int | **System Id**: The unique system record identifier.
    request_body = None # List[object] | Add POA&M(s) to a system (systemID)

    try:
        # Add one or many POA&M items in a system
        api_response = api_instance.add_poam_by_system_id(system_id, request_body)
        print("The response of POAMApi->add_poam_by_system_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling POAMApi->add_poam_by_system_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **int**| **System Id**: The unique system record identifier. | 
 **request_body** | [**List[object]**](object.md)| Add POA&amp;M(s) to a system (systemID) | 

### Return type

[**PoamResponsePost**](PoamResponsePost.md)

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

# **delete_poam**
> PoamResponseDelete delete_poam(system_id, poam_request_delete_body_inner)

Remove one or many POA&M items in a system

Remove the POA&M matching `systemId` path parameter and `poamId` Request Body<br>

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (mockType):
* Api Key Authentication (userId):
```python
import time
import os
import emass_client
from emass_client.models.poam_request_delete_body_inner import PoamRequestDeleteBodyInner
from emass_client.models.poam_response_delete import PoamResponseDelete
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
    api_instance = emass_client.POAMApi(api_client)
    system_id = 35 # int | **System Id**: The unique system record identifier.
    poam_request_delete_body_inner = [emass_client.PoamRequestDeleteBodyInner()] # List[PoamRequestDeleteBodyInner] | Delete the given POA&M Id

    try:
        # Remove one or many POA&M items in a system
        api_response = api_instance.delete_poam(system_id, poam_request_delete_body_inner)
        print("The response of POAMApi->delete_poam:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling POAMApi->delete_poam: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **int**| **System Id**: The unique system record identifier. | 
 **poam_request_delete_body_inner** | [**List[PoamRequestDeleteBodyInner]**](PoamRequestDeleteBodyInner.md)| Delete the given POA&amp;M Id | 

### Return type

[**PoamResponseDelete**](PoamResponseDelete.md)

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

# **get_system_poams**
> PoamResponseGetSystems get_system_poams(system_id, scheduled_completion_date_start=scheduled_completion_date_start, scheduled_completion_date_end=scheduled_completion_date_end, control_acronyms=control_acronyms, ccis=ccis, system_only=system_only)

Get one or many POA&M items in a system

Returns system(s) containing POA&M items for matching parameters.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (mockType):
* Api Key Authentication (userId):
```python
import time
import os
import emass_client
from emass_client.models.poam_response_get_systems import PoamResponseGetSystems
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
    api_instance = emass_client.POAMApi(api_client)
    system_id = 35 # int | **System Id**: The unique system record identifier.
    scheduled_completion_date_start = 'scheduled_completion_date_start_example' # str | **Date Started**: Filter query by the scheduled completion start date (Unix date format). (optional)
    scheduled_completion_date_end = 'scheduled_completion_date_end_example' # str | **Date Ended**: Filter query by the scheduled completion start date (Unix date format). (optional)
    control_acronyms = 'control_acronyms_example' # str | **System Acronym**: Filter query by given system acronym (single or comma separated). (optional)
    ccis = 'ccis_example' # str | **CCI System**: Filter query by Control Correlation Identifiers (CCIs) (single or comma separated). (optional)
    system_only = True # bool | **Systems Only**: Indicates that only system(s) information is retrieved. (optional) (default to True)

    try:
        # Get one or many POA&M items in a system
        api_response = api_instance.get_system_poams(system_id, scheduled_completion_date_start=scheduled_completion_date_start, scheduled_completion_date_end=scheduled_completion_date_end, control_acronyms=control_acronyms, ccis=ccis, system_only=system_only)
        print("The response of POAMApi->get_system_poams:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling POAMApi->get_system_poams: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **int**| **System Id**: The unique system record identifier. | 
 **scheduled_completion_date_start** | **str**| **Date Started**: Filter query by the scheduled completion start date (Unix date format). | [optional] 
 **scheduled_completion_date_end** | **str**| **Date Ended**: Filter query by the scheduled completion start date (Unix date format). | [optional] 
 **control_acronyms** | **str**| **System Acronym**: Filter query by given system acronym (single or comma separated). | [optional] 
 **ccis** | **str**| **CCI System**: Filter query by Control Correlation Identifiers (CCIs) (single or comma separated). | [optional] 
 **system_only** | **bool**| **Systems Only**: Indicates that only system(s) information is retrieved. | [optional] [default to True]

### Return type

[**PoamResponseGetSystems**](PoamResponseGetSystems.md)

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

# **get_system_poams_by_poam_id**
> PoamResponseGetPoams get_system_poams_by_poam_id(system_id, poam_id)

Get POA&M item by ID in a system

Returns system(s) containing POA&M items for matching parameters.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (mockType):
* Api Key Authentication (userId):
```python
import time
import os
import emass_client
from emass_client.models.poam_response_get_poams import PoamResponseGetPoams
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
    api_instance = emass_client.POAMApi(api_client)
    system_id = 35 # int | **System Id**: The unique system record identifier.
    poam_id = 45 # int | **POA&M Id**: The unique POA&M record identifier.

    try:
        # Get POA&M item by ID in a system
        api_response = api_instance.get_system_poams_by_poam_id(system_id, poam_id)
        print("The response of POAMApi->get_system_poams_by_poam_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling POAMApi->get_system_poams_by_poam_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **int**| **System Id**: The unique system record identifier. | 
 **poam_id** | **int**| **POA&amp;M Id**: The unique POA&amp;M record identifier. | 

### Return type

[**PoamResponseGetPoams**](PoamResponseGetPoams.md)

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

# **update_poam_by_system_id**
> PoamResponsePut update_poam_by_system_id(system_id, request_body)

Update one or many POA&M items in a system

Update a POA&M for given `systemId`<br>  **Request Body Required Fields** - `poamId` - `displayPoamId` - `status` - `vulnerabilityDescription` - `sourceIdentVuln` - `pocOrganization` - `reviewStatus`  **Notes** - If a POC email is supplied, the application will attempt to locate a user already   registered within the application and pre-populate any information not explicitly supplied   in the request. If no such user is found, these fields are **required** within the request.<br>   `pocOrganization`, `pocFirstName`, `pocLastName`, `pocEmail`, `pocPhoneNumber`<br />  - To delete a milestone through the POA&M PUT the field `isActive` must be set to `false`: `isActive=false`.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (mockType):
* Api Key Authentication (userId):
```python
import time
import os
import emass_client
from emass_client.models.poam_response_put import PoamResponsePut
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
    api_instance = emass_client.POAMApi(api_client)
    system_id = 35 # int | **System Id**: The unique system record identifier.
    request_body = None # List[object] | Update an existing control by Id

    try:
        # Update one or many POA&M items in a system
        api_response = api_instance.update_poam_by_system_id(system_id, request_body)
        print("The response of POAMApi->update_poam_by_system_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling POAMApi->update_poam_by_system_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **int**| **System Id**: The unique system record identifier. | 
 **request_body** | [**List[object]**](object.md)| Update an existing control by Id | 

### Return type

[**PoamResponsePut**](PoamResponsePut.md)

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

