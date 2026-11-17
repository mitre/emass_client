# \ArtifactsAPI

All URIs are relative to *http://localhost:4010*

Method | HTTP request | Description
------------- | ------------- | -------------
[**AddArtifactsBySystemId**](ArtifactsAPI.md#AddArtifactsBySystemId) | **Post** /api/systems/{systemId}/artifacts | Add one or many artifacts in a system
[**DeleteArtifact**](ArtifactsAPI.md#DeleteArtifact) | **Delete** /api/systems/{systemId}/artifacts | Remove one or many artifacts in a system
[**GetSystemArtifacts**](ArtifactsAPI.md#GetSystemArtifacts) | **Get** /api/systems/{systemId}/artifacts | Get one or many artifacts in a system
[**UpdateArtifactBySystemId**](ArtifactsAPI.md#UpdateArtifactBySystemId) | **Put** /api/systems/{systemId}/artifacts | Update one or many artifacts in a system



## AddArtifactsBySystemId

> ArtifactsResponsePutPost AddArtifactsBySystemId(ctx, systemId).Filename(filename).IsBulk(isBulk).IsTemplate(isTemplate).Type_(type_).Category(category).Execute()

Add one or many artifacts in a system



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/mitre/emass_client/src/go_client/v3"
)

func main() {
	systemId := int32(35) // int32 | **System Id**: The unique system record identifier.
	filename := os.NewFile(1234, "some_file") // *os.File | The file to upload. Must be a .zip file if isBulk is set to true, otherwise any acceptable artifact file. Max 30MB per artifact.
	isBulk := true // bool | **Is Bulk**: If no value is specified, the default is false, and an individual artifact file is expected. When set to true, a .zip file is expected which can contain multiple artifact files.  (optional) (default to false)
	isTemplate := true // bool | Is the artifact a template?  Indicates whether an artifact is a template (optional)
	type_ := "type__example" // string | The type of artifact. Possible values are:  Procedure, Diagram, Policy, Labor, Document, Image, Other, Scan Result, Auditor Report. May also accept custom artifact type values set by system administrators. (optional)
	category := "category_example" // string | The category of artifact. Possible values are:  Implementation Guidance, Evidence.  May also accept custom artifact category values set by system administrators. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ArtifactsAPI.AddArtifactsBySystemId(context.Background(), systemId).Filename(filename).IsBulk(isBulk).IsTemplate(isTemplate).Type_(type_).Category(category).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ArtifactsAPI.AddArtifactsBySystemId``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `AddArtifactsBySystemId`: ArtifactsResponsePutPost
	fmt.Fprintf(os.Stdout, "Response from `ArtifactsAPI.AddArtifactsBySystemId`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**systemId** | **int32** | **System Id**: The unique system record identifier. | 

### Other Parameters

Other parameters are passed through a pointer to a apiAddArtifactsBySystemIdRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **filename** | ***os.File** | The file to upload. Must be a .zip file if isBulk is set to true, otherwise any acceptable artifact file. Max 30MB per artifact. | 
 **isBulk** | **bool** | **Is Bulk**: If no value is specified, the default is false, and an individual artifact file is expected. When set to true, a .zip file is expected which can contain multiple artifact files.  | [default to false]
 **isTemplate** | **bool** | Is the artifact a template?  Indicates whether an artifact is a template | 
 **type_** | **string** | The type of artifact. Possible values are:  Procedure, Diagram, Policy, Labor, Document, Image, Other, Scan Result, Auditor Report. May also accept custom artifact type values set by system administrators. | 
 **category** | **string** | The category of artifact. Possible values are:  Implementation Guidance, Evidence.  May also accept custom artifact category values set by system administrators. | 

### Return type

[**ArtifactsResponsePutPost**](ArtifactsResponsePutPost.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeleteArtifact

> ArtifactsResponseDel DeleteArtifact(ctx, systemId).ArtifactsRequestDeleteBodyInner(artifactsRequestDeleteBodyInner).Execute()

Remove one or many artifacts in a system



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/mitre/emass_client/src/go_client/v3"
)

func main() {
	systemId := int32(35) // int32 | **System Id**: The unique system record identifier.
	artifactsRequestDeleteBodyInner := []openapiclient.ArtifactsRequestDeleteBodyInner{*openapiclient.NewArtifactsRequestDeleteBodyInner()} // []ArtifactsRequestDeleteBodyInner | Delete artifact files for the given System Id

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ArtifactsAPI.DeleteArtifact(context.Background(), systemId).ArtifactsRequestDeleteBodyInner(artifactsRequestDeleteBodyInner).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ArtifactsAPI.DeleteArtifact``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `DeleteArtifact`: ArtifactsResponseDel
	fmt.Fprintf(os.Stdout, "Response from `ArtifactsAPI.DeleteArtifact`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**systemId** | **int32** | **System Id**: The unique system record identifier. | 

### Other Parameters

Other parameters are passed through a pointer to a apiDeleteArtifactRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **artifactsRequestDeleteBodyInner** | [**[]ArtifactsRequestDeleteBodyInner**](ArtifactsRequestDeleteBodyInner.md) | Delete artifact files for the given System Id | 

### Return type

[**ArtifactsResponseDel**](ArtifactsResponseDel.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetSystemArtifacts

> ArtifactsResponseGet GetSystemArtifacts(ctx, systemId).Filename(filename).ControlAcronyms(controlAcronyms).AssessmentProcedures(assessmentProcedures).Ccis(ccis).SystemOnly(systemOnly).Execute()

Get one or many artifacts in a system



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/mitre/emass_client/src/go_client/v3"
)

func main() {
	systemId := int32(35) // int32 | **System Id**: The unique system record identifier.
	filename := "ArtifactsExporFile.pdf" // string | **File Name**: The file name (to include file-extension). (optional)
	controlAcronyms := "controlAcronyms_example" // string | **Control Acronym**: Filter query by given system acronym (single value or comma separated). (optional)
	assessmentProcedures := "assessmentProcedures_example" // string | **Assessment Procedure**: Filter query by given Security Control Assessment Procedure (single value or comma separated). (optional)
	ccis := "ccis_example" // string | **CCI System**: Filter query by Control Correlation Identifiers (CCIs) (single value or comma separated). (optional)
	systemOnly := true // bool | **Systems Only**: Indicates that only system(s) information is retrieved. (optional) (default to true)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ArtifactsAPI.GetSystemArtifacts(context.Background(), systemId).Filename(filename).ControlAcronyms(controlAcronyms).AssessmentProcedures(assessmentProcedures).Ccis(ccis).SystemOnly(systemOnly).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ArtifactsAPI.GetSystemArtifacts``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetSystemArtifacts`: ArtifactsResponseGet
	fmt.Fprintf(os.Stdout, "Response from `ArtifactsAPI.GetSystemArtifacts`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**systemId** | **int32** | **System Id**: The unique system record identifier. | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetSystemArtifactsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **filename** | **string** | **File Name**: The file name (to include file-extension). | 
 **controlAcronyms** | **string** | **Control Acronym**: Filter query by given system acronym (single value or comma separated). | 
 **assessmentProcedures** | **string** | **Assessment Procedure**: Filter query by given Security Control Assessment Procedure (single value or comma separated). | 
 **ccis** | **string** | **CCI System**: Filter query by Control Correlation Identifiers (CCIs) (single value or comma separated). | 
 **systemOnly** | **bool** | **Systems Only**: Indicates that only system(s) information is retrieved. | [default to true]

### Return type

[**ArtifactsResponseGet**](ArtifactsResponseGet.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UpdateArtifactBySystemId

> ArtifactsResponsePutPost UpdateArtifactBySystemId(ctx, systemId).ArtifactsRequiredFields(artifactsRequiredFields).Execute()

Update one or many artifacts in a system



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/mitre/emass_client/src/go_client/v3"
)

func main() {
	systemId := int32(35) // int32 | **System Id**: The unique system record identifier.
	artifactsRequiredFields := []openapiclient.ArtifactsRequiredFields{*openapiclient.NewArtifactsRequiredFields()} // []ArtifactsRequiredFields | See `information` above for additional instructions

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ArtifactsAPI.UpdateArtifactBySystemId(context.Background(), systemId).ArtifactsRequiredFields(artifactsRequiredFields).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ArtifactsAPI.UpdateArtifactBySystemId``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UpdateArtifactBySystemId`: ArtifactsResponsePutPost
	fmt.Fprintf(os.Stdout, "Response from `ArtifactsAPI.UpdateArtifactBySystemId`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**systemId** | **int32** | **System Id**: The unique system record identifier. | 

### Other Parameters

Other parameters are passed through a pointer to a apiUpdateArtifactBySystemIdRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **artifactsRequiredFields** | [**[]ArtifactsRequiredFields**](ArtifactsRequiredFields.md) | See &#x60;information&#x60; above for additional instructions | 

### Return type

[**ArtifactsResponsePutPost**](ArtifactsResponsePutPost.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

