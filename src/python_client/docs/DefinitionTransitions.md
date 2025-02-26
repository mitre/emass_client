# DefinitionTransitions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_stage** | **str** | [Read-Only] The landing stage that is active after performing a transition. | [optional] 
**description** | **str** | [Read-Only] Description that matches the action dropdown that appears for PAC users. | [optional] 
**roles** | **List[object]** |  | [optional] 

## Example

```python
from emass_client.models.definition_transitions import DefinitionTransitions

# TODO update the JSON string below
json = "{}"
# create an instance of DefinitionTransitions from a JSON string
definition_transitions_instance = DefinitionTransitions.from_json(json)
# print the JSON string representation of the object
print(DefinitionTransitions.to_json())

# convert the object into a dict
definition_transitions_dict = definition_transitions_instance.to_dict()
# create an instance of DefinitionTransitions from a dict
definition_transitions_from_dict = DefinitionTransitions.from_dict(definition_transitions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


