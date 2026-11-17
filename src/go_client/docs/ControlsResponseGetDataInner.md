# ControlsResponseGetDataInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**SystemId** | Pointer to **int64** | [Required] Unique eMASS system identifier. | [optional] 
**Acronym** | Pointer to **string** | [Required] Acronym of the system record. | [optional] 
**ResponsibleEntities** | Pointer to **string** | [Required] Include written description of Responsible Entities that are responsible for the Security Control. Character Limit 2,000. | [optional] 
**ControlDesignation** | Pointer to **string** | [Required] Control designations | [optional] 
**EstimatedCompletionDate** | Pointer to **int64** | [Required] Field is required for Implementation Plan. Unix time format. | [optional] 
**ImplementationNarrative** | Pointer to **string** | [Required] Includes security control comments. Character Limit 2,000. | [optional] 
**CommonControlProvider** | Pointer to **NullableString** | [Conditional] Indicate the type of Common Control Provider for an Inherited Security Control. | [optional] 
**NaJustification** | Pointer to **NullableString** | [Conditional] Provide justification for Security Controls deemed Not Applicable to the system. | [optional] 
**SlcmCriticality** | Pointer to **NullableString** | [Conditional] Criticality of Security Control regarding SLCM. Character Limit &#x3D; 2,000. | [optional] 
**SlcmFrequency** | Pointer to **NullableString** | [Conditional] SLCM frequency | [optional] 
**SlcmMethod** | Pointer to **NullableString** | [Conditional] SLCM method utilized | [optional] 
**SlcmReporting** | Pointer to **NullableString** | [Conditional] Method for reporting Security Control for SLCM. Character Limit &#x3D; 2,000. | [optional] 
**SlcmTracking** | Pointer to **NullableString** | [Conditional] How Non-Compliant Security Controls will be tracked for SLCM. Character Limit &#x3D; 2,000. | [optional] 
**SlcmComments** | Pointer to **NullableString** | [Conditional] Additional comments for Security Control regarding SLCM. Character Limit &#x3D; 4,000. | [optional] 
**ImplementationStatus** | Pointer to **NullableString** | [Optional] Implementation Status of the Security Control for the information system. | [optional] 
**Severity** | Pointer to **NullableString** | [Optional] Values include the following options (Very Low, Low, Moderate,High,Very High) | [optional] 
**VulnerabiltySummary** | Pointer to **NullableString** | [Optional] Include vulnerability summary. Character Limit &#x3D; 2,000. | [optional] 
**Recommendations** | Pointer to **NullableString** | [Optional] Include recommendations. Character Limit &#x3D; 2,000. | [optional] 
**RelevanceOfThreat** | Pointer to **NullableString** | [Optional] Values include the following options (Very Low, Low, Moderate,High,Very High) | [optional] 
**Likelihood** | Pointer to **NullableString** | [Optional] Values include the following options (Very Low, Low, Moderate,High,Very High) | [optional] 
**Impact** | Pointer to **NullableString** | [Optional] Values include the following options (Very Low, Low, Moderate,High,Very High) | [optional] 
**ImpactDescription** | Pointer to **NullableString** | [Optional] Include description of Security Control&#39;s impact. | [optional] 
**ResidualRiskLevel** | Pointer to **NullableString** | [Optional] Values include the following options (Very Low, Low, Moderate,High,Very High) | [optional] 
**TestMethod** | Pointer to **NullableString** | [Optional] Identifies the assessment method / combination that will determine if the security requirements are implemented correctly. | [optional] 
**Mitigations** | Pointer to **NullableString** | [Optional] Identify any mitigations in place for the Non-Compliant Security Control&#39;s vulnerabilities. Character Limit &#x3D; 2,000. | [optional] 
**ApplicationLayer** | Pointer to **NullableString** | [Optional] If the Financial Management (Navy) overlay is applied to the system, this field appears and can be populated. Character Limit &#x3D; 2,000. Navy only. | [optional] 
**DatabaseLayer** | Pointer to **NullableString** | [Optional] If the Financial Management (Navy) overlay is applied to the system, this field appears and can be populated. Navy only. | [optional] 
**OperatingSystemLayer** | Pointer to **NullableString** | [Optional] If the Financial Management (Navy) overlay is applied to the system, this field appears and can be populated. Navy only. | [optional] 
**Name** | Pointer to **NullableString** | [Read-only] Name of the system record. | [optional] 
**Ccis** | Pointer to **NullableString** | [Read-only] Comma separated list of CCIs associated with the control. | [optional] 
**IsInherited** | Pointer to **NullableBool** | [Read-only] Indicates whether a control is inherited. | [optional] 
**ModifiedByOverlays** | Pointer to **NullableString** | [Read-only] List of overlays that affect the control. | [optional] 
**IncludedStatus** | Pointer to **NullableString** | [Read-only] Indicates the manner by which a control was included in the system&#39;s categorization. | [optional] 
**ComplianceStatus** | Pointer to **NullableString** | [Read-only] Compliance of the control. | [optional] 

## Methods

### NewControlsResponseGetDataInner

`func NewControlsResponseGetDataInner() *ControlsResponseGetDataInner`

