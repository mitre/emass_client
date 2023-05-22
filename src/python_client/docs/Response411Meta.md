# Response411Meta


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [default to 411]
**error_message** | **str** |  | [optional] [default to 'Request was of type POST and failed to provide the server information about the data/content length being submitted']

## Example

```python
from emass_client.models.response411_meta import Response411Meta

# TODO update the JSON string below
json = "{}"
# create an instance of Response411Meta from a JSON string
response411_meta_instance = Response411Meta.from_json(json)
# print the JSON string representation of the object
print Response411Meta.to_json()

# convert the object into a dict
response411_meta_dict = response411_meta_instance.to_dict()
# create an instance of Response411Meta from a dict
response411_meta_form_dict = response411_meta.from_dict(response411_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


