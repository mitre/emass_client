# ContainersResourcesPostDelete


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**container_id** | **str** | [Required] Unique identifier of the container | [optional] 
**success** | **bool** |  | [optional] 
**system_id** | **int** |  | [optional] 
**errors** | **List[object]** |  | [optional] 

## Example

```python
from emass_client.models.containers_resources_post_delete import ContainersResourcesPostDelete

# TODO update the JSON string below
json = "{}"
# create an instance of ContainersResourcesPostDelete from a JSON string
containers_resources_post_delete_instance = ContainersResourcesPostDelete.from_json(json)
# print the JSON string representation of the object
print(ContainersResourcesPostDelete.to_json())

# convert the object into a dict
containers_resources_post_delete_dict = containers_resources_post_delete_instance.to_dict()
# create an instance of ContainersResourcesPostDelete from a dict
containers_resources_post_delete_from_dict = ContainersResourcesPostDelete.from_dict(containers_resources_post_delete_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


