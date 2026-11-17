# ControlsConditionalFields

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**CommonControlProvider** | Pointer to **NullableString** | [Conditional] Indicate the type of Common Control Provider for an Inherited Security Control. | [optional] 
**NaJustification** | Pointer to **NullableString** | [Conditional] Provide justification for Security Controls deemed Not Applicable to the system. | [optional] 
**SlcmCriticality** | Pointer to **NullableString** | [Conditional] Criticality of Security Control regarding SLCM. Character Limit &#x3D; 2,000. | [optional] 
**SlcmFrequency** | Pointer to **NullableString** | [Conditional] SLCM frequency | [optional] 
**SlcmMethod** | Pointer to **NullableString** | [Conditional] SLCM method utilized | [optional] 
**SlcmReporting** | Pointer to **NullableString** | [Conditional] Method for reporting Security Control for SLCM. Character Limit &#x3D; 2,000. | [optional] 
**SlcmTracking** | Pointer to **NullableString** | [Conditional] How Non-Compliant Security Controls will be tracked for SLCM. Character Limit &#x3D; 2,000. | [optional] 
**SlcmComments** | Pointer to **NullableString** | [Conditional] Additional comments for Security Control regarding SLCM. Character Limit &#x3D; 4,000. | [optional] 

## Methods

### NewControlsConditionalFields

`func NewControlsConditionalFields() *ControlsConditionalFields`

NewControlsConditionalFields instantiates a new ControlsConditionalFields object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewControlsConditionalFieldsWithDefaults

`func NewControlsConditionalFieldsWithDefaults() *ControlsConditionalFields`

NewControlsConditionalFieldsWithDefaults instantiates a new ControlsConditionalFields object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCommonControlProvider

`func (o *ControlsConditionalFields) GetCommonControlProvider() string`

GetCommonControlProvider returns the CommonControlProvider field if non-nil, zero value otherwise.

### GetCommonControlProviderOk

`func (o *ControlsConditionalFields) GetCommonControlProviderOk() (*string, bool)`

GetCommonControlProviderOk returns a tuple with the CommonControlProvider field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCommonControlProvider

`func (o *ControlsConditionalFields) SetCommonControlProvider(v string)`

SetCommonControlProvider sets CommonControlProvider field to given value.

### HasCommonControlProvider

`func (o *ControlsConditionalFields) HasCommonControlProvider() bool`

HasCommonControlProvider returns a boolean if a field has been set.

### SetCommonControlProviderNil

`func (o *ControlsConditionalFields) SetCommonControlProviderNil(b bool)`

 SetCommonControlProviderNil sets the value for CommonControlProvider to be an explicit nil

### UnsetCommonControlProvider
`func (o *ControlsConditionalFields) UnsetCommonControlProvider()`

UnsetCommonControlProvider ensures that no value is present for CommonControlProvider, not even an explicit nil
### GetNaJustification

`func (o *ControlsConditionalFields) GetNaJustification() string`

GetNaJustification returns the NaJustification field if non-nil, zero value otherwise.

### GetNaJustificationOk

`func (o *ControlsConditionalFields) GetNaJustificationOk() (*string, bool)`

GetNaJustificationOk returns a tuple with the NaJustification field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNaJustification

`func (o *ControlsConditionalFields) SetNaJustification(v string)`

SetNaJustification sets NaJustification field to given value.

### HasNaJustification

`func (o *ControlsConditionalFields) HasNaJustification() bool`

HasNaJustification returns a boolean if a field has been set.

### SetNaJustificationNil

`func (o *ControlsConditionalFields) SetNaJustificationNil(b bool)`

 SetNaJustificationNil sets the value for NaJustification to be an explicit nil

### UnsetNaJustification
`func (o *ControlsConditionalFields) UnsetNaJustification()`

UnsetNaJustification ensures that no value is present for NaJustification, not even an explicit nil
### GetSlcmCriticality

`func (o *ControlsConditionalFields) GetSlcmCriticality() string`

GetSlcmCriticality returns the SlcmCriticality field if non-nil, zero value otherwise.

### GetSlcmCriticalityOk

`func (o *ControlsConditionalFields) GetSlcmCriticalityOk() (*string, bool)`

GetSlcmCriticalityOk returns a tuple with the SlcmCriticality field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSlcmCriticality

`func (o *ControlsConditionalFields) SetSlcmCriticality(v string)`

SetSlcmCriticality sets SlcmCriticality field to given value.

### HasSlcmCriticality

`func (o *ControlsConditionalFields) HasSlcmCriticality() bool`

HasSlcmCriticality returns a boolean if a field has been set.

### SetSlcmCriticalityNil

`func (o *ControlsConditionalFields) SetSlcmCriticalityNil(b bool)`

 SetSlcmCriticalityNil sets the value for SlcmCriticality to be an explicit nil

### UnsetSlcmCriticality
`func (o *ControlsConditionalFields) UnsetSlcmCriticality()`

UnsetSlcmCriticality ensures that no value is present for SlcmCriticality, not even an explicit nil
### GetSlcmFrequency

`func (o *ControlsConditionalFields) GetSlcmFrequency() string`

GetSlcmFrequency returns the SlcmFrequency field if non-nil, zero value otherwise.

### GetSlcmFrequencyOk

