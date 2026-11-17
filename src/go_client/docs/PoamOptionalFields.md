# PoamOptionalFields

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ExternalUid** | Pointer to **string** | [Optional] Unique identifier external to the eMASS application for use with associating POA&amp;Ms. 100 Characters. | [optional] 
**ControlAcronym** | Pointer to **string** | [Optional] Control acronym associated with the POA&amp;M Item. NIST SP 800-53 Revision 4 defined. | [optional] 
**AssessmentProcedure** | Pointer to **string** | [Optional] The Security Control Assessment Procedure being associated with the POA&amp;M Item. | [optional] 
**SecurityChecks** | Pointer to **string** | [Optional] Security Checks that are associated with the POA&amp;M. | [optional] 
**RawSeverity** | Pointer to **string** | [Optional] Scan vulnerability ratting Values include the following options: (Very Low, Low, Moderate,High,Very High) | [optional] 
**RelevanceOfThreat** | Pointer to **string** | [Optional] Values include the following options (Very Low, Low, Moderate,High,Very High) | [optional] 
**Likelihood** | Pointer to **string** | [Optional] Values include the following options (Very Low, Low, Moderate,High,Very High) | [optional] 
**Impact** | Pointer to **string** | [Optional] Values include the following options (Very Low, Low, Moderate,High,Very High) | [optional] 
**ImpactDescription** | Pointer to **string** | [Optional] Include description of Security Control&#39;s impact. | [optional] 
**ResidualRiskLevel** | Pointer to **string** | [Optional] Values include the following options (Very Low, Low, Moderate,High,Very High) | [optional] 
**Recommendations** | Pointer to **string** | [Optional] Include recommendations. Character Limit &#x3D; 2,000. | [optional] 
**Mitigations** | Pointer to **string** | [Optional] Include mitigation explanation. 2000 Characters. | [optional] 
**ResultingResidualRiskLevelAfterProposedMitigations** | Pointer to **NullableString** | [Optional] Indicate the risk level expected after any proposed mitigations are implemented. Proposed mitigations should be appropriately documented as POA&amp;M milestones. Navy only. | [optional] 
**PredisposingConditions** | Pointer to **NullableString** | [Optional] A predisposing condition is a condition existing within an organization, a mission or business process, enterprise architecture, information system/PIT, or environment of operation, which affects (i.e., increases or decreases) the likelihood that threat events, once initiated, result in adverse impacts. Navy only. | [optional] 
**ThreatDescription** | Pointer to **NullableString** | [Optional] Describe the identified threat(s) and relevance to the information system. Navy only. | [optional] 
**DevicesAffected** | Pointer to **NullableString** | [Optional] List any affected devices by hostname. If all devices in the information system are affected, state &#39;system&#39; or &#39;all&#39;. Navy only | [optional] 

## Methods

### NewPoamOptionalFields

`func NewPoamOptionalFields() *PoamOptionalFields`

NewPoamOptionalFields instantiates a new PoamOptionalFields object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPoamOptionalFieldsWithDefaults

`func NewPoamOptionalFieldsWithDefaults() *PoamOptionalFields`

NewPoamOptionalFieldsWithDefaults instantiates a new PoamOptionalFields object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetExternalUid

`func (o *PoamOptionalFields) GetExternalUid() string`

GetExternalUid returns the ExternalUid field if non-nil, zero value otherwise.

### GetExternalUidOk

`func (o *PoamOptionalFields) GetExternalUidOk() (*string, bool)`

GetExternalUidOk returns a tuple with the ExternalUid field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExternalUid

`func (o *PoamOptionalFields) SetExternalUid(v string)`

SetExternalUid sets ExternalUid field to given value.

### HasExternalUid

`func (o *PoamOptionalFields) HasExternalUid() bool`

HasExternalUid returns a boolean if a field has been set.

### GetControlAcronym

`func (o *PoamOptionalFields) GetControlAcronym() string`

GetControlAcronym returns the ControlAcronym field if non-nil, zero value otherwise.

### GetControlAcronymOk

`func (o *PoamOptionalFields) GetControlAcronymOk() (*string, bool)`

