# WorkflowInstanceGet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**WorkflowUid** | Pointer to **NullableString** | [Read-Only] Unique workflow definition identifier. | [optional] 
**SystemId** | Pointer to **NullableInt64** | [Read-only] Unique system record identifier. | [optional] 
**SystemName** | Pointer to **NullableString** | [Read-Only] The system name. | [optional] 
**WorkflowInstanceId** | Pointer to **NullableInt64** | [Read-Only] Unique workflow instance identifier. | [optional] 
**PackageName** | Pointer to **NullableString** | [Read-Only] The package name. | [optional] 
**CreatedDate** | Pointer to **NullableInt64** | [Read-Only] Date the workflow instance or the workflow transition was created. | [optional] 
**LastEditedDate** | Pointer to **NullableInt64** | [Read-Only] Date the workflow was last acted on. | [optional] 
**LastEditedBy** | Pointer to **NullableString** | [Read-Only] User that last acted on the workflow. | [optional] 
**Workflow** | Pointer to **NullableString** | [Read-Only] The workflow type. | [optional] 
**Version** | Pointer to **NullableInt64** | [Read-Only] Version of the workflow definition. | [optional] 
**CurrentStage** | Pointer to **NullableString** | [Read-Only] Name of the current stage. | [optional] 
**Transitions** | Pointer to [**[]InstanceTransitions**](InstanceTransitions.md) |  | [optional] 

## Methods

### NewWorkflowInstanceGet

`func NewWorkflowInstanceGet() *WorkflowInstanceGet`

NewWorkflowInstanceGet instantiates a new WorkflowInstanceGet object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewWorkflowInstanceGetWithDefaults

`func NewWorkflowInstanceGetWithDefaults() *WorkflowInstanceGet`

NewWorkflowInstanceGetWithDefaults instantiates a new WorkflowInstanceGet object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetWorkflowUid

`func (o *WorkflowInstanceGet) GetWorkflowUid() string`

GetWorkflowUid returns the WorkflowUid field if non-nil, zero value otherwise.

### GetWorkflowUidOk

`func (o *WorkflowInstanceGet) GetWorkflowUidOk() (*string, bool)`

GetWorkflowUidOk returns a tuple with the WorkflowUid field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWorkflowUid

`func (o *WorkflowInstanceGet) SetWorkflowUid(v string)`

SetWorkflowUid sets WorkflowUid field to given value.

### HasWorkflowUid

`func (o *WorkflowInstanceGet) HasWorkflowUid() bool`

HasWorkflowUid returns a boolean if a field has been set.

### SetWorkflowUidNil

`func (o *WorkflowInstanceGet) SetWorkflowUidNil(b bool)`

 SetWorkflowUidNil sets the value for WorkflowUid to be an explicit nil

### UnsetWorkflowUid
`func (o *WorkflowInstanceGet) UnsetWorkflowUid()`

UnsetWorkflowUid ensures that no value is present for WorkflowUid, not even an explicit nil
### GetSystemId

`func (o *WorkflowInstanceGet) GetSystemId() int64`

GetSystemId returns the SystemId field if non-nil, zero value otherwise.

### GetSystemIdOk

`func (o *WorkflowInstanceGet) GetSystemIdOk() (*int64, bool)`

GetSystemIdOk returns a tuple with the SystemId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSystemId

`func (o *WorkflowInstanceGet) SetSystemId(v int64)`

SetSystemId sets SystemId field to given value.

### HasSystemId

`func (o *WorkflowInstanceGet) HasSystemId() bool`

HasSystemId returns a boolean if a field has been set.

### SetSystemIdNil

`func (o *WorkflowInstanceGet) SetSystemIdNil(b bool)`

 SetSystemIdNil sets the value for SystemId to be an explicit nil

### UnsetSystemId
`func (o *WorkflowInstanceGet) UnsetSystemId()`

UnsetSystemId ensures that no value is present for SystemId, not even an explicit nil
### GetSystemName

`func (o *WorkflowInstanceGet) GetSystemName() string`

GetSystemName returns the SystemName field if non-nil, zero value otherwise.

### GetSystemNameOk

`func (o *WorkflowInstanceGet) GetSystemNameOk() (*string, bool)`

GetSystemNameOk returns a tuple with the SystemName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSystemName

`func (o *WorkflowInstanceGet) SetSystemName(v string)`

SetSystemName sets SystemName field to given value.

### HasSystemName

`func (o *WorkflowInstanceGet) HasSystemName() bool`

HasSystemName returns a boolean if a field has been set.

### SetSystemNameNil

`func (o *WorkflowInstanceGet) SetSystemNameNil(b bool)`

 SetSystemNameNil sets the value for SystemName to be an explicit nil

