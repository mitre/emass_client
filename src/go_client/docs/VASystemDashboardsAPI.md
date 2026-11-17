# \VASystemDashboardsAPI

All URIs are relative to *http://localhost:4010*

Method | HTTP request | Description
------------- | ------------- | -------------
[**GetVaSystemA2Summary**](VASystemDashboardsAPI.md#GetVaSystemA2Summary) | **Get** /api/dashboards/va-system-a2-summary | VA System A2.0 Summary
[**GetVaSystemAaSummary**](VASystemDashboardsAPI.md#GetVaSystemAaSummary) | **Get** /api/dashboards/va-system-aa-summary | VA System A&amp;A Summary
[**GetVaSystemFismaInvetoryCryptoSummary**](VASystemDashboardsAPI.md#GetVaSystemFismaInvetoryCryptoSummary) | **Get** /api/dashboards/va-system-fisma-inventory-crypto-summary | VA System FISMA Inventory Crypto Summary
[**GetVaSystemFismaInvetorySummary**](VASystemDashboardsAPI.md#GetVaSystemFismaInvetorySummary) | **Get** /api/dashboards/va-system-fisma-inventory-summary | VA System FISMA Inventory Summary
[**GetVaSystemIcampTableauPoamDetails**](VASystemDashboardsAPI.md#GetVaSystemIcampTableauPoamDetails) | **Get** /api/dashboards/va-system-icamp-tableau-poam-details | VA System ICAMP Tableau POAM Details
[**GetVaSystemPl109ReportingSummary**](VASystemDashboardsAPI.md#GetVaSystemPl109ReportingSummary) | **Get** /api/dashboards/va-system-pl-109-reporting-summary | VA System P.L. 109 Reporting Summary
[**GetVaSystemThreatArchitectureDetails**](VASystemDashboardsAPI.md#GetVaSystemThreatArchitectureDetails) | **Get** /api/dashboards/va-system-threat-architecture-details | VA System Threat Architecture Details
[**GetVaSystemThreatRiskSummary**](VASystemDashboardsAPI.md#GetVaSystemThreatRiskSummary) | **Get** /api/dashboards/va-system-threat-risks-summary | VA System Threat Risks Summary
[**GetVaSystemThreatSourceDetails**](VASystemDashboardsAPI.md#GetVaSystemThreatSourceDetails) | **Get** /api/dashboards/va-system-threat-sources-details | VA System Threat Sources Details



## GetVaSystemA2Summary

> GetSystemStatusDetails200Response GetVaSystemA2Summary(ctx).OrgId(orgId).Excludeinherited(excludeinherited).PageIndex(pageIndex).PageSize(pageSize).Execute()

VA System A2.0 Summary



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
	resp, r, err := apiClient.VASystemDashboardsAPI.GetVaSystemA2Summary(context.Background()).OrgId(orgId).Excludeinherited(excludeinherited).PageIndex(pageIndex).PageSize(pageSize).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `VASystemDashboardsAPI.GetVaSystemA2Summary``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetVaSystemA2Summary`: GetSystemStatusDetails200Response
	fmt.Fprintf(os.Stdout, "Response from `VASystemDashboardsAPI.GetVaSystemA2Summary`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetVaSystemA2SummaryRequest struct via the builder pattern


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


## GetVaSystemAaSummary

> GetSystemStatusDetails200Response GetVaSystemAaSummary(ctx).OrgId(orgId).Excludeinherited(excludeinherited).PageIndex(pageIndex).PageSize(pageSize).Execute()

VA System A&A Summary



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
	resp, r, err := apiClient.VASystemDashboardsAPI.GetVaSystemAaSummary(context.Background()).OrgId(orgId).Excludeinherited(excludeinherited).PageIndex(pageIndex).PageSize(pageSize).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `VASystemDashboardsAPI.GetVaSystemAaSummary``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetVaSystemAaSummary`: GetSystemStatusDetails200Response
	fmt.Fprintf(os.Stdout, "Response from `VASystemDashboardsAPI.GetVaSystemAaSummary`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetVaSystemAaSummaryRequest struct via the builder pattern


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


## GetVaSystemFismaInvetoryCryptoSummary

> GetSystemStatusDetails200Response GetVaSystemFismaInvetoryCryptoSummary(ctx).OrgId(orgId).Excludeinherited(excludeinherited).PageIndex(pageIndex).PageSize(pageSize).Execute()

VA System FISMA Inventory Crypto Summary



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
	resp, r, err := apiClient.VASystemDashboardsAPI.GetVaSystemFismaInvetoryCryptoSummary(context.Background()).OrgId(orgId).Excludeinherited(excludeinherited).PageIndex(pageIndex).PageSize(pageSize).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `VASystemDashboardsAPI.GetVaSystemFismaInvetoryCryptoSummary``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetVaSystemFismaInvetoryCryptoSummary`: GetSystemStatusDetails200Response
	fmt.Fprintf(os.Stdout, "Response from `VASystemDashboardsAPI.GetVaSystemFismaInvetoryCryptoSummary`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetVaSystemFismaInvetoryCryptoSummaryRequest struct via the builder pattern


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


## GetVaSystemFismaInvetorySummary

> GetSystemStatusDetails200Response GetVaSystemFismaInvetorySummary(ctx).OrgId(orgId).Excludeinherited(excludeinherited).PageIndex(pageIndex).PageSize(pageSize).Execute()

VA System FISMA Inventory Summary



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
	resp, r, err := apiClient.VASystemDashboardsAPI.GetVaSystemFismaInvetorySummary(context.Background()).OrgId(orgId).Excludeinherited(excludeinherited).PageIndex(pageIndex).PageSize(pageSize).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `VASystemDashboardsAPI.GetVaSystemFismaInvetorySummary``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetVaSystemFismaInvetorySummary`: GetSystemStatusDetails200Response
	fmt.Fprintf(os.Stdout, "Response from `VASystemDashboardsAPI.GetVaSystemFismaInvetorySummary`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetVaSystemFismaInvetorySummaryRequest struct via the builder pattern


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


## GetVaSystemIcampTableauPoamDetails

> GetSystemStatusDetails200Response GetVaSystemIcampTableauPoamDetails(ctx).OrgId(orgId).Excludeinherited(excludeinherited).PageIndex(pageIndex).PageSize(pageSize).Execute()

VA System ICAMP Tableau POAM Details



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
	resp, r, err := apiClient.VASystemDashboardsAPI.GetVaSystemIcampTableauPoamDetails(context.Background()).OrgId(orgId).Excludeinherited(excludeinherited).PageIndex(pageIndex).PageSize(pageSize).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `VASystemDashboardsAPI.GetVaSystemIcampTableauPoamDetails``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetVaSystemIcampTableauPoamDetails`: GetSystemStatusDetails200Response
	fmt.Fprintf(os.Stdout, "Response from `VASystemDashboardsAPI.GetVaSystemIcampTableauPoamDetails`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetVaSystemIcampTableauPoamDetailsRequest struct via the builder pattern


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


## GetVaSystemPl109ReportingSummary

> GetSystemStatusDetails200Response GetVaSystemPl109ReportingSummary(ctx).OrgId(orgId).Excludeinherited(excludeinherited).PageIndex(pageIndex).PageSize(pageSize).Execute()

VA System P.L. 109 Reporting Summary



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
	resp, r, err := apiClient.VASystemDashboardsAPI.GetVaSystemPl109ReportingSummary(context.Background()).OrgId(orgId).Excludeinherited(excludeinherited).PageIndex(pageIndex).PageSize(pageSize).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `VASystemDashboardsAPI.GetVaSystemPl109ReportingSummary``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetVaSystemPl109ReportingSummary`: GetSystemStatusDetails200Response
	fmt.Fprintf(os.Stdout, "Response from `VASystemDashboardsAPI.GetVaSystemPl109ReportingSummary`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetVaSystemPl109ReportingSummaryRequest struct via the builder pattern


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


## GetVaSystemThreatArchitectureDetails

> GetSystemStatusDetails200Response GetVaSystemThreatArchitectureDetails(ctx).OrgId(orgId).Excludeinherited(excludeinherited).PageIndex(pageIndex).PageSize(pageSize).Execute()

VA System Threat Architecture Details



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
	resp, r, err := apiClient.VASystemDashboardsAPI.GetVaSystemThreatArchitectureDetails(context.Background()).OrgId(orgId).Excludeinherited(excludeinherited).PageIndex(pageIndex).PageSize(pageSize).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `VASystemDashboardsAPI.GetVaSystemThreatArchitectureDetails``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetVaSystemThreatArchitectureDetails`: GetSystemStatusDetails200Response
	fmt.Fprintf(os.Stdout, "Response from `VASystemDashboardsAPI.GetVaSystemThreatArchitectureDetails`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetVaSystemThreatArchitectureDetailsRequest struct via the builder pattern


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


## GetVaSystemThreatRiskSummary

> GetSystemStatusDetails200Response GetVaSystemThreatRiskSummary(ctx).OrgId(orgId).Excludeinherited(excludeinherited).PageIndex(pageIndex).PageSize(pageSize).Execute()

VA System Threat Risks Summary



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
	resp, r, err := apiClient.VASystemDashboardsAPI.GetVaSystemThreatRiskSummary(context.Background()).OrgId(orgId).Excludeinherited(excludeinherited).PageIndex(pageIndex).PageSize(pageSize).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `VASystemDashboardsAPI.GetVaSystemThreatRiskSummary``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetVaSystemThreatRiskSummary`: GetSystemStatusDetails200Response
	fmt.Fprintf(os.Stdout, "Response from `VASystemDashboardsAPI.GetVaSystemThreatRiskSummary`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetVaSystemThreatRiskSummaryRequest struct via the builder pattern


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


## GetVaSystemThreatSourceDetails

> GetSystemStatusDetails200Response GetVaSystemThreatSourceDetails(ctx).OrgId(orgId).Excludeinherited(excludeinherited).PageIndex(pageIndex).PageSize(pageSize).Execute()

VA System Threat Sources Details



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
	resp, r, err := apiClient.VASystemDashboardsAPI.GetVaSystemThreatSourceDetails(context.Background()).OrgId(orgId).Excludeinherited(excludeinherited).PageIndex(pageIndex).PageSize(pageSize).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `VASystemDashboardsAPI.GetVaSystemThreatSourceDetails``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetVaSystemThreatSourceDetails`: GetSystemStatusDetails200Response
	fmt.Fprintf(os.Stdout, "Response from `VASystemDashboardsAPI.GetVaSystemThreatSourceDetails`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetVaSystemThreatSourceDetailsRequest struct via the builder pattern


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

