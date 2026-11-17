# WorkflowInstancesResponseGet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Meta** | Pointer to [**Response200**](Response200.md) |  | [optional] 
**Data** | Pointer to [**[]WorkflowInstanceGet**](WorkflowInstanceGet.md) |  | [optional] 
**Pagination** | Pointer to [**WorkflowInstancesResponseGetPagination**](WorkflowInstancesResponseGetPagination.md) |  | [optional] 

## Methods

### NewWorkflowInstancesResponseGet

`func NewWorkflowInstancesResponseGet() *WorkflowInstancesResponseGet`

NewWorkflowInstancesResponseGet instantiates a new WorkflowInstancesResponseGet object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewWorkflowInstancesResponseGetWithDefaults

`func NewWorkflowInstancesResponseGetWithDefaults() *WorkflowInstancesResponseGet`

NewWorkflowInstancesResponseGetWithDefaults instantiates a new WorkflowInstancesResponseGet object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetMeta

`func (o *WorkflowInstancesResponseGet) GetMeta() Response200`

GetMeta returns the Meta field if non-nil, zero value otherwise.

### GetMetaOk

`func (o *WorkflowInstancesResponseGet) GetMetaOk() (*Response200, bool)`

GetMetaOk returns a tuple with the Meta field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMeta

`func (o *WorkflowInstancesResponseGet) SetMeta(v Response200)`

SetMeta sets Meta field to given value.

### HasMeta

`func (o *WorkflowInstancesResponseGet) HasMeta() bool`

HasMeta returns a boolean if a field has been set.

### GetData

`func (o *WorkflowInstancesResponseGet) GetData() []WorkflowInstanceGet`

GetData returns the Data field if non-nil, zero value otherwise.

### GetDataOk

`func (o *WorkflowInstancesResponseGet) GetDataOk() (*[]WorkflowInstanceGet, bool)`

GetDataOk returns a tuple with the Data field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetData

`func (o *WorkflowInstancesResponseGet) SetData(v []WorkflowInstanceGet)`

SetData sets Data field to given value.

### HasData

`func (o *WorkflowInstancesResponseGet) HasData() bool`

HasData returns a boolean if a field has been set.

### GetPagination

`func (o *WorkflowInstancesResponseGet) GetPagination() WorkflowInstancesResponseGetPagination`

GetPagination returns the Pagination field if non-nil, zero value otherwise.

### GetPaginationOk

`func (o *WorkflowInstancesResponseGet) GetPaginationOk() (*WorkflowInstancesResponseGetPagination, bool)`

GetPaginationOk returns a tuple with the Pagination field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPagination

`func (o *WorkflowInstancesResponseGet) SetPagination(v WorkflowInstancesResponseGetPagination)`

SetPagination sets Pagination field to given value.

### HasPagination

`func (o *WorkflowInstancesResponseGet) HasPagination() bool`

HasPagination returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


