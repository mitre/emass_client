# TestResultsResponsePost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Response200**](Response200.md) |  | [optional] 
**data** | [**List[TestResultsPost]**](TestResultsPost.md) |  | [optional] 

## Example

```python
from emass_client.models.test_results_response_post import TestResultsResponsePost

# TODO update the JSON string below
json = "{}"
# create an instance of TestResultsResponsePost from a JSON string
test_results_response_post_instance = TestResultsResponsePost.from_json(json)
# print the JSON string representation of the object
print(TestResultsResponsePost.to_json())

# convert the object into a dict
test_results_response_post_dict = test_results_response_post_instance.to_dict()
# create an instance of TestResultsResponsePost from a dict
test_results_response_post_from_dict = TestResultsResponsePost.from_dict(test_results_response_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


