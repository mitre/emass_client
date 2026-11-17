# \SystemPOAMDashboardsAPI

All URIs are relative to *http://localhost:4010*

Method | HTTP request | Description
------------- | ------------- | -------------
[**GetSystemPoamDetails**](SystemPOAMDashboardsAPI.md#GetSystemPoamDetails) | **Get** /api/dashboards/system-poam-details | System POA&amp;M Details
[**GetSystemPoamSummary**](SystemPOAMDashboardsAPI.md#GetSystemPoamSummary) | **Get** /api/dashboards/system-poam-summary | System POA&amp;M Summary



## GetSystemPoamDetails

> GetSystemStatusDetails200Response GetSystemPoamDetails(ctx).OrgId(orgId).Excludeinherited(excludeinherited).PageIndex(pageIndex).PageSize(pageSize).Execute()

System POA&M Details



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
	orgId := int32(1) // int32 | **Organization Id**: The unique organization identifier.
	excludeinherited := true // bool | **Exclude Inherited**: If no value is specified, the default returns false to include inherited data.  (optional) (default to false)
	pageIndex := int32(56) // int32 | **Page Index**: If no value is specified, the default returns results from the first page with an index of 0.  (optional) (default to 0)
	pageSize := int32(56) // int32 | **Page Size**: If no value is specified, the default returns 20000 per page.  (optional) (default to 20000)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SystemPOAMDashboardsAPI.GetSystemPoamDetails(context.Background()).OrgId(orgId).Excludeinherited(excludeinherited).PageIndex(pageIndex).PageSize(pageSize).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SystemPOAMDashboardsAPI.GetSystemPoamDetails``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetSystemPoamDetails`: GetSystemStatusDetails200Response
	fmt.Fprintf(os.Stdout, "Response from `SystemPOAMDashboardsAPI.GetSystemPoamDetails`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetSystemPoamDetailsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgId** | **int32** | **Organization Id**: The unique organization identifier. | 
 **excludeinherited** | **bool** | **Exclude Inherited**: If no value is specified, the default returns false to include inherited data.  | [default to false]
 **pageIndex** | **int32** | **Page Index**: If no value is specified, the default returns results from the first page with an index of 0.  | [default to 0]
 **pageSize** | **int32** | **Page Size**: If no value is specified, the default returns 20000 per page.  | [default to 20000]

### Return type

[**GetSystemStatusDetails200Response**](GetSystemStatusDetails200Response.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetSystemPoamSummary

> GetSystemStatusDetails200Response GetSystemPoamSummary(ctx).OrgId(orgId).Excludeinherited(excludeinherited).PageIndex(pageIndex).PageSize(pageSize).Execute()

System POA&M Summary



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
	orgId := int32(1) // int32 | **Organization Id**: The unique organization identifier.
	excludeinherited := true // bool | **Exclude Inherited**: If no value is specified, the default returns false to include inherited data.  (optional) (default to false)
	pageIndex := int32(56) // int32 | **Page Index**: If no value is specified, the default returns results from the first page with an index of 0.  (optional) (default to 0)
	pageSize := int32(56) // int32 | **Page Size**: If no value is specified, the default returns 20000 per page.  (optional) (default to 20000)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SystemPOAMDashboardsAPI.GetSystemPoamSummary(context.Background()).OrgId(orgId).Excludeinherited(excludeinherited).PageIndex(pageIndex).PageSize(pageSize).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SystemPOAMDashboardsAPI.GetSystemPoamSummary``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetSystemPoamSummary`: GetSystemStatusDetails200Response
	fmt.Fprintf(os.Stdout, "Response from `SystemPOAMDashboardsAPI.GetSystemPoamSummary`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetSystemPoamSummaryRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgId** | **int32** | **Organization Id**: The unique organization identifier. | 
 **excludeinherited** | **bool** | **Exclude Inherited**: If no value is specified, the default returns false to include inherited data.  | [default to false]
 **pageIndex** | **int32** | **Page Index**: If no value is specified, the default returns results from the first page with an index of 0.  | [default to 0]
 **pageSize** | **int32** | **Page Size**: If no value is specified, the default returns 20000 per page.  | [default to 20000]

### Return type

[**GetSystemStatusDetails200Response**](GetSystemStatusDetails200Response.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

