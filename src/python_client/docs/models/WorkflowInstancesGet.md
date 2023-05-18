# emass_client.model.workflow_instances_get.WorkflowInstancesGet

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**workflowUid** | None, str,  | NoneClass, str,  | [Read-Only] Unique workflow definition identifier. | [optional] 
**systemId** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | [Read-only] Unique system record identifier. | [optional] value must be a 64 bit integer
**systemName** | None, str,  | NoneClass, str,  | [Read-Only] The system name. | [optional] 
**workflowInstanceId** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | [Read-Only] Unique workflow instance identifier. | [optional] value must be a 64 bit integer
**packageName** | None, str,  | NoneClass, str,  | [Read-Only] The package name. | [optional] 
**createdDate** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | [Read-Only] Date the workflow instance or the workflow transition was created. | [optional] value must be a 64 bit integer
**lastEditedDate** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | [Read-Only] Date the workflow was last acted on. | [optional] value must be a 64 bit integer
**lastEditedBy** | None, str,  | NoneClass, str,  | [Read-Only] User that last acted on the workflow. | [optional] 
**workflow** | None, str,  | NoneClass, str,  | [Read-Only] The workflow type. | [optional] 
**version** | None, str,  | NoneClass, str,  | [Read-Only] Version of the workflow definition. | [optional] 
**currentStage** | None, str,  | NoneClass, str,  | [Read-Only] Name of the current stage. | [optional] 
**[transitions](#transitions)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# transitions

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**InstancesTransitions**](InstancesTransitions.md) | [**InstancesTransitions**](InstancesTransitions.md) | [**InstancesTransitions**](InstancesTransitions.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

