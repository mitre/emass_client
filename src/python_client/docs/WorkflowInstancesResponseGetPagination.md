# WorkflowInstancesResponseGetPagination


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**prev_page_url** | **str** |  | [optional] 
**next_page_url** | **str** |  | [optional] 

## Example

```python
from emass_client.models.workflow_instances_response_get_pagination import WorkflowInstancesResponseGetPagination

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowInstancesResponseGetPagination from a JSON string
workflow_instances_response_get_pagination_instance = WorkflowInstancesResponseGetPagination.from_json(json)
# print the JSON string representation of the object
print WorkflowInstancesResponseGetPagination.to_json()

# convert the object into a dict
workflow_instances_response_get_pagination_dict = workflow_instances_response_get_pagination_instance.to_dict()
# create an instance of WorkflowInstancesResponseGetPagination from a dict
workflow_instances_response_get_pagination_form_dict = workflow_instances_response_get_pagination.from_dict(workflow_instances_response_get_pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


