# PacGet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Workflow** | Pointer to **string** | [Required] Values include the following:(Assess and Authorize, Assess Only, Security Plan Approval) | [optional] 
**Name** | Pointer to **string** | [Required] Package name. 100 Characters. | [optional] 
**CurrentStageName** | Pointer to **NullableString** | [Read-Only] Name of the current stage in the active workflow. | [optional] 
**CurrentStage** | Pointer to **NullableInt32** | [Read-Only] Number of the current stage in the active workflow. | [optional] 
**TotalStages** | Pointer to **NullableInt32** | [Read-Only] Total number of stages in the active workflow. | [optional] 
**DaysAtCurrentStage** | Pointer to **NullableInt32** | [Read-Only] Indicates the number of days at current workflow stage. | [optional] 
**Comments** | Pointer to **NullableString** | [Required]] Comments submitted upon initiation of the indicated workflow. Character Limit &#x3D; 4,000. | [optional] 

## Methods

### NewPacGet

`func NewPacGet() *PacGet`

NewPacGet instantiates a new PacGet object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPacGetWithDefaults

`func NewPacGetWithDefaults() *PacGet`

NewPacGetWithDefaults instantiates a new PacGet object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetWorkflow

`func (o *PacGet) GetWorkflow() string`

GetWorkflow returns the Workflow field if non-nil, zero value otherwise.

### GetWorkflowOk

`func (o *PacGet) GetWorkflowOk() (*string, bool)`

GetWorkflowOk returns a tuple with the Workflow field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWorkflow

`func (o *PacGet) SetWorkflow(v string)`

SetWorkflow sets Workflow field to given value.

### HasWorkflow

`func (o *PacGet) HasWorkflow() bool`

HasWorkflow returns a boolean if a field has been set.

### GetName

`func (o *PacGet) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *PacGet) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *PacGet) SetName(v string)`

SetName sets Name field to given value.

### HasName

`func (o *PacGet) HasName() bool`

HasName returns a boolean if a field has been set.

### GetCurrentStageName

`func (o *PacGet) GetCurrentStageName() string`

GetCurrentStageName returns the CurrentStageName field if non-nil, zero value otherwise.

### GetCurrentStageNameOk

`func (o *PacGet) GetCurrentStageNameOk() (*string, bool)`

GetCurrentStageNameOk returns a tuple with the CurrentStageName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCurrentStageName

`func (o *PacGet) SetCurrentStageName(v string)`

SetCurrentStageName sets CurrentStageName field to given value.

### HasCurrentStageName

`func (o *PacGet) HasCurrentStageName() bool`

HasCurrentStageName returns a boolean if a field has been set.

### SetCurrentStageNameNil

`func (o *PacGet) SetCurrentStageNameNil(b bool)`

 SetCurrentStageNameNil sets the value for CurrentStageName to be an explicit nil

### UnsetCurrentStageName
`func (o *PacGet) UnsetCurrentStageName()`

UnsetCurrentStageName ensures that no value is present for CurrentStageName, not even an explicit nil
### GetCurrentStage

`func (o *PacGet) GetCurrentStage() int32`

GetCurrentStage returns the CurrentStage field if non-nil, zero value otherwise.

### GetCurrentStageOk

`func (o *PacGet) GetCurrentStageOk() (*int32, bool)`

GetCurrentStageOk returns a tuple with the CurrentStage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCurrentStage

`func (o *PacGet) SetCurrentStage(v int32)`

SetCurrentStage sets CurrentStage field to given value.

### HasCurrentStage

`func (o *PacGet) HasCurrentStage() bool`

HasCurrentStage returns a boolean if a field has been set.

### SetCurrentStageNil

`func (o *PacGet) SetCurrentStageNil(b bool)`

 SetCurrentStageNil sets the value for CurrentStage to be an explicit nil

### UnsetCurrentStage
`func (o *PacGet) UnsetCurrentStage()`

UnsetCurrentStage ensures that no value is present for CurrentStage, not even an explicit nil
### GetTotalStages

`func (o *PacGet) GetTotalStages() int32`

GetTotalStages returns the TotalStages field if non-nil, zero value otherwise.

### GetTotalStagesOk

`func (o *PacGet) GetTotalStagesOk() (*int32, bool)`

GetTotalStagesOk returns a tuple with the TotalStages field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotalStages

`func (o *PacGet) SetTotalStages(v int32)`

SetTotalStages sets TotalStages field to given value.

### HasTotalStages

`func (o *PacGet) HasTotalStages() bool`

HasTotalStages returns a boolean if a field has been set.

### SetTotalStagesNil

`func (o *PacGet) SetTotalStagesNil(b bool)`

 SetTotalStagesNil sets the value for TotalStages to be an explicit nil

### UnsetTotalStages
`func (o *PacGet) UnsetTotalStages()`

UnsetTotalStages ensures that no value is present for TotalStages, not even an explicit nil
### GetDaysAtCurrentStage

`func (o *PacGet) GetDaysAtCurrentStage() int32`

GetDaysAtCurrentStage returns the DaysAtCurrentStage field if non-nil, zero value otherwise.

### GetDaysAtCurrentStageOk

`func (o *PacGet) GetDaysAtCurrentStageOk() (*int32, bool)`

GetDaysAtCurrentStageOk returns a tuple with the DaysAtCurrentStage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDaysAtCurrentStage

`func (o *PacGet) SetDaysAtCurrentStage(v int32)`

SetDaysAtCurrentStage sets DaysAtCurrentStage field to given value.

### HasDaysAtCurrentStage

`func (o *PacGet) HasDaysAtCurrentStage() bool`

HasDaysAtCurrentStage returns a boolean if a field has been set.

### SetDaysAtCurrentStageNil

`func (o *PacGet) SetDaysAtCurrentStageNil(b bool)`

 SetDaysAtCurrentStageNil sets the value for DaysAtCurrentStage to be an explicit nil

### UnsetDaysAtCurrentStage
`func (o *PacGet) UnsetDaysAtCurrentStage()`

UnsetDaysAtCurrentStage ensures that no value is present for DaysAtCurrentStage, not even an explicit nil
### GetComments

`func (o *PacGet) GetComments() string`

GetComments returns the Comments field if non-nil, zero value otherwise.

### GetCommentsOk

`func (o *PacGet) GetCommentsOk() (*string, bool)`

GetCommentsOk returns a tuple with the Comments field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetComments

`func (o *PacGet) SetComments(v string)`

SetComments sets Comments field to given value.

### HasComments

`func (o *PacGet) HasComments() bool`

HasComments returns a boolean if a field has been set.

### SetCommentsNil

`func (o *PacGet) SetCommentsNil(b bool)`

 SetCommentsNil sets the value for Comments to be an explicit nil

### UnsetComments
`func (o *PacGet) UnsetComments()`

UnsetComments ensures that no value is present for Comments, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


