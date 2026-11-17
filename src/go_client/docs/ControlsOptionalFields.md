# ControlsOptionalFields

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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

## Methods

### NewControlsOptionalFields

`func NewControlsOptionalFields() *ControlsOptionalFields`

NewControlsOptionalFields instantiates a new ControlsOptionalFields object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewControlsOptionalFieldsWithDefaults

`func NewControlsOptionalFieldsWithDefaults() *ControlsOptionalFields`

NewControlsOptionalFieldsWithDefaults instantiates a new ControlsOptionalFields object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetImplementationStatus

`func (o *ControlsOptionalFields) GetImplementationStatus() string`

GetImplementationStatus returns the ImplementationStatus field if non-nil, zero value otherwise.

### GetImplementationStatusOk

`func (o *ControlsOptionalFields) GetImplementationStatusOk() (*string, bool)`

GetImplementationStatusOk returns a tuple with the ImplementationStatus field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetImplementationStatus

`func (o *ControlsOptionalFields) SetImplementationStatus(v string)`

SetImplementationStatus sets ImplementationStatus field to given value.

### HasImplementationStatus

`func (o *ControlsOptionalFields) HasImplementationStatus() bool`

HasImplementationStatus returns a boolean if a field has been set.

### SetImplementationStatusNil

`func (o *ControlsOptionalFields) SetImplementationStatusNil(b bool)`

 SetImplementationStatusNil sets the value for ImplementationStatus to be an explicit nil

### UnsetImplementationStatus
`func (o *ControlsOptionalFields) UnsetImplementationStatus()`

UnsetImplementationStatus ensures that no value is present for ImplementationStatus, not even an explicit nil
### GetSeverity

`func (o *ControlsOptionalFields) GetSeverity() string`

GetSeverity returns the Severity field if non-nil, zero value otherwise.

### GetSeverityOk

`func (o *ControlsOptionalFields) GetSeverityOk() (*string, bool)`

GetSeverityOk returns a tuple with the Severity field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSeverity

`func (o *ControlsOptionalFields) SetSeverity(v string)`

SetSeverity sets Severity field to given value.

### HasSeverity

`func (o *ControlsOptionalFields) HasSeverity() bool`

HasSeverity returns a boolean if a field has been set.

### SetSeverityNil

`func (o *ControlsOptionalFields) SetSeverityNil(b bool)`

 SetSeverityNil sets the value for Severity to be an explicit nil

### UnsetSeverity
`func (o *ControlsOptionalFields) UnsetSeverity()`

UnsetSeverity ensures that no value is present for Severity, not even an explicit nil
### GetVulnerabiltySummary

`func (o *ControlsOptionalFields) GetVulnerabiltySummary() string`

GetVulnerabiltySummary returns the VulnerabiltySummary field if non-nil, zero value otherwise.

### GetVulnerabiltySummaryOk

`func (o *ControlsOptionalFields) GetVulnerabiltySummaryOk() (*string, bool)`

GetVulnerabiltySummaryOk returns a tuple with the VulnerabiltySummary field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVulnerabiltySummary

`func (o *ControlsOptionalFields) SetVulnerabiltySummary(v string)`

SetVulnerabiltySummary sets VulnerabiltySummary field to given value.

### HasVulnerabiltySummary

`func (o *ControlsOptionalFields) HasVulnerabiltySummary() bool`

HasVulnerabiltySummary returns a boolean if a field has been set.

### SetVulnerabiltySummaryNil

`func (o *ControlsOptionalFields) SetVulnerabiltySummaryNil(b bool)`

 SetVulnerabiltySummaryNil sets the value for VulnerabiltySummary to be an explicit nil

### UnsetVulnerabiltySummary
`func (o *ControlsOptionalFields) UnsetVulnerabiltySummary()`

UnsetVulnerabiltySummary ensures that no value is present for VulnerabiltySummary, not even an explicit nil
### GetRecommendations

`func (o *ControlsOptionalFields) GetRecommendations() string`

