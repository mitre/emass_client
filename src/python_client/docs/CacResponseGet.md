# CacResponseGet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Response200**](Response200.md) |  | [optional] 
**data** | [**List[CacGet]**](CacGet.md) |  | [optional] 

## Example

```python
from emass_client.models.cac_response_get import CacResponseGet

# TODO update the JSON string below
json = "{}"
# create an instance of CacResponseGet from a JSON string
cac_response_get_instance = CacResponseGet.from_json(json)
# print the JSON string representation of the object
print(CacResponseGet.to_json())

# convert the object into a dict
cac_response_get_dict = cac_response_get_instance.to_dict()
# create an instance of CacResponseGet from a dict
cac_response_get_from_dict = CacResponseGet.from_dict(cac_response_get_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


