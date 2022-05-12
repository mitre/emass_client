# EmassClient::Roles

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **role_category** | **String** | [Required] System role categories | [optional] |
| **role** | **String** | [Required] System role description | [optional] |
| **users** | [**Array&lt;Users&gt;**](Users.md) |  | [optional] |

## Example

```ruby
require 'emass_client'

instance = EmassClient::Roles.new(
  role_category: PAC,
  role: AO,
  users: null
)
```

