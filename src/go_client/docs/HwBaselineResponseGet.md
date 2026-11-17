# HwBaselineResponseGet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Meta** | Pointer to [**Response200**](Response200.md) |  | [optional] 
**Data** | Pointer to [**[]HwBaselineResponseGetDataInner**](HwBaselineResponseGetDataInner.md) |  | [optional] 
**Pagination** | Pointer to [**Pagination**](Pagination.md) |  | [optional] 

## Methods

### NewHwBaselineResponseGet

`func NewHwBaselineResponseGet() *HwBaselineResponseGet`

NewHwBaselineResponseGet instantiates a new HwBaselineResponseGet object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewHwBaselineResponseGetWithDefaults

`func NewHwBaselineResponseGetWithDefaults() *HwBaselineResponseGet`

NewHwBaselineResponseGetWithDefaults instantiates a new HwBaselineResponseGet object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetMeta

`func (o *HwBaselineResponseGet) GetMeta() Response200`

GetMeta returns the Meta field if non-nil, zero value otherwise.

### GetMetaOk

`func (o *HwBaselineResponseGet) GetMetaOk() (*Response200, bool)`

GetMetaOk returns a tuple with the Meta field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMeta

`func (o *HwBaselineResponseGet) SetMeta(v Response200)`

SetMeta sets Meta field to given value.

### HasMeta

`func (o *HwBaselineResponseGet) HasMeta() bool`

HasMeta returns a boolean if a field has been set.

### GetData

`func (o *HwBaselineResponseGet) GetData() []HwBaselineResponseGetDataInner`

GetData returns the Data field if non-nil, zero value otherwise.

### GetDataOk

`func (o *HwBaselineResponseGet) GetDataOk() (*[]HwBaselineResponseGetDataInner, bool)`

GetDataOk returns a tuple with the Data field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetData

`func (o *HwBaselineResponseGet) SetData(v []HwBaselineResponseGetDataInner)`

SetData sets Data field to given value.

### HasData

`func (o *HwBaselineResponseGet) HasData() bool`

HasData returns a boolean if a field has been set.

### GetPagination

`func (o *HwBaselineResponseGet) GetPagination() Pagination`

GetPagination returns the Pagination field if non-nil, zero value otherwise.

### GetPaginationOk

`func (o *HwBaselineResponseGet) GetPaginationOk() (*Pagination, bool)`

GetPaginationOk returns a tuple with the Pagination field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPagination

`func (o *HwBaselineResponseGet) SetPagination(v Pagination)`

SetPagination sets Pagination field to given value.

### HasPagination

`func (o *HwBaselineResponseGet) HasPagination() bool`

HasPagination returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


