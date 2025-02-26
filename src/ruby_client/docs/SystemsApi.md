# EmassClient::SystemsApi

All URIs are relative to *http://localhost:4010*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**get_system**](SystemsApi.md#get_system) | **GET** /api/systems/{systemId} | Get system information for a specific system |
| [**get_systems**](SystemsApi.md#get_systems) | **GET** /api/systems | Get system information |


## get_system

> <SystemResponse> get_system(system_id, opts)

Get system information for a specific system

Returns the system matching provided parameters

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

api_instance = EmassClient::SystemsApi.new
system_id = 35 # Integer | **System Id**: The unique system record identifier.
opts = {
  policy: 'diacap' # String | **System Policy**: Filter query by system policy. If no value is specified, the default returns RMF policy information for dual-policy systems.
}

begin
  # Get system information for a specific system
  result = api_instance.get_system(system_id, opts)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling SystemsApi->get_system: #{e}"
end
```

#### Using the get_system_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<SystemResponse>, Integer, Hash)> get_system_with_http_info(system_id, opts)

```ruby
begin
  # Get system information for a specific system
  data, status_code, headers = api_instance.get_system_with_http_info(system_id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <SystemResponse>
rescue EmassClient::ApiError => e
  puts "Error when calling SystemsApi->get_system_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **system_id** | **Integer** | **System Id**: The unique system record identifier. |  |
| **policy** | **String** | **System Policy**: Filter query by system policy. If no value is specified, the default returns RMF policy information for dual-policy systems. | [optional][default to &#39;rmf&#39;] |

### Return type

[**SystemResponse**](SystemResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## get_systems

> <SystemsResponse> get_systems(opts)

Get system information

Returns all system(s) that match the query parameters

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

api_instance = EmassClient::SystemsApi.new
opts = {
  coams_id: 'coams_id_example', # String | **COAMS ID**: Filter query by Cyber Operational Attributes Management System (COAMS).
  ditpr_id: 'ditpr_id_example', # String | **DITPR ID**: Filter query by DoD Information Technology (IT) Portfolio Repository (DITPR).
  include_decommissioned: true, # Boolean | **Include Decommissioned Systems**: Indicates if decommissioned systems are retrieved. If no value is specified, the default returns true to include decommissioned systems.
  include_ditpr_metrics: true, # Boolean | **Include DITPR**: Indicates if DITPR metrics are retrieved. This query string parameter cannot be used in conjunction with the following parameters:   - ditprId   - coamsId  If no value is specified, the default returns false to not include DITPR Metrics.
  policy: 'diacap', # String | **System Policy**: Filter query by system policy. If no value is specified, the default returns RMF policy information for dual-policy systems.
  registration_type: 'registration_type_example', # String | **Registration Type**: Filter record by selected registration type (single value or comma delimited values).  **Valid Options Are:** assessAndAuthorize, assessOnly, guest, regular, functional, cloudServiceProvider, commonControlProvider, authorizationToUse, reciprocityAcceptanc 
  reports_for_scorecard: true # Boolean | **DoD Cyber Hygiene Scorecard**: Used to filter results to only return systems that report to the DoD Cyber Hygiene Scorecard.
}

begin
  # Get system information
  result = api_instance.get_systems(opts)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling SystemsApi->get_systems: #{e}"
end
```

#### Using the get_systems_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<SystemsResponse>, Integer, Hash)> get_systems_with_http_info(opts)

```ruby
begin
  # Get system information
  data, status_code, headers = api_instance.get_systems_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <SystemsResponse>
rescue EmassClient::ApiError => e
  puts "Error when calling SystemsApi->get_systems_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **coams_id** | **String** | **COAMS ID**: Filter query by Cyber Operational Attributes Management System (COAMS). | [optional] |
| **ditpr_id** | **String** | **DITPR ID**: Filter query by DoD Information Technology (IT) Portfolio Repository (DITPR). | [optional] |
| **include_decommissioned** | **Boolean** | **Include Decommissioned Systems**: Indicates if decommissioned systems are retrieved. If no value is specified, the default returns true to include decommissioned systems. | [optional][default to true] |
| **include_ditpr_metrics** | **Boolean** | **Include DITPR**: Indicates if DITPR metrics are retrieved. This query string parameter cannot be used in conjunction with the following parameters:   - ditprId   - coamsId  If no value is specified, the default returns false to not include DITPR Metrics. | [optional][default to false] |
| **policy** | **String** | **System Policy**: Filter query by system policy. If no value is specified, the default returns RMF policy information for dual-policy systems. | [optional][default to &#39;rmf&#39;] |
| **registration_type** | **String** | **Registration Type**: Filter record by selected registration type (single value or comma delimited values).  **Valid Options Are:** assessAndAuthorize, assessOnly, guest, regular, functional, cloudServiceProvider, commonControlProvider, authorizationToUse, reciprocityAcceptanc  | [optional][default to &#39;regular&#39;] |
| **reports_for_scorecard** | **Boolean** | **DoD Cyber Hygiene Scorecard**: Used to filter results to only return systems that report to the DoD Cyber Hygiene Scorecard. | [optional][default to true] |

### Return type

[**SystemsResponse**](SystemsResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

