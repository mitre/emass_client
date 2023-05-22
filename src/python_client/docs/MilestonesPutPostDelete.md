# MilestonesPutPostDelete


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**system_id** | **int** | The system identifier that the POAM was added. | [optional] 
**poam_id** | **int** | The newly created POAM identifier | [optional] 
**milestone_id** | **int** | The Milestone unique item identifier | [optional] 
**external_uid** | **str** | The unique identifier external to the eMASS application for use with associating POA&amp;Ms. 100 Characters. | [optional] 
**success** | **bool** | Indicates if operations result (success/fail) | [optional] 
**errors** | **List[object]** |  | [optional] 

## Example

```python
from emass_client.models.milestones_put_post_delete import MilestonesPutPostDelete

# TODO update the JSON string below
json = "{}"
# create an instance of MilestonesPutPostDelete from a JSON string
milestones_put_post_delete_instance = MilestonesPutPostDelete.from_json(json)
# print the JSON string representation of the object
print MilestonesPutPostDelete.to_json()

# convert the object into a dict
milestones_put_post_delete_dict = milestones_put_post_delete_instance.to_dict()
# create an instance of MilestonesPutPostDelete from a dict
milestones_put_post_delete_form_dict = milestones_put_post_delete.from_dict(milestones_put_post_delete_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


