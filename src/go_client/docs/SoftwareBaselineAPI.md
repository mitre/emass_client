# \SoftwareBaselineAPI

All URIs are relative to *http://localhost:4010*

Method | HTTP request | Description
------------- | ------------- | -------------
[**AddSwBaselineAssets**](SoftwareBaselineAPI.md#AddSwBaselineAssets) | **Post** /api/systems/{systemId}/sw-baseline | Add one or many software assets in a system
[**DeleteSwBaselineAssets**](SoftwareBaselineAPI.md#DeleteSwBaselineAssets) | **Delete** /api/systems/{systemId}/sw-baseline | Delete one or many software assets in a system
[**GetSystemSwBaseline**](SoftwareBaselineAPI.md#GetSystemSwBaseline) | **Get** /api/systems/{systemId}/sw-baseline | Get software baseline for a system
[**UpdateSwBaselineAssets**](SoftwareBaselineAPI.md#UpdateSwBaselineAssets) | **Put** /api/systems/{systemId}/sw-baseline | Update one or many software assets in a system



## AddSwBaselineAssets

> SwBaselineResponsePostPut AddSwBaselineAssets(ctx, systemId).SwBaselineRequiredFields(swBaselineRequiredFields).Execute()

Add one or many software assets in a system



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
	swBaselineRequiredFields := []openapiclient.SwBaselineRequiredFields{*openapiclient.NewSwBaselineRequiredFields()} // []SwBaselineRequiredFields | Example request body for adding software baseline assets to an existing System (systemId)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SoftwareBaselineAPI.AddSwBaselineAssets(context.Background(), systemId).SwBaselineRequiredFields(swBaselineRequiredFields).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SoftwareBaselineAPI.AddSwBaselineAssets``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `AddSwBaselineAssets`: SwBaselineResponsePostPut
	fmt.Fprintf(os.Stdout, "Response from `SoftwareBaselineAPI.AddSwBaselineAssets`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**systemId** | **int32** | **System Id**: The unique system record identifier. | 

### Other Parameters

Other parameters are passed through a pointer to a apiAddSwBaselineAssetsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **swBaselineRequiredFields** | [**[]SwBaselineRequiredFields**](SwBaselineRequiredFields.md) | Example request body for adding software baseline assets to an existing System (systemId) | 

### Return type

[**SwBaselineResponsePostPut**](SwBaselineResponsePostPut.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeleteSwBaselineAssets

> SwBaselineResponseDelete DeleteSwBaselineAssets(ctx, systemId).SwBaselineRequestDeleteBodyInner(swBaselineRequestDeleteBodyInner).Execute()

Delete one or many software assets in a system



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
	swBaselineRequestDeleteBodyInner := []openapiclient.SwBaselineRequestDeleteBodyInner{*openapiclient.NewSwBaselineRequestDeleteBodyInner()} // []SwBaselineRequestDeleteBodyInner | Example request body for deleting one or many Software Baseline assets

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SoftwareBaselineAPI.DeleteSwBaselineAssets(context.Background(), systemId).SwBaselineRequestDeleteBodyInner(swBaselineRequestDeleteBodyInner).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SoftwareBaselineAPI.DeleteSwBaselineAssets``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `DeleteSwBaselineAssets`: SwBaselineResponseDelete
	fmt.Fprintf(os.Stdout, "Response from `SoftwareBaselineAPI.DeleteSwBaselineAssets`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**systemId** | **int32** | **System Id**: The unique system record identifier. | 

### Other Parameters

Other parameters are passed through a pointer to a apiDeleteSwBaselineAssetsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **swBaselineRequestDeleteBodyInner** | [**[]SwBaselineRequestDeleteBodyInner**](SwBaselineRequestDeleteBodyInner.md) | Example request body for deleting one or many Software Baseline assets | 

### Return type

[**SwBaselineResponseDelete**](SwBaselineResponseDelete.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetSystemSwBaseline

> SwBaselineResponseGet GetSystemSwBaseline(ctx, systemId).PageIndex(pageIndex).PageSize(pageSize).Execute()

Get software baseline for a system



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
	resp, r, err := apiClient.SoftwareBaselineAPI.GetSystemSwBaseline(context.Background(), systemId).PageIndex(pageIndex).PageSize(pageSize).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SoftwareBaselineAPI.GetSystemSwBaseline``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetSystemSwBaseline`: SwBaselineResponseGet
	fmt.Fprintf(os.Stdout, "Response from `SoftwareBaselineAPI.GetSystemSwBaseline`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**systemId** | **int32** | **System Id**: The unique system record identifier. | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetSystemSwBaselineRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **pageIndex** | **int32** | **Page Index**: If no value is specified, the default returns results from the first page with an index of 0.  | [default to 0]
 **pageSize** | **int32** | **Page Size**: If no value is specified, the default returns 20000 per page.  | [default to 20000]

### Return type

[**SwBaselineResponseGet**](SwBaselineResponseGet.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UpdateSwBaselineAssets

> SwBaselineResponsePostPut UpdateSwBaselineAssets(ctx, systemId).SwBaselineReadOnlyFields(swBaselineReadOnlyFields).Execute()

Update one or many software assets in a system



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
	swBaselineReadOnlyFields := []openapiclient.SwBaselineReadOnlyFields{*openapiclient.NewSwBaselineReadOnlyFields()} // []SwBaselineReadOnlyFields | Example request body for updating software baseline assets to an existing System (systemId)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SoftwareBaselineAPI.UpdateSwBaselineAssets(context.Background(), systemId).SwBaselineReadOnlyFields(swBaselineReadOnlyFields).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SoftwareBaselineAPI.UpdateSwBaselineAssets``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UpdateSwBaselineAssets`: SwBaselineResponsePostPut
	fmt.Fprintf(os.Stdout, "Response from `SoftwareBaselineAPI.UpdateSwBaselineAssets`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**systemId** | **int32** | **System Id**: The unique system record identifier. | 

### Other Parameters

Other parameters are passed through a pointer to a apiUpdateSwBaselineAssetsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **swBaselineReadOnlyFields** | [**[]SwBaselineReadOnlyFields**](SwBaselineReadOnlyFields.md) | Example request body for updating software baseline assets to an existing System (systemId) | 

### Return type

[**SwBaselineResponsePostPut**](SwBaselineResponsePostPut.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

