# CloudResourcesDelete


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Response200**](Response200.md) |  | [optional] 
**data** | [**List[CloudResourcesPostDelete]**](CloudResourcesPostDelete.md) |  | [optional] 

## Example

```python
from emass_client.models.cloud_resources_delete import CloudResourcesDelete

# TODO update the JSON string below
json = "{}"
# create an instance of CloudResourcesDelete from a JSON string
cloud_resources_delete_instance = CloudResourcesDelete.from_json(json)
# print the JSON string representation of the object
print CloudResourcesDelete.to_json()

# convert the object into a dict
cloud_resources_delete_dict = cloud_resources_delete_instance.to_dict()
# create an instance of CloudResourcesDelete from a dict
cloud_resources_delete_form_dict = cloud_resources_delete.from_dict(cloud_resources_delete_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


