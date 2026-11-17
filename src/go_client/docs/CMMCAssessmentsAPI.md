# \CMMCAssessmentsAPI

All URIs are relative to *http://localhost:4010*

Method | HTTP request | Description
------------- | ------------- | -------------
[**GetCmmcAssessments**](CMMCAssessmentsAPI.md#GetCmmcAssessments) | **Get** /api/cmmc-assessments | Get CMMC assessment information



## GetCmmcAssessments

> CmmcResponseGet GetCmmcAssessments(ctx).SinceDate(sinceDate).Execute()

Get CMMC assessment information



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
	sinceDate := "1638764040" // string | **Date** CMMC date (Unix date format)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.CMMCAssessmentsAPI.GetCmmcAssessments(context.Background()).SinceDate(sinceDate).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CMMCAssessmentsAPI.GetCmmcAssessments``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetCmmcAssessments`: CmmcResponseGet
	fmt.Fprintf(os.Stdout, "Response from `CMMCAssessmentsAPI.GetCmmcAssessments`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetCmmcAssessmentsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sinceDate** | **string** | **Date** CMMC date (Unix date format) | 

### Return type

[**CmmcResponseGet**](CmmcResponseGet.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