### UnsetSystemName
`func (o *WorkflowInstanceGet) UnsetSystemName()`

UnsetSystemName ensures that no value is present for SystemName, not even an explicit nil
### GetWorkflowInstanceId

`func (o *WorkflowInstanceGet) GetWorkflowInstanceId() int64`

GetWorkflowInstanceId returns the WorkflowInstanceId field if non-nil, zero value otherwise.

### GetWorkflowInstanceIdOk

`func (o *WorkflowInstanceGet) GetWorkflowInstanceIdOk() (*int64, bool)`

GetWorkflowInstanceIdOk returns a tuple with the WorkflowInstanceId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWorkflowInstanceId

`func (o *WorkflowInstanceGet) SetWorkflowInstanceId(v int64)`

SetWorkflowInstanceId sets WorkflowInstanceId field to given value.

### HasWorkflowInstanceId

`func (o *WorkflowInstanceGet) HasWorkflowInstanceId() bool`

HasWorkflowInstanceId returns a boolean if a field has been set.

### SetWorkflowInstanceIdNil

`func (o *WorkflowInstanceGet) SetWorkflowInstanceIdNil(b bool)`

 SetWorkflowInstanceIdNil sets the value for WorkflowInstanceId to be an explicit nil

### UnsetWorkflowInstanceId
`func (o *WorkflowInstanceGet) UnsetWorkflowInstanceId()`

UnsetWorkflowInstanceId ensures that no value is present for WorkflowInstanceId, not even an explicit nil
### GetPackageName

`func (o *WorkflowInstanceGet) GetPackageName() string`

GetPackageName returns the PackageName field if non-nil, zero value otherwise.

### GetPackageNameOk

`func (o *WorkflowInstanceGet) GetPackageNameOk() (*string, bool)`

GetPackageNameOk returns a tuple with the PackageName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPackageName

`func (o *WorkflowInstanceGet) SetPackageName(v string)`

SetPackageName sets PackageName field to given value.

### HasPackageName

`func (o *WorkflowInstanceGet) HasPackageName() bool`

HasPackageName returns a boolean if a field has been set.

### SetPackageNameNil

`func (o *WorkflowInstanceGet) SetPackageNameNil(b bool)`

 SetPackageNameNil sets the value for PackageName to be an explicit nil

### UnsetPackageName
`func (o *WorkflowInstanceGet) UnsetPackageName()`

UnsetPackageName ensures that no value is present for PackageName, not even an explicit nil
### GetCreatedDate

`func (o *WorkflowInstanceGet) GetCreatedDate() int64`

GetCreatedDate returns the CreatedDate field if non-nil, zero value otherwise.

### GetCreatedDateOk

`func (o *WorkflowInstanceGet) GetCreatedDateOk() (*int64, bool)`

GetCreatedDateOk returns a tuple with the CreatedDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedDate

`func (o *WorkflowInstanceGet) SetCreatedDate(v int64)`

SetCreatedDate sets CreatedDate field to given value.

### HasCreatedDate

`func (o *WorkflowInstanceGet) HasCreatedDate() bool`

HasCreatedDate returns a boolean if a field has been set.

### SetCreatedDateNil

`func (o *WorkflowInstanceGet) SetCreatedDateNil(b bool)`

 SetCreatedDateNil sets the value for CreatedDate to be an explicit nil

### UnsetCreatedDate
`func (o *WorkflowInstanceGet) UnsetCreatedDate()`

UnsetCreatedDate ensures that no value is present for CreatedDate, not even an explicit nil
### GetLastEditedDate

`func (o *WorkflowInstanceGet) GetLastEditedDate() int64`

GetLastEditedDate returns the LastEditedDate field if non-nil, zero value otherwise.

### GetLastEditedDateOk

`func (o *WorkflowInstanceGet) GetLastEditedDateOk() (*int64, bool)`

GetLastEditedDateOk returns a tuple with the LastEditedDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLastEditedDate

`func (o *WorkflowInstanceGet) SetLastEditedDate(v int64)`

SetLastEditedDate sets LastEditedDate field to given value.

### HasLastEditedDate

`func (o *WorkflowInstanceGet) HasLastEditedDate() bool`

HasLastEditedDate returns a boolean if a field has been set.

### SetLastEditedDateNil

`func (o *WorkflowInstanceGet) SetLastEditedDateNil(b bool)`

 SetLastEditedDateNil sets the value for LastEditedDate to be an explicit nil

### UnsetLastEditedDate
`func (o *WorkflowInstanceGet) UnsetLastEditedDate()`

UnsetLastEditedDate ensures that no value is present for LastEditedDate, not even an explicit nil
### GetLastEditedBy

