# HwBaselineResponseDelete


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Response200**](Response200.md) |  | [optional] 
**data** | [**List[HwBaselineResponseDeleteDataInner]**](HwBaselineResponseDeleteDataInner.md) |  | [optional] 

## Example

```python
from emass_client.models.hw_baseline_response_delete import HwBaselineResponseDelete

# TODO update the JSON string below
json = "{}"
# create an instance of HwBaselineResponseDelete from a JSON string
hw_baseline_response_delete_instance = HwBaselineResponseDelete.from_json(json)
# print the JSON string representation of the object
print(HwBaselineResponseDelete.to_json())

# convert the object into a dict
hw_baseline_response_delete_dict = hw_baseline_response_delete_instance.to_dict()
# create an instance of HwBaselineResponseDelete from a dict
hw_baseline_response_delete_from_dict = HwBaselineResponseDelete.from_dict(hw_baseline_response_delete_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


