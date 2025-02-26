# InternalServerErrorMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [default to 500]
**error_message** | **str** |  | [optional] [default to 'Server encountered an unexpected condition which prevented it from fulfilling the request']

## Example

```python
from emass_client.models.internal_server_error_meta import InternalServerErrorMeta

# TODO update the JSON string below
json = "{}"
# create an instance of InternalServerErrorMeta from a JSON string
internal_server_error_meta_instance = InternalServerErrorMeta.from_json(json)
# print the JSON string representation of the object
print(InternalServerErrorMeta.to_json())

# convert the object into a dict
internal_server_error_meta_dict = internal_server_error_meta_instance.to_dict()
# create an instance of InternalServerErrorMeta from a dict
internal_server_error_meta_from_dict = InternalServerErrorMeta.from_dict(internal_server_error_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


