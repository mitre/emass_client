# MilestoneResponsePost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Response200**](Response200.md) |  | [optional] 
**data** | [**List[MilestonesPutPostDelete]**](MilestonesPutPostDelete.md) |  | [optional] 

## Example

```python
from emass_client.models.milestone_response_post import MilestoneResponsePost

# TODO update the JSON string below
json = "{}"
# create an instance of MilestoneResponsePost from a JSON string
milestone_response_post_instance = MilestoneResponsePost.from_json(json)
# print the JSON string representation of the object
print(MilestoneResponsePost.to_json())

# convert the object into a dict
milestone_response_post_dict = milestone_response_post_instance.to_dict()
# create an instance of MilestoneResponsePost from a dict
milestone_response_post_from_dict = MilestoneResponsePost.from_dict(milestone_response_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


