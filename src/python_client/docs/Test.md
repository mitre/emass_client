# Test


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Response200**](Response200.md) |  | [optional] 
**data** | [**TestData**](TestData.md) |  | [optional] 

## Example

```python
from emass_client.models.test import Test

# TODO update the JSON string below
json = "{}"
# create an instance of Test from a JSON string
test_instance = Test.from_json(json)
# print the JSON string representation of the object
print Test.to_json()

# convert the object into a dict
test_dict = test_instance.to_dict()
# create an instance of Test from a dict
test_form_dict = test.from_dict(test_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


