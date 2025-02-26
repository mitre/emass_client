# EmassClient::SwBaselineReadOnlyFields

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **software_id** | **String** | [Read-Only] GUID identifying the specific software asset. | [optional] |

## Example

```ruby
require 'emass_client'

instance = EmassClient::SwBaselineReadOnlyFields.new(
  software_id: 171fc7d0-6957-4f54-bd51-3b7cbc6c39d5
)
```

