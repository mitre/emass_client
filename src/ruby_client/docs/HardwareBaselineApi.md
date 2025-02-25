# EmassClient::HardwareBaselineApi

All URIs are relative to *http://localhost:4010*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**add_hw_baseline_assets**](HardwareBaselineApi.md#add_hw_baseline_assets) | **POST** /api/systems/{systemId}/hw-baseline | Add one or many hardware assets in a system |
| [**delete_hw_baseline_assets**](HardwareBaselineApi.md#delete_hw_baseline_assets) | **DELETE** /api/systems/{systemId}/hw-baseline | Delete one or many hardware assets in a system |
| [**get_system_hw_baseline**](HardwareBaselineApi.md#get_system_hw_baseline) | **GET** /api/systems/{systemId}/hw-baseline | Get hardware baseline for a system |
| [**update_hw_baseline_assets**](HardwareBaselineApi.md#update_hw_baseline_assets) | **PUT** /api/systems/{systemId}/hw-baseline | Update one or many hardware assets in a system |


## add_hw_baseline_assets

> <HwBaselineResponsePostPut> add_hw_baseline_assets(system_id, hw_baseline_required_fields)

Add one or many hardware assets in a system

Adds assets to the Hardware Baseline for given `systemId`  **Request Body Required Fields** - `assetName`

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

api_instance = EmassClient::HardwareBaselineApi.new
system_id = 35 # Integer | **System Id**: The unique system record identifier.
hw_baseline_required_fields = [EmassClient::HwBaselineRequiredFields.new] # Array<HwBaselineRequiredFields> | Example request body for adding hardware baseline assets to an existing System (systemId)

begin
  # Add one or many hardware assets in a system
  result = api_instance.add_hw_baseline_assets(system_id, hw_baseline_required_fields)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling HardwareBaselineApi->add_hw_baseline_assets: #{e}"
end
```

#### Using the add_hw_baseline_assets_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<HwBaselineResponsePostPut>, Integer, Hash)> add_hw_baseline_assets_with_http_info(system_id, hw_baseline_required_fields)

```ruby
begin
  # Add one or many hardware assets in a system
  data, status_code, headers = api_instance.add_hw_baseline_assets_with_http_info(system_id, hw_baseline_required_fields)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <HwBaselineResponsePostPut>
rescue EmassClient::ApiError => e
  puts "Error when calling HardwareBaselineApi->add_hw_baseline_assets_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **system_id** | **Integer** | **System Id**: The unique system record identifier. |  |
| **hw_baseline_required_fields** | [**Array&lt;HwBaselineRequiredFields&gt;**](HwBaselineRequiredFields.md) | Example request body for adding hardware baseline assets to an existing System (systemId) |  |

### Return type

[**HwBaselineResponsePostPut**](HwBaselineResponsePostPut.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## delete_hw_baseline_assets

> <HwBaselineResponseDelete> delete_hw_baseline_assets(system_id, hw_baseline_request_delete_body_inner)

Delete one or many hardware assets in a system

Remove (delete) one or multiple assets from a system Hardware Baseline

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

api_instance = EmassClient::HardwareBaselineApi.new
system_id = 35 # Integer | **System Id**: The unique system record identifier.
hw_baseline_request_delete_body_inner = [EmassClient::HwBaselineRequestDeleteBodyInner.new] # Array<HwBaselineRequestDeleteBodyInner> | Example request body for deleting one or many Hardware Baseline assets

begin
  # Delete one or many hardware assets in a system
  result = api_instance.delete_hw_baseline_assets(system_id, hw_baseline_request_delete_body_inner)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling HardwareBaselineApi->delete_hw_baseline_assets: #{e}"
end
```

#### Using the delete_hw_baseline_assets_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<HwBaselineResponseDelete>, Integer, Hash)> delete_hw_baseline_assets_with_http_info(system_id, hw_baseline_request_delete_body_inner)

```ruby
begin
  # Delete one or many hardware assets in a system
  data, status_code, headers = api_instance.delete_hw_baseline_assets_with_http_info(system_id, hw_baseline_request_delete_body_inner)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <HwBaselineResponseDelete>
rescue EmassClient::ApiError => e
  puts "Error when calling HardwareBaselineApi->delete_hw_baseline_assets_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **system_id** | **Integer** | **System Id**: The unique system record identifier. |  |
| **hw_baseline_request_delete_body_inner** | [**Array&lt;HwBaselineRequestDeleteBodyInner&gt;**](HwBaselineRequestDeleteBodyInner.md) | Example request body for deleting one or many Hardware Baseline assets |  |

### Return type

[**HwBaselineResponseDelete**](HwBaselineResponseDelete.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## get_system_hw_baseline

> <HwBaselineResponseGet> get_system_hw_baseline(system_id, opts)

Get hardware baseline for a system

Returns the hardware baseline for a system matching the `systemId` path parameter

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

api_instance = EmassClient::HardwareBaselineApi.new
system_id = 35 # Integer | **System Id**: The unique system record identifier.
opts = {
  page_index: 56, # Integer | **Page Index**: If no value is specified, the default returns results from the first page with an index of 0. 
  page_size: 56 # Integer | **Page Size**: If no value is specified, the default returns 20000 per page. 
}

begin
  # Get hardware baseline for a system
  result = api_instance.get_system_hw_baseline(system_id, opts)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling HardwareBaselineApi->get_system_hw_baseline: #{e}"
end
```

#### Using the get_system_hw_baseline_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<HwBaselineResponseGet>, Integer, Hash)> get_system_hw_baseline_with_http_info(system_id, opts)

```ruby
begin
  # Get hardware baseline for a system
  data, status_code, headers = api_instance.get_system_hw_baseline_with_http_info(system_id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <HwBaselineResponseGet>
rescue EmassClient::ApiError => e
  puts "Error when calling HardwareBaselineApi->get_system_hw_baseline_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **system_id** | **Integer** | **System Id**: The unique system record identifier. |  |
| **page_index** | **Integer** | **Page Index**: If no value is specified, the default returns results from the first page with an index of 0.  | [optional][default to 0] |
| **page_size** | **Integer** | **Page Size**: If no value is specified, the default returns 20000 per page.  | [optional][default to 20000] |

### Return type

[**HwBaselineResponseGet**](HwBaselineResponseGet.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## update_hw_baseline_assets

> <HwBaselineResponsePostPut> update_hw_baseline_assets(system_id, hw_baseline_read_only_fields)

Update one or many hardware assets in a system

Updates assets in the Hardware Baseline for given `systemId`  **Request Body Required Fields** - `assetName` - `hardwareId`

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

api_instance = EmassClient::HardwareBaselineApi.new
system_id = 35 # Integer | **System Id**: The unique system record identifier.
hw_baseline_read_only_fields = [EmassClient::HwBaselineReadOnlyFields.new] # Array<HwBaselineReadOnlyFields> | Example request body for updating hardware baseline assets to an existing System (systemId)

begin
  # Update one or many hardware assets in a system
  result = api_instance.update_hw_baseline_assets(system_id, hw_baseline_read_only_fields)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling HardwareBaselineApi->update_hw_baseline_assets: #{e}"
end
```

#### Using the update_hw_baseline_assets_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<HwBaselineResponsePostPut>, Integer, Hash)> update_hw_baseline_assets_with_http_info(system_id, hw_baseline_read_only_fields)

```ruby
begin
  # Update one or many hardware assets in a system
  data, status_code, headers = api_instance.update_hw_baseline_assets_with_http_info(system_id, hw_baseline_read_only_fields)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <HwBaselineResponsePostPut>
rescue EmassClient::ApiError => e
  puts "Error when calling HardwareBaselineApi->update_hw_baseline_assets_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **system_id** | **Integer** | **System Id**: The unique system record identifier. |  |
| **hw_baseline_read_only_fields** | [**Array&lt;HwBaselineReadOnlyFields&gt;**](HwBaselineReadOnlyFields.md) | Example request body for updating hardware baseline assets to an existing System (systemId) |  |

### Return type

[**HwBaselineResponsePostPut**](HwBaselineResponsePostPut.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

