# emass_client.model.test_results_post.TestResultsPost

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**cci** | str,  | str,  | CCI associated with test result. | [optional] 
**success** | bool,  | BoolClass,  | Indicates if operations result (success/fail) | [optional] 
**systemId** | decimal.Decimal, int,  | decimal.Decimal,  | The system identifier for the system being updated. | [optional] value must be a 64 bit integer
**errors** | [**Errors**](Errors.md) | [**Errors**](Errors.md) |  | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

