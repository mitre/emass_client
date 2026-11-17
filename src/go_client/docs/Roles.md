# Roles

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**RoleCategory** | Pointer to **string** | [Required] System role categories | [optional] 
**Role** | Pointer to **string** | [Required] System role description | [optional] 
**Users** | Pointer to [**[]Users**](Users.md) |  | [optional] 

## Methods

### NewRoles

`func NewRoles() *Roles`

NewRoles instantiates a new Roles object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewRolesWithDefaults

`func NewRolesWithDefaults() *Roles`

NewRolesWithDefaults instantiates a new Roles object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetRoleCategory

`func (o *Roles) GetRoleCategory() string`

GetRoleCategory returns the RoleCategory field if non-nil, zero value otherwise.

### GetRoleCategoryOk

`func (o *Roles) GetRoleCategoryOk() (*string, bool)`

GetRoleCategoryOk returns a tuple with the RoleCategory field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRoleCategory

`func (o *Roles) SetRoleCategory(v string)`

SetRoleCategory sets RoleCategory field to given value.

### HasRoleCategory

`func (o *Roles) HasRoleCategory() bool`

HasRoleCategory returns a boolean if a field has been set.

### GetRole

`func (o *Roles) GetRole() string`

GetRole returns the Role field if non-nil, zero value otherwise.

### GetRoleOk

`func (o *Roles) GetRoleOk() (*string, bool)`

GetRoleOk returns a tuple with the Role field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRole

`func (o *Roles) SetRole(v string)`

SetRole sets Role field to given value.

### HasRole

`func (o *Roles) HasRole() bool`

HasRole returns a boolean if a field has been set.

### GetUsers

`func (o *Roles) GetUsers() []Users`

GetUsers returns the Users field if non-nil, zero value otherwise.

### GetUsersOk

`func (o *Roles) GetUsersOk() (*[]Users, bool)`

GetUsersOk returns a tuple with the Users field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUsers

`func (o *Roles) SetUsers(v []Users)`

SetUsers sets Users field to given value.

### HasUsers

`func (o *Roles) HasUsers() bool`

HasUsers returns a boolean if a field has been set.

### SetUsersNil

`func (o *Roles) SetUsersNil(b bool)`

 SetUsersNil sets the value for Users to be an explicit nil

### UnsetUsers
`func (o *Roles) UnsetUsers()`

UnsetUsers ensures that no value is present for Users, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


