# MilestonesRequiredPostMilestonesInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Description** | **string** | [Required] Include milestone description. | 
**ScheduledCompletionDate** | **int64** | [Required] Required for ongoing and completed POA&amp;M items. Unix time format. | 

## Methods

### NewMilestonesRequiredPostMilestonesInner

`func NewMilestonesRequiredPostMilestonesInner(description string, scheduledCompletionDate int64, ) *MilestonesRequiredPostMilestonesInner`

NewMilestonesRequiredPostMilestonesInner instantiates a new MilestonesRequiredPostMilestonesInner object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewMilestonesRequiredPostMilestonesInnerWithDefaults

`func NewMilestonesRequiredPostMilestonesInnerWithDefaults() *MilestonesRequiredPostMilestonesInner`

NewMilestonesRequiredPostMilestonesInnerWithDefaults instantiates a new MilestonesRequiredPostMilestonesInner object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetDescription

`func (o *MilestonesRequiredPostMilestonesInner) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *MilestonesRequiredPostMilestonesInner) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *MilestonesRequiredPostMilestonesInner) SetDescription(v string)`

SetDescription sets Description field to given value.


### GetScheduledCompletionDate

`func (o *MilestonesRequiredPostMilestonesInner) GetScheduledCompletionDate() int64`

GetScheduledCompletionDate returns the ScheduledCompletionDate field if non-nil, zero value otherwise.

### GetScheduledCompletionDateOk

`func (o *MilestonesRequiredPostMilestonesInner) GetScheduledCompletionDateOk() (*int64, bool)`

GetScheduledCompletionDateOk returns a tuple with the ScheduledCompletionDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetScheduledCompletionDate

`func (o *MilestonesRequiredPostMilestonesInner) SetScheduledCompletionDate(v int64)`

SetScheduledCompletionDate sets ScheduledCompletionDate field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


