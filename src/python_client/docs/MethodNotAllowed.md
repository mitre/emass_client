# MethodNotAllowed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**MethodNotAllowedMeta**](MethodNotAllowedMeta.md) |  | [optional] 

## Example

```python
from emass_client.models.method_not_allowed import MethodNotAllowed

# TODO update the JSON string below
json = "{}"
# create an instance of MethodNotAllowed from a JSON string
method_not_allowed_instance = MethodNotAllowed.from_json(json)
# print the JSON string representation of the object
print(MethodNotAllowed.to_json())

# convert the object into a dict
method_not_allowed_dict = method_not_allowed_instance.to_dict()
# create an instance of MethodNotAllowed from a dict
method_not_allowed_from_dict = MethodNotAllowed.from_dict(method_not_allowed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


