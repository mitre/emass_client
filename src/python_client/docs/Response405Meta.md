# Response405Meta


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [default to 405]
**error_message** | **str** |  | [optional] [default to 'Request was made with a verb (GET, POST, etc.) that is not permitted for the endpoint']

## Example

```python
from emass_client.models.response405_meta import Response405Meta

# TODO update the JSON string below
json = "{}"
# create an instance of Response405Meta from a JSON string
response405_meta_instance = Response405Meta.from_json(json)
# print the JSON string representation of the object
print Response405Meta.to_json()

# convert the object into a dict
response405_meta_dict = response405_meta_instance.to_dict()
# create an instance of Response405Meta from a dict
response405_meta_form_dict = response405_meta.from_dict(response405_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