GetRecommendations returns the Recommendations field if non-nil, zero value otherwise.

### GetRecommendationsOk

`func (o *ControlsOptionalFields) GetRecommendationsOk() (*string, bool)`

GetRecommendationsOk returns a tuple with the Recommendations field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRecommendations

`func (o *ControlsOptionalFields) SetRecommendations(v string)`

SetRecommendations sets Recommendations field to given value.

### HasRecommendations

`func (o *ControlsOptionalFields) HasRecommendations() bool`

HasRecommendations returns a boolean if a field has been set.

### SetRecommendationsNil

`func (o *ControlsOptionalFields) SetRecommendationsNil(b bool)`

 SetRecommendationsNil sets the value for Recommendations to be an explicit nil

### UnsetRecommendations
`func (o *ControlsOptionalFields) UnsetRecommendations()`

UnsetRecommendations ensures that no value is present for Recommendations, not even an explicit nil
### GetRelevanceOfThreat

`func (o *ControlsOptionalFields) GetRelevanceOfThreat() string`

GetRelevanceOfThreat returns the RelevanceOfThreat field if non-nil, zero value otherwise.

### GetRelevanceOfThreatOk

`func (o *ControlsOptionalFields) GetRelevanceOfThreatOk() (*string, bool)`

GetRelevanceOfThreatOk returns a tuple with the RelevanceOfThreat field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRelevanceOfThreat

`func (o *ControlsOptionalFields) SetRelevanceOfThreat(v string)`

SetRelevanceOfThreat sets RelevanceOfThreat field to given value.

### HasRelevanceOfThreat

`func (o *ControlsOptionalFields) HasRelevanceOfThreat() bool`

HasRelevanceOfThreat returns a boolean if a field has been set.

### SetRelevanceOfThreatNil

`func (o *ControlsOptionalFields) SetRelevanceOfThreatNil(b bool)`

 SetRelevanceOfThreatNil sets the value for RelevanceOfThreat to be an explicit nil

### UnsetRelevanceOfThreat
`func (o *ControlsOptionalFields) UnsetRelevanceOfThreat()`

UnsetRelevanceOfThreat ensures that no value is present for RelevanceOfThreat, not even an explicit nil
### GetLikelihood

`func (o *ControlsOptionalFields) GetLikelihood() string`

GetLikelihood returns the Likelihood field if non-nil, zero value otherwise.

### GetLikelihoodOk

`func (o *ControlsOptionalFields) GetLikelihoodOk() (*string, bool)`

GetLikelihoodOk returns a tuple with the Likelihood field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLikelihood

`func (o *ControlsOptionalFields) SetLikelihood(v string)`

SetLikelihood sets Likelihood field to given value.

### HasLikelihood

`func (o *ControlsOptionalFields) HasLikelihood() bool`

HasLikelihood returns a boolean if a field has been set.

### SetLikelihoodNil

`func (o *ControlsOptionalFields) SetLikelihoodNil(b bool)`

 SetLikelihoodNil sets the value for Likelihood to be an explicit nil

### UnsetLikelihood
`func (o *ControlsOptionalFields) UnsetLikelihood()`

UnsetLikelihood ensures that no value is present for Likelihood, not even an explicit nil
### GetImpact

`func (o *ControlsOptionalFields) GetImpact() string`

GetImpact returns the Impact field if non-nil, zero value otherwise.

### GetImpactOk

`func (o *ControlsOptionalFields) GetImpactOk() (*string, bool)`

GetImpactOk returns a tuple with the Impact field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetImpact

`func (o *ControlsOptionalFields) SetImpact(v string)`

SetImpact sets Impact field to given value.

### HasImpact

`func (o *ControlsOptionalFields) HasImpact() bool`

HasImpact returns a boolean if a field has been set.

### SetImpactNil

`func (o *ControlsOptionalFields) SetImpactNil(b bool)`

 SetImpactNil sets the value for Impact to be an explicit nil

### UnsetImpact
`func (o *ControlsOptionalFields) UnsetImpact()`

