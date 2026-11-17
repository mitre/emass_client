# MilestonesGet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**SystemId** | Pointer to **int64** | [Required] Unique eMASS system identifier. | [optional] 
**MilestoneId** | Pointer to **int64** | [Required] Unique item identifier. | [optional] 
**PoamId** | Pointer to **int64** | [Required] Unique item identifier. | [optional] 
**Description** | Pointer to **string** | [Required] Include milestone description. | [optional] 
**ScheduledCompletionDate** | Pointer to **int64** | [Required] Required for ongoing and completed POA&amp;M items. Unix time format. | [optional] 
**ReviewStatus** | Pointer to **NullableString** | [Read-Only] Values include the following options: (Not Approved,Under Review,Approved). | [optional] 
**CreatedBy** | Pointer to **NullableString** | [Read-Only] Last, first name of the user that created the milestone. | [optional] 
**CreatedDate** | Pointer to **int64** | [Read-Only] Timestamp representing when the milestone was entered into the database. | [optional] 

## Methods

### NewMilestonesGet

`func NewMilestonesGet() *MilestonesGet`

NewMilestonesGet instantiates a new MilestonesGet object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewMilestonesGetWithDefaults

`func NewMilestonesGetWithDefaults() *MilestonesGet`

NewMilestonesGetWithDefaults instantiates a new MilestonesGet object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetSystemId

`func (o *MilestonesGet) GetSystemId() int64`

GetSystemId returns the SystemId field if non-nil, zero value otherwise.

### GetSystemIdOk

`func (o *MilestonesGet) GetSystemIdOk() (*int64, bool)`

GetSystemIdOk returns a tuple with the SystemId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSystemId

`func (o *MilestonesGet) SetSystemId(v int64)`

SetSystemId sets SystemId field to given value.

### HasSystemId

`func (o *MilestonesGet) HasSystemId() bool`

HasSystemId returns a boolean if a field has been set.

### GetMilestoneId

`func (o *MilestonesGet) GetMilestoneId() int64`

GetMilestoneId returns the MilestoneId field if non-nil, zero value otherwise.

### GetMilestoneIdOk

`func (o *MilestonesGet) GetMilestoneIdOk() (*int64, bool)`

GetMilestoneIdOk returns a tuple with the MilestoneId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMilestoneId

`func (o *MilestonesGet) SetMilestoneId(v int64)`

SetMilestoneId sets MilestoneId field to given value.

### HasMilestoneId

`func (o *MilestonesGet) HasMilestoneId() bool`

HasMilestoneId returns a boolean if a field has been set.

### GetPoamId

`func (o *MilestonesGet) GetPoamId() int64`

GetPoamId returns the PoamId field if non-nil, zero value otherwise.

### GetPoamIdOk

`func (o *MilestonesGet) GetPoamIdOk() (*int64, bool)`

GetPoamIdOk returns a tuple with the PoamId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPoamId

`func (o *MilestonesGet) SetPoamId(v int64)`

SetPoamId sets PoamId field to given value.

### HasPoamId

`func (o *MilestonesGet) HasPoamId() bool`

HasPoamId returns a boolean if a field has been set.

### GetDescription

`func (o *MilestonesGet) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *MilestonesGet) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *MilestonesGet) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *MilestonesGet) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### GetScheduledCompletionDate

`func (o *MilestonesGet) GetScheduledCompletionDate() int64`

GetScheduledCompletionDate returns the ScheduledCompletionDate field if non-nil, zero value otherwise.

### GetScheduledCompletionDateOk

`func (o *MilestonesGet) GetScheduledCompletionDateOk() (*int64, bool)`

GetScheduledCompletionDateOk returns a tuple with the ScheduledCompletionDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetScheduledCompletionDate

`func (o *MilestonesGet) SetScheduledCompletionDate(v int64)`

SetScheduledCompletionDate sets ScheduledCompletionDate field to given value.

### HasScheduledCompletionDate

`func (o *MilestonesGet) HasScheduledCompletionDate() bool`

HasScheduledCompletionDate returns a boolean if a field has been set.

### GetReviewStatus

`func (o *MilestonesGet) GetReviewStatus() string`

GetReviewStatus returns the ReviewStatus field if non-nil, zero value otherwise.

### GetReviewStatusOk

`func (o *MilestonesGet) GetReviewStatusOk() (*string, bool)`

GetReviewStatusOk returns a tuple with the ReviewStatus field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetReviewStatus

`func (o *MilestonesGet) SetReviewStatus(v string)`

SetReviewStatus sets ReviewStatus field to given value.

### HasReviewStatus

`func (o *MilestonesGet) HasReviewStatus() bool`

HasReviewStatus returns a boolean if a field has been set.

### SetReviewStatusNil

`func (o *MilestonesGet) SetReviewStatusNil(b bool)`

 SetReviewStatusNil sets the value for ReviewStatus to be an explicit nil

### UnsetReviewStatus
`func (o *MilestonesGet) UnsetReviewStatus()`

UnsetReviewStatus ensures that no value is present for ReviewStatus, not even an explicit nil
### GetCreatedBy

`func (o *MilestonesGet) GetCreatedBy() string`

GetCreatedBy returns the CreatedBy field if non-nil, zero value otherwise.

### GetCreatedByOk

`func (o *MilestonesGet) GetCreatedByOk() (*string, bool)`

GetCreatedByOk returns a tuple with the CreatedBy field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedBy

`func (o *MilestonesGet) SetCreatedBy(v string)`

SetCreatedBy sets CreatedBy field to given value.

### HasCreatedBy

`func (o *MilestonesGet) HasCreatedBy() bool`

HasCreatedBy returns a boolean if a field has been set.

### SetCreatedByNil

`func (o *MilestonesGet) SetCreatedByNil(b bool)`

 SetCreatedByNil sets the value for CreatedBy to be an explicit nil

### UnsetCreatedBy
`func (o *MilestonesGet) UnsetCreatedBy()`

UnsetCreatedBy ensures that no value is present for CreatedBy, not even an explicit nil
### GetCreatedDate

`func (o *MilestonesGet) GetCreatedDate() int64`

GetCreatedDate returns the CreatedDate field if non-nil, zero value otherwise.

### GetCreatedDateOk

`func (o *MilestonesGet) GetCreatedDateOk() (*int64, bool)`

GetCreatedDateOk returns a tuple with the CreatedDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedDate

`func (o *MilestonesGet) SetCreatedDate(v int64)`

SetCreatedDate sets CreatedDate field to given value.

### HasCreatedDate

`func (o *MilestonesGet) HasCreatedDate() bool`

HasCreatedDate returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