GetControlAcronymOk returns a tuple with the ControlAcronym field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetControlAcronym

`func (o *PoamOptionalFields) SetControlAcronym(v string)`

SetControlAcronym sets ControlAcronym field to given value.

### HasControlAcronym

`func (o *PoamOptionalFields) HasControlAcronym() bool`

HasControlAcronym returns a boolean if a field has been set.

### GetAssessmentProcedure

`func (o *PoamOptionalFields) GetAssessmentProcedure() string`

GetAssessmentProcedure returns the AssessmentProcedure field if non-nil, zero value otherwise.

### GetAssessmentProcedureOk

`func (o *PoamOptionalFields) GetAssessmentProcedureOk() (*string, bool)`

GetAssessmentProcedureOk returns a tuple with the AssessmentProcedure field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAssessmentProcedure

`func (o *PoamOptionalFields) SetAssessmentProcedure(v string)`

SetAssessmentProcedure sets AssessmentProcedure field to given value.

### HasAssessmentProcedure

`func (o *PoamOptionalFields) HasAssessmentProcedure() bool`

HasAssessmentProcedure returns a boolean if a field has been set.

### GetSecurityChecks

`func (o *PoamOptionalFields) GetSecurityChecks() string`

GetSecurityChecks returns the SecurityChecks field if non-nil, zero value otherwise.

### GetSecurityChecksOk

`func (o *PoamOptionalFields) GetSecurityChecksOk() (*string, bool)`

GetSecurityChecksOk returns a tuple with the SecurityChecks field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSecurityChecks

`func (o *PoamOptionalFields) SetSecurityChecks(v string)`

SetSecurityChecks sets SecurityChecks field to given value.

### HasSecurityChecks

`func (o *PoamOptionalFields) HasSecurityChecks() bool`

HasSecurityChecks returns a boolean if a field has been set.

### GetRawSeverity

`func (o *PoamOptionalFields) GetRawSeverity() string`

GetRawSeverity returns the RawSeverity field if non-nil, zero value otherwise.

### GetRawSeverityOk

`func (o *PoamOptionalFields) GetRawSeverityOk() (*string, bool)`

GetRawSeverityOk returns a tuple with the RawSeverity field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRawSeverity

`func (o *PoamOptionalFields) SetRawSeverity(v string)`

SetRawSeverity sets RawSeverity field to given value.

### HasRawSeverity

`func (o *PoamOptionalFields) HasRawSeverity() bool`

HasRawSeverity returns a boolean if a field has been set.

### GetRelevanceOfThreat

`func (o *PoamOptionalFields) GetRelevanceOfThreat() string`

GetRelevanceOfThreat returns the RelevanceOfThreat field if non-nil, zero value otherwise.

### GetRelevanceOfThreatOk

`func (o *PoamOptionalFields) GetRelevanceOfThreatOk() (*string, bool)`

GetRelevanceOfThreatOk returns a tuple with the RelevanceOfThreat field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRelevanceOfThreat

`func (o *PoamOptionalFields) SetRelevanceOfThreat(v string)`

SetRelevanceOfThreat sets RelevanceOfThreat field to given value.

### HasRelevanceOfThreat

`func (o *PoamOptionalFields) HasRelevanceOfThreat() bool`

HasRelevanceOfThreat returns a boolean if a field has been set.

### GetLikelihood

`func (o *PoamOptionalFields) GetLikelihood() string`

GetLikelihood returns the Likelihood field if non-nil, zero value otherwise.

### GetLikelihoodOk

`func (o *PoamOptionalFields) GetLikelihoodOk() (*string, bool)`

GetLikelihoodOk returns a tuple with the Likelihood field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLikelihood

`func (o *PoamOptionalFields) SetLikelihood(v string)`

SetLikelihood sets Likelihood field to given value.

### HasLikelihood

`func (o *PoamOptionalFields) HasLikelihood() bool`

HasLikelihood returns a boolean if a field has been set.

### GetImpact

`func (o *PoamOptionalFields) GetImpact() string`

GetImpact returns the Impact field if non-nil, zero value otherwise.

### GetImpactOk

`func (o *PoamOptionalFields) GetImpactOk() (*string, bool)`

