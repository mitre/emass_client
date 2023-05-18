# emass_client.model.workflow_instances_response_get.WorkflowInstancesResponseGet

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**meta** | [**Response200**](Response200.md) | [**Response200**](Response200.md) |  | [optional] 
**[data](#data)** | list, tuple,  | tuple,  |  | [optional] 
**[pagination](#pagination)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 

# data

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**WorkflowInstancesGet**](WorkflowInstancesGet.md) | [**WorkflowInstancesGet**](WorkflowInstancesGet.md) | [**WorkflowInstancesGet**](WorkflowInstancesGet.md) |  | 

# pagination

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**totalCount** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**totalPages** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**prevPageUrl** | str,  | str,  |  | [optional] 
**nextPageUrl** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

