# EmassClient::ConnectivityCcsd

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ccsd_number** | **String** | [Read-Only] Identifier for specific connections to the system. | [optional] |
| **connectivity** | **String** | [Read-Only] Choose connection type for the system. | [optional] |

## Example

```ruby
require 'emass_client'

instance = EmassClient::ConnectivityCcsd.new(
  ccsd_number: CCSD-579,
  connectivity: Not Yet Authorized
)
```

