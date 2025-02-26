# ControlsResponsePut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Response200**](Response200.md) |  | [optional] 
**data** | [**List[ControlsPut]**](ControlsPut.md) |  | [optional] 

## Example

```python
from emass_client.models.controls_response_put import ControlsResponsePut

# TODO update the JSON string below
json = "{}"
# create an instance of ControlsResponsePut from a JSON string
controls_response_put_instance = ControlsResponsePut.from_json(json)
# print the JSON string representation of the object
print(ControlsResponsePut.to_json())

# convert the object into a dict
controls_response_put_dict = controls_response_put_instance.to_dict()
# create an instance of ControlsResponsePut from a dict
controls_response_put_from_dict = ControlsResponsePut.from_dict(controls_response_put_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


