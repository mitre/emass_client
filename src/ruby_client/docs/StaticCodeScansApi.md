# EmassClient::StaticCodeScansApi

All URIs are relative to *http://localhost:4010*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**add_static_code_scans_by_system_id**](StaticCodeScansApi.md#add_static_code_scans_by_system_id) | **POST** /api/systems/{systemId}/static-code-scans | Upload static code scans or Clear static code scans |


## add_static_code_scans_by_system_id

> <StaticCodeResponsePost> add_static_code_scans_by_system_id(system_id, static_code_request_post_body)

Upload static code scans or Clear static code scans

Upload or clear application scan findings into a system's `systemId` assets module.  **Request Body Required Fields** - Application Object (`application`)   - `applicationName`   - `version` - Application Findings Object Array (`applicationFindings`)   - `codeCheckName`   - `count`   - `scanDate`             - `cweId`  **Note:** To clear an application's findings, use only the field `clearFindings` as the Request body and set it to true. Example:  ``` [    {      \"application\": {        \"applicationName\": \"application name\",        \"version\": \"application version\"      },      \"applicationFindings\": [        { \"clearFindings\": true }      ]    }  ] ```

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

api_instance = EmassClient::StaticCodeScansApi.new
system_id = 35 # Integer | **System Id**: The unique system record identifier.
static_code_request_post_body = EmassClient::StaticCodeRequestPostBody.new # StaticCodeRequestPostBody | Add static code scans or Clear static code scans

begin
  # Upload static code scans or Clear static code scans
  result = api_instance.add_static_code_scans_by_system_id(system_id, static_code_request_post_body)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling StaticCodeScansApi->add_static_code_scans_by_system_id: #{e}"
end
```

#### Using the add_static_code_scans_by_system_id_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<StaticCodeResponsePost>, Integer, Hash)> add_static_code_scans_by_system_id_with_http_info(system_id, static_code_request_post_body)

```ruby
begin
  # Upload static code scans or Clear static code scans
  data, status_code, headers = api_instance.add_static_code_scans_by_system_id_with_http_info(system_id, static_code_request_post_body)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <StaticCodeResponsePost>
rescue EmassClient::ApiError => e
  puts "Error when calling StaticCodeScansApi->add_static_code_scans_by_system_id_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **system_id** | **Integer** | **System Id**: The unique system record identifier. |  |
| **static_code_request_post_body** | [**StaticCodeRequestPostBody**](StaticCodeRequestPostBody.md) | Add static code scans or Clear static code scans |  |

### Return type

[**StaticCodeResponsePost**](StaticCodeResponsePost.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