NewControlsResponseGetDataInner instantiates a new ControlsResponseGetDataInner object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewControlsResponseGetDataInnerWithDefaults

`func NewControlsResponseGetDataInnerWithDefaults() *ControlsResponseGetDataInner`

NewControlsResponseGetDataInnerWithDefaults instantiates a new ControlsResponseGetDataInner object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetSystemId

`func (o *ControlsResponseGetDataInner) GetSystemId() int64`

GetSystemId returns the SystemId field if non-nil, zero value otherwise.

### GetSystemIdOk

`func (o *ControlsResponseGetDataInner) GetSystemIdOk() (*int64, bool)`

GetSystemIdOk returns a tuple with the SystemId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSystemId

`func (o *ControlsResponseGetDataInner) SetSystemId(v int64)`

SetSystemId sets SystemId field to given value.

### HasSystemId

`func (o *ControlsResponseGetDataInner) HasSystemId() bool`

HasSystemId returns a boolean if a field has been set.

### GetAcronym

`func (o *ControlsResponseGetDataInner) GetAcronym() string`

GetAcronym returns the Acronym field if non-nil, zero value otherwise.

### GetAcronymOk

`func (o *ControlsResponseGetDataInner) GetAcronymOk() (*string, bool)`

GetAcronymOk returns a tuple with the Acronym field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAcronym

`func (o *ControlsResponseGetDataInner) SetAcronym(v string)`

SetAcronym sets Acronym field to given value.

### HasAcronym

`func (o *ControlsResponseGetDataInner) HasAcronym() bool`

HasAcronym returns a boolean if a field has been set.

### GetResponsibleEntities

`func (o *ControlsResponseGetDataInner) GetResponsibleEntities() string`

GetResponsibleEntities returns the ResponsibleEntities field if non-nil, zero value otherwise.

### GetResponsibleEntitiesOk

`func (o *ControlsResponseGetDataInner) GetResponsibleEntitiesOk() (*string, bool)`

GetResponsibleEntitiesOk returns a tuple with the ResponsibleEntities field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetResponsibleEntities

`func (o *ControlsResponseGetDataInner) SetResponsibleEntities(v string)`

SetResponsibleEntities sets ResponsibleEntities field to given value.

### HasResponsibleEntities

`func (o *ControlsResponseGetDataInner) HasResponsibleEntities() bool`

HasResponsibleEntities returns a boolean if a field has been set.

### GetControlDesignation

`func (o *ControlsResponseGetDataInner) GetControlDesignation() string`

GetControlDesignation returns the ControlDesignation field if non-nil, zero value otherwise.

### GetControlDesignationOk

`func (o *ControlsResponseGetDataInner) GetControlDesignationOk() (*string, bool)`

GetControlDesignationOk returns a tuple with the ControlDesignation field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetControlDesignation

`func (o *ControlsResponseGetDataInner) SetControlDesignation(v string)`

SetControlDesignation sets ControlDesignation field to given value.

### HasControlDesignation

`func (o *ControlsResponseGetDataInner) HasControlDesignation() bool`

HasControlDesignation returns a boolean if a field has been set.

### GetEstimatedCompletionDate

`func (o *ControlsResponseGetDataInner) GetEstimatedCompletionDate() int64`

GetEstimatedCompletionDate returns the EstimatedCompletionDate field if non-nil, zero value otherwise.

### GetEstimatedCompletionDateOk

`func (o *ControlsResponseGetDataInner) GetEstimatedCompletionDateOk() (*int64, bool)`

GetEstimatedCompletionDateOk returns a tuple with the EstimatedCompletionDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEstimatedCompletionDate

`func (o *ControlsResponseGetDataInner) SetEstimatedCompletionDate(v int64)`

SetEstimatedCompletionDate sets EstimatedCompletionDate field to given value.

### HasEstimatedCompletionDate

`func (o *ControlsResponseGetDataInner) HasEstimatedCompletionDate() bool`

HasEstimatedCompletionDate returns a boolean if a field has been set.

### GetImplementationNarrative

`func (o *ControlsResponseGetDataInner) GetImplementationNarrative() string`

GetImplementationNarrative returns the ImplementationNarrative field if non-nil, zero value otherwise.

### GetImplementationNarrativeOk

`func (o *ControlsResponseGetDataInner) GetImplementationNarrativeOk() (*string, bool)`

GetImplementationNarrativeOk returns a tuple with the ImplementationNarrative field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetImplementationNarrative

`func (o *ControlsResponseGetDataInner) SetImplementationNarrative(v string)`

SetImplementationNarrative sets ImplementationNarrative field to given value.

### HasImplementationNarrative

`func (o *ControlsResponseGetDataInner) HasImplementationNarrative() bool`

HasImplementationNarrative returns a boolean if a field has been set.

### GetCommonControlProvider

`func (o *ControlsResponseGetDataInner) GetCommonControlProvider() string`

GetCommonControlProvider returns the CommonControlProvider field if non-nil, zero value otherwise.

### GetCommonControlProviderOk

`func (o *ControlsResponseGetDataInner) GetCommonControlProviderOk() (*string, bool)`

GetCommonControlProviderOk returns a tuple with the CommonControlProvider field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCommonControlProvider

