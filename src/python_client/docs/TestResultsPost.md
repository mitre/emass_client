# TestResultsPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cci** | **str** | CCI associated with test result. | [optional] 
**success** | **bool** | Indicates if operations result (success/fail) | [optional] 
**system_id** | **int** | The system identifier for the system being updated. | [optional] 
**errors** | **List[object]** |  | [optional] 

## Example

```python
from emass_client.models.test_results_post import TestResultsPost

# TODO update the JSON string below
json = "{}"
# create an instance of TestResultsPost from a JSON string
test_results_post_instance = TestResultsPost.from_json(json)
# print the JSON string representation of the object
print(TestResultsPost.to_json())

# convert the object into a dict
test_results_post_dict = test_results_post_instance.to_dict()
# create an instance of TestResultsPost from a dict
test_results_post_from_dict = TestResultsPost.from_dict(test_results_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


