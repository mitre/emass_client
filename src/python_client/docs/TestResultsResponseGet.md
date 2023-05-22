# TestResultsResponseGet


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Response200**](Response200.md) |  | [optional] 
**data** | [**List[TestResultsGet]**](TestResultsGet.md) |  | [optional] 

## Example

```python
from emass_client.models.test_results_response_get import TestResultsResponseGet

# TODO update the JSON string below
json = "{}"
# create an instance of TestResultsResponseGet from a JSON string
test_results_response_get_instance = TestResultsResponseGet.from_json(json)
# print the JSON string representation of the object
print TestResultsResponseGet.to_json()

# convert the object into a dict
test_results_response_get_dict = test_results_response_get_instance.to_dict()
# create an instance of TestResultsResponseGet from a dict
test_results_response_get_form_dict = test_results_response_get.from_dict(test_results_response_get_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


