# DefinitionTransitions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**EndStage** | Pointer to **NullableString** | [Read-Only] The landing stage that is active after performing a transition. | [optional] 
**Description** | Pointer to **NullableString** | [Read-Only] Description that matches the action dropdown that appears for PAC users. | [optional] 
**Roles** | Pointer to **[]interface{}** |  | [optional] 

## Methods

### NewDefinitionTransitions

`func NewDefinitionTransitions() *DefinitionTransitions`

NewDefinitionTransitions instantiates a new DefinitionTransitions object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewDefinitionTransitionsWithDefaults

`func NewDefinitionTransitionsWithDefaults() *DefinitionTransitions`

NewDefinitionTransitionsWithDefaults instantiates a new DefinitionTransitions object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetEndStage

`func (o *DefinitionTransitions) GetEndStage() string`

GetEndStage returns the EndStage field if non-nil, zero value otherwise.

### GetEndStageOk

`func (o *DefinitionTransitions) GetEndStageOk() (*string, bool)`

GetEndStageOk returns a tuple with the EndStage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEndStage

`func (o *DefinitionTransitions) SetEndStage(v string)`

SetEndStage sets EndStage field to given value.

### HasEndStage

`func (o *DefinitionTransitions) HasEndStage() bool`

HasEndStage returns a boolean if a field has been set.

### SetEndStageNil

`func (o *DefinitionTransitions) SetEndStageNil(b bool)`

 SetEndStageNil sets the value for EndStage to be an explicit nil

### UnsetEndStage
`func (o *DefinitionTransitions) UnsetEndStage()`

UnsetEndStage ensures that no value is present for EndStage, not even an explicit nil
### GetDescription

`func (o *DefinitionTransitions) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *DefinitionTransitions) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *DefinitionTransitions) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *DefinitionTransitions) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### SetDescriptionNil

`func (o *DefinitionTransitions) SetDescriptionNil(b bool)`

 SetDescriptionNil sets the value for Description to be an explicit nil

### UnsetDescription
`func (o *DefinitionTransitions) UnsetDescription()`

UnsetDescription ensures that no value is present for Description, not even an explicit nil
### GetRoles

`func (o *DefinitionTransitions) GetRoles() []interface{}`

GetRoles returns the Roles field if non-nil, zero value otherwise.

### GetRolesOk

`func (o *DefinitionTransitions) GetRolesOk() (*[]interface{}, bool)`

GetRolesOk returns a tuple with the Roles field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRoles

`func (o *DefinitionTransitions) SetRoles(v []interface{})`

SetRoles sets Roles field to given value.

### HasRoles

`func (o *DefinitionTransitions) HasRoles() bool`

HasRoles returns a boolean if a field has been set.

### SetRolesNil

`func (o *DefinitionTransitions) SetRolesNil(b bool)`

 SetRolesNil sets the value for Roles to be an explicit nil

### UnsetRoles
`func (o *DefinitionTransitions) UnsetRoles()`

UnsetRoles ensures that no value is present for Roles, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


