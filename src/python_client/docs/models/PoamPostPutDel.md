# emass_client.model.poam_post_put_del.PoamPostPutDel

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**systemId** | decimal.Decimal, int,  | decimal.Decimal,  | The system identifier for the system being updated. | [optional] value must be a 64 bit integer
**poamId** | decimal.Decimal, int,  | decimal.Decimal,  | The newly created POAM identifier | [optional] value must be a 64 bit integer
**externalUid** | str,  | str,  | The unique identifier external to the eMASS application for use with associating POA&amp;Ms. 100 Characters. | [optional] 
**success** | bool,  | BoolClass,  | Indicates if operations result (success/fail) | [optional] 
**errors** | [**Errors**](Errors.md) | [**Errors**](Errors.md) |  | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