`func (o *ControlsConditionalFields) GetSlcmFrequencyOk() (*string, bool)`

GetSlcmFrequencyOk returns a tuple with the SlcmFrequency field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSlcmFrequency

`func (o *ControlsConditionalFields) SetSlcmFrequency(v string)`

SetSlcmFrequency sets SlcmFrequency field to given value.

### HasSlcmFrequency

`func (o *ControlsConditionalFields) HasSlcmFrequency() bool`

HasSlcmFrequency returns a boolean if a field has been set.

### SetSlcmFrequencyNil

`func (o *ControlsConditionalFields) SetSlcmFrequencyNil(b bool)`

 SetSlcmFrequencyNil sets the value for SlcmFrequency to be an explicit nil

### UnsetSlcmFrequency
`func (o *ControlsConditionalFields) UnsetSlcmFrequency()`

UnsetSlcmFrequency ensures that no value is present for SlcmFrequency, not even an explicit nil
### GetSlcmMethod

`func (o *ControlsConditionalFields) GetSlcmMethod() string`

GetSlcmMethod returns the SlcmMethod field if non-nil, zero value otherwise.

### GetSlcmMethodOk

`func (o *ControlsConditionalFields) GetSlcmMethodOk() (*string, bool)`

GetSlcmMethodOk returns a tuple with the SlcmMethod field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSlcmMethod

`func (o *ControlsConditionalFields) SetSlcmMethod(v string)`

SetSlcmMethod sets SlcmMethod field to given value.

### HasSlcmMethod

`func (o *ControlsConditionalFields) HasSlcmMethod() bool`

HasSlcmMethod returns a boolean if a field has been set.

### SetSlcmMethodNil

`func (o *ControlsConditionalFields) SetSlcmMethodNil(b bool)`

 SetSlcmMethodNil sets the value for SlcmMethod to be an explicit nil

### UnsetSlcmMethod
`func (o *ControlsConditionalFields) UnsetSlcmMethod()`

UnsetSlcmMethod ensures that no value is present for SlcmMethod, not even an explicit nil
### GetSlcmReporting

`func (o *ControlsConditionalFields) GetSlcmReporting() string`

GetSlcmReporting returns the SlcmReporting field if non-nil, zero value otherwise.

### GetSlcmReportingOk

`func (o *ControlsConditionalFields) GetSlcmReportingOk() (*string, bool)`

GetSlcmReportingOk returns a tuple with the SlcmReporting field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSlcmReporting

`func (o *ControlsConditionalFields) SetSlcmReporting(v string)`

SetSlcmReporting sets SlcmReporting field to given value.

### HasSlcmReporting

`func (o *ControlsConditionalFields) HasSlcmReporting() bool`

HasSlcmReporting returns a boolean if a field has been set.

### SetSlcmReportingNil

`func (o *ControlsConditionalFields) SetSlcmReportingNil(b bool)`

 SetSlcmReportingNil sets the value for SlcmReporting to be an explicit nil

### UnsetSlcmReporting
`func (o *ControlsConditionalFields) UnsetSlcmReporting()`

UnsetSlcmReporting ensures that no value is present for SlcmReporting, not even an explicit nil
### GetSlcmTracking

`func (o *ControlsConditionalFields) GetSlcmTracking() string`

GetSlcmTracking returns the SlcmTracking field if non-nil, zero value otherwise.

### GetSlcmTrackingOk

`func (o *ControlsConditionalFields) GetSlcmTrackingOk() (*string, bool)`

GetSlcmTrackingOk returns a tuple with the SlcmTracking field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSlcmTracking

`func (o *ControlsConditionalFields) SetSlcmTracking(v string)`

SetSlcmTracking sets SlcmTracking field to given value.

### HasSlcmTracking

`func (o *ControlsConditionalFields) HasSlcmTracking() bool`

HasSlcmTracking returns a boolean if a field has been set.

### SetSlcmTrackingNil

`func (o *ControlsConditionalFields) SetSlcmTrackingNil(b bool)`

 SetSlcmTrackingNil sets the value for SlcmTracking to be an explicit nil

### UnsetSlcmTracking
`func (o *ControlsConditionalFields) UnsetSlcmTracking()`

UnsetSlcmTracking ensures that no value is present for SlcmTracking, not even an explicit nil
### GetSlcmComments

`func (o *ControlsConditionalFields) GetSlcmComments() string`

GetSlcmComments returns the SlcmComments field if non-nil, zero value otherwise.

### GetSlcmCommentsOk

`func (o *ControlsConditionalFields) GetSlcmCommentsOk() (*string, bool)`

GetSlcmCommentsOk returns a tuple with the SlcmComments field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSlcmComments

`func (o *ControlsConditionalFields) SetSlcmComments(v string)`

SetSlcmComments sets SlcmComments field to given value.

### HasSlcmComments

`func (o *ControlsConditionalFields) HasSlcmComments() bool`

HasSlcmComments returns a boolean if a field has been set.

### SetSlcmCommentsNil

`func (o *ControlsConditionalFields) SetSlcmCommentsNil(b bool)`

 SetSlcmCommentsNil sets the value for SlcmComments to be an explicit nil

### UnsetSlcmComments
`func (o *ControlsConditionalFields) UnsetSlcmComments()`

UnsetSlcmComments ensures that no value is present for SlcmComments, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


