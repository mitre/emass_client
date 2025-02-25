# MilestonesRequiredPutMilestonesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | [Required] Include milestone description. | 
**scheduled_completion_date** | **int** | [Required] Required for ongoing and completed POA&amp;M items. Unix time format. | 
**is_active** | **bool** | [Conditional] Optionally used in PUT to delete milestones when updating a POA&amp;M. | 

## Example

```python
from emass_client.models.milestones_required_put_milestones_inner import MilestonesRequiredPutMilestonesInner

# TODO update the JSON string below
json = "{}"
# create an instance of MilestonesRequiredPutMilestonesInner from a JSON string
milestones_required_put_milestones_inner_instance = MilestonesRequiredPutMilestonesInner.from_json(json)
# print the JSON string representation of the object
print(MilestonesRequiredPutMilestonesInner.to_json())

# convert the object into a dict
milestones_required_put_milestones_inner_dict = milestones_required_put_milestones_inner_instance.to_dict()
# create an instance of MilestonesRequiredPutMilestonesInner from a dict
milestones_required_put_milestones_inner_from_dict = MilestonesRequiredPutMilestonesInner.from_dict(milestones_required_put_milestones_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


