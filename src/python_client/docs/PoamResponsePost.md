# PoamResponsePost


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Response200**](Response200.md) |  | [optional] 
**data** | [**List[PoamPostPutDel]**](PoamPostPutDel.md) |  | [optional] 

## Example

```python
from emass_client.models.poam_response_post import PoamResponsePost

# TODO update the JSON string below
json = "{}"
# create an instance of PoamResponsePost from a JSON string
poam_response_post_instance = PoamResponsePost.from_json(json)
# print the JSON string representation of the object
print PoamResponsePost.to_json()

# convert the object into a dict
poam_response_post_dict = poam_response_post_instance.to_dict()
# create an instance of PoamResponsePost from a dict
poam_response_post_form_dict = poam_response_post.from_dict(poam_response_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


