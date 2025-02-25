# EmassClient::VASystemDashboardsApi

All URIs are relative to *http://localhost:4010*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**get_va_system_a2_summary**](VASystemDashboardsApi.md#get_va_system_a2_summary) | **GET** /api/dashboards/va-system-a2-summary | VA System A2.0 Summary |
| [**get_va_system_aa_summary**](VASystemDashboardsApi.md#get_va_system_aa_summary) | **GET** /api/dashboards/va-system-aa-summary | VA System A&amp;A Summary |
| [**get_va_system_fisma_invetory_crypto_summary**](VASystemDashboardsApi.md#get_va_system_fisma_invetory_crypto_summary) | **GET** /api/dashboards/va-system-fisma-inventory-crypto-summary | VA System FISMA Inventory Crypto Summary |
| [**get_va_system_fisma_invetory_summary**](VASystemDashboardsApi.md#get_va_system_fisma_invetory_summary) | **GET** /api/dashboards/va-system-fisma-inventory-summary | VA System FISMA Inventory Summary |
| [**get_va_system_icamp_tableau_poam_details**](VASystemDashboardsApi.md#get_va_system_icamp_tableau_poam_details) | **GET** /api/dashboards/va-system-icamp-tableau-poam-details | VA System ICAMP Tableau POAM Details |
| [**get_va_system_pl109_reporting_summary**](VASystemDashboardsApi.md#get_va_system_pl109_reporting_summary) | **GET** /api/dashboards/va-system-pl-109-reporting-summary | VA System P.L. 109 Reporting Summary |
| [**get_va_system_threat_architecture_details**](VASystemDashboardsApi.md#get_va_system_threat_architecture_details) | **GET** /api/dashboards/va-system-threat-architecture-details | VA System Threat Architecture Details |
| [**get_va_system_threat_risk_summary**](VASystemDashboardsApi.md#get_va_system_threat_risk_summary) | **GET** /api/dashboards/va-system-threat-risks-summary | VA System Threat Risks Summary |
| [**get_va_system_threat_source_details**](VASystemDashboardsApi.md#get_va_system_threat_source_details) | **GET** /api/dashboards/va-system-threat-sources-details | VA System Threat Sources Details |


## get_va_system_a2_summary

> <GetSystemStatusDetails200Response> get_va_system_a2_summary(org_id, opts)

VA System A2.0 Summary

Get VA system A2.0 summary dashboard information.

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

api_instance = EmassClient::VASystemDashboardsApi.new
org_id = 1 # Integer | **Organization Id**: The unique organization identifier.
opts = {
  excludeinherited: true, # Boolean | **Exclude Inherited**: If no value is specified, the default returns false to include inherited data. 
  page_index: 56, # Integer | **Page Index**: If no value is specified, the default returns results from the first page with an index of 0. 
  page_size: 56 # Integer | **Page Size**: If no value is specified, the default returns 20000 per page. 
}

begin
  # VA System A2.0 Summary
  result = api_instance.get_va_system_a2_summary(org_id, opts)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling VASystemDashboardsApi->get_va_system_a2_summary: #{e}"
end
```

#### Using the get_va_system_a2_summary_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<GetSystemStatusDetails200Response>, Integer, Hash)> get_va_system_a2_summary_with_http_info(org_id, opts)

```ruby
begin
  # VA System A2.0 Summary
  data, status_code, headers = api_instance.get_va_system_a2_summary_with_http_info(org_id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <GetSystemStatusDetails200Response>
rescue EmassClient::ApiError => e
  puts "Error when calling VASystemDashboardsApi->get_va_system_a2_summary_with_http_info: #{e}"
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


## get_va_system_aa_summary

> <GetSystemStatusDetails200Response> get_va_system_aa_summary(org_id, opts)

VA System A&A Summary

Get VA system A&A summary dashboard information.

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

api_instance = EmassClient::VASystemDashboardsApi.new
org_id = 1 # Integer | **Organization Id**: The unique organization identifier.
opts = {
  excludeinherited: true, # Boolean | **Exclude Inherited**: If no value is specified, the default returns false to include inherited data. 
  page_index: 56, # Integer | **Page Index**: If no value is specified, the default returns results from the first page with an index of 0. 
  page_size: 56 # Integer | **Page Size**: If no value is specified, the default returns 20000 per page. 
}

begin
  # VA System A&A Summary
  result = api_instance.get_va_system_aa_summary(org_id, opts)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling VASystemDashboardsApi->get_va_system_aa_summary: #{e}"
end
```

#### Using the get_va_system_aa_summary_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<GetSystemStatusDetails200Response>, Integer, Hash)> get_va_system_aa_summary_with_http_info(org_id, opts)

```ruby
begin
  # VA System A&A Summary
  data, status_code, headers = api_instance.get_va_system_aa_summary_with_http_info(org_id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <GetSystemStatusDetails200Response>
rescue EmassClient::ApiError => e
  puts "Error when calling VASystemDashboardsApi->get_va_system_aa_summary_with_http_info: #{e}"
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


## get_va_system_fisma_invetory_crypto_summary

> <GetSystemStatusDetails200Response> get_va_system_fisma_invetory_crypto_summary(org_id, opts)

VA System FISMA Inventory Crypto Summary

Get VA system FISMA inventory crypto summary dashboard information.

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

api_instance = EmassClient::VASystemDashboardsApi.new
org_id = 1 # Integer | **Organization Id**: The unique organization identifier.
opts = {
  excludeinherited: true, # Boolean | **Exclude Inherited**: If no value is specified, the default returns false to include inherited data. 
  page_index: 56, # Integer | **Page Index**: If no value is specified, the default returns results from the first page with an index of 0. 
  page_size: 56 # Integer | **Page Size**: If no value is specified, the default returns 20000 per page. 
}

begin
  # VA System FISMA Inventory Crypto Summary
  result = api_instance.get_va_system_fisma_invetory_crypto_summary(org_id, opts)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling VASystemDashboardsApi->get_va_system_fisma_invetory_crypto_summary: #{e}"
end
```

#### Using the get_va_system_fisma_invetory_crypto_summary_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<GetSystemStatusDetails200Response>, Integer, Hash)> get_va_system_fisma_invetory_crypto_summary_with_http_info(org_id, opts)

```ruby
begin
  # VA System FISMA Inventory Crypto Summary
  data, status_code, headers = api_instance.get_va_system_fisma_invetory_crypto_summary_with_http_info(org_id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <GetSystemStatusDetails200Response>
rescue EmassClient::ApiError => e
  puts "Error when calling VASystemDashboardsApi->get_va_system_fisma_invetory_crypto_summary_with_http_info: #{e}"
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


## get_va_system_fisma_invetory_summary

> <GetSystemStatusDetails200Response> get_va_system_fisma_invetory_summary(org_id, opts)

VA System FISMA Inventory Summary

Get VA system FISMA inventory summary dashboard information.

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

api_instance = EmassClient::VASystemDashboardsApi.new
org_id = 1 # Integer | **Organization Id**: The unique organization identifier.
opts = {
  excludeinherited: true, # Boolean | **Exclude Inherited**: If no value is specified, the default returns false to include inherited data. 
  page_index: 56, # Integer | **Page Index**: If no value is specified, the default returns results from the first page with an index of 0. 
  page_size: 56 # Integer | **Page Size**: If no value is specified, the default returns 20000 per page. 
}

begin
  # VA System FISMA Inventory Summary
  result = api_instance.get_va_system_fisma_invetory_summary(org_id, opts)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling VASystemDashboardsApi->get_va_system_fisma_invetory_summary: #{e}"
end
```

#### Using the get_va_system_fisma_invetory_summary_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<GetSystemStatusDetails200Response>, Integer, Hash)> get_va_system_fisma_invetory_summary_with_http_info(org_id, opts)

```ruby
begin
  # VA System FISMA Inventory Summary
  data, status_code, headers = api_instance.get_va_system_fisma_invetory_summary_with_http_info(org_id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <GetSystemStatusDetails200Response>
rescue EmassClient::ApiError => e
  puts "Error when calling VASystemDashboardsApi->get_va_system_fisma_invetory_summary_with_http_info: #{e}"
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


## get_va_system_icamp_tableau_poam_details

> <GetSystemStatusDetails200Response> get_va_system_icamp_tableau_poam_details(org_id, opts)

VA System ICAMP Tableau POAM Details

Get VA system ICAMP Tableau POAM details dashboard information.

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

api_instance = EmassClient::VASystemDashboardsApi.new
org_id = 1 # Integer | **Organization Id**: The unique organization identifier.
opts = {
  excludeinherited: true, # Boolean | **Exclude Inherited**: If no value is specified, the default returns false to include inherited data. 
  page_index: 56, # Integer | **Page Index**: If no value is specified, the default returns results from the first page with an index of 0. 
  page_size: 56 # Integer | **Page Size**: If no value is specified, the default returns 20000 per page. 
}

begin
  # VA System ICAMP Tableau POAM Details
  result = api_instance.get_va_system_icamp_tableau_poam_details(org_id, opts)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling VASystemDashboardsApi->get_va_system_icamp_tableau_poam_details: #{e}"
end
```

#### Using the get_va_system_icamp_tableau_poam_details_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<GetSystemStatusDetails200Response>, Integer, Hash)> get_va_system_icamp_tableau_poam_details_with_http_info(org_id, opts)

```ruby
begin
  # VA System ICAMP Tableau POAM Details
  data, status_code, headers = api_instance.get_va_system_icamp_tableau_poam_details_with_http_info(org_id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <GetSystemStatusDetails200Response>
rescue EmassClient::ApiError => e
  puts "Error when calling VASystemDashboardsApi->get_va_system_icamp_tableau_poam_details_with_http_info: #{e}"
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


## get_va_system_pl109_reporting_summary

> <GetSystemStatusDetails200Response> get_va_system_pl109_reporting_summary(org_id, opts)

VA System P.L. 109 Reporting Summary

Get VA system P.L. 109 reporting summary dashboard information.

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

api_instance = EmassClient::VASystemDashboardsApi.new
org_id = 1 # Integer | **Organization Id**: The unique organization identifier.
opts = {
  excludeinherited: true, # Boolean | **Exclude Inherited**: If no value is specified, the default returns false to include inherited data. 
  page_index: 56, # Integer | **Page Index**: If no value is specified, the default returns results from the first page with an index of 0. 
  page_size: 56 # Integer | **Page Size**: If no value is specified, the default returns 20000 per page. 
}

begin
  # VA System P.L. 109 Reporting Summary
  result = api_instance.get_va_system_pl109_reporting_summary(org_id, opts)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling VASystemDashboardsApi->get_va_system_pl109_reporting_summary: #{e}"
end
```

#### Using the get_va_system_pl109_reporting_summary_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<GetSystemStatusDetails200Response>, Integer, Hash)> get_va_system_pl109_reporting_summary_with_http_info(org_id, opts)

```ruby
begin
  # VA System P.L. 109 Reporting Summary
  data, status_code, headers = api_instance.get_va_system_pl109_reporting_summary_with_http_info(org_id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <GetSystemStatusDetails200Response>
rescue EmassClient::ApiError => e
  puts "Error when calling VASystemDashboardsApi->get_va_system_pl109_reporting_summary_with_http_info: #{e}"
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


## get_va_system_threat_architecture_details

> <GetSystemStatusDetails200Response> get_va_system_threat_architecture_details(org_id, opts)

VA System Threat Architecture Details

Get VA system threat architecture details dashboard information.

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

api_instance = EmassClient::VASystemDashboardsApi.new
org_id = 1 # Integer | **Organization Id**: The unique organization identifier.
opts = {
  excludeinherited: true, # Boolean | **Exclude Inherited**: If no value is specified, the default returns false to include inherited data. 
  page_index: 56, # Integer | **Page Index**: If no value is specified, the default returns results from the first page with an index of 0. 
  page_size: 56 # Integer | **Page Size**: If no value is specified, the default returns 20000 per page. 
}

begin
  # VA System Threat Architecture Details
  result = api_instance.get_va_system_threat_architecture_details(org_id, opts)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling VASystemDashboardsApi->get_va_system_threat_architecture_details: #{e}"
end
```

#### Using the get_va_system_threat_architecture_details_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<GetSystemStatusDetails200Response>, Integer, Hash)> get_va_system_threat_architecture_details_with_http_info(org_id, opts)

```ruby
begin
  # VA System Threat Architecture Details
  data, status_code, headers = api_instance.get_va_system_threat_architecture_details_with_http_info(org_id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <GetSystemStatusDetails200Response>
rescue EmassClient::ApiError => e
  puts "Error when calling VASystemDashboardsApi->get_va_system_threat_architecture_details_with_http_info: #{e}"
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


## get_va_system_threat_risk_summary

> <GetSystemStatusDetails200Response> get_va_system_threat_risk_summary(org_id, opts)

VA System Threat Risks Summary

Get VA system threat risk summary dashboard information.

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

api_instance = EmassClient::VASystemDashboardsApi.new
org_id = 1 # Integer | **Organization Id**: The unique organization identifier.
opts = {
  excludeinherited: true, # Boolean | **Exclude Inherited**: If no value is specified, the default returns false to include inherited data. 
  page_index: 56, # Integer | **Page Index**: If no value is specified, the default returns results from the first page with an index of 0. 
  page_size: 56 # Integer | **Page Size**: If no value is specified, the default returns 20000 per page. 
}

begin
  # VA System Threat Risks Summary
  result = api_instance.get_va_system_threat_risk_summary(org_id, opts)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling VASystemDashboardsApi->get_va_system_threat_risk_summary: #{e}"
end
```

#### Using the get_va_system_threat_risk_summary_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<GetSystemStatusDetails200Response>, Integer, Hash)> get_va_system_threat_risk_summary_with_http_info(org_id, opts)

```ruby
begin
  # VA System Threat Risks Summary
  data, status_code, headers = api_instance.get_va_system_threat_risk_summary_with_http_info(org_id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <GetSystemStatusDetails200Response>
rescue EmassClient::ApiError => e
  puts "Error when calling VASystemDashboardsApi->get_va_system_threat_risk_summary_with_http_info: #{e}"
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


## get_va_system_threat_source_details

> <GetSystemStatusDetails200Response> get_va_system_threat_source_details(org_id, opts)

VA System Threat Sources Details

Get VA system threat source details dashboard information.

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

api_instance = EmassClient::VASystemDashboardsApi.new
org_id = 1 # Integer | **Organization Id**: The unique organization identifier.
opts = {
  excludeinherited: true, # Boolean | **Exclude Inherited**: If no value is specified, the default returns false to include inherited data. 
  page_index: 56, # Integer | **Page Index**: If no value is specified, the default returns results from the first page with an index of 0. 
  page_size: 56 # Integer | **Page Size**: If no value is specified, the default returns 20000 per page. 
}

begin
  # VA System Threat Sources Details
  result = api_instance.get_va_system_threat_source_details(org_id, opts)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling VASystemDashboardsApi->get_va_system_threat_source_details: #{e}"
end
```

#### Using the get_va_system_threat_source_details_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<GetSystemStatusDetails200Response>, Integer, Hash)> get_va_system_threat_source_details_with_http_info(org_id, opts)

```ruby
begin
  # VA System Threat Sources Details
  data, status_code, headers = api_instance.get_va_system_threat_source_details_with_http_info(org_id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <GetSystemStatusDetails200Response>
rescue EmassClient::ApiError => e
  puts "Error when calling VASystemDashboardsApi->get_va_system_threat_source_details_with_http_info: #{e}"
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

