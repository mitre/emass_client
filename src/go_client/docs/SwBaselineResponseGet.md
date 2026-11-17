# SwBaselineResponseGet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Meta** | Pointer to [**Response200**](Response200.md) |  | [optional] 
**Data** | Pointer to [**[]SwBaselineResponseGetDataInner**](SwBaselineResponseGetDataInner.md) |  | [optional] 
**Pagination** | Pointer to [**Pagination**](Pagination.md) |  | [optional] 

## Methods

### NewSwBaselineResponseGet

`func NewSwBaselineResponseGet() *SwBaselineResponseGet`

NewSwBaselineResponseGet instantiates a new SwBaselineResponseGet object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSwBaselineResponseGetWithDefaults

`func NewSwBaselineResponseGetWithDefaults() *SwBaselineResponseGet`

NewSwBaselineResponseGetWithDefaults instantiates a new SwBaselineResponseGet object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetMeta

`func (o *SwBaselineResponseGet) GetMeta() Response200`

GetMeta returns the Meta field if non-nil, zero value otherwise.

### GetMetaOk

`func (o *SwBaselineResponseGet) GetMetaOk() (*Response200, bool)`

GetMetaOk returns a tuple with the Meta field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMeta

`func (o *SwBaselineResponseGet) SetMeta(v Response200)`

SetMeta sets Meta field to given value.

### HasMeta

`func (o *SwBaselineResponseGet) HasMeta() bool`

HasMeta returns a boolean if a field has been set.

### GetData

`func (o *SwBaselineResponseGet) GetData() []SwBaselineResponseGetDataInner`

GetData returns the Data field if non-nil, zero value otherwise.

### GetDataOk

`func (o *SwBaselineResponseGet) GetDataOk() (*[]SwBaselineResponseGetDataInner, bool)`

GetDataOk returns a tuple with the Data field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetData

`func (o *SwBaselineResponseGet) SetData(v []SwBaselineResponseGetDataInner)`

SetData sets Data field to given value.

### HasData

`func (o *SwBaselineResponseGet) HasData() bool`

HasData returns a boolean if a field has been set.

### GetPagination

`func (o *SwBaselineResponseGet) GetPagination() Pagination`

GetPagination returns the Pagination field if non-nil, zero value otherwise.

### GetPaginationOk

`func (o *SwBaselineResponseGet) GetPaginationOk() (*Pagination, bool)`

GetPaginationOk returns a tuple with the Pagination field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPagination

`func (o *SwBaselineResponseGet) SetPagination(v Pagination)`

SetPagination sets Pagination field to given value.

### HasPagination

`func (o *SwBaselineResponseGet) HasPagination() bool`

HasPagination returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


