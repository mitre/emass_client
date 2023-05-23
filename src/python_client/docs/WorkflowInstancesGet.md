# WorkflowInstancesGet


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_uid** | **str** | [Read-Only] Unique workflow definition identifier. | [optional] 
**system_id** | **int** | [Read-only] Unique system record identifier. | [optional] 
**system_name** | **str** | [Read-Only] The system name. | [optional] 
**workflow_instance_id** | **int** | [Read-Only] Unique workflow instance identifier. | [optional] 
**package_name** | **str** | [Read-Only] The package name. | [optional] 
**created_date** | **int** | [Read-Only] Date the workflow instance or the workflow transition was created. | [optional] 
**last_edited_date** | **int** | [Read-Only] Date the workflow was last acted on. | [optional] 
**last_edited_by** | **str** | [Read-Only] User that last acted on the workflow. | [optional] 
**workflow** | **str** | [Read-Only] The workflow type. | [optional] 
**version** | **str** | [Read-Only] Version of the workflow definition. | [optional] 
**current_stage** | **str** | [Read-Only] Name of the current stage. | [optional] 
**transitions** | [**List[InstancesTransitions]**](InstancesTransitions.md) |  | [optional] 

## Example

```python
from emass_client.models.workflow_instances_get import WorkflowInstancesGet

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowInstancesGet from a JSON string
workflow_instances_get_instance = WorkflowInstancesGet.from_json(json)
# print the JSON string representation of the object
print WorkflowInstancesGet.to_json()

# convert the object into a dict
workflow_instances_get_dict = workflow_instances_get_instance.to_dict()
# create an instance of WorkflowInstancesGet from a dict
workflow_instances_get_form_dict = workflow_instances_get.from_dict(workflow_instances_get_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


