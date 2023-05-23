# emass_client.ArtifactsApi

All URIs are relative to *http://localhost:4010*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_artifacts_by_system_id**](ArtifactsApi.md#add_artifacts_by_system_id) | **POST** /api/systems/{systemId}/artifacts | Add one or many artifacts in a system
[**delete_artifact**](ArtifactsApi.md#delete_artifact) | **DELETE** /api/systems/{systemId}/artifacts | Remove one or many artifacts in a system
[**get_system_artifacts**](ArtifactsApi.md#get_system_artifacts) | **GET** /api/systems/{systemId}/artifacts | Get one or many artifacts in a system
[**update_artifact_by_system_id**](ArtifactsApi.md#update_artifact_by_system_id) | **PUT** /api/systems/{systemId}/artifacts | Update one or many artifacts in a system


# **add_artifacts_by_system_id**
> ArtifactsResponsePutPost add_artifacts_by_system_id(system_id, zipper, is_bulk=is_bulk, is_template=is_template, type=type, category=category)

Add one or many artifacts in a system

<strong>Information</strong><br> The body of a request through the Artifacts POST endpoint accepts a single binary file. Two  Artifact POST methods are currently accepted: individual and bulk. Filename uniqueness within  an eMASS system will be enforced by the API for both methods. <br><br> For POST requests that should result in a single artifact, the request should include the file. <br><br> For POST requests that should result in the creation of many artifacts, the request should include  a single file with the extension \".zip\" only and the parameter isBulk should be set to true. This  .zip file should contain one or more files corresponding to existing artifacts or new artifacts that  will be created upon successful receipt. <br><br> Upon successful receipt of one or many artifacts, if a file is matched via filename to an artifact  existing within the application, the file associated with the artifact will be updated. If no artifact  is matched via filename to the application, a new artifact will be created with the following  default values. Any values not specified below will be null <ul>   <li>isTemplate: false</li>   <li>type: Other</li>   <li>category: Evidence</li> </ul> To update values other than the file itself, please submit a PUT request.<br>  <strong>Business Rules</strong><br> Artifact cannot be saved if the fields below exceed the following character limits: <ul>   <li>Filename - 1,000 characters</li>   <li>Name - 100 characters</li>   <li>Description - 10,000 characters</li>   <li>Reference Page Number - 50 characters</li> </ul> Artifact cannot be saved if the file does not have an allowable file extension/type:      .docx,.doc,.txt,.rtf,.xfdl,.xml,.mht,.mh,tml,.html,.htm,.pdf,.mdb,.accdb,.ppt,     .pptx,.xls,.xlsx,.csv,.log,.jpeg,.jpg,.tiff,.bmp,.tif,.png,.gif,.zip,.rar,.msg,     .vsd,.vsw,.vdx,.z{#},.ckl,.avi,.vsdx  Artifact version cannot be saved if an Artifact with the same file name already exist in the system.  Artifact cannot be saved if the file size exceeds 30MB.  Artifact cannot be saved if the following fields are missing data: <ul>   <li>Filename</li>   <li>Type</li>   <li>Category</li> </ul>  Artifact cannot be saved if the Last Review Date (`lastReviewedDate`) is set in the future.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (mockType):
* Api Key Authentication (userId):
```python
import time
import os
import emass_client
from emass_client.models.artifacts_response_put_post import ArtifactsResponsePutPost
from emass_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:4010
# See configuration.py for a list of all supported configuration parameters.
configuration = emass_client.Configuration(
    host = "http://localhost:4010"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: mockType
configuration.api_key['mockType'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['mockType'] = 'Bearer'

# Configure API key authorization: userId
configuration.api_key['userId'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userId'] = 'Bearer'

# Enter a context with an instance of the API client
with emass_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = emass_client.ArtifactsApi(api_client)
    system_id = 35 # int | **System Id**: The unique system record identifier.
    zipper = None # bytearray | 
    is_bulk = False # bool | **Is Bulk**: If no value is specified, the default is false, and an individual artifact file is expected.  When set to true, a .zip file is expected which  can contain multiple artifact files\"  (optional) (default to False)
    is_template = True # bool |  (optional)
    type = 'type_example' # str |  (optional)
    category = 'category_example' # str |  (optional)

    try:
        # Add one or many artifacts in a system
        api_response = api_instance.add_artifacts_by_system_id(system_id, zipper, is_bulk=is_bulk, is_template=is_template, type=type, category=category)
        print("The response of ArtifactsApi->add_artifacts_by_system_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArtifactsApi->add_artifacts_by_system_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **int**| **System Id**: The unique system record identifier. | 
 **zipper** | **bytearray**|  | 
 **is_bulk** | **bool**| **Is Bulk**: If no value is specified, the default is false, and an individual artifact file is expected.  When set to true, a .zip file is expected which  can contain multiple artifact files\&quot;  | [optional] [default to False]
 **is_template** | **bool**|  | [optional] 
 **type** | **str**|  | [optional] 
 **category** | **str**|  | [optional] 

### Return type

[**ArtifactsResponsePutPost**](ArtifactsResponsePutPost.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**405** | Method Not Allowed |  -  |
**411** | Length Required |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_artifact**
> ArtifactsResponseDel delete_artifact(system_id, artifacts_request_delete_body_inner)

Remove one or many artifacts in a system

Remove the Artifact(s) matching `systemId` path parameter and request body artifact(s) file name<br><br> <b>Note:</b> Multiple files can be deleted by providing multiple file names at the CL (comma delimited)  Example: --files file1.txt, file2.txt

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (mockType):
* Api Key Authentication (userId):
```python
import time
import os
import emass_client
from emass_client.models.artifacts_request_delete_body_inner import ArtifactsRequestDeleteBodyInner
from emass_client.models.artifacts_response_del import ArtifactsResponseDel
from emass_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:4010
# See configuration.py for a list of all supported configuration parameters.
configuration = emass_client.Configuration(
    host = "http://localhost:4010"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: mockType
configuration.api_key['mockType'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['mockType'] = 'Bearer'

# Configure API key authorization: userId
configuration.api_key['userId'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userId'] = 'Bearer'

# Enter a context with an instance of the API client
with emass_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = emass_client.ArtifactsApi(api_client)
    system_id = 35 # int | **System Id**: The unique system record identifier.
    artifacts_request_delete_body_inner = [emass_client.ArtifactsRequestDeleteBodyInner()] # List[ArtifactsRequestDeleteBodyInner] | Delete artifact files for the given System Id

    try:
        # Remove one or many artifacts in a system
        api_response = api_instance.delete_artifact(system_id, artifacts_request_delete_body_inner)
        print("The response of ArtifactsApi->delete_artifact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArtifactsApi->delete_artifact: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **int**| **System Id**: The unique system record identifier. | 
 **artifacts_request_delete_body_inner** | [**List[ArtifactsRequestDeleteBodyInner]**](ArtifactsRequestDeleteBodyInner.md)| Delete artifact files for the given System Id | 

### Return type

[**ArtifactsResponseDel**](ArtifactsResponseDel.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_artifacts**
> ArtifactsResponseGet get_system_artifacts(system_id, filename=filename, control_acronyms=control_acronyms, ccis=ccis, system_only=system_only)

Get one or many artifacts in a system

Returns selected artifacts matching parameters to include the file name containing the artifacts.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (mockType):
* Api Key Authentication (userId):
```python
import time
import os
import emass_client
from emass_client.models.artifacts_response_get import ArtifactsResponseGet
from emass_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:4010
# See configuration.py for a list of all supported configuration parameters.
configuration = emass_client.Configuration(
    host = "http://localhost:4010"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: mockType
configuration.api_key['mockType'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['mockType'] = 'Bearer'

# Configure API key authorization: userId
configuration.api_key['userId'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userId'] = 'Bearer'

# Enter a context with an instance of the API client
with emass_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = emass_client.ArtifactsApi(api_client)
    system_id = 35 # int | **System Id**: The unique system record identifier.
    filename = 'ArtifactsExporFile.pdf' # str | **File Name**: The file name (to include file-extension). (optional)
    control_acronyms = 'control_acronyms_example' # str | **System Acronym**: Filter query by given system acronym (single or comma separated). (optional)
    ccis = 'ccis_example' # str | **CCI System**: Filter query by Control Correlation Identifiers (CCIs) (single or comma separated). (optional)
    system_only = True # bool | **Systems Only**: Indicates that only system(s) information is retrieved. (optional) (default to True)

    try:
        # Get one or many artifacts in a system
        api_response = api_instance.get_system_artifacts(system_id, filename=filename, control_acronyms=control_acronyms, ccis=ccis, system_only=system_only)
        print("The response of ArtifactsApi->get_system_artifacts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArtifactsApi->get_system_artifacts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **int**| **System Id**: The unique system record identifier. | 
 **filename** | **str**| **File Name**: The file name (to include file-extension). | [optional] 
 **control_acronyms** | **str**| **System Acronym**: Filter query by given system acronym (single or comma separated). | [optional] 
 **ccis** | **str**| **CCI System**: Filter query by Control Correlation Identifiers (CCIs) (single or comma separated). | [optional] 
 **system_only** | **bool**| **Systems Only**: Indicates that only system(s) information is retrieved. | [optional] [default to True]

### Return type

[**ArtifactsResponseGet**](ArtifactsResponseGet.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**405** | Method Not Allowed |  -  |
**490** | API Rule Failed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_artifact_by_system_id**
> ArtifactsResponsePutPost update_artifact_by_system_id(system_id, request_body)

Update one or many artifacts in a system

Updates an artifact for given `systemId` path parameter<br><br>  **Request Body Required Fields** - `filename` - `isTemplate` - `type` - `category`

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (mockType):
* Api Key Authentication (userId):
```python
import time
import os
import emass_client
from emass_client.models.artifacts_response_put_post import ArtifactsResponsePutPost
from emass_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:4010
# See configuration.py for a list of all supported configuration parameters.
configuration = emass_client.Configuration(
    host = "http://localhost:4010"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: mockType
configuration.api_key['mockType'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['mockType'] = 'Bearer'

# Configure API key authorization: userId
configuration.api_key['userId'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userId'] = 'Bearer'

# Enter a context with an instance of the API client
with emass_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = emass_client.ArtifactsApi(api_client)
    system_id = 35 # int | **System Id**: The unique system record identifier.
    request_body = None # List[object] | See `information` above for additional instructions

    try:
        # Update one or many artifacts in a system
        api_response = api_instance.update_artifact_by_system_id(system_id, request_body)
        print("The response of ArtifactsApi->update_artifact_by_system_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArtifactsApi->update_artifact_by_system_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **int**| **System Id**: The unique system record identifier. | 
 **request_body** | [**List[object]**](object.md)| See &#x60;information&#x60; above for additional instructions | 

### Return type

[**ArtifactsResponsePutPost**](ArtifactsResponsePutPost.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

