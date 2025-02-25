# ForbiddenMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [default to 403]
**error_message** | **str** |  | [optional] [default to 'Request was blocked by the application due to a lack of client permissions to the API or to a specific endpoint']

## Example

```python
from emass_client.models.forbidden_meta import ForbiddenMeta

# TODO update the JSON string below
json = "{}"
# create an instance of ForbiddenMeta from a JSON string
forbidden_meta_instance = ForbiddenMeta.from_json(json)
# print the JSON string representation of the object
print(ForbiddenMeta.to_json())

# convert the object into a dict
forbidden_meta_dict = forbidden_meta_instance.to_dict()
# create an instance of ForbiddenMeta from a dict
forbidden_meta_from_dict = ForbiddenMeta.from_dict(forbidden_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


