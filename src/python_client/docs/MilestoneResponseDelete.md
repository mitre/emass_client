# MilestoneResponseDelete


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Response200**](Response200.md) |  | [optional] 
**data** | [**List[MilestonesPutPostDelete]**](MilestonesPutPostDelete.md) |  | [optional] 

## Example

```python
from emass_client.models.milestone_response_delete import MilestoneResponseDelete

# TODO update the JSON string below
json = "{}"
# create an instance of MilestoneResponseDelete from a JSON string
milestone_response_delete_instance = MilestoneResponseDelete.from_json(json)
# print the JSON string representation of the object
print MilestoneResponseDelete.to_json()

# convert the object into a dict
milestone_response_delete_dict = milestone_response_delete_instance.to_dict()
# create an instance of MilestoneResponseDelete from a dict
milestone_response_delete_form_dict = milestone_response_delete.from_dict(milestone_response_delete_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


