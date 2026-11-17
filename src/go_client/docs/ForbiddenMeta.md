# ForbiddenMeta

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Code** | Pointer to **int32** |  | [optional] [default to 403]
**ErrorMessage** | Pointer to **string** |  | [optional] [default to "Request was blocked by the application due to a lack of client permissions to the API or to a specific endpoint"]

## Methods

### NewForbiddenMeta

`func NewForbiddenMeta() *ForbiddenMeta`

NewForbiddenMeta instantiates a new ForbiddenMeta object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewForbiddenMetaWithDefaults

`func NewForbiddenMetaWithDefaults() *ForbiddenMeta`

NewForbiddenMetaWithDefaults instantiates a new ForbiddenMeta object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCode

`func (o *ForbiddenMeta) GetCode() int32`

GetCode returns the Code field if non-nil, zero value otherwise.

### GetCodeOk

`func (o *ForbiddenMeta) GetCodeOk() (*int32, bool)`

GetCodeOk returns a tuple with the Code field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCode

`func (o *ForbiddenMeta) SetCode(v int32)`

SetCode sets Code field to given value.

### HasCode

`func (o *ForbiddenMeta) HasCode() bool`

HasCode returns a boolean if a field has been set.

### GetErrorMessage

`func (o *ForbiddenMeta) GetErrorMessage() string`

GetErrorMessage returns the ErrorMessage field if non-nil, zero value otherwise.

### GetErrorMessageOk

`func (o *ForbiddenMeta) GetErrorMessageOk() (*string, bool)`

GetErrorMessageOk returns a tuple with the ErrorMessage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetErrorMessage

`func (o *ForbiddenMeta) SetErrorMessage(v string)`

SetErrorMessage sets ErrorMessage field to given value.

### HasErrorMessage

`func (o *ForbiddenMeta) HasErrorMessage() bool`

HasErrorMessage returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


