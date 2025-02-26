# NotFound


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [default to 404]
**error_message** | **str** |  | [optional] [default to 'Request has failed because the URL provided in the request did not match any available endpoint locations']

## Example

```python
from emass_client.models.not_found import NotFound

# TODO update the JSON string below
json = "{}"
# create an instance of NotFound from a JSON string
not_found_instance = NotFound.from_json(json)
# print the JSON string representation of the object
print(NotFound.to_json())

# convert the object into a dict
not_found_dict = not_found_instance.to_dict()
# create an instance of NotFound from a dict
not_found_from_dict = NotFound.from_dict(not_found_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


