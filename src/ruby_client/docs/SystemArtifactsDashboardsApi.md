# EmassClient::SystemArtifactsDashboardsApi

All URIs are relative to *http://localhost:4010*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**get_system_artifacts_details**](SystemArtifactsDashboardsApi.md#get_system_artifacts_details) | **GET** /api/dashboards/system-artifacts-details | System Artifacts Details |
| [**get_system_artifacts_summary**](SystemArtifactsDashboardsApi.md#get_system_artifacts_summary) | **GET** /api/dashboards/system-artifacts-summary | System Artifacts Summary |


## get_system_artifacts_details

> <GetSystemStatusDetails200Response> get_system_artifacts_details(org_id, opts)

System Artifacts Details

Get system Artifacts details information.

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

api_instance = EmassClient::SystemArtifactsDashboardsApi.new
org_id = 1 # Integer | **Organization Id**: The unique organization identifier.
opts = {
  excludeinherited: true, # Boolean | **Exclude Inherited**: If no value is specified, the default returns false to include inherited data. 
  page_index: 56, # Integer | **Page Index**: If no value is specified, the default returns results from the first page with an index of 0. 
  page_size: 56 # Integer | **Page Size**: If no value is specified, the default returns 20000 per page. 
}

begin
  # System Artifacts Details
  result = api_instance.get_system_artifacts_details(org_id, opts)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling SystemArtifactsDashboardsApi->get_system_artifacts_details: #{e}"
end
```

#### Using the get_system_artifacts_details_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<GetSystemStatusDetails200Response>, Integer, Hash)> get_system_artifacts_details_with_http_info(org_id, opts)

```ruby
begin
  # System Artifacts Details
  data, status_code, headers = api_instance.get_system_artifacts_details_with_http_info(org_id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <GetSystemStatusDetails200Response>
rescue EmassClient::ApiError => e
  puts "Error when calling SystemArtifactsDashboardsApi->get_system_artifacts_details_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **org_id** | **Integer** | **Organization Id**: The unique organization identifier. |  |
| **excludeinherited** | **Boolean** | **Exclude Inherited**: If no value is specified, the default returns false to include inherited data.  | [optional][default to false] |
| **page_index** | **Integer** | **Page Index**: If no value is specified, the default returns results from the first page with an index of 0.  | [optional][default to 0] |
| **page_size** | **Integer** | **Page Size**: If no value is specified, the default returns 20000 per page.  | [optional][default to 20000] |

### Return type

[**GetSystemStatusDetails200Response**](GetSystemStatusDetails200Response.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## get_system_artifacts_summary

> <GetSystemStatusDetails200Response> get_system_artifacts_summary(org_id, opts)

System Artifacts Summary

Get system Artifacts summary information.

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

api_instance = EmassClient::SystemArtifactsDashboardsApi.new
org_id = 1 # Integer | **Organization Id**: The unique organization identifier.
opts = {
  excludeinherited: true, # Boolean | **Exclude Inherited**: If no value is specified, the default returns false to include inherited data. 
  page_index: 56, # Integer | **Page Index**: If no value is specified, the default returns results from the first page with an index of 0. 
  page_size: 56 # Integer | **Page Size**: If no value is specified, the default returns 20000 per page. 
}

begin
  # System Artifacts Summary
  result = api_instance.get_system_artifacts_summary(org_id, opts)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling SystemArtifactsDashboardsApi->get_system_artifacts_summary: #{e}"
end
```

#### Using the get_system_artifacts_summary_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<GetSystemStatusDetails200Response>, Integer, Hash)> get_system_artifacts_summary_with_http_info(org_id, opts)

```ruby
begin
  # System Artifacts Summary
  data, status_code, headers = api_instance.get_system_artifacts_summary_with_http_info(org_id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <GetSystemStatusDetails200Response>
rescue EmassClient::ApiError => e
  puts "Error when calling SystemArtifactsDashboardsApi->get_system_artifacts_summary_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **org_id** | **Integer** | **Organization Id**: The unique organization identifier. |  |
| **excludeinherited** | **Boolean** | **Exclude Inherited**: If no value is specified, the default returns false to include inherited data.  | [optional][default to false] |
| **page_index** | **Integer** | **Page Index**: If no value is specified, the default returns results from the first page with an index of 0.  | [optional][default to 0] |
| **page_size** | **Integer** | **Page Size**: If no value is specified, the default returns 20000 per page.  | [optional][default to 20000] |

### Return type

[**GetSystemStatusDetails200Response**](GetSystemStatusDetails200Response.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

