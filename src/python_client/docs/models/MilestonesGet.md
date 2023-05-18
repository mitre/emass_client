# emass_client.model.milestones_get.MilestonesGet

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**systemId** | decimal.Decimal, int,  | decimal.Decimal,  | [Required] Unique eMASS system identifier. | [optional] value must be a 64 bit integer
**milestoneId** | decimal.Decimal, int,  | decimal.Decimal,  | [Required] Unique item identifier | [optional] value must be a 64 bit integer
**poamId** | decimal.Decimal, int,  | decimal.Decimal,  | [Required] Unique item identifier | [optional] value must be a 64 bit integer
**description** | str,  | str,  | [Required] Include milestone description. | [optional] 
**scheduledCompletionDate** | decimal.Decimal, int,  | decimal.Decimal,  | [Required] Required for ongoing and completed POA&amp;M items. Unix time format. | [optional] value must be a 64 bit integer
**reviewStatus** | str,  | str,  | [Read-Only] Values include the following options: (Not Approved,Under Review,Approved) | [optional] must be one of ["Not Approved", "Under Review", "Approved", ] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

