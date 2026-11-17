# CacResponsePostDataInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ControlAcronym** | Pointer to **string** | [Required] System acronym name. | [optional] 
**Success** | Pointer to **bool** |  | [optional] 
**SystemId** | Pointer to **int64** |  | [optional] 
**Errors** | Pointer to **[]interface{}** |  | [optional] 

## Methods

### NewCacResponsePostDataInner

`func NewCacResponsePostDataInner() *CacResponsePostDataInner`

NewCacResponsePostDataInner instantiates a new CacResponsePostDataInner object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCacResponsePostDataInnerWithDefaults

`func NewCacResponsePostDataInnerWithDefaults() *CacResponsePostDataInner`

NewCacResponsePostDataInnerWithDefaults instantiates a new CacResponsePostDataInner object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetControlAcronym

`func (o *CacResponsePostDataInner) GetControlAcronym() string`

GetControlAcronym returns the ControlAcronym field if non-nil, zero value otherwise.

### GetControlAcronymOk

`func (o *CacResponsePostDataInner) GetControlAcronymOk() (*string, bool)`

GetControlAcronymOk returns a tuple with the ControlAcronym field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetControlAcronym

`func (o *CacResponsePostDataInner) SetControlAcronym(v string)`

SetControlAcronym sets ControlAcronym field to given value.

### HasControlAcronym

`func (o *CacResponsePostDataInner) HasControlAcronym() bool`

HasControlAcronym returns a boolean if a field has been set.

### GetSuccess

`func (o *CacResponsePostDataInner) GetSuccess() bool`

GetSuccess returns the Success field if non-nil, zero value otherwise.

### GetSuccessOk

`func (o *CacResponsePostDataInner) GetSuccessOk() (*bool, bool)`

GetSuccessOk returns a tuple with the Success field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSuccess

`func (o *CacResponsePostDataInner) SetSuccess(v bool)`

SetSuccess sets Success field to given value.

### HasSuccess

`func (o *CacResponsePostDataInner) HasSuccess() bool`

HasSuccess returns a boolean if a field has been set.

### GetSystemId

`func (o *CacResponsePostDataInner) GetSystemId() int64`

GetSystemId returns the SystemId field if non-nil, zero value otherwise.

### GetSystemIdOk

`func (o *CacResponsePostDataInner) GetSystemIdOk() (*int64, bool)`

GetSystemIdOk returns a tuple with the SystemId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSystemId

`func (o *CacResponsePostDataInner) SetSystemId(v int64)`

SetSystemId sets SystemId field to given value.

### HasSystemId

`func (o *CacResponsePostDataInner) HasSystemId() bool`

HasSystemId returns a boolean if a field has been set.

### GetErrors

`func (o *CacResponsePostDataInner) GetErrors() []interface{}`

GetErrors returns the Errors field if non-nil, zero value otherwise.

### GetErrorsOk

`func (o *CacResponsePostDataInner) GetErrorsOk() (*[]interface{}, bool)`

GetErrorsOk returns a tuple with the Errors field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetErrors

`func (o *CacResponsePostDataInner) SetErrors(v []interface{})`

SetErrors sets Errors field to given value.

### HasErrors

`func (o *CacResponsePostDataInner) HasErrors() bool`

HasErrors returns a boolean if a field has been set.

### SetErrorsNil

`func (o *CacResponsePostDataInner) SetErrorsNil(b bool)`

 SetErrorsNil sets the value for Errors to be an explicit nil

### UnsetErrors
`func (o *CacResponsePostDataInner) UnsetErrors()`

UnsetErrors ensures that no value is present for Errors, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


