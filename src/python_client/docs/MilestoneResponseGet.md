# MilestoneResponseGet


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Response200**](Response200.md) |  | [optional] 
**data** | [**List[MilestonesGet]**](MilestonesGet.md) |  | [optional] 

## Example

```python
from emass_client.models.milestone_response_get import MilestoneResponseGet

# TODO update the JSON string below
json = "{}"
# create an instance of MilestoneResponseGet from a JSON string
milestone_response_get_instance = MilestoneResponseGet.from_json(json)
# print the JSON string representation of the object
print MilestoneResponseGet.to_json()

# convert the object into a dict
milestone_response_get_dict = milestone_response_get_instance.to_dict()
# create an instance of MilestoneResponseGet from a dict
milestone_response_get_form_dict = milestone_response_get.from_dict(milestone_response_get_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