GetImpactOk returns a tuple with the Impact field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetImpact

`func (o *PoamOptionalFields) SetImpact(v string)`

SetImpact sets Impact field to given value.

### HasImpact

`func (o *PoamOptionalFields) HasImpact() bool`

HasImpact returns a boolean if a field has been set.

### GetImpactDescription

`func (o *PoamOptionalFields) GetImpactDescription() string`

GetImpactDescription returns the ImpactDescription field if non-nil, zero value otherwise.

### GetImpactDescriptionOk

`func (o *PoamOptionalFields) GetImpactDescriptionOk() (*string, bool)`

GetImpactDescriptionOk returns a tuple with the ImpactDescription field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetImpactDescription

`func (o *PoamOptionalFields) SetImpactDescription(v string)`

SetImpactDescription sets ImpactDescription field to given value.

### HasImpactDescription

`func (o *PoamOptionalFields) HasImpactDescription() bool`

HasImpactDescription returns a boolean if a field has been set.

### GetResidualRiskLevel

`func (o *PoamOptionalFields) GetResidualRiskLevel() string`

GetResidualRiskLevel returns the ResidualRiskLevel field if non-nil, zero value otherwise.

### GetResidualRiskLevelOk

`func (o *PoamOptionalFields) GetResidualRiskLevelOk() (*string, bool)`

GetResidualRiskLevelOk returns a tuple with the ResidualRiskLevel field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetResidualRiskLevel

`func (o *PoamOptionalFields) SetResidualRiskLevel(v string)`

SetResidualRiskLevel sets ResidualRiskLevel field to given value.

### HasResidualRiskLevel

`func (o *PoamOptionalFields) HasResidualRiskLevel() bool`

HasResidualRiskLevel returns a boolean if a field has been set.

### GetRecommendations

`func (o *PoamOptionalFields) GetRecommendations() string`

GetRecommendations returns the Recommendations field if non-nil, zero value otherwise.

### GetRecommendationsOk

`func (o *PoamOptionalFields) GetRecommendationsOk() (*string, bool)`

GetRecommendationsOk returns a tuple with the Recommendations field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRecommendations

`func (o *PoamOptionalFields) SetRecommendations(v string)`

SetRecommendations sets Recommendations field to given value.

### HasRecommendations

`func (o *PoamOptionalFields) HasRecommendations() bool`

HasRecommendations returns a boolean if a field has been set.

### GetMitigations

`func (o *PoamOptionalFields) GetMitigations() string`

GetMitigations returns the Mitigations field if non-nil, zero value otherwise.

### GetMitigationsOk

`func (o *PoamOptionalFields) GetMitigationsOk() (*string, bool)`

GetMitigationsOk returns a tuple with the Mitigations field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMitigations

`func (o *PoamOptionalFields) SetMitigations(v string)`

SetMitigations sets Mitigations field to given value.

### HasMitigations

`func (o *PoamOptionalFields) HasMitigations() bool`

HasMitigations returns a boolean if a field has been set.

### GetResultingResidualRiskLevelAfterProposedMitigations

`func (o *PoamOptionalFields) GetResultingResidualRiskLevelAfterProposedMitigations() string`

GetResultingResidualRiskLevelAfterProposedMitigations returns the ResultingResidualRiskLevelAfterProposedMitigations field if non-nil, zero value otherwise.

### GetResultingResidualRiskLevelAfterProposedMitigationsOk

`func (o *PoamOptionalFields) GetResultingResidualRiskLevelAfterProposedMitigationsOk() (*string, bool)`

GetResultingResidualRiskLevelAfterProposedMitigationsOk returns a tuple with the ResultingResidualRiskLevelAfterProposedMitigations field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetResultingResidualRiskLevelAfterProposedMitigations

`func (o *PoamOptionalFields) SetResultingResidualRiskLevelAfterProposedMitigations(v string)`

SetResultingResidualRiskLevelAfterProposedMitigations sets ResultingResidualRiskLevelAfterProposedMitigations field to given value.

### HasResultingResidualRiskLevelAfterProposedMitigations

`func (o *PoamOptionalFields) HasResultingResidualRiskLevelAfterProposedMitigations() bool`

