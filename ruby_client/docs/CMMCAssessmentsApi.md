# EmassClient::CMMCAssessmentsApi

All URIs are relative to *http://localhost:4010*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**get_cmmc_assessments**](CMMCAssessmentsApi.md#get_cmmc_assessments) | **GET** /api/cmmc-assessments | Get CMMC assessment information |


## get_cmmc_assessments

> <CmmcResponseGet> get_cmmc_assessments(since_date)

Get CMMC assessment information

Get all CMMC assessment after the given date `sinceDate` parameter. It is available to CMMC eMASS only.

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

api_instance = EmassClient::CMMCAssessmentsApi.new
since_date = '1638764040' # String | **Date** CMMC date (Unix date format)

begin
  # Get CMMC assessment information
  result = api_instance.get_cmmc_assessments(since_date)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling CMMCAssessmentsApi->get_cmmc_assessments: #{e}"
end
```

#### Using the get_cmmc_assessments_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<CmmcResponseGet>, Integer, Hash)> get_cmmc_assessments_with_http_info(since_date)

```ruby
begin
  # Get CMMC assessment information
  data, status_code, headers = api_instance.get_cmmc_assessments_with_http_info(since_date)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <CmmcResponseGet>
rescue EmassClient::ApiError => e
  puts "Error when calling CMMCAssessmentsApi->get_cmmc_assessments_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **since_date** | **String** | **Date** CMMC date (Unix date format) |  |

### Return type

[**CmmcResponseGet**](CmmcResponseGet.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

