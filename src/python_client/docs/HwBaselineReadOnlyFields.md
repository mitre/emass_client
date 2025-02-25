# HwBaselineReadOnlyFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hardware_id** | **str** | [Read-Only] GUID identifying the specific hardware asset. Required for a PUT call. | [optional] 

## Example

```python
from emass_client.models.hw_baseline_read_only_fields import HwBaselineReadOnlyFields

# TODO update the JSON string below
json = "{}"
# create an instance of HwBaselineReadOnlyFields from a JSON string
hw_baseline_read_only_fields_instance = HwBaselineReadOnlyFields.from_json(json)
# print the JSON string representation of the object
print(HwBaselineReadOnlyFields.to_json())

# convert the object into a dict
hw_baseline_read_only_fields_dict = hw_baseline_read_only_fields_instance.to_dict()
# create an instance of HwBaselineReadOnlyFields from a dict
hw_baseline_read_only_fields_from_dict = HwBaselineReadOnlyFields.from_dict(hw_baseline_read_only_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


