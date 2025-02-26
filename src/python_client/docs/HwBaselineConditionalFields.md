# HwBaselineConditionalFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**public_facing_fqdn** | **str** | [Conditional] Public facing FQDN. Only applicable if Public Facing is set to true. | [optional] 
**public_facing_ip_address** | **str** | [Conditional] Public facing IP address. Only applicable if Public Facing is set to true. | [optional] 
**public_facing_urls** | **str** | [Conditional] Public facing URLs. Only applicable if Public Facing is set to true. | [optional] 

## Example

```python
from emass_client.models.hw_baseline_conditional_fields import HwBaselineConditionalFields

# TODO update the JSON string below
json = "{}"
# create an instance of HwBaselineConditionalFields from a JSON string
hw_baseline_conditional_fields_instance = HwBaselineConditionalFields.from_json(json)
# print the JSON string representation of the object
print(HwBaselineConditionalFields.to_json())

# convert the object into a dict
hw_baseline_conditional_fields_dict = hw_baseline_conditional_fields_instance.to_dict()
# create an instance of HwBaselineConditionalFields from a dict
hw_baseline_conditional_fields_from_dict = HwBaselineConditionalFields.from_dict(hw_baseline_conditional_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


