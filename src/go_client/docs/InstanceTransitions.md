# InstanceTransitions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Comments** | Pointer to **NullableString** | [Read-Only] Comments entered by the user when performing the transition. | [optional] 
**CreatedBy** | Pointer to **NullableString** | [Read-Only] User that performed the workflow transition. | [optional] 
**CreatedDate** | Pointer to **NullableInt64** | [Read-Only] Date the workflow instance or the workflow transition was created. | [optional] 
**Description** | Pointer to **NullableString** | [Read-Only] Description of the stage transition. This matches the action dropdown that appears for PAC users. | [optional] 
**EndStage** | Pointer to **NullableString** | [Read-Only] The landing stage that is active after performing a transition. | [optional] 
**StartStage** | Pointer to **NullableString** | [Read-Only] The beginning stage that is active before performing a transition. | [optional] 

## Methods

### NewInstanceTransitions

`func NewInstanceTransitions() *InstanceTransitions`

NewInstanceTransitions instantiates a new InstanceTransitions object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewInstanceTransitionsWithDefaults

`func NewInstanceTransitionsWithDefaults() *InstanceTransitions`

NewInstanceTransitionsWithDefaults instantiates a new InstanceTransitions object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetComments

`func (o *InstanceTransitions) GetComments() string`

GetComments returns the Comments field if non-nil, zero value otherwise.

### GetCommentsOk

`func (o *InstanceTransitions) GetCommentsOk() (*string, bool)`

GetCommentsOk returns a tuple with the Comments field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetComments

`func (o *InstanceTransitions) SetComments(v string)`

SetComments sets Comments field to given value.

### HasComments

`func (o *InstanceTransitions) HasComments() bool`

HasComments returns a boolean if a field has been set.

### SetCommentsNil

`func (o *InstanceTransitions) SetCommentsNil(b bool)`

 SetCommentsNil sets the value for Comments to be an explicit nil

### UnsetComments
`func (o *InstanceTransitions) UnsetComments()`

UnsetComments ensures that no value is present for Comments, not even an explicit nil
### GetCreatedBy

`func (o *InstanceTransitions) GetCreatedBy() string`

GetCreatedBy returns the CreatedBy field if non-nil, zero value otherwise.

### GetCreatedByOk

`func (o *InstanceTransitions) GetCreatedByOk() (*string, bool)`

GetCreatedByOk returns a tuple with the CreatedBy field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedBy

`func (o *InstanceTransitions) SetCreatedBy(v string)`

SetCreatedBy sets CreatedBy field to given value.

### HasCreatedBy

`func (o *InstanceTransitions) HasCreatedBy() bool`

HasCreatedBy returns a boolean if a field has been set.

### SetCreatedByNil

`func (o *InstanceTransitions) SetCreatedByNil(b bool)`

 SetCreatedByNil sets the value for CreatedBy to be an explicit nil

### UnsetCreatedBy
`func (o *InstanceTransitions) UnsetCreatedBy()`

UnsetCreatedBy ensures that no value is present for CreatedBy, not even an explicit nil
### GetCreatedDate

`func (o *InstanceTransitions) GetCreatedDate() int64`

GetCreatedDate returns the CreatedDate field if non-nil, zero value otherwise.

### GetCreatedDateOk

`func (o *InstanceTransitions) GetCreatedDateOk() (*int64, bool)`

GetCreatedDateOk returns a tuple with the CreatedDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedDate

`func (o *InstanceTransitions) SetCreatedDate(v int64)`

SetCreatedDate sets CreatedDate field to given value.

### HasCreatedDate

`func (o *InstanceTransitions) HasCreatedDate() bool`

HasCreatedDate returns a boolean if a field has been set.

### SetCreatedDateNil

`func (o *InstanceTransitions) SetCreatedDateNil(b bool)`

 SetCreatedDateNil sets the value for CreatedDate to be an explicit nil

### UnsetCreatedDate
`func (o *InstanceTransitions) UnsetCreatedDate()`

UnsetCreatedDate ensures that no value is present for CreatedDate, not even an explicit nil
### GetDescription

`func (o *InstanceTransitions) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *InstanceTransitions) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *InstanceTransitions) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *InstanceTransitions) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### SetDescriptionNil

`func (o *InstanceTransitions) SetDescriptionNil(b bool)`

 SetDescriptionNil sets the value for Description to be an explicit nil

### UnsetDescription
`func (o *InstanceTransitions) UnsetDescription()`

UnsetDescription ensures that no value is present for Description, not even an explicit nil
### GetEndStage

`func (o *InstanceTransitions) GetEndStage() string`

GetEndStage returns the EndStage field if non-nil, zero value otherwise.

### GetEndStageOk

`func (o *InstanceTransitions) GetEndStageOk() (*string, bool)`

GetEndStageOk returns a tuple with the EndStage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEndStage

`func (o *InstanceTransitions) SetEndStage(v string)`

SetEndStage sets EndStage field to given value.

### HasEndStage

`func (o *InstanceTransitions) HasEndStage() bool`

HasEndStage returns a boolean if a field has been set.

### SetEndStageNil

`func (o *InstanceTransitions) SetEndStageNil(b bool)`

 SetEndStageNil sets the value for EndStage to be an explicit nil

### UnsetEndStage
`func (o *InstanceTransitions) UnsetEndStage()`

UnsetEndStage ensures that no value is present for EndStage, not even an explicit nil
### GetStartStage

`func (o *InstanceTransitions) GetStartStage() string`

GetStartStage returns the StartStage field if non-nil, zero value otherwise.

### GetStartStageOk

`func (o *InstanceTransitions) GetStartStageOk() (*string, bool)`

GetStartStageOk returns a tuple with the StartStage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStartStage

`func (o *InstanceTransitions) SetStartStage(v string)`

SetStartStage sets StartStage field to given value.

### HasStartStage

`func (o *InstanceTransitions) HasStartStage() bool`

HasStartStage returns a boolean if a field has been set.

### SetStartStageNil

`func (o *InstanceTransitions) SetStartStageNil(b bool)`

 SetStartStageNil sets the value for StartStage to be an explicit nil

### UnsetStartStage
`func (o *InstanceTransitions) UnsetStartStage()`

UnsetStartStage ensures that no value is present for StartStage, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


