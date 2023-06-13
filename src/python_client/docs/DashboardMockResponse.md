# DashboardMockResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Response200**](Response200.md) |  | [optional] 
**data** | [**List[MockObject]**](MockObject.md) |  | [optional] 
**pagination** | [**DashboardMockResponsePagination**](DashboardMockResponsePagination.md) |  | [optional] 

## Example

```python
from emass_client.models.dashboard_mock_response import DashboardMockResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DashboardMockResponse from a JSON string
dashboard_mock_response_instance = DashboardMockResponse.from_json(json)
# print the JSON string representation of the object
print DashboardMockResponse.to_json()

# convert the object into a dict
dashboard_mock_response_dict = dashboard_mock_response_instance.to_dict()
# create an instance of DashboardMockResponse from a dict
dashboard_mock_response_form_dict = dashboard_mock_response.from_dict(dashboard_mock_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


