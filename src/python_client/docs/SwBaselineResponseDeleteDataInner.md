# SwBaselineResponseDeleteDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**system_id** | **int** |  | [optional] 
**software_id** | **str** |  | [optional] 
**success** | **bool** |  | [optional] 
**errors** | **List[object]** |  | [optional] 

## Example

```python
from emass_client.models.sw_baseline_response_delete_data_inner import SwBaselineResponseDeleteDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of SwBaselineResponseDeleteDataInner from a JSON string
sw_baseline_response_delete_data_inner_instance = SwBaselineResponseDeleteDataInner.from_json(json)
# print the JSON string representation of the object
print(SwBaselineResponseDeleteDataInner.to_json())

# convert the object into a dict
sw_baseline_response_delete_data_inner_dict = sw_baseline_response_delete_data_inner_instance.to_dict()
# create an instance of SwBaselineResponseDeleteDataInner from a dict
sw_baseline_response_delete_data_inner_from_dict = SwBaselineResponseDeleteDataInner.from_dict(sw_baseline_response_delete_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


