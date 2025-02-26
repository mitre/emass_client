# WorkflowInstancesResponseGet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Response200**](Response200.md) |  | [optional] 
**data** | [**List[WorkflowInstanceGet]**](WorkflowInstanceGet.md) |  | [optional] 
**pagination** | [**WorkflowInstancesResponseGetPagination**](WorkflowInstancesResponseGetPagination.md) |  | [optional] 

## Example

```python
from emass_client.models.workflow_instances_response_get import WorkflowInstancesResponseGet

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowInstancesResponseGet from a JSON string
workflow_instances_response_get_instance = WorkflowInstancesResponseGet.from_json(json)
# print the JSON string representation of the object
print(WorkflowInstancesResponseGet.to_json())

# convert the object into a dict
workflow_instances_response_get_dict = workflow_instances_response_get_instance.to_dict()
# create an instance of WorkflowInstancesResponseGet from a dict
workflow_instances_response_get_from_dict = WorkflowInstancesResponseGet.from_dict(workflow_instances_response_get_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


