# emass_client.model.pac_get.PacGet

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**systemId** | decimal.Decimal, int,  | decimal.Decimal,  | [Required] Unique eMASS system identifier. | [optional] value must be a 64 bit integer
**workflow** | str,  | str,  | [Required] Values include the following:(Assess and Authorize, Assess Only, Security Plan Approval) | [optional] must be one of ["Assess and Authorize", "Assess Only", "Security Plan Approval", ] 
**name** | str,  | str,  | [Required] Package name. 100 Characters. | [optional] 
**currentStageName** | None, str,  | NoneClass, str,  | [Read-Only] Name of the current stage in the active workflow. | [optional] 
**currentStage** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | [Read-Only] Number of the current stage in the active workflow. | [optional] 
**totalStages** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | [Read-Only] Total number of stages in the active workflow. | [optional] 
**daysAtCurrentStage** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | [Read-Only] Indicates the number of days at current workflow stage. | [optional] 
**comments** | str,  | str,  | [Required] Comments related to package approval chain. Character Limit &#x3D; 4,000. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

