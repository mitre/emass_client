# ContainersResponsePost


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Response200**](Response200.md) |  | [optional] 
**data** | [**List[ContainersResourcesPostDelete]**](ContainersResourcesPostDelete.md) |  | [optional] 

## Example

```python
from emass_client.models.containers_response_post import ContainersResponsePost

# TODO update the JSON string below
json = "{}"
# create an instance of ContainersResponsePost from a JSON string
containers_response_post_instance = ContainersResponsePost.from_json(json)
# print the JSON string representation of the object
print ContainersResponsePost.to_json()

# convert the object into a dict
containers_response_post_dict = containers_response_post_instance.to_dict()
# create an instance of ContainersResponsePost from a dict
containers_response_post_form_dict = containers_response_post.from_dict(containers_response_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


