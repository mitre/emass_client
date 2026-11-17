# CloudResourcesPostDelete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ResourceId** | Pointer to **string** | [Required] Unique identifier/resource namespace for policy compliance result | [optional] 
**Success** | Pointer to **bool** |  | [optional] 
**SystemId** | Pointer to **int64** |  | [optional] 
**Errors** | Pointer to **[]interface{}** |  | [optional] 

## Methods

### NewCloudResourcesPostDelete

`func NewCloudResourcesPostDelete() *CloudResourcesPostDelete`

NewCloudResourcesPostDelete instantiates a new CloudResourcesPostDelete object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCloudResourcesPostDeleteWithDefaults

`func NewCloudResourcesPostDeleteWithDefaults() *CloudResourcesPostDelete`

NewCloudResourcesPostDeleteWithDefaults instantiates a new CloudResourcesPostDelete object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetResourceId

`func (o *CloudResourcesPostDelete) GetResourceId() string`

GetResourceId returns the ResourceId field if non-nil, zero value otherwise.

### GetResourceIdOk

`func (o *CloudResourcesPostDelete) GetResourceIdOk() (*string, bool)`

GetResourceIdOk returns a tuple with the ResourceId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetResourceId

`func (o *CloudResourcesPostDelete) SetResourceId(v string)`

SetResourceId sets ResourceId field to given value.

### HasResourceId

`func (o *CloudResourcesPostDelete) HasResourceId() bool`

HasResourceId returns a boolean if a field has been set.

### GetSuccess

`func (o *CloudResourcesPostDelete) GetSuccess() bool`

GetSuccess returns the Success field if non-nil, zero value otherwise.

### GetSuccessOk

`func (o *CloudResourcesPostDelete) GetSuccessOk() (*bool, bool)`

GetSuccessOk returns a tuple with the Success field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSuccess

`func (o *CloudResourcesPostDelete) SetSuccess(v bool)`

SetSuccess sets Success field to given value.

### HasSuccess

`func (o *CloudResourcesPostDelete) HasSuccess() bool`

HasSuccess returns a boolean if a field has been set.

### GetSystemId

`func (o *CloudResourcesPostDelete) GetSystemId() int64`

GetSystemId returns the SystemId field if non-nil, zero value otherwise.

### GetSystemIdOk

`func (o *CloudResourcesPostDelete) GetSystemIdOk() (*int64, bool)`

GetSystemIdOk returns a tuple with the SystemId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSystemId

`func (o *CloudResourcesPostDelete) SetSystemId(v int64)`

SetSystemId sets SystemId field to given value.

### HasSystemId

`func (o *CloudResourcesPostDelete) HasSystemId() bool`

HasSystemId returns a boolean if a field has been set.

### GetErrors

`func (o *CloudResourcesPostDelete) GetErrors() []interface{}`

GetErrors returns the Errors field if non-nil, zero value otherwise.

### GetErrorsOk

`func (o *CloudResourcesPostDelete) GetErrorsOk() (*[]interface{}, bool)`

GetErrorsOk returns a tuple with the Errors field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetErrors

`func (o *CloudResourcesPostDelete) SetErrors(v []interface{})`

SetErrors sets Errors field to given value.

### HasErrors

`func (o *CloudResourcesPostDelete) HasErrors() bool`

HasErrors returns a boolean if a field has been set.

### SetErrorsNil

`func (o *CloudResourcesPostDelete) SetErrorsNil(b bool)`

 SetErrorsNil sets the value for Errors to be an explicit nil

### UnsetErrors
`func (o *CloudResourcesPostDelete) UnsetErrors()`

UnsetErrors ensures that no value is present for Errors, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


