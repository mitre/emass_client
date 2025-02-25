# PoamRequestDeleteBodyInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**poam_id** | **int** | [Required] Unique item identifier | [optional] 

## Example

```python
from emass_client.models.poam_request_delete_body_inner import PoamRequestDeleteBodyInner

# TODO update the JSON string below
json = "{}"
# create an instance of PoamRequestDeleteBodyInner from a JSON string
poam_request_delete_body_inner_instance = PoamRequestDeleteBodyInner.from_json(json)
# print the JSON string representation of the object
print(PoamRequestDeleteBodyInner.to_json())

# convert the object into a dict
poam_request_delete_body_inner_dict = poam_request_delete_body_inner_instance.to_dict()
# create an instance of PoamRequestDeleteBodyInner from a dict
poam_request_delete_body_inner_from_dict = PoamRequestDeleteBodyInner.from_dict(poam_request_delete_body_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


