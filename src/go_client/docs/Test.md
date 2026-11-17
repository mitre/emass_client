# Test

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Meta** | Pointer to [**Response200**](Response200.md) |  | [optional] 
**Data** | Pointer to [**TestData**](TestData.md) |  | [optional] 

## Methods

### NewTest

`func NewTest() *Test`

NewTest instantiates a new Test object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewTestWithDefaults

`func NewTestWithDefaults() *Test`

NewTestWithDefaults instantiates a new Test object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetMeta

`func (o *Test) GetMeta() Response200`

GetMeta returns the Meta field if non-nil, zero value otherwise.

### GetMetaOk

`func (o *Test) GetMetaOk() (*Response200, bool)`

GetMetaOk returns a tuple with the Meta field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMeta

`func (o *Test) SetMeta(v Response200)`

SetMeta sets Meta field to given value.

### HasMeta

`func (o *Test) HasMeta() bool`

HasMeta returns a boolean if a field has been set.

### GetData

`func (o *Test) GetData() TestData`

GetData returns the Data field if non-nil, zero value otherwise.

### GetDataOk

`func (o *Test) GetDataOk() (*TestData, bool)`

GetDataOk returns a tuple with the Data field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetData

`func (o *Test) SetData(v TestData)`

SetData sets Data field to given value.

### HasData

`func (o *Test) HasData() bool`

HasData returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


