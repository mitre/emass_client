# EmassClient::ControlsApi

All URIs are relative to *http://localhost:4010*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**get_system_controls**](ControlsApi.md#get_system_controls) | **GET** /api/systems/{systemId}/controls | Get control information in a system for one or many controls |
| [**update_control_by_system_id**](ControlsApi.md#update_control_by_system_id) | **PUT** /api/systems/{systemId}/controls | Update control information in a system for one or many controls |


## get_system_controls

> <ControlsResponseGet> get_system_controls(system_id, opts)

Get control information in a system for one or many controls

Returns system control information for matching `systemId` path parameter

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

api_instance = EmassClient::ControlsApi.new
system_id = 35 # Integer | **System Id**: The unique system record identifier.
opts = {
  acronyms: 'acronyms_example' # String | **Acronym**: The system acronym(s) being queried (single value or comma delimited values).
}

begin
  # Get control information in a system for one or many controls
  result = api_instance.get_system_controls(system_id, opts)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling ControlsApi->get_system_controls: #{e}"
end
```

#### Using the get_system_controls_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ControlsResponseGet>, Integer, Hash)> get_system_controls_with_http_info(system_id, opts)

```ruby
begin
  # Get control information in a system for one or many controls
  data, status_code, headers = api_instance.get_system_controls_with_http_info(system_id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ControlsResponseGet>
rescue EmassClient::ApiError => e
  puts "Error when calling ControlsApi->get_system_controls_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **system_id** | **Integer** | **System Id**: The unique system record identifier. |  |
| **acronyms** | **String** | **Acronym**: The system acronym(s) being queried (single value or comma delimited values). | [optional][default to &#39;PM-6&#39;] |

### Return type

[**ControlsResponseGet**](ControlsResponseGet.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## update_control_by_system_id

> <ControlsResponsePut> update_control_by_system_id(system_id, request_body)

Update control information in a system for one or many controls

 Update a Control for given `systemId`<br>  **Request Body Required Fields** - `acronym` - `responsibleEntities` - `controlDesignation` - `estimatedCompletionDate` - `implementationNarrative`  The following optional fields are required based on the Implementation Status `implementationStatus` value<br> | Value                    | Required Fields |--------------------------|--------------------------------------------------- | Planned  or Implemented  | `estimatedCompletionDate`, `responsibleEntities`, `slcmCriticality`, `slcmFrequency`, `slcmMethod`, `slcmReporting`, `slcmTracking`, `slcmComments` | Not Applicable           | `naJustification`, `responsibleEntities` | Manually Inherited       | `commonControlProvider`, `estimatedCompletionDate`, `responsibleEntities`, `slcmCriticality`, `slcmFrequency`, `slcmMethod`, `slcmReporting`, `slcmTracking`, `slcmComments`  If the Implementation Status `implementationStatus` value is `Inherited`, only the following fields can be updated:   - `controlDesignation`   - `commonnControlProvider`

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

api_instance = EmassClient::ControlsApi.new
system_id = 35 # Integer | **System Id**: The unique system record identifier.
request_body = [3.56] # Array<Object> | Update an existing control by Id

begin
  # Update control information in a system for one or many controls
  result = api_instance.update_control_by_system_id(system_id, request_body)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling ControlsApi->update_control_by_system_id: #{e}"
end
```

#### Using the update_control_by_system_id_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ControlsResponsePut>, Integer, Hash)> update_control_by_system_id_with_http_info(system_id, request_body)

```ruby
begin
  # Update control information in a system for one or many controls
  data, status_code, headers = api_instance.update_control_by_system_id_with_http_info(system_id, request_body)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ControlsResponsePut>
rescue EmassClient::ApiError => e
  puts "Error when calling ControlsApi->update_control_by_system_id_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **system_id** | **Integer** | **System Id**: The unique system record identifier. |  |
| **request_body** | [**Array&lt;Object&gt;**](Object.md) | Update an existing control by Id |  |

### Return type

[**ControlsResponsePut**](ControlsResponsePut.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

