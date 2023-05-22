# Success200ResponseDataInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] 
**errors** | **List[object]** |  | [optional] 

## Example

```python
from emass_client.models.success200_response_data_inner import Success200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of Success200ResponseDataInner from a JSON string
success200_response_data_inner_instance = Success200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print Success200ResponseDataInner.to_json()

# convert the object into a dict
success200_response_data_inner_dict = success200_response_data_inner_instance.to_dict()
# create an instance of Success200ResponseDataInner from a dict
success200_response_data_inner_form_dict = success200_response_data_inner.from_dict(success200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


