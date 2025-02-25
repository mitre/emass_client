# PoamIds


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**system_id** | **int** | [Required] Unique eMASS system identifier. | [optional] 
**poam_id** | **int** | [Required] Unique item identifier | [optional] 
**display_poam_id** | **int** | [Required] Globally unique identifier for individual POA&amp;M Items, seen on the front-end as ID. | [optional] 

## Example

```python
from emass_client.models.poam_ids import PoamIds

# TODO update the JSON string below
json = "{}"
# create an instance of PoamIds from a JSON string
poam_ids_instance = PoamIds.from_json(json)
# print the JSON string representation of the object
print(PoamIds.to_json())

# convert the object into a dict
poam_ids_dict = poam_ids_instance.to_dict()
# create an instance of PoamIds from a dict
poam_ids_from_dict = PoamIds.from_dict(poam_ids_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


