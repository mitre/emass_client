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

<strong>Information</strong><br> The body of a request through the Artifacts POST endpoint accepts a single binary file. Two  Artifact POST methods are currently accepted: individual and bulk. Filename uniqueness within  an eMASS system will be enforced by the API for both methods. <br><br> For POST requests that should result in a single artifact, the request should include the file. <br><br> For POST requests that should result in the creation of many artifacts, the request should include  a single file with the extension \".zip\" only and the parameter isBulk should be set to true. This  .zip file should contain one or more files corresponding to existing artifacts or new artifacts that  will be created upon successful receipt. <br><br> Upon successful receipt of one or many artifacts, if a file is matched via filename to an artifact  existing within the application, the file associated with the artifact will be updated. If no artifact  is matched via filename to the application, a new artifact will be created with the following  default values. Any values not specified below will be null <ul>   <li>isTemplate: false</li>   <li>type: Other</li>   <li>category: Evidence</li> </ul> To update values other than the file itself, please submit a PUT request.<br>  <strong>Business Rules</strong><br> Artifact cannot be saved if the fields below exceed the following character limits: <ul>   <li>Filename - 1,000 characters</li>   <li>Name - 100 characters</li>   <li>Description - 10,000 characters</li>   <li>Reference Page Number - 50 characters</li> </ul> Artifact cannot be saved if the file does not have an allowable file extension/type:      .docx,.doc,.txt,.rtf,.xfdl,.xml,.mht,.mh,tml,.html,.htm,.pdf,.mdb,.accdb,.ppt,     .pptx,.xls,.xlsx,.csv,.log,.jpeg,.jpg,.tiff,.bmp,.tif,.png,.gif,.zip,.rar,.msg,     .vsd,.vsw,.vdx,.z{#},.ckl,.avi,.vsdx  Artifact version cannot be saved if an Artifact with the same file name (filename) already exist in the system.  Artifact cannot be saved if the file size exceeds 30MB.  Artifact cannot be saved if the following fields are missing data: <ul>   <li>Filename (filename)</li>   <li>Type (type)</li>   <li>Category (category)</li> </ul>  Artifact cannot be saved if the Last Review Date (`lastReviewedDate`) is set in the future.

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
  is_bulk: true, # Boolean | **Is Bulk**: If no value is specified, the default is false, and an individual artifact file is expected.  When set to true, a .zip file is expected which  can contain multiple artifact files\" 
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
| **is_bulk** | **Boolean** | **Is Bulk**: If no value is specified, the default is false, and an individual artifact file is expected.  When set to true, a .zip file is expected which  can contain multiple artifact files\&quot;  | [optional][default to false] |
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

> <ArtifactsResponseDel> delete_artifact(system_id, artifacts_request_delete_body_inner)

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
artifacts_request_delete_body_inner = [EmassClient::ArtifactsRequestDeleteBodyInner.new] # Array<ArtifactsRequestDeleteBodyInner> | Delete artifact files for the given System Id

begin
  # Remove one or many artifacts in a system
  result = api_instance.delete_artifact(system_id, artifacts_request_delete_body_inner)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling ArtifactsApi->delete_artifact: #{e}"
end
```

#### Using the delete_artifact_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ArtifactsResponseDel>, Integer, Hash)> delete_artifact_with_http_info(system_id, artifacts_request_delete_body_inner)

```ruby
begin
  # Remove one or many artifacts in a system
  data, status_code, headers = api_instance.delete_artifact_with_http_info(system_id, artifacts_request_delete_body_inner)
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
| **artifacts_request_delete_body_inner** | [**Array&lt;ArtifactsRequestDeleteBodyInner&gt;**](ArtifactsRequestDeleteBodyInner.md) | Delete artifact files for the given System Id |  |

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
  control_acronyms: 'control_acronyms_example', # String | **Control Acronym**: Filter query by given system acronym (single value or comma separated).
  assessment_procedures: 'assessment_procedures_example', # String | **Assessment Procedure**: Filter query by given Security Control Assessment Procedure (single value or comma separated).
  ccis: 'ccis_example', # String | **CCI System**: Filter query by Control Correlation Identifiers (CCIs) (single value or comma separated).
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
| **control_acronyms** | **String** | **Control Acronym**: Filter query by given system acronym (single value or comma separated). | [optional] |
| **assessment_procedures** | **String** | **Assessment Procedure**: Filter query by given Security Control Assessment Procedure (single value or comma separated). | [optional] |
| **ccis** | **String** | **CCI System**: Filter query by Control Correlation Identifiers (CCIs) (single value or comma separated). | [optional] |
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

Updates an artifact for given `systemId` path parameter<br><br>  **Request Body Required Fields** - `filename` - `isTemplate` - `type` - `category`  <strong>Information</strong><br> The PUT request will replace all existing data with the field/value combinations included in the request body.   If any fields are not included, the absent fields will become null.     The fields `name` and `isTemplate` are non-nullable fields. If not specified in the PUT command they will default to the following:   - `name=filename`   - `isTemplate=false`    Also, note that one-to-many fields (`controls` and `ccis`) will also be replaced with the values specified in the PUT.  If existing `control or cci` mappings exist in eMASS, the values in the PUT will not append, but  rather replace all existing control and cci mappings with the values in the request body.

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

