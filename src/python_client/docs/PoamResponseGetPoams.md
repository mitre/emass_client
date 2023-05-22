# PoamResponseGetPoams


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Response200**](Response200.md) |  | [optional] 
**data** | [**PoamGet**](PoamGet.md) |  | [optional] 

## Example

```python
from emass_client.models.poam_response_get_poams import PoamResponseGetPoams

# TODO update the JSON string below
json = "{}"
# create an instance of PoamResponseGetPoams from a JSON string
poam_response_get_poams_instance = PoamResponseGetPoams.from_json(json)
# print the JSON string representation of the object
print PoamResponseGetPoams.to_json()

# convert the object into a dict
poam_response_get_poams_dict = poam_response_get_poams_instance.to_dict()
# create an instance of PoamResponseGetPoams from a dict
poam_response_get_poams_form_dict = poam_response_get_poams.from_dict(poam_response_get_poams_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


