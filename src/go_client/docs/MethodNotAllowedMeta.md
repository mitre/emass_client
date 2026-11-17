# MethodNotAllowedMeta

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Code** | Pointer to **int32** |  | [optional] [default to 405]
**ErrorMessage** | Pointer to **string** |  | [optional] [default to "Request was made with a verb (GET, POST, etc.) that is not permitted for the endpoint"]

## Methods

### NewMethodNotAllowedMeta

`func NewMethodNotAllowedMeta() *MethodNotAllowedMeta`

NewMethodNotAllowedMeta instantiates a new MethodNotAllowedMeta object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewMethodNotAllowedMetaWithDefaults

`func NewMethodNotAllowedMetaWithDefaults() *MethodNotAllowedMeta`

NewMethodNotAllowedMetaWithDefaults instantiates a new MethodNotAllowedMeta object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCode

`func (o *MethodNotAllowedMeta) GetCode() int32`

GetCode returns the Code field if non-nil, zero value otherwise.

### GetCodeOk

`func (o *MethodNotAllowedMeta) GetCodeOk() (*int32, bool)`

GetCodeOk returns a tuple with the Code field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCode

`func (o *MethodNotAllowedMeta) SetCode(v int32)`

SetCode sets Code field to given value.

### HasCode

`func (o *MethodNotAllowedMeta) HasCode() bool`

HasCode returns a boolean if a field has been set.

### GetErrorMessage

`func (o *MethodNotAllowedMeta) GetErrorMessage() string`

GetErrorMessage returns the ErrorMessage field if non-nil, zero value otherwise.

### GetErrorMessageOk

`func (o *MethodNotAllowedMeta) GetErrorMessageOk() (*string, bool)`

GetErrorMessageOk returns a tuple with the ErrorMessage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetErrorMessage

`func (o *MethodNotAllowedMeta) SetErrorMessage(v string)`

SetErrorMessage sets ErrorMessage field to given value.

### HasErrorMessage

`func (o *MethodNotAllowedMeta) HasErrorMessage() bool`

HasErrorMessage returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


