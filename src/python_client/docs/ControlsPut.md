# ControlsPut


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acronym** | **str** | Acronym of the system record. | [optional] 
**success** | **bool** | Indicates if operations result (success/fail) | [optional] 
**system_id** | **int** | The system identifier for the system being updated. | [optional] 
**errors** | **List[object]** |  | [optional] 

## Example

```python
from emass_client.models.controls_put import ControlsPut

# TODO update the JSON string below
json = "{}"
# create an instance of ControlsPut from a JSON string
controls_put_instance = ControlsPut.from_json(json)
# print the JSON string representation of the object
print ControlsPut.to_json()

# convert the object into a dict
controls_put_dict = controls_put_instance.to_dict()
# create an instance of ControlsPut from a dict
controls_put_form_dict = controls_put.from_dict(controls_put_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


