# MilestonesRequiredPut


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**milestone_id** | **int** | [Required] Unique item identifier | 
**description** | **str** | [Required] Include milestone description. | 
**scheduled_completion_date** | **int** | [Required] Shecdule completion date. Unix time format. | 

## Example

```python
from emass_client.models.milestones_required_put import MilestonesRequiredPut

# TODO update the JSON string below
json = "{}"
# create an instance of MilestonesRequiredPut from a JSON string
milestones_required_put_instance = MilestonesRequiredPut.from_json(json)
# print the JSON string representation of the object
print MilestonesRequiredPut.to_json()

# convert the object into a dict
milestones_required_put_dict = milestones_required_put_instance.to_dict()
# create an instance of MilestonesRequiredPut from a dict
milestones_required_put_form_dict = milestones_required_put.from_dict(milestones_required_put_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


