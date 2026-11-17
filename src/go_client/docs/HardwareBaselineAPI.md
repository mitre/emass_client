# \HardwareBaselineAPI

All URIs are relative to *http://localhost:4010*

Method | HTTP request | Description
------------- | ------------- | -------------
[**AddHwBaselineAssets**](HardwareBaselineAPI.md#AddHwBaselineAssets) | **Post** /api/systems/{systemId}/hw-baseline | Add one or many hardware assets in a system
[**DeleteHwBaselineAssets**](HardwareBaselineAPI.md#DeleteHwBaselineAssets) | **Delete** /api/systems/{systemId}/hw-baseline | Delete one or many hardware assets in a system
[**GetSystemHwBaseline**](HardwareBaselineAPI.md#GetSystemHwBaseline) | **Get** /api/systems/{systemId}/hw-baseline | Get hardware baseline for a system
[**UpdateHwBaselineAssets**](HardwareBaselineAPI.md#UpdateHwBaselineAssets) | **Put** /api/systems/{systemId}/hw-baseline | Update one or many hardware assets in a system



## AddHwBaselineAssets

> HwBaselineResponsePostPut AddHwBaselineAssets(ctx, systemId).HwBaselineRequiredFields(hwBaselineRequiredFields).Execute()

Add one or many hardware assets in a system



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
	hwBaselineRequiredFields := []openapiclient.HwBaselineRequiredFields{*openapiclient.NewHwBaselineRequiredFields()} // []HwBaselineRequiredFields | Example request body for adding hardware baseline assets to an existing System (systemId)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.HardwareBaselineAPI.AddHwBaselineAssets(context.Background(), systemId).HwBaselineRequiredFields(hwBaselineRequiredFields).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `HardwareBaselineAPI.AddHwBaselineAssets``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `AddHwBaselineAssets`: HwBaselineResponsePostPut
	fmt.Fprintf(os.Stdout, "Response from `HardwareBaselineAPI.AddHwBaselineAssets`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**systemId** | **int32** | **System Id**: The unique system record identifier. | 

### Other Parameters

Other parameters are passed through a pointer to a apiAddHwBaselineAssetsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **hwBaselineRequiredFields** | [**[]HwBaselineRequiredFields**](HwBaselineRequiredFields.md) | Example request body for adding hardware baseline assets to an existing System (systemId) | 

### Return type

[**HwBaselineResponsePostPut**](HwBaselineResponsePostPut.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeleteHwBaselineAssets

> HwBaselineResponseDelete DeleteHwBaselineAssets(ctx, systemId).HwBaselineRequestDeleteBodyInner(hwBaselineRequestDeleteBodyInner).Execute()

Delete one or many hardware assets in a system



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
	hwBaselineRequestDeleteBodyInner := []openapiclient.HwBaselineRequestDeleteBodyInner{*openapiclient.NewHwBaselineRequestDeleteBodyInner()} // []HwBaselineRequestDeleteBodyInner | Example request body for deleting one or many Hardware Baseline assets

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.HardwareBaselineAPI.DeleteHwBaselineAssets(context.Background(), systemId).HwBaselineRequestDeleteBodyInner(hwBaselineRequestDeleteBodyInner).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `HardwareBaselineAPI.DeleteHwBaselineAssets``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `DeleteHwBaselineAssets`: HwBaselineResponseDelete
	fmt.Fprintf(os.Stdout, "Response from `HardwareBaselineAPI.DeleteHwBaselineAssets`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**systemId** | **int32** | **System Id**: The unique system record identifier. | 

### Other Parameters

Other parameters are passed through a pointer to a apiDeleteHwBaselineAssetsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **hwBaselineRequestDeleteBodyInner** | [**[]HwBaselineRequestDeleteBodyInner**](HwBaselineRequestDeleteBodyInner.md) | Example request body for deleting one or many Hardware Baseline assets | 

### Return type

[**HwBaselineResponseDelete**](HwBaselineResponseDelete.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetSystemHwBaseline

> HwBaselineResponseGet GetSystemHwBaseline(ctx, systemId).PageIndex(pageIndex).PageSize(pageSize).Execute()

Get hardware baseline for a system



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
	pageIndex := int32(56) // int32 | **Page Index**: If no value is specified, the default returns results from the first page with an index of 0.  (optional) (default to 0)
	pageSize := int32(56) // int32 | **Page Size**: If no value is specified, the default returns 20000 per page.  (optional) (default to 20000)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.HardwareBaselineAPI.GetSystemHwBaseline(context.Background(), systemId).PageIndex(pageIndex).PageSize(pageSize).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `HardwareBaselineAPI.GetSystemHwBaseline``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetSystemHwBaseline`: HwBaselineResponseGet
	fmt.Fprintf(os.Stdout, "Response from `HardwareBaselineAPI.GetSystemHwBaseline`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**systemId** | **int32** | **System Id**: The unique system record identifier. | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetSystemHwBaselineRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **pageIndex** | **int32** | **Page Index**: If no value is specified, the default returns results from the first page with an index of 0.  | [default to 0]
 **pageSize** | **int32** | **Page Size**: If no value is specified, the default returns 20000 per page.  | [default to 20000]

### Return type

[**HwBaselineResponseGet**](HwBaselineResponseGet.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UpdateHwBaselineAssets

> HwBaselineResponsePostPut UpdateHwBaselineAssets(ctx, systemId).HwBaselineReadOnlyFields(hwBaselineReadOnlyFields).Execute()

Update one or many hardware assets in a system



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
	hwBaselineReadOnlyFields := []openapiclient.HwBaselineReadOnlyFields{*openapiclient.NewHwBaselineReadOnlyFields()} // []HwBaselineReadOnlyFields | Example request body for updating hardware baseline assets to an existing System (systemId)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.HardwareBaselineAPI.UpdateHwBaselineAssets(context.Background(), systemId).HwBaselineReadOnlyFields(hwBaselineReadOnlyFields).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `HardwareBaselineAPI.UpdateHwBaselineAssets``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UpdateHwBaselineAssets`: HwBaselineResponsePostPut
	fmt.Fprintf(os.Stdout, "Response from `HardwareBaselineAPI.UpdateHwBaselineAssets`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**systemId** | **int32** | **System Id**: The unique system record identifier. | 

### Other Parameters

Other parameters are passed through a pointer to a apiUpdateHwBaselineAssetsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **hwBaselineReadOnlyFields** | [**[]HwBaselineReadOnlyFields**](HwBaselineReadOnlyFields.md) | Example request body for updating hardware baseline assets to an existing System (systemId) | 

### Return type

[**HwBaselineResponsePostPut**](HwBaselineResponsePostPut.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

