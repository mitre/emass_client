# emass_client.ContainerScanResultsApi

All URIs are relative to *http://localhost:4010*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_container_sans_by_system_id**](ContainerScanResultsApi.md#add_container_sans_by_system_id) | **POST** /api/systems/{systemId}/container-scan-results | Add one or many containers and their scan results
[**delete_container_sans**](ContainerScanResultsApi.md#delete_container_sans) | **DELETE** /api/systems/{systemId}/container-scan-results | Remove one or many containers in a system


# **add_container_sans_by_system_id**
> ContainersResponsePost add_container_sans_by_system_id(system_id, request_body)

Add one or many containers and their scan results

Add containers and their scan results in the assets module for a system `systemId`.

**Request Body Required Fields**
- `containerId`
- `containerName`
- `time`
- `benchmarks` (Object Array)
  - `benchmark`
  - `results` (Object Array)
    - `ruleId`
    - `status`
    - `lastSeen`

**Example Request Body Required Fields**
```
[
  {
    "containerId": "container identification",
    "containerName": "container name",
    "time": Datetime of scan/result (1648217219),
    "benchmarks": [
      {
        "benchmark": "RHEL_8_STIG",
        "results": [
          {
            "ruleId": "rule identification",
            "status": [Pass,Fail,Other,Not Reviewed,Not Checked,Not Applicable],
            "lastSeen": Unix date format (1648217219)
          }, {
            "ruleId": "rule identification",
            "status": [Pass,Fail,Other,Not Reviewed,Not Checked,Not Applicable],
            "lastSeen": Unix date format (1648217219)
          }
        ]
      }
    ]
  }
]
````

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (mockType):
* Api Key Authentication (userId):

```python
import emass_client
from emass_client.models.containers_response_post import ContainersResponsePost
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
    api_instance = emass_client.ContainerScanResultsApi(api_client)
    system_id = 35 # int | **System Id**: The unique system record identifier.
    request_body = None # List[object] | Example request body for adding containers and their scan results

    try:
        # Add one or many containers and their scan results
        api_response = api_instance.add_container_sans_by_system_id(system_id, request_body)
        print("The response of ContainerScanResultsApi->add_container_sans_by_system_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContainerScanResultsApi->add_container_sans_by_system_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **int**| **System Id**: The unique system record identifier. | 
 **request_body** | [**List[object]**](object.md)| Example request body for adding containers and their scan results | 

### Return type

[**ContainersResponsePost**](ContainersResponsePost.md)

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

# **delete_container_sans**
> ContainersResponseDelete delete_container_sans(system_id, container_resources_delete_body_inner)

Remove one or many containers in a system

Removes container scan resources and their scan results in the assets module for a system `systemId`

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (mockType):
* Api Key Authentication (userId):

```python
import emass_client
from emass_client.models.container_resources_delete_body_inner import ContainerResourcesDeleteBodyInner
from emass_client.models.containers_response_delete import ContainersResponseDelete
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
    api_instance = emass_client.ContainerScanResultsApi(api_client)
    system_id = 35 # int | **System Id**: The unique system record identifier.
    container_resources_delete_body_inner = [emass_client.ContainerResourcesDeleteBodyInner()] # List[ContainerResourcesDeleteBodyInner] | Delete the given Container Scan Id

    try:
        # Remove one or many containers in a system
        api_response = api_instance.delete_container_sans(system_id, container_resources_delete_body_inner)
        print("The response of ContainerScanResultsApi->delete_container_sans:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContainerScanResultsApi->delete_container_sans: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **int**| **System Id**: The unique system record identifier. | 
 **container_resources_delete_body_inner** | [**List[ContainerResourcesDeleteBodyInner]**](ContainerResourcesDeleteBodyInner.md)| Delete the given Container Scan Id | 

### Return type

[**ContainersResponseDelete**](ContainersResponseDelete.md)

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

