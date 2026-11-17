# PoamReadOnlyFields

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ConditionId** | Pointer to **NullableString** | [Read-Only] Unique identifier of the authorization term/condition linked to the POA&amp;M Item. | [optional] 
**IsInherited** | Pointer to **NullableBool** | [Read-only] Indicates whether a test result is inherited. | [optional] 
**Cci** | Pointer to **NullableString** | [Read-Only] CCI associated with POA&amp;M Item. | [optional] 
**ReviewStatus** | Pointer to **NullableString** | [Read-Only] Values include the following options: (Not Approved,Under Review,Approved) | [optional] 
**CreatedDate** | Pointer to **int64** | [Read-Only] Timestamp representing when the POA&amp;M Item was entered into the database. | [optional] 
**ExtensionDate** | Pointer to **NullableInt64** | [Read-Only] Value returned for a POA&amp;M Item with review status \&quot;Approved\&quot; and has a milestone with a scheduled completion date that extends beyond the POA&amp;M Item&#39;s scheduled completion date.  | [optional] 
**PendingExtensionDate** | Pointer to **NullableInt64** | [Read-Only] Value returned for a POA&amp;M Item with a review status of \&quot;Approved\&quot; and an unapproved milestone with a scheduled completion date that extends beyond the POA&amp;M Item&#39;s scheduled completion date.  | [optional] 
**Artifacts** | Pointer to **NullableString** | [Read-Only] Lists the filenames of any artifact files attached to the POA&amp;M Item. Multiple values are separated by “; ”. | [optional] 

## Methods

### NewPoamReadOnlyFields

`func NewPoamReadOnlyFields() *PoamReadOnlyFields`

NewPoamReadOnlyFields instantiates a new PoamReadOnlyFields object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPoamReadOnlyFieldsWithDefaults

`func NewPoamReadOnlyFieldsWithDefaults() *PoamReadOnlyFields`

NewPoamReadOnlyFieldsWithDefaults instantiates a new PoamReadOnlyFields object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetConditionId

`func (o *PoamReadOnlyFields) GetConditionId() string`

GetConditionId returns the ConditionId field if non-nil, zero value otherwise.

### GetConditionIdOk

`func (o *PoamReadOnlyFields) GetConditionIdOk() (*string, bool)`

GetConditionIdOk returns a tuple with the ConditionId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetConditionId

`func (o *PoamReadOnlyFields) SetConditionId(v string)`

SetConditionId sets ConditionId field to given value.

### HasConditionId

`func (o *PoamReadOnlyFields) HasConditionId() bool`

HasConditionId returns a boolean if a field has been set.

### SetConditionIdNil

`func (o *PoamReadOnlyFields) SetConditionIdNil(b bool)`

 SetConditionIdNil sets the value for ConditionId to be an explicit nil

### UnsetConditionId
`func (o *PoamReadOnlyFields) UnsetConditionId()`

UnsetConditionId ensures that no value is present for ConditionId, not even an explicit nil
### GetIsInherited

`func (o *PoamReadOnlyFields) GetIsInherited() bool`

GetIsInherited returns the IsInherited field if non-nil, zero value otherwise.

### GetIsInheritedOk

`func (o *PoamReadOnlyFields) GetIsInheritedOk() (*bool, bool)`

GetIsInheritedOk returns a tuple with the IsInherited field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsInherited

`func (o *PoamReadOnlyFields) SetIsInherited(v bool)`

SetIsInherited sets IsInherited field to given value.

### HasIsInherited

`func (o *PoamReadOnlyFields) HasIsInherited() bool`

HasIsInherited returns a boolean if a field has been set.

### SetIsInheritedNil

`func (o *PoamReadOnlyFields) SetIsInheritedNil(b bool)`

 SetIsInheritedNil sets the value for IsInherited to be an explicit nil

### UnsetIsInherited
`func (o *PoamReadOnlyFields) UnsetIsInherited()`

UnsetIsInherited ensures that no value is present for IsInherited, not even an explicit nil
### GetCci

`func (o *PoamReadOnlyFields) GetCci() string`

GetCci returns the Cci field if non-nil, zero value otherwise.

### GetCciOk

`func (o *PoamReadOnlyFields) GetCciOk() (*string, bool)`

GetCciOk returns a tuple with the Cci field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCci

`func (o *PoamReadOnlyFields) SetCci(v string)`

SetCci sets Cci field to given value.

### HasCci

`func (o *PoamReadOnlyFields) HasCci() bool`

HasCci returns a boolean if a field has been set.

### SetCciNil

`func (o *PoamReadOnlyFields) SetCciNil(b bool)`

 SetCciNil sets the value for Cci to be an explicit nil

### UnsetCci
`func (o *PoamReadOnlyFields) UnsetCci()`

UnsetCci ensures that no value is present for Cci, not even an explicit nil
### GetReviewStatus

`func (o *PoamReadOnlyFields) GetReviewStatus() string`

