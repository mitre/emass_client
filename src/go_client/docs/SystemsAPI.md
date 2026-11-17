# \SystemsAPI

All URIs are relative to *http://localhost:4010*

Method | HTTP request | Description
------------- | ------------- | -------------
[**GetSystem**](SystemsAPI.md#GetSystem) | **Get** /api/systems/{systemId} | Get system information for a specific system
[**GetSystems**](SystemsAPI.md#GetSystems) | **Get** /api/systems | Get system information



## GetSystem

> SystemResponse GetSystem(ctx, systemId).Policy(policy).Execute()

Get system information for a specific system



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
	policy := "policy_example" // string | **System Policy**: Filter query by system policy. If no value is specified, the default returns RMF policy information for dual-policy systems. (optional) (default to "rmf")

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SystemsAPI.GetSystem(context.Background(), systemId).Policy(policy).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SystemsAPI.GetSystem``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetSystem`: SystemResponse
	fmt.Fprintf(os.Stdout, "Response from `SystemsAPI.GetSystem`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**systemId** | **int32** | **System Id**: The unique system record identifier. | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetSystemRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **policy** | **string** | **System Policy**: Filter query by system policy. If no value is specified, the default returns RMF policy information for dual-policy systems. | [default to &quot;rmf&quot;]

### Return type

[**SystemResponse**](SystemResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetSystems

> SystemsResponse GetSystems(ctx).CoamsId(coamsId).DitprId(ditprId).IncludeDecommissioned(includeDecommissioned).IncludeDitprMetrics(includeDitprMetrics).Policy(policy).RegistrationType(registrationType).ReportsForScorecard(reportsForScorecard).Execute()

Get system information



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
	coamsId := "coamsId_example" // string | **COAMS ID**: Filter query by Cyber Operational Attributes Management System (COAMS). (optional)
	ditprId := "ditprId_example" // string | **DITPR ID**: Filter query by DoD Information Technology (IT) Portfolio Repository (DITPR). (optional)
	includeDecommissioned := true // bool | **Include Decommissioned Systems**: Indicates if decommissioned systems are retrieved. If no value is specified, the default returns true to include decommissioned systems. (optional) (default to true)
	includeDitprMetrics := true // bool | **Include DITPR**: Indicates if DITPR metrics are retrieved. This query string parameter cannot be used in conjunction with the following parameters:   - ditprId   - coamsId  If no value is specified, the default returns false to not include DITPR Metrics. (optional) (default to false)
	policy := "policy_example" // string | **System Policy**: Filter query by system policy. If no value is specified, the default returns RMF policy information for dual-policy systems. (optional) (default to "rmf")
	registrationType := "registrationType_example" // string | **Registration Type**: Filter record by selected registration type (single value or comma delimited values).  **Valid Options Are:** assessAndAuthorize, assessOnly, guest, regular, functional, cloudServiceProvider, commonControlProvider, authorizationToUse, reciprocityAcceptanc  (optional) (default to "regular")
	reportsForScorecard := true // bool | **DoD Cyber Hygiene Scorecard**: Used to filter results to only return systems that report to the DoD Cyber Hygiene Scorecard. (optional) (default to true)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SystemsAPI.GetSystems(context.Background()).CoamsId(coamsId).DitprId(ditprId).IncludeDecommissioned(includeDecommissioned).IncludeDitprMetrics(includeDitprMetrics).Policy(policy).RegistrationType(registrationType).ReportsForScorecard(reportsForScorecard).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SystemsAPI.GetSystems``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetSystems`: SystemsResponse
	fmt.Fprintf(os.Stdout, "Response from `SystemsAPI.GetSystems`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetSystemsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coamsId** | **string** | **COAMS ID**: Filter query by Cyber Operational Attributes Management System (COAMS). | 
 **ditprId** | **string** | **DITPR ID**: Filter query by DoD Information Technology (IT) Portfolio Repository (DITPR). | 
 **includeDecommissioned** | **bool** | **Include Decommissioned Systems**: Indicates if decommissioned systems are retrieved. If no value is specified, the default returns true to include decommissioned systems. | [default to true]
 **includeDitprMetrics** | **bool** | **Include DITPR**: Indicates if DITPR metrics are retrieved. This query string parameter cannot be used in conjunction with the following parameters:   - ditprId   - coamsId  If no value is specified, the default returns false to not include DITPR Metrics. | [default to false]
 **policy** | **string** | **System Policy**: Filter query by system policy. If no value is specified, the default returns RMF policy information for dual-policy systems. | [default to &quot;rmf&quot;]
 **registrationType** | **string** | **Registration Type**: Filter record by selected registration type (single value or comma delimited values).  **Valid Options Are:** assessAndAuthorize, assessOnly, guest, regular, functional, cloudServiceProvider, commonControlProvider, authorizationToUse, reciprocityAcceptanc  | [default to &quot;regular&quot;]
 **reportsForScorecard** | **bool** | **DoD Cyber Hygiene Scorecard**: Used to filter results to only return systems that report to the DoD Cyber Hygiene Scorecard. | [default to true]

### Return type

[**SystemsResponse**](SystemsResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

