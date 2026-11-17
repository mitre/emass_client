# \CMMCAssessmentDashboardsAPI

All URIs are relative to *http://localhost:4010*

Method | HTTP request | Description
------------- | ------------- | -------------
[**GetCmmcAssessmentRequirementObjectivesDetails**](CMMCAssessmentDashboardsAPI.md#GetCmmcAssessmentRequirementObjectivesDetails) | **Get** /api/dashboards/cmmc-assessment-requirement-objectives-details | CMMC Assessment Requirement Objectives Details
[**GetCmmcAssessmentRequirementsComplianceSummary**](CMMCAssessmentDashboardsAPI.md#GetCmmcAssessmentRequirementsComplianceSummary) | **Get** /api/dashboards/cmmc-assessment-requirements-compliance-summary | CMMC Assessment Requirements Compliance Summary
[**GetCmmcAssessmentSecurityRequirementsDetails**](CMMCAssessmentDashboardsAPI.md#GetCmmcAssessmentSecurityRequirementsDetails) | **Get** /api/dashboards/cmmc-assessment-security-requirements-details | CMMC Assessment Security Requirements Details
[**GetCmmcAssessmentStatusSummary**](CMMCAssessmentDashboardsAPI.md#GetCmmcAssessmentStatusSummary) | **Get** /api/dashboards/cmmc-assessment-status-summary | CMMC Assessment Status Summary



## GetCmmcAssessmentRequirementObjectivesDetails

> GetSystemStatusDetails200Response GetCmmcAssessmentRequirementObjectivesDetails(ctx).OrgId(orgId).Excludeinherited(excludeinherited).PageIndex(pageIndex).PageSize(pageSize).Execute()

CMMC Assessment Requirement Objectives Details



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
	resp, r, err := apiClient.CMMCAssessmentDashboardsAPI.GetCmmcAssessmentRequirementObjectivesDetails(context.Background()).OrgId(orgId).Excludeinherited(excludeinherited).PageIndex(pageIndex).PageSize(pageSize).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CMMCAssessmentDashboardsAPI.GetCmmcAssessmentRequirementObjectivesDetails``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetCmmcAssessmentRequirementObjectivesDetails`: GetSystemStatusDetails200Response
	fmt.Fprintf(os.Stdout, "Response from `CMMCAssessmentDashboardsAPI.GetCmmcAssessmentRequirementObjectivesDetails`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetCmmcAssessmentRequirementObjectivesDetailsRequest struct via the builder pattern


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


## GetCmmcAssessmentRequirementsComplianceSummary

> GetSystemStatusDetails200Response GetCmmcAssessmentRequirementsComplianceSummary(ctx).OrgId(orgId).Excludeinherited(excludeinherited).PageIndex(pageIndex).PageSize(pageSize).Execute()

CMMC Assessment Requirements Compliance Summary



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
	resp, r, err := apiClient.CMMCAssessmentDashboardsAPI.GetCmmcAssessmentRequirementsComplianceSummary(context.Background()).OrgId(orgId).Excludeinherited(excludeinherited).PageIndex(pageIndex).PageSize(pageSize).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CMMCAssessmentDashboardsAPI.GetCmmcAssessmentRequirementsComplianceSummary``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetCmmcAssessmentRequirementsComplianceSummary`: GetSystemStatusDetails200Response
	fmt.Fprintf(os.Stdout, "Response from `CMMCAssessmentDashboardsAPI.GetCmmcAssessmentRequirementsComplianceSummary`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetCmmcAssessmentRequirementsComplianceSummaryRequest struct via the builder pattern


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


## GetCmmcAssessmentSecurityRequirementsDetails

> GetSystemStatusDetails200Response GetCmmcAssessmentSecurityRequirementsDetails(ctx).OrgId(orgId).Excludeinherited(excludeinherited).PageIndex(pageIndex).PageSize(pageSize).Execute()

CMMC Assessment Security Requirements Details



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
	resp, r, err := apiClient.CMMCAssessmentDashboardsAPI.GetCmmcAssessmentSecurityRequirementsDetails(context.Background()).OrgId(orgId).Excludeinherited(excludeinherited).PageIndex(pageIndex).PageSize(pageSize).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CMMCAssessmentDashboardsAPI.GetCmmcAssessmentSecurityRequirementsDetails``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetCmmcAssessmentSecurityRequirementsDetails`: GetSystemStatusDetails200Response
	fmt.Fprintf(os.Stdout, "Response from `CMMCAssessmentDashboardsAPI.GetCmmcAssessmentSecurityRequirementsDetails`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetCmmcAssessmentSecurityRequirementsDetailsRequest struct via the builder pattern


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


## GetCmmcAssessmentStatusSummary

> GetSystemStatusDetails200Response GetCmmcAssessmentStatusSummary(ctx).OrgId(orgId).Excludeinherited(excludeinherited).PageIndex(pageIndex).PageSize(pageSize).Execute()

CMMC Assessment Status Summary



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
	resp, r, err := apiClient.CMMCAssessmentDashboardsAPI.GetCmmcAssessmentStatusSummary(context.Background()).OrgId(orgId).Excludeinherited(excludeinherited).PageIndex(pageIndex).PageSize(pageSize).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CMMCAssessmentDashboardsAPI.GetCmmcAssessmentStatusSummary``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetCmmcAssessmentStatusSummary`: GetSystemStatusDetails200Response
	fmt.Fprintf(os.Stdout, "Response from `CMMCAssessmentDashboardsAPI.GetCmmcAssessmentStatusSummary`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetCmmcAssessmentStatusSummaryRequest struct via the builder pattern


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

