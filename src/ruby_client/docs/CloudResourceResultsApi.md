# EmassClient::CloudResourceResultsApi

All URIs are relative to *http://localhost:4010*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**add_cloud_resources_by_system_id**](CloudResourceResultsApi.md#add_cloud_resources_by_system_id) | **POST** /api/systems/{systemId}/cloud-resource-results | Add one or many cloud resources and their scan results |


## add_cloud_resources_by_system_id

> <CloudResourcesResponsePost> add_cloud_resources_by_system_id(system_id, request_body)

Add one or many cloud resources and their scan results

Add cloud resources and their scan results in the assets module for a system `systemId`

### Examples

```ruby
require 'time'
require 'emass_client'
# setup authorization
EmassClient.configure do |config|
  # Configure API key authorization: apiKey
  config.api_key['apiKey'] = 'YOUR API KEY'
  # Uncomment the following line to set a prefix for the API key, e.g. 'Bearer' (defaults to nil)
  # config.api_key_prefix['apiKey'] = 'Bearer'

  # Configure API key authorization: mockType
  config.api_key['mockType'] = 'YOUR API KEY'
  # Uncomment the following line to set a prefix for the API key, e.g. 'Bearer' (defaults to nil)
  # config.api_key_prefix['mockType'] = 'Bearer'

  # Configure API key authorization: userId
  config.api_key['userId'] = 'YOUR API KEY'
  # Uncomment the following line to set a prefix for the API key, e.g. 'Bearer' (defaults to nil)
  # config.api_key_prefix['userId'] = 'Bearer'
end

api_instance = EmassClient::CloudResourceResultsApi.new
system_id = 35 # Integer | **System Id**: The unique system record identifier.
request_body = [3.56] # Array<Object> | Add cloud resources and their scan results

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
| **request_body** | [**Array&lt;Object&gt;**](Object.md) | Add cloud resources and their scan results |  |

### Return type

[**CloudResourcesResponsePost**](CloudResourcesResponsePost.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

