# SystemsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Meta** | Pointer to [**Response200**](Response200.md) |  | [optional] 
**Data** | Pointer to [**[]Systems**](Systems.md) |  | [optional] 

## Methods

### NewSystemsResponse

`func NewSystemsResponse() *SystemsResponse`

NewSystemsResponse instantiates a new SystemsResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSystemsResponseWithDefaults

`func NewSystemsResponseWithDefaults() *SystemsResponse`

NewSystemsResponseWithDefaults instantiates a new SystemsResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetMeta

`func (o *SystemsResponse) GetMeta() Response200`

GetMeta returns the Meta field if non-nil, zero value otherwise.

### GetMetaOk

`func (o *SystemsResponse) GetMetaOk() (*Response200, bool)`

GetMetaOk returns a tuple with the Meta field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMeta

`func (o *SystemsResponse) SetMeta(v Response200)`

SetMeta sets Meta field to given value.

### HasMeta

`func (o *SystemsResponse) HasMeta() bool`

HasMeta returns a boolean if a field has been set.

### GetData

`func (o *SystemsResponse) GetData() []Systems`

GetData returns the Data field if non-nil, zero value otherwise.

### GetDataOk

`func (o *SystemsResponse) GetDataOk() (*[]Systems, bool)`

GetDataOk returns a tuple with the Data field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetData

`func (o *SystemsResponse) SetData(v []Systems)`

SetData sets Data field to given value.

### HasData

`func (o *SystemsResponse) HasData() bool`

HasData returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


