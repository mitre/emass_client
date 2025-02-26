# UnauthorizedMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [default to 401]
**error_message** | **str** |  | [optional] [default to 'Request has failed to provide suitable authentication from the client']

## Example

```python
from emass_client.models.unauthorized_meta import UnauthorizedMeta

# TODO update the JSON string below
json = "{}"
# create an instance of UnauthorizedMeta from a JSON string
unauthorized_meta_instance = UnauthorizedMeta.from_json(json)
# print the JSON string representation of the object
print(UnauthorizedMeta.to_json())

# convert the object into a dict
unauthorized_meta_dict = unauthorized_meta_instance.to_dict()
# create an instance of UnauthorizedMeta from a dict
unauthorized_meta_from_dict = UnauthorizedMeta.from_dict(unauthorized_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


