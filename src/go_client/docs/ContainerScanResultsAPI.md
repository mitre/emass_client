# \ContainerScanResultsAPI

All URIs are relative to *http://localhost:4010*

Method | HTTP request | Description
------------- | ------------- | -------------
[**AddContainerSansBySystemId**](ContainerScanResultsAPI.md#AddContainerSansBySystemId) | **Post** /api/systems/{systemId}/container-scan-results | Add one or many containers and their scan results
[**DeleteContainerSans**](ContainerScanResultsAPI.md#DeleteContainerSans) | **Delete** /api/systems/{systemId}/container-scan-results | Remove one or many containers in a system



## AddContainerSansBySystemId

> ContainersResponsePost AddContainerSansBySystemId(ctx, systemId).RequestBody(requestBody).Execute()

Add one or many containers and their scan results



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
	requestBody := []interface{}{interface{}(123)} // []interface{} | Example request body for adding containers and their scan results

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ContainerScanResultsAPI.AddContainerSansBySystemId(context.Background(), systemId).RequestBody(requestBody).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ContainerScanResultsAPI.AddContainerSansBySystemId``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `AddContainerSansBySystemId`: ContainersResponsePost
	fmt.Fprintf(os.Stdout, "Response from `ContainerScanResultsAPI.AddContainerSansBySystemId`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**systemId** | **int32** | **System Id**: The unique system record identifier. | 

### Other Parameters

Other parameters are passed through a pointer to a apiAddContainerSansBySystemIdRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **requestBody** | **[]interface{}** | Example request body for adding containers and their scan results | 

### Return type

[**ContainersResponsePost**](ContainersResponsePost.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeleteContainerSans

> ContainersResponseDelete DeleteContainerSans(ctx, systemId).ContainerResourcesDeleteBodyInner(containerResourcesDeleteBodyInner).Execute()

Remove one or many containers in a system



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
	containerResourcesDeleteBodyInner := []openapiclient.ContainerResourcesDeleteBodyInner{*openapiclient.NewContainerResourcesDeleteBodyInner()} // []ContainerResourcesDeleteBodyInner | Delete the given Container Scan Id

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ContainerScanResultsAPI.DeleteContainerSans(context.Background(), systemId).ContainerResourcesDeleteBodyInner(containerResourcesDeleteBodyInner).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ContainerScanResultsAPI.DeleteContainerSans``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `DeleteContainerSans`: ContainersResponseDelete
	fmt.Fprintf(os.Stdout, "Response from `ContainerScanResultsAPI.DeleteContainerSans`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**systemId** | **int32** | **System Id**: The unique system record identifier. | 

### Other Parameters

Other parameters are passed through a pointer to a apiDeleteContainerSansRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **containerResourcesDeleteBodyInner** | [**[]ContainerResourcesDeleteBodyInner**](ContainerResourcesDeleteBodyInner.md) | Delete the given Container Scan Id | 

### Return type

[**ContainersResponseDelete**](ContainersResponseDelete.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

