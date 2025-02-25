# SystemsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Response200**](Response200.md) |  | [optional] 
**data** | [**List[Systems]**](Systems.md) |  | [optional] 

## Example

```python
from emass_client.models.systems_response import SystemsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SystemsResponse from a JSON string
systems_response_instance = SystemsResponse.from_json(json)
# print the JSON string representation of the object
print(SystemsResponse.to_json())

# convert the object into a dict
systems_response_dict = systems_response_instance.to_dict()
# create an instance of SystemsResponse from a dict
systems_response_from_dict = SystemsResponse.from_dict(systems_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


