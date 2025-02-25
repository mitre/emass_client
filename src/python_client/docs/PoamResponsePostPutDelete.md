# PoamResponsePostPutDelete


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Response200**](Response200.md) |  | [optional] 
**data** | [**List[PoamPostPutDel]**](PoamPostPutDel.md) |  | [optional] 

## Example

```python
from emass_client.models.poam_response_post_put_delete import PoamResponsePostPutDelete

# TODO update the JSON string below
json = "{}"
# create an instance of PoamResponsePostPutDelete from a JSON string
poam_response_post_put_delete_instance = PoamResponsePostPutDelete.from_json(json)
# print the JSON string representation of the object
print(PoamResponsePostPutDelete.to_json())

# convert the object into a dict
poam_response_post_put_delete_dict = poam_response_post_put_delete_instance.to_dict()
# create an instance of PoamResponsePostPutDelete from a dict
poam_response_post_put_delete_from_dict = PoamResponsePostPutDelete.from_dict(poam_response_post_put_delete_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


