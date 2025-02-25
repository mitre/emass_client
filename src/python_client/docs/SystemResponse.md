# SystemResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Response200**](Response200.md) |  | [optional] 
**data** | [**Systems**](Systems.md) |  | [optional] 

## Example

```python
from emass_client.models.system_response import SystemResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SystemResponse from a JSON string
system_response_instance = SystemResponse.from_json(json)
# print the JSON string representation of the object
print(SystemResponse.to_json())

# convert the object into a dict
system_response_dict = system_response_instance.to_dict()
# create an instance of SystemResponse from a dict
system_response_from_dict = SystemResponse.from_dict(system_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


