# CmmcResponseGet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Meta** | Pointer to [**Response200**](Response200.md) |  | [optional] 
**Data** | Pointer to [**[]CmmcGet**](CmmcGet.md) |  | [optional] 

## Methods

### NewCmmcResponseGet

`func NewCmmcResponseGet() *CmmcResponseGet`

NewCmmcResponseGet instantiates a new CmmcResponseGet object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCmmcResponseGetWithDefaults

`func NewCmmcResponseGetWithDefaults() *CmmcResponseGet`

NewCmmcResponseGetWithDefaults instantiates a new CmmcResponseGet object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetMeta

`func (o *CmmcResponseGet) GetMeta() Response200`

GetMeta returns the Meta field if non-nil, zero value otherwise.

### GetMetaOk

`func (o *CmmcResponseGet) GetMetaOk() (*Response200, bool)`

GetMetaOk returns a tuple with the Meta field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMeta

`func (o *CmmcResponseGet) SetMeta(v Response200)`

SetMeta sets Meta field to given value.

### HasMeta

`func (o *CmmcResponseGet) HasMeta() bool`

HasMeta returns a boolean if a field has been set.

### GetData

`func (o *CmmcResponseGet) GetData() []CmmcGet`

GetData returns the Data field if non-nil, zero value otherwise.

### GetDataOk

`func (o *CmmcResponseGet) GetDataOk() (*[]CmmcGet, bool)`

GetDataOk returns a tuple with the Data field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetData

`func (o *CmmcResponseGet) SetData(v []CmmcGet)`

SetData sets Data field to given value.

### HasData

`func (o *CmmcResponseGet) HasData() bool`

HasData returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


