# BadRequestMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [default to 400]
**error_message** | **str** |  | [optional] [default to 'Request could not be understood by the server due to incorrect syntax or an unexpected format']

## Example

```python
from emass_client.models.bad_request_meta import BadRequestMeta

# TODO update the JSON string below
json = "{}"
# create an instance of BadRequestMeta from a JSON string
bad_request_meta_instance = BadRequestMeta.from_json(json)
# print the JSON string representation of the object
print(BadRequestMeta.to_json())

# convert the object into a dict
bad_request_meta_dict = bad_request_meta_instance.to_dict()
# create an instance of BadRequestMeta from a dict
bad_request_meta_from_dict = BadRequestMeta.from_dict(bad_request_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


