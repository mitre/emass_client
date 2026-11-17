# \POAMAPI

All URIs are relative to *http://localhost:4010*

Method | HTTP request | Description
------------- | ------------- | -------------
[**AddPoamBySystemId**](POAMAPI.md#AddPoamBySystemId) | **Post** /api/systems/{systemId}/poams | Add one or many POA&amp;M items in a system
[**DeletePoam**](POAMAPI.md#DeletePoam) | **Delete** /api/systems/{systemId}/poams | Remove one or many POA&amp;M items in a system
[**GetSystemPoams**](POAMAPI.md#GetSystemPoams) | **Get** /api/systems/{systemId}/poams | Get one or many POA&amp;M items in a system
[**GetSystemPoamsByPoamId**](POAMAPI.md#GetSystemPoamsByPoamId) | **Get** /api/systems/{systemId}/poams/{poamId} | Get POA&amp;M item by ID in a system
[**UpdatePoamBySystemId**](POAMAPI.md#UpdatePoamBySystemId) | **Put** /api/systems/{systemId}/poams | Update one or many POA&amp;M items in a system



## AddPoamBySystemId

> PoamResponsePostPutDelete AddPoamBySystemId(ctx, systemId).PoamRequiredFields(poamRequiredFields).Execute()

Add one or many POA&M items in a system



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
	poamRequiredFields := []openapiclient.PoamRequiredFields{*openapiclient.NewPoamRequiredFields()} // []PoamRequiredFields | Example request body to add POA&M(s) to a system (systemId)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.POAMAPI.AddPoamBySystemId(context.Background(), systemId).PoamRequiredFields(poamRequiredFields).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `POAMAPI.AddPoamBySystemId``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `AddPoamBySystemId`: PoamResponsePostPutDelete
	fmt.Fprintf(os.Stdout, "Response from `POAMAPI.AddPoamBySystemId`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**systemId** | **int32** | **System Id**: The unique system record identifier. | 

### Other Parameters

Other parameters are passed through a pointer to a apiAddPoamBySystemIdRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **poamRequiredFields** | [**[]PoamRequiredFields**](PoamRequiredFields.md) | Example request body to add POA&amp;M(s) to a system (systemId) | 

### Return type

[**PoamResponsePostPutDelete**](PoamResponsePostPutDelete.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeletePoam

> PoamResponsePostPutDelete DeletePoam(ctx, systemId).PoamRequestDeleteBodyInner(poamRequestDeleteBodyInner).Execute()

Remove one or many POA&M items in a system



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
	poamRequestDeleteBodyInner := []openapiclient.PoamRequestDeleteBodyInner{*openapiclient.NewPoamRequestDeleteBodyInner()} // []PoamRequestDeleteBodyInner | Delete the given POA&M Id

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.POAMAPI.DeletePoam(context.Background(), systemId).PoamRequestDeleteBodyInner(poamRequestDeleteBodyInner).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `POAMAPI.DeletePoam``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `DeletePoam`: PoamResponsePostPutDelete
	fmt.Fprintf(os.Stdout, "Response from `POAMAPI.DeletePoam`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**systemId** | **int32** | **System Id**: The unique system record identifier. | 

### Other Parameters

Other parameters are passed through a pointer to a apiDeletePoamRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **poamRequestDeleteBodyInner** | [**[]PoamRequestDeleteBodyInner**](PoamRequestDeleteBodyInner.md) | Delete the given POA&amp;M Id | 

### Return type

[**PoamResponsePostPutDelete**](PoamResponsePostPutDelete.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetSystemPoams

> PoamResponseGetSystems GetSystemPoams(ctx, systemId).ScheduledCompletionDateStart(scheduledCompletionDateStart).ScheduledCompletionDateEnd(scheduledCompletionDateEnd).ControlAcronyms(controlAcronyms).AssessmentProcedures(assessmentProcedures).Ccis(ccis).SystemOnly(systemOnly).Execute()

Get one or many POA&M items in a system



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
	scheduledCompletionDateStart := "scheduledCompletionDateStart_example" // string | **Date Started**: Filter query by the scheduled completion start date (Unix date format). (optional)
	scheduledCompletionDateEnd := "scheduledCompletionDateEnd_example" // string | **Date Ended**: Filter query by the scheduled completion start date (Unix date format). (optional)
	controlAcronyms := "controlAcronyms_example" // string | **Control Acronym**: Filter query by given system acronym (single value or comma separated). (optional)
	assessmentProcedures := "assessmentProcedures_example" // string | **Assessment Procedure**: Filter query by given Security Control Assessment Procedure (single value or comma separated). (optional)
	ccis := "ccis_example" // string | **CCI System**: Filter query by Control Correlation Identifiers (CCIs) (single value or comma separated). (optional)
	systemOnly := true // bool | **Systems Only**: Indicates that only system(s) information is retrieved. (optional) (default to true)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.POAMAPI.GetSystemPoams(context.Background(), systemId).ScheduledCompletionDateStart(scheduledCompletionDateStart).ScheduledCompletionDateEnd(scheduledCompletionDateEnd).ControlAcronyms(controlAcronyms).AssessmentProcedures(assessmentProcedures).Ccis(ccis).SystemOnly(systemOnly).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `POAMAPI.GetSystemPoams``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetSystemPoams`: PoamResponseGetSystems
	fmt.Fprintf(os.Stdout, "Response from `POAMAPI.GetSystemPoams`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**systemId** | **int32** | **System Id**: The unique system record identifier. | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetSystemPoamsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **scheduledCompletionDateStart** | **string** | **Date Started**: Filter query by the scheduled completion start date (Unix date format). | 
 **scheduledCompletionDateEnd** | **string** | **Date Ended**: Filter query by the scheduled completion start date (Unix date format). | 
 **controlAcronyms** | **string** | **Control Acronym**: Filter query by given system acronym (single value or comma separated). | 
 **assessmentProcedures** | **string** | **Assessment Procedure**: Filter query by given Security Control Assessment Procedure (single value or comma separated). | 
 **ccis** | **string** | **CCI System**: Filter query by Control Correlation Identifiers (CCIs) (single value or comma separated). | 
 **systemOnly** | **bool** | **Systems Only**: Indicates that only system(s) information is retrieved. | [default to true]

### Return type

[**PoamResponseGetSystems**](PoamResponseGetSystems.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetSystemPoamsByPoamId

> PoamResponseGetPoams GetSystemPoamsByPoamId(ctx, systemId, poamId).Execute()

Get POA&M item by ID in a system



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
	poamId := int32(45) // int32 | **POA&M Id**: The unique POA&M record identifier.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.POAMAPI.GetSystemPoamsByPoamId(context.Background(), systemId, poamId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `POAMAPI.GetSystemPoamsByPoamId``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetSystemPoamsByPoamId`: PoamResponseGetPoams
	fmt.Fprintf(os.Stdout, "Response from `POAMAPI.GetSystemPoamsByPoamId`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**systemId** | **int32** | **System Id**: The unique system record identifier. | 
**poamId** | **int32** | **POA&amp;M Id**: The unique POA&amp;M record identifier. | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetSystemPoamsByPoamIdRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

[**PoamResponseGetPoams**](PoamResponseGetPoams.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UpdatePoamBySystemId

> PoamResponsePostPutDelete UpdatePoamBySystemId(ctx, systemId).PoamIds(poamIds).Execute()

Update one or many POA&M items in a system



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
	poamIds := []openapiclient.PoamIds{*openapiclient.NewPoamIds()} // []PoamIds | Example request body for updating a POA&M for a system (systemId)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.POAMAPI.UpdatePoamBySystemId(context.Background(), systemId).PoamIds(poamIds).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `POAMAPI.UpdatePoamBySystemId``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UpdatePoamBySystemId`: PoamResponsePostPutDelete
	fmt.Fprintf(os.Stdout, "Response from `POAMAPI.UpdatePoamBySystemId`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**systemId** | **int32** | **System Id**: The unique system record identifier. | 

### Other Parameters

Other parameters are passed through a pointer to a apiUpdatePoamBySystemIdRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **poamIds** | [**[]PoamIds**](PoamIds.md) | Example request body for updating a POA&amp;M for a system (systemId) | 

### Return type

[**PoamResponsePostPutDelete**](PoamResponsePostPutDelete.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

