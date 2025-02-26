# emass_client.HardwareBaselineApi

All URIs are relative to *http://localhost:4010*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_hw_baseline_assets**](HardwareBaselineApi.md#add_hw_baseline_assets) | **POST** /api/systems/{systemId}/hw-baseline | Add one or many hardware assets in a system
[**delete_hw_baseline_assets**](HardwareBaselineApi.md#delete_hw_baseline_assets) | **DELETE** /api/systems/{systemId}/hw-baseline | Delete one or many hardware assets in a system
[**get_system_hw_baseline**](HardwareBaselineApi.md#get_system_hw_baseline) | **GET** /api/systems/{systemId}/hw-baseline | Get hardware baseline for a system
[**update_hw_baseline_assets**](HardwareBaselineApi.md#update_hw_baseline_assets) | **PUT** /api/systems/{systemId}/hw-baseline | Update one or many hardware assets in a system


# **add_hw_baseline_assets**
> HwBaselineResponsePostPut add_hw_baseline_assets(system_id, hw_baseline_required_fields)

Add one or many hardware assets in a system

Adds assets to the Hardware Baseline for given `systemId`

**Request Body Required Fields**
- `assetName`

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (mockType):
* Api Key Authentication (userId):

```python
import emass_client
from emass_client.models.hw_baseline_response_post_put import HwBaselineResponsePostPut
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
    api_instance = emass_client.HardwareBaselineApi(api_client)
    system_id = 35 # int | **System Id**: The unique system record identifier.
    hw_baseline_required_fields = [emass_client.HwBaselineRequiredFields()] # List[HwBaselineRequiredFields] | Example request body for adding hardware baseline assets to an existing System (systemId)

    try:
        # Add one or many hardware assets in a system
        api_response = api_instance.add_hw_baseline_assets(system_id, hw_baseline_required_fields)
        print("The response of HardwareBaselineApi->add_hw_baseline_assets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HardwareBaselineApi->add_hw_baseline_assets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **int**| **System Id**: The unique system record identifier. | 
 **hw_baseline_required_fields** | [**List[HwBaselineRequiredFields]**](HwBaselineRequiredFields.md)| Example request body for adding hardware baseline assets to an existing System (systemId) | 

### Return type

[**HwBaselineResponsePostPut**](HwBaselineResponsePostPut.md)

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

# **delete_hw_baseline_assets**
> HwBaselineResponseDelete delete_hw_baseline_assets(system_id, hw_baseline_request_delete_body_inner)

Delete one or many hardware assets in a system

Remove (delete) one or multiple assets from a system Hardware Baseline

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (mockType):
* Api Key Authentication (userId):

```python
import emass_client
from emass_client.models.hw_baseline_request_delete_body_inner import HwBaselineRequestDeleteBodyInner
from emass_client.models.hw_baseline_response_delete import HwBaselineResponseDelete
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
    api_instance = emass_client.HardwareBaselineApi(api_client)
    system_id = 35 # int | **System Id**: The unique system record identifier.
    hw_baseline_request_delete_body_inner = [emass_client.HwBaselineRequestDeleteBodyInner()] # List[HwBaselineRequestDeleteBodyInner] | Example request body for deleting one or many Hardware Baseline assets

    try:
        # Delete one or many hardware assets in a system
        api_response = api_instance.delete_hw_baseline_assets(system_id, hw_baseline_request_delete_body_inner)
        print("The response of HardwareBaselineApi->delete_hw_baseline_assets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HardwareBaselineApi->delete_hw_baseline_assets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **int**| **System Id**: The unique system record identifier. | 
 **hw_baseline_request_delete_body_inner** | [**List[HwBaselineRequestDeleteBodyInner]**](HwBaselineRequestDeleteBodyInner.md)| Example request body for deleting one or many Hardware Baseline assets | 

### Return type

[**HwBaselineResponseDelete**](HwBaselineResponseDelete.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_hw_baseline**
> HwBaselineResponseGet get_system_hw_baseline(system_id, page_index=page_index, page_size=page_size)

Get hardware baseline for a system

Returns the hardware baseline for a system matching the `systemId` path parameter

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (mockType):
* Api Key Authentication (userId):

```python
import emass_client
from emass_client.models.hw_baseline_response_get import HwBaselineResponseGet
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
    api_instance = emass_client.HardwareBaselineApi(api_client)
    system_id = 35 # int | **System Id**: The unique system record identifier.
    page_index = 0 # int | **Page Index**: If no value is specified, the default returns results from the first page with an index of 0.  (optional) (default to 0)
    page_size = 20000 # int | **Page Size**: If no value is specified, the default returns 20000 per page.  (optional) (default to 20000)

    try:
        # Get hardware baseline for a system
        api_response = api_instance.get_system_hw_baseline(system_id, page_index=page_index, page_size=page_size)
        print("The response of HardwareBaselineApi->get_system_hw_baseline:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HardwareBaselineApi->get_system_hw_baseline: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **int**| **System Id**: The unique system record identifier. | 
 **page_index** | **int**| **Page Index**: If no value is specified, the default returns results from the first page with an index of 0.  | [optional] [default to 0]
 **page_size** | **int**| **Page Size**: If no value is specified, the default returns 20000 per page.  | [optional] [default to 20000]

### Return type

[**HwBaselineResponseGet**](HwBaselineResponseGet.md)

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

# **update_hw_baseline_assets**
> HwBaselineResponsePostPut update_hw_baseline_assets(system_id, hw_baseline_read_only_fields)

Update one or many hardware assets in a system

Updates assets in the Hardware Baseline for given `systemId`

**Request Body Required Fields**
- `assetName`
- `hardwareId`

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (mockType):
* Api Key Authentication (userId):

```python
import emass_client
from emass_client.models.hw_baseline_response_post_put import HwBaselineResponsePostPut
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
    api_instance = emass_client.HardwareBaselineApi(api_client)
    system_id = 35 # int | **System Id**: The unique system record identifier.
    hw_baseline_read_only_fields = [emass_client.HwBaselineReadOnlyFields()] # List[HwBaselineReadOnlyFields] | Example request body for updating hardware baseline assets to an existing System (systemId)

    try:
        # Update one or many hardware assets in a system
        api_response = api_instance.update_hw_baseline_assets(system_id, hw_baseline_read_only_fields)
        print("The response of HardwareBaselineApi->update_hw_baseline_assets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HardwareBaselineApi->update_hw_baseline_assets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **int**| **System Id**: The unique system record identifier. | 
 **hw_baseline_read_only_fields** | [**List[HwBaselineReadOnlyFields]**](HwBaselineReadOnlyFields.md)| Example request body for updating hardware baseline assets to an existing System (systemId) | 

### Return type

[**HwBaselineResponsePostPut**](HwBaselineResponsePostPut.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

