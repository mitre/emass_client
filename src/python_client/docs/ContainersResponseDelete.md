# ContainersResponseDelete


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Response200**](Response200.md) |  | [optional] 
**data** | [**List[ContainersResourcesPostDelete]**](ContainersResourcesPostDelete.md) |  | [optional] 

## Example

```python
from emass_client.models.containers_response_delete import ContainersResponseDelete

# TODO update the JSON string below
json = "{}"
# create an instance of ContainersResponseDelete from a JSON string
containers_response_delete_instance = ContainersResponseDelete.from_json(json)
# print the JSON string representation of the object
print(ContainersResponseDelete.to_json())

# convert the object into a dict
containers_response_delete_dict = containers_response_delete_instance.to_dict()
# create an instance of ContainersResponseDelete from a dict
containers_response_delete_from_dict = ContainersResponseDelete.from_dict(containers_response_delete_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


