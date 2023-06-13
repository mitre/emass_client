# DashboardMockResponsePagination


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**page_index** | **int** |  | [optional] 
**page_size** | **int** |  | [optional] 
**prev_page_url** | **str** |  | [optional] 
**next_page_url** | **str** |  | [optional] 

## Example

```python
from emass_client.models.dashboard_mock_response_pagination import DashboardMockResponsePagination

# TODO update the JSON string below
json = "{}"
# create an instance of DashboardMockResponsePagination from a JSON string
dashboard_mock_response_pagination_instance = DashboardMockResponsePagination.from_json(json)
# print the JSON string representation of the object
print DashboardMockResponsePagination.to_json()

# convert the object into a dict
dashboard_mock_response_pagination_dict = dashboard_mock_response_pagination_instance.to_dict()
# create an instance of DashboardMockResponsePagination from a dict
dashboard_mock_response_pagination_form_dict = dashboard_mock_response_pagination.from_dict(dashboard_mock_response_pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


