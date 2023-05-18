# emass_client.model.cac_get.CacGet

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**systemId** | decimal.Decimal, int,  | decimal.Decimal,  | [Required] Unique eMASS system identifier. | [optional] value must be a 64 bit integer
**controlAcronym** | str,  | str,  | [Required] System acronym name. | [optional] 
**complianceStatus** | None, str,  | NoneClass, str,  | [Read-only] Compliance status of the control. | [optional] 
**currentStageName** | None, str,  | NoneClass, str,  | [Read-Only] Role in current stage. | [optional] 
**currentStage** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | [Read-Only] Current step in the Control Approval Chain. | [optional] 
**totalStages** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | [Read-Only] Total number of steps in Control Approval Chain. | [optional] 
**comments** | None, str,  | NoneClass, str,  | [Conditional] Control Approval Chain comments - 2000 Characters. | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

