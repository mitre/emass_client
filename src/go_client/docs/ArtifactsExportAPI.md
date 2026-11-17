# \ArtifactsExportAPI

All URIs are relative to *http://localhost:4010*

Method | HTTP request | Description
------------- | ------------- | -------------
[**GetSystemArtifactsExport**](ArtifactsExportAPI.md#GetSystemArtifactsExport) | **Get** /api/systems/{systemId}/artifacts-export | Get the file of an artifact in a system



## GetSystemArtifactsExport

> *os.File GetSystemArtifactsExport(ctx, systemId).Filename(filename).Compress(compress).Execute()

Get the file of an artifact in a system



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
	filename := "ArtifactsExporFile.pdf" // string | **File Name**: The file name (to include file-extension).
	compress := true // bool | **Compress File**: Determines if returned file is compressed. (optional) (default to true)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ArtifactsExportAPI.GetSystemArtifactsExport(context.Background(), systemId).Filename(filename).Compress(compress).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ArtifactsExportAPI.GetSystemArtifactsExport``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetSystemArtifactsExport`: *os.File
	fmt.Fprintf(os.Stdout, "Response from `ArtifactsExportAPI.GetSystemArtifactsExport`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**systemId** | **int32** | **System Id**: The unique system record identifier. | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetSystemArtifactsExportRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **filename** | **string** | **File Name**: The file name (to include file-extension). | 
 **compress** | **bool** | **Compress File**: Determines if returned file is compressed. | [default to true]

### Return type

[***os.File**](*os.File.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

