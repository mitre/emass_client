# \StaticCodeScansAPI

All URIs are relative to *http://localhost:4010*

Method | HTTP request | Description
------------- | ------------- | -------------
[**AddStaticCodeScansBySystemId**](StaticCodeScansAPI.md#AddStaticCodeScansBySystemId) | **Post** /api/systems/{systemId}/static-code-scans | Upload static code scans or Clear static code scans



## AddStaticCodeScansBySystemId

> StaticCodeResponsePost AddStaticCodeScansBySystemId(ctx, systemId).StaticCodeRequestPostBody(staticCodeRequestPostBody).Execute()

Upload static code scans or Clear static code scans



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
	staticCodeRequestPostBody := *openapiclient.NewStaticCodeRequestPostBody() // StaticCodeRequestPostBody | Example request body for adding static code scans or Clear static code scans

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.StaticCodeScansAPI.AddStaticCodeScansBySystemId(context.Background(), systemId).StaticCodeRequestPostBody(staticCodeRequestPostBody).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `StaticCodeScansAPI.AddStaticCodeScansBySystemId``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `AddStaticCodeScansBySystemId`: StaticCodeResponsePost
	fmt.Fprintf(os.Stdout, "Response from `StaticCodeScansAPI.AddStaticCodeScansBySystemId`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**systemId** | **int32** | **System Id**: The unique system record identifier. | 

### Other Parameters

Other parameters are passed through a pointer to a apiAddStaticCodeScansBySystemIdRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **staticCodeRequestPostBody** | [**StaticCodeRequestPostBody**](StaticCodeRequestPostBody.md) | Example request body for adding static code scans or Clear static code scans | 

### Return type

[**StaticCodeResponsePost**](StaticCodeResponsePost.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

