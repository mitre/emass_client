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

> <ControlsResponsePut> update_control_by_system_id(system_id, controls_required_fields)

Update control information in a system for one or many controls

Update a Control for given `systemId`<br>  **Request Body Required Fields** - `acronym` - `responsibleEntities` - `controlDesignation` - `estimatedCompletionDate` - `implementationNarrative`  <br> **Business Rules**  The following **optional fields** (plus the **Request Body Required Fields**) are required based on the Implementation Status (`implementationStatus`) field value:<br>  <table>   <thead>     <tr><th><b>Status</b></th><th><b>Required Fields</b></th></tr>   </thead>   <tbody>     <tr><td><b>Planned</b> or <b>Implemented</b></td><td><code>slcmCriticality, slcmFrequency, slcmMethod, slcmReporting, slcmTracking, slcmComments</code></td></tr>     <tr><td><b>Not Applicable</b></td><td><code>naJustification</code></td></tr>     <tr><td><b>Manually Inherited</b></td><td><code>commonControlProvider, slcmCriticality, slcmFrequency, slcmMethod, slcmReporting, slcmTracking, slcmComments</code></td></tr>   </tbody> </table>   **NOTES:** - Risk Assessment information cannot be updated if a Security Control is `Inherited`. - Risk Assessment information cannot be updated for a DIACAP system record. - Implementation Plan information cannot be saved if the these fields exceed 2,000 character limits:   - `naJustification`,`responsibleEntities`,`implementationNarrative`,`slcmCriticality`   - `slcmFrequency`,`slcmMethod`,`slcmReporting`,`slcmTracking`,`slcmComments` - Implementation Plan or Risk Assessment information cannot be updated if Security Control does not exist in the system record.

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

api_instance = EmassClient::ControlsApi.new
system_id = 35 # Integer | **System Id**: The unique system record identifier.
controls_required_fields = [EmassClient::ControlsRequiredFields.new] # Array<ControlsRequiredFields> | Example request body for updating an existing control for a given system.

begin
  # Update control information in a system for one or many controls
  result = api_instance.update_control_by_system_id(system_id, controls_required_fields)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling ControlsApi->update_control_by_system_id: #{e}"
end
```

#### Using the update_control_by_system_id_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ControlsResponsePut>, Integer, Hash)> update_control_by_system_id_with_http_info(system_id, controls_required_fields)

```ruby
begin
  # Update control information in a system for one or many controls
  data, status_code, headers = api_instance.update_control_by_system_id_with_http_info(system_id, controls_required_fields)
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
| **controls_required_fields** | [**Array&lt;ControlsRequiredFields&gt;**](ControlsRequiredFields.md) | Example request body for updating an existing control for a given system. |  |

### Return type

[**ControlsResponsePut**](ControlsResponsePut.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

