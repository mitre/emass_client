# CmmcGet


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation** | **str** | [Read-Only] Indicates the action that should be taken on the assessment record since the provided sinceDate. | [optional] 
**hq_organization_name** | **str** | [Read-Only] The name of the DIB Company. | [optional] 
**uei** | **str** | [Read-Only] The Unique Entity Identifier assigned to the DIB Company. | [optional] 
**cage_codes_in_scope** | **str** | [Read-Only] The five position code(s) associated with the Organization Seeking Certification (OSC). | [optional] 
**osc_name** | **str** | [Read-Only] The name of the Organization Seeking Certification. | [optional] 
**scope** | **str** | [Read-Only] The scope of the OSC assessment. | [optional] 
**scope_description** | **str** | [Read-Only] Brief description of the scope of the OSC assessment | [optional] 
**awarded_cmmc_level** | **str** | [Read-Only] The CMMC award level. | [optional] 
**expiration_date** | **int** | [Read-Only] Expiration date of the awarded CMMC certification. | [optional] 
**assessment_id** | **str** | [Read-Only] Unique identifier for the assessment/certificate. | [optional] 
**model_version** | **str** | [Read-Only] Version of the CMMC Model used as part of the assessment. | [optional] 
**highest_level_cage_code** | **str** | [Read-Only] Identifies the highest-level CAGE Code associated with a given organization. | [optional] 
**certification_unique_id** | **str** | [Read-Only] Identifies the unique ID that is associated with a given CMMC certification for an organization. | [optional] 
**poam** | **bool** | [Read-Only] Identifies whether any security requirements received a POA&amp;M during the assessment. | [optional] 
**overall_score** | **int** | [Read-Only] Identifies the overall calculated score for the assessment based on the assigned values to each applicable security requirement. | [optional] 
**osc_assessment_official_last_name** | **str** | [Read-Only] Last name of the company official contracting with the C3PAO for the assessment. | [optional] 
**osc_assessment_official_first_name** | **str** | [Read-Only] First name of the company official contracting with the C3PAO for the assessment. | [optional] 
**osc_assessment_official_email** | **str** | [Read-Only] Email of the company official contracting with the C3PAO for the assessment. | [optional] 
**osc_assessment_official_title** | **str** | [Read-Only] Title of the company official contracting with the C3PAO for the assessment. | [optional] 
**ssps** | [**List[Ssps]**](Ssps.md) |  | [optional] 

## Example

```python
from emass_client.models.cmmc_get import CmmcGet

# TODO update the JSON string below
json = "{}"
# create an instance of CmmcGet from a JSON string
cmmc_get_instance = CmmcGet.from_json(json)
# print the JSON string representation of the object
print CmmcGet.to_json()

# convert the object into a dict
cmmc_get_dict = cmmc_get_instance.to_dict()
# create an instance of CmmcGet from a dict
cmmc_get_form_dict = cmmc_get.from_dict(cmmc_get_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


