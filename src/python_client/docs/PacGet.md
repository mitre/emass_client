# PacGet


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**system_id** | **int** | [Required] Unique eMASS system identifier. | [optional] 
**workflow** | **str** | [Required] Values include the following:(Assess and Authorize, Assess Only, Security Plan Approval) | [optional] 
**name** | **str** | [Required] Package name. 100 Characters. | [optional] 
**current_stage_name** | **str** | [Read-Only] Name of the current stage in the active workflow. | [optional] 
**current_stage** | **int** | [Read-Only] Number of the current stage in the active workflow. | [optional] 
**total_stages** | **int** | [Read-Only] Total number of stages in the active workflow. | [optional] 
**days_at_current_stage** | **int** | [Read-Only] Indicates the number of days at current workflow stage. | [optional] 
**comments** | **str** | [Required] Comments related to package approval chain. Character Limit &#x3D; 4,000. | [optional] 

## Example

```python
from emass_client.models.pac_get import PacGet

# TODO update the JSON string below
json = "{}"
# create an instance of PacGet from a JSON string
pac_get_instance = PacGet.from_json(json)
# print the JSON string representation of the object
print PacGet.to_json()

# convert the object into a dict
pac_get_dict = pac_get_instance.to_dict()
# create an instance of PacGet from a dict
pac_get_form_dict = pac_get.from_dict(pac_get_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


