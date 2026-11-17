# SystemRolesResponseDataInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**RoleCategory** | Pointer to **string** |  | [optional] [default to "PAC"]
**Role** | Pointer to **string** |  | [optional] [default to "PM/IAM"]

## Methods

### NewSystemRolesResponseDataInner

`func NewSystemRolesResponseDataInner() *SystemRolesResponseDataInner`

NewSystemRolesResponseDataInner instantiates a new SystemRolesResponseDataInner object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSystemRolesResponseDataInnerWithDefaults

`func NewSystemRolesResponseDataInnerWithDefaults() *SystemRolesResponseDataInner`

NewSystemRolesResponseDataInnerWithDefaults instantiates a new SystemRolesResponseDataInner object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetRoleCategory

`func (o *SystemRolesResponseDataInner) GetRoleCategory() string`

GetRoleCategory returns the RoleCategory field if non-nil, zero value otherwise.

### GetRoleCategoryOk

`func (o *SystemRolesResponseDataInner) GetRoleCategoryOk() (*string, bool)`

GetRoleCategoryOk returns a tuple with the RoleCategory field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRoleCategory

`func (o *SystemRolesResponseDataInner) SetRoleCategory(v string)`

SetRoleCategory sets RoleCategory field to given value.

### HasRoleCategory

`func (o *SystemRolesResponseDataInner) HasRoleCategory() bool`

HasRoleCategory returns a boolean if a field has been set.

### GetRole

`func (o *SystemRolesResponseDataInner) GetRole() string`

GetRole returns the Role field if non-nil, zero value otherwise.

### GetRoleOk

`func (o *SystemRolesResponseDataInner) GetRoleOk() (*string, bool)`

GetRoleOk returns a tuple with the Role field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRole

`func (o *SystemRolesResponseDataInner) SetRole(v string)`

SetRole sets Role field to given value.

### HasRole

`func (o *SystemRolesResponseDataInner) HasRole() bool`

HasRole returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


