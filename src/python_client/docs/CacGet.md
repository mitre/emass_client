# CacGet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**system_id** | **int** | [Required] Unique eMASS system identifier. | [optional] 
**control_acronym** | **str** | [Required] System acronym name. | [optional] 
**compliance_status** | **str** | [Read-only] Compliance status of the control. | [optional] 
**current_stage_name** | **str** | [Read-Only] Role in current stage. | [optional] 
**current_stage** | **int** | [Read-Only] Current step in the Control Approval Chain. | [optional] 
**total_stages** | **int** | [Read-Only] Total number of steps in Control Approval Chain. | [optional] 
**comments** | **str** | [Conditional] Control Approval Chain comments - 2000 Characters. | [optional] 

## Example

```python
from emass_client.models.cac_get import CacGet

# TODO update the JSON string below
json = "{}"
# create an instance of CacGet from a JSON string
cac_get_instance = CacGet.from_json(json)
# print the JSON string representation of the object
print(CacGet.to_json())

# convert the object into a dict
cac_get_dict = cac_get_instance.to_dict()
# create an instance of CacGet from a dict
cac_get_from_dict = CacGet.from_dict(cac_get_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


