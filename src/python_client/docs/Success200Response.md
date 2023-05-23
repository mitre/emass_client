# Success200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Response200**](Response200.md) |  | [optional] 
**data** | [**List[Success200ResponseDataInner]**](Success200ResponseDataInner.md) |  | [optional] 

## Example

```python
from emass_client.models.success200_response import Success200Response

# TODO update the JSON string below
json = "{}"
# create an instance of Success200Response from a JSON string
success200_response_instance = Success200Response.from_json(json)
# print the JSON string representation of the object
print Success200Response.to_json()

# convert the object into a dict
success200_response_dict = success200_response_instance.to_dict()
# create an instance of Success200Response from a dict
success200_response_form_dict = success200_response.from_dict(success200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