`func (o *ControlsResponseGetDataInner) SetCommonControlProvider(v string)`

SetCommonControlProvider sets CommonControlProvider field to given value.

### HasCommonControlProvider

`func (o *ControlsResponseGetDataInner) HasCommonControlProvider() bool`

HasCommonControlProvider returns a boolean if a field has been set.

### SetCommonControlProviderNil

`func (o *ControlsResponseGetDataInner) SetCommonControlProviderNil(b bool)`

 SetCommonControlProviderNil sets the value for CommonControlProvider to be an explicit nil

### UnsetCommonControlProvider
`func (o *ControlsResponseGetDataInner) UnsetCommonControlProvider()`

UnsetCommonControlProvider ensures that no value is present for CommonControlProvider, not even an explicit nil
### GetNaJustification

`func (o *ControlsResponseGetDataInner) GetNaJustification() string`

GetNaJustification returns the NaJustification field if non-nil, zero value otherwise.

### GetNaJustificationOk

`func (o *ControlsResponseGetDataInner) GetNaJustificationOk() (*string, bool)`

GetNaJustificationOk returns a tuple with the NaJustification field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNaJustification

`func (o *ControlsResponseGetDataInner) SetNaJustification(v string)`

SetNaJustification sets NaJustification field to given value.

### HasNaJustification

`func (o *ControlsResponseGetDataInner) HasNaJustification() bool`

HasNaJustification returns a boolean if a field has been set.

### SetNaJustificationNil

`func (o *ControlsResponseGetDataInner) SetNaJustificationNil(b bool)`

 SetNaJustificationNil sets the value for NaJustification to be an explicit nil

### UnsetNaJustification
`func (o *ControlsResponseGetDataInner) UnsetNaJustification()`

UnsetNaJustification ensures that no value is present for NaJustification, not even an explicit nil
### GetSlcmCriticality

`func (o *ControlsResponseGetDataInner) GetSlcmCriticality() string`

GetSlcmCriticality returns the SlcmCriticality field if non-nil, zero value otherwise.

### GetSlcmCriticalityOk

`func (o *ControlsResponseGetDataInner) GetSlcmCriticalityOk() (*string, bool)`

GetSlcmCriticalityOk returns a tuple with the SlcmCriticality field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSlcmCriticality

`func (o *ControlsResponseGetDataInner) SetSlcmCriticality(v string)`

SetSlcmCriticality sets SlcmCriticality field to given value.

### HasSlcmCriticality

`func (o *ControlsResponseGetDataInner) HasSlcmCriticality() bool`

HasSlcmCriticality returns a boolean if a field has been set.

### SetSlcmCriticalityNil

`func (o *ControlsResponseGetDataInner) SetSlcmCriticalityNil(b bool)`

 SetSlcmCriticalityNil sets the value for SlcmCriticality to be an explicit nil

### UnsetSlcmCriticality
`func (o *ControlsResponseGetDataInner) UnsetSlcmCriticality()`

UnsetSlcmCriticality ensures that no value is present for SlcmCriticality, not even an explicit nil
### GetSlcmFrequency

`func (o *ControlsResponseGetDataInner) GetSlcmFrequency() string`

GetSlcmFrequency returns the SlcmFrequency field if non-nil, zero value otherwise.

### GetSlcmFrequencyOk

`func (o *ControlsResponseGetDataInner) GetSlcmFrequencyOk() (*string, bool)`

GetSlcmFrequencyOk returns a tuple with the SlcmFrequency field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSlcmFrequency

`func (o *ControlsResponseGetDataInner) SetSlcmFrequency(v string)`

SetSlcmFrequency sets SlcmFrequency field to given value.

### HasSlcmFrequency

`func (o *ControlsResponseGetDataInner) HasSlcmFrequency() bool`

HasSlcmFrequency returns a boolean if a field has been set.

### SetSlcmFrequencyNil

`func (o *ControlsResponseGetDataInner) SetSlcmFrequencyNil(b bool)`

 SetSlcmFrequencyNil sets the value for SlcmFrequency to be an explicit nil

### UnsetSlcmFrequency
`func (o *ControlsResponseGetDataInner) UnsetSlcmFrequency()`

UnsetSlcmFrequency ensures that no value is present for SlcmFrequency, not even an explicit nil
### GetSlcmMethod

`func (o *ControlsResponseGetDataInner) GetSlcmMethod() string`

GetSlcmMethod returns the SlcmMethod field if non-nil, zero value otherwise.

### GetSlcmMethodOk

`func (o *ControlsResponseGetDataInner) GetSlcmMethodOk() (*string, bool)`

GetSlcmMethodOk returns a tuple with the SlcmMethod field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSlcmMethod

`func (o *ControlsResponseGetDataInner) SetSlcmMethod(v string)`

SetSlcmMethod sets SlcmMethod field to given value.

### HasSlcmMethod

`func (o *ControlsResponseGetDataInner) HasSlcmMethod() bool`

HasSlcmMethod returns a boolean if a field has been set.

### SetSlcmMethodNil

`func (o *ControlsResponseGetDataInner) SetSlcmMethodNil(b bool)`

 SetSlcmMethodNil sets the value for SlcmMethod to be an explicit nil

