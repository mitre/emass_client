# EmassClient::PrivacyComplianceDashboardsApi

All URIs are relative to *http://localhost:4010*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**get_system_privacy_summary**](PrivacyComplianceDashboardsApi.md#get_system_privacy_summary) | **GET** /api/dashboards/system-privacy-summary | System Privacy Summary |
| [**get_va_omb_fsma_saop_summary**](PrivacyComplianceDashboardsApi.md#get_va_omb_fsma_saop_summary) | **GET** /api/dashboards/va-omb-fisma-saop-summary | VA OMB FISMA SAOP Summary |


## get_system_privacy_summary

> Object get_system_privacy_summary(org_id, opts)

System Privacy Summary

Get user system privacy summary dashboard information.

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

api_instance = EmassClient::PrivacyComplianceDashboardsApi.new
org_id = 1 # Integer | **Organization Id**: The unique organization identifier.
opts = {
  excludeinherited: true, # Boolean | **Exclude Inherited**: If no value is specified, the default returns false to include inherited data. 
  page_index: 56, # Integer | **Page Index**: If no value is specified, the default returns results from the first page with an index of 0. 
  page_size: 56 # Integer | **Page Size**: If no value is specified, the default returns 20000 per page. 
}

begin
  # System Privacy Summary
  result = api_instance.get_system_privacy_summary(org_id, opts)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling PrivacyComplianceDashboardsApi->get_system_privacy_summary: #{e}"
end
```

#### Using the get_system_privacy_summary_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(Object, Integer, Hash)> get_system_privacy_summary_with_http_info(org_id, opts)

```ruby
begin
  # System Privacy Summary
  data, status_code, headers = api_instance.get_system_privacy_summary_with_http_info(org_id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => Object
rescue EmassClient::ApiError => e
  puts "Error when calling PrivacyComplianceDashboardsApi->get_system_privacy_summary_with_http_info: #{e}"
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

**Object**

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## get_va_omb_fsma_saop_summary

> Object get_va_omb_fsma_saop_summary(org_id, opts)

VA OMB FISMA SAOP Summary

Get VA OMB-FISMA SAOP summary dashboard information.

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

api_instance = EmassClient::PrivacyComplianceDashboardsApi.new
org_id = 1 # Integer | **Organization Id**: The unique organization identifier.
opts = {
  excludeinherited: true, # Boolean | **Exclude Inherited**: If no value is specified, the default returns false to include inherited data. 
  page_index: 56, # Integer | **Page Index**: If no value is specified, the default returns results from the first page with an index of 0. 
  page_size: 56 # Integer | **Page Size**: If no value is specified, the default returns 20000 per page. 
}

begin
  # VA OMB FISMA SAOP Summary
  result = api_instance.get_va_omb_fsma_saop_summary(org_id, opts)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling PrivacyComplianceDashboardsApi->get_va_omb_fsma_saop_summary: #{e}"
end
```

#### Using the get_va_omb_fsma_saop_summary_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(Object, Integer, Hash)> get_va_omb_fsma_saop_summary_with_http_info(org_id, opts)

```ruby
begin
  # VA OMB FISMA SAOP Summary
  data, status_code, headers = api_instance.get_va_omb_fsma_saop_summary_with_http_info(org_id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => Object
rescue EmassClient::ApiError => e
  puts "Error when calling PrivacyComplianceDashboardsApi->get_va_omb_fsma_saop_summary_with_http_info: #{e}"
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

**Object**

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json
