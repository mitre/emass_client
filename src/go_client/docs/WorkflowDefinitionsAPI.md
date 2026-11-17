# \WorkflowDefinitionsAPI

All URIs are relative to *http://localhost:4010*

Method | HTTP request | Description
------------- | ------------- | -------------
[**GetWorkflowDefinitions**](WorkflowDefinitionsAPI.md#GetWorkflowDefinitions) | **Get** /api/workflows/definitions | Get workflow definitions in a site



## GetWorkflowDefinitions

> WorkflowDefinitionResponseGet GetWorkflowDefinitions(ctx).IncludeInactive(includeInactive).RegistrationType(registrationType).Execute()

Get workflow definitions in a site



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
	includeInactive := true // bool | **Include Inactive**: If no value is specified, the default returns false to not include outdated workflow definitions. (optional) (default to true)
	registrationType := "registrationType_example" // string | **Registration Type**: Filter record by selected registration type (single value or comma delimited values).  **Valid Options Are:** assessAndAuthorize, assessOnly, guest, regular, functional, cloudServiceProvider, commonControlProvider, authorizationToUse, reciprocityAcceptanc  (optional) (default to "regular")

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.WorkflowDefinitionsAPI.GetWorkflowDefinitions(context.Background()).IncludeInactive(includeInactive).RegistrationType(registrationType).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `WorkflowDefinitionsAPI.GetWorkflowDefinitions``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetWorkflowDefinitions`: WorkflowDefinitionResponseGet
	fmt.Fprintf(os.Stdout, "Response from `WorkflowDefinitionsAPI.GetWorkflowDefinitions`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetWorkflowDefinitionsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **includeInactive** | **bool** | **Include Inactive**: If no value is specified, the default returns false to not include outdated workflow definitions. | [default to true]
 **registrationType** | **string** | **Registration Type**: Filter record by selected registration type (single value or comma delimited values).  **Valid Options Are:** assessAndAuthorize, assessOnly, guest, regular, functional, cloudServiceProvider, commonControlProvider, authorizationToUse, reciprocityAcceptanc  | [default to &quot;regular&quot;]

### Return type

[**WorkflowDefinitionResponseGet**](WorkflowDefinitionResponseGet.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

