# PoamPostPutDel

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**SystemId** | Pointer to **int64** | The system identifier for the system being updated. | [optional] 
**PoamId** | Pointer to **int64** | The newly created POAM identifier | [optional] 
**ExternalUid** | Pointer to **string** | The unique identifier external to the eMASS application for use with associating POA&amp;Ms. 100 Characters. | [optional] 
**Success** | Pointer to **bool** | Indicates if operations result (success/fail) | [optional] 
**Errors** | Pointer to **[]interface{}** |  | [optional] 

## Methods

### NewPoamPostPutDel

`func NewPoamPostPutDel() *PoamPostPutDel`

NewPoamPostPutDel instantiates a new PoamPostPutDel object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPoamPostPutDelWithDefaults

`func NewPoamPostPutDelWithDefaults() *PoamPostPutDel`

NewPoamPostPutDelWithDefaults instantiates a new PoamPostPutDel object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetSystemId

`func (o *PoamPostPutDel) GetSystemId() int64`

GetSystemId returns the SystemId field if non-nil, zero value otherwise.

### GetSystemIdOk

`func (o *PoamPostPutDel) GetSystemIdOk() (*int64, bool)`

GetSystemIdOk returns a tuple with the SystemId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSystemId

`func (o *PoamPostPutDel) SetSystemId(v int64)`

SetSystemId sets SystemId field to given value.

### HasSystemId

`func (o *PoamPostPutDel) HasSystemId() bool`

HasSystemId returns a boolean if a field has been set.

### GetPoamId

`func (o *PoamPostPutDel) GetPoamId() int64`

GetPoamId returns the PoamId field if non-nil, zero value otherwise.

### GetPoamIdOk

`func (o *PoamPostPutDel) GetPoamIdOk() (*int64, bool)`

GetPoamIdOk returns a tuple with the PoamId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPoamId

`func (o *PoamPostPutDel) SetPoamId(v int64)`

SetPoamId sets PoamId field to given value.

### HasPoamId

`func (o *PoamPostPutDel) HasPoamId() bool`

HasPoamId returns a boolean if a field has been set.

### GetExternalUid

`func (o *PoamPostPutDel) GetExternalUid() string`

GetExternalUid returns the ExternalUid field if non-nil, zero value otherwise.

### GetExternalUidOk

`func (o *PoamPostPutDel) GetExternalUidOk() (*string, bool)`

GetExternalUidOk returns a tuple with the ExternalUid field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExternalUid

`func (o *PoamPostPutDel) SetExternalUid(v string)`

SetExternalUid sets ExternalUid field to given value.

### HasExternalUid

`func (o *PoamPostPutDel) HasExternalUid() bool`

HasExternalUid returns a boolean if a field has been set.

### GetSuccess

`func (o *PoamPostPutDel) GetSuccess() bool`

GetSuccess returns the Success field if non-nil, zero value otherwise.

### GetSuccessOk

`func (o *PoamPostPutDel) GetSuccessOk() (*bool, bool)`

GetSuccessOk returns a tuple with the Success field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSuccess

`func (o *PoamPostPutDel) SetSuccess(v bool)`

SetSuccess sets Success field to given value.

### HasSuccess

`func (o *PoamPostPutDel) HasSuccess() bool`

HasSuccess returns a boolean if a field has been set.

### GetErrors

`func (o *PoamPostPutDel) GetErrors() []interface{}`

GetErrors returns the Errors field if non-nil, zero value otherwise.

### GetErrorsOk

`func (o *PoamPostPutDel) GetErrorsOk() (*[]interface{}, bool)`

GetErrorsOk returns a tuple with the Errors field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetErrors

`func (o *PoamPostPutDel) SetErrors(v []interface{})`

SetErrors sets Errors field to given value.

### HasErrors

`func (o *PoamPostPutDel) HasErrors() bool`

HasErrors returns a boolean if a field has been set.

### SetErrorsNil

`func (o *PoamPostPutDel) SetErrorsNil(b bool)`

 SetErrorsNil sets the value for Errors to be an explicit nil

### UnsetErrors
`func (o *PoamPostPutDel) UnsetErrors()`

UnsetErrors ensures that no value is present for Errors, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


