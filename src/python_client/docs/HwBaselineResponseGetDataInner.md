# HwBaselineResponseGetDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**system_id** | **int** | [Required] Unique eMASS system identifier. | [optional] 
**hardware_id** | **str** | [Read-Only] GUID identifying the specific hardware asset. Required for a PUT call. | [optional] 
**asset_name** | **str** | [Required] Name of the hardware asset. | [optional] 
**component_type** | **str** | [Optional] Type of the hardware asset. | [optional] 
**nickname** | **str** | [Optional] Nickname of the hardware asset. | [optional] 
**asset_ip_address** | **str** | [Optional] IP address of the hardware asset. | [optional] 
**public_facing** | **bool** | [Optional] Public facing is defined as any asset that is accessible from a commercial connection. | [optional] 
**virtual_asset** | **bool** | [Optional] Determine if this is a virtual hardware asset. | [optional] 
**manufacturer** | **str** | [Optional] Manufacturer of the hardware asset. Populated with \&quot;Virtual\&quot; by default if Virtual Asset is true, however this can be overridden. | [optional] 
**model_number** | **str** | [Optional] Model number of the hardware asset. Populated with \&quot;Virtual\&quot; by default if Virtual Asset is true, however this can be overridden | [optional] 
**serial_number** | **str** | [Optional] Serial number of the hardware asset. Populated with \&quot;Virtual\&quot; by default if Virtual Asset is true, however this can be overridden. | [optional] 
**os_ios_fw_version** | **str** | [Optional] Operating System, IOS, or Firmware version of the hardware asset. | [optional] 
**memory_size_type** | **str** | [Optional] Memory size / type of the hardware asset. | [optional] 
**location** | **str** | [Optional] Location of the hardware asset. | [optional] 
**approval_status** | **str** | [Optional] Approval status of the hardware asset. | [optional] 
**critical_asset** | **bool** | [Optional] Indicates whether the asset is a critical information system asset. | [optional] 
**public_facing_fqdn** | **str** | [Conditional] Public facing FQDN. Only applicable if Public Facing is set to true. | [optional] 
**public_facing_ip_address** | **str** | [Conditional] Public facing IP address. Only applicable if Public Facing is set to true. | [optional] 
**public_facing_urls** | **str** | [Conditional] Public facing URLs. Only applicable if Public Facing is set to true. | [optional] 

## Example

```python
from emass_client.models.hw_baseline_response_get_data_inner import HwBaselineResponseGetDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of HwBaselineResponseGetDataInner from a JSON string
hw_baseline_response_get_data_inner_instance = HwBaselineResponseGetDataInner.from_json(json)
# print the JSON string representation of the object
print(HwBaselineResponseGetDataInner.to_json())

# convert the object into a dict
hw_baseline_response_get_data_inner_dict = hw_baseline_response_get_data_inner_instance.to_dict()
# create an instance of HwBaselineResponseGetDataInner from a dict
hw_baseline_response_get_data_inner_from_dict = HwBaselineResponseGetDataInner.from_dict(hw_baseline_response_get_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


