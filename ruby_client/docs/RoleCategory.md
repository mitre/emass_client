# EmassClient::RoleCategory

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **system_id** | **Integer** | [Read-only] Unique system record identifier. | [optional] |
| **system_name** | **String** | [Read-only] Name of the system record. | [optional] |
| **system_acronym** | **String** | [Read-only] Acronym of the system record. | [optional] |
| **roles** | [**Array&lt;Roles&gt;**](Roles.md) |  | [optional] |

## Example

```ruby
require 'emass_client'

instance = EmassClient::RoleCategory.new(
  system_id: 35,
  system_name: eMASS API Example System,
  system_acronym: S-XYZ,
  roles: null
)
```