### UnsetSlcmMethod
`func (o *ControlsResponseGetDataInner) UnsetSlcmMethod()`

UnsetSlcmMethod ensures that no value is present for SlcmMethod, not even an explicit nil
### GetSlcmReporting

`func (o *ControlsResponseGetDataInner) GetSlcmReporting() string`

GetSlcmReporting returns the SlcmReporting field if non-nil, zero value otherwise.

### GetSlcmReportingOk

`func (o *ControlsResponseGetDataInner) GetSlcmReportingOk() (*string, bool)`

GetSlcmReportingOk returns a tuple with the SlcmReporting field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSlcmReporting

`func (o *ControlsResponseGetDataInner) SetSlcmReporting(v string)`

SetSlcmReporting sets SlcmReporting field to given value.

### HasSlcmReporting

`func (o *ControlsResponseGetDataInner) HasSlcmReporting() bool`

HasSlcmReporting returns a boolean if a field has been set.

### SetSlcmReportingNil

`func (o *ControlsResponseGetDataInner) SetSlcmReportingNil(b bool)`

 SetSlcmReportingNil sets the value for SlcmReporting to be an explicit nil

### UnsetSlcmReporting
`func (o *ControlsResponseGetDataInner) UnsetSlcmReporting()`

UnsetSlcmReporting ensures that no value is present for SlcmReporting, not even an explicit nil
### GetSlcmTracking

`func (o *ControlsResponseGetDataInner) GetSlcmTracking() string`

GetSlcmTracking returns the SlcmTracking field if non-nil, zero value otherwise.

### GetSlcmTrackingOk

`func (o *ControlsResponseGetDataInner) GetSlcmTrackingOk() (*string, bool)`

GetSlcmTrackingOk returns a tuple with the SlcmTracking field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSlcmTracking

`func (o *ControlsResponseGetDataInner) SetSlcmTracking(v string)`

SetSlcmTracking sets SlcmTracking field to given value.

### HasSlcmTracking

`func (o *ControlsResponseGetDataInner) HasSlcmTracking() bool`

HasSlcmTracking returns a boolean if a field has been set.

### SetSlcmTrackingNil

`func (o *ControlsResponseGetDataInner) SetSlcmTrackingNil(b bool)`

 SetSlcmTrackingNil sets the value for SlcmTracking to be an explicit nil

### UnsetSlcmTracking
`func (o *ControlsResponseGetDataInner) UnsetSlcmTracking()`

UnsetSlcmTracking ensures that no value is present for SlcmTracking, not even an explicit nil
### GetSlcmComments

`func (o *ControlsResponseGetDataInner) GetSlcmComments() string`

GetSlcmComments returns the SlcmComments field if non-nil, zero value otherwise.

### GetSlcmCommentsOk

`func (o *ControlsResponseGetDataInner) GetSlcmCommentsOk() (*string, bool)`

GetSlcmCommentsOk returns a tuple with the SlcmComments field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSlcmComments

`func (o *ControlsResponseGetDataInner) SetSlcmComments(v string)`

SetSlcmComments sets SlcmComments field to given value.

### HasSlcmComments

`func (o *ControlsResponseGetDataInner) HasSlcmComments() bool`

HasSlcmComments returns a boolean if a field has been set.

### SetSlcmCommentsNil

`func (o *ControlsResponseGetDataInner) SetSlcmCommentsNil(b bool)`

 SetSlcmCommentsNil sets the value for SlcmComments to be an explicit nil

### UnsetSlcmComments
`func (o *ControlsResponseGetDataInner) UnsetSlcmComments()`

UnsetSlcmComments ensures that no value is present for SlcmComments, not even an explicit nil
### GetImplementationStatus

`func (o *ControlsResponseGetDataInner) GetImplementationStatus() string`

GetImplementationStatus returns the ImplementationStatus field if non-nil, zero value otherwise.

### GetImplementationStatusOk

`func (o *ControlsResponseGetDataInner) GetImplementationStatusOk() (*string, bool)`

GetImplementationStatusOk returns a tuple with the ImplementationStatus field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetImplementationStatus

`func (o *ControlsResponseGetDataInner) SetImplementationStatus(v string)`

SetImplementationStatus sets ImplementationStatus field to given value.

### HasImplementationStatus

`func (o *ControlsResponseGetDataInner) HasImplementationStatus() bool`

HasImplementationStatus returns a boolean if a field has been set.

### SetImplementationStatusNil

`func (o *ControlsResponseGetDataInner) SetImplementationStatusNil(b bool)`

 SetImplementationStatusNil sets the value for ImplementationStatus to be an explicit nil

### UnsetImplementationStatus
`func (o *ControlsResponseGetDataInner) UnsetImplementationStatus()`

UnsetImplementationStatus ensures that no value is present for ImplementationStatus, not even an explicit nil
### GetSeverity

`func (o *ControlsResponseGetDataInner) GetSeverity() string`

GetSeverity returns the Severity field if non-nil, zero value otherwise.

### GetSeverityOk

`func (o *ControlsResponseGetDataInner) GetSeverityOk() (*string, bool)`

GetSeverityOk returns a tuple with the Severity field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSeverity

