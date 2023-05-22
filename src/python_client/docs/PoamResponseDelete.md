# PoamResponseDelete


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Response200**](Response200.md) |  | [optional] 
**data** | [**List[PoamPostPutDel]**](PoamPostPutDel.md) |  | [optional] 

## Example

```python
from emass_client.models.poam_response_delete import PoamResponseDelete

# TODO update the JSON string below
json = "{}"
# create an instance of PoamResponseDelete from a JSON string
poam_response_delete_instance = PoamResponseDelete.from_json(json)
# print the JSON string representation of the object
print PoamResponseDelete.to_json()

# convert the object into a dict
poam_response_delete_dict = poam_response_delete_instance.to_dict()
# create an instance of PoamResponseDelete from a dict
poam_response_delete_form_dict = poam_response_delete.from_dict(poam_response_delete_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


