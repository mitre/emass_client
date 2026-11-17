# SystemRolesCategoryResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Meta** | Pointer to [**Response200**](Response200.md) |  | [optional] 
**Data** | Pointer to [**[]RoleCategory**](RoleCategory.md) |  | [optional] 

## Methods

### NewSystemRolesCategoryResponse

`func NewSystemRolesCategoryResponse() *SystemRolesCategoryResponse`

NewSystemRolesCategoryResponse instantiates a new SystemRolesCategoryResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSystemRolesCategoryResponseWithDefaults

`func NewSystemRolesCategoryResponseWithDefaults() *SystemRolesCategoryResponse`

NewSystemRolesCategoryResponseWithDefaults instantiates a new SystemRolesCategoryResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetMeta

`func (o *SystemRolesCategoryResponse) GetMeta() Response200`

GetMeta returns the Meta field if non-nil, zero value otherwise.

### GetMetaOk

`func (o *SystemRolesCategoryResponse) GetMetaOk() (*Response200, bool)`

GetMetaOk returns a tuple with the Meta field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMeta

`func (o *SystemRolesCategoryResponse) SetMeta(v Response200)`

SetMeta sets Meta field to given value.

### HasMeta

`func (o *SystemRolesCategoryResponse) HasMeta() bool`

HasMeta returns a boolean if a field has been set.

### GetData

`func (o *SystemRolesCategoryResponse) GetData() []RoleCategory`

GetData returns the Data field if non-nil, zero value otherwise.

### GetDataOk

`func (o *SystemRolesCategoryResponse) GetDataOk() (*[]RoleCategory, bool)`

GetDataOk returns a tuple with the Data field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetData

`func (o *SystemRolesCategoryResponse) SetData(v []RoleCategory)`

SetData sets Data field to given value.

### HasData

`func (o *SystemRolesCategoryResponse) HasData() bool`

HasData returns a boolean if a field has been set.

### SetDataNil

`func (o *SystemRolesCategoryResponse) SetDataNil(b bool)`

 SetDataNil sets the value for Data to be an explicit nil

### UnsetData
`func (o *SystemRolesCategoryResponse) UnsetData()`

UnsetData ensures that no value is present for Data, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


