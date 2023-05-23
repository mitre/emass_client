# Response490Meta


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [default to 490]
**error_message** | **str** |  | [optional] [default to 'Request has failed because too much data was requested in a single batch. This error is specific to eMASS']

## Example

```python
from emass_client.models.response490_meta import Response490Meta

# TODO update the JSON string below
json = "{}"
# create an instance of Response490Meta from a JSON string
response490_meta_instance = Response490Meta.from_json(json)
# print the JSON string representation of the object
print Response490Meta.to_json()

# convert the object into a dict
response490_meta_dict = response490_meta_instance.to_dict()
# create an instance of Response490Meta from a dict
response490_meta_form_dict = response490_meta.from_dict(response490_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


