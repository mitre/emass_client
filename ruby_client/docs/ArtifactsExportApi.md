# EmassClient::ArtifactsExportApi

All URIs are relative to *http://localhost:4010*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**get_system_artifacts_export**](ArtifactsExportApi.md#get_system_artifacts_export) | **GET** /api/systems/{systemId}/artifacts-export | Get the file of an artifact in a system |


## get_system_artifacts_export

> String get_system_artifacts_export(system_id, filename, opts)

Get the file of an artifact in a system

<strong>Sample Responce</strong><br>  Binary file associated with given filename.<br>  If `compress` parameter is specified, zip archive of binary file associated with given filename.

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

api_instance = EmassClient::ArtifactsExportApi.new
system_id = 35 # Integer | **System Id**: The unique system record identifier.
filename = 'ArtifactsExporFile.pdf' # String | **File Name**: The file name (to include file-extension).
opts = {
  compress: true # Boolean | **Compress File**: Determines if returned file is compressed.
}

begin
  # Get the file of an artifact in a system
  result = api_instance.get_system_artifacts_export(system_id, filename, opts)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling ArtifactsExportApi->get_system_artifacts_export: #{e}"
end
```

#### Using the get_system_artifacts_export_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(String, Integer, Hash)> get_system_artifacts_export_with_http_info(system_id, filename, opts)

```ruby
begin
  # Get the file of an artifact in a system
  data, status_code, headers = api_instance.get_system_artifacts_export_with_http_info(system_id, filename, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => String
rescue EmassClient::ApiError => e
  puts "Error when calling ArtifactsExportApi->get_system_artifacts_export_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **system_id** | **Integer** | **System Id**: The unique system record identifier. |  |
| **filename** | **String** | **File Name**: The file name (to include file-extension). |  |
| **compress** | **Boolean** | **Compress File**: Determines if returned file is compressed. | [optional][default to true] |

### Return type

**String**

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain, application/octet-stream, application/json

