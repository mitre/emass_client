# CreatedMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [default to 201]
**message** | **str** |  | [optional] [default to 'Request was fulfilled and resulted in on or more new resources being successfully created on the server.']

## Example

```python
from emass_client.models.created_meta import CreatedMeta

# TODO update the JSON string below
json = "{}"
# create an instance of CreatedMeta from a JSON string
created_meta_instance = CreatedMeta.from_json(json)
# print the JSON string representation of the object
print(CreatedMeta.to_json())

# convert the object into a dict
created_meta_dict = created_meta_instance.to_dict()
# create an instance of CreatedMeta from a dict
created_meta_from_dict = CreatedMeta.from_dict(created_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


