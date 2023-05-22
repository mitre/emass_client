# PoamPostPutDel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**system_id** | **int** | The system identifier for the system being updated. | [optional] 
**poam_id** | **int** | The newly created POAM identifier | [optional] 
**external_uid** | **str** | The unique identifier external to the eMASS application for use with associating POA&amp;Ms. 100 Characters. | [optional] 
**success** | **bool** | Indicates if operations result (success/fail) | [optional] 
**errors** | **List[object]** |  | [optional] 

## Example

```python
from emass_client.models.poam_post_put_del import PoamPostPutDel

# TODO update the JSON string below
json = "{}"
# create an instance of PoamPostPutDel from a JSON string
poam_post_put_del_instance = PoamPostPutDel.from_json(json)
# print the JSON string representation of the object
print PoamPostPutDel.to_json()

# convert the object into a dict
poam_post_put_del_dict = poam_post_put_del_instance.to_dict()
# create an instance of PoamPostPutDel from a dict
poam_post_put_del_form_dict = poam_post_put_del.from_dict(poam_post_put_del_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


