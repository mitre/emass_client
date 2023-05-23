# Response400Meta


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [default to 400]
**error_message** | **str** |  | [optional] [default to 'Request could not be understood by the server due to incorrect syntax or an unexpected format']

## Example

```python
from emass_client.models.response400_meta import Response400Meta

# TODO update the JSON string below
json = "{}"
# create an instance of Response400Meta from a JSON string
response400_meta_instance = Response400Meta.from_json(json)
# print the JSON string representation of the object
print Response400Meta.to_json()

# convert the object into a dict
response400_meta_dict = response400_meta_instance.to_dict()
# create an instance of Response400Meta from a dict
response400_meta_form_dict = response400_meta.from_dict(response400_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


