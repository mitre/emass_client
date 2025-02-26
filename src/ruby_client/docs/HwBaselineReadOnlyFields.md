# EmassClient::HwBaselineReadOnlyFields

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **hardware_id** | **String** | [Read-Only] GUID identifying the specific hardware asset. Required for a PUT call. | [optional] |

## Example

```ruby
require 'emass_client'

instance = EmassClient::HwBaselineReadOnlyFields.new(
  hardware_id: 0bcaba59-a4f4-4918-a267-aedee3ea750d
)
```

