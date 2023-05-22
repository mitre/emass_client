# PoamResponsePut


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Response200**](Response200.md) |  | [optional] 
**data** | [**List[PoamPostPutDel]**](PoamPostPutDel.md) |  | [optional] 

## Example

```python
from emass_client.models.poam_response_put import PoamResponsePut

# TODO update the JSON string below
json = "{}"
# create an instance of PoamResponsePut from a JSON string
poam_response_put_instance = PoamResponsePut.from_json(json)
# print the JSON string representation of the object
print PoamResponsePut.to_json()

# convert the object into a dict
poam_response_put_dict = poam_response_put_instance.to_dict()
# create an instance of PoamResponsePut from a dict
poam_response_put_form_dict = poam_response_put.from_dict(poam_response_put_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


