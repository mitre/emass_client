# \TestResultsAPI

All URIs are relative to *http://localhost:4010*

Method | HTTP request | Description
------------- | ------------- | -------------
[**AddTestResultsBySystemId**](TestResultsAPI.md#AddTestResultsBySystemId) | **Post** /api/systems/{systemId}/test-results | Add one or many test results in a system
[**GetSystemTestResults**](TestResultsAPI.md#GetSystemTestResults) | **Get** /api/systems/{systemId}/test-results | Get one or many test results in a system



## AddTestResultsBySystemId

> TestResultsResponsePost AddTestResultsBySystemId(ctx, systemId).RequestBody(requestBody).Execute()

Add one or many test results in a system



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
	requestBody := []interface{}{interface{}(123)} // []interface{} | Example request body to add test results to a system (systemId)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.TestResultsAPI.AddTestResultsBySystemId(context.Background(), systemId).RequestBody(requestBody).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TestResultsAPI.AddTestResultsBySystemId``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `AddTestResultsBySystemId`: TestResultsResponsePost
	fmt.Fprintf(os.Stdout, "Response from `TestResultsAPI.AddTestResultsBySystemId`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**systemId** | **int32** | **System Id**: The unique system record identifier. | 

### Other Parameters

Other parameters are passed through a pointer to a apiAddTestResultsBySystemIdRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **requestBody** | **[]interface{}** | Example request body to add test results to a system (systemId) | 

### Return type

[**TestResultsResponsePost**](TestResultsResponsePost.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetSystemTestResults

> TestResultsResponseGet GetSystemTestResults(ctx, systemId).ControlAcronyms(controlAcronyms).AssessmentProcedures(assessmentProcedures).Ccis(ccis).LatestOnly(latestOnly).Execute()

Get one or many test results in a system



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
	controlAcronyms := "controlAcronyms_example" // string | **Control Acronym**: Filter query by given system acronym (single value or comma separated). (optional)
	assessmentProcedures := "assessmentProcedures_example" // string | **Assessment Procedure**: Filter query by given Security Control Assessment Procedure (single value or comma separated). (optional)
	ccis := "ccis_example" // string | **CCI System**: Filter query by Control Correlation Identifiers (CCIs) (single value or comma separated). (optional)
	latestOnly := true // bool | **Latest Results Only**: Indicates that only the latest test resultes are retrieved. (optional) (default to true)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.TestResultsAPI.GetSystemTestResults(context.Background(), systemId).ControlAcronyms(controlAcronyms).AssessmentProcedures(assessmentProcedures).Ccis(ccis).LatestOnly(latestOnly).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TestResultsAPI.GetSystemTestResults``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetSystemTestResults`: TestResultsResponseGet
	fmt.Fprintf(os.Stdout, "Response from `TestResultsAPI.GetSystemTestResults`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**systemId** | **int32** | **System Id**: The unique system record identifier. | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetSystemTestResultsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **controlAcronyms** | **string** | **Control Acronym**: Filter query by given system acronym (single value or comma separated). | 
 **assessmentProcedures** | **string** | **Assessment Procedure**: Filter query by given Security Control Assessment Procedure (single value or comma separated). | 
 **ccis** | **string** | **CCI System**: Filter query by Control Correlation Identifiers (CCIs) (single value or comma separated). | 
 **latestOnly** | **bool** | **Latest Results Only**: Indicates that only the latest test resultes are retrieved. | [default to true]

### Return type

[**TestResultsResponseGet**](TestResultsResponseGet.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

