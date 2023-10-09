# EmassClient::TestResultsApi

All URIs are relative to *http://localhost:4010*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**add_test_results_by_system_id**](TestResultsApi.md#add_test_results_by_system_id) | **POST** /api/systems/{systemId}/test-results | Add one or many test results in a system |
| [**get_system_test_results**](TestResultsApi.md#get_system_test_results) | **GET** /api/systems/{systemId}/test-results | Get one or many test results in a system |


## add_test_results_by_system_id

> <TestResultsResponsePost> add_test_results_by_system_id(system_id, request_body)

Add one or many test results in a system

Adds test results for given `systemId`  **Request Body Required Fields** - `testedBy` - `testDate` - `description` - `complianceStatus` - `assessmentProcedure`       

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

api_instance = EmassClient::TestResultsApi.new
system_id = 35 # Integer | **System Id**: The unique system record identifier.
request_body = [3.56] # Array<Object> | Add test results to a system (systemId)

begin
  # Add one or many test results in a system
  result = api_instance.add_test_results_by_system_id(system_id, request_body)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling TestResultsApi->add_test_results_by_system_id: #{e}"
end
```

#### Using the add_test_results_by_system_id_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TestResultsResponsePost>, Integer, Hash)> add_test_results_by_system_id_with_http_info(system_id, request_body)

```ruby
begin
  # Add one or many test results in a system
  data, status_code, headers = api_instance.add_test_results_by_system_id_with_http_info(system_id, request_body)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TestResultsResponsePost>
rescue EmassClient::ApiError => e
  puts "Error when calling TestResultsApi->add_test_results_by_system_id_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **system_id** | **Integer** | **System Id**: The unique system record identifier. |  |
| **request_body** | [**Array&lt;Object&gt;**](Object.md) | Add test results to a system (systemId) |  |

### Return type

[**TestResultsResponsePost**](TestResultsResponsePost.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## get_system_test_results

> <TestResultsResponseGet> get_system_test_results(system_id, opts)

Get one or many test results in a system

Returns system test results information for matching parameters.<br>

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

api_instance = EmassClient::TestResultsApi.new
system_id = 35 # Integer | **System Id**: The unique system record identifier.
opts = {
  control_acronyms: 'control_acronyms_example', # String | **Control Acronym**: Filter query by given system acronym (single value or comma separated).
  assessment_procedures: 'assessment_procedures_example', # String | **Assessment Procedure**: Filter query by given Security Control Assessment Procedure (single value or comma separated).
  ccis: 'ccis_example', # String | **CCI System**: Filter query by Control Correlation Identifiers (CCIs) (single value or comma separated).
  latest_only: true # Boolean | **Latest Results Only**: Indicates that only the latest test resultes are retrieved.
}

begin
  # Get one or many test results in a system
  result = api_instance.get_system_test_results(system_id, opts)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling TestResultsApi->get_system_test_results: #{e}"
end
```

#### Using the get_system_test_results_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TestResultsResponseGet>, Integer, Hash)> get_system_test_results_with_http_info(system_id, opts)

```ruby
begin
  # Get one or many test results in a system
  data, status_code, headers = api_instance.get_system_test_results_with_http_info(system_id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TestResultsResponseGet>
rescue EmassClient::ApiError => e
  puts "Error when calling TestResultsApi->get_system_test_results_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **system_id** | **Integer** | **System Id**: The unique system record identifier. |  |
| **control_acronyms** | **String** | **Control Acronym**: Filter query by given system acronym (single value or comma separated). | [optional] |
| **assessment_procedures** | **String** | **Assessment Procedure**: Filter query by given Security Control Assessment Procedure (single value or comma separated). | [optional] |
| **ccis** | **String** | **CCI System**: Filter query by Control Correlation Identifiers (CCIs) (single value or comma separated). | [optional] |
| **latest_only** | **Boolean** | **Latest Results Only**: Indicates that only the latest test resultes are retrieved. | [optional][default to true] |

### Return type

[**TestResultsResponseGet**](TestResultsResponseGet.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

