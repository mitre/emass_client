# Response403Meta


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [default to 403]
**error_message** | **str** |  | [optional] [default to 'Request was blocked by the application due to a lack of client permissions to the API or to a specific endpoint']

## Example

```python
from emass_client.models.response403_meta import Response403Meta

# TODO update the JSON string below
json = "{}"
# create an instance of Response403Meta from a JSON string
response403_meta_instance = Response403Meta.from_json(json)
# print the JSON string representation of the object
print Response403Meta.to_json()

# convert the object into a dict
response403_meta_dict = response403_meta_instance.to_dict()
# create an instance of Response403Meta from a dict
response403_meta_form_dict = response403_meta.from_dict(response403_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


