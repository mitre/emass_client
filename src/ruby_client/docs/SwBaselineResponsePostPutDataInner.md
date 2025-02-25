# EmassClient::SwBaselineResponsePostPutDataInner

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

instance = EmassClient::SwBaselineResponsePostPutDataInner.new(
  system_id: 85,
  software_id: 0bcaba59-a4f4-4918-a267-aedee3ea750d,
  success: true,
  errors: null
)
```

