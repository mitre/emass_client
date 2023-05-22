# CacResponsePost


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Response200**](Response200.md) |  | [optional] 
**data** | [**List[CacResponsePostDataInner]**](CacResponsePostDataInner.md) |  | [optional] 

## Example

```python
from emass_client.models.cac_response_post import CacResponsePost

# TODO update the JSON string below
json = "{}"
# create an instance of CacResponsePost from a JSON string
cac_response_post_instance = CacResponsePost.from_json(json)
# print the JSON string representation of the object
print CacResponsePost.to_json()

# convert the object into a dict
cac_response_post_dict = cac_response_post_instance.to_dict()
# create an instance of CacResponsePost from a dict
cac_response_post_form_dict = cac_response_post.from_dict(cac_response_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


