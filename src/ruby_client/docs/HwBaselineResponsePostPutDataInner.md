# EmassClient::HwBaselineResponsePostPutDataInner

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

instance = EmassClient::HwBaselineResponsePostPutDataInner.new(
  system_id: 75,
  hardware_id: 0bcaba59-a4f4-4918-a267-aedee3ea750d,
  success: true,
  errors: null
)
```

