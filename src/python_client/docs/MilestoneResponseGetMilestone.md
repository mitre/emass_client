# MilestoneResponseGetMilestone


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Response200**](Response200.md) |  | [optional] 
**data** | [**MilestonesGet**](MilestonesGet.md) |  | [optional] 

## Example

```python
from emass_client.models.milestone_response_get_milestone import MilestoneResponseGetMilestone

# TODO update the JSON string below
json = "{}"
# create an instance of MilestoneResponseGetMilestone from a JSON string
milestone_response_get_milestone_instance = MilestoneResponseGetMilestone.from_json(json)
# print the JSON string representation of the object
print(MilestoneResponseGetMilestone.to_json())

# convert the object into a dict
milestone_response_get_milestone_dict = milestone_response_get_milestone_instance.to_dict()
# create an instance of MilestoneResponseGetMilestone from a dict
milestone_response_get_milestone_from_dict = MilestoneResponseGetMilestone.from_dict(milestone_response_get_milestone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


