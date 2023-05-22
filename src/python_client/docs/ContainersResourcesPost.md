# ContainersResourcesPost


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**container_id** | **str** | [Required] Unique identifier of the container | [optional] 
**success** | **bool** |  | [optional] 
**system_id** | **int** |  | [optional] 
**errors** | **List[object]** |  | [optional] 

## Example

```python
from emass_client.models.containers_resources_post import ContainersResourcesPost

# TODO update the JSON string below
json = "{}"
# create an instance of ContainersResourcesPost from a JSON string
containers_resources_post_instance = ContainersResourcesPost.from_json(json)
# print the JSON string representation of the object
print ContainersResourcesPost.to_json()

# convert the object into a dict
containers_resources_post_dict = containers_resources_post_instance.to_dict()
# create an instance of ContainersResourcesPost from a dict
containers_resources_post_form_dict = containers_resources_post.from_dict(containers_resources_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