HasResultingResidualRiskLevelAfterProposedMitigations returns a boolean if a field has been set.

### SetResultingResidualRiskLevelAfterProposedMitigationsNil

`func (o *PoamOptionalFields) SetResultingResidualRiskLevelAfterProposedMitigationsNil(b bool)`

 SetResultingResidualRiskLevelAfterProposedMitigationsNil sets the value for ResultingResidualRiskLevelAfterProposedMitigations to be an explicit nil

### UnsetResultingResidualRiskLevelAfterProposedMitigations
`func (o *PoamOptionalFields) UnsetResultingResidualRiskLevelAfterProposedMitigations()`

UnsetResultingResidualRiskLevelAfterProposedMitigations ensures that no value is present for ResultingResidualRiskLevelAfterProposedMitigations, not even an explicit nil
### GetPredisposingConditions

`func (o *PoamOptionalFields) GetPredisposingConditions() string`

GetPredisposingConditions returns the PredisposingConditions field if non-nil, zero value otherwise.

### GetPredisposingConditionsOk

`func (o *PoamOptionalFields) GetPredisposingConditionsOk() (*string, bool)`

GetPredisposingConditionsOk returns a tuple with the PredisposingConditions field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPredisposingConditions

`func (o *PoamOptionalFields) SetPredisposingConditions(v string)`

SetPredisposingConditions sets PredisposingConditions field to given value.

### HasPredisposingConditions

`func (o *PoamOptionalFields) HasPredisposingConditions() bool`

HasPredisposingConditions returns a boolean if a field has been set.

### SetPredisposingConditionsNil

`func (o *PoamOptionalFields) SetPredisposingConditionsNil(b bool)`

 SetPredisposingConditionsNil sets the value for PredisposingConditions to be an explicit nil

### UnsetPredisposingConditions
`func (o *PoamOptionalFields) UnsetPredisposingConditions()`

UnsetPredisposingConditions ensures that no value is present for PredisposingConditions, not even an explicit nil
### GetThreatDescription

`func (o *PoamOptionalFields) GetThreatDescription() string`

GetThreatDescription returns the ThreatDescription field if non-nil, zero value otherwise.

### GetThreatDescriptionOk

`func (o *PoamOptionalFields) GetThreatDescriptionOk() (*string, bool)`

GetThreatDescriptionOk returns a tuple with the ThreatDescription field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetThreatDescription

`func (o *PoamOptionalFields) SetThreatDescription(v string)`

SetThreatDescription sets ThreatDescription field to given value.

### HasThreatDescription

`func (o *PoamOptionalFields) HasThreatDescription() bool`

HasThreatDescription returns a boolean if a field has been set.

### SetThreatDescriptionNil

`func (o *PoamOptionalFields) SetThreatDescriptionNil(b bool)`

 SetThreatDescriptionNil sets the value for ThreatDescription to be an explicit nil

### UnsetThreatDescription
`func (o *PoamOptionalFields) UnsetThreatDescription()`

UnsetThreatDescription ensures that no value is present for ThreatDescription, not even an explicit nil
### GetDevicesAffected

`func (o *PoamOptionalFields) GetDevicesAffected() string`

GetDevicesAffected returns the DevicesAffected field if non-nil, zero value otherwise.

### GetDevicesAffectedOk

`func (o *PoamOptionalFields) GetDevicesAffectedOk() (*string, bool)`

GetDevicesAffectedOk returns a tuple with the DevicesAffected field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDevicesAffected

`func (o *PoamOptionalFields) SetDevicesAffected(v string)`

SetDevicesAffected sets DevicesAffected field to given value.

### HasDevicesAffected

`func (o *PoamOptionalFields) HasDevicesAffected() bool`

HasDevicesAffected returns a boolean if a field has been set.

### SetDevicesAffectedNil

`func (o *PoamOptionalFields) SetDevicesAffectedNil(b bool)`

 SetDevicesAffectedNil sets the value for DevicesAffected to be an explicit nil

### UnsetDevicesAffected
`func (o *PoamOptionalFields) UnsetDevicesAffected()`

UnsetDevicesAffected ensures that no value is present for DevicesAffected, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


