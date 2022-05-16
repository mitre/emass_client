# EmassClient::WorkflowInstancesApi

All URIs are relative to *http://localhost:4010*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**get_system_workflow_instances**](WorkflowInstancesApi.md#get_system_workflow_instances) | **GET** /api/workflows/instances | Get workflow instances in a site |
| [**get_system_workflow_instances_by_workflow_instance_id**](WorkflowInstancesApi.md#get_system_workflow_instances_by_workflow_instance_id) | **GET** /api/workflows/instances/{workflowInstanceId} | Get workflow instance by ID |


## get_system_workflow_instances

> <WorkflowInstancesResponseGet> get_system_workflow_instances(opts)

Get workflow instances in a site

View detailed information on all active and historical workflows filtered by provided parameters.

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

api_instance = EmassClient::WorkflowInstancesApi.new
opts = {
  include_comments: true, # Boolean | **Include Comments**: If no value is specified, the default returns true to not include transition comments.  Note: Corresponds to the Comments textbox that is required at most workflow transitions. Does not include other text input fields such as Terms / Conditions for Authorization. 
  page_index: 56, # Integer | **Page Index**: If no value is specified, the default returns true to not include transition comments.
  since_date: '1638764040', # String | **Date**: Filter on authorization/assessment date (Unix date format).  Note: Filters off the lastEditedDate field.  Note: The authorization/assessment decisions on completed workflows  can be edited for up to 30 days after the initial decision is made. 
  status: 'active' # String | **Status**: Filter by status.  If no value is specified, the default returns all to include both active and inactive workflows.  Note: Any workflows at a current stage of Complete or Cancelled are inactive. Ongoing workflows currently at other stages are active. 
}

begin
  # Get workflow instances in a site
  result = api_instance.get_system_workflow_instances(opts)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling WorkflowInstancesApi->get_system_workflow_instances: #{e}"
end
```

#### Using the get_system_workflow_instances_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<WorkflowInstancesResponseGet>, Integer, Hash)> get_system_workflow_instances_with_http_info(opts)

```ruby
begin
  # Get workflow instances in a site
  data, status_code, headers = api_instance.get_system_workflow_instances_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <WorkflowInstancesResponseGet>
rescue EmassClient::ApiError => e
  puts "Error when calling WorkflowInstancesApi->get_system_workflow_instances_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **include_comments** | **Boolean** | **Include Comments**: If no value is specified, the default returns true to not include transition comments.  Note: Corresponds to the Comments textbox that is required at most workflow transitions. Does not include other text input fields such as Terms / Conditions for Authorization.  | [optional][default to true] |
| **page_index** | **Integer** | **Page Index**: If no value is specified, the default returns true to not include transition comments. | [optional][default to 0] |
| **since_date** | **String** | **Date**: Filter on authorization/assessment date (Unix date format).  Note: Filters off the lastEditedDate field.  Note: The authorization/assessment decisions on completed workflows  can be edited for up to 30 days after the initial decision is made.  | [optional] |
| **status** | **String** | **Status**: Filter by status.  If no value is specified, the default returns all to include both active and inactive workflows.  Note: Any workflows at a current stage of Complete or Cancelled are inactive. Ongoing workflows currently at other stages are active.  | [optional][default to &#39;all&#39;] |

### Return type

[**WorkflowInstancesResponseGet**](WorkflowInstancesResponseGet.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## get_system_workflow_instances_by_workflow_instance_id

> <WorkflowInstanceResponseGet> get_system_workflow_instances_by_workflow_instance_id(workflow_instance_id)

Get workflow instance by ID

View detailed historical workflow information for `workflowInstanceId`.

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

api_instance = EmassClient::WorkflowInstancesApi.new
workflow_instance_id = 123 # Integer | **Workflow Instance Id**: The unique workflow definition identifier.

begin
  # Get workflow instance by ID
  result = api_instance.get_system_workflow_instances_by_workflow_instance_id(workflow_instance_id)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling WorkflowInstancesApi->get_system_workflow_instances_by_workflow_instance_id: #{e}"
end
```

#### Using the get_system_workflow_instances_by_workflow_instance_id_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<WorkflowInstanceResponseGet>, Integer, Hash)> get_system_workflow_instances_by_workflow_instance_id_with_http_info(workflow_instance_id)

```ruby
begin
  # Get workflow instance by ID
  data, status_code, headers = api_instance.get_system_workflow_instances_by_workflow_instance_id_with_http_info(workflow_instance_id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <WorkflowInstanceResponseGet>
rescue EmassClient::ApiError => e
  puts "Error when calling WorkflowInstancesApi->get_system_workflow_instances_by_workflow_instance_id_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **workflow_instance_id** | **Integer** | **Workflow Instance Id**: The unique workflow definition identifier. |  |

### Return type

[**WorkflowInstanceResponseGet**](WorkflowInstanceResponseGet.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

