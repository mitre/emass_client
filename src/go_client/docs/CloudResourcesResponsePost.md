# CloudResourcesResponsePost

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Meta** | Pointer to [**Response200**](Response200.md) |  | [optional] 
**Data** | Pointer to [**[]CloudResourcesPostDelete**](CloudResourcesPostDelete.md) |  | [optional] 

## Methods

### NewCloudResourcesResponsePost

`func NewCloudResourcesResponsePost() *CloudResourcesResponsePost`

NewCloudResourcesResponsePost instantiates a new CloudResourcesResponsePost object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCloudResourcesResponsePostWithDefaults

`func NewCloudResourcesResponsePostWithDefaults() *CloudResourcesResponsePost`

NewCloudResourcesResponsePostWithDefaults instantiates a new CloudResourcesResponsePost object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetMeta

`func (o *CloudResourcesResponsePost) GetMeta() Response200`

GetMeta returns the Meta field if non-nil, zero value otherwise.

### GetMetaOk

`func (o *CloudResourcesResponsePost) GetMetaOk() (*Response200, bool)`

GetMetaOk returns a tuple with the Meta field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMeta

`func (o *CloudResourcesResponsePost) SetMeta(v Response200)`

SetMeta sets Meta field to given value.

### HasMeta

`func (o *CloudResourcesResponsePost) HasMeta() bool`

HasMeta returns a boolean if a field has been set.

### GetData

`func (o *CloudResourcesResponsePost) GetData() []CloudResourcesPostDelete`

GetData returns the Data field if non-nil, zero value otherwise.

### GetDataOk

`func (o *CloudResourcesResponsePost) GetDataOk() (*[]CloudResourcesPostDelete, bool)`

GetDataOk returns a tuple with the Data field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetData

`func (o *CloudResourcesResponsePost) SetData(v []CloudResourcesPostDelete)`

SetData sets Data field to given value.

### HasData

`func (o *CloudResourcesResponsePost) HasData() bool`

HasData returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