`func (o *WorkflowInstanceGet) GetLastEditedBy() string`

GetLastEditedBy returns the LastEditedBy field if non-nil, zero value otherwise.

### GetLastEditedByOk

`func (o *WorkflowInstanceGet) GetLastEditedByOk() (*string, bool)`

GetLastEditedByOk returns a tuple with the LastEditedBy field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLastEditedBy

`func (o *WorkflowInstanceGet) SetLastEditedBy(v string)`

SetLastEditedBy sets LastEditedBy field to given value.

### HasLastEditedBy

`func (o *WorkflowInstanceGet) HasLastEditedBy() bool`

HasLastEditedBy returns a boolean if a field has been set.

### SetLastEditedByNil

`func (o *WorkflowInstanceGet) SetLastEditedByNil(b bool)`

 SetLastEditedByNil sets the value for LastEditedBy to be an explicit nil

### UnsetLastEditedBy
`func (o *WorkflowInstanceGet) UnsetLastEditedBy()`

UnsetLastEditedBy ensures that no value is present for LastEditedBy, not even an explicit nil
### GetWorkflow

`func (o *WorkflowInstanceGet) GetWorkflow() string`

GetWorkflow returns the Workflow field if non-nil, zero value otherwise.

### GetWorkflowOk

`func (o *WorkflowInstanceGet) GetWorkflowOk() (*string, bool)`

GetWorkflowOk returns a tuple with the Workflow field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWorkflow

`func (o *WorkflowInstanceGet) SetWorkflow(v string)`

SetWorkflow sets Workflow field to given value.

### HasWorkflow

`func (o *WorkflowInstanceGet) HasWorkflow() bool`

HasWorkflow returns a boolean if a field has been set.

### SetWorkflowNil

`func (o *WorkflowInstanceGet) SetWorkflowNil(b bool)`

 SetWorkflowNil sets the value for Workflow to be an explicit nil

### UnsetWorkflow
`func (o *WorkflowInstanceGet) UnsetWorkflow()`

UnsetWorkflow ensures that no value is present for Workflow, not even an explicit nil
### GetVersion

`func (o *WorkflowInstanceGet) GetVersion() int64`

GetVersion returns the Version field if non-nil, zero value otherwise.

### GetVersionOk

`func (o *WorkflowInstanceGet) GetVersionOk() (*int64, bool)`

GetVersionOk returns a tuple with the Version field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVersion

`func (o *WorkflowInstanceGet) SetVersion(v int64)`

SetVersion sets Version field to given value.

### HasVersion

`func (o *WorkflowInstanceGet) HasVersion() bool`

HasVersion returns a boolean if a field has been set.

### SetVersionNil

`func (o *WorkflowInstanceGet) SetVersionNil(b bool)`

 SetVersionNil sets the value for Version to be an explicit nil

### UnsetVersion
`func (o *WorkflowInstanceGet) UnsetVersion()`

UnsetVersion ensures that no value is present for Version, not even an explicit nil
### GetCurrentStage

`func (o *WorkflowInstanceGet) GetCurrentStage() string`

GetCurrentStage returns the CurrentStage field if non-nil, zero value otherwise.

### GetCurrentStageOk

`func (o *WorkflowInstanceGet) GetCurrentStageOk() (*string, bool)`

GetCurrentStageOk returns a tuple with the CurrentStage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCurrentStage

`func (o *WorkflowInstanceGet) SetCurrentStage(v string)`

SetCurrentStage sets CurrentStage field to given value.

### HasCurrentStage

`func (o *WorkflowInstanceGet) HasCurrentStage() bool`

HasCurrentStage returns a boolean if a field has been set.

### SetCurrentStageNil

`func (o *WorkflowInstanceGet) SetCurrentStageNil(b bool)`

 SetCurrentStageNil sets the value for CurrentStage to be an explicit nil

### UnsetCurrentStage
`func (o *WorkflowInstanceGet) UnsetCurrentStage()`

UnsetCurrentStage ensures that no value is present for CurrentStage, not even an explicit nil
### GetTransitions

`func (o *WorkflowInstanceGet) GetTransitions() []InstanceTransitions`

GetTransitions returns the Transitions field if non-nil, zero value otherwise.

### GetTransitionsOk

`func (o *WorkflowInstanceGet) GetTransitionsOk() (*[]InstanceTransitions, bool)`

GetTransitionsOk returns a tuple with the Transitions field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTransitions

`func (o *WorkflowInstanceGet) SetTransitions(v []InstanceTransitions)`

SetTransitions sets Transitions field to given value.

### HasTransitions

`func (o *WorkflowInstanceGet) HasTransitions() bool`

HasTransitions returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


