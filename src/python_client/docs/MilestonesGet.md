# MilestonesGet


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**system_id** | **int** | [Required] Unique eMASS system identifier. | [optional] 
**milestone_id** | **int** | [Required] Unique item identifier | [optional] 
**poam_id** | **int** | [Required] Unique item identifier | [optional] 
**description** | **str** | [Required] Include milestone description. | [optional] 
**scheduled_completion_date** | **int** | [Required] Required for ongoing and completed POA&amp;M items. Unix time format. | [optional] 
**review_status** | **str** | [Read-Only] Values include the following options: (Not Approved,Under Review,Approved) | [optional] 

## Example

```python
from emass_client.models.milestones_get import MilestonesGet

# TODO update the JSON string below
json = "{}"
# create an instance of MilestonesGet from a JSON string
milestones_get_instance = MilestonesGet.from_json(json)
# print the JSON string representation of the object
print MilestonesGet.to_json()

# convert the object into a dict
milestones_get_dict = milestones_get_instance.to_dict()
# create an instance of MilestonesGet from a dict
milestones_get_form_dict = milestones_get.from_dict(milestones_get_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


