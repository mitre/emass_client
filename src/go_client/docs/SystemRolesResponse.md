# SystemRolesResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Meta** | Pointer to [**Response200**](Response200.md) |  | [optional] 
**Data** | Pointer to [**[]SystemRolesResponseDataInner**](SystemRolesResponseDataInner.md) |  | [optional] 

## Methods

### NewSystemRolesResponse

`func NewSystemRolesResponse() *SystemRolesResponse`

NewSystemRolesResponse instantiates a new SystemRolesResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSystemRolesResponseWithDefaults

`func NewSystemRolesResponseWithDefaults() *SystemRolesResponse`

NewSystemRolesResponseWithDefaults instantiates a new SystemRolesResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetMeta

`func (o *SystemRolesResponse) GetMeta() Response200`

GetMeta returns the Meta field if non-nil, zero value otherwise.

### GetMetaOk

`func (o *SystemRolesResponse) GetMetaOk() (*Response200, bool)`

GetMetaOk returns a tuple with the Meta field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMeta

`func (o *SystemRolesResponse) SetMeta(v Response200)`

SetMeta sets Meta field to given value.

### HasMeta

`func (o *SystemRolesResponse) HasMeta() bool`

HasMeta returns a boolean if a field has been set.

### GetData

`func (o *SystemRolesResponse) GetData() []SystemRolesResponseDataInner`

GetData returns the Data field if non-nil, zero value otherwise.

### GetDataOk

`func (o *SystemRolesResponse) GetDataOk() (*[]SystemRolesResponseDataInner, bool)`

GetDataOk returns a tuple with the Data field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetData

`func (o *SystemRolesResponse) SetData(v []SystemRolesResponseDataInner)`

SetData sets Data field to given value.

### HasData

`func (o *SystemRolesResponse) HasData() bool`

HasData returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


