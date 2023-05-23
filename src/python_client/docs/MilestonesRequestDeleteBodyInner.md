# MilestonesRequestDeleteBodyInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**milestone_id** | **int** | [Required] Unique item identifier | [optional] 

## Example

```python
from emass_client.models.milestones_request_delete_body_inner import MilestonesRequestDeleteBodyInner

# TODO update the JSON string below
json = "{}"
# create an instance of MilestonesRequestDeleteBodyInner from a JSON string
milestones_request_delete_body_inner_instance = MilestonesRequestDeleteBodyInner.from_json(json)
# print the JSON string representation of the object
print MilestonesRequestDeleteBodyInner.to_json()

# convert the object into a dict
milestones_request_delete_body_inner_dict = milestones_request_delete_body_inner_instance.to_dict()
# create an instance of MilestonesRequestDeleteBodyInner from a dict
milestones_request_delete_body_inner_form_dict = milestones_request_delete_body_inner.from_dict(milestones_request_delete_body_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


