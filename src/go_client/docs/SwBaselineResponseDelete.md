# SwBaselineResponseDelete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Meta** | Pointer to [**Response200**](Response200.md) |  | [optional] 
**Data** | Pointer to [**[]SwBaselineResponseDeleteDataInner**](SwBaselineResponseDeleteDataInner.md) |  | [optional] 

## Methods

### NewSwBaselineResponseDelete

`func NewSwBaselineResponseDelete() *SwBaselineResponseDelete`

NewSwBaselineResponseDelete instantiates a new SwBaselineResponseDelete object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSwBaselineResponseDeleteWithDefaults

`func NewSwBaselineResponseDeleteWithDefaults() *SwBaselineResponseDelete`

NewSwBaselineResponseDeleteWithDefaults instantiates a new SwBaselineResponseDelete object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetMeta

`func (o *SwBaselineResponseDelete) GetMeta() Response200`

GetMeta returns the Meta field if non-nil, zero value otherwise.

### GetMetaOk

`func (o *SwBaselineResponseDelete) GetMetaOk() (*Response200, bool)`

GetMetaOk returns a tuple with the Meta field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMeta

`func (o *SwBaselineResponseDelete) SetMeta(v Response200)`

SetMeta sets Meta field to given value.

### HasMeta

`func (o *SwBaselineResponseDelete) HasMeta() bool`

HasMeta returns a boolean if a field has been set.

### GetData

`func (o *SwBaselineResponseDelete) GetData() []SwBaselineResponseDeleteDataInner`

GetData returns the Data field if non-nil, zero value otherwise.

### GetDataOk

`func (o *SwBaselineResponseDelete) GetDataOk() (*[]SwBaselineResponseDeleteDataInner, bool)`

GetDataOk returns a tuple with the Data field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetData

`func (o *SwBaselineResponseDelete) SetData(v []SwBaselineResponseDeleteDataInner)`

SetData sets Data field to given value.

### HasData

`func (o *SwBaselineResponseDelete) HasData() bool`

HasData returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


