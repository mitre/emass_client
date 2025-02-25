# HwBaselineRequiredFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_name** | **str** | [Required] Name of the hardware asset. | [optional] 

## Example

```python
from emass_client.models.hw_baseline_required_fields import HwBaselineRequiredFields

# TODO update the JSON string below
json = "{}"
# create an instance of HwBaselineRequiredFields from a JSON string
hw_baseline_required_fields_instance = HwBaselineRequiredFields.from_json(json)
# print the JSON string representation of the object
print(HwBaselineRequiredFields.to_json())

# convert the object into a dict
hw_baseline_required_fields_dict = hw_baseline_required_fields_instance.to_dict()
# create an instance of HwBaselineRequiredFields from a dict
hw_baseline_required_fields_from_dict = HwBaselineRequiredFields.from_dict(hw_baseline_required_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


