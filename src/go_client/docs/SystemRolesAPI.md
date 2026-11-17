# \SystemRolesAPI

All URIs are relative to *http://localhost:4010*

Method | HTTP request | Description
------------- | ------------- | -------------
[**GetSystemRoles**](SystemRolesAPI.md#GetSystemRoles) | **Get** /api/system-roles | Get available roles
[**GetSystemRolesByCategoryId**](SystemRolesAPI.md#GetSystemRolesByCategoryId) | **Get** /api/system-roles/{roleCategory} | Get system roles



## GetSystemRoles

> SystemRolesResponse GetSystemRoles(ctx).Execute()

Get available roles



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

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SystemRolesAPI.GetSystemRoles(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SystemRolesAPI.GetSystemRoles``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetSystemRoles`: SystemRolesResponse
	fmt.Fprintf(os.Stdout, "Response from `SystemRolesAPI.GetSystemRoles`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiGetSystemRolesRequest struct via the builder pattern


### Return type

[**SystemRolesResponse**](SystemRolesResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetSystemRolesByCategoryId

> SystemRolesCategoryResponse GetSystemRolesByCategoryId(ctx, roleCategory).Role(role).Policy(policy).Execute()

Get system roles



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
	roleCategory := "roleCategory_example" // string | **Role Category**: The system role category been queried (default to "PAC")
	role := "role_example" // string | **Role**: Accepts single value from options available at base system-roles endpoint e.g., SCA. (default to "IAO")
	policy := "policy_example" // string | **System Policy**: Filter query by system policy. If no value is specified, the default returns RMF policy information for dual-policy systems. (optional) (default to "rmf")

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SystemRolesAPI.GetSystemRolesByCategoryId(context.Background(), roleCategory).Role(role).Policy(policy).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SystemRolesAPI.GetSystemRolesByCategoryId``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetSystemRolesByCategoryId`: SystemRolesCategoryResponse
	fmt.Fprintf(os.Stdout, "Response from `SystemRolesAPI.GetSystemRolesByCategoryId`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**roleCategory** | **string** | **Role Category**: The system role category been queried | [default to &quot;PAC&quot;]

### Other Parameters

Other parameters are passed through a pointer to a apiGetSystemRolesByCategoryIdRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **role** | **string** | **Role**: Accepts single value from options available at base system-roles endpoint e.g., SCA. | [default to &quot;IAO&quot;]
 **policy** | **string** | **System Policy**: Filter query by system policy. If no value is specified, the default returns RMF policy information for dual-policy systems. | [default to &quot;rmf&quot;]

### Return type

[**SystemRolesCategoryResponse**](SystemRolesCategoryResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

