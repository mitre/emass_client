# EmassClient::ArtifactsApi

All URIs are relative to *http://localhost:4010*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**add_artifacts_by_system_id**](ArtifactsApi.md#add_artifacts_by_system_id) | **POST** /api/systems/{systemId}/artifacts | Add one or many artifacts in a system |
| [**delete_artifact**](ArtifactsApi.md#delete_artifact) | **DELETE** /api/systems/{systemId}/artifacts | Remove one or many artifacts in a system |
| [**get_system_artifacts**](ArtifactsApi.md#get_system_artifacts) | **GET** /api/systems/{systemId}/artifacts | Get one or many artifacts in a system |
| [**update_artifact_by_system_id**](ArtifactsApi.md#update_artifact_by_system_id) | **PUT** /api/systems/{systemId}/artifacts | Update one or many artifacts in a system |


## add_artifacts_by_system_id

> <ArtifactsResponsePutPost> add_artifacts_by_system_id(system_id, zipper, opts)

Add one or many artifacts in a system

<strong>Information</strong><br> The request body of a POST request through the Artifact Endpoint accepts a single binary file with file extension \".zip\" only. This accepted .zip file should contain one or more files corresponding to existing artifacts or new artifacts that will be created upon successful receipt. Filename uniqueness throughout eMASS will be enforced by the API.<br><br> Upon successful receipt of a file, if a file within the .zip is matched via filename to an artifact existing within the application, the file associated with the artifact will be updated. If no artifact is matched via filename to the application, a new artifact will be created with the following default values. Any values not specified below will be blank. <ul>   <li>isTemplate: false</li>   <li>type: other</li>   <li>category: evidence</li> </ul> To update values other than the file itself, please submit a PUT request.<br>  <strong>Zip file information</strong><br> Upload a zip file contain one or more files corresponding to existing artifacts or new artifacts that will be created upon successful receipt.<br><br> <strong>Business Rules</strong><br> Artifact cannot be saved if the file does not have the following file extensions:      .docx,.doc,.txt,.rtf,.xfdl,.xml,.mht,.mh,tml,.html,.htm,.pdf,.mdb,.accdb,.ppt,     .pptx,.xls,.xlsx,.csv,.log,.jpeg,.jpg,.tiff,.bmp,.tif,.png,.gif,.zip,.rar,.msg,     .vsd,.vsw,.vdx,.z{#},.ckl,.avi,.vsdx  Artifact version cannot be saved if an Artifact with the same file name already exist in the system.  Artifact cannot be saved if the file size exceeds 30MB.

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

api_instance = EmassClient::ArtifactsApi.new
system_id = 35 # Integer | **System Id**: The unique system record identifier.
zipper = File.new('/path/to/some/file') # File | 
opts = {
  is_template: true, # Boolean | 
  type: 'Procedure', # String | 
  category: 'Implementation Guidance' # String | 
}

begin
  # Add one or many artifacts in a system
  result = api_instance.add_artifacts_by_system_id(system_id, zipper, opts)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling ArtifactsApi->add_artifacts_by_system_id: #{e}"
end
```

#### Using the add_artifacts_by_system_id_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ArtifactsResponsePutPost>, Integer, Hash)> add_artifacts_by_system_id_with_http_info(system_id, zipper, opts)

```ruby
begin
  # Add one or many artifacts in a system
  data, status_code, headers = api_instance.add_artifacts_by_system_id_with_http_info(system_id, zipper, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ArtifactsResponsePutPost>
rescue EmassClient::ApiError => e
  puts "Error when calling ArtifactsApi->add_artifacts_by_system_id_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **system_id** | **Integer** | **System Id**: The unique system record identifier. |  |
| **zipper** | **File** |  |  |
| **is_template** | **Boolean** |  | [optional] |
| **type** | **String** |  | [optional] |
| **category** | **String** |  | [optional] |

### Return type

[**ArtifactsResponsePutPost**](ArtifactsResponsePutPost.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## delete_artifact

> <ArtifactsResponseDel> delete_artifact(system_id, opts)

Remove one or many artifacts in a system

Remove the Artifact(s) matching `systemId` path parameter and request body artifact(s) file name<br><br> <b>Note:</b> Multiple files can be deleted by providing multiple file names at the CL (comma delimited)  Example: --files file1.txt, file2.txt

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

api_instance = EmassClient::ArtifactsApi.new
system_id = 35 # Integer | **System Id**: The unique system record identifier.
opts = {
  delete_artifacts_inner: [EmassClient::DeleteArtifactsInner.new] # Array<DeleteArtifactsInner> | Delete artifact files for the given System Id
}

begin
  # Remove one or many artifacts in a system
  result = api_instance.delete_artifact(system_id, opts)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling ArtifactsApi->delete_artifact: #{e}"
end
```

#### Using the delete_artifact_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ArtifactsResponseDel>, Integer, Hash)> delete_artifact_with_http_info(system_id, opts)

```ruby
begin
  # Remove one or many artifacts in a system
  data, status_code, headers = api_instance.delete_artifact_with_http_info(system_id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ArtifactsResponseDel>
rescue EmassClient::ApiError => e
  puts "Error when calling ArtifactsApi->delete_artifact_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **system_id** | **Integer** | **System Id**: The unique system record identifier. |  |
| **delete_artifacts_inner** | [**Array&lt;DeleteArtifactsInner&gt;**](DeleteArtifactsInner.md) | Delete artifact files for the given System Id | [optional] |

### Return type

[**ArtifactsResponseDel**](ArtifactsResponseDel.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## get_system_artifacts

> <ArtifactsResponseGet> get_system_artifacts(system_id, opts)

Get one or many artifacts in a system

Returns selected artifacts matching parameters to include the file name containing the artifacts.

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

api_instance = EmassClient::ArtifactsApi.new
system_id = 35 # Integer | **System Id**: The unique system record identifier.
opts = {
  filename: 'ArtifactsExporFile.pdf', # String | **File Name**: The file name (to include file-extension).
  control_acronyms: 'control_acronyms_example', # String | **System Acronym**: Filter query by given system acronym (single or comma separated).
  ccis: 'ccis_example', # String | **CCI System**: Filter query by Control Correlation Identifiers (CCIs) (single or comma separated).
  system_only: true # Boolean | **Systems Only**: Indicates that only system(s) information is retrieved.
}

begin
  # Get one or many artifacts in a system
  result = api_instance.get_system_artifacts(system_id, opts)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling ArtifactsApi->get_system_artifacts: #{e}"
end
```

#### Using the get_system_artifacts_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ArtifactsResponseGet>, Integer, Hash)> get_system_artifacts_with_http_info(system_id, opts)

```ruby
begin
  # Get one or many artifacts in a system
  data, status_code, headers = api_instance.get_system_artifacts_with_http_info(system_id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ArtifactsResponseGet>
rescue EmassClient::ApiError => e
  puts "Error when calling ArtifactsApi->get_system_artifacts_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **system_id** | **Integer** | **System Id**: The unique system record identifier. |  |
| **filename** | **String** | **File Name**: The file name (to include file-extension). | [optional] |
| **control_acronyms** | **String** | **System Acronym**: Filter query by given system acronym (single or comma separated). | [optional] |
| **ccis** | **String** | **CCI System**: Filter query by Control Correlation Identifiers (CCIs) (single or comma separated). | [optional] |
| **system_only** | **Boolean** | **Systems Only**: Indicates that only system(s) information is retrieved. | [optional][default to true] |

### Return type

[**ArtifactsResponseGet**](ArtifactsResponseGet.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## update_artifact_by_system_id

> <ArtifactsResponsePutPost> update_artifact_by_system_id(system_id, request_body)

Update one or many artifacts in a system

Updates an artifact for given `systemId` path parameter<br><br>  **Request Body Required Fields** - `filename` - `isTemplate` - `type` - `category`

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

api_instance = EmassClient::ArtifactsApi.new
system_id = 35 # Integer | **System Id**: The unique system record identifier.
request_body = [3.56] # Array<Object> | See `information` above for additional instructions

begin
  # Update one or many artifacts in a system
  result = api_instance.update_artifact_by_system_id(system_id, request_body)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling ArtifactsApi->update_artifact_by_system_id: #{e}"
end
```

#### Using the update_artifact_by_system_id_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ArtifactsResponsePutPost>, Integer, Hash)> update_artifact_by_system_id_with_http_info(system_id, request_body)

```ruby
begin
  # Update one or many artifacts in a system
  data, status_code, headers = api_instance.update_artifact_by_system_id_with_http_info(system_id, request_body)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ArtifactsResponsePutPost>
rescue EmassClient::ApiError => e
  puts "Error when calling ArtifactsApi->update_artifact_by_system_id_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **system_id** | **Integer** | **System Id**: The unique system record identifier. |  |
| **request_body** | [**Array&lt;Object&gt;**](Object.md) | See &#x60;information&#x60; above for additional instructions |  |

### Return type

[**ArtifactsResponsePutPost**](ArtifactsResponsePutPost.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

