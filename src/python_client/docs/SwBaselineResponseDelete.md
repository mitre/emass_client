# SwBaselineResponseDelete


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Response200**](Response200.md) |  | [optional] 
**data** | [**List[SwBaselineResponseDeleteDataInner]**](SwBaselineResponseDeleteDataInner.md) |  | [optional] 

## Example

```python
from emass_client.models.sw_baseline_response_delete import SwBaselineResponseDelete

# TODO update the JSON string below
json = "{}"
# create an instance of SwBaselineResponseDelete from a JSON string
sw_baseline_response_delete_instance = SwBaselineResponseDelete.from_json(json)
# print the JSON string representation of the object
print(SwBaselineResponseDelete.to_json())

# convert the object into a dict
sw_baseline_response_delete_dict = sw_baseline_response_delete_instance.to_dict()
# create an instance of SwBaselineResponseDelete from a dict
sw_baseline_response_delete_from_dict = SwBaselineResponseDelete.from_dict(sw_baseline_response_delete_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


