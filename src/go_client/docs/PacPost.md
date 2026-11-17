# PacPost

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Workflow** | Pointer to **string** | [Required] Values include the following:(Assess and Authorize, Assess Only, Security Plan Approval) | [optional] 
**Success** | Pointer to **bool** |  | [optional] 
**SystemId** | Pointer to **int64** |  | [optional] 
**Errors** | Pointer to **[]interface{}** |  | [optional] 

## Methods

### NewPacPost

`func NewPacPost() *PacPost`

NewPacPost instantiates a new PacPost object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPacPostWithDefaults

`func NewPacPostWithDefaults() *PacPost`

NewPacPostWithDefaults instantiates a new PacPost object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetWorkflow

`func (o *PacPost) GetWorkflow() string`

GetWorkflow returns the Workflow field if non-nil, zero value otherwise.

### GetWorkflowOk

`func (o *PacPost) GetWorkflowOk() (*string, bool)`

GetWorkflowOk returns a tuple with the Workflow field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWorkflow

`func (o *PacPost) SetWorkflow(v string)`

SetWorkflow sets Workflow field to given value.

### HasWorkflow

`func (o *PacPost) HasWorkflow() bool`

HasWorkflow returns a boolean if a field has been set.

### GetSuccess

`func (o *PacPost) GetSuccess() bool`

GetSuccess returns the Success field if non-nil, zero value otherwise.

### GetSuccessOk

`func (o *PacPost) GetSuccessOk() (*bool, bool)`

GetSuccessOk returns a tuple with the Success field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSuccess

`func (o *PacPost) SetSuccess(v bool)`

SetSuccess sets Success field to given value.

### HasSuccess

`func (o *PacPost) HasSuccess() bool`

HasSuccess returns a boolean if a field has been set.

### GetSystemId

`func (o *PacPost) GetSystemId() int64`

GetSystemId returns the SystemId field if non-nil, zero value otherwise.

### GetSystemIdOk

`func (o *PacPost) GetSystemIdOk() (*int64, bool)`

GetSystemIdOk returns a tuple with the SystemId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSystemId

`func (o *PacPost) SetSystemId(v int64)`

SetSystemId sets SystemId field to given value.

### HasSystemId

`func (o *PacPost) HasSystemId() bool`

HasSystemId returns a boolean if a field has been set.

### GetErrors

`func (o *PacPost) GetErrors() []interface{}`

GetErrors returns the Errors field if non-nil, zero value otherwise.

### GetErrorsOk

`func (o *PacPost) GetErrorsOk() (*[]interface{}, bool)`

GetErrorsOk returns a tuple with the Errors field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetErrors

`func (o *PacPost) SetErrors(v []interface{})`

SetErrors sets Errors field to given value.

### HasErrors

`func (o *PacPost) HasErrors() bool`

HasErrors returns a boolean if a field has been set.

### SetErrorsNil

`func (o *PacPost) SetErrorsNil(b bool)`

 SetErrorsNil sets the value for Errors to be an explicit nil

### UnsetErrors
`func (o *PacPost) UnsetErrors()`

UnsetErrors ensures that no value is present for Errors, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


