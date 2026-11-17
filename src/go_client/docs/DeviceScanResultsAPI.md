# \DeviceScanResultsAPI

All URIs are relative to *http://localhost:4010*

Method | HTTP request | Description
------------- | ------------- | -------------
[**AddScanResultsBySystemId**](DeviceScanResultsAPI.md#AddScanResultsBySystemId) | **Post** /api/systems/{systemId}/device-scan-results | Add device scans in a system



## AddScanResultsBySystemId

> DeviceScanResultsResponsePost AddScanResultsBySystemId(ctx, systemId).ScanType(scanType).Filename(filename).IsBaseline(isBaseline).Execute()

Add device scans in a system



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
	scanType := "scanType_example" // string | **Scan Type**: The file scan type to upload (default to "disaStigViewerCklCklb")
	filename := os.NewFile(1234, "some_file") // *os.File | The file to upload. Can be a single file or a .zip file.
	isBaseline := true // bool | **Is Baseline**: Indicates that the imported file represents a baseline scan that includes all findings and results. Importing as a baseline scan, which assumes a common set of scan policies are used when conducting a scan, will replace a device's findings for a specific Benchmark. Applicable to ASR/ARF scans only.  (optional) (default to false)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DeviceScanResultsAPI.AddScanResultsBySystemId(context.Background(), systemId).ScanType(scanType).Filename(filename).IsBaseline(isBaseline).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DeviceScanResultsAPI.AddScanResultsBySystemId``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `AddScanResultsBySystemId`: DeviceScanResultsResponsePost
	fmt.Fprintf(os.Stdout, "Response from `DeviceScanResultsAPI.AddScanResultsBySystemId`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**systemId** | **int32** | **System Id**: The unique system record identifier. | 

### Other Parameters

Other parameters are passed through a pointer to a apiAddScanResultsBySystemIdRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **scanType** | **string** | **Scan Type**: The file scan type to upload | [default to &quot;disaStigViewerCklCklb&quot;]
 **filename** | ***os.File** | The file to upload. Can be a single file or a .zip file. | 
 **isBaseline** | **bool** | **Is Baseline**: Indicates that the imported file represents a baseline scan that includes all findings and results. Importing as a baseline scan, which assumes a common set of scan policies are used when conducting a scan, will replace a device&#39;s findings for a specific Benchmark. Applicable to ASR/ARF scans only.  | [default to false]

### Return type

[**DeviceScanResultsResponsePost**](DeviceScanResultsResponsePost.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

