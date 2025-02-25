# LengthRequiredMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [default to 411]
**error_message** | **str** |  | [optional] [default to 'Request was of type POST and failed to provide the server information about the data/content length being submitted']

## Example

```python
from emass_client.models.length_required_meta import LengthRequiredMeta

# TODO update the JSON string below
json = "{}"
# create an instance of LengthRequiredMeta from a JSON string
length_required_meta_instance = LengthRequiredMeta.from_json(json)
# print the JSON string representation of the object
print(LengthRequiredMeta.to_json())

# convert the object into a dict
length_required_meta_dict = length_required_meta_instance.to_dict()
# create an instance of LengthRequiredMeta from a dict
length_required_meta_from_dict = LengthRequiredMeta.from_dict(length_required_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