UnsetImpact ensures that no value is present for Impact, not even an explicit nil
### GetImpactDescription

`func (o *ControlsOptionalFields) GetImpactDescription() string`

GetImpactDescription returns the ImpactDescription field if non-nil, zero value otherwise.

### GetImpactDescriptionOk

`func (o *ControlsOptionalFields) GetImpactDescriptionOk() (*string, bool)`

GetImpactDescriptionOk returns a tuple with the ImpactDescription field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetImpactDescription

`func (o *ControlsOptionalFields) SetImpactDescription(v string)`

SetImpactDescription sets ImpactDescription field to given value.

### HasImpactDescription

`func (o *ControlsOptionalFields) HasImpactDescription() bool`

HasImpactDescription returns a boolean if a field has been set.

### SetImpactDescriptionNil

`func (o *ControlsOptionalFields) SetImpactDescriptionNil(b bool)`

 SetImpactDescriptionNil sets the value for ImpactDescription to be an explicit nil

### UnsetImpactDescription
`func (o *ControlsOptionalFields) UnsetImpactDescription()`

UnsetImpactDescription ensures that no value is present for ImpactDescription, not even an explicit nil
### GetResidualRiskLevel

`func (o *ControlsOptionalFields) GetResidualRiskLevel() string`

GetResidualRiskLevel returns the ResidualRiskLevel field if non-nil, zero value otherwise.

### GetResidualRiskLevelOk

`func (o *ControlsOptionalFields) GetResidualRiskLevelOk() (*string, bool)`

GetResidualRiskLevelOk returns a tuple with the ResidualRiskLevel field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetResidualRiskLevel

`func (o *ControlsOptionalFields) SetResidualRiskLevel(v string)`

SetResidualRiskLevel sets ResidualRiskLevel field to given value.

### HasResidualRiskLevel

`func (o *ControlsOptionalFields) HasResidualRiskLevel() bool`

HasResidualRiskLevel returns a boolean if a field has been set.

### SetResidualRiskLevelNil

`func (o *ControlsOptionalFields) SetResidualRiskLevelNil(b bool)`

 SetResidualRiskLevelNil sets the value for ResidualRiskLevel to be an explicit nil

### UnsetResidualRiskLevel
`func (o *ControlsOptionalFields) UnsetResidualRiskLevel()`

UnsetResidualRiskLevel ensures that no value is present for ResidualRiskLevel, not even an explicit nil
### GetTestMethod

`func (o *ControlsOptionalFields) GetTestMethod() string`

GetTestMethod returns the TestMethod field if non-nil, zero value otherwise.

### GetTestMethodOk

`func (o *ControlsOptionalFields) GetTestMethodOk() (*string, bool)`

GetTestMethodOk returns a tuple with the TestMethod field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTestMethod

`func (o *ControlsOptionalFields) SetTestMethod(v string)`

SetTestMethod sets TestMethod field to given value.

### HasTestMethod

`func (o *ControlsOptionalFields) HasTestMethod() bool`

HasTestMethod returns a boolean if a field has been set.

### SetTestMethodNil

`func (o *ControlsOptionalFields) SetTestMethodNil(b bool)`

 SetTestMethodNil sets the value for TestMethod to be an explicit nil

### UnsetTestMethod
`func (o *ControlsOptionalFields) UnsetTestMethod()`

UnsetTestMethod ensures that no value is present for TestMethod, not even an explicit nil
### GetMitigations

`func (o *ControlsOptionalFields) GetMitigations() string`

GetMitigations returns the Mitigations field if non-nil, zero value otherwise.

### GetMitigationsOk

`func (o *ControlsOptionalFields) GetMitigationsOk() (*string, bool)`

GetMitigationsOk returns a tuple with the Mitigations field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMitigations

`func (o *ControlsOptionalFields) SetMitigations(v string)`

SetMitigations sets Mitigations field to given value.

### HasMitigations

`func (o *ControlsOptionalFields) HasMitigations() bool`

