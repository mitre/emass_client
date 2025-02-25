# EmassClient::TestApi

All URIs are relative to *http://localhost:4010*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**test_connection**](TestApi.md#test_connection) | **GET** /api | Test connection to the API |


## test_connection

> <Test> test_connection

Test connection to the API

Tests the endpoint connection

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

api_instance = EmassClient::TestApi.new

begin
  # Test connection to the API
  result = api_instance.test_connection
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling TestApi->test_connection: #{e}"
end
```

#### Using the test_connection_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Test>, Integer, Hash)> test_connection_with_http_info

```ruby
begin
  # Test connection to the API
  data, status_code, headers = api_instance.test_connection_with_http_info
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Test>
rescue EmassClient::ApiError => e
  puts "Error when calling TestApi->test_connection_with_http_info: #{e}"
end
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**Test**](Test.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

