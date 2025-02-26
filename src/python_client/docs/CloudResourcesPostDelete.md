# CloudResourcesPostDelete


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **str** | [Required] Unique identifier/resource namespace for policy compliance result | [optional] 
**success** | **bool** |  | [optional] 
**system_id** | **int** |  | [optional] 
**errors** | **List[object]** |  | [optional] 

## Example

```python
from emass_client.models.cloud_resources_post_delete import CloudResourcesPostDelete

# TODO update the JSON string below
json = "{}"
# create an instance of CloudResourcesPostDelete from a JSON string
cloud_resources_post_delete_instance = CloudResourcesPostDelete.from_json(json)
# print the JSON string representation of the object
print(CloudResourcesPostDelete.to_json())

# convert the object into a dict
cloud_resources_post_delete_dict = cloud_resources_post_delete_instance.to_dict()
# create an instance of CloudResourcesPostDelete from a dict
cloud_resources_post_delete_from_dict = CloudResourcesPostDelete.from_dict(cloud_resources_post_delete_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


