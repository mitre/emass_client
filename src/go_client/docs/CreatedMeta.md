# CreatedMeta

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Code** | Pointer to **int32** |  | [optional] [default to 201]
**Message** | Pointer to **string** |  | [optional] [default to "Request was fulfilled and resulted in on or more new resources being successfully created on the server."]

## Methods

### NewCreatedMeta

`func NewCreatedMeta() *CreatedMeta`

NewCreatedMeta instantiates a new CreatedMeta object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCreatedMetaWithDefaults

`func NewCreatedMetaWithDefaults() *CreatedMeta`

NewCreatedMetaWithDefaults instantiates a new CreatedMeta object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCode

`func (o *CreatedMeta) GetCode() int32`

GetCode returns the Code field if non-nil, zero value otherwise.

### GetCodeOk

`func (o *CreatedMeta) GetCodeOk() (*int32, bool)`

GetCodeOk returns a tuple with the Code field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCode

`func (o *CreatedMeta) SetCode(v int32)`

SetCode sets Code field to given value.

### HasCode

`func (o *CreatedMeta) HasCode() bool`

HasCode returns a boolean if a field has been set.

### GetMessage

`func (o *CreatedMeta) GetMessage() string`

GetMessage returns the Message field if non-nil, zero value otherwise.

### GetMessageOk

`func (o *CreatedMeta) GetMessageOk() (*string, bool)`

GetMessageOk returns a tuple with the Message field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMessage

`func (o *CreatedMeta) SetMessage(v string)`

SetMessage sets Message field to given value.

### HasMessage

`func (o *CreatedMeta) HasMessage() bool`

HasMessage returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


