# CacResponsePostDataInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**control_acronym** | **str** | [Required] System acronym name. | [optional] 
**success** | **bool** |  | [optional] 
**system_id** | **int** |  | [optional] 
**errors** | **List[object]** |  | [optional] 

## Example

```python
from emass_client.models.cac_response_post_data_inner import CacResponsePostDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of CacResponsePostDataInner from a JSON string
cac_response_post_data_inner_instance = CacResponsePostDataInner.from_json(json)
# print the JSON string representation of the object
print CacResponsePostDataInner.to_json()

# convert the object into a dict
cac_response_post_data_inner_dict = cac_response_post_data_inner_instance.to_dict()
# create an instance of CacResponsePostDataInner from a dict
cac_response_post_data_inner_form_dict = cac_response_post_data_inner.from_dict(cac_response_post_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


