# \WorkflowInstancesAPI

All URIs are relative to *http://localhost:4010*

Method | HTTP request | Description
------------- | ------------- | -------------
[**GetSystemWorkflowInstances**](WorkflowInstancesAPI.md#GetSystemWorkflowInstances) | **Get** /api/workflows/instances | Get workflow instances in a site
[**GetSystemWorkflowInstancesByWorkflowInstanceId**](WorkflowInstancesAPI.md#GetSystemWorkflowInstancesByWorkflowInstanceId) | **Get** /api/workflows/instances/{workflowInstanceId} | Get workflow instance by ID



## GetSystemWorkflowInstances

> WorkflowInstancesResponseGet GetSystemWorkflowInstances(ctx).IncludeComments(includeComments).IncludeDecommissionSystems(includeDecommissionSystems).PageIndex(pageIndex).SinceDate(sinceDate).Status(status).Execute()

Get workflow instances in a site



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
	includeComments := true // bool | **Include Comments**: If no value is specified, the default returns true to not include transition comments. Note: Corresponds to the Comments textbox that is required at most workflow transitions. Does not include other text input fields such as Terms / Conditions for Authorization.  (optional) (default to true)
	includeDecommissionSystems := true // bool | **Include Decommission Systems**: If no value is specified, the default returns false to exclude decommissioned systems.  (optional) (default to false)
	pageIndex := int32(56) // int32 | **Page Index**: If no value is specified, the default returns results from the first page with an index of 0. **Note:** Pages contain 1000 workflow instances.  (optional) (default to 0)
	sinceDate := "1638764040" // string | **Date**: Filter on authorization/assessment date (Unix date format). Note: Filters off the lastEditedDate field. Note: The authorization/assessment decisions on completed workflows can be edited for up to 30 days after the initial decision is made.  (optional)
	status := "status_example" // string | **Status**: Filter by status. If no value is specified, the default returns all to include both active and inactive workflows. Note: Any workflows at a current stage of Complete or Cancelled are inactive. Ongoing workflows currently at other stages are active.  (optional) (default to "all")

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.WorkflowInstancesAPI.GetSystemWorkflowInstances(context.Background()).IncludeComments(includeComments).IncludeDecommissionSystems(includeDecommissionSystems).PageIndex(pageIndex).SinceDate(sinceDate).Status(status).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `WorkflowInstancesAPI.GetSystemWorkflowInstances``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetSystemWorkflowInstances`: WorkflowInstancesResponseGet
	fmt.Fprintf(os.Stdout, "Response from `WorkflowInstancesAPI.GetSystemWorkflowInstances`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetSystemWorkflowInstancesRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **includeComments** | **bool** | **Include Comments**: If no value is specified, the default returns true to not include transition comments. Note: Corresponds to the Comments textbox that is required at most workflow transitions. Does not include other text input fields such as Terms / Conditions for Authorization.  | [default to true]
 **includeDecommissionSystems** | **bool** | **Include Decommission Systems**: If no value is specified, the default returns false to exclude decommissioned systems.  | [default to false]
 **pageIndex** | **int32** | **Page Index**: If no value is specified, the default returns results from the first page with an index of 0. **Note:** Pages contain 1000 workflow instances.  | [default to 0]
 **sinceDate** | **string** | **Date**: Filter on authorization/assessment date (Unix date format). Note: Filters off the lastEditedDate field. Note: The authorization/assessment decisions on completed workflows can be edited for up to 30 days after the initial decision is made.  | 
 **status** | **string** | **Status**: Filter by status. If no value is specified, the default returns all to include both active and inactive workflows. Note: Any workflows at a current stage of Complete or Cancelled are inactive. Ongoing workflows currently at other stages are active.  | [default to &quot;all&quot;]

### Return type

[**WorkflowInstancesResponseGet**](WorkflowInstancesResponseGet.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetSystemWorkflowInstancesByWorkflowInstanceId

> WorkflowInstanceResponseGet GetSystemWorkflowInstancesByWorkflowInstanceId(ctx, workflowInstanceId).Execute()

Get workflow instance by ID



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
	workflowInstanceId := int32(123) // int32 | **Workflow Instance Id**: The unique workflow definition identifier.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.WorkflowInstancesAPI.GetSystemWorkflowInstancesByWorkflowInstanceId(context.Background(), workflowInstanceId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `WorkflowInstancesAPI.GetSystemWorkflowInstancesByWorkflowInstanceId``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetSystemWorkflowInstancesByWorkflowInstanceId`: WorkflowInstanceResponseGet
	fmt.Fprintf(os.Stdout, "Response from `WorkflowInstancesAPI.GetSystemWorkflowInstancesByWorkflowInstanceId`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**workflowInstanceId** | **int32** | **Workflow Instance Id**: The unique workflow definition identifier. | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetSystemWorkflowInstancesByWorkflowInstanceIdRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**WorkflowInstanceResponseGet**](WorkflowInstanceResponseGet.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

