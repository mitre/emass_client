# GetSystemStatusDetails200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Meta** | Pointer to [**Response200**](Response200.md) |  | [optional] 
**Data** | Pointer to **[]map[string]interface{}** |  | [optional] 
**Pagination** | Pointer to [**Pagination**](Pagination.md) |  | [optional] 

## Methods

### NewGetSystemStatusDetails200Response

`func NewGetSystemStatusDetails200Response() *GetSystemStatusDetails200Response`

NewGetSystemStatusDetails200Response instantiates a new GetSystemStatusDetails200Response object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewGetSystemStatusDetails200ResponseWithDefaults

`func NewGetSystemStatusDetails200ResponseWithDefaults() *GetSystemStatusDetails200Response`

NewGetSystemStatusDetails200ResponseWithDefaults instantiates a new GetSystemStatusDetails200Response object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetMeta

`func (o *GetSystemStatusDetails200Response) GetMeta() Response200`

GetMeta returns the Meta field if non-nil, zero value otherwise.

### GetMetaOk

`func (o *GetSystemStatusDetails200Response) GetMetaOk() (*Response200, bool)`

GetMetaOk returns a tuple with the Meta field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMeta

`func (o *GetSystemStatusDetails200Response) SetMeta(v Response200)`

SetMeta sets Meta field to given value.

### HasMeta

`func (o *GetSystemStatusDetails200Response) HasMeta() bool`

HasMeta returns a boolean if a field has been set.

### GetData

`func (o *GetSystemStatusDetails200Response) GetData() []map[string]interface{}`

GetData returns the Data field if non-nil, zero value otherwise.

### GetDataOk

`func (o *GetSystemStatusDetails200Response) GetDataOk() (*[]map[string]interface{}, bool)`

GetDataOk returns a tuple with the Data field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetData

`func (o *GetSystemStatusDetails200Response) SetData(v []map[string]interface{})`

SetData sets Data field to given value.

### HasData

`func (o *GetSystemStatusDetails200Response) HasData() bool`

HasData returns a boolean if a field has been set.

### GetPagination

`func (o *GetSystemStatusDetails200Response) GetPagination() Pagination`

GetPagination returns the Pagination field if non-nil, zero value otherwise.

### GetPaginationOk

`func (o *GetSystemStatusDetails200Response) GetPaginationOk() (*Pagination, bool)`

GetPaginationOk returns a tuple with the Pagination field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPagination

`func (o *GetSystemStatusDetails200Response) SetPagination(v Pagination)`

SetPagination sets Pagination field to given value.

### HasPagination

`func (o *GetSystemStatusDetails200Response) HasPagination() bool`

HasPagination returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


