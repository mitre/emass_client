# \SystemSecurityControlsDashboardsAPI

All URIs are relative to *http://localhost:4010*

Method | HTTP request | Description
------------- | ------------- | -------------
[**GetSystemAssessmentProceduresDetails**](SystemSecurityControlsDashboardsAPI.md#GetSystemAssessmentProceduresDetails) | **Get** /api/dashboards/system-assessment-procedures-details | System Assessment Procedures Details
[**GetSystemControlComplianceSummary**](SystemSecurityControlsDashboardsAPI.md#GetSystemControlComplianceSummary) | **Get** /api/dashboards/system-control-compliance-summary | System Control Compliance Summary
[**GetSystemSecurityControlDetails**](SystemSecurityControlsDashboardsAPI.md#GetSystemSecurityControlDetails) | **Get** /api/dashboards/system-security-controls-details | System Control Compliance Details



## GetSystemAssessmentProceduresDetails

> GetSystemStatusDetails200Response GetSystemAssessmentProceduresDetails(ctx).OrgId(orgId).Excludeinherited(excludeinherited).PageIndex(pageIndex).PageSize(pageSize).Execute()

System Assessment Procedures Details



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
	resp, r, err := apiClient.SystemSecurityControlsDashboardsAPI.GetSystemAssessmentProceduresDetails(context.Background()).OrgId(orgId).Excludeinherited(excludeinherited).PageIndex(pageIndex).PageSize(pageSize).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SystemSecurityControlsDashboardsAPI.GetSystemAssessmentProceduresDetails``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetSystemAssessmentProceduresDetails`: GetSystemStatusDetails200Response
	fmt.Fprintf(os.Stdout, "Response from `SystemSecurityControlsDashboardsAPI.GetSystemAssessmentProceduresDetails`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetSystemAssessmentProceduresDetailsRequest struct via the builder pattern


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


## GetSystemControlComplianceSummary

> GetSystemStatusDetails200Response GetSystemControlComplianceSummary(ctx).OrgId(orgId).Excludeinherited(excludeinherited).PageIndex(pageIndex).PageSize(pageSize).Execute()

System Control Compliance Summary



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
	resp, r, err := apiClient.SystemSecurityControlsDashboardsAPI.GetSystemControlComplianceSummary(context.Background()).OrgId(orgId).Excludeinherited(excludeinherited).PageIndex(pageIndex).PageSize(pageSize).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SystemSecurityControlsDashboardsAPI.GetSystemControlComplianceSummary``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetSystemControlComplianceSummary`: GetSystemStatusDetails200Response
	fmt.Fprintf(os.Stdout, "Response from `SystemSecurityControlsDashboardsAPI.GetSystemControlComplianceSummary`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetSystemControlComplianceSummaryRequest struct via the builder pattern


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


## GetSystemSecurityControlDetails

> GetSystemStatusDetails200Response GetSystemSecurityControlDetails(ctx).OrgId(orgId).Excludeinherited(excludeinherited).PageIndex(pageIndex).PageSize(pageSize).Execute()

System Control Compliance Details



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
	resp, r, err := apiClient.SystemSecurityControlsDashboardsAPI.GetSystemSecurityControlDetails(context.Background()).OrgId(orgId).Excludeinherited(excludeinherited).PageIndex(pageIndex).PageSize(pageSize).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SystemSecurityControlsDashboardsAPI.GetSystemSecurityControlDetails``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetSystemSecurityControlDetails`: GetSystemStatusDetails200Response
	fmt.Fprintf(os.Stdout, "Response from `SystemSecurityControlsDashboardsAPI.GetSystemSecurityControlDetails`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetSystemSecurityControlDetailsRequest struct via the builder pattern


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

