# WorkflowInstanceResponseGet


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Response200**](Response200.md) |  | [optional] 
**data** | [**List[WorkflowInstanceGet]**](WorkflowInstanceGet.md) |  | [optional] 

## Example

```python
from emass_client.models.workflow_instance_response_get import WorkflowInstanceResponseGet

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowInstanceResponseGet from a JSON string
workflow_instance_response_get_instance = WorkflowInstanceResponseGet.from_json(json)
# print the JSON string representation of the object
print WorkflowInstanceResponseGet.to_json()

# convert the object into a dict
workflow_instance_response_get_dict = workflow_instance_response_get_instance.to_dict()
# create an instance of WorkflowInstanceResponseGet from a dict
workflow_instance_response_get_form_dict = workflow_instance_response_get.from_dict(workflow_instance_response_get_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


