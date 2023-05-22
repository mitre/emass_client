# MilestonesRequiredPost


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | [Required] Include milestone description. | 
**scheduled_completion_date** | **int** | [Required] Required for ongoing and completed POA&amp;M items. Unix time format. | 

## Example

```python
from emass_client.models.milestones_required_post import MilestonesRequiredPost

# TODO update the JSON string below
json = "{}"
# create an instance of MilestonesRequiredPost from a JSON string
milestones_required_post_instance = MilestonesRequiredPost.from_json(json)
# print the JSON string representation of the object
print MilestonesRequiredPost.to_json()

# convert the object into a dict
milestones_required_post_dict = milestones_required_post_instance.to_dict()
# create an instance of MilestonesRequiredPost from a dict
milestones_required_post_form_dict = milestones_required_post.from_dict(milestones_required_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


