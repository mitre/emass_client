# EmassClient::CacResponsePostDataInner

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **control_acronym** | **String** | [Required] System acronym name. | [optional] |
| **success** | **Boolean** |  | [optional] |
| **system_id** | **Integer** |  | [optional] |
| **errors** | **Array&lt;Object&gt;** |  | [optional] |

## Example

```ruby
require 'emass_client'

instance = EmassClient::CacResponsePostDataInner.new(
  control_acronym: AC-3,
  success: true,
  system_id: 35,
  errors: null
)
```

