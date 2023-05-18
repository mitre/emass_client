# EmassClient::DashboardsApi

All URIs are relative to *http://localhost:4010*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**get_system_artifacts_details**](DashboardsApi.md#get_system_artifacts_details) | **GET** /api/dashboards/system-artifacts-details | Get dashboard information |
| [**get_system_artifacts_summary**](DashboardsApi.md#get_system_artifacts_summary) | **GET** /api/dashboards/system-artifacts-summary | Get dashboard information |
| [**get_system_assessment_procedures_details**](DashboardsApi.md#get_system_assessment_procedures_details) | **GET** /api/dashboards/system-assessment-procedures-details | Get dashboard information |
| [**get_system_associations_details**](DashboardsApi.md#get_system_associations_details) | **GET** /api/dashboards/system-associations-details | Get dashboard information |
| [**get_system_control_compliance_summary**](DashboardsApi.md#get_system_control_compliance_summary) | **GET** /api/dashboards/system-control-compliance-summary | Get dashboard information |
| [**get_system_hardware_details**](DashboardsApi.md#get_system_hardware_details) | **GET** /api/dashboards/system-hardware-details | Get dashboard information |
| [**get_system_hardware_summary**](DashboardsApi.md#get_system_hardware_summary) | **GET** /api/dashboards/system-hardware-summary | Get dashboard information |
| [**get_system_poam_details**](DashboardsApi.md#get_system_poam_details) | **GET** /api/dashboards/system-poam-details | Get dashboard information |
| [**get_system_poam_summary**](DashboardsApi.md#get_system_poam_summary) | **GET** /api/dashboards/system-poam-summary | Get dashboard information |
| [**get_system_ports_protocols_details**](DashboardsApi.md#get_system_ports_protocols_details) | **GET** /api/dashboards/system-ports-protocols-details | Get dashboard information |
| [**get_system_ports_protocols_summary**](DashboardsApi.md#get_system_ports_protocols_summary) | **GET** /api/dashboards/system-ports-protocols-summary | Get dashboard information |
| [**get_system_privacy_summary**](DashboardsApi.md#get_system_privacy_summary) | **GET** /api/dashboards/system-privacy-summary | Get dashboard information |
| [**get_system_security_control_details**](DashboardsApi.md#get_system_security_control_details) | **GET** /api/dashboards/system-security-controls-details | Get dashboard information |
| [**get_system_sensor_hardware_details**](DashboardsApi.md#get_system_sensor_hardware_details) | **GET** /api/dashboards/system-sensor-hardware-details | Get dashboard information |
| [**get_system_sensor_hardware_summary**](DashboardsApi.md#get_system_sensor_hardware_summary) | **GET** /api/dashboards/system-sensor-hardware-summary | Get dashboard information |
| [**get_system_status_details**](DashboardsApi.md#get_system_status_details) | **GET** /api/dashboards/system-status-details | Get dashboard information |
| [**get_user_system_assignments_details**](DashboardsApi.md#get_user_system_assignments_details) | **GET** /api/dashboards/user-system-assignments-details | Get dashboard information |
| [**get_va_omb_fsma_saop_summary**](DashboardsApi.md#get_va_omb_fsma_saop_summary) | **GET** /api/dashboards/va-omb-fisma-saop-summary | Get dashboard information |
| [**get_va_system_a2_summary**](DashboardsApi.md#get_va_system_a2_summary) | **GET** /api/dashboards/va-system-a2-summary | Get dashboard information |
| [**get_va_system_aa_summary**](DashboardsApi.md#get_va_system_aa_summary) | **GET** /api/dashboards/va-system-aa-summary | Get dashboard information |
| [**get_va_system_fisma_invetory_crypto_summary**](DashboardsApi.md#get_va_system_fisma_invetory_crypto_summary) | **GET** /api/dashboards/va-system-fisma-inventory-crypto-summary | Get dashboard information |
| [**get_va_system_fisma_invetory_summary**](DashboardsApi.md#get_va_system_fisma_invetory_summary) | **GET** /api/dashboards/va-system-fisma-inventory-summary | Get dashboard information |
| [**get_va_system_pl109_reporting_summary**](DashboardsApi.md#get_va_system_pl109_reporting_summary) | **GET** /api/dashboards/va-system-pl-109-reporting-summary | Get dashboard information |
| [**get_va_system_threat_architecture_details**](DashboardsApi.md#get_va_system_threat_architecture_details) | **GET** /api/dashboards/va-system-threat-architecture-details | Get dashboard information |
| [**get_va_system_threat_risk_summary**](DashboardsApi.md#get_va_system_threat_risk_summary) | **GET** /api/dashboards/va-system-threat-risks-summary | Get dashboard information |
| [**get_va_system_threat_source_details**](DashboardsApi.md#get_va_system_threat_source_details) | **GET** /api/dashboards/va-system-threat-sources-details | Get dashboard information |


## get_system_artifacts_details

> Object get_system_artifacts_details(org_id, opts)

Get dashboard information

Get system Artifacts details information.

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

api_instance = EmassClient::DashboardsApi.new
org_id = 1 # Integer | **Organization Id**: The unique organization identifier.
opts = {
  excludeinherited: true, # Boolean | **Exclude Inherited**: If no value is specified, the default returns false to include inherited data. 
  page_index: 56, # Integer | **Page Index**: If no value is specified, the default returns results from the first page with an index of 0. 
  page_size: 56 # Integer | **Page Size**: If no value is specified, the default returns 20000 per page. 
}

begin
  # Get dashboard information
  result = api_instance.get_system_artifacts_details(org_id, opts)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling DashboardsApi->get_system_artifacts_details: #{e}"
end
```

#### Using the get_system_artifacts_details_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(Object, Integer, Hash)> get_system_artifacts_details_with_http_info(org_id, opts)

```ruby
begin
  # Get dashboard information
  data, status_code, headers = api_instance.get_system_artifacts_details_with_http_info(org_id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => Object
rescue EmassClient::ApiError => e
  puts "Error when calling DashboardsApi->get_system_artifacts_details_with_http_info: #{e}"
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


## get_system_artifacts_summary

> Object get_system_artifacts_summary(org_id, opts)

Get dashboard information

Get system Artifacts summary information.

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

api_instance = EmassClient::DashboardsApi.new
org_id = 1 # Integer | **Organization Id**: The unique organization identifier.
opts = {
  excludeinherited: true, # Boolean | **Exclude Inherited**: If no value is specified, the default returns false to include inherited data. 
  page_index: 56, # Integer | **Page Index**: If no value is specified, the default returns results from the first page with an index of 0. 
  page_size: 56 # Integer | **Page Size**: If no value is specified, the default returns 20000 per page. 
}

begin
  # Get dashboard information
  result = api_instance.get_system_artifacts_summary(org_id, opts)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling DashboardsApi->get_system_artifacts_summary: #{e}"
end
```

#### Using the get_system_artifacts_summary_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(Object, Integer, Hash)> get_system_artifacts_summary_with_http_info(org_id, opts)

```ruby
begin
  # Get dashboard information
  data, status_code, headers = api_instance.get_system_artifacts_summary_with_http_info(org_id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => Object
rescue EmassClient::ApiError => e
  puts "Error when calling DashboardsApi->get_system_artifacts_summary_with_http_info: #{e}"
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


## get_system_assessment_procedures_details

> Object get_system_assessment_procedures_details(org_id, opts)

Get dashboard information

Get systems assessement procdures details dashboard information.

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

api_instance = EmassClient::DashboardsApi.new
org_id = 1 # Integer | **Organization Id**: The unique organization identifier.
opts = {
  excludeinherited: true, # Boolean | **Exclude Inherited**: If no value is specified, the default returns false to include inherited data. 
  page_index: 56, # Integer | **Page Index**: If no value is specified, the default returns results from the first page with an index of 0. 
  page_size: 56 # Integer | **Page Size**: If no value is specified, the default returns 20000 per page. 
}

begin
  # Get dashboard information
  result = api_instance.get_system_assessment_procedures_details(org_id, opts)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling DashboardsApi->get_system_assessment_procedures_details: #{e}"
end
```

#### Using the get_system_assessment_procedures_details_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(Object, Integer, Hash)> get_system_assessment_procedures_details_with_http_info(org_id, opts)

```ruby
begin
  # Get dashboard information
  data, status_code, headers = api_instance.get_system_assessment_procedures_details_with_http_info(org_id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => Object
rescue EmassClient::ApiError => e
  puts "Error when calling DashboardsApi->get_system_assessment_procedures_details_with_http_info: #{e}"
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


## get_system_associations_details

> Object get_system_associations_details(org_id, opts)

Get dashboard information

Get system associations details dashboard information.

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

api_instance = EmassClient::DashboardsApi.new
org_id = 1 # Integer | **Organization Id**: The unique organization identifier.
opts = {
  excludeinherited: true, # Boolean | **Exclude Inherited**: If no value is specified, the default returns false to include inherited data. 
  page_index: 56, # Integer | **Page Index**: If no value is specified, the default returns results from the first page with an index of 0. 
  page_size: 56 # Integer | **Page Size**: If no value is specified, the default returns 20000 per page. 
}

begin
  # Get dashboard information
  result = api_instance.get_system_associations_details(org_id, opts)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling DashboardsApi->get_system_associations_details: #{e}"
end
```

#### Using the get_system_associations_details_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(Object, Integer, Hash)> get_system_associations_details_with_http_info(org_id, opts)

```ruby
begin
  # Get dashboard information
  data, status_code, headers = api_instance.get_system_associations_details_with_http_info(org_id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => Object
rescue EmassClient::ApiError => e
  puts "Error when calling DashboardsApi->get_system_associations_details_with_http_info: #{e}"
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


## get_system_control_compliance_summary

> Object get_system_control_compliance_summary(org_id, opts)

Get dashboard information

Get systems control compliance summary dashboard information.

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

api_instance = EmassClient::DashboardsApi.new
org_id = 1 # Integer | **Organization Id**: The unique organization identifier.
opts = {
  excludeinherited: true, # Boolean | **Exclude Inherited**: If no value is specified, the default returns false to include inherited data. 
  page_index: 56, # Integer | **Page Index**: If no value is specified, the default returns results from the first page with an index of 0. 
  page_size: 56 # Integer | **Page Size**: If no value is specified, the default returns 20000 per page. 
}

begin
  # Get dashboard information
  result = api_instance.get_system_control_compliance_summary(org_id, opts)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling DashboardsApi->get_system_control_compliance_summary: #{e}"
end
```

#### Using the get_system_control_compliance_summary_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(Object, Integer, Hash)> get_system_control_compliance_summary_with_http_info(org_id, opts)

```ruby
begin
  # Get dashboard information
  data, status_code, headers = api_instance.get_system_control_compliance_summary_with_http_info(org_id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => Object
rescue EmassClient::ApiError => e
  puts "Error when calling DashboardsApi->get_system_control_compliance_summary_with_http_info: #{e}"
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


## get_system_hardware_details

> Object get_system_hardware_details(org_id, opts)

Get dashboard information

Get system hardware details dashboard information.

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

api_instance = EmassClient::DashboardsApi.new
org_id = 1 # Integer | **Organization Id**: The unique organization identifier.
opts = {
  excludeinherited: true, # Boolean | **Exclude Inherited**: If no value is specified, the default returns false to include inherited data. 
  page_index: 56, # Integer | **Page Index**: If no value is specified, the default returns results from the first page with an index of 0. 
  page_size: 56 # Integer | **Page Size**: If no value is specified, the default returns 20000 per page. 
}

begin
  # Get dashboard information
  result = api_instance.get_system_hardware_details(org_id, opts)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling DashboardsApi->get_system_hardware_details: #{e}"
end
```

#### Using the get_system_hardware_details_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(Object, Integer, Hash)> get_system_hardware_details_with_http_info(org_id, opts)

```ruby
begin
  # Get dashboard information
  data, status_code, headers = api_instance.get_system_hardware_details_with_http_info(org_id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => Object
rescue EmassClient::ApiError => e
  puts "Error when calling DashboardsApi->get_system_hardware_details_with_http_info: #{e}"
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


## get_system_hardware_summary

> Object get_system_hardware_summary(org_id, opts)

Get dashboard information

Get system hardware summary dashboard information.

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

api_instance = EmassClient::DashboardsApi.new
org_id = 1 # Integer | **Organization Id**: The unique organization identifier.
opts = {
  excludeinherited: true, # Boolean | **Exclude Inherited**: If no value is specified, the default returns false to include inherited data. 
  page_index: 56, # Integer | **Page Index**: If no value is specified, the default returns results from the first page with an index of 0. 
  page_size: 56 # Integer | **Page Size**: If no value is specified, the default returns 20000 per page. 
}

begin
  # Get dashboard information
  result = api_instance.get_system_hardware_summary(org_id, opts)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling DashboardsApi->get_system_hardware_summary: #{e}"
end
```

#### Using the get_system_hardware_summary_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(Object, Integer, Hash)> get_system_hardware_summary_with_http_info(org_id, opts)

```ruby
begin
  # Get dashboard information
  data, status_code, headers = api_instance.get_system_hardware_summary_with_http_info(org_id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => Object
rescue EmassClient::ApiError => e
  puts "Error when calling DashboardsApi->get_system_hardware_summary_with_http_info: #{e}"
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


## get_system_poam_details

> Object get_system_poam_details(org_id, opts)

Get dashboard information

Get system POA&Ms details dashboard information.

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

api_instance = EmassClient::DashboardsApi.new
org_id = 1 # Integer | **Organization Id**: The unique organization identifier.
opts = {
  excludeinherited: true, # Boolean | **Exclude Inherited**: If no value is specified, the default returns false to include inherited data. 
  page_index: 56, # Integer | **Page Index**: If no value is specified, the default returns results from the first page with an index of 0. 
  page_size: 56 # Integer | **Page Size**: If no value is specified, the default returns 20000 per page. 
}

begin
  # Get dashboard information
  result = api_instance.get_system_poam_details(org_id, opts)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling DashboardsApi->get_system_poam_details: #{e}"
end
```

#### Using the get_system_poam_details_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(Object, Integer, Hash)> get_system_poam_details_with_http_info(org_id, opts)

```ruby
begin
  # Get dashboard information
  data, status_code, headers = api_instance.get_system_poam_details_with_http_info(org_id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => Object
rescue EmassClient::ApiError => e
  puts "Error when calling DashboardsApi->get_system_poam_details_with_http_info: #{e}"
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


## get_system_poam_summary

> Object get_system_poam_summary(org_id, opts)

Get dashboard information

Get systems POA&Ms summary dashboard information.

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

api_instance = EmassClient::DashboardsApi.new
org_id = 1 # Integer | **Organization Id**: The unique organization identifier.
opts = {
  excludeinherited: true, # Boolean | **Exclude Inherited**: If no value is specified, the default returns false to include inherited data. 
  page_index: 56, # Integer | **Page Index**: If no value is specified, the default returns results from the first page with an index of 0. 
  page_size: 56 # Integer | **Page Size**: If no value is specified, the default returns 20000 per page. 
}

begin
  # Get dashboard information
  result = api_instance.get_system_poam_summary(org_id, opts)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling DashboardsApi->get_system_poam_summary: #{e}"
end
```

#### Using the get_system_poam_summary_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(Object, Integer, Hash)> get_system_poam_summary_with_http_info(org_id, opts)

```ruby
begin
  # Get dashboard information
  data, status_code, headers = api_instance.get_system_poam_summary_with_http_info(org_id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => Object
rescue EmassClient::ApiError => e
  puts "Error when calling DashboardsApi->get_system_poam_summary_with_http_info: #{e}"
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


## get_system_ports_protocols_details

> Object get_system_ports_protocols_details(org_id, opts)

Get dashboard information

Get system ports and protocols details dashboard information.

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

api_instance = EmassClient::DashboardsApi.new
org_id = 1 # Integer | **Organization Id**: The unique organization identifier.
opts = {
  excludeinherited: true, # Boolean | **Exclude Inherited**: If no value is specified, the default returns false to include inherited data. 
  page_index: 56, # Integer | **Page Index**: If no value is specified, the default returns results from the first page with an index of 0. 
  page_size: 56 # Integer | **Page Size**: If no value is specified, the default returns 20000 per page. 
}

begin
  # Get dashboard information
  result = api_instance.get_system_ports_protocols_details(org_id, opts)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling DashboardsApi->get_system_ports_protocols_details: #{e}"
end
```

#### Using the get_system_ports_protocols_details_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(Object, Integer, Hash)> get_system_ports_protocols_details_with_http_info(org_id, opts)

```ruby
begin
  # Get dashboard information
  data, status_code, headers = api_instance.get_system_ports_protocols_details_with_http_info(org_id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => Object
rescue EmassClient::ApiError => e
  puts "Error when calling DashboardsApi->get_system_ports_protocols_details_with_http_info: #{e}"
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


## get_system_ports_protocols_summary

> Object get_system_ports_protocols_summary(org_id, opts)

Get dashboard information

Get system ports and protocols summary dashboard information.

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

api_instance = EmassClient::DashboardsApi.new
org_id = 1 # Integer | **Organization Id**: The unique organization identifier.
opts = {
  excludeinherited: true, # Boolean | **Exclude Inherited**: If no value is specified, the default returns false to include inherited data. 
  page_index: 56, # Integer | **Page Index**: If no value is specified, the default returns results from the first page with an index of 0. 
  page_size: 56 # Integer | **Page Size**: If no value is specified, the default returns 20000 per page. 
}

begin
  # Get dashboard information
  result = api_instance.get_system_ports_protocols_summary(org_id, opts)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling DashboardsApi->get_system_ports_protocols_summary: #{e}"
end
```

#### Using the get_system_ports_protocols_summary_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(Object, Integer, Hash)> get_system_ports_protocols_summary_with_http_info(org_id, opts)

```ruby
begin
  # Get dashboard information
  data, status_code, headers = api_instance.get_system_ports_protocols_summary_with_http_info(org_id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => Object
rescue EmassClient::ApiError => e
  puts "Error when calling DashboardsApi->get_system_ports_protocols_summary_with_http_info: #{e}"
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


## get_system_privacy_summary

> Object get_system_privacy_summary(org_id, opts)

Get dashboard information

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

api_instance = EmassClient::DashboardsApi.new
org_id = 1 # Integer | **Organization Id**: The unique organization identifier.
opts = {
  excludeinherited: true, # Boolean | **Exclude Inherited**: If no value is specified, the default returns false to include inherited data. 
  page_index: 56, # Integer | **Page Index**: If no value is specified, the default returns results from the first page with an index of 0. 
  page_size: 56 # Integer | **Page Size**: If no value is specified, the default returns 20000 per page. 
}

begin
  # Get dashboard information
  result = api_instance.get_system_privacy_summary(org_id, opts)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling DashboardsApi->get_system_privacy_summary: #{e}"
end
```

#### Using the get_system_privacy_summary_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(Object, Integer, Hash)> get_system_privacy_summary_with_http_info(org_id, opts)

```ruby
begin
  # Get dashboard information
  data, status_code, headers = api_instance.get_system_privacy_summary_with_http_info(org_id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => Object
rescue EmassClient::ApiError => e
  puts "Error when calling DashboardsApi->get_system_privacy_summary_with_http_info: #{e}"
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


## get_system_security_control_details

> Object get_system_security_control_details(org_id, opts)

Get dashboard information

Get systems security control details dashboard information.

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

api_instance = EmassClient::DashboardsApi.new
org_id = 1 # Integer | **Organization Id**: The unique organization identifier.
opts = {
  excludeinherited: true, # Boolean | **Exclude Inherited**: If no value is specified, the default returns false to include inherited data. 
  page_index: 56, # Integer | **Page Index**: If no value is specified, the default returns results from the first page with an index of 0. 
  page_size: 56 # Integer | **Page Size**: If no value is specified, the default returns 20000 per page. 
}

begin
  # Get dashboard information
  result = api_instance.get_system_security_control_details(org_id, opts)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling DashboardsApi->get_system_security_control_details: #{e}"
end
```

#### Using the get_system_security_control_details_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(Object, Integer, Hash)> get_system_security_control_details_with_http_info(org_id, opts)

```ruby
begin
  # Get dashboard information
  data, status_code, headers = api_instance.get_system_security_control_details_with_http_info(org_id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => Object
rescue EmassClient::ApiError => e
  puts "Error when calling DashboardsApi->get_system_security_control_details_with_http_info: #{e}"
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


## get_system_sensor_hardware_details

> Object get_system_sensor_hardware_details(org_id, opts)

Get dashboard information

Get system sensor hardware details dashboard information.

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

api_instance = EmassClient::DashboardsApi.new
org_id = 1 # Integer | **Organization Id**: The unique organization identifier.
opts = {
  excludeinherited: true, # Boolean | **Exclude Inherited**: If no value is specified, the default returns false to include inherited data. 
  page_index: 56, # Integer | **Page Index**: If no value is specified, the default returns results from the first page with an index of 0. 
  page_size: 56 # Integer | **Page Size**: If no value is specified, the default returns 20000 per page. 
}

begin
  # Get dashboard information
  result = api_instance.get_system_sensor_hardware_details(org_id, opts)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling DashboardsApi->get_system_sensor_hardware_details: #{e}"
end
```

#### Using the get_system_sensor_hardware_details_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(Object, Integer, Hash)> get_system_sensor_hardware_details_with_http_info(org_id, opts)

```ruby
begin
  # Get dashboard information
  data, status_code, headers = api_instance.get_system_sensor_hardware_details_with_http_info(org_id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => Object
rescue EmassClient::ApiError => e
  puts "Error when calling DashboardsApi->get_system_sensor_hardware_details_with_http_info: #{e}"
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


## get_system_sensor_hardware_summary

> Object get_system_sensor_hardware_summary(org_id, opts)

Get dashboard information

Get system sensor hardware summary dashboard information.

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

api_instance = EmassClient::DashboardsApi.new
org_id = 1 # Integer | **Organization Id**: The unique organization identifier.
opts = {
  excludeinherited: true, # Boolean | **Exclude Inherited**: If no value is specified, the default returns false to include inherited data. 
  page_index: 56, # Integer | **Page Index**: If no value is specified, the default returns results from the first page with an index of 0. 
  page_size: 56 # Integer | **Page Size**: If no value is specified, the default returns 20000 per page. 
}

begin
  # Get dashboard information
  result = api_instance.get_system_sensor_hardware_summary(org_id, opts)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling DashboardsApi->get_system_sensor_hardware_summary: #{e}"
end
```

#### Using the get_system_sensor_hardware_summary_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(Object, Integer, Hash)> get_system_sensor_hardware_summary_with_http_info(org_id, opts)

```ruby
begin
  # Get dashboard information
  data, status_code, headers = api_instance.get_system_sensor_hardware_summary_with_http_info(org_id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => Object
rescue EmassClient::ApiError => e
  puts "Error when calling DashboardsApi->get_system_sensor_hardware_summary_with_http_info: #{e}"
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


## get_system_status_details

> Object get_system_status_details(org_id, opts)

Get dashboard information

Get systems status detail dashboard information.

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

api_instance = EmassClient::DashboardsApi.new
org_id = 1 # Integer | **Organization Id**: The unique organization identifier.
opts = {
  excludeinherited: true, # Boolean | **Exclude Inherited**: If no value is specified, the default returns false to include inherited data. 
  page_index: 56, # Integer | **Page Index**: If no value is specified, the default returns results from the first page with an index of 0. 
  page_size: 56 # Integer | **Page Size**: If no value is specified, the default returns 20000 per page. 
}

begin
  # Get dashboard information
  result = api_instance.get_system_status_details(org_id, opts)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling DashboardsApi->get_system_status_details: #{e}"
end
```

#### Using the get_system_status_details_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(Object, Integer, Hash)> get_system_status_details_with_http_info(org_id, opts)

```ruby
begin
  # Get dashboard information
  data, status_code, headers = api_instance.get_system_status_details_with_http_info(org_id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => Object
rescue EmassClient::ApiError => e
  puts "Error when calling DashboardsApi->get_system_status_details_with_http_info: #{e}"
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


## get_user_system_assignments_details

> Object get_user_system_assignments_details(org_id, opts)

Get dashboard information

Get user system assignments details dashboard information.

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

api_instance = EmassClient::DashboardsApi.new
org_id = 1 # Integer | **Organization Id**: The unique organization identifier.
opts = {
  excludeinherited: true, # Boolean | **Exclude Inherited**: If no value is specified, the default returns false to include inherited data. 
  page_index: 56, # Integer | **Page Index**: If no value is specified, the default returns results from the first page with an index of 0. 
  page_size: 56 # Integer | **Page Size**: If no value is specified, the default returns 20000 per page. 
}

begin
  # Get dashboard information
  result = api_instance.get_user_system_assignments_details(org_id, opts)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling DashboardsApi->get_user_system_assignments_details: #{e}"
end
```

#### Using the get_user_system_assignments_details_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(Object, Integer, Hash)> get_user_system_assignments_details_with_http_info(org_id, opts)

```ruby
begin
  # Get dashboard information
  data, status_code, headers = api_instance.get_user_system_assignments_details_with_http_info(org_id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => Object
rescue EmassClient::ApiError => e
  puts "Error when calling DashboardsApi->get_user_system_assignments_details_with_http_info: #{e}"
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

Get dashboard information

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

api_instance = EmassClient::DashboardsApi.new
org_id = 1 # Integer | **Organization Id**: The unique organization identifier.
opts = {
  excludeinherited: true, # Boolean | **Exclude Inherited**: If no value is specified, the default returns false to include inherited data. 
  page_index: 56, # Integer | **Page Index**: If no value is specified, the default returns results from the first page with an index of 0. 
  page_size: 56 # Integer | **Page Size**: If no value is specified, the default returns 20000 per page. 
}

begin
  # Get dashboard information
  result = api_instance.get_va_omb_fsma_saop_summary(org_id, opts)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling DashboardsApi->get_va_omb_fsma_saop_summary: #{e}"
end
```

#### Using the get_va_omb_fsma_saop_summary_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(Object, Integer, Hash)> get_va_omb_fsma_saop_summary_with_http_info(org_id, opts)

```ruby
begin
  # Get dashboard information
  data, status_code, headers = api_instance.get_va_omb_fsma_saop_summary_with_http_info(org_id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => Object
rescue EmassClient::ApiError => e
  puts "Error when calling DashboardsApi->get_va_omb_fsma_saop_summary_with_http_info: #{e}"
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


## get_va_system_a2_summary

> Object get_va_system_a2_summary(org_id, opts)

Get dashboard information

Get VA system A2.0 summary dashboard information.

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

api_instance = EmassClient::DashboardsApi.new
org_id = 1 # Integer | **Organization Id**: The unique organization identifier.
opts = {
  excludeinherited: true, # Boolean | **Exclude Inherited**: If no value is specified, the default returns false to include inherited data. 
  page_index: 56, # Integer | **Page Index**: If no value is specified, the default returns results from the first page with an index of 0. 
  page_size: 56 # Integer | **Page Size**: If no value is specified, the default returns 20000 per page. 
}

begin
  # Get dashboard information
  result = api_instance.get_va_system_a2_summary(org_id, opts)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling DashboardsApi->get_va_system_a2_summary: #{e}"
end
```

#### Using the get_va_system_a2_summary_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(Object, Integer, Hash)> get_va_system_a2_summary_with_http_info(org_id, opts)

```ruby
begin
  # Get dashboard information
  data, status_code, headers = api_instance.get_va_system_a2_summary_with_http_info(org_id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => Object
rescue EmassClient::ApiError => e
  puts "Error when calling DashboardsApi->get_va_system_a2_summary_with_http_info: #{e}"
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


## get_va_system_aa_summary

> Object get_va_system_aa_summary(org_id, opts)

Get dashboard information

Get VA system A&A summary dashboard information.

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

api_instance = EmassClient::DashboardsApi.new
org_id = 1 # Integer | **Organization Id**: The unique organization identifier.
opts = {
  excludeinherited: true, # Boolean | **Exclude Inherited**: If no value is specified, the default returns false to include inherited data. 
  page_index: 56, # Integer | **Page Index**: If no value is specified, the default returns results from the first page with an index of 0. 
  page_size: 56 # Integer | **Page Size**: If no value is specified, the default returns 20000 per page. 
}

begin
  # Get dashboard information
  result = api_instance.get_va_system_aa_summary(org_id, opts)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling DashboardsApi->get_va_system_aa_summary: #{e}"
end
```

#### Using the get_va_system_aa_summary_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(Object, Integer, Hash)> get_va_system_aa_summary_with_http_info(org_id, opts)

```ruby
begin
  # Get dashboard information
  data, status_code, headers = api_instance.get_va_system_aa_summary_with_http_info(org_id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => Object
rescue EmassClient::ApiError => e
  puts "Error when calling DashboardsApi->get_va_system_aa_summary_with_http_info: #{e}"
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


## get_va_system_fisma_invetory_crypto_summary

> Object get_va_system_fisma_invetory_crypto_summary(org_id, opts)

Get dashboard information

Get VA system FISMA inventory crypto summary dashboard information.

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

api_instance = EmassClient::DashboardsApi.new
org_id = 1 # Integer | **Organization Id**: The unique organization identifier.
opts = {
  excludeinherited: true, # Boolean | **Exclude Inherited**: If no value is specified, the default returns false to include inherited data. 
  page_index: 56, # Integer | **Page Index**: If no value is specified, the default returns results from the first page with an index of 0. 
  page_size: 56 # Integer | **Page Size**: If no value is specified, the default returns 20000 per page. 
}

begin
  # Get dashboard information
  result = api_instance.get_va_system_fisma_invetory_crypto_summary(org_id, opts)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling DashboardsApi->get_va_system_fisma_invetory_crypto_summary: #{e}"
end
```

#### Using the get_va_system_fisma_invetory_crypto_summary_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(Object, Integer, Hash)> get_va_system_fisma_invetory_crypto_summary_with_http_info(org_id, opts)

```ruby
begin
  # Get dashboard information
  data, status_code, headers = api_instance.get_va_system_fisma_invetory_crypto_summary_with_http_info(org_id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => Object
rescue EmassClient::ApiError => e
  puts "Error when calling DashboardsApi->get_va_system_fisma_invetory_crypto_summary_with_http_info: #{e}"
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


## get_va_system_fisma_invetory_summary

> Object get_va_system_fisma_invetory_summary(org_id, opts)

Get dashboard information

Get VA system FISMA inventory summary dashboard information.

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

api_instance = EmassClient::DashboardsApi.new
org_id = 1 # Integer | **Organization Id**: The unique organization identifier.
opts = {
  excludeinherited: true, # Boolean | **Exclude Inherited**: If no value is specified, the default returns false to include inherited data. 
  page_index: 56, # Integer | **Page Index**: If no value is specified, the default returns results from the first page with an index of 0. 
  page_size: 56 # Integer | **Page Size**: If no value is specified, the default returns 20000 per page. 
}

begin
  # Get dashboard information
  result = api_instance.get_va_system_fisma_invetory_summary(org_id, opts)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling DashboardsApi->get_va_system_fisma_invetory_summary: #{e}"
end
```

#### Using the get_va_system_fisma_invetory_summary_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(Object, Integer, Hash)> get_va_system_fisma_invetory_summary_with_http_info(org_id, opts)

```ruby
begin
  # Get dashboard information
  data, status_code, headers = api_instance.get_va_system_fisma_invetory_summary_with_http_info(org_id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => Object
rescue EmassClient::ApiError => e
  puts "Error when calling DashboardsApi->get_va_system_fisma_invetory_summary_with_http_info: #{e}"
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


## get_va_system_pl109_reporting_summary

> Object get_va_system_pl109_reporting_summary(org_id, opts)

Get dashboard information

Get VA system P.L. 109 reporting summary dashboard information.

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

api_instance = EmassClient::DashboardsApi.new
org_id = 1 # Integer | **Organization Id**: The unique organization identifier.
opts = {
  excludeinherited: true, # Boolean | **Exclude Inherited**: If no value is specified, the default returns false to include inherited data. 
  page_index: 56, # Integer | **Page Index**: If no value is specified, the default returns results from the first page with an index of 0. 
  page_size: 56 # Integer | **Page Size**: If no value is specified, the default returns 20000 per page. 
}

begin
  # Get dashboard information
  result = api_instance.get_va_system_pl109_reporting_summary(org_id, opts)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling DashboardsApi->get_va_system_pl109_reporting_summary: #{e}"
end
```

#### Using the get_va_system_pl109_reporting_summary_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(Object, Integer, Hash)> get_va_system_pl109_reporting_summary_with_http_info(org_id, opts)

```ruby
begin
  # Get dashboard information
  data, status_code, headers = api_instance.get_va_system_pl109_reporting_summary_with_http_info(org_id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => Object
rescue EmassClient::ApiError => e
  puts "Error when calling DashboardsApi->get_va_system_pl109_reporting_summary_with_http_info: #{e}"
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


## get_va_system_threat_architecture_details

> Object get_va_system_threat_architecture_details(org_id, opts)

Get dashboard information

Get VA system threat architecture details dashboard information.

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

api_instance = EmassClient::DashboardsApi.new
org_id = 1 # Integer | **Organization Id**: The unique organization identifier.
opts = {
  excludeinherited: true, # Boolean | **Exclude Inherited**: If no value is specified, the default returns false to include inherited data. 
  page_index: 56, # Integer | **Page Index**: If no value is specified, the default returns results from the first page with an index of 0. 
  page_size: 56 # Integer | **Page Size**: If no value is specified, the default returns 20000 per page. 
}

begin
  # Get dashboard information
  result = api_instance.get_va_system_threat_architecture_details(org_id, opts)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling DashboardsApi->get_va_system_threat_architecture_details: #{e}"
end
```

#### Using the get_va_system_threat_architecture_details_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(Object, Integer, Hash)> get_va_system_threat_architecture_details_with_http_info(org_id, opts)

```ruby
begin
  # Get dashboard information
  data, status_code, headers = api_instance.get_va_system_threat_architecture_details_with_http_info(org_id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => Object
rescue EmassClient::ApiError => e
  puts "Error when calling DashboardsApi->get_va_system_threat_architecture_details_with_http_info: #{e}"
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


## get_va_system_threat_risk_summary

> Object get_va_system_threat_risk_summary(org_id, opts)

Get dashboard information

Get VA system threat risk summary dashboard information.

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

api_instance = EmassClient::DashboardsApi.new
org_id = 1 # Integer | **Organization Id**: The unique organization identifier.
opts = {
  excludeinherited: true, # Boolean | **Exclude Inherited**: If no value is specified, the default returns false to include inherited data. 
  page_index: 56, # Integer | **Page Index**: If no value is specified, the default returns results from the first page with an index of 0. 
  page_size: 56 # Integer | **Page Size**: If no value is specified, the default returns 20000 per page. 
}

begin
  # Get dashboard information
  result = api_instance.get_va_system_threat_risk_summary(org_id, opts)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling DashboardsApi->get_va_system_threat_risk_summary: #{e}"
end
```

#### Using the get_va_system_threat_risk_summary_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(Object, Integer, Hash)> get_va_system_threat_risk_summary_with_http_info(org_id, opts)

```ruby
begin
  # Get dashboard information
  data, status_code, headers = api_instance.get_va_system_threat_risk_summary_with_http_info(org_id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => Object
rescue EmassClient::ApiError => e
  puts "Error when calling DashboardsApi->get_va_system_threat_risk_summary_with_http_info: #{e}"
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


## get_va_system_threat_source_details

> Object get_va_system_threat_source_details(org_id, opts)

Get dashboard information

Get VA system threat source details dashboard information.

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

api_instance = EmassClient::DashboardsApi.new
org_id = 1 # Integer | **Organization Id**: The unique organization identifier.
opts = {
  excludeinherited: true, # Boolean | **Exclude Inherited**: If no value is specified, the default returns false to include inherited data. 
  page_index: 56, # Integer | **Page Index**: If no value is specified, the default returns results from the first page with an index of 0. 
  page_size: 56 # Integer | **Page Size**: If no value is specified, the default returns 20000 per page. 
}

begin
  # Get dashboard information
  result = api_instance.get_va_system_threat_source_details(org_id, opts)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling DashboardsApi->get_va_system_threat_source_details: #{e}"
end
```

#### Using the get_va_system_threat_source_details_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(Object, Integer, Hash)> get_va_system_threat_source_details_with_http_info(org_id, opts)

```ruby
begin
  # Get dashboard information
  data, status_code, headers = api_instance.get_va_system_threat_source_details_with_http_info(org_id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => Object
rescue EmassClient::ApiError => e
  puts "Error when calling DashboardsApi->get_va_system_threat_source_details_with_http_info: #{e}"
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

