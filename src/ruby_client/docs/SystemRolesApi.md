# EmassClient::SystemRolesApi

All URIs are relative to *http://localhost:4010*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**get_system_roles**](SystemRolesApi.md#get_system_roles) | **GET** /api/system-roles | Get available roles |
| [**get_system_roles_by_category_id**](SystemRolesApi.md#get_system_roles_by_category_id) | **GET** /api/system-roles/{roleCategory} | Get system roles |


## get_system_roles

> <SystemRolesResponse> get_system_roles

Get available roles

Returns all available roles

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

api_instance = EmassClient::SystemRolesApi.new

begin
  # Get available roles
  result = api_instance.get_system_roles
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling SystemRolesApi->get_system_roles: #{e}"
end
```

#### Using the get_system_roles_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<SystemRolesResponse>, Integer, Hash)> get_system_roles_with_http_info

```ruby
begin
  # Get available roles
  data, status_code, headers = api_instance.get_system_roles_with_http_info
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <SystemRolesResponse>
rescue EmassClient::ApiError => e
  puts "Error when calling SystemRolesApi->get_system_roles_with_http_info: #{e}"
end
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**SystemRolesResponse**](SystemRolesResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## get_system_roles_by_category_id

> <SystemRolesCategoryResponse> get_system_roles_by_category_id(role_category, role, opts)

Get system roles

Returns the role(s) data matching parameters.

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

api_instance = EmassClient::SystemRolesApi.new
role_category = 'CAC' # String | **Role Category**: The system role category been queried
role = 'role_example' # String | **Role**: Accepts single value from options available at base system-roles endpoint e.g., SCA.
opts = {
  policy: 'diacap' # String | **System Policy**: Filter query by system policy.  If no value is specified, the default returns RMF policy information for dual-policy systems.
}

begin
  # Get system roles
  result = api_instance.get_system_roles_by_category_id(role_category, role, opts)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling SystemRolesApi->get_system_roles_by_category_id: #{e}"
end
```

#### Using the get_system_roles_by_category_id_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<SystemRolesCategoryResponse>, Integer, Hash)> get_system_roles_by_category_id_with_http_info(role_category, role, opts)

```ruby
begin
  # Get system roles
  data, status_code, headers = api_instance.get_system_roles_by_category_id_with_http_info(role_category, role, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <SystemRolesCategoryResponse>
rescue EmassClient::ApiError => e
  puts "Error when calling SystemRolesApi->get_system_roles_by_category_id_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **role_category** | **String** | **Role Category**: The system role category been queried | [default to &#39;PAC&#39;] |
| **role** | **String** | **Role**: Accepts single value from options available at base system-roles endpoint e.g., SCA. | [default to &#39;IAO&#39;] |
| **policy** | **String** | **System Policy**: Filter query by system policy.  If no value is specified, the default returns RMF policy information for dual-policy systems. | [optional][default to &#39;rmf&#39;] |

### Return type

[**SystemRolesCategoryResponse**](SystemRolesCategoryResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

