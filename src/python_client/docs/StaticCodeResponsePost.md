# StaticCodeResponsePost


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Response200**](Response200.md) |  | [optional] 
**data** | [**List[StaticCodePost]**](StaticCodePost.md) |  | [optional] 

## Example

```python
from emass_client.models.static_code_response_post import StaticCodeResponsePost

# TODO update the JSON string below
json = "{}"
# create an instance of StaticCodeResponsePost from a JSON string
static_code_response_post_instance = StaticCodeResponsePost.from_json(json)
# print the JSON string representation of the object
print StaticCodeResponsePost.to_json()

# convert the object into a dict
static_code_response_post_dict = static_code_response_post_instance.to_dict()
# create an instance of StaticCodeResponsePost from a dict
static_code_response_post_form_dict = static_code_response_post.from_dict(static_code_response_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


