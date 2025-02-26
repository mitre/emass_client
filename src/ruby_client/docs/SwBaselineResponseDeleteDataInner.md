# EmassClient::SwBaselineResponseDeleteDataInner

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **system_id** | **Integer** |  | [optional] |
| **software_id** | **String** |  | [optional] |
| **success** | **Boolean** |  | [optional] |
| **errors** | **Array&lt;Object&gt;** |  | [optional] |

## Example

```ruby
require 'emass_client'

instance = EmassClient::SwBaselineResponseDeleteDataInner.new(
  system_id: 85,
  software_id: 171fc7d0-6957-4f54-bd51-3b7cbc6c39d5,
  success: true,
  errors: null
)
```

