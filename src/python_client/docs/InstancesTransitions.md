# InstancesTransitions


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comments** | **str** | [Read-Only] Comments entered by the user when performing the transition. | [optional] 
**created_by** | **str** | [Read-Only] User that performed the workflow transition. | [optional] 
**created_date** | **int** | [Read-Only] Date the workflow instance or the workflow transition was created. | [optional] 
**description** | **str** | [Read-Only] Description of the stage transition. This matches the action dropdown that appears for PAC users. | [optional] 
**end_stage** | **str** | [Read-Only] The landing stage that is active after performing a transition. | [optional] 
**start_stage** | **str** | [Read-Only] The beginning stage that is active before performing a transition. | [optional] 

## Example

```python
from emass_client.models.instances_transitions import InstancesTransitions

# TODO update the JSON string below
json = "{}"
# create an instance of InstancesTransitions from a JSON string
instances_transitions_instance = InstancesTransitions.from_json(json)
# print the JSON string representation of the object
print InstancesTransitions.to_json()

# convert the object into a dict
instances_transitions_dict = instances_transitions_instance.to_dict()
# create an instance of InstancesTransitions from a dict
instances_transitions_form_dict = instances_transitions.from_dict(instances_transitions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


