# CloudResourcesResponsePost


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Response200**](Response200.md) |  | [optional] 
**data** | [**List[CloudResourcesPost]**](CloudResourcesPost.md) |  | [optional] 

## Example

```python
from emass_client.models.cloud_resources_response_post import CloudResourcesResponsePost

# TODO update the JSON string below
json = "{}"
# create an instance of CloudResourcesResponsePost from a JSON string
cloud_resources_response_post_instance = CloudResourcesResponsePost.from_json(json)
# print the JSON string representation of the object
print CloudResourcesResponsePost.to_json()

# convert the object into a dict
cloud_resources_response_post_dict = cloud_resources_response_post_instance.to_dict()
# create an instance of CloudResourcesResponsePost from a dict
cloud_resources_response_post_form_dict = cloud_resources_response_post.from_dict(cloud_resources_response_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


