# PacResponseGet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Response200**](Response200.md) |  | [optional] 
**data** | [**List[PacGet]**](PacGet.md) |  | [optional] 

## Example

```python
from emass_client.models.pac_response_get import PacResponseGet

# TODO update the JSON string below
json = "{}"
# create an instance of PacResponseGet from a JSON string
pac_response_get_instance = PacResponseGet.from_json(json)
# print the JSON string representation of the object
print(PacResponseGet.to_json())

# convert the object into a dict
pac_response_get_dict = pac_response_get_instance.to_dict()
# create an instance of PacResponseGet from a dict
pac_response_get_from_dict = PacResponseGet.from_dict(pac_response_get_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


