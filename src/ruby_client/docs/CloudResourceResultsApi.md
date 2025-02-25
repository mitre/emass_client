# EmassClient::CloudResourceResultsApi

All URIs are relative to *http://localhost:4010*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**add_cloud_resources_by_system_id**](CloudResourceResultsApi.md#add_cloud_resources_by_system_id) | **POST** /api/systems/{systemId}/cloud-resource-results | Add one or many cloud resources and their scan results |
| [**delete_cloud_resources**](CloudResourceResultsApi.md#delete_cloud_resources) | **DELETE** /api/systems/{systemId}/cloud-resource-results | Remove one or many cloud resources in a system |


## add_cloud_resources_by_system_id

> <CloudResourcesResponsePost> add_cloud_resources_by_system_id(system_id, request_body)

Add one or many cloud resources and their scan results

Add cloud resources and their scan results in the assets module for a system `systemId`  **Request Body Required Fields** - `provider` - `resourceId` - `resourceName` - `resourceType` - `complianceResults` (Object Array)   - `cspPolicyDefinitionId`   - `isCompliant`   - `policyDefinitionTitle`  **Example Request Body Required Fields** ``` [   {     \"provider\": \"provide name\",     \"resourceId\": \"resource identification\",     \"resourceName\": \"resource name\",     \"resourceType\": \"resource type\",     \"complianceResults\": [       {         \"cspPolicyDefinitionId\": \"CSP policy definition identification\",         \"policyDefinitionTitle\": \"policy definition title\",         \"isCompliant\": [true or false]       }     ]   } ] ```

### Examples

```ruby
require 'time'
require 'emass_client'
# setup authorization
EmassClient.configure do |config|
  # Configure API key authorization: apiKey
  config.api_key['api-key'] = 'YOUR API KEY'
  # Uncomment the following line to set a prefix for the API key, e.g. 'Bearer' (defaults to nil)
  # config.api_key_prefix['api-key'] = 'Bearer'

  # Configure API key authorization: mockType
  config.api_key['Prefer'] = 'YOUR API KEY'
  # Uncomment the following line to set a prefix for the API key, e.g. 'Bearer' (defaults to nil)
  # config.api_key_prefix['Prefer'] = 'Bearer'

  # Configure API key authorization: userId
  config.api_key['user-uid'] = 'YOUR API KEY'
  # Uncomment the following line to set a prefix for the API key, e.g. 'Bearer' (defaults to nil)
  # config.api_key_prefix['user-uid'] = 'Bearer'
end

api_instance = EmassClient::CloudResourceResultsApi.new
system_id = 35 # Integer | **System Id**: The unique system record identifier.
request_body = [3.56] # Array<Object> | Example request body for adding cloud resources and their scan results

begin
  # Add one or many cloud resources and their scan results
  result = api_instance.add_cloud_resources_by_system_id(system_id, request_body)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling CloudResourceResultsApi->add_cloud_resources_by_system_id: #{e}"
end
```

#### Using the add_cloud_resources_by_system_id_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<CloudResourcesResponsePost>, Integer, Hash)> add_cloud_resources_by_system_id_with_http_info(system_id, request_body)

```ruby
begin
  # Add one or many cloud resources and their scan results
  data, status_code, headers = api_instance.add_cloud_resources_by_system_id_with_http_info(system_id, request_body)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <CloudResourcesResponsePost>
rescue EmassClient::ApiError => e
  puts "Error when calling CloudResourceResultsApi->add_cloud_resources_by_system_id_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **system_id** | **Integer** | **System Id**: The unique system record identifier. |  |
| **request_body** | [**Array&lt;Object&gt;**](Object.md) | Example request body for adding cloud resources and their scan results |  |

### Return type

[**CloudResourcesResponsePost**](CloudResourcesResponsePost.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## delete_cloud_resources

> <CloudResourcesDelete> delete_cloud_resources(system_id, cloud_resources_delete_body_inner)

Remove one or many cloud resources in a system

Removes cloud resources and their scan results in the assets module for a system `systemId`

### Examples

```ruby
require 'time'
require 'emass_client'
# setup authorization
EmassClient.configure do |config|
  # Configure API key authorization: apiKey
  config.api_key['api-key'] = 'YOUR API KEY'
  # Uncomment the following line to set a prefix for the API key, e.g. 'Bearer' (defaults to nil)
  # config.api_key_prefix['api-key'] = 'Bearer'

  # Configure API key authorization: mockType
  config.api_key['Prefer'] = 'YOUR API KEY'
  # Uncomment the following line to set a prefix for the API key, e.g. 'Bearer' (defaults to nil)
  # config.api_key_prefix['Prefer'] = 'Bearer'

  # Configure API key authorization: userId
  config.api_key['user-uid'] = 'YOUR API KEY'
  # Uncomment the following line to set a prefix for the API key, e.g. 'Bearer' (defaults to nil)
  # config.api_key_prefix['user-uid'] = 'Bearer'
end

api_instance = EmassClient::CloudResourceResultsApi.new
system_id = 35 # Integer | **System Id**: The unique system record identifier.
cloud_resources_delete_body_inner = [EmassClient::CloudResourcesDeleteBodyInner.new] # Array<CloudResourcesDeleteBodyInner> | Delete the given Cloud Resource Id

begin
  # Remove one or many cloud resources in a system
  result = api_instance.delete_cloud_resources(system_id, cloud_resources_delete_body_inner)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling CloudResourceResultsApi->delete_cloud_resources: #{e}"
end
```

#### Using the delete_cloud_resources_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<CloudResourcesDelete>, Integer, Hash)> delete_cloud_resources_with_http_info(system_id, cloud_resources_delete_body_inner)

```ruby
begin
  # Remove one or many cloud resources in a system
  data, status_code, headers = api_instance.delete_cloud_resources_with_http_info(system_id, cloud_resources_delete_body_inner)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <CloudResourcesDelete>
rescue EmassClient::ApiError => e
  puts "Error when calling CloudResourceResultsApi->delete_cloud_resources_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **system_id** | **Integer** | **System Id**: The unique system record identifier. |  |
| **cloud_resources_delete_body_inner** | [**Array&lt;CloudResourcesDeleteBodyInner&gt;**](CloudResourcesDeleteBodyInner.md) | Delete the given Cloud Resource Id |  |

### Return type

[**CloudResourcesDelete**](CloudResourcesDelete.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

