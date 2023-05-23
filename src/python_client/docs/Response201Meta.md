# Response201Meta


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [default to 201]
**message** | **str** |  | [optional] [default to 'Request was fulfilled and resulted in on or more new resources being successfully created on the server.']

## Example

```python
from emass_client.models.response201_meta import Response201Meta

# TODO update the JSON string below
json = "{}"
# create an instance of Response201Meta from a JSON string
response201_meta_instance = Response201Meta.from_json(json)
# print the JSON string representation of the object
print Response201Meta.to_json()

# convert the object into a dict
response201_meta_dict = response201_meta_instance.to_dict()
# create an instance of Response201Meta from a dict
response201_meta_form_dict = response201_meta.from_dict(response201_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


