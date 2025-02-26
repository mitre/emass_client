# MethodNotAllowedMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [default to 405]
**error_message** | **str** |  | [optional] [default to 'Request was made with a verb (GET, POST, etc.) that is not permitted for the endpoint']

## Example

```python
from emass_client.models.method_not_allowed_meta import MethodNotAllowedMeta

# TODO update the JSON string below
json = "{}"
# create an instance of MethodNotAllowedMeta from a JSON string
method_not_allowed_meta_instance = MethodNotAllowedMeta.from_json(json)
# print the JSON string representation of the object
print(MethodNotAllowedMeta.to_json())

# convert the object into a dict
method_not_allowed_meta_dict = method_not_allowed_meta_instance.to_dict()
# create an instance of MethodNotAllowedMeta from a dict
method_not_allowed_meta_from_dict = MethodNotAllowedMeta.from_dict(method_not_allowed_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


