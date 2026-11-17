# MilestonesPutPostDelete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**SystemId** | Pointer to **int64** | The system identifier that the POAM was added. | [optional] 
**PoamId** | Pointer to **int64** | The newly created POAM identifier | [optional] 
**MilestoneId** | Pointer to **int64** | The Milestone unique item identifier | [optional] 
**ExternalUid** | Pointer to **string** | The unique identifier external to the eMASS application for use with associating POA&amp;Ms. 100 Characters. | [optional] 
**Success** | Pointer to **bool** | Indicates if operations result (success/fail) | [optional] 
**Errors** | Pointer to **[]interface{}** |  | [optional] 

## Methods

### NewMilestonesPutPostDelete

`func NewMilestonesPutPostDelete() *MilestonesPutPostDelete`

NewMilestonesPutPostDelete instantiates a new MilestonesPutPostDelete object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewMilestonesPutPostDeleteWithDefaults

`func NewMilestonesPutPostDeleteWithDefaults() *MilestonesPutPostDelete`

NewMilestonesPutPostDeleteWithDefaults instantiates a new MilestonesPutPostDelete object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetSystemId

`func (o *MilestonesPutPostDelete) GetSystemId() int64`

GetSystemId returns the SystemId field if non-nil, zero value otherwise.

### GetSystemIdOk

`func (o *MilestonesPutPostDelete) GetSystemIdOk() (*int64, bool)`

GetSystemIdOk returns a tuple with the SystemId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSystemId

`func (o *MilestonesPutPostDelete) SetSystemId(v int64)`

SetSystemId sets SystemId field to given value.

### HasSystemId

`func (o *MilestonesPutPostDelete) HasSystemId() bool`

HasSystemId returns a boolean if a field has been set.

### GetPoamId

`func (o *MilestonesPutPostDelete) GetPoamId() int64`

GetPoamId returns the PoamId field if non-nil, zero value otherwise.

### GetPoamIdOk

`func (o *MilestonesPutPostDelete) GetPoamIdOk() (*int64, bool)`

GetPoamIdOk returns a tuple with the PoamId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPoamId

`func (o *MilestonesPutPostDelete) SetPoamId(v int64)`

SetPoamId sets PoamId field to given value.

### HasPoamId

`func (o *MilestonesPutPostDelete) HasPoamId() bool`

HasPoamId returns a boolean if a field has been set.

### GetMilestoneId

`func (o *MilestonesPutPostDelete) GetMilestoneId() int64`

GetMilestoneId returns the MilestoneId field if non-nil, zero value otherwise.

### GetMilestoneIdOk

`func (o *MilestonesPutPostDelete) GetMilestoneIdOk() (*int64, bool)`

GetMilestoneIdOk returns a tuple with the MilestoneId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMilestoneId

`func (o *MilestonesPutPostDelete) SetMilestoneId(v int64)`

SetMilestoneId sets MilestoneId field to given value.

### HasMilestoneId

`func (o *MilestonesPutPostDelete) HasMilestoneId() bool`

HasMilestoneId returns a boolean if a field has been set.

### GetExternalUid

`func (o *MilestonesPutPostDelete) GetExternalUid() string`

GetExternalUid returns the ExternalUid field if non-nil, zero value otherwise.

### GetExternalUidOk

`func (o *MilestonesPutPostDelete) GetExternalUidOk() (*string, bool)`

GetExternalUidOk returns a tuple with the ExternalUid field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExternalUid

`func (o *MilestonesPutPostDelete) SetExternalUid(v string)`

SetExternalUid sets ExternalUid field to given value.

### HasExternalUid

`func (o *MilestonesPutPostDelete) HasExternalUid() bool`

HasExternalUid returns a boolean if a field has been set.

### GetSuccess

`func (o *MilestonesPutPostDelete) GetSuccess() bool`

GetSuccess returns the Success field if non-nil, zero value otherwise.

### GetSuccessOk

`func (o *MilestonesPutPostDelete) GetSuccessOk() (*bool, bool)`

GetSuccessOk returns a tuple with the Success field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSuccess

`func (o *MilestonesPutPostDelete) SetSuccess(v bool)`

SetSuccess sets Success field to given value.

### HasSuccess

`func (o *MilestonesPutPostDelete) HasSuccess() bool`

HasSuccess returns a boolean if a field has been set.

### GetErrors

`func (o *MilestonesPutPostDelete) GetErrors() []interface{}`

GetErrors returns the Errors field if non-nil, zero value otherwise.

### GetErrorsOk

`func (o *MilestonesPutPostDelete) GetErrorsOk() (*[]interface{}, bool)`

GetErrorsOk returns a tuple with the Errors field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetErrors

`func (o *MilestonesPutPostDelete) SetErrors(v []interface{})`

SetErrors sets Errors field to given value.

### HasErrors

`func (o *MilestonesPutPostDelete) HasErrors() bool`

HasErrors returns a boolean if a field has been set.

### SetErrorsNil

`func (o *MilestonesPutPostDelete) SetErrorsNil(b bool)`

 SetErrorsNil sets the value for Errors to be an explicit nil

### UnsetErrors
`func (o *MilestonesPutPostDelete) UnsetErrors()`

UnsetErrors ensures that no value is present for Errors, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


