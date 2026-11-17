# APIRuleFailedMeta

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Code** | Pointer to **int32** |  | [optional] [default to 490]
**ErrorMessage** | Pointer to **string** |  | [optional] [default to "Request has failed because too much data was requested in a single batch. This error is specific to eMASS"]

## Methods

### NewAPIRuleFailedMeta

`func NewAPIRuleFailedMeta() *APIRuleFailedMeta`

NewAPIRuleFailedMeta instantiates a new APIRuleFailedMeta object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewAPIRuleFailedMetaWithDefaults

`func NewAPIRuleFailedMetaWithDefaults() *APIRuleFailedMeta`

NewAPIRuleFailedMetaWithDefaults instantiates a new APIRuleFailedMeta object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCode

`func (o *APIRuleFailedMeta) GetCode() int32`

GetCode returns the Code field if non-nil, zero value otherwise.

### GetCodeOk

`func (o *APIRuleFailedMeta) GetCodeOk() (*int32, bool)`

GetCodeOk returns a tuple with the Code field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCode

`func (o *APIRuleFailedMeta) SetCode(v int32)`

SetCode sets Code field to given value.

### HasCode

`func (o *APIRuleFailedMeta) HasCode() bool`

HasCode returns a boolean if a field has been set.

### GetErrorMessage

`func (o *APIRuleFailedMeta) GetErrorMessage() string`

GetErrorMessage returns the ErrorMessage field if non-nil, zero value otherwise.

### GetErrorMessageOk

`func (o *APIRuleFailedMeta) GetErrorMessageOk() (*string, bool)`

GetErrorMessageOk returns a tuple with the ErrorMessage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetErrorMessage

`func (o *APIRuleFailedMeta) SetErrorMessage(v string)`

SetErrorMessage sets ErrorMessage field to given value.

### HasErrorMessage

`func (o *APIRuleFailedMeta) HasErrorMessage() bool`

HasErrorMessage returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


