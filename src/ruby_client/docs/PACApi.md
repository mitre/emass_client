# EmassClient::PACApi

All URIs are relative to *http://localhost:4010*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**add_system_pac**](PACApi.md#add_system_pac) | **POST** /api/systems/{systemId}/approval/pac | Submit system package for review |
| [**get_system_pac**](PACApi.md#get_system_pac) | **GET** /api/systems/{systemId}/approval/pac | Get location of system package in PAC |


## add_system_pac

> <PacResponsePost> add_system_pac(system_id, request_body)

Submit system package for review

Adds a Package Approval Chain (PAC) for given `systemId` path parameter

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

api_instance = EmassClient::PACApi.new
system_id = 35 # Integer | **System Id**: The unique system record identifier.
request_body = [3.56] # Array<Object> | Add system package to PAC for review

begin
  # Submit system package for review
  result = api_instance.add_system_pac(system_id, request_body)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling PACApi->add_system_pac: #{e}"
end
```

#### Using the add_system_pac_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PacResponsePost>, Integer, Hash)> add_system_pac_with_http_info(system_id, request_body)

```ruby
begin
  # Submit system package for review
  data, status_code, headers = api_instance.add_system_pac_with_http_info(system_id, request_body)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PacResponsePost>
rescue EmassClient::ApiError => e
  puts "Error when calling PACApi->add_system_pac_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **system_id** | **Integer** | **System Id**: The unique system record identifier. |  |
| **request_body** | [**Array&lt;Object&gt;**](Object.md) | Add system package to PAC for review |  |

### Return type

[**PacResponsePost**](PacResponsePost.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## get_system_pac

> <PacResponseGet> get_system_pac(system_id)

Get location of system package in PAC

Returns the location of a system's package in the Package Approval Chain (PAC) for matching `systemId` path parameter

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

api_instance = EmassClient::PACApi.new
system_id = 35 # Integer | **System Id**: The unique system record identifier.

begin
  # Get location of system package in PAC
  result = api_instance.get_system_pac(system_id)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling PACApi->get_system_pac: #{e}"
end
```

#### Using the get_system_pac_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PacResponseGet>, Integer, Hash)> get_system_pac_with_http_info(system_id)

```ruby
begin
  # Get location of system package in PAC
  data, status_code, headers = api_instance.get_system_pac_with_http_info(system_id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PacResponseGet>
rescue EmassClient::ApiError => e
  puts "Error when calling PACApi->get_system_pac_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **system_id** | **Integer** | **System Id**: The unique system record identifier. |  |

### Return type

[**PacResponseGet**](PacResponseGet.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

