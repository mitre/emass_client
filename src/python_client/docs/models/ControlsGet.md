# emass_client.model.controls_get.ControlsGet

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**systemId** | decimal.Decimal, int,  | decimal.Decimal,  | [Required] Unique system record identifier. | [optional] value must be a 64 bit integer
**name** | None, str,  | NoneClass, str,  | [Read-only] Name of the system record. | [optional] 
**acronym** | str,  | str,  | [Required] Acronym of the system record. | [optional] 
**ccis** | None, str,  | NoneClass, str,  | [Read-only] Comma separated list of CCIs associated with the control. | [optional] 
**isInherited** | None, bool,  | NoneClass, BoolClass,  | [Read-only] Indicates whether a control is inherited. | [optional] 
**modifiedByOverlays** | None, str,  | NoneClass, str,  | [Read-only] List of overlays that affect the control. | [optional] must be one of ["Privacy", "Requirements", "Concurrency", ] 
**includedStatus** | None, str,  | NoneClass, str,  | [Read-only] Indicates the manner by which a control was included in the system’s categorization. | [optional] 
**complianceStatus** | None, str,  | NoneClass, str,  | [Read-only] Compliance of the control. | [optional] 
**responsibleEntities** | str,  | str,  | [Required] Include written description of Responsible Entities that are responsible for the Security Control. Character Limit &#x3D; 2,000. | [optional] 
**implementationStatus** | None, str,  | NoneClass, str,  | [Optional] Implementation Status of the Security Control for the information system. | [optional] must be one of ["Planned", "Implemented", "Inherited", "Not Applicable", "Manually Inherited", ] 
**commonControlProvider** | None, str,  | NoneClass, str,  | [Conditional] Indicate the type of Common Control Provider for an “Inherited” Security Control. | [optional] must be one of ["DoD", "Component", "Enclave", ] 
**naJustification** | None, str,  | NoneClass, str,  | [Conditional] Provide justification for Security Controls deemed Not Applicable to the system. | [optional] 
**controlDesignation** | str,  | str,  | [Required] Control designations | [optional] must be one of ["Common", "System-Specific", "Hybrid", ] 
**estimatedCompletionDate** | decimal.Decimal, int,  | decimal.Decimal,  | [Required] Field is required for Implementation Plan. | [optional] 
**implementationNarrative** | str,  | str,  | [Required] Includes security control comments. Character Limit &#x3D; 2,000. | [optional] 
**slcmCriticality** | None, str,  | NoneClass, str,  | [Conditional] Criticality of Security Control regarding SLCM. Character Limit &#x3D; 2,000. | [optional] 
**slcmFrequency** | None, str,  | NoneClass, str,  | [Conditional] SLCM frequency | [optional] must be one of ["Constantly", "Daily", "Weekly", "Monthly", "Quarterly", "Semi-Annually", "Annually", "Every Two Years", "Every Three Years", "Undetermined", ] 
**slcmMethod** | None, str,  | NoneClass, str,  | [Conditional] SLCM method utilized | [optional] must be one of ["Automated", "Semi-Automated", "Manual", "Undetermined", ] 
**slcmReporting** | None, str,  | NoneClass, str,  | [Conditional] Method for reporting Security Control for SLCM. Character Limit &#x3D; 2,000. | [optional] 
**slcmTracking** | None, str,  | NoneClass, str,  | [Conditional] How Non-Compliant Security Controls will be tracked for SLCM. Character Limit &#x3D; 2,000. | [optional] 
**slcmComments** | None, str,  | NoneClass, str,  | [Conditional] Additional comments for Security Control regarding SLCM. Character Limit &#x3D; 4,000. | [optional] 
**severity** | None, str,  | NoneClass, str,  | [Optional] Values include the following options (Very Low, Low, Moderate,High,Very High) | [optional] must be one of ["Very Low", "Low", "Moderate", "High", "Very High", ] 
**vulnerabiltySummary** | None, str,  | NoneClass, str,  | [Optional] Include vulnerability summary. Character Limit &#x3D; 2,000. | [optional] 
**recommendations** | None, str,  | NoneClass, str,  | [Optional] Include recommendations. Character Limit &#x3D; 2,000. | [optional] 
**relevanceOfThreat** | None, str,  | NoneClass, str,  | [Optional] Values include the following options (Very Low, Low, Moderate,High,Very High) | [optional] must be one of ["Very Low", "Low", "Moderate", "High", "Very High", ] 
**likelihood** | None, str,  | NoneClass, str,  | [Optional] Values include the following options (Very Low, Low, Moderate,High,Very High) | [optional] must be one of ["Very Low", "Low", "Moderate", "High", "Very High", ] 
**impact** | None, str,  | NoneClass, str,  | [Optional] Values include the following options (Very Low, Low, Moderate,High,Very High) | [optional] must be one of ["Very Low", "Low", "Moderate", "High", "Very High", ] 
**impactDescription** | None, str,  | NoneClass, str,  | [Optional] Include description of Security Control’s impact. | [optional] 
**residualRiskLevel** | None, str,  | NoneClass, str,  | [Optional] Values include the following options (Very Low, Low, Moderate,High,Very High) | [optional] must be one of ["Very Low", "Low", "Moderate", "High", "Very High", ] 
**testMethod** | None, str,  | NoneClass, str,  | [Optional] Identifies the assessment method / combination that will determine if the security requirements are implemented correctly. | [optional] must be one of ["Test", "Interview", "Examine", "Test, Interview", "Test, Examine", "Interview, Examine", "Test, Interview, Examine", ] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

