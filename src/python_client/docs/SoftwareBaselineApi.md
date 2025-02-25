# emass_client.SoftwareBaselineApi

All URIs are relative to *http://localhost:4010*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_sw_baseline_assets**](SoftwareBaselineApi.md#add_sw_baseline_assets) | **POST** /api/systems/{systemId}/sw-baseline | Add one or many software assets in a system
[**delete_sw_baseline_assets**](SoftwareBaselineApi.md#delete_sw_baseline_assets) | **DELETE** /api/systems/{systemId}/sw-baseline | Delete one or many software assets in a system
[**get_system_sw_baseline**](SoftwareBaselineApi.md#get_system_sw_baseline) | **GET** /api/systems/{systemId}/sw-baseline | Get software baseline for a system
[**update_sw_baseline_assets**](SoftwareBaselineApi.md#update_sw_baseline_assets) | **PUT** /api/systems/{systemId}/sw-baseline | Update one or many software assets in a system


# **add_sw_baseline_assets**
> SwBaselineResponsePostPut add_sw_baseline_assets(system_id, sw_baseline_required_fields)

Add one or many software assets in a system

Adds assets to the Software Baseline for given `systemId`

**Request Body Required Fields**
- `softwareVendor`
- `softwareName`
- `version`

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (mockType):
* Api Key Authentication (userId):

```python
import emass_client
from emass_client.models.sw_baseline_response_post_put import SwBaselineResponsePostPut
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
    api_instance = emass_client.SoftwareBaselineApi(api_client)
    system_id = 35 # int | **System Id**: The unique system record identifier.
    sw_baseline_required_fields = [emass_client.SwBaselineRequiredFields()] # List[SwBaselineRequiredFields] | Example request body for adding software baseline assets to an existing System (systemId)

    try:
        # Add one or many software assets in a system
        api_response = api_instance.add_sw_baseline_assets(system_id, sw_baseline_required_fields)
        print("The response of SoftwareBaselineApi->add_sw_baseline_assets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SoftwareBaselineApi->add_sw_baseline_assets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **int**| **System Id**: The unique system record identifier. | 
 **sw_baseline_required_fields** | [**List[SwBaselineRequiredFields]**](SwBaselineRequiredFields.md)| Example request body for adding software baseline assets to an existing System (systemId) | 

### Return type

[**SwBaselineResponsePostPut**](SwBaselineResponsePostPut.md)

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

# **delete_sw_baseline_assets**
> SwBaselineResponseDelete delete_sw_baseline_assets(system_id, sw_baseline_request_delete_body_inner)

Delete one or many software assets in a system

Remove (delete) one or multiple assets from a system Software Baseline

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (mockType):
* Api Key Authentication (userId):

```python
import emass_client
from emass_client.models.sw_baseline_request_delete_body_inner import SwBaselineRequestDeleteBodyInner
from emass_client.models.sw_baseline_response_delete import SwBaselineResponseDelete
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
    api_instance = emass_client.SoftwareBaselineApi(api_client)
    system_id = 35 # int | **System Id**: The unique system record identifier.
    sw_baseline_request_delete_body_inner = [emass_client.SwBaselineRequestDeleteBodyInner()] # List[SwBaselineRequestDeleteBodyInner] | Example request body for deleting one or many Software Baseline assets

    try:
        # Delete one or many software assets in a system
        api_response = api_instance.delete_sw_baseline_assets(system_id, sw_baseline_request_delete_body_inner)
        print("The response of SoftwareBaselineApi->delete_sw_baseline_assets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SoftwareBaselineApi->delete_sw_baseline_assets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **int**| **System Id**: The unique system record identifier. | 
 **sw_baseline_request_delete_body_inner** | [**List[SwBaselineRequestDeleteBodyInner]**](SwBaselineRequestDeleteBodyInner.md)| Example request body for deleting one or many Software Baseline assets | 

### Return type

[**SwBaselineResponseDelete**](SwBaselineResponseDelete.md)

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

# **get_system_sw_baseline**
> SwBaselineResponseGet get_system_sw_baseline(system_id, page_index=page_index, page_size=page_size)

Get software baseline for a system

Returns the software baseline for a system matching the `systemId` path parameter

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (mockType):
* Api Key Authentication (userId):

```python
import emass_client
from emass_client.models.sw_baseline_response_get import SwBaselineResponseGet
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
    api_instance = emass_client.SoftwareBaselineApi(api_client)
    system_id = 35 # int | **System Id**: The unique system record identifier.
    page_index = 0 # int | **Page Index**: If no value is specified, the default returns results from the first page with an index of 0.  (optional) (default to 0)
    page_size = 20000 # int | **Page Size**: If no value is specified, the default returns 20000 per page.  (optional) (default to 20000)

    try:
        # Get software baseline for a system
        api_response = api_instance.get_system_sw_baseline(system_id, page_index=page_index, page_size=page_size)
        print("The response of SoftwareBaselineApi->get_system_sw_baseline:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SoftwareBaselineApi->get_system_sw_baseline: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **int**| **System Id**: The unique system record identifier. | 
 **page_index** | **int**| **Page Index**: If no value is specified, the default returns results from the first page with an index of 0.  | [optional] [default to 0]
 **page_size** | **int**| **Page Size**: If no value is specified, the default returns 20000 per page.  | [optional] [default to 20000]

### Return type

[**SwBaselineResponseGet**](SwBaselineResponseGet.md)

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

# **update_sw_baseline_assets**
> SwBaselineResponsePostPut update_sw_baseline_assets(system_id, sw_baseline_read_only_fields)

Update one or many software assets in a system

Updates assets in the Software Baseline for given `systemId`

**Request Body Required Fields**
- `softwareId`
- `softwareVendor`
- `softwareName`
- `version`

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (mockType):
* Api Key Authentication (userId):

```python
import emass_client
from emass_client.models.sw_baseline_response_post_put import SwBaselineResponsePostPut
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
    api_instance = emass_client.SoftwareBaselineApi(api_client)
    system_id = 35 # int | **System Id**: The unique system record identifier.
    sw_baseline_read_only_fields = [emass_client.SwBaselineReadOnlyFields()] # List[SwBaselineReadOnlyFields] | Example request body for updating software baseline assets to an existing System (systemId)

    try:
        # Update one or many software assets in a system
        api_response = api_instance.update_sw_baseline_assets(system_id, sw_baseline_read_only_fields)
        print("The response of SoftwareBaselineApi->update_sw_baseline_assets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SoftwareBaselineApi->update_sw_baseline_assets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **int**| **System Id**: The unique system record identifier. | 
 **sw_baseline_read_only_fields** | [**List[SwBaselineReadOnlyFields]**](SwBaselineReadOnlyFields.md)| Example request body for updating software baseline assets to an existing System (systemId) | 

### Return type

[**SwBaselineResponsePostPut**](SwBaselineResponsePostPut.md)

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

