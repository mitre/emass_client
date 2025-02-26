# MilestonesRequiredPostMilestonesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | [Required] Include milestone description. | 
**scheduled_completion_date** | **int** | [Required] Required for ongoing and completed POA&amp;M items. Unix time format. | 

## Example

```python
from emass_client.models.milestones_required_post_milestones_inner import MilestonesRequiredPostMilestonesInner

# TODO update the JSON string below
json = "{}"
# create an instance of MilestonesRequiredPostMilestonesInner from a JSON string
milestones_required_post_milestones_inner_instance = MilestonesRequiredPostMilestonesInner.from_json(json)
# print the JSON string representation of the object
print(MilestonesRequiredPostMilestonesInner.to_json())

# convert the object into a dict
milestones_required_post_milestones_inner_dict = milestones_required_post_milestones_inner_instance.to_dict()
# create an instance of MilestonesRequiredPostMilestonesInner from a dict
milestones_required_post_milestones_inner_from_dict = MilestonesRequiredPostMilestonesInner.from_dict(milestones_required_post_milestones_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


