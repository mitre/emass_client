# emass_client.model.poam_get.PoamGet

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**externalUid** | None, str,  | NoneClass, str,  | [Optional] Unique identifier external to the eMASS application for use with associating POA&amp;Ms. 100 Characters. | [optional] 
**systemId** | decimal.Decimal, int,  | decimal.Decimal,  | [Required] Unique eMASS system identifier. | [optional] value must be a 64 bit integer
**poamId** | decimal.Decimal, int,  | decimal.Decimal,  | [Required] Unique item identifier | [optional] value must be a 64 bit integer
**displayPoamId** | decimal.Decimal, int,  | decimal.Decimal,  | [Required] Globally unique identifier for individual POA&amp;M Items, seen on the front-end as “ID”. | [optional] value must be a 64 bit integer
**isInherited** | None, bool,  | NoneClass, BoolClass,  | [Read-only] Indicates whether a test result is inherited. | [optional] 
**controlAcronym** | None, str,  | NoneClass, str,  | [Optional] System acronym name. | [optional] 
**cci** | None, str,  | NoneClass, str,  | [Optional] CCI associated with POA&amp;M Item.. | [optional] 
**status** | str,  | str,  | [Required] Values include the following: (Ongoing,Risk Accepted,Completed,Not Applicable | [optional] must be one of ["Ongoing", "Risk Accepted", "Completed", "Not Applicable", "Archived", ] 
**reviewStatus** | None, str,  | NoneClass, str,  | [Read-Only] Values include the following options: (Not Approved,Under Review,Approved) | [optional] must be one of ["Not Approved", "Under Review", "Approved", ] 
**vulnerabilityDescription** | str,  | str,  | [Required] Provide a description of the POA&amp;M Item. 2000 Characters. | [optional] 
**sourceIdentVuln** | str,  | str,  | [Required] Include Source Identifying Vulnerability text. 2000 Characters. | [optional] 
**securityChecks** | None, str,  | NoneClass, str,  | [Optional] Security Checks that are associated with the POA&amp;M. | [optional] 
**[milestones](#milestones)** | list, tuple,  | tuple,  |  | [optional] 
**pocOrganization** | str,  | str,  | [Required] Organization/Office represented. 100 Characters. | [optional] 
**pocFirstName** | None, str,  | NoneClass, str,  | [Conditional] First name of POC. 100 Characters. | [optional] 
**pocLastName** | None, str,  | NoneClass, str,  | [Conditional] Last name of POC. 100 Characters. | [optional] 
**pocEmail** | None, str,  | NoneClass, str,  | [Conditional] Email address of POC. 100 Characters. | [optional] 
**pocPhoneNumber** | None, str,  | NoneClass, str,  | [Conditional] Phone number of POC. 100 Characters. | [optional] 
**severity** | None, str,  | NoneClass, str,  | [Conditional] Required for approved items. Values include the following options (Very Low,Low,Moderate,High,Very High) | [optional] must be one of ["Very Low", "Low", "Moderate", "High", "Very High", ] 
**rawSeverity** | None, str,  | NoneClass, str,  | [Optional] Values include the following options (I,II,III) | [optional] must be one of ["I", "II", "III", ] 
**relevanceOfThreat** | None, str,  | NoneClass, str,  | [Optional] Values include the following options: (Very Low,Low,Moderate,High,Very High) | [optional] must be one of ["Very Low", "Low", "Moderate", "High", "Very High", ] 
**likelihood** | None, str,  | NoneClass, str,  | [Optional] Values include the following options: (Very Low,Low,Moderate,High,Very High) | [optional] must be one of ["Very Low", "Low", "Moderate", "High", "Very High", ] 
**impact** | None, str,  | NoneClass, str,  | [Optional] Values include the following options: (Very Low,Low,Moderate,High,Very High) | [optional] must be one of ["Very Low", "Low", "Moderate", "High", "Very High", ] 
**impactDescription** | None, str,  | NoneClass, str,  | [Optional] Include description of Security Control’s impact. | [optional] 
**residualRiskLevel** | None, str,  | NoneClass, str,  | [Optional] Values include the following options: (Very Low,Low,Moderate,High,Very High) | [optional] must be one of ["Very Low", "Low", "Moderate", "High", "Very High", ] 
**recommendations** | None, str,  | NoneClass, str,  | [Optional] Include recommendations. Character Limit &#x3D; 2,000. | [optional] 
**resources** | str,  | str,  | [Required] List of resources used. 250 Characters. | [optional] 
**scheduledCompletionDate** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | [Conditional] Required for ongoing and completed POA&amp;M items. Unix time format. | [optional] value must be a 64 bit integer
**completionDate** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | [Conditional] Field is required for completed POA&amp;M items. Unix time format. | [optional] value must be a 64 bit integer
**extensionDate** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | [Read-Only] Value returned for a POA&amp;M Item with review status Approved” and has a milestone with a scheduled completion date that extends beyond the POA&amp;M Item’s scheduled completion date.  | [optional] value must be a 64 bit integer
**comments** | None, str,  | NoneClass, str,  | [Conditional] Field is required for completed and risk accepted POA&amp;M items. 2000 Characters | [optional] 
**mitigation** | None, str,  | NoneClass, str,  | [Optional] Include mitigation explanation. 2000 Characters. | [optional] 
**isActive** | None, bool,  | NoneClass, BoolClass,  | [Conditional] Optionally used in PUT to delete milestones when updating a POA&amp;M. | [optional] 

# milestones

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**MilestonesGet**](MilestonesGet.md) | [**MilestonesGet**](MilestonesGet.md) | [**MilestonesGet**](MilestonesGet.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

