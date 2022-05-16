# EmassClient::MilestonesApi

All URIs are relative to *http://localhost:4010*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**add_milestone_by_system_id_and_poam_id**](MilestonesApi.md#add_milestone_by_system_id_and_poam_id) | **POST** /api/systems/{systemId}/poams/{poamId}/milestones | Add milestones to one or many POA&amp;M items in a system |
| [**delete_milestone**](MilestonesApi.md#delete_milestone) | **DELETE** /api/systems/{systemId}/poams/{poamId}/milestones | Remove milestones in a system for one or many POA&amp;M items |
| [**get_system_milestones_by_poam_id**](MilestonesApi.md#get_system_milestones_by_poam_id) | **GET** /api/systems/{systemId}/poams/{poamId}/milestones | Get milestones in one or many POA&amp;M items in a system |
| [**get_system_milestones_by_poam_id_and_milestone_id**](MilestonesApi.md#get_system_milestones_by_poam_id_and_milestone_id) | **GET** /api/systems/{systemId}/poams/{poamId}/milestones/{milestoneId} | Get milestone by ID in POA&amp;M item in a system |
| [**update_milestone_by_system_id_and_poam_id**](MilestonesApi.md#update_milestone_by_system_id_and_poam_id) | **PUT** /api/systems/{systemId}/poams/{poamId}/milestones | Update one or many POA&amp;M items in a system |


## add_milestone_by_system_id_and_poam_id

> <MilestoneResponsePost> add_milestone_by_system_id_and_poam_id(system_id, poam_id, request_body)

Add milestones to one or many POA&M items in a system

Adds a milestone for given `systemId` and `poamId` path parameters  **Request Body Required Fields** - `description` - `scheduledCompletionDate`

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

api_instance = EmassClient::MilestonesApi.new
system_id = 35 # Integer | **System Id**: The unique system record identifier.
poam_id = 45 # Integer | **POA&M Id**: The unique POA&M record identifier.
request_body = [3.56] # Array<Object> | Add milestones to an existing system poam

begin
  # Add milestones to one or many POA&M items in a system
  result = api_instance.add_milestone_by_system_id_and_poam_id(system_id, poam_id, request_body)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling MilestonesApi->add_milestone_by_system_id_and_poam_id: #{e}"
end
```

#### Using the add_milestone_by_system_id_and_poam_id_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<MilestoneResponsePost>, Integer, Hash)> add_milestone_by_system_id_and_poam_id_with_http_info(system_id, poam_id, request_body)

```ruby
begin
  # Add milestones to one or many POA&M items in a system
  data, status_code, headers = api_instance.add_milestone_by_system_id_and_poam_id_with_http_info(system_id, poam_id, request_body)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <MilestoneResponsePost>
rescue EmassClient::ApiError => e
  puts "Error when calling MilestonesApi->add_milestone_by_system_id_and_poam_id_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **system_id** | **Integer** | **System Id**: The unique system record identifier. |  |
| **poam_id** | **Integer** | **POA&amp;M Id**: The unique POA&amp;M record identifier. |  |
| **request_body** | [**Array&lt;Object&gt;**](Object.md) | Add milestones to an existing system poam |  |

### Return type

[**MilestoneResponsePost**](MilestoneResponsePost.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## delete_milestone

> <MilestonesPutPostDelete> delete_milestone(system_id, poam_id, delete_poams_inner1)

Remove milestones in a system for one or many POA&M items

Remove the POA&M matching `systemId` and `poamId` for path parameters and `milstoneId` provide in the Requst Body  **Notes**<br> To delete a milestone the record must be inactive by having the field isActive set to false (`isActive=false`).

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

api_instance = EmassClient::MilestonesApi.new
system_id = 35 # Integer | **System Id**: The unique system record identifier.
poam_id = 45 # Integer | **POA&M Id**: The unique POA&M record identifier.
delete_poams_inner1 = [EmassClient::DeletePoamsInner1.new] # Array<DeletePoamsInner1> | Delete the given Milestone Id

begin
  # Remove milestones in a system for one or many POA&M items
  result = api_instance.delete_milestone(system_id, poam_id, delete_poams_inner1)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling MilestonesApi->delete_milestone: #{e}"
end
```

#### Using the delete_milestone_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<MilestonesPutPostDelete>, Integer, Hash)> delete_milestone_with_http_info(system_id, poam_id, delete_poams_inner1)

```ruby
begin
  # Remove milestones in a system for one or many POA&M items
  data, status_code, headers = api_instance.delete_milestone_with_http_info(system_id, poam_id, delete_poams_inner1)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <MilestonesPutPostDelete>
rescue EmassClient::ApiError => e
  puts "Error when calling MilestonesApi->delete_milestone_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **system_id** | **Integer** | **System Id**: The unique system record identifier. |  |
| **poam_id** | **Integer** | **POA&amp;M Id**: The unique POA&amp;M record identifier. |  |
| **delete_poams_inner1** | [**Array&lt;DeletePoamsInner1&gt;**](DeletePoamsInner1.md) | Delete the given Milestone Id |  |

### Return type

[**MilestonesPutPostDelete**](MilestonesPutPostDelete.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## get_system_milestones_by_poam_id

> <MilestoneResponseGet> get_system_milestones_by_poam_id(system_id, poam_id, opts)

Get milestones in one or many POA&M items in a system

Returns system containing milestones for matching parameters.

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

api_instance = EmassClient::MilestonesApi.new
system_id = 35 # Integer | **System Id**: The unique system record identifier.
poam_id = 45 # Integer | **POA&M Id**: The unique POA&M record identifier.
opts = {
  scheduled_completion_date_start: 'scheduled_completion_date_start_example', # String | **Date Started**: Filter query by the scheduled completion start date (Unix date format).
  scheduled_completion_date_end: 'scheduled_completion_date_end_example' # String | **Date Ended**: Filter query by the scheduled completion start date (Unix date format).
}

begin
  # Get milestones in one or many POA&M items in a system
  result = api_instance.get_system_milestones_by_poam_id(system_id, poam_id, opts)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling MilestonesApi->get_system_milestones_by_poam_id: #{e}"
end
```

#### Using the get_system_milestones_by_poam_id_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<MilestoneResponseGet>, Integer, Hash)> get_system_milestones_by_poam_id_with_http_info(system_id, poam_id, opts)

```ruby
begin
  # Get milestones in one or many POA&M items in a system
  data, status_code, headers = api_instance.get_system_milestones_by_poam_id_with_http_info(system_id, poam_id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <MilestoneResponseGet>
rescue EmassClient::ApiError => e
  puts "Error when calling MilestonesApi->get_system_milestones_by_poam_id_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **system_id** | **Integer** | **System Id**: The unique system record identifier. |  |
| **poam_id** | **Integer** | **POA&amp;M Id**: The unique POA&amp;M record identifier. |  |
| **scheduled_completion_date_start** | **String** | **Date Started**: Filter query by the scheduled completion start date (Unix date format). | [optional] |
| **scheduled_completion_date_end** | **String** | **Date Ended**: Filter query by the scheduled completion start date (Unix date format). | [optional] |

### Return type

[**MilestoneResponseGet**](MilestoneResponseGet.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## get_system_milestones_by_poam_id_and_milestone_id

> <MilestoneResponseGetMilestone> get_system_milestones_by_poam_id_and_milestone_id(system_id, poam_id, milestone_id)

Get milestone by ID in POA&M item in a system

Returns systems containing milestones for matching parameters.

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

api_instance = EmassClient::MilestonesApi.new
system_id = 35 # Integer | **System Id**: The unique system record identifier.
poam_id = 45 # Integer | **POA&M Id**: The unique POA&M record identifier.
milestone_id = 77 # Integer | **Milestone Id**: The unique milestone record identifier.

begin
  # Get milestone by ID in POA&M item in a system
  result = api_instance.get_system_milestones_by_poam_id_and_milestone_id(system_id, poam_id, milestone_id)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling MilestonesApi->get_system_milestones_by_poam_id_and_milestone_id: #{e}"
end
```

#### Using the get_system_milestones_by_poam_id_and_milestone_id_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<MilestoneResponseGetMilestone>, Integer, Hash)> get_system_milestones_by_poam_id_and_milestone_id_with_http_info(system_id, poam_id, milestone_id)

```ruby
begin
  # Get milestone by ID in POA&M item in a system
  data, status_code, headers = api_instance.get_system_milestones_by_poam_id_and_milestone_id_with_http_info(system_id, poam_id, milestone_id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <MilestoneResponseGetMilestone>
rescue EmassClient::ApiError => e
  puts "Error when calling MilestonesApi->get_system_milestones_by_poam_id_and_milestone_id_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **system_id** | **Integer** | **System Id**: The unique system record identifier. |  |
| **poam_id** | **Integer** | **POA&amp;M Id**: The unique POA&amp;M record identifier. |  |
| **milestone_id** | **Integer** | **Milestone Id**: The unique milestone record identifier. |  |

### Return type

[**MilestoneResponseGetMilestone**](MilestoneResponseGetMilestone.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## update_milestone_by_system_id_and_poam_id

> <MilestoneResponsePut> update_milestone_by_system_id_and_poam_id(system_id, poam_id, request_body)

Update one or many POA&M items in a system

Updates a milestone for given `systemId` and `poamId` path parameters  **Request Body Required Fields** - `milestoneId` - `description` - `scheduledCompletionDate`

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

api_instance = EmassClient::MilestonesApi.new
system_id = 35 # Integer | **System Id**: The unique system record identifier.
poam_id = 45 # Integer | **POA&M Id**: The unique POA&M record identifier.
request_body = [3.56] # Array<Object> | Update milestones for an existing system poam

begin
  # Update one or many POA&M items in a system
  result = api_instance.update_milestone_by_system_id_and_poam_id(system_id, poam_id, request_body)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling MilestonesApi->update_milestone_by_system_id_and_poam_id: #{e}"
end
```

#### Using the update_milestone_by_system_id_and_poam_id_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<MilestoneResponsePut>, Integer, Hash)> update_milestone_by_system_id_and_poam_id_with_http_info(system_id, poam_id, request_body)

```ruby
begin
  # Update one or many POA&M items in a system
  data, status_code, headers = api_instance.update_milestone_by_system_id_and_poam_id_with_http_info(system_id, poam_id, request_body)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <MilestoneResponsePut>
rescue EmassClient::ApiError => e
  puts "Error when calling MilestonesApi->update_milestone_by_system_id_and_poam_id_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **system_id** | **Integer** | **System Id**: The unique system record identifier. |  |
| **poam_id** | **Integer** | **POA&amp;M Id**: The unique POA&amp;M record identifier. |  |
| **request_body** | [**Array&lt;Object&gt;**](Object.md) | Update milestones for an existing system poam |  |

### Return type

[**MilestoneResponsePut**](MilestoneResponsePut.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

