# CmmcGet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation** | **str** | [Read-Only] Indicates the action that should be taken on the assessment record since the provided sinceDate. | [optional] 
**hq_organization_name** | **str** | [Read-Only] The name of the DIB Company. | [optional] 
**uei** | **str** | [Read-Only] The Unique Entity Identifier assigned to the DIB Company. | [optional] 
**osc_name** | **str** | [Read-Only] The name of the Organization Seeking Certification. | [optional] 
**highest_level_owner_cage_code** | **str** | [Read-Only] Identifies the highest-level CAGE Code associated with a given organization. | [optional] 
**cage_codes_in_scope** | **str** | [Read-Only] The five position code(s) associated with the Organization Seeking Certification (OSC). | [optional] 
**number_of_employees** | **int** | [Read-Only] The number of employees affiliated with the Organization Seeking Certification. | [optional] 
**scope** | **str** | [Read-Only] The scope of the OSC assessment. | [optional] 
**scope_description** | **str** | [Read-Only] Brief description of the scope of the OSC assessment | [optional] 
**assessment_standard** | **str** | [Read-Only] Version of the CMMC Model used as part of the assessment. | [optional] 
**assessment_id** | **str** | [Read-Only] Unique identifier for the assessment/certificate. | [optional] 
**cmmc_uid** | **str** | [Read-Only] Identifies the unique ID that is associated with a given CMMC certification for an organization. | [optional] 
**overall_score** | **int** | [Read-Only] Identifies the overall calculated score for the assessment based on the assigned values to each applicable security requirement. | [optional] 
**cmmc_status** | **str** | [Read-Only] The status of the CMMC certification. | [optional] 
**cmmc_status_date** | **int** | [Read-Only] Date of the CMMC status. | [optional] 
**cmmc_status_expiration_date** | **int** | [Read-Only] Expiration date of the CMMC status. | [optional] 

## Example

```python
from emass_client.models.cmmc_get import CmmcGet

# TODO update the JSON string below
json = "{}"
# create an instance of CmmcGet from a JSON string
cmmc_get_instance = CmmcGet.from_json(json)
# print the JSON string representation of the object
print(CmmcGet.to_json())

# convert the object into a dict
cmmc_get_dict = cmmc_get_instance.to_dict()
# create an instance of CmmcGet from a dict
cmmc_get_from_dict = CmmcGet.from_dict(cmmc_get_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


