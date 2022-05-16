# EmassClient::CACApi

All URIs are relative to *http://localhost:4010*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**add_system_cac**](CACApi.md#add_system_cac) | **POST** /api/systems/{systemId}/approval/cac | Submit control to second role of CAC |
| [**get_system_cac**](CACApi.md#get_system_cac) | **GET** /api/systems/{systemId}/approval/cac | Get location of one or many controls in CAC |


## add_system_cac

> <CacResponsePost> add_system_cac(system_id, request_body)

Submit control to second role of CAC

Adds a Control Approval Chain (CAC) for given `systemId` path parameter<br><br> POST requests will only yield successful results if the control is currently sitting at the first role of the CAC. If the control is not currently sitting at the first role, then an error will be returned.

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

api_instance = EmassClient::CACApi.new
system_id = 35 # Integer | **System Id**: The unique system record identifier.
request_body = [3.56] # Array<Object> | Add control(s) to second role of CAC

begin
  # Submit control to second role of CAC
  result = api_instance.add_system_cac(system_id, request_body)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling CACApi->add_system_cac: #{e}"
end
```

#### Using the add_system_cac_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<CacResponsePost>, Integer, Hash)> add_system_cac_with_http_info(system_id, request_body)

```ruby
begin
  # Submit control to second role of CAC
  data, status_code, headers = api_instance.add_system_cac_with_http_info(system_id, request_body)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <CacResponsePost>
rescue EmassClient::ApiError => e
  puts "Error when calling CACApi->add_system_cac_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **system_id** | **Integer** | **System Id**: The unique system record identifier. |  |
| **request_body** | [**Array&lt;Object&gt;**](Object.md) | Add control(s) to second role of CAC |  |

### Return type

[**CacResponsePost**](CacResponsePost.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## get_system_cac

> <CacResponseGet> get_system_cac(system_id, opts)

Get location of one or many controls in CAC

Returns the location of a system's package in the Control Approval Chain (CAC) for matching `systemId` path parameter

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

api_instance = EmassClient::CACApi.new
system_id = 35 # Integer | **System Id**: The unique system record identifier.
opts = {
  control_acronyms: 'control_acronyms_example' # String | **System Acronym**: Filter query by given system acronym (single or comma separated).
}

begin
  # Get location of one or many controls in CAC
  result = api_instance.get_system_cac(system_id, opts)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling CACApi->get_system_cac: #{e}"
end
```

#### Using the get_system_cac_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<CacResponseGet>, Integer, Hash)> get_system_cac_with_http_info(system_id, opts)

```ruby
begin
  # Get location of one or many controls in CAC
  data, status_code, headers = api_instance.get_system_cac_with_http_info(system_id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <CacResponseGet>
rescue EmassClient::ApiError => e
  puts "Error when calling CACApi->get_system_cac_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **system_id** | **Integer** | **System Id**: The unique system record identifier. |  |
| **control_acronyms** | **String** | **System Acronym**: Filter query by given system acronym (single or comma separated). | [optional] |

### Return type

[**CacResponseGet**](CacResponseGet.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

