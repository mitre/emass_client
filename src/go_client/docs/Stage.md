# Stage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | Pointer to **NullableString** | [Read-Only] Name of the stage. For older workflows, this will match the user assigned to the stage. | [optional] 
**Transitions** | Pointer to [**[]DefinitionTransitions**](DefinitionTransitions.md) |  | [optional] 

## Methods

### NewStage

`func NewStage() *Stage`

NewStage instantiates a new Stage object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewStageWithDefaults

`func NewStageWithDefaults() *Stage`

NewStageWithDefaults instantiates a new Stage object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *Stage) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *Stage) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *Stage) SetName(v string)`

SetName sets Name field to given value.

### HasName

`func (o *Stage) HasName() bool`

HasName returns a boolean if a field has been set.

### SetNameNil

`func (o *Stage) SetNameNil(b bool)`

 SetNameNil sets the value for Name to be an explicit nil

### UnsetName
`func (o *Stage) UnsetName()`

UnsetName ensures that no value is present for Name, not even an explicit nil
### GetTransitions

`func (o *Stage) GetTransitions() []DefinitionTransitions`

GetTransitions returns the Transitions field if non-nil, zero value otherwise.

### GetTransitionsOk

`func (o *Stage) GetTransitionsOk() (*[]DefinitionTransitions, bool)`

GetTransitionsOk returns a tuple with the Transitions field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTransitions

`func (o *Stage) SetTransitions(v []DefinitionTransitions)`

SetTransitions sets Transitions field to given value.

### HasTransitions

`func (o *Stage) HasTransitions() bool`

HasTransitions returns a boolean if a field has been set.

### SetTransitionsNil

`func (o *Stage) SetTransitionsNil(b bool)`

 SetTransitionsNil sets the value for Transitions to be an explicit nil

### UnsetTransitions
`func (o *Stage) UnsetTransitions()`

UnsetTransitions ensures that no value is present for Transitions, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


