# CacGet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**SystemId** | Pointer to **int64** | [Required] Unique eMASS system identifier. | [optional] 
**ControlAcronym** | Pointer to **string** | [Required] System acronym name. | [optional] 
**ComplianceStatus** | Pointer to **NullableString** | [Read-only] Compliance status of the control. | [optional] 
**CurrentStageName** | Pointer to **NullableString** | [Read-Only] Role in current stage. | [optional] 
**CurrentStage** | Pointer to **NullableInt32** | [Read-Only] Current step in the Control Approval Chain. | [optional] 
**TotalStages** | Pointer to **NullableInt32** | [Read-Only] Total number of steps in Control Approval Chain. | [optional] 
**Comments** | Pointer to **NullableString** | [Conditional] Control Approval Chain comments - 2000 Characters. | [optional] 

## Methods

### NewCacGet

`func NewCacGet() *CacGet`

NewCacGet instantiates a new CacGet object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCacGetWithDefaults

`func NewCacGetWithDefaults() *CacGet`

NewCacGetWithDefaults instantiates a new CacGet object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetSystemId

`func (o *CacGet) GetSystemId() int64`

GetSystemId returns the SystemId field if non-nil, zero value otherwise.

### GetSystemIdOk

`func (o *CacGet) GetSystemIdOk() (*int64, bool)`

GetSystemIdOk returns a tuple with the SystemId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSystemId

`func (o *CacGet) SetSystemId(v int64)`

SetSystemId sets SystemId field to given value.

### HasSystemId

`func (o *CacGet) HasSystemId() bool`

HasSystemId returns a boolean if a field has been set.

### GetControlAcronym

`func (o *CacGet) GetControlAcronym() string`

GetControlAcronym returns the ControlAcronym field if non-nil, zero value otherwise.

### GetControlAcronymOk

`func (o *CacGet) GetControlAcronymOk() (*string, bool)`

GetControlAcronymOk returns a tuple with the ControlAcronym field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetControlAcronym

`func (o *CacGet) SetControlAcronym(v string)`

SetControlAcronym sets ControlAcronym field to given value.

### HasControlAcronym

`func (o *CacGet) HasControlAcronym() bool`

HasControlAcronym returns a boolean if a field has been set.

### GetComplianceStatus

`func (o *CacGet) GetComplianceStatus() string`

GetComplianceStatus returns the ComplianceStatus field if non-nil, zero value otherwise.

### GetComplianceStatusOk

`func (o *CacGet) GetComplianceStatusOk() (*string, bool)`

GetComplianceStatusOk returns a tuple with the ComplianceStatus field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetComplianceStatus

`func (o *CacGet) SetComplianceStatus(v string)`

SetComplianceStatus sets ComplianceStatus field to given value.

### HasComplianceStatus

`func (o *CacGet) HasComplianceStatus() bool`

HasComplianceStatus returns a boolean if a field has been set.

### SetComplianceStatusNil

`func (o *CacGet) SetComplianceStatusNil(b bool)`

 SetComplianceStatusNil sets the value for ComplianceStatus to be an explicit nil

### UnsetComplianceStatus
`func (o *CacGet) UnsetComplianceStatus()`

UnsetComplianceStatus ensures that no value is present for ComplianceStatus, not even an explicit nil
### GetCurrentStageName

`func (o *CacGet) GetCurrentStageName() string`

GetCurrentStageName returns the CurrentStageName field if non-nil, zero value otherwise.

### GetCurrentStageNameOk

`func (o *CacGet) GetCurrentStageNameOk() (*string, bool)`

GetCurrentStageNameOk returns a tuple with the CurrentStageName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCurrentStageName

`func (o *CacGet) SetCurrentStageName(v string)`

SetCurrentStageName sets CurrentStageName field to given value.

### HasCurrentStageName

`func (o *CacGet) HasCurrentStageName() bool`

HasCurrentStageName returns a boolean if a field has been set.

### SetCurrentStageNameNil

`func (o *CacGet) SetCurrentStageNameNil(b bool)`

 SetCurrentStageNameNil sets the value for CurrentStageName to be an explicit nil

### UnsetCurrentStageName
`func (o *CacGet) UnsetCurrentStageName()`

UnsetCurrentStageName ensures that no value is present for CurrentStageName, not even an explicit nil
### GetCurrentStage

`func (o *CacGet) GetCurrentStage() int32`

GetCurrentStage returns the CurrentStage field if non-nil, zero value otherwise.

### GetCurrentStageOk

`func (o *CacGet) GetCurrentStageOk() (*int32, bool)`

GetCurrentStageOk returns a tuple with the CurrentStage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCurrentStage

`func (o *CacGet) SetCurrentStage(v int32)`

SetCurrentStage sets CurrentStage field to given value.

### HasCurrentStage

`func (o *CacGet) HasCurrentStage() bool`

HasCurrentStage returns a boolean if a field has been set.

### SetCurrentStageNil

`func (o *CacGet) SetCurrentStageNil(b bool)`

 SetCurrentStageNil sets the value for CurrentStage to be an explicit nil

### UnsetCurrentStage
`func (o *CacGet) UnsetCurrentStage()`

UnsetCurrentStage ensures that no value is present for CurrentStage, not even an explicit nil
### GetTotalStages

`func (o *CacGet) GetTotalStages() int32`

GetTotalStages returns the TotalStages field if non-nil, zero value otherwise.

### GetTotalStagesOk

`func (o *CacGet) GetTotalStagesOk() (*int32, bool)`

GetTotalStagesOk returns a tuple with the TotalStages field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotalStages

`func (o *CacGet) SetTotalStages(v int32)`

SetTotalStages sets TotalStages field to given value.

### HasTotalStages

`func (o *CacGet) HasTotalStages() bool`

HasTotalStages returns a boolean if a field has been set.

### SetTotalStagesNil

`func (o *CacGet) SetTotalStagesNil(b bool)`

 SetTotalStagesNil sets the value for TotalStages to be an explicit nil

### UnsetTotalStages
`func (o *CacGet) UnsetTotalStages()`

UnsetTotalStages ensures that no value is present for TotalStages, not even an explicit nil
### GetComments

`func (o *CacGet) GetComments() string`

GetComments returns the Comments field if non-nil, zero value otherwise.

### GetCommentsOk

`func (o *CacGet) GetCommentsOk() (*string, bool)`

GetCommentsOk returns a tuple with the Comments field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetComments

`func (o *CacGet) SetComments(v string)`

SetComments sets Comments field to given value.

### HasComments

`func (o *CacGet) HasComments() bool`

HasComments returns a boolean if a field has been set.

### SetCommentsNil

`func (o *CacGet) SetCommentsNil(b bool)`

 SetCommentsNil sets the value for Comments to be an explicit nil

### UnsetComments
`func (o *CacGet) UnsetComments()`

UnsetComments ensures that no value is present for Comments, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