`func (o *ControlsResponseGetDataInner) SetSeverity(v string)`

SetSeverity sets Severity field to given value.

### HasSeverity

`func (o *ControlsResponseGetDataInner) HasSeverity() bool`

HasSeverity returns a boolean if a field has been set.

### SetSeverityNil

`func (o *ControlsResponseGetDataInner) SetSeverityNil(b bool)`

 SetSeverityNil sets the value for Severity to be an explicit nil

### UnsetSeverity
`func (o *ControlsResponseGetDataInner) UnsetSeverity()`

UnsetSeverity ensures that no value is present for Severity, not even an explicit nil
### GetVulnerabiltySummary

`func (o *ControlsResponseGetDataInner) GetVulnerabiltySummary() string`

GetVulnerabiltySummary returns the VulnerabiltySummary field if non-nil, zero value otherwise.

### GetVulnerabiltySummaryOk

`func (o *ControlsResponseGetDataInner) GetVulnerabiltySummaryOk() (*string, bool)`

GetVulnerabiltySummaryOk returns a tuple with the VulnerabiltySummary field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVulnerabiltySummary

`func (o *ControlsResponseGetDataInner) SetVulnerabiltySummary(v string)`

SetVulnerabiltySummary sets VulnerabiltySummary field to given value.

### HasVulnerabiltySummary

`func (o *ControlsResponseGetDataInner) HasVulnerabiltySummary() bool`

HasVulnerabiltySummary returns a boolean if a field has been set.

### SetVulnerabiltySummaryNil

`func (o *ControlsResponseGetDataInner) SetVulnerabiltySummaryNil(b bool)`

 SetVulnerabiltySummaryNil sets the value for VulnerabiltySummary to be an explicit nil

### UnsetVulnerabiltySummary
`func (o *ControlsResponseGetDataInner) UnsetVulnerabiltySummary()`

UnsetVulnerabiltySummary ensures that no value is present for VulnerabiltySummary, not even an explicit nil
### GetRecommendations

`func (o *ControlsResponseGetDataInner) GetRecommendations() string`

GetRecommendations returns the Recommendations field if non-nil, zero value otherwise.

### GetRecommendationsOk

`func (o *ControlsResponseGetDataInner) GetRecommendationsOk() (*string, bool)`

GetRecommendationsOk returns a tuple with the Recommendations field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRecommendations

`func (o *ControlsResponseGetDataInner) SetRecommendations(v string)`

SetRecommendations sets Recommendations field to given value.

### HasRecommendations

`func (o *ControlsResponseGetDataInner) HasRecommendations() bool`

HasRecommendations returns a boolean if a field has been set.

### SetRecommendationsNil

`func (o *ControlsResponseGetDataInner) SetRecommendationsNil(b bool)`

 SetRecommendationsNil sets the value for Recommendations to be an explicit nil

### UnsetRecommendations
`func (o *ControlsResponseGetDataInner) UnsetRecommendations()`

UnsetRecommendations ensures that no value is present for Recommendations, not even an explicit nil
### GetRelevanceOfThreat

`func (o *ControlsResponseGetDataInner) GetRelevanceOfThreat() string`

GetRelevanceOfThreat returns the RelevanceOfThreat field if non-nil, zero value otherwise.

### GetRelevanceOfThreatOk

`func (o *ControlsResponseGetDataInner) GetRelevanceOfThreatOk() (*string, bool)`

GetRelevanceOfThreatOk returns a tuple with the RelevanceOfThreat field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRelevanceOfThreat

`func (o *ControlsResponseGetDataInner) SetRelevanceOfThreat(v string)`

SetRelevanceOfThreat sets RelevanceOfThreat field to given value.

### HasRelevanceOfThreat

`func (o *ControlsResponseGetDataInner) HasRelevanceOfThreat() bool`

HasRelevanceOfThreat returns a boolean if a field has been set.

### SetRelevanceOfThreatNil

`func (o *ControlsResponseGetDataInner) SetRelevanceOfThreatNil(b bool)`

 SetRelevanceOfThreatNil sets the value for RelevanceOfThreat to be an explicit nil

### UnsetRelevanceOfThreat
`func (o *ControlsResponseGetDataInner) UnsetRelevanceOfThreat()`

UnsetRelevanceOfThreat ensures that no value is present for RelevanceOfThreat, not even an explicit nil
### GetLikelihood

`func (o *ControlsResponseGetDataInner) GetLikelihood() string`

GetLikelihood returns the Likelihood field if non-nil, zero value otherwise.

### GetLikelihoodOk

`func (o *ControlsResponseGetDataInner) GetLikelihoodOk() (*string, bool)`

GetLikelihoodOk returns a tuple with the Likelihood field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLikelihood

`func (o *ControlsResponseGetDataInner) SetLikelihood(v string)`

SetLikelihood sets Likelihood field to given value.

### HasLikelihood

`func (o *ControlsResponseGetDataInner) HasLikelihood() bool`

HasLikelihood returns a boolean if a field has been set.

### SetLikelihoodNil

`func (o *ControlsResponseGetDataInner) SetLikelihoodNil(b bool)`

 SetLikelihoodNil sets the value for Likelihood to be an explicit nil

