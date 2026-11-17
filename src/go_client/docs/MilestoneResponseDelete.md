# MilestoneResponseDelete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Meta** | Pointer to [**Response200**](Response200.md) |  | [optional] 
**Data** | Pointer to [**[]MilestonesPutPostDelete**](MilestonesPutPostDelete.md) |  | [optional] 

## Methods

### NewMilestoneResponseDelete

`func NewMilestoneResponseDelete() *MilestoneResponseDelete`

NewMilestoneResponseDelete instantiates a new MilestoneResponseDelete object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewMilestoneResponseDeleteWithDefaults

`func NewMilestoneResponseDeleteWithDefaults() *MilestoneResponseDelete`

NewMilestoneResponseDeleteWithDefaults instantiates a new MilestoneResponseDelete object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetMeta

`func (o *MilestoneResponseDelete) GetMeta() Response200`

GetMeta returns the Meta field if non-nil, zero value otherwise.

### GetMetaOk

`func (o *MilestoneResponseDelete) GetMetaOk() (*Response200, bool)`

GetMetaOk returns a tuple with the Meta field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMeta

`func (o *MilestoneResponseDelete) SetMeta(v Response200)`

SetMeta sets Meta field to given value.

### HasMeta

`func (o *MilestoneResponseDelete) HasMeta() bool`

HasMeta returns a boolean if a field has been set.

### GetData

`func (o *MilestoneResponseDelete) GetData() []MilestonesPutPostDelete`

GetData returns the Data field if non-nil, zero value otherwise.

### GetDataOk

`func (o *MilestoneResponseDelete) GetDataOk() (*[]MilestonesPutPostDelete, bool)`

GetDataOk returns a tuple with the Data field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetData

`func (o *MilestoneResponseDelete) SetData(v []MilestonesPutPostDelete)`

SetData sets Data field to given value.

### HasData

`func (o *MilestoneResponseDelete) HasData() bool`

HasData returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


