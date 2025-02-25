# EmassClient::ContainerScanResultsApi

All URIs are relative to *http://localhost:4010*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**add_container_sans_by_system_id**](ContainerScanResultsApi.md#add_container_sans_by_system_id) | **POST** /api/systems/{systemId}/container-scan-results | Add one or many containers and their scan results |
| [**delete_container_sans**](ContainerScanResultsApi.md#delete_container_sans) | **DELETE** /api/systems/{systemId}/container-scan-results | Remove one or many containers in a system |


## add_container_sans_by_system_id

> <ContainersResponsePost> add_container_sans_by_system_id(system_id, request_body)

Add one or many containers and their scan results

Add containers and their scan results in the assets module for a system `systemId`.  **Request Body Required Fields** - `containerId` - `containerName` - `time` - `benchmarks` (Object Array)   - `benchmark`   - `results` (Object Array)     - `ruleId`     - `status`     - `lastSeen`  **Example Request Body Required Fields** ``` [   {     \"containerId\": \"container identification\",     \"containerName\": \"container name\",     \"time\": Datetime of scan/result (1648217219),     \"benchmarks\": [       {         \"benchmark\": \"RHEL_8_STIG\",         \"results\": [           {             \"ruleId\": \"rule identification\",             \"status\": [Pass,Fail,Other,Not Reviewed,Not Checked,Not Applicable],             \"lastSeen\": Unix date format (1648217219)           }, {             \"ruleId\": \"rule identification\",             \"status\": [Pass,Fail,Other,Not Reviewed,Not Checked,Not Applicable],             \"lastSeen\": Unix date format (1648217219)           }         ]       }     ]   } ] ````

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

api_instance = EmassClient::ContainerScanResultsApi.new
system_id = 35 # Integer | **System Id**: The unique system record identifier.
request_body = [3.56] # Array<Object> | Example request body for adding containers and their scan results

begin
  # Add one or many containers and their scan results
  result = api_instance.add_container_sans_by_system_id(system_id, request_body)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling ContainerScanResultsApi->add_container_sans_by_system_id: #{e}"
end
```

#### Using the add_container_sans_by_system_id_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ContainersResponsePost>, Integer, Hash)> add_container_sans_by_system_id_with_http_info(system_id, request_body)

```ruby
begin
  # Add one or many containers and their scan results
  data, status_code, headers = api_instance.add_container_sans_by_system_id_with_http_info(system_id, request_body)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ContainersResponsePost>
rescue EmassClient::ApiError => e
  puts "Error when calling ContainerScanResultsApi->add_container_sans_by_system_id_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **system_id** | **Integer** | **System Id**: The unique system record identifier. |  |
| **request_body** | [**Array&lt;Object&gt;**](Object.md) | Example request body for adding containers and their scan results |  |

### Return type

[**ContainersResponsePost**](ContainersResponsePost.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## delete_container_sans

> <ContainersResponseDelete> delete_container_sans(system_id, container_resources_delete_body_inner)

Remove one or many containers in a system

Removes container scan resources and their scan results in the assets module for a system `systemId`

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

api_instance = EmassClient::ContainerScanResultsApi.new
system_id = 35 # Integer | **System Id**: The unique system record identifier.
container_resources_delete_body_inner = [EmassClient::ContainerResourcesDeleteBodyInner.new] # Array<ContainerResourcesDeleteBodyInner> | Delete the given Container Scan Id

begin
  # Remove one or many containers in a system
  result = api_instance.delete_container_sans(system_id, container_resources_delete_body_inner)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling ContainerScanResultsApi->delete_container_sans: #{e}"
end
```

#### Using the delete_container_sans_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ContainersResponseDelete>, Integer, Hash)> delete_container_sans_with_http_info(system_id, container_resources_delete_body_inner)

```ruby
begin
  # Remove one or many containers in a system
  data, status_code, headers = api_instance.delete_container_sans_with_http_info(system_id, container_resources_delete_body_inner)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ContainersResponseDelete>
rescue EmassClient::ApiError => e
  puts "Error when calling ContainerScanResultsApi->delete_container_sans_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **system_id** | **Integer** | **System Id**: The unique system record identifier. |  |
| **container_resources_delete_body_inner** | [**Array&lt;ContainerResourcesDeleteBodyInner&gt;**](ContainerResourcesDeleteBodyInner.md) | Delete the given Container Scan Id |  |

### Return type

[**ContainersResponseDelete**](ContainersResponseDelete.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

