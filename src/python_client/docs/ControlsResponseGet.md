# ControlsResponseGet


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Response200**](Response200.md) |  | [optional] 
**data** | [**List[ControlsGet]**](ControlsGet.md) |  | [optional] 

## Example

```python
from emass_client.models.controls_response_get import ControlsResponseGet

# TODO update the JSON string below
json = "{}"
# create an instance of ControlsResponseGet from a JSON string
controls_response_get_instance = ControlsResponseGet.from_json(json)
# print the JSON string representation of the object
print ControlsResponseGet.to_json()

# convert the object into a dict
controls_response_get_dict = controls_response_get_instance.to_dict()
# create an instance of ControlsResponseGet from a dict
controls_response_get_form_dict = controls_response_get.from_dict(controls_response_get_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


