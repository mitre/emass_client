# LengthRequiredMeta

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Code** | Pointer to **int32** |  | [optional] [default to 411]
**ErrorMessage** | Pointer to **string** |  | [optional] [default to "Request was of type POST and failed to provide the server information about the data/content length being submitted"]

## Methods

### NewLengthRequiredMeta

`func NewLengthRequiredMeta() *LengthRequiredMeta`

NewLengthRequiredMeta instantiates a new LengthRequiredMeta object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewLengthRequiredMetaWithDefaults

`func NewLengthRequiredMetaWithDefaults() *LengthRequiredMeta`

NewLengthRequiredMetaWithDefaults instantiates a new LengthRequiredMeta object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCode

`func (o *LengthRequiredMeta) GetCode() int32`

GetCode returns the Code field if non-nil, zero value otherwise.

### GetCodeOk

`func (o *LengthRequiredMeta) GetCodeOk() (*int32, bool)`

GetCodeOk returns a tuple with the Code field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCode

`func (o *LengthRequiredMeta) SetCode(v int32)`

SetCode sets Code field to given value.

### HasCode

`func (o *LengthRequiredMeta) HasCode() bool`

HasCode returns a boolean if a field has been set.

### GetErrorMessage

`func (o *LengthRequiredMeta) GetErrorMessage() string`

GetErrorMessage returns the ErrorMessage field if non-nil, zero value otherwise.

### GetErrorMessageOk

`func (o *LengthRequiredMeta) GetErrorMessageOk() (*string, bool)`

GetErrorMessageOk returns a tuple with the ErrorMessage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetErrorMessage

`func (o *LengthRequiredMeta) SetErrorMessage(v string)`

SetErrorMessage sets ErrorMessage field to given value.

### HasErrorMessage

`func (o *LengthRequiredMeta) HasErrorMessage() bool`

HasErrorMessage returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


