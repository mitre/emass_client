# Response401Meta


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [default to 401]
**error_message** | **str** |  | [optional] [default to 'Request has failed to provide suitable authentication from the client']

## Example

```python
from emass_client.models.response401_meta import Response401Meta

# TODO update the JSON string below
json = "{}"
# create an instance of Response401Meta from a JSON string
response401_meta_instance = Response401Meta.from_json(json)
# print the JSON string representation of the object
print Response401Meta.to_json()

# convert the object into a dict
response401_meta_dict = response401_meta_instance.to_dict()
# create an instance of Response401Meta from a dict
response401_meta_form_dict = response401_meta.from_dict(response401_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


