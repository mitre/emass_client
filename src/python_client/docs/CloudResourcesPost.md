# CloudResourcesPost


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **str** | [Required] Unique identifier/resource namespace for policy compliance result | [optional] 
**success** | **bool** |  | [optional] 
**system_id** | **int** |  | [optional] 
**errors** | **List[object]** |  | [optional] 

## Example

```python
from emass_client.models.cloud_resources_post import CloudResourcesPost

# TODO update the JSON string below
json = "{}"
# create an instance of CloudResourcesPost from a JSON string
cloud_resources_post_instance = CloudResourcesPost.from_json(json)
# print the JSON string representation of the object
print CloudResourcesPost.to_json()

# convert the object into a dict
cloud_resources_post_dict = cloud_resources_post_instance.to_dict()
# create an instance of CloudResourcesPost from a dict
cloud_resources_post_form_dict = cloud_resources_post.from_dict(cloud_resources_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


