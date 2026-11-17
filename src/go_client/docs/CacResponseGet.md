# CacResponseGet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Meta** | Pointer to [**Response200**](Response200.md) |  | [optional] 
**Data** | Pointer to [**[]CacGet**](CacGet.md) |  | [optional] 

## Methods

### NewCacResponseGet

`func NewCacResponseGet() *CacResponseGet`

NewCacResponseGet instantiates a new CacResponseGet object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCacResponseGetWithDefaults

`func NewCacResponseGetWithDefaults() *CacResponseGet`

NewCacResponseGetWithDefaults instantiates a new CacResponseGet object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetMeta

`func (o *CacResponseGet) GetMeta() Response200`

GetMeta returns the Meta field if non-nil, zero value otherwise.

### GetMetaOk

`func (o *CacResponseGet) GetMetaOk() (*Response200, bool)`

GetMetaOk returns a tuple with the Meta field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMeta

`func (o *CacResponseGet) SetMeta(v Response200)`

SetMeta sets Meta field to given value.

### HasMeta

`func (o *CacResponseGet) HasMeta() bool`

HasMeta returns a boolean if a field has been set.

### GetData

`func (o *CacResponseGet) GetData() []CacGet`

GetData returns the Data field if non-nil, zero value otherwise.

### GetDataOk

`func (o *CacResponseGet) GetDataOk() (*[]CacGet, bool)`

GetDataOk returns a tuple with the Data field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetData

`func (o *CacResponseGet) SetData(v []CacGet)`

SetData sets Data field to given value.

### HasData

`func (o *CacResponseGet) HasData() bool`

HasData returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


