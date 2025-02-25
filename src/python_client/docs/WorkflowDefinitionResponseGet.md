# WorkflowDefinitionResponseGet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Response200**](Response200.md) |  | [optional] 
**data** | [**List[WorkflowDefinitionGet]**](WorkflowDefinitionGet.md) |  | [optional] 

## Example

```python
from emass_client.models.workflow_definition_response_get import WorkflowDefinitionResponseGet

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowDefinitionResponseGet from a JSON string
workflow_definition_response_get_instance = WorkflowDefinitionResponseGet.from_json(json)
# print the JSON string representation of the object
print(WorkflowDefinitionResponseGet.to_json())

# convert the object into a dict
workflow_definition_response_get_dict = workflow_definition_response_get_instance.to_dict()
# create an instance of WorkflowDefinitionResponseGet from a dict
workflow_definition_response_get_from_dict = WorkflowDefinitionResponseGet.from_dict(workflow_definition_response_get_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


