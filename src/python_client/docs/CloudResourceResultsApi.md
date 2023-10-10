# emass_client.CloudResourceResultsApi

All URIs are relative to *http://localhost:4010*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_cloud_resources_by_system_id**](CloudResourceResultsApi.md#add_cloud_resources_by_system_id) | **POST** /api/systems/{systemId}/cloud-resource-results | Add one or many cloud resources and their scan results
[**delete_cloud_resources**](CloudResourceResultsApi.md#delete_cloud_resources) | **DELETE** /api/systems/{systemId}/cloud-resource-results | Remove one or many cloud resources in a system


# **add_cloud_resources_by_system_id**
> CloudResourcesResponsePost add_cloud_resources_by_system_id(system_id, request_body)

Add one or many cloud resources and their scan results

Add cloud resources and their scan results in the assets module for a system `systemId`  **Request Body Required Fields** - `provider` - `resourceId` - `resourceName` - `resourceType` - Compliance Results Object Array `complianceResults`   - `cspPolicyDefinitionId`   - `isCompliant`   - `policyDefinitionTitle`  **Example Request Body Required Fields** ``` [    {      \"provider\": \"provide name\",     \"resourceId\": \"resource identification\",     \"resourceName\": \"resource name\",     \"resourceType\": \"resource type\",     \"complianceResults\": [        {          \"cspPolicyDefinitionId\": \"CSP policy definition identification\",         \"policyDefinitionTitle\": \"policy definition title\",         \"isCompliant\": [true or false]       }      ]    }  ] ```

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (mockType):
* Api Key Authentication (userId):
```python
import time
import os
import emass_client
from emass_client.models.cloud_resources_response_post import CloudResourcesResponsePost
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
    api_instance = emass_client.CloudResourceResultsApi(api_client)
    system_id = 35 # int | **System Id**: The unique system record identifier.
    request_body = None # List[object] | Add cloud resources and their scan results

    try:
        # Add one or many cloud resources and their scan results
        api_response = api_instance.add_cloud_resources_by_system_id(system_id, request_body)
        print("The response of CloudResourceResultsApi->add_cloud_resources_by_system_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudResourceResultsApi->add_cloud_resources_by_system_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **int**| **System Id**: The unique system record identifier. | 
 **request_body** | [**List[object]**](object.md)| Add cloud resources and their scan results | 

### Return type

[**CloudResourcesResponsePost**](CloudResourcesResponsePost.md)

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

# **delete_cloud_resources**
> CloudResourcesDelete delete_cloud_resources(system_id, cloud_resources_delete_body_inner)

Remove one or many cloud resources in a system

Removes cloud resources and their scan results in the assets module for a system `systemId`

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (mockType):
* Api Key Authentication (userId):
```python
import time
import os
import emass_client
from emass_client.models.cloud_resources_delete import CloudResourcesDelete
from emass_client.models.cloud_resources_delete_body_inner import CloudResourcesDeleteBodyInner
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
    api_instance = emass_client.CloudResourceResultsApi(api_client)
    system_id = 35 # int | **System Id**: The unique system record identifier.
    cloud_resources_delete_body_inner = [emass_client.CloudResourcesDeleteBodyInner()] # List[CloudResourcesDeleteBodyInner] | Delete the given Cloud Resource Id

    try:
        # Remove one or many cloud resources in a system
        api_response = api_instance.delete_cloud_resources(system_id, cloud_resources_delete_body_inner)
        print("The response of CloudResourceResultsApi->delete_cloud_resources:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudResourceResultsApi->delete_cloud_resources: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **int**| **System Id**: The unique system record identifier. | 
 **cloud_resources_delete_body_inner** | [**List[CloudResourcesDeleteBodyInner]**](CloudResourcesDeleteBodyInner.md)| Delete the given Cloud Resource Id | 

### Return type

[**CloudResourcesDelete**](CloudResourcesDelete.md)

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

