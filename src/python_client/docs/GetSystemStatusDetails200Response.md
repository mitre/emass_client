# GetSystemStatusDetails200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Response200**](Response200.md) |  | [optional] 
**data** | **List[object]** |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from emass_client.models.get_system_status_details200_response import GetSystemStatusDetails200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetSystemStatusDetails200Response from a JSON string
get_system_status_details200_response_instance = GetSystemStatusDetails200Response.from_json(json)
# print the JSON string representation of the object
print(GetSystemStatusDetails200Response.to_json())

# convert the object into a dict
get_system_status_details200_response_dict = get_system_status_details200_response_instance.to_dict()
# create an instance of GetSystemStatusDetails200Response from a dict
get_system_status_details200_response_from_dict = GetSystemStatusDetails200Response.from_dict(get_system_status_details200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


