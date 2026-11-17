# RoleCategory

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**SystemId** | Pointer to **int64** | [Read-only] Unique system record identifier. | [optional] 
**SystemName** | Pointer to **NullableString** | [Read-only] Name of the system record. | [optional] 
**SystemAcronym** | Pointer to **NullableString** | [Read-only] Acronym of the system record. | [optional] 
**Roles** | Pointer to [**[]Roles**](Roles.md) |  | [optional] 

## Methods

### NewRoleCategory

`func NewRoleCategory() *RoleCategory`

NewRoleCategory instantiates a new RoleCategory object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewRoleCategoryWithDefaults

`func NewRoleCategoryWithDefaults() *RoleCategory`

NewRoleCategoryWithDefaults instantiates a new RoleCategory object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetSystemId

`func (o *RoleCategory) GetSystemId() int64`

GetSystemId returns the SystemId field if non-nil, zero value otherwise.

### GetSystemIdOk

`func (o *RoleCategory) GetSystemIdOk() (*int64, bool)`

GetSystemIdOk returns a tuple with the SystemId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSystemId

`func (o *RoleCategory) SetSystemId(v int64)`

SetSystemId sets SystemId field to given value.

### HasSystemId

`func (o *RoleCategory) HasSystemId() bool`

HasSystemId returns a boolean if a field has been set.

### GetSystemName

`func (o *RoleCategory) GetSystemName() string`

GetSystemName returns the SystemName field if non-nil, zero value otherwise.

### GetSystemNameOk

`func (o *RoleCategory) GetSystemNameOk() (*string, bool)`

GetSystemNameOk returns a tuple with the SystemName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSystemName

`func (o *RoleCategory) SetSystemName(v string)`

SetSystemName sets SystemName field to given value.

### HasSystemName

`func (o *RoleCategory) HasSystemName() bool`

HasSystemName returns a boolean if a field has been set.

### SetSystemNameNil

`func (o *RoleCategory) SetSystemNameNil(b bool)`

 SetSystemNameNil sets the value for SystemName to be an explicit nil

### UnsetSystemName
`func (o *RoleCategory) UnsetSystemName()`

UnsetSystemName ensures that no value is present for SystemName, not even an explicit nil
### GetSystemAcronym

`func (o *RoleCategory) GetSystemAcronym() string`

GetSystemAcronym returns the SystemAcronym field if non-nil, zero value otherwise.

### GetSystemAcronymOk

`func (o *RoleCategory) GetSystemAcronymOk() (*string, bool)`

GetSystemAcronymOk returns a tuple with the SystemAcronym field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSystemAcronym

`func (o *RoleCategory) SetSystemAcronym(v string)`

SetSystemAcronym sets SystemAcronym field to given value.

### HasSystemAcronym

`func (o *RoleCategory) HasSystemAcronym() bool`

HasSystemAcronym returns a boolean if a field has been set.

### SetSystemAcronymNil

`func (o *RoleCategory) SetSystemAcronymNil(b bool)`

 SetSystemAcronymNil sets the value for SystemAcronym to be an explicit nil

### UnsetSystemAcronym
`func (o *RoleCategory) UnsetSystemAcronym()`

UnsetSystemAcronym ensures that no value is present for SystemAcronym, not even an explicit nil
### GetRoles

`func (o *RoleCategory) GetRoles() []Roles`

GetRoles returns the Roles field if non-nil, zero value otherwise.

### GetRolesOk

`func (o *RoleCategory) GetRolesOk() (*[]Roles, bool)`

GetRolesOk returns a tuple with the Roles field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRoles

`func (o *RoleCategory) SetRoles(v []Roles)`

SetRoles sets Roles field to given value.

### HasRoles

`func (o *RoleCategory) HasRoles() bool`

HasRoles returns a boolean if a field has been set.

### SetRolesNil

`func (o *RoleCategory) SetRolesNil(b bool)`

 SetRolesNil sets the value for Roles to be an explicit nil

### UnsetRoles
`func (o *RoleCategory) UnsetRoles()`

UnsetRoles ensures that no value is present for Roles, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


