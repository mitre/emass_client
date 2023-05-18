# emass_client.model.cmmc_get.CmmcGet

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**operation** | None, str,  | NoneClass, str,  | [Read-Only] Indicates the action that should be taken on the assessment record since the provided sinceDate. | [optional] must be one of ["ADDED", "UPDATED", "DELETED", ] 
**hqOrganizationName** | None, str,  | NoneClass, str,  | [Read-Only] The name of the DIB Company. | [optional] 
**uei** | None, str,  | NoneClass, str,  | [Read-Only] The Unique Entity Identifier assigned to the DIB Company. | [optional] 
**cageCodesInScope** | None, str,  | NoneClass, str,  | [Read-Only] The five position code(s) associated with the Organization Seeking Certification (OSC). | [optional] 
**oscName** | None, str,  | NoneClass, str,  | [Read-Only] The name of the Organization Seeking Certification. | [optional] 
**scope** | None, str,  | NoneClass, str,  | [Read-Only] The scope of the OSC assessment. | [optional] 
**scopeDescription** | None, str,  | NoneClass, str,  | [Read-Only] Brief description of the scope of the OSC assessment | [optional] 
**awardedCMMCLevel** | None, str,  | NoneClass, str,  | [Read-Only] The CMMC award level. | [optional] 
**expirationDate** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | [Read-Only] Expiration date of the awarded CMMC certification. | [optional] value must be a 64 bit integer
**assessmentId** | None, str,  | NoneClass, str,  | [Read-Only] Unique identifier for the assessment/certificate. | [optional] 
**modelVersion** | None, str,  | NoneClass, str,  | [Read-Only] Version of the CMMC Model used as part of the assessment. | [optional] 
**highestLevelCageCode** | None, str,  | NoneClass, str,  | [Read-Only] Identifies the highest-level CAGE Code associated with a given organization. | [optional] 
**certificationUniqueId** | None, str,  | NoneClass, str,  | [Read-Only] Identifies the unique ID that is associated with a given CMMC certification for an organization. | [optional] 
**poam** | None, bool,  | NoneClass, BoolClass,  | [Read-Only] Identifies whether any security requirements received a POA&amp;M during the assessment. | [optional] 
**overallScore** | decimal.Decimal, int,  | decimal.Decimal,  | [Read-Only] Identifies the overall calculated score for the assessment based on the assigned values to each applicable security requirement. | [optional] value must be a 64 bit integer
**oscAssessmentOfficialLastName** | None, str,  | NoneClass, str,  | [Read-Only] Last name of the company official contracting with the C3PAO for the assessment. | [optional] 
**oscAssessmentOfficialFirstName** | None, str,  | NoneClass, str,  | [Read-Only] First name of the company official contracting with the C3PAO for the assessment. | [optional] 
**oscAssessmentOfficialEmail** | None, str,  | NoneClass, str,  | [Read-Only] Email of the company official contracting with the C3PAO for the assessment. | [optional] 
**oscAssessmentOfficialTitle** | None, str,  | NoneClass, str,  | [Read-Only] Title of the company official contracting with the C3PAO for the assessment. | [optional] 
**[ssps](#ssps)** | list, tuple, None,  | tuple, NoneClass,  |  | [optional] 

# ssps

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Ssps**](Ssps.md) | [**Ssps**](Ssps.md) | [**Ssps**](Ssps.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

