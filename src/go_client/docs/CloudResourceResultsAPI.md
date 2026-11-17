# \CloudResourceResultsAPI

All URIs are relative to *http://localhost:4010*

Method | HTTP request | Description
------------- | ------------- | -------------
[**AddCloudResourcesBySystemId**](CloudResourceResultsAPI.md#AddCloudResourcesBySystemId) | **Post** /api/systems/{systemId}/cloud-resource-results | Add one or many cloud resources and their scan results
[**DeleteCloudResources**](CloudResourceResultsAPI.md#DeleteCloudResources) | **Delete** /api/systems/{systemId}/cloud-resource-results | Remove one or many cloud resources in a system



## AddCloudResourcesBySystemId

> CloudResourcesResponsePost AddCloudResourcesBySystemId(ctx, systemId).RequestBody(requestBody).Execute()

Add one or many cloud resources and their scan results



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
	requestBody := []interface{}{interface{}(123)} // []interface{} | Example request body for adding cloud resources and their scan results

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.CloudResourceResultsAPI.AddCloudResourcesBySystemId(context.Background(), systemId).RequestBody(requestBody).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CloudResourceResultsAPI.AddCloudResourcesBySystemId``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `AddCloudResourcesBySystemId`: CloudResourcesResponsePost
	fmt.Fprintf(os.Stdout, "Response from `CloudResourceResultsAPI.AddCloudResourcesBySystemId`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**systemId** | **int32** | **System Id**: The unique system record identifier. | 

### Other Parameters

Other parameters are passed through a pointer to a apiAddCloudResourcesBySystemIdRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **requestBody** | **[]interface{}** | Example request body for adding cloud resources and their scan results | 

### Return type

[**CloudResourcesResponsePost**](CloudResourcesResponsePost.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeleteCloudResources

> CloudResourcesDelete DeleteCloudResources(ctx, systemId).CloudResourcesDeleteBodyInner(cloudResourcesDeleteBodyInner).Execute()

Remove one or many cloud resources in a system



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
	cloudResourcesDeleteBodyInner := []openapiclient.CloudResourcesDeleteBodyInner{*openapiclient.NewCloudResourcesDeleteBodyInner()} // []CloudResourcesDeleteBodyInner | Delete the given Cloud Resource Id

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.CloudResourceResultsAPI.DeleteCloudResources(context.Background(), systemId).CloudResourcesDeleteBodyInner(cloudResourcesDeleteBodyInner).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CloudResourceResultsAPI.DeleteCloudResources``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `DeleteCloudResources`: CloudResourcesDelete
	fmt.Fprintf(os.Stdout, "Response from `CloudResourceResultsAPI.DeleteCloudResources`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**systemId** | **int32** | **System Id**: The unique system record identifier. | 

### Other Parameters

Other parameters are passed through a pointer to a apiDeleteCloudResourcesRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **cloudResourcesDeleteBodyInner** | [**[]CloudResourcesDeleteBodyInner**](CloudResourcesDeleteBodyInner.md) | Delete the given Cloud Resource Id | 

### Return type

[**CloudResourcesDelete**](CloudResourcesDelete.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

