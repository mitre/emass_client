# ControlsPut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Acronym** | Pointer to **string** | Acronym of the system record. | [optional] 
**Success** | Pointer to **bool** | Indicates if operations result (success/fail) | [optional] 
**SystemId** | Pointer to **int64** | The system identifier for the system being updated. | [optional] 
**Errors** | Pointer to **[]interface{}** |  | [optional] 

## Methods

### NewControlsPut

`func NewControlsPut() *ControlsPut`

NewControlsPut instantiates a new ControlsPut object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewControlsPutWithDefaults

`func NewControlsPutWithDefaults() *ControlsPut`

NewControlsPutWithDefaults instantiates a new ControlsPut object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAcronym

`func (o *ControlsPut) GetAcronym() string`

GetAcronym returns the Acronym field if non-nil, zero value otherwise.

### GetAcronymOk

`func (o *ControlsPut) GetAcronymOk() (*string, bool)`

GetAcronymOk returns a tuple with the Acronym field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAcronym

`func (o *ControlsPut) SetAcronym(v string)`

SetAcronym sets Acronym field to given value.

### HasAcronym

`func (o *ControlsPut) HasAcronym() bool`

HasAcronym returns a boolean if a field has been set.

### GetSuccess

`func (o *ControlsPut) GetSuccess() bool`

GetSuccess returns the Success field if non-nil, zero value otherwise.

### GetSuccessOk

`func (o *ControlsPut) GetSuccessOk() (*bool, bool)`

GetSuccessOk returns a tuple with the Success field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSuccess

`func (o *ControlsPut) SetSuccess(v bool)`

SetSuccess sets Success field to given value.

### HasSuccess

`func (o *ControlsPut) HasSuccess() bool`

HasSuccess returns a boolean if a field has been set.

### GetSystemId

`func (o *ControlsPut) GetSystemId() int64`

GetSystemId returns the SystemId field if non-nil, zero value otherwise.

### GetSystemIdOk

`func (o *ControlsPut) GetSystemIdOk() (*int64, bool)`

GetSystemIdOk returns a tuple with the SystemId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSystemId

`func (o *ControlsPut) SetSystemId(v int64)`

SetSystemId sets SystemId field to given value.

### HasSystemId

`func (o *ControlsPut) HasSystemId() bool`

HasSystemId returns a boolean if a field has been set.

### GetErrors

`func (o *ControlsPut) GetErrors() []interface{}`

GetErrors returns the Errors field if non-nil, zero value otherwise.

### GetErrorsOk

`func (o *ControlsPut) GetErrorsOk() (*[]interface{}, bool)`

GetErrorsOk returns a tuple with the Errors field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetErrors

`func (o *ControlsPut) SetErrors(v []interface{})`

SetErrors sets Errors field to given value.

### HasErrors

`func (o *ControlsPut) HasErrors() bool`

HasErrors returns a boolean if a field has been set.

### SetErrorsNil

`func (o *ControlsPut) SetErrorsNil(b bool)`

 SetErrorsNil sets the value for Errors to be an explicit nil

### UnsetErrors
`func (o *ControlsPut) UnsetErrors()`

UnsetErrors ensures that no value is present for Errors, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


