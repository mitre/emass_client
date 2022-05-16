# EmassClient::ControlsPut

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **acronym** | **String** | Acronym of the system record. | [optional] |
| **success** | **Boolean** | Indicates if operations result (success/fail) | [optional] |
| **system_id** | **Integer** | The system identifier for the system being updated. | [optional] |
| **errors** | **Array&lt;Object&gt;** |  | [optional] |

## Example

```ruby
require 'emass_client'

instance = EmassClient::ControlsPut.new(
  acronym: AC-34,
  success: true,
  system_id: 33,
  errors: null
)
```

