# WorkflowDefinitionGet


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_uid** | **str** | [Read-Only] Unique workflow definition identifier. | [optional] 
**workflow** | **str** | [Read-Only] The workflow type. | [optional] 
**version** | **str** | [Read-Only] Version of the workflow definition. | [optional] 
**description** | **str** | [Read-Only] Description of the workflow or the stage transition. | [optional] 
**is_active** | **bool** | [Read-Only] Returns true if the workflow is available to the site. | [optional] 
**stages** | [**List[Stage]**](Stage.md) |  | [optional] 

## Example

```python
from emass_client.models.workflow_definition_get import WorkflowDefinitionGet

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowDefinitionGet from a JSON string
workflow_definition_get_instance = WorkflowDefinitionGet.from_json(json)
# print the JSON string representation of the object
print WorkflowDefinitionGet.to_json()

# convert the object into a dict
workflow_definition_get_dict = workflow_definition_get_instance.to_dict()
# create an instance of WorkflowDefinitionGet from a dict
workflow_definition_get_form_dict = workflow_definition_get.from_dict(workflow_definition_get_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


