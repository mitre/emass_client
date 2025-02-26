# SwBaselineResponseGet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Response200**](Response200.md) |  | [optional] 
**data** | [**List[SwBaselineResponseGetDataInner]**](SwBaselineResponseGetDataInner.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from emass_client.models.sw_baseline_response_get import SwBaselineResponseGet

# TODO update the JSON string below
json = "{}"
# create an instance of SwBaselineResponseGet from a JSON string
sw_baseline_response_get_instance = SwBaselineResponseGet.from_json(json)
# print the JSON string representation of the object
print(SwBaselineResponseGet.to_json())

# convert the object into a dict
sw_baseline_response_get_dict = sw_baseline_response_get_instance.to_dict()
# create an instance of SwBaselineResponseGet from a dict
sw_baseline_response_get_from_dict = SwBaselineResponseGet.from_dict(sw_baseline_response_get_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