### UnsetLikelihood
`func (o *ControlsResponseGetDataInner) UnsetLikelihood()`

UnsetLikelihood ensures that no value is present for Likelihood, not even an explicit nil
### GetImpact

`func (o *ControlsResponseGetDataInner) GetImpact() string`

GetImpact returns the Impact field if non-nil, zero value otherwise.

### GetImpactOk

`func (o *ControlsResponseGetDataInner) GetImpactOk() (*string, bool)`

GetImpactOk returns a tuple with the Impact field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetImpact

`func (o *ControlsResponseGetDataInner) SetImpact(v string)`

SetImpact sets Impact field to given value.

### HasImpact

`func (o *ControlsResponseGetDataInner) HasImpact() bool`

HasImpact returns a boolean if a field has been set.

### SetImpactNil

`func (o *ControlsResponseGetDataInner) SetImpactNil(b bool)`

 SetImpactNil sets the value for Impact to be an explicit nil

### UnsetImpact
`func (o *ControlsResponseGetDataInner) UnsetImpact()`

UnsetImpact ensures that no value is present for Impact, not even an explicit nil
### GetImpactDescription

`func (o *ControlsResponseGetDataInner) GetImpactDescription() string`

GetImpactDescription returns the ImpactDescription field if non-nil, zero value otherwise.

### GetImpactDescriptionOk

`func (o *ControlsResponseGetDataInner) GetImpactDescriptionOk() (*string, bool)`

GetImpactDescriptionOk returns a tuple with the ImpactDescription field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetImpactDescription

`func (o *ControlsResponseGetDataInner) SetImpactDescription(v string)`

SetImpactDescription sets ImpactDescription field to given value.

### HasImpactDescription

`func (o *ControlsResponseGetDataInner) HasImpactDescription() bool`

HasImpactDescription returns a boolean if a field has been set.

### SetImpactDescriptionNil

`func (o *ControlsResponseGetDataInner) SetImpactDescriptionNil(b bool)`

 SetImpactDescriptionNil sets the value for ImpactDescription to be an explicit nil

### UnsetImpactDescription
`func (o *ControlsResponseGetDataInner) UnsetImpactDescription()`

UnsetImpactDescription ensures that no value is present for ImpactDescription, not even an explicit nil
### GetResidualRiskLevel

`func (o *ControlsResponseGetDataInner) GetResidualRiskLevel() string`

GetResidualRiskLevel returns the ResidualRiskLevel field if non-nil, zero value otherwise.

### GetResidualRiskLevelOk

`func (o *ControlsResponseGetDataInner) GetResidualRiskLevelOk() (*string, bool)`

GetResidualRiskLevelOk returns a tuple with the ResidualRiskLevel field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetResidualRiskLevel

`func (o *ControlsResponseGetDataInner) SetResidualRiskLevel(v string)`

SetResidualRiskLevel sets ResidualRiskLevel field to given value.

### HasResidualRiskLevel

`func (o *ControlsResponseGetDataInner) HasResidualRiskLevel() bool`

HasResidualRiskLevel returns a boolean if a field has been set.

### SetResidualRiskLevelNil

`func (o *ControlsResponseGetDataInner) SetResidualRiskLevelNil(b bool)`

 SetResidualRiskLevelNil sets the value for ResidualRiskLevel to be an explicit nil

### UnsetResidualRiskLevel
`func (o *ControlsResponseGetDataInner) UnsetResidualRiskLevel()`

UnsetResidualRiskLevel ensures that no value is present for ResidualRiskLevel, not even an explicit nil
### GetTestMethod

`func (o *ControlsResponseGetDataInner) GetTestMethod() string`

GetTestMethod returns the TestMethod field if non-nil, zero value otherwise.

### GetTestMethodOk

`func (o *ControlsResponseGetDataInner) GetTestMethodOk() (*string, bool)`

GetTestMethodOk returns a tuple with the TestMethod field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTestMethod

`func (o *ControlsResponseGetDataInner) SetTestMethod(v string)`

SetTestMethod sets TestMethod field to given value.

### HasTestMethod

`func (o *ControlsResponseGetDataInner) HasTestMethod() bool`

HasTestMethod returns a boolean if a field has been set.

### SetTestMethodNil

`func (o *ControlsResponseGetDataInner) SetTestMethodNil(b bool)`

 SetTestMethodNil sets the value for TestMethod to be an explicit nil

### UnsetTestMethod
`func (o *ControlsResponseGetDataInner) UnsetTestMethod()`

UnsetTestMethod ensures that no value is present for TestMethod, not even an explicit nil
### GetMitigations

`func (o *ControlsResponseGetDataInner) GetMitigations() string`

GetMitigations returns the Mitigations field if non-nil, zero value otherwise.

### GetMitigationsOk

`func (o *ControlsResponseGetDataInner) GetMitigationsOk() (*string, bool)`

GetMitigationsOk returns a tuple with the Mitigations field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMitigations

`func (o *ControlsResponseGetDataInner) SetMitigations(v string)`

SetMitigations sets Mitigations field to given value.

### HasMitigations

`func (o *ControlsResponseGetDataInner) HasMitigations() bool`

