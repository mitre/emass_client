# emass_client.model.static_code_application.StaticCodeApplication

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**rawSeverity** | str,  | str,  | [Optional] Scan vulnerability ratting | [optional] must be one of ["Low", "Medium", "Moderate", "High", "Critical", ] 
**codeCheckName** | str,  | str,  | [Required] Name of the software vulnerability or weakness. | [optional] 
**count** | decimal.Decimal, int,  | decimal.Decimal,  | [Required] Number of instances observed for a specified finding. | [optional] value must be a 64 bit integer
**scanDate** | decimal.Decimal, int,  | decimal.Decimal,  | [Required] The date of the scan. Unix date format. | [optional] value must be a 64 bit integer
**cweId** | str,  | str,  | [Required] The Common Weakness Enumerator (CWE) identifier. | [optional] 
**clearFindings** | bool,  | BoolClass,  | [Optional] When used by itself, can clear out all application findings for a single application/version pairing. | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

