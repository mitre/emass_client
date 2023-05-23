# PoamResponseGetSystems


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Response200**](Response200.md) |  | [optional] 
**data** | [**List[PoamGet]**](PoamGet.md) |  | [optional] 

## Example

```python
from emass_client.models.poam_response_get_systems import PoamResponseGetSystems

# TODO update the JSON string below
json = "{}"
# create an instance of PoamResponseGetSystems from a JSON string
poam_response_get_systems_instance = PoamResponseGetSystems.from_json(json)
# print the JSON string representation of the object
print PoamResponseGetSystems.to_json()

# convert the object into a dict
poam_response_get_systems_dict = poam_response_get_systems_instance.to_dict()
# create an instance of PoamResponseGetSystems from a dict
poam_response_get_systems_form_dict = poam_response_get_systems.from_dict(poam_response_get_systems_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


