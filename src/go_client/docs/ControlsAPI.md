# \ControlsAPI

All URIs are relative to *http://localhost:4010*

Method | HTTP request | Description
------------- | ------------- | -------------
[**GetSystemControls**](ControlsAPI.md#GetSystemControls) | **Get** /api/systems/{systemId}/controls | Get control information in a system for one or many controls
[**UpdateControlBySystemId**](ControlsAPI.md#UpdateControlBySystemId) | **Put** /api/systems/{systemId}/controls | Update control information in a system for one or many controls



## GetSystemControls

> ControlsResponseGet GetSystemControls(ctx, systemId).Acronyms(acronyms).Execute()

Get control information in a system for one or many controls



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
	acronyms := "acronyms_example" // string | **Acronym**: The system acronym(s) being queried (single value or comma delimited values). (optional) (default to "PM-6")

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ControlsAPI.GetSystemControls(context.Background(), systemId).Acronyms(acronyms).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ControlsAPI.GetSystemControls``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetSystemControls`: ControlsResponseGet
	fmt.Fprintf(os.Stdout, "Response from `ControlsAPI.GetSystemControls`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**systemId** | **int32** | **System Id**: The unique system record identifier. | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetSystemControlsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **acronyms** | **string** | **Acronym**: The system acronym(s) being queried (single value or comma delimited values). | [default to &quot;PM-6&quot;]

### Return type

[**ControlsResponseGet**](ControlsResponseGet.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UpdateControlBySystemId

> ControlsResponsePut UpdateControlBySystemId(ctx, systemId).ControlsRequiredFields(controlsRequiredFields).Execute()

Update control information in a system for one or many controls



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
	controlsRequiredFields := []openapiclient.ControlsRequiredFields{*openapiclient.NewControlsRequiredFields()} // []ControlsRequiredFields | Example request body for updating an existing control for a given system.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ControlsAPI.UpdateControlBySystemId(context.Background(), systemId).ControlsRequiredFields(controlsRequiredFields).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ControlsAPI.UpdateControlBySystemId``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UpdateControlBySystemId`: ControlsResponsePut
	fmt.Fprintf(os.Stdout, "Response from `ControlsAPI.UpdateControlBySystemId`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**systemId** | **int32** | **System Id**: The unique system record identifier. | 

### Other Parameters

Other parameters are passed through a pointer to a apiUpdateControlBySystemIdRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **controlsRequiredFields** | [**[]ControlsRequiredFields**](ControlsRequiredFields.md) | Example request body for updating an existing control for a given system. | 

### Return type

[**ControlsResponsePut**](ControlsResponsePut.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

