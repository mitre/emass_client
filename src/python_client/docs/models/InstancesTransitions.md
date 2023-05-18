# emass_client.model.instances_transitions.InstancesTransitions

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**comments** | None, str,  | NoneClass, str,  | [Read-Only] Comments entered by the user when performing the transition. | [optional] 
**createdBy** | None, str,  | NoneClass, str,  | [Read-Only] User that performed the workflow transition. | [optional] 
**createdDate** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | [Read-Only] Date the workflow instance or the workflow transition was created. | [optional] value must be a 64 bit integer
**description** | None, str,  | NoneClass, str,  | [Read-Only] Description of the stage transition. This matches the action dropdown that appears for PAC users. | [optional] 
**endStage** | None, str,  | NoneClass, str,  | [Read-Only] The landing stage that is active after performing a transition. | [optional] 
**startStage** | None, str,  | NoneClass, str,  | [Read-Only] The beginning stage that is active before performing a transition. | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

