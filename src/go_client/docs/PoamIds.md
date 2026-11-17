# PoamIds

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**SystemId** | Pointer to **int64** | [Required] Unique eMASS system identifier. | [optional] 
**PoamId** | Pointer to **int64** | [Required] Unique item identifier | [optional] 
**DisplayPoamId** | Pointer to **int64** | [Required] Globally unique identifier for individual POA&amp;M Items, seen on the front-end as ID. | [optional] 

## Methods

### NewPoamIds

`func NewPoamIds() *PoamIds`

NewPoamIds instantiates a new PoamIds object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPoamIdsWithDefaults

`func NewPoamIdsWithDefaults() *PoamIds`

NewPoamIdsWithDefaults instantiates a new PoamIds object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetSystemId

`func (o *PoamIds) GetSystemId() int64`

GetSystemId returns the SystemId field if non-nil, zero value otherwise.

### GetSystemIdOk

`func (o *PoamIds) GetSystemIdOk() (*int64, bool)`

GetSystemIdOk returns a tuple with the SystemId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSystemId

`func (o *PoamIds) SetSystemId(v int64)`

SetSystemId sets SystemId field to given value.

### HasSystemId

`func (o *PoamIds) HasSystemId() bool`

HasSystemId returns a boolean if a field has been set.

### GetPoamId

`func (o *PoamIds) GetPoamId() int64`

GetPoamId returns the PoamId field if non-nil, zero value otherwise.

### GetPoamIdOk

`func (o *PoamIds) GetPoamIdOk() (*int64, bool)`

GetPoamIdOk returns a tuple with the PoamId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPoamId

`func (o *PoamIds) SetPoamId(v int64)`

SetPoamId sets PoamId field to given value.

### HasPoamId

`func (o *PoamIds) HasPoamId() bool`

HasPoamId returns a boolean if a field has been set.

### GetDisplayPoamId

`func (o *PoamIds) GetDisplayPoamId() int64`

GetDisplayPoamId returns the DisplayPoamId field if non-nil, zero value otherwise.

### GetDisplayPoamIdOk

`func (o *PoamIds) GetDisplayPoamIdOk() (*int64, bool)`

GetDisplayPoamIdOk returns a tuple with the DisplayPoamId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDisplayPoamId

`func (o *PoamIds) SetDisplayPoamId(v int64)`

SetDisplayPoamId sets DisplayPoamId field to given value.

### HasDisplayPoamId

`func (o *PoamIds) HasDisplayPoamId() bool`

HasDisplayPoamId returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


