# EmassClient::HwBaselineOptionalFields

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **component_type** | **String** | [Optional] Type of the hardware asset. | [optional] |
| **nickname** | **String** | [Optional] Nickname of the hardware asset. | [optional] |
| **asset_ip_address** | **String** | [Optional] IP address of the hardware asset. | [optional] |
| **public_facing** | **Boolean** | [Optional] Public facing is defined as any asset that is accessible from a commercial connection. | [optional] |
| **virtual_asset** | **Boolean** | [Optional] Determine if this is a virtual hardware asset. | [optional] |
| **manufacturer** | **String** | [Optional] Manufacturer of the hardware asset. Populated with \&quot;Virtual\&quot; by default if Virtual Asset is true, however this can be overridden. | [optional] |
| **model_number** | **String** | [Optional] Model number of the hardware asset. Populated with \&quot;Virtual\&quot; by default if Virtual Asset is true, however this can be overridden | [optional] |
| **serial_number** | **String** | [Optional] Serial number of the hardware asset. Populated with \&quot;Virtual\&quot; by default if Virtual Asset is true, however this can be overridden. | [optional] |
| **os_ios_fw_version** | **String** | [Optional] Operating System, IOS, or Firmware version of the hardware asset. | [optional] |
| **memory_size_type** | **String** | [Optional] Memory size / type of the hardware asset. | [optional] |
| **location** | **String** | [Optional] Location of the hardware asset. | [optional] |
| **approval_status** | **String** | [Optional] Approval status of the hardware asset. | [optional] |
| **critical_asset** | **Boolean** | [Optional] Indicates whether the asset is a critical information system asset. | [optional] |

## Example

```ruby
require 'emass_client'

instance = EmassClient::HwBaselineOptionalFields.new(
  component_type: IDS/IPS,
  nickname: Hardware,
  asset_ip_address: 79.102.116.145,
  public_facing: true,
  virtual_asset: false,
  manufacturer: Test Manufacturer,
  model_number: 1.0,
  serial_number: 5.2.1.5,
  os_ios_fw_version: Win Server 2000,
  memory_size_type: 32 GB SIM,
  location: Test Location,
  approval_status: In Progress,
  critical_asset: false
)
```