HasMitigations returns a boolean if a field has been set.

### SetMitigationsNil

`func (o *ControlsResponseGetDataInner) SetMitigationsNil(b bool)`

 SetMitigationsNil sets the value for Mitigations to be an explicit nil

### UnsetMitigations
`func (o *ControlsResponseGetDataInner) UnsetMitigations()`

UnsetMitigations ensures that no value is present for Mitigations, not even an explicit nil
### GetApplicationLayer

`func (o *ControlsResponseGetDataInner) GetApplicationLayer() string`

GetApplicationLayer returns the ApplicationLayer field if non-nil, zero value otherwise.

### GetApplicationLayerOk

`func (o *ControlsResponseGetDataInner) GetApplicationLayerOk() (*string, bool)`

GetApplicationLayerOk returns a tuple with the ApplicationLayer field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetApplicationLayer

`func (o *ControlsResponseGetDataInner) SetApplicationLayer(v string)`

SetApplicationLayer sets ApplicationLayer field to given value.

### HasApplicationLayer

`func (o *ControlsResponseGetDataInner) HasApplicationLayer() bool`

HasApplicationLayer returns a boolean if a field has been set.

### SetApplicationLayerNil

`func (o *ControlsResponseGetDataInner) SetApplicationLayerNil(b bool)`

 SetApplicationLayerNil sets the value for ApplicationLayer to be an explicit nil

### UnsetApplicationLayer
`func (o *ControlsResponseGetDataInner) UnsetApplicationLayer()`

UnsetApplicationLayer ensures that no value is present for ApplicationLayer, not even an explicit nil
### GetDatabaseLayer

`func (o *ControlsResponseGetDataInner) GetDatabaseLayer() string`

GetDatabaseLayer returns the DatabaseLayer field if non-nil, zero value otherwise.

### GetDatabaseLayerOk

`func (o *ControlsResponseGetDataInner) GetDatabaseLayerOk() (*string, bool)`

GetDatabaseLayerOk returns a tuple with the DatabaseLayer field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDatabaseLayer

`func (o *ControlsResponseGetDataInner) SetDatabaseLayer(v string)`

SetDatabaseLayer sets DatabaseLayer field to given value.

### HasDatabaseLayer

`func (o *ControlsResponseGetDataInner) HasDatabaseLayer() bool`

HasDatabaseLayer returns a boolean if a field has been set.

### SetDatabaseLayerNil

`func (o *ControlsResponseGetDataInner) SetDatabaseLayerNil(b bool)`

 SetDatabaseLayerNil sets the value for DatabaseLayer to be an explicit nil

### UnsetDatabaseLayer
`func (o *ControlsResponseGetDataInner) UnsetDatabaseLayer()`

UnsetDatabaseLayer ensures that no value is present for DatabaseLayer, not even an explicit nil
### GetOperatingSystemLayer

`func (o *ControlsResponseGetDataInner) GetOperatingSystemLayer() string`

GetOperatingSystemLayer returns the OperatingSystemLayer field if non-nil, zero value otherwise.

### GetOperatingSystemLayerOk

`func (o *ControlsResponseGetDataInner) GetOperatingSystemLayerOk() (*string, bool)`

GetOperatingSystemLayerOk returns a tuple with the OperatingSystemLayer field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOperatingSystemLayer

`func (o *ControlsResponseGetDataInner) SetOperatingSystemLayer(v string)`

SetOperatingSystemLayer sets OperatingSystemLayer field to given value.

### HasOperatingSystemLayer

`func (o *ControlsResponseGetDataInner) HasOperatingSystemLayer() bool`

HasOperatingSystemLayer returns a boolean if a field has been set.

### SetOperatingSystemLayerNil

`func (o *ControlsResponseGetDataInner) SetOperatingSystemLayerNil(b bool)`

 SetOperatingSystemLayerNil sets the value for OperatingSystemLayer to be an explicit nil

### UnsetOperatingSystemLayer
`func (o *ControlsResponseGetDataInner) UnsetOperatingSystemLayer()`

UnsetOperatingSystemLayer ensures that no value is present for OperatingSystemLayer, not even an explicit nil
### GetName

`func (o *ControlsResponseGetDataInner) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *ControlsResponseGetDataInner) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *ControlsResponseGetDataInner) SetName(v string)`

SetName sets Name field to given value.

### HasName

`func (o *ControlsResponseGetDataInner) HasName() bool`

HasName returns a boolean if a field has been set.

### SetNameNil

`func (o *ControlsResponseGetDataInner) SetNameNil(b bool)`

 SetNameNil sets the value for Name to be an explicit nil

### UnsetName
`func (o *ControlsResponseGetDataInner) UnsetName()`

UnsetName ensures that no value is present for Name, not even an explicit nil
### GetCcis

`func (o *ControlsResponseGetDataInner) GetCcis() string`

GetCcis returns the Ccis field if non-nil, zero value otherwise.

### GetCcisOk

`func (o *ControlsResponseGetDataInner) GetCcisOk() (*string, bool)`

GetCcisOk returns a tuple with the Ccis field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCcis

`func (o *ControlsResponseGetDataInner) SetCcis(v string)`

