# EmassClient::SoftwareBaselineApi

All URIs are relative to *http://localhost:4010*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**add_sw_baseline_assets**](SoftwareBaselineApi.md#add_sw_baseline_assets) | **POST** /api/systems/{systemId}/sw-baseline | Add one or many software assets in a system |
| [**delete_sw_baseline_assets**](SoftwareBaselineApi.md#delete_sw_baseline_assets) | **DELETE** /api/systems/{systemId}/sw-baseline | Delete one or many software assets in a system |
| [**get_system_sw_baseline**](SoftwareBaselineApi.md#get_system_sw_baseline) | **GET** /api/systems/{systemId}/sw-baseline | Get software baseline for a system |
| [**update_sw_baseline_assets**](SoftwareBaselineApi.md#update_sw_baseline_assets) | **PUT** /api/systems/{systemId}/sw-baseline | Update one or many software assets in a system |


## add_sw_baseline_assets

> <SwBaselineResponsePostPut> add_sw_baseline_assets(system_id, sw_baseline_required_fields)

Add one or many software assets in a system

Adds assets to the Software Baseline for given `systemId`  **Request Body Required Fields** - `softwareVendor` - `softwareName` - `version`

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

api_instance = EmassClient::SoftwareBaselineApi.new
system_id = 35 # Integer | **System Id**: The unique system record identifier.
sw_baseline_required_fields = [EmassClient::SwBaselineRequiredFields.new] # Array<SwBaselineRequiredFields> | Example request body for adding software baseline assets to an existing System (systemId)

begin
  # Add one or many software assets in a system
  result = api_instance.add_sw_baseline_assets(system_id, sw_baseline_required_fields)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling SoftwareBaselineApi->add_sw_baseline_assets: #{e}"
end
```

#### Using the add_sw_baseline_assets_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<SwBaselineResponsePostPut>, Integer, Hash)> add_sw_baseline_assets_with_http_info(system_id, sw_baseline_required_fields)

```ruby
begin
  # Add one or many software assets in a system
  data, status_code, headers = api_instance.add_sw_baseline_assets_with_http_info(system_id, sw_baseline_required_fields)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <SwBaselineResponsePostPut>
rescue EmassClient::ApiError => e
  puts "Error when calling SoftwareBaselineApi->add_sw_baseline_assets_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **system_id** | **Integer** | **System Id**: The unique system record identifier. |  |
| **sw_baseline_required_fields** | [**Array&lt;SwBaselineRequiredFields&gt;**](SwBaselineRequiredFields.md) | Example request body for adding software baseline assets to an existing System (systemId) |  |

### Return type

[**SwBaselineResponsePostPut**](SwBaselineResponsePostPut.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## delete_sw_baseline_assets

> <SwBaselineResponseDelete> delete_sw_baseline_assets(system_id, sw_baseline_request_delete_body_inner)

Delete one or many software assets in a system

Remove (delete) one or multiple assets from a system Software Baseline

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

api_instance = EmassClient::SoftwareBaselineApi.new
system_id = 35 # Integer | **System Id**: The unique system record identifier.
sw_baseline_request_delete_body_inner = [EmassClient::SwBaselineRequestDeleteBodyInner.new] # Array<SwBaselineRequestDeleteBodyInner> | Example request body for deleting one or many Software Baseline assets

begin
  # Delete one or many software assets in a system
  result = api_instance.delete_sw_baseline_assets(system_id, sw_baseline_request_delete_body_inner)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling SoftwareBaselineApi->delete_sw_baseline_assets: #{e}"
end
```

#### Using the delete_sw_baseline_assets_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<SwBaselineResponseDelete>, Integer, Hash)> delete_sw_baseline_assets_with_http_info(system_id, sw_baseline_request_delete_body_inner)

```ruby
begin
  # Delete one or many software assets in a system
  data, status_code, headers = api_instance.delete_sw_baseline_assets_with_http_info(system_id, sw_baseline_request_delete_body_inner)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <SwBaselineResponseDelete>
rescue EmassClient::ApiError => e
  puts "Error when calling SoftwareBaselineApi->delete_sw_baseline_assets_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **system_id** | **Integer** | **System Id**: The unique system record identifier. |  |
| **sw_baseline_request_delete_body_inner** | [**Array&lt;SwBaselineRequestDeleteBodyInner&gt;**](SwBaselineRequestDeleteBodyInner.md) | Example request body for deleting one or many Software Baseline assets |  |

### Return type

[**SwBaselineResponseDelete**](SwBaselineResponseDelete.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## get_system_sw_baseline

> <SwBaselineResponseGet> get_system_sw_baseline(system_id, opts)

Get software baseline for a system

Returns the software baseline for a system matching the `systemId` path parameter

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

api_instance = EmassClient::SoftwareBaselineApi.new
system_id = 35 # Integer | **System Id**: The unique system record identifier.
opts = {
  page_index: 56, # Integer | **Page Index**: If no value is specified, the default returns results from the first page with an index of 0. 
  page_size: 56 # Integer | **Page Size**: If no value is specified, the default returns 20000 per page. 
}

begin
  # Get software baseline for a system
  result = api_instance.get_system_sw_baseline(system_id, opts)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling SoftwareBaselineApi->get_system_sw_baseline: #{e}"
end
```

#### Using the get_system_sw_baseline_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<SwBaselineResponseGet>, Integer, Hash)> get_system_sw_baseline_with_http_info(system_id, opts)

```ruby
begin
  # Get software baseline for a system
  data, status_code, headers = api_instance.get_system_sw_baseline_with_http_info(system_id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <SwBaselineResponseGet>
rescue EmassClient::ApiError => e
  puts "Error when calling SoftwareBaselineApi->get_system_sw_baseline_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **system_id** | **Integer** | **System Id**: The unique system record identifier. |  |
| **page_index** | **Integer** | **Page Index**: If no value is specified, the default returns results from the first page with an index of 0.  | [optional][default to 0] |
| **page_size** | **Integer** | **Page Size**: If no value is specified, the default returns 20000 per page.  | [optional][default to 20000] |

### Return type

[**SwBaselineResponseGet**](SwBaselineResponseGet.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## update_sw_baseline_assets

> <SwBaselineResponsePostPut> update_sw_baseline_assets(system_id, sw_baseline_read_only_fields)

Update one or many software assets in a system

Updates assets in the Software Baseline for given `systemId`  **Request Body Required Fields** - `softwareId` - `softwareVendor` - `softwareName` - `version`

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

api_instance = EmassClient::SoftwareBaselineApi.new
system_id = 35 # Integer | **System Id**: The unique system record identifier.
sw_baseline_read_only_fields = [EmassClient::SwBaselineReadOnlyFields.new] # Array<SwBaselineReadOnlyFields> | Example request body for updating software baseline assets to an existing System (systemId)

begin
  # Update one or many software assets in a system
  result = api_instance.update_sw_baseline_assets(system_id, sw_baseline_read_only_fields)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling SoftwareBaselineApi->update_sw_baseline_assets: #{e}"
end
```

#### Using the update_sw_baseline_assets_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<SwBaselineResponsePostPut>, Integer, Hash)> update_sw_baseline_assets_with_http_info(system_id, sw_baseline_read_only_fields)

```ruby
begin
  # Update one or many software assets in a system
  data, status_code, headers = api_instance.update_sw_baseline_assets_with_http_info(system_id, sw_baseline_read_only_fields)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <SwBaselineResponsePostPut>
rescue EmassClient::ApiError => e
  puts "Error when calling SoftwareBaselineApi->update_sw_baseline_assets_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **system_id** | **Integer** | **System Id**: The unique system record identifier. |  |
| **sw_baseline_read_only_fields** | [**Array&lt;SwBaselineReadOnlyFields&gt;**](SwBaselineReadOnlyFields.md) | Example request body for updating software baseline assets to an existing System (systemId) |  |

### Return type

[**SwBaselineResponsePostPut**](SwBaselineResponsePostPut.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

