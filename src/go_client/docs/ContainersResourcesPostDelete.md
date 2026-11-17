# ContainersResourcesPostDelete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ContainerId** | Pointer to **string** | [Required] Unique identifier of the container | [optional] 
**Success** | Pointer to **bool** |  | [optional] 
**SystemId** | Pointer to **int64** |  | [optional] 
**Errors** | Pointer to **[]interface{}** |  | [optional] 

## Methods

### NewContainersResourcesPostDelete

`func NewContainersResourcesPostDelete() *ContainersResourcesPostDelete`

NewContainersResourcesPostDelete instantiates a new ContainersResourcesPostDelete object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewContainersResourcesPostDeleteWithDefaults

`func NewContainersResourcesPostDeleteWithDefaults() *ContainersResourcesPostDelete`

NewContainersResourcesPostDeleteWithDefaults instantiates a new ContainersResourcesPostDelete object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetContainerId

`func (o *ContainersResourcesPostDelete) GetContainerId() string`

GetContainerId returns the ContainerId field if non-nil, zero value otherwise.

### GetContainerIdOk

`func (o *ContainersResourcesPostDelete) GetContainerIdOk() (*string, bool)`

GetContainerIdOk returns a tuple with the ContainerId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContainerId

`func (o *ContainersResourcesPostDelete) SetContainerId(v string)`

SetContainerId sets ContainerId field to given value.

### HasContainerId

`func (o *ContainersResourcesPostDelete) HasContainerId() bool`

HasContainerId returns a boolean if a field has been set.

### GetSuccess

`func (o *ContainersResourcesPostDelete) GetSuccess() bool`

GetSuccess returns the Success field if non-nil, zero value otherwise.

### GetSuccessOk

`func (o *ContainersResourcesPostDelete) GetSuccessOk() (*bool, bool)`

GetSuccessOk returns a tuple with the Success field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSuccess

`func (o *ContainersResourcesPostDelete) SetSuccess(v bool)`

SetSuccess sets Success field to given value.

### HasSuccess

`func (o *ContainersResourcesPostDelete) HasSuccess() bool`

HasSuccess returns a boolean if a field has been set.

### GetSystemId

`func (o *ContainersResourcesPostDelete) GetSystemId() int64`

GetSystemId returns the SystemId field if non-nil, zero value otherwise.

### GetSystemIdOk

`func (o *ContainersResourcesPostDelete) GetSystemIdOk() (*int64, bool)`

GetSystemIdOk returns a tuple with the SystemId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSystemId

`func (o *ContainersResourcesPostDelete) SetSystemId(v int64)`

SetSystemId sets SystemId field to given value.

### HasSystemId

`func (o *ContainersResourcesPostDelete) HasSystemId() bool`

HasSystemId returns a boolean if a field has been set.

### GetErrors

`func (o *ContainersResourcesPostDelete) GetErrors() []interface{}`

GetErrors returns the Errors field if non-nil, zero value otherwise.

### GetErrorsOk

`func (o *ContainersResourcesPostDelete) GetErrorsOk() (*[]interface{}, bool)`

GetErrorsOk returns a tuple with the Errors field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetErrors

`func (o *ContainersResourcesPostDelete) SetErrors(v []interface{})`

SetErrors sets Errors field to given value.

### HasErrors

`func (o *ContainersResourcesPostDelete) HasErrors() bool`

HasErrors returns a boolean if a field has been set.

### SetErrorsNil

`func (o *ContainersResourcesPostDelete) SetErrorsNil(b bool)`

 SetErrorsNil sets the value for Errors to be an explicit nil

### UnsetErrors
`func (o *ContainersResourcesPostDelete) UnsetErrors()`

UnsetErrors ensures that no value is present for Errors, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