SetCcis sets Ccis field to given value.

### HasCcis

`func (o *ControlsResponseGetDataInner) HasCcis() bool`

HasCcis returns a boolean if a field has been set.

### SetCcisNil

`func (o *ControlsResponseGetDataInner) SetCcisNil(b bool)`

 SetCcisNil sets the value for Ccis to be an explicit nil

### UnsetCcis
`func (o *ControlsResponseGetDataInner) UnsetCcis()`

UnsetCcis ensures that no value is present for Ccis, not even an explicit nil
### GetIsInherited

`func (o *ControlsResponseGetDataInner) GetIsInherited() bool`

GetIsInherited returns the IsInherited field if non-nil, zero value otherwise.

### GetIsInheritedOk

`func (o *ControlsResponseGetDataInner) GetIsInheritedOk() (*bool, bool)`

GetIsInheritedOk returns a tuple with the IsInherited field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsInherited

`func (o *ControlsResponseGetDataInner) SetIsInherited(v bool)`

SetIsInherited sets IsInherited field to given value.

### HasIsInherited

`func (o *ControlsResponseGetDataInner) HasIsInherited() bool`

HasIsInherited returns a boolean if a field has been set.

### SetIsInheritedNil

`func (o *ControlsResponseGetDataInner) SetIsInheritedNil(b bool)`

 SetIsInheritedNil sets the value for IsInherited to be an explicit nil

### UnsetIsInherited
`func (o *ControlsResponseGetDataInner) UnsetIsInherited()`

UnsetIsInherited ensures that no value is present for IsInherited, not even an explicit nil
### GetModifiedByOverlays

`func (o *ControlsResponseGetDataInner) GetModifiedByOverlays() string`

GetModifiedByOverlays returns the ModifiedByOverlays field if non-nil, zero value otherwise.

### GetModifiedByOverlaysOk

`func (o *ControlsResponseGetDataInner) GetModifiedByOverlaysOk() (*string, bool)`

GetModifiedByOverlaysOk returns a tuple with the ModifiedByOverlays field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetModifiedByOverlays

`func (o *ControlsResponseGetDataInner) SetModifiedByOverlays(v string)`

SetModifiedByOverlays sets ModifiedByOverlays field to given value.

### HasModifiedByOverlays

`func (o *ControlsResponseGetDataInner) HasModifiedByOverlays() bool`

HasModifiedByOverlays returns a boolean if a field has been set.

### SetModifiedByOverlaysNil

`func (o *ControlsResponseGetDataInner) SetModifiedByOverlaysNil(b bool)`

 SetModifiedByOverlaysNil sets the value for ModifiedByOverlays to be an explicit nil

### UnsetModifiedByOverlays
`func (o *ControlsResponseGetDataInner) UnsetModifiedByOverlays()`

UnsetModifiedByOverlays ensures that no value is present for ModifiedByOverlays, not even an explicit nil
### GetIncludedStatus

`func (o *ControlsResponseGetDataInner) GetIncludedStatus() string`

GetIncludedStatus returns the IncludedStatus field if non-nil, zero value otherwise.

### GetIncludedStatusOk

`func (o *ControlsResponseGetDataInner) GetIncludedStatusOk() (*string, bool)`

GetIncludedStatusOk returns a tuple with the IncludedStatus field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIncludedStatus

`func (o *ControlsResponseGetDataInner) SetIncludedStatus(v string)`

SetIncludedStatus sets IncludedStatus field to given value.

### HasIncludedStatus

`func (o *ControlsResponseGetDataInner) HasIncludedStatus() bool`

HasIncludedStatus returns a boolean if a field has been set.

### SetIncludedStatusNil

`func (o *ControlsResponseGetDataInner) SetIncludedStatusNil(b bool)`

 SetIncludedStatusNil sets the value for IncludedStatus to be an explicit nil

### UnsetIncludedStatus
`func (o *ControlsResponseGetDataInner) UnsetIncludedStatus()`

UnsetIncludedStatus ensures that no value is present for IncludedStatus, not even an explicit nil
### GetComplianceStatus

`func (o *ControlsResponseGetDataInner) GetComplianceStatus() string`

GetComplianceStatus returns the ComplianceStatus field if non-nil, zero value otherwise.

### GetComplianceStatusOk

`func (o *ControlsResponseGetDataInner) GetComplianceStatusOk() (*string, bool)`

GetComplianceStatusOk returns a tuple with the ComplianceStatus field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetComplianceStatus

`func (o *ControlsResponseGetDataInner) SetComplianceStatus(v string)`

SetComplianceStatus sets ComplianceStatus field to given value.

### HasComplianceStatus

`func (o *ControlsResponseGetDataInner) HasComplianceStatus() bool`

HasComplianceStatus returns a boolean if a field has been set.

### SetComplianceStatusNil

`func (o *ControlsResponseGetDataInner) SetComplianceStatusNil(b bool)`

 SetComplianceStatusNil sets the value for ComplianceStatus to be an explicit nil

### UnsetComplianceStatus
`func (o *ControlsResponseGetDataInner) UnsetComplianceStatus()`

UnsetComplianceStatus ensures that no value is present for ComplianceStatus, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


