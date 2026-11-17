# PacResponseGet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Meta** | Pointer to [**Response200**](Response200.md) |  | [optional] 
**Data** | Pointer to [**[]PacGet**](PacGet.md) |  | [optional] 

## Methods

### NewPacResponseGet

`func NewPacResponseGet() *PacResponseGet`

NewPacResponseGet instantiates a new PacResponseGet object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPacResponseGetWithDefaults

`func NewPacResponseGetWithDefaults() *PacResponseGet`

NewPacResponseGetWithDefaults instantiates a new PacResponseGet object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetMeta

`func (o *PacResponseGet) GetMeta() Response200`

GetMeta returns the Meta field if non-nil, zero value otherwise.

### GetMetaOk

`func (o *PacResponseGet) GetMetaOk() (*Response200, bool)`

GetMetaOk returns a tuple with the Meta field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMeta

`func (o *PacResponseGet) SetMeta(v Response200)`

SetMeta sets Meta field to given value.

### HasMeta

`func (o *PacResponseGet) HasMeta() bool`

HasMeta returns a boolean if a field has been set.

### GetData

`func (o *PacResponseGet) GetData() []PacGet`

GetData returns the Data field if non-nil, zero value otherwise.

### GetDataOk

`func (o *PacResponseGet) GetDataOk() (*[]PacGet, bool)`

GetDataOk returns a tuple with the Data field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetData

`func (o *PacResponseGet) SetData(v []PacGet)`

SetData sets Data field to given value.

### HasData

`func (o *PacResponseGet) HasData() bool`

HasData returns a boolean if a field has been set.

### SetDataNil

`func (o *PacResponseGet) SetDataNil(b bool)`

 SetDataNil sets the value for Data to be an explicit nil

### UnsetData
`func (o *PacResponseGet) UnsetData()`

UnsetData ensures that no value is present for Data, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


