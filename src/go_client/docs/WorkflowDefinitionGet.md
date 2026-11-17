# WorkflowDefinitionGet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**WorkflowUid** | Pointer to **NullableString** | [Read-Only] Unique workflow definition identifier. | [optional] 
**Workflow** | Pointer to **NullableString** | [Read-Only] The workflow type. | [optional] 
**Version** | Pointer to **NullableString** | [Read-Only] Version of the workflow definition. | [optional] 
**Description** | Pointer to **NullableString** | [Read-Only] Description of the workflow or the stage transition. | [optional] 
**IsActive** | Pointer to **NullableBool** | [Read-Only] Returns true if the workflow is available to the site. | [optional] 
**Stages** | Pointer to [**[]Stage**](Stage.md) |  | [optional] 

## Methods

### NewWorkflowDefinitionGet

`func NewWorkflowDefinitionGet() *WorkflowDefinitionGet`

NewWorkflowDefinitionGet instantiates a new WorkflowDefinitionGet object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewWorkflowDefinitionGetWithDefaults

`func NewWorkflowDefinitionGetWithDefaults() *WorkflowDefinitionGet`

NewWorkflowDefinitionGetWithDefaults instantiates a new WorkflowDefinitionGet object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetWorkflowUid

`func (o *WorkflowDefinitionGet) GetWorkflowUid() string`

GetWorkflowUid returns the WorkflowUid field if non-nil, zero value otherwise.

### GetWorkflowUidOk

`func (o *WorkflowDefinitionGet) GetWorkflowUidOk() (*string, bool)`

GetWorkflowUidOk returns a tuple with the WorkflowUid field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWorkflowUid

`func (o *WorkflowDefinitionGet) SetWorkflowUid(v string)`

SetWorkflowUid sets WorkflowUid field to given value.

### HasWorkflowUid

`func (o *WorkflowDefinitionGet) HasWorkflowUid() bool`

HasWorkflowUid returns a boolean if a field has been set.

### SetWorkflowUidNil

`func (o *WorkflowDefinitionGet) SetWorkflowUidNil(b bool)`

 SetWorkflowUidNil sets the value for WorkflowUid to be an explicit nil

### UnsetWorkflowUid
`func (o *WorkflowDefinitionGet) UnsetWorkflowUid()`

UnsetWorkflowUid ensures that no value is present for WorkflowUid, not even an explicit nil
### GetWorkflow

`func (o *WorkflowDefinitionGet) GetWorkflow() string`

GetWorkflow returns the Workflow field if non-nil, zero value otherwise.

### GetWorkflowOk

`func (o *WorkflowDefinitionGet) GetWorkflowOk() (*string, bool)`

GetWorkflowOk returns a tuple with the Workflow field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWorkflow

`func (o *WorkflowDefinitionGet) SetWorkflow(v string)`

SetWorkflow sets Workflow field to given value.

### HasWorkflow

`func (o *WorkflowDefinitionGet) HasWorkflow() bool`

HasWorkflow returns a boolean if a field has been set.

### SetWorkflowNil

`func (o *WorkflowDefinitionGet) SetWorkflowNil(b bool)`

 SetWorkflowNil sets the value for Workflow to be an explicit nil

### UnsetWorkflow
`func (o *WorkflowDefinitionGet) UnsetWorkflow()`

UnsetWorkflow ensures that no value is present for Workflow, not even an explicit nil
### GetVersion

`func (o *WorkflowDefinitionGet) GetVersion() string`

GetVersion returns the Version field if non-nil, zero value otherwise.

### GetVersionOk

`func (o *WorkflowDefinitionGet) GetVersionOk() (*string, bool)`

GetVersionOk returns a tuple with the Version field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVersion

`func (o *WorkflowDefinitionGet) SetVersion(v string)`

SetVersion sets Version field to given value.

### HasVersion

`func (o *WorkflowDefinitionGet) HasVersion() bool`

HasVersion returns a boolean if a field has been set.

### SetVersionNil

`func (o *WorkflowDefinitionGet) SetVersionNil(b bool)`

 SetVersionNil sets the value for Version to be an explicit nil

### UnsetVersion
`func (o *WorkflowDefinitionGet) UnsetVersion()`

UnsetVersion ensures that no value is present for Version, not even an explicit nil
### GetDescription

`func (o *WorkflowDefinitionGet) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *WorkflowDefinitionGet) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *WorkflowDefinitionGet) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *WorkflowDefinitionGet) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### SetDescriptionNil

`func (o *WorkflowDefinitionGet) SetDescriptionNil(b bool)`

 SetDescriptionNil sets the value for Description to be an explicit nil

### UnsetDescription
`func (o *WorkflowDefinitionGet) UnsetDescription()`

UnsetDescription ensures that no value is present for Description, not even an explicit nil
### GetIsActive

`func (o *WorkflowDefinitionGet) GetIsActive() bool`

GetIsActive returns the IsActive field if non-nil, zero value otherwise.

### GetIsActiveOk

`func (o *WorkflowDefinitionGet) GetIsActiveOk() (*bool, bool)`

GetIsActiveOk returns a tuple with the IsActive field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsActive

`func (o *WorkflowDefinitionGet) SetIsActive(v bool)`

SetIsActive sets IsActive field to given value.

### HasIsActive

`func (o *WorkflowDefinitionGet) HasIsActive() bool`

HasIsActive returns a boolean if a field has been set.

### SetIsActiveNil

`func (o *WorkflowDefinitionGet) SetIsActiveNil(b bool)`

 SetIsActiveNil sets the value for IsActive to be an explicit nil

### UnsetIsActive
`func (o *WorkflowDefinitionGet) UnsetIsActive()`

UnsetIsActive ensures that no value is present for IsActive, not even an explicit nil
### GetStages

`func (o *WorkflowDefinitionGet) GetStages() []Stage`

GetStages returns the Stages field if non-nil, zero value otherwise.

### GetStagesOk

`func (o *WorkflowDefinitionGet) GetStagesOk() (*[]Stage, bool)`

GetStagesOk returns a tuple with the Stages field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStages

`func (o *WorkflowDefinitionGet) SetStages(v []Stage)`

SetStages sets Stages field to given value.

### HasStages

`func (o *WorkflowDefinitionGet) HasStages() bool`

HasStages returns a boolean if a field has been set.

### SetStagesNil

`func (o *WorkflowDefinitionGet) SetStagesNil(b bool)`

 SetStagesNil sets the value for Stages to be an explicit nil

### UnsetStages
`func (o *WorkflowDefinitionGet) UnsetStages()`

UnsetStages ensures that no value is present for Stages, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


