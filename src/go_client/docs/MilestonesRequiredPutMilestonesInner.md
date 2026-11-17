# MilestonesRequiredPutMilestonesInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Description** | **string** | [Required] Include milestone description. | 
**ScheduledCompletionDate** | **int64** | [Required] Required for ongoing and completed POA&amp;M items. Unix time format. | 
**IsActive** | **bool** | [Conditional] Optionally used in PUT to delete milestones when updating a POA&amp;M. | 

## Methods

### NewMilestonesRequiredPutMilestonesInner

`func NewMilestonesRequiredPutMilestonesInner(description string, scheduledCompletionDate int64, isActive bool, ) *MilestonesRequiredPutMilestonesInner`

NewMilestonesRequiredPutMilestonesInner instantiates a new MilestonesRequiredPutMilestonesInner object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewMilestonesRequiredPutMilestonesInnerWithDefaults

`func NewMilestonesRequiredPutMilestonesInnerWithDefaults() *MilestonesRequiredPutMilestonesInner`

NewMilestonesRequiredPutMilestonesInnerWithDefaults instantiates a new MilestonesRequiredPutMilestonesInner object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetDescription

`func (o *MilestonesRequiredPutMilestonesInner) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *MilestonesRequiredPutMilestonesInner) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *MilestonesRequiredPutMilestonesInner) SetDescription(v string)`

SetDescription sets Description field to given value.


### GetScheduledCompletionDate

`func (o *MilestonesRequiredPutMilestonesInner) GetScheduledCompletionDate() int64`

GetScheduledCompletionDate returns the ScheduledCompletionDate field if non-nil, zero value otherwise.

### GetScheduledCompletionDateOk

`func (o *MilestonesRequiredPutMilestonesInner) GetScheduledCompletionDateOk() (*int64, bool)`

GetScheduledCompletionDateOk returns a tuple with the ScheduledCompletionDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetScheduledCompletionDate

`func (o *MilestonesRequiredPutMilestonesInner) SetScheduledCompletionDate(v int64)`

SetScheduledCompletionDate sets ScheduledCompletionDate field to given value.


### GetIsActive

`func (o *MilestonesRequiredPutMilestonesInner) GetIsActive() bool`

GetIsActive returns the IsActive field if non-nil, zero value otherwise.

### GetIsActiveOk

`func (o *MilestonesRequiredPutMilestonesInner) GetIsActiveOk() (*bool, bool)`

GetIsActiveOk returns a tuple with the IsActive field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsActive

`func (o *MilestonesRequiredPutMilestonesInner) SetIsActive(v bool)`

SetIsActive sets IsActive field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


