# EmassClient::WorkflowDefinitionsApi

All URIs are relative to *http://localhost:4010*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**get_workflow_definitions**](WorkflowDefinitionsApi.md#get_workflow_definitions) | **GET** /api/workflows/definitions | Get workflow definitions in a site |


## get_workflow_definitions

> <WorkflowDefinitionResponseGet> get_workflow_definitions(opts)

Get workflow definitions in a site

View all workflow schemas available on the eMASS instance filtered by status `includeInactive` and registration type `registrationType`.

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

api_instance = EmassClient::WorkflowDefinitionsApi.new
opts = {
  include_inactive: true, # Boolean | **Include Inactive**: If no value is specified, the default returns false to not include outdated workflow definitions.
  registration_type: 'registration_type_example' # String | **Registration Type**: Filter record by selected registration type (single value or comma delimited values).  **Valid Options Are:** assessAndAuthorize, assessOnly, guest, regular, functional, cloudServiceProvider, commonControlProvider, authorizationToUse, reciprocityAcceptanc 
}

begin
  # Get workflow definitions in a site
  result = api_instance.get_workflow_definitions(opts)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling WorkflowDefinitionsApi->get_workflow_definitions: #{e}"
end
```

#### Using the get_workflow_definitions_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<WorkflowDefinitionResponseGet>, Integer, Hash)> get_workflow_definitions_with_http_info(opts)

```ruby
begin
  # Get workflow definitions in a site
  data, status_code, headers = api_instance.get_workflow_definitions_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <WorkflowDefinitionResponseGet>
rescue EmassClient::ApiError => e
  puts "Error when calling WorkflowDefinitionsApi->get_workflow_definitions_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **include_inactive** | **Boolean** | **Include Inactive**: If no value is specified, the default returns false to not include outdated workflow definitions. | [optional][default to true] |
| **registration_type** | **String** | **Registration Type**: Filter record by selected registration type (single value or comma delimited values).  **Valid Options Are:** assessAndAuthorize, assessOnly, guest, regular, functional, cloudServiceProvider, commonControlProvider, authorizationToUse, reciprocityAcceptanc  | [optional][default to &#39;regular&#39;] |

### Return type

[**WorkflowDefinitionResponseGet**](WorkflowDefinitionResponseGet.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

