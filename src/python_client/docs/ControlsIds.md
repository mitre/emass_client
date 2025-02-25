# ControlsIds


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**system_id** | **int** | [Required] Unique eMASS system identifier. | [optional] 

## Example

```python
from emass_client.models.controls_ids import ControlsIds

# TODO update the JSON string below
json = "{}"
# create an instance of ControlsIds from a JSON string
controls_ids_instance = ControlsIds.from_json(json)
# print the JSON string representation of the object
print(ControlsIds.to_json())

# convert the object into a dict
controls_ids_dict = controls_ids_instance.to_dict()
# create an instance of ControlsIds from a dict
controls_ids_from_dict = ControlsIds.from_dict(controls_ids_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


