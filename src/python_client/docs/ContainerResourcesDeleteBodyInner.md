# ContainerResourcesDeleteBodyInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**container_id** | **str** | [Required] Unique item identifier | [optional] 

## Example

```python
from emass_client.models.container_resources_delete_body_inner import ContainerResourcesDeleteBodyInner

# TODO update the JSON string below
json = "{}"
# create an instance of ContainerResourcesDeleteBodyInner from a JSON string
container_resources_delete_body_inner_instance = ContainerResourcesDeleteBodyInner.from_json(json)
# print the JSON string representation of the object
print ContainerResourcesDeleteBodyInner.to_json()

# convert the object into a dict
container_resources_delete_body_inner_dict = container_resources_delete_body_inner_instance.to_dict()
# create an instance of ContainerResourcesDeleteBodyInner from a dict
container_resources_delete_body_inner_form_dict = container_resources_delete_body_inner.from_dict(container_resources_delete_body_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


