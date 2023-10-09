# CloudResourcesDeleteBodyInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **str** | [Required] Unique item identifier | [optional] 

## Example

```python
from emass_client.models.cloud_resources_delete_body_inner import CloudResourcesDeleteBodyInner

# TODO update the JSON string below
json = "{}"
# create an instance of CloudResourcesDeleteBodyInner from a JSON string
cloud_resources_delete_body_inner_instance = CloudResourcesDeleteBodyInner.from_json(json)
# print the JSON string representation of the object
print CloudResourcesDeleteBodyInner.to_json()

# convert the object into a dict
cloud_resources_delete_body_inner_dict = cloud_resources_delete_body_inner_instance.to_dict()
# create an instance of CloudResourcesDeleteBodyInner from a dict
cloud_resources_delete_body_inner_form_dict = cloud_resources_delete_body_inner.from_dict(cloud_resources_delete_body_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


