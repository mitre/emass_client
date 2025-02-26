# MilestoneResponsePut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Response200**](Response200.md) |  | [optional] 
**data** | [**List[MilestonesPutPostDelete]**](MilestonesPutPostDelete.md) |  | [optional] 

## Example

```python
from emass_client.models.milestone_response_put import MilestoneResponsePut

# TODO update the JSON string below
json = "{}"
# create an instance of MilestoneResponsePut from a JSON string
milestone_response_put_instance = MilestoneResponsePut.from_json(json)
# print the JSON string representation of the object
print(MilestoneResponsePut.to_json())

# convert the object into a dict
milestone_response_put_dict = milestone_response_put_instance.to_dict()
# create an instance of MilestoneResponsePut from a dict
milestone_response_put_from_dict = MilestoneResponsePut.from_dict(milestone_response_put_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