HasMitigations returns a boolean if a field has been set.

### SetMitigationsNil

`func (o *ControlsOptionalFields) SetMitigationsNil(b bool)`

 SetMitigationsNil sets the value for Mitigations to be an explicit nil

### UnsetMitigations
`func (o *ControlsOptionalFields) UnsetMitigations()`

UnsetMitigations ensures that no value is present for Mitigations, not even an explicit nil
### GetApplicationLayer

`func (o *ControlsOptionalFields) GetApplicationLayer() string`

GetApplicationLayer returns the ApplicationLayer field if non-nil, zero value otherwise.

### GetApplicationLayerOk

`func (o *ControlsOptionalFields) GetApplicationLayerOk() (*string, bool)`

GetApplicationLayerOk returns a tuple with the ApplicationLayer field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetApplicationLayer

`func (o *ControlsOptionalFields) SetApplicationLayer(v string)`

SetApplicationLayer sets ApplicationLayer field to given value.

### HasApplicationLayer

`func (o *ControlsOptionalFields) HasApplicationLayer() bool`

HasApplicationLayer returns a boolean if a field has been set.

### SetApplicationLayerNil

`func (o *ControlsOptionalFields) SetApplicationLayerNil(b bool)`

 SetApplicationLayerNil sets the value for ApplicationLayer to be an explicit nil

### UnsetApplicationLayer
`func (o *ControlsOptionalFields) UnsetApplicationLayer()`

UnsetApplicationLayer ensures that no value is present for ApplicationLayer, not even an explicit nil
### GetDatabaseLayer

`func (o *ControlsOptionalFields) GetDatabaseLayer() string`

GetDatabaseLayer returns the DatabaseLayer field if non-nil, zero value otherwise.

### GetDatabaseLayerOk

`func (o *ControlsOptionalFields) GetDatabaseLayerOk() (*string, bool)`

GetDatabaseLayerOk returns a tuple with the DatabaseLayer field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDatabaseLayer

`func (o *ControlsOptionalFields) SetDatabaseLayer(v string)`

SetDatabaseLayer sets DatabaseLayer field to given value.

### HasDatabaseLayer

`func (o *ControlsOptionalFields) HasDatabaseLayer() bool`

HasDatabaseLayer returns a boolean if a field has been set.

### SetDatabaseLayerNil

`func (o *ControlsOptionalFields) SetDatabaseLayerNil(b bool)`

 SetDatabaseLayerNil sets the value for DatabaseLayer to be an explicit nil

### UnsetDatabaseLayer
`func (o *ControlsOptionalFields) UnsetDatabaseLayer()`

UnsetDatabaseLayer ensures that no value is present for DatabaseLayer, not even an explicit nil
### GetOperatingSystemLayer

`func (o *ControlsOptionalFields) GetOperatingSystemLayer() string`

GetOperatingSystemLayer returns the OperatingSystemLayer field if non-nil, zero value otherwise.

### GetOperatingSystemLayerOk

`func (o *ControlsOptionalFields) GetOperatingSystemLayerOk() (*string, bool)`

GetOperatingSystemLayerOk returns a tuple with the OperatingSystemLayer field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOperatingSystemLayer

`func (o *ControlsOptionalFields) SetOperatingSystemLayer(v string)`

SetOperatingSystemLayer sets OperatingSystemLayer field to given value.

### HasOperatingSystemLayer

`func (o *ControlsOptionalFields) HasOperatingSystemLayer() bool`

HasOperatingSystemLayer returns a boolean if a field has been set.

### SetOperatingSystemLayerNil

`func (o *ControlsOptionalFields) SetOperatingSystemLayerNil(b bool)`

 SetOperatingSystemLayerNil sets the value for OperatingSystemLayer to be an explicit nil

### UnsetOperatingSystemLayer
`func (o *ControlsOptionalFields) UnsetOperatingSystemLayer()`

UnsetOperatingSystemLayer ensures that no value is present for OperatingSystemLayer, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


