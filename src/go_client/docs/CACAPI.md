# \CACAPI

All URIs are relative to *http://localhost:4010*

Method | HTTP request | Description
------------- | ------------- | -------------
[**AddSystemCac**](CACAPI.md#AddSystemCac) | **Post** /api/systems/{systemId}/approval/cac | Submit control to second role of CAC
[**GetSystemCac**](CACAPI.md#GetSystemCac) | **Get** /api/systems/{systemId}/approval/cac | Get location of one or many controls in CAC



## AddSystemCac

> CacResponsePost AddSystemCac(ctx, systemId).RequestBody(requestBody).Execute()

Submit control to second role of CAC



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
	requestBody := []interface{}{interface{}(123)} // []interface{} | Example request body for adding control(s) to second role of CAC

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.CACAPI.AddSystemCac(context.Background(), systemId).RequestBody(requestBody).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CACAPI.AddSystemCac``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `AddSystemCac`: CacResponsePost
	fmt.Fprintf(os.Stdout, "Response from `CACAPI.AddSystemCac`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**systemId** | **int32** | **System Id**: The unique system record identifier. | 

### Other Parameters

Other parameters are passed through a pointer to a apiAddSystemCacRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **requestBody** | **[]interface{}** | Example request body for adding control(s) to second role of CAC | 

### Return type

[**CacResponsePost**](CacResponsePost.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetSystemCac

> CacResponseGet GetSystemCac(ctx, systemId).ControlAcronyms(controlAcronyms).Execute()

Get location of one or many controls in CAC



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

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.CACAPI.GetSystemCac(context.Background(), systemId).ControlAcronyms(controlAcronyms).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CACAPI.GetSystemCac``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetSystemCac`: CacResponseGet
	fmt.Fprintf(os.Stdout, "Response from `CACAPI.GetSystemCac`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**systemId** | **int32** | **System Id**: The unique system record identifier. | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetSystemCacRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **controlAcronyms** | **string** | **Control Acronym**: Filter query by given system acronym (single value or comma separated). | 

### Return type

[**CacResponseGet**](CacResponseGet.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

