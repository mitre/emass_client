# Response500Meta


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [default to 500]
**error_message** | **str** |  | [optional] [default to 'Server encountered an unexpected condition which prevented it from fulfilling the request']

## Example

```python
from emass_client.models.response500_meta import Response500Meta

# TODO update the JSON string below
json = "{}"
# create an instance of Response500Meta from a JSON string
response500_meta_instance = Response500Meta.from_json(json)
# print the JSON string representation of the object
print Response500Meta.to_json()

# convert the object into a dict
response500_meta_dict = response500_meta_instance.to_dict()
# create an instance of Response500Meta from a dict
response500_meta_form_dict = response500_meta.from_dict(response500_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


