# Register

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Meta** | Pointer to [**Response200**](Response200.md) |  | [optional] 
**Data** | Pointer to [**RegisterData**](RegisterData.md) |  | [optional] 

## Methods

### NewRegister

`func NewRegister() *Register`

NewRegister instantiates a new Register object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewRegisterWithDefaults

`func NewRegisterWithDefaults() *Register`

NewRegisterWithDefaults instantiates a new Register object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetMeta

`func (o *Register) GetMeta() Response200`

GetMeta returns the Meta field if non-nil, zero value otherwise.

### GetMetaOk

`func (o *Register) GetMetaOk() (*Response200, bool)`

GetMetaOk returns a tuple with the Meta field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMeta

`func (o *Register) SetMeta(v Response200)`

SetMeta sets Meta field to given value.

### HasMeta

`func (o *Register) HasMeta() bool`

HasMeta returns a boolean if a field has been set.

### GetData

`func (o *Register) GetData() RegisterData`

GetData returns the Data field if non-nil, zero value otherwise.

### GetDataOk

`func (o *Register) GetDataOk() (*RegisterData, bool)`

GetDataOk returns a tuple with the Data field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetData

`func (o *Register) SetData(v RegisterData)`

SetData sets Data field to given value.

### HasData

`func (o *Register) HasData() bool`

HasData returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


