# InternalServerErrorMeta

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Code** | Pointer to **int32** |  | [optional] [default to 500]
**ErrorMessage** | Pointer to **string** |  | [optional] [default to "Server encountered an unexpected condition which prevented it from fulfilling the request"]

## Methods

### NewInternalServerErrorMeta

`func NewInternalServerErrorMeta() *InternalServerErrorMeta`

NewInternalServerErrorMeta instantiates a new InternalServerErrorMeta object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewInternalServerErrorMetaWithDefaults

`func NewInternalServerErrorMetaWithDefaults() *InternalServerErrorMeta`

NewInternalServerErrorMetaWithDefaults instantiates a new InternalServerErrorMeta object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCode

`func (o *InternalServerErrorMeta) GetCode() int32`

GetCode returns the Code field if non-nil, zero value otherwise.

### GetCodeOk

`func (o *InternalServerErrorMeta) GetCodeOk() (*int32, bool)`

GetCodeOk returns a tuple with the Code field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCode

`func (o *InternalServerErrorMeta) SetCode(v int32)`

SetCode sets Code field to given value.

### HasCode

`func (o *InternalServerErrorMeta) HasCode() bool`

HasCode returns a boolean if a field has been set.

### GetErrorMessage

`func (o *InternalServerErrorMeta) GetErrorMessage() string`

GetErrorMessage returns the ErrorMessage field if non-nil, zero value otherwise.

### GetErrorMessageOk

`func (o *InternalServerErrorMeta) GetErrorMessageOk() (*string, bool)`

GetErrorMessageOk returns a tuple with the ErrorMessage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetErrorMessage

`func (o *InternalServerErrorMeta) SetErrorMessage(v string)`

SetErrorMessage sets ErrorMessage field to given value.

### HasErrorMessage

`func (o *InternalServerErrorMeta) HasErrorMessage() bool`

HasErrorMessage returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


