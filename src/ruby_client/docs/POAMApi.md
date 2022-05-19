# EmassClient::POAMApi

All URIs are relative to *http://localhost:4010*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**add_poam_by_system_id**](POAMApi.md#add_poam_by_system_id) | **POST** /api/systems/{systemId}/poams | Add one or many POA&amp;M items in a system |
| [**delete_poam**](POAMApi.md#delete_poam) | **DELETE** /api/systems/{systemId}/poams | Remove one or many POA&amp;M items in a system |
| [**get_system_poams**](POAMApi.md#get_system_poams) | **GET** /api/systems/{systemId}/poams | Get one or many POA&amp;M items in a system |
| [**get_system_poams_by_poam_id**](POAMApi.md#get_system_poams_by_poam_id) | **GET** /api/systems/{systemId}/poams/{poamId} | Get POA&amp;M item by ID in a system |
| [**update_poam_by_system_id**](POAMApi.md#update_poam_by_system_id) | **PUT** /api/systems/{systemId}/poams | Update one or many POA&amp;M items in a system |


## add_poam_by_system_id

> <PoamResponsePost> add_poam_by_system_id(system_id, request_body)

Add one or many POA&M items in a system

Add a POA&M for given `systemId`<br>  **Request Body Required Fields** - `status` - `vulnerabilityDescription` - `sourceIdentVuln` - `pocOrganization` - `resources`  **Note**<br /> If a POC email is supplied, the application will attempt to locate a user already registered within the application and pre-populate any information not explicitly supplied in the request. If no such user is found, these fields are **required** within the request.<br> `pocFirstName`, `pocLastName`, `pocPhoneNumber`<br />

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

api_instance = EmassClient::POAMApi.new
system_id = 35 # Integer | **System Id**: The unique system record identifier.
request_body = [3.56] # Array<Object> | Add POA&M(s) to a system (systemID)

begin
  # Add one or many POA&M items in a system
  result = api_instance.add_poam_by_system_id(system_id, request_body)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling POAMApi->add_poam_by_system_id: #{e}"
end
```

#### Using the add_poam_by_system_id_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PoamResponsePost>, Integer, Hash)> add_poam_by_system_id_with_http_info(system_id, request_body)

```ruby
begin
  # Add one or many POA&M items in a system
  data, status_code, headers = api_instance.add_poam_by_system_id_with_http_info(system_id, request_body)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PoamResponsePost>
rescue EmassClient::ApiError => e
  puts "Error when calling POAMApi->add_poam_by_system_id_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **system_id** | **Integer** | **System Id**: The unique system record identifier. |  |
| **request_body** | [**Array&lt;Object&gt;**](Object.md) | Add POA&amp;M(s) to a system (systemID) |  |

### Return type

[**PoamResponsePost**](PoamResponsePost.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## delete_poam

> <PoamResponseDelete> delete_poam(system_id, poam_request_delete_body_inner)

Remove one or many POA&M items in a system

Remove the POA&M matching `systemId` path parameter and `poamId` Request Body<br>

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

api_instance = EmassClient::POAMApi.new
system_id = 35 # Integer | **System Id**: The unique system record identifier.
poam_request_delete_body_inner = [EmassClient::PoamRequestDeleteBodyInner.new] # Array<PoamRequestDeleteBodyInner> | Delete the given POA&M Id

begin
  # Remove one or many POA&M items in a system
  result = api_instance.delete_poam(system_id, poam_request_delete_body_inner)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling POAMApi->delete_poam: #{e}"
end
```

#### Using the delete_poam_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PoamResponseDelete>, Integer, Hash)> delete_poam_with_http_info(system_id, poam_request_delete_body_inner)

```ruby
begin
  # Remove one or many POA&M items in a system
  data, status_code, headers = api_instance.delete_poam_with_http_info(system_id, poam_request_delete_body_inner)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PoamResponseDelete>
rescue EmassClient::ApiError => e
  puts "Error when calling POAMApi->delete_poam_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **system_id** | **Integer** | **System Id**: The unique system record identifier. |  |
| **poam_request_delete_body_inner** | [**Array&lt;PoamRequestDeleteBodyInner&gt;**](PoamRequestDeleteBodyInner.md) | Delete the given POA&amp;M Id |  |

### Return type

[**PoamResponseDelete**](PoamResponseDelete.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## get_system_poams

> <PoamResponseGetSystems> get_system_poams(system_id, opts)

Get one or many POA&M items in a system

Returns system(s) containing POA&M items for matching parameters.

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

api_instance = EmassClient::POAMApi.new
system_id = 35 # Integer | **System Id**: The unique system record identifier.
opts = {
  scheduled_completion_date_start: 'scheduled_completion_date_start_example', # String | **Date Started**: Filter query by the scheduled completion start date (Unix date format).
  scheduled_completion_date_end: 'scheduled_completion_date_end_example', # String | **Date Ended**: Filter query by the scheduled completion start date (Unix date format).
  control_acronyms: 'control_acronyms_example', # String | **System Acronym**: Filter query by given system acronym (single or comma separated).
  ccis: 'ccis_example', # String | **CCI System**: Filter query by Control Correlation Identifiers (CCIs) (single or comma separated).
  system_only: true # Boolean | **Systems Only**: Indicates that only system(s) information is retrieved.
}

begin
  # Get one or many POA&M items in a system
  result = api_instance.get_system_poams(system_id, opts)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling POAMApi->get_system_poams: #{e}"
end
```

#### Using the get_system_poams_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PoamResponseGetSystems>, Integer, Hash)> get_system_poams_with_http_info(system_id, opts)

```ruby
begin
  # Get one or many POA&M items in a system
  data, status_code, headers = api_instance.get_system_poams_with_http_info(system_id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PoamResponseGetSystems>
rescue EmassClient::ApiError => e
  puts "Error when calling POAMApi->get_system_poams_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **system_id** | **Integer** | **System Id**: The unique system record identifier. |  |
| **scheduled_completion_date_start** | **String** | **Date Started**: Filter query by the scheduled completion start date (Unix date format). | [optional] |
| **scheduled_completion_date_end** | **String** | **Date Ended**: Filter query by the scheduled completion start date (Unix date format). | [optional] |
| **control_acronyms** | **String** | **System Acronym**: Filter query by given system acronym (single or comma separated). | [optional] |
| **ccis** | **String** | **CCI System**: Filter query by Control Correlation Identifiers (CCIs) (single or comma separated). | [optional] |
| **system_only** | **Boolean** | **Systems Only**: Indicates that only system(s) information is retrieved. | [optional][default to true] |

### Return type

[**PoamResponseGetSystems**](PoamResponseGetSystems.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## get_system_poams_by_poam_id

> <PoamResponseGetPoams> get_system_poams_by_poam_id(system_id, poam_id)

Get POA&M item by ID in a system

Returns system(s) containing POA&M items for matching parameters.

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

api_instance = EmassClient::POAMApi.new
system_id = 35 # Integer | **System Id**: The unique system record identifier.
poam_id = 45 # Integer | **POA&M Id**: The unique POA&M record identifier.

begin
  # Get POA&M item by ID in a system
  result = api_instance.get_system_poams_by_poam_id(system_id, poam_id)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling POAMApi->get_system_poams_by_poam_id: #{e}"
end
```

#### Using the get_system_poams_by_poam_id_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PoamResponseGetPoams>, Integer, Hash)> get_system_poams_by_poam_id_with_http_info(system_id, poam_id)

```ruby
begin
  # Get POA&M item by ID in a system
  data, status_code, headers = api_instance.get_system_poams_by_poam_id_with_http_info(system_id, poam_id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PoamResponseGetPoams>
rescue EmassClient::ApiError => e
  puts "Error when calling POAMApi->get_system_poams_by_poam_id_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **system_id** | **Integer** | **System Id**: The unique system record identifier. |  |
| **poam_id** | **Integer** | **POA&amp;M Id**: The unique POA&amp;M record identifier. |  |

### Return type

[**PoamResponseGetPoams**](PoamResponseGetPoams.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## update_poam_by_system_id

> <PoamResponsePut> update_poam_by_system_id(system_id, request_body)

Update one or many POA&M items in a system

Update a POA&M for given `systemId`<br>  **Request Body Required Fields** - `poamId` - `displayPoamId` - `status` - `vulnerabilityDescription` - `sourceIdentVuln` - `pocOrganization` - `reviewStatus`  **Notes** - If a POC email is supplied, the application will attempt to locate a user already   registered within the application and pre-populate any information not explicitly supplied   in the request. If no such user is found, these fields are **required** within the request.<br>   `pocOrganization`, `pocFirstName`, `pocLastName`, `pocEmail`, `pocPhoneNumber`<br />  - To delete a milestone through the POA&M PUT the field `isActive` must be set to `false`: `isActive=false`.

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

api_instance = EmassClient::POAMApi.new
system_id = 35 # Integer | **System Id**: The unique system record identifier.
request_body = [3.56] # Array<Object> | Update an existing control by Id

begin
  # Update one or many POA&M items in a system
  result = api_instance.update_poam_by_system_id(system_id, request_body)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling POAMApi->update_poam_by_system_id: #{e}"
end
```

#### Using the update_poam_by_system_id_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PoamResponsePut>, Integer, Hash)> update_poam_by_system_id_with_http_info(system_id, request_body)

```ruby
begin
  # Update one or many POA&M items in a system
  data, status_code, headers = api_instance.update_poam_by_system_id_with_http_info(system_id, request_body)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PoamResponsePut>
rescue EmassClient::ApiError => e
  puts "Error when calling POAMApi->update_poam_by_system_id_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **system_id** | **Integer** | **System Id**: The unique system record identifier. |  |
| **request_body** | [**Array&lt;Object&gt;**](Object.md) | Update an existing control by Id |  |

### Return type

[**PoamResponsePut**](PoamResponsePut.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

