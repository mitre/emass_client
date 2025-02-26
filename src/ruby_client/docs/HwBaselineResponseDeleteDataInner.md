# EmassClient::HwBaselineResponseDeleteDataInner

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **system_id** | **Integer** |  | [optional] |
| **hardware_id** | **String** |  | [optional] |
| **success** | **Boolean** |  | [optional] |
| **errors** | **Array&lt;Object&gt;** |  | [optional] |

## Example

```ruby
require 'emass_client'

instance = EmassClient::HwBaselineResponseDeleteDataInner.new(
  system_id: 75,
  hardware_id: 0da80542-daa0-4170-85ce-551bcaf4be15,
  success: true,
  errors: null
)
```

