# emass_client.model.workflow_definition_get.WorkflowDefinitionGet

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**workflowUid** | None, str,  | NoneClass, str,  | [Read-Only] Unique workflow definition identifier. | [optional] 
**workflow** | None, str,  | NoneClass, str,  | [Read-Only] The workflow type. | [optional] 
**version** | None, str,  | NoneClass, str,  | [Read-Only] Version of the workflow definition. | [optional] 
**description** | None, str,  | NoneClass, str,  | [Read-Only] Description of the workflow or the stage transition. | [optional] 
**isActive** | None, bool,  | NoneClass, BoolClass,  | [Read-Only] Returns true if the workflow is available to the site. | [optional] 
**[stages](#stages)** | list, tuple, None,  | tuple, NoneClass,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# stages

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Stage**](Stage.md) | [**Stage**](Stage.md) | [**Stage**](Stage.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

