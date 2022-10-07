# EmassClient::RegistrationApi

All URIs are relative to *http://localhost:4010*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**register_user**](RegistrationApi.md#register_user) | **POST** /api/api-key | Register user certificate and obtain an API key |


## register_user

> <Register> register_user

Register user certificate and obtain an API key

Returns the API Key (api-key) that must be provided in the request header for all endpoint calls.

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

api_instance = EmassClient::RegistrationApi.new

begin
  # Register user certificate and obtain an API key
  result = api_instance.register_user
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling RegistrationApi->register_user: #{e}"
end
```

#### Using the register_user_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Register>, Integer, Hash)> register_user_with_http_info

```ruby
begin
  # Register user certificate and obtain an API key
  data, status_code, headers = api_instance.register_user_with_http_info
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Register>
rescue EmassClient::ApiError => e
  puts "Error when calling RegistrationApi->register_user_with_http_info: #{e}"
end
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**Register**](Register.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

