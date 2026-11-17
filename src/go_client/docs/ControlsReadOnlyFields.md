# ControlsReadOnlyFields

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | Pointer to **NullableString** | [Read-only] Name of the system record. | [optional] 
**Ccis** | Pointer to **NullableString** | [Read-only] Comma separated list of CCIs associated with the control. | [optional] 
**IsInherited** | Pointer to **NullableBool** | [Read-only] Indicates whether a control is inherited. | [optional] 
**ModifiedByOverlays** | Pointer to **NullableString** | [Read-only] List of overlays that affect the control. | [optional] 
**IncludedStatus** | Pointer to **NullableString** | [Read-only] Indicates the manner by which a control was included in the system&#39;s categorization. | [optional] 
**ComplianceStatus** | Pointer to **NullableString** | [Read-only] Compliance of the control. | [optional] 

## Methods

### NewControlsReadOnlyFields

`func NewControlsReadOnlyFields() *ControlsReadOnlyFields`

NewControlsReadOnlyFields instantiates a new ControlsReadOnlyFields object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewControlsReadOnlyFieldsWithDefaults

`func NewControlsReadOnlyFieldsWithDefaults() *ControlsReadOnlyFields`

NewControlsReadOnlyFieldsWithDefaults instantiates a new ControlsReadOnlyFields object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *ControlsReadOnlyFields) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *ControlsReadOnlyFields) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *ControlsReadOnlyFields) SetName(v string)`

SetName sets Name field to given value.

### HasName

`func (o *ControlsReadOnlyFields) HasName() bool`

HasName returns a boolean if a field has been set.

### SetNameNil

`func (o *ControlsReadOnlyFields) SetNameNil(b bool)`

 SetNameNil sets the value for Name to be an explicit nil

### UnsetName
`func (o *ControlsReadOnlyFields) UnsetName()`

UnsetName ensures that no value is present for Name, not even an explicit nil
### GetCcis

`func (o *ControlsReadOnlyFields) GetCcis() string`

GetCcis returns the Ccis field if non-nil, zero value otherwise.

### GetCcisOk

`func (o *ControlsReadOnlyFields) GetCcisOk() (*string, bool)`

GetCcisOk returns a tuple with the Ccis field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCcis

`func (o *ControlsReadOnlyFields) SetCcis(v string)`

SetCcis sets Ccis field to given value.

### HasCcis

`func (o *ControlsReadOnlyFields) HasCcis() bool`

HasCcis returns a boolean if a field has been set.

### SetCcisNil

`func (o *ControlsReadOnlyFields) SetCcisNil(b bool)`

 SetCcisNil sets the value for Ccis to be an explicit nil

### UnsetCcis
`func (o *ControlsReadOnlyFields) UnsetCcis()`

UnsetCcis ensures that no value is present for Ccis, not even an explicit nil
### GetIsInherited

`func (o *ControlsReadOnlyFields) GetIsInherited() bool`

GetIsInherited returns the IsInherited field if non-nil, zero value otherwise.

### GetIsInheritedOk

`func (o *ControlsReadOnlyFields) GetIsInheritedOk() (*bool, bool)`

GetIsInheritedOk returns a tuple with the IsInherited field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsInherited

`func (o *ControlsReadOnlyFields) SetIsInherited(v bool)`

SetIsInherited sets IsInherited field to given value.

### HasIsInherited

`func (o *ControlsReadOnlyFields) HasIsInherited() bool`

HasIsInherited returns a boolean if a field has been set.

### SetIsInheritedNil

`func (o *ControlsReadOnlyFields) SetIsInheritedNil(b bool)`

 SetIsInheritedNil sets the value for IsInherited to be an explicit nil

### UnsetIsInherited
`func (o *ControlsReadOnlyFields) UnsetIsInherited()`

UnsetIsInherited ensures that no value is present for IsInherited, not even an explicit nil
### GetModifiedByOverlays

`func (o *ControlsReadOnlyFields) GetModifiedByOverlays() string`

GetModifiedByOverlays returns the ModifiedByOverlays field if non-nil, zero value otherwise.

### GetModifiedByOverlaysOk

`func (o *ControlsReadOnlyFields) GetModifiedByOverlaysOk() (*string, bool)`

GetModifiedByOverlaysOk returns a tuple with the ModifiedByOverlays field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetModifiedByOverlays

`func (o *ControlsReadOnlyFields) SetModifiedByOverlays(v string)`

SetModifiedByOverlays sets ModifiedByOverlays field to given value.

### HasModifiedByOverlays

`func (o *ControlsReadOnlyFields) HasModifiedByOverlays() bool`

HasModifiedByOverlays returns a boolean if a field has been set.

### SetModifiedByOverlaysNil

`func (o *ControlsReadOnlyFields) SetModifiedByOverlaysNil(b bool)`

 SetModifiedByOverlaysNil sets the value for ModifiedByOverlays to be an explicit nil

### UnsetModifiedByOverlays
`func (o *ControlsReadOnlyFields) UnsetModifiedByOverlays()`

UnsetModifiedByOverlays ensures that no value is present for ModifiedByOverlays, not even an explicit nil
### GetIncludedStatus

`func (o *ControlsReadOnlyFields) GetIncludedStatus() string`

GetIncludedStatus returns the IncludedStatus field if non-nil, zero value otherwise.

### GetIncludedStatusOk

`func (o *ControlsReadOnlyFields) GetIncludedStatusOk() (*string, bool)`

GetIncludedStatusOk returns a tuple with the IncludedStatus field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIncludedStatus

`func (o *ControlsReadOnlyFields) SetIncludedStatus(v string)`

SetIncludedStatus sets IncludedStatus field to given value.

### HasIncludedStatus

`func (o *ControlsReadOnlyFields) HasIncludedStatus() bool`

HasIncludedStatus returns a boolean if a field has been set.

### SetIncludedStatusNil

`func (o *ControlsReadOnlyFields) SetIncludedStatusNil(b bool)`

 SetIncludedStatusNil sets the value for IncludedStatus to be an explicit nil

### UnsetIncludedStatus
`func (o *ControlsReadOnlyFields) UnsetIncludedStatus()`

UnsetIncludedStatus ensures that no value is present for IncludedStatus, not even an explicit nil
### GetComplianceStatus

`func (o *ControlsReadOnlyFields) GetComplianceStatus() string`

GetComplianceStatus returns the ComplianceStatus field if non-nil, zero value otherwise.

### GetComplianceStatusOk

`func (o *ControlsReadOnlyFields) GetComplianceStatusOk() (*string, bool)`

GetComplianceStatusOk returns a tuple with the ComplianceStatus field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetComplianceStatus

`func (o *ControlsReadOnlyFields) SetComplianceStatus(v string)`

SetComplianceStatus sets ComplianceStatus field to given value.

### HasComplianceStatus

`func (o *ControlsReadOnlyFields) HasComplianceStatus() bool`

HasComplianceStatus returns a boolean if a field has been set.

### SetComplianceStatusNil

`func (o *ControlsReadOnlyFields) SetComplianceStatusNil(b bool)`

 SetComplianceStatusNil sets the value for ComplianceStatus to be an explicit nil

### UnsetComplianceStatus
`func (o *ControlsReadOnlyFields) UnsetComplianceStatus()`

UnsetComplianceStatus ensures that no value is present for ComplianceStatus, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