GetReviewStatus returns the ReviewStatus field if non-nil, zero value otherwise.

### GetReviewStatusOk

`func (o *PoamReadOnlyFields) GetReviewStatusOk() (*string, bool)`

GetReviewStatusOk returns a tuple with the ReviewStatus field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetReviewStatus

`func (o *PoamReadOnlyFields) SetReviewStatus(v string)`

SetReviewStatus sets ReviewStatus field to given value.

### HasReviewStatus

`func (o *PoamReadOnlyFields) HasReviewStatus() bool`

HasReviewStatus returns a boolean if a field has been set.

### SetReviewStatusNil

`func (o *PoamReadOnlyFields) SetReviewStatusNil(b bool)`

 SetReviewStatusNil sets the value for ReviewStatus to be an explicit nil

### UnsetReviewStatus
`func (o *PoamReadOnlyFields) UnsetReviewStatus()`

UnsetReviewStatus ensures that no value is present for ReviewStatus, not even an explicit nil
### GetCreatedDate

`func (o *PoamReadOnlyFields) GetCreatedDate() int64`

GetCreatedDate returns the CreatedDate field if non-nil, zero value otherwise.

### GetCreatedDateOk

`func (o *PoamReadOnlyFields) GetCreatedDateOk() (*int64, bool)`

GetCreatedDateOk returns a tuple with the CreatedDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedDate

`func (o *PoamReadOnlyFields) SetCreatedDate(v int64)`

SetCreatedDate sets CreatedDate field to given value.

### HasCreatedDate

`func (o *PoamReadOnlyFields) HasCreatedDate() bool`

HasCreatedDate returns a boolean if a field has been set.

### GetExtensionDate

`func (o *PoamReadOnlyFields) GetExtensionDate() int64`

GetExtensionDate returns the ExtensionDate field if non-nil, zero value otherwise.

### GetExtensionDateOk

`func (o *PoamReadOnlyFields) GetExtensionDateOk() (*int64, bool)`

GetExtensionDateOk returns a tuple with the ExtensionDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExtensionDate

`func (o *PoamReadOnlyFields) SetExtensionDate(v int64)`

SetExtensionDate sets ExtensionDate field to given value.

### HasExtensionDate

`func (o *PoamReadOnlyFields) HasExtensionDate() bool`

HasExtensionDate returns a boolean if a field has been set.

### SetExtensionDateNil

`func (o *PoamReadOnlyFields) SetExtensionDateNil(b bool)`

 SetExtensionDateNil sets the value for ExtensionDate to be an explicit nil

### UnsetExtensionDate
`func (o *PoamReadOnlyFields) UnsetExtensionDate()`

UnsetExtensionDate ensures that no value is present for ExtensionDate, not even an explicit nil
### GetPendingExtensionDate

`func (o *PoamReadOnlyFields) GetPendingExtensionDate() int64`

GetPendingExtensionDate returns the PendingExtensionDate field if non-nil, zero value otherwise.

### GetPendingExtensionDateOk

`func (o *PoamReadOnlyFields) GetPendingExtensionDateOk() (*int64, bool)`

GetPendingExtensionDateOk returns a tuple with the PendingExtensionDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPendingExtensionDate

`func (o *PoamReadOnlyFields) SetPendingExtensionDate(v int64)`

SetPendingExtensionDate sets PendingExtensionDate field to given value.

### HasPendingExtensionDate

`func (o *PoamReadOnlyFields) HasPendingExtensionDate() bool`

HasPendingExtensionDate returns a boolean if a field has been set.

### SetPendingExtensionDateNil

`func (o *PoamReadOnlyFields) SetPendingExtensionDateNil(b bool)`

 SetPendingExtensionDateNil sets the value for PendingExtensionDate to be an explicit nil

### UnsetPendingExtensionDate
`func (o *PoamReadOnlyFields) UnsetPendingExtensionDate()`

UnsetPendingExtensionDate ensures that no value is present for PendingExtensionDate, not even an explicit nil
### GetArtifacts

`func (o *PoamReadOnlyFields) GetArtifacts() string`

GetArtifacts returns the Artifacts field if non-nil, zero value otherwise.

### GetArtifactsOk

`func (o *PoamReadOnlyFields) GetArtifactsOk() (*string, bool)`

GetArtifactsOk returns a tuple with the Artifacts field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetArtifacts

`func (o *PoamReadOnlyFields) SetArtifacts(v string)`

SetArtifacts sets Artifacts field to given value.

### HasArtifacts

`func (o *PoamReadOnlyFields) HasArtifacts() bool`

HasArtifacts returns a boolean if a field has been set.

### SetArtifactsNil

`func (o *PoamReadOnlyFields) SetArtifactsNil(b bool)`

 SetArtifactsNil sets the value for Artifacts to be an explicit nil

### UnsetArtifacts
`func (o *PoamReadOnlyFields) UnsetArtifacts()`

UnsetArtifacts ensures that no value is present for Artifacts, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


