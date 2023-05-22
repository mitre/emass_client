# PacResponsePost


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Response200**](Response200.md) |  | [optional] 
**data** | [**List[PacPost]**](PacPost.md) |  | [optional] 

## Example

```python
from emass_client.models.pac_response_post import PacResponsePost

# TODO update the JSON string below
json = "{}"
# create an instance of PacResponsePost from a JSON string
pac_response_post_instance = PacResponsePost.from_json(json)
# print the JSON string representation of the object
print PacResponsePost.to_json()

# convert the object into a dict
pac_response_post_dict = pac_response_post_instance.to_dict()
# create an instance of PacResponsePost from a dict
pac_response_post_form_dict = pac_response_post.from_dict(pac_response_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


