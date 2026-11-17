# \MilestonesAPI

All URIs are relative to *http://localhost:4010*

Method | HTTP request | Description
------------- | ------------- | -------------
[**AddMilestoneBySystemIdAndPoamId**](MilestonesAPI.md#AddMilestoneBySystemIdAndPoamId) | **Post** /api/systems/{systemId}/poams/{poamId}/milestones | Add milestones to one or many POA&amp;M items in a system
[**DeleteMilestone**](MilestonesAPI.md#DeleteMilestone) | **Delete** /api/systems/{systemId}/poams/{poamId}/milestones | Remove milestones in a system for one or many POA&amp;M items
[**GetSystemMilestonesByPoamId**](MilestonesAPI.md#GetSystemMilestonesByPoamId) | **Get** /api/systems/{systemId}/poams/{poamId}/milestones | Get milestones in one or many POA&amp;M items in a system
[**GetSystemMilestonesByPoamIdAndMilestoneId**](MilestonesAPI.md#GetSystemMilestonesByPoamIdAndMilestoneId) | **Get** /api/systems/{systemId}/poams/{poamId}/milestones/{milestoneId} | Get milestone by ID in POA&amp;M item in a system
[**UpdateMilestoneBySystemIdAndPoamId**](MilestonesAPI.md#UpdateMilestoneBySystemIdAndPoamId) | **Put** /api/systems/{systemId}/poams/{poamId}/milestones | Update one or many POA&amp;M items in a system



## AddMilestoneBySystemIdAndPoamId

> MilestoneResponsePost AddMilestoneBySystemIdAndPoamId(ctx, systemId, poamId).RequestBody(requestBody).Execute()

Add milestones to one or many POA&M items in a system



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
	requestBody := []interface{}{interface{}(123)} // []interface{} | Example request body for adding milestones to an existing System (systemId) POA&M (poamId)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.MilestonesAPI.AddMilestoneBySystemIdAndPoamId(context.Background(), systemId, poamId).RequestBody(requestBody).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MilestonesAPI.AddMilestoneBySystemIdAndPoamId``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `AddMilestoneBySystemIdAndPoamId`: MilestoneResponsePost
	fmt.Fprintf(os.Stdout, "Response from `MilestonesAPI.AddMilestoneBySystemIdAndPoamId`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**systemId** | **int32** | **System Id**: The unique system record identifier. | 
**poamId** | **int32** | **POA&amp;M Id**: The unique POA&amp;M record identifier. | 

### Other Parameters

Other parameters are passed through a pointer to a apiAddMilestoneBySystemIdAndPoamIdRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **requestBody** | **[]interface{}** | Example request body for adding milestones to an existing System (systemId) POA&amp;M (poamId) | 

### Return type

[**MilestoneResponsePost**](MilestoneResponsePost.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeleteMilestone

> MilestoneResponseDelete DeleteMilestone(ctx, systemId, poamId).MilestonesRequestDeleteBodyInner(milestonesRequestDeleteBodyInner).Execute()

Remove milestones in a system for one or many POA&M items



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
	milestonesRequestDeleteBodyInner := []openapiclient.MilestonesRequestDeleteBodyInner{*openapiclient.NewMilestonesRequestDeleteBodyInner()} // []MilestonesRequestDeleteBodyInner | Delete the given Milestone Id

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.MilestonesAPI.DeleteMilestone(context.Background(), systemId, poamId).MilestonesRequestDeleteBodyInner(milestonesRequestDeleteBodyInner).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MilestonesAPI.DeleteMilestone``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `DeleteMilestone`: MilestoneResponseDelete
	fmt.Fprintf(os.Stdout, "Response from `MilestonesAPI.DeleteMilestone`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**systemId** | **int32** | **System Id**: The unique system record identifier. | 
**poamId** | **int32** | **POA&amp;M Id**: The unique POA&amp;M record identifier. | 

### Other Parameters

Other parameters are passed through a pointer to a apiDeleteMilestoneRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **milestonesRequestDeleteBodyInner** | [**[]MilestonesRequestDeleteBodyInner**](MilestonesRequestDeleteBodyInner.md) | Delete the given Milestone Id | 

### Return type

[**MilestoneResponseDelete**](MilestoneResponseDelete.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetSystemMilestonesByPoamId

> MilestoneResponseGet GetSystemMilestonesByPoamId(ctx, systemId, poamId).ScheduledCompletionDateStart(scheduledCompletionDateStart).ScheduledCompletionDateEnd(scheduledCompletionDateEnd).Execute()

Get milestones in one or many POA&M items in a system



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
	scheduledCompletionDateStart := "scheduledCompletionDateStart_example" // string | **Date Started**: Filter query by the scheduled completion start date (Unix date format). (optional)
	scheduledCompletionDateEnd := "scheduledCompletionDateEnd_example" // string | **Date Ended**: Filter query by the scheduled completion start date (Unix date format). (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.MilestonesAPI.GetSystemMilestonesByPoamId(context.Background(), systemId, poamId).ScheduledCompletionDateStart(scheduledCompletionDateStart).ScheduledCompletionDateEnd(scheduledCompletionDateEnd).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MilestonesAPI.GetSystemMilestonesByPoamId``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetSystemMilestonesByPoamId`: MilestoneResponseGet
	fmt.Fprintf(os.Stdout, "Response from `MilestonesAPI.GetSystemMilestonesByPoamId`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**systemId** | **int32** | **System Id**: The unique system record identifier. | 
**poamId** | **int32** | **POA&amp;M Id**: The unique POA&amp;M record identifier. | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetSystemMilestonesByPoamIdRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **scheduledCompletionDateStart** | **string** | **Date Started**: Filter query by the scheduled completion start date (Unix date format). | 
 **scheduledCompletionDateEnd** | **string** | **Date Ended**: Filter query by the scheduled completion start date (Unix date format). | 

### Return type

[**MilestoneResponseGet**](MilestoneResponseGet.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetSystemMilestonesByPoamIdAndMilestoneId

> MilestoneResponseGetMilestone GetSystemMilestonesByPoamIdAndMilestoneId(ctx, systemId, poamId, milestoneId).Execute()

Get milestone by ID in POA&M item in a system



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
	milestoneId := int32(77) // int32 | **Milestone Id**: The unique milestone record identifier.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.MilestonesAPI.GetSystemMilestonesByPoamIdAndMilestoneId(context.Background(), systemId, poamId, milestoneId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MilestonesAPI.GetSystemMilestonesByPoamIdAndMilestoneId``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetSystemMilestonesByPoamIdAndMilestoneId`: MilestoneResponseGetMilestone
	fmt.Fprintf(os.Stdout, "Response from `MilestonesAPI.GetSystemMilestonesByPoamIdAndMilestoneId`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**systemId** | **int32** | **System Id**: The unique system record identifier. | 
**poamId** | **int32** | **POA&amp;M Id**: The unique POA&amp;M record identifier. | 
**milestoneId** | **int32** | **Milestone Id**: The unique milestone record identifier. | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetSystemMilestonesByPoamIdAndMilestoneIdRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------




### Return type

[**MilestoneResponseGetMilestone**](MilestoneResponseGetMilestone.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UpdateMilestoneBySystemIdAndPoamId

> MilestoneResponsePut UpdateMilestoneBySystemIdAndPoamId(ctx, systemId, poamId).RequestBody(requestBody).Execute()

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
	poamId := int32(45) // int32 | **POA&M Id**: The unique POA&M record identifier.
	requestBody := []interface{}{interface{}(123)} // []interface{} | Example request body for updating milestones (milestoneId) of an existing System (systemId) POA&M (poamId)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.MilestonesAPI.UpdateMilestoneBySystemIdAndPoamId(context.Background(), systemId, poamId).RequestBody(requestBody).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MilestonesAPI.UpdateMilestoneBySystemIdAndPoamId``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UpdateMilestoneBySystemIdAndPoamId`: MilestoneResponsePut
	fmt.Fprintf(os.Stdout, "Response from `MilestonesAPI.UpdateMilestoneBySystemIdAndPoamId`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**systemId** | **int32** | **System Id**: The unique system record identifier. | 
**poamId** | **int32** | **POA&amp;M Id**: The unique POA&amp;M record identifier. | 

### Other Parameters

Other parameters are passed through a pointer to a apiUpdateMilestoneBySystemIdAndPoamIdRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **requestBody** | **[]interface{}** | Example request body for updating milestones (milestoneId) of an existing System (systemId) POA&amp;M (poamId) | 

### Return type

[**MilestoneResponsePut**](MilestoneResponsePut.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

