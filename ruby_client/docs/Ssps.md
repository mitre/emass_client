# EmassClient::Ssps

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ssp_name** | **String** | [Read-Only] Name of the System Security Plan. | [optional] |
| **ssp_version** | **String** | [Read-Only] Version of the System Security Plan. | [optional] |
| **ssp_date** | **Integer** | [Read-Only] Date of the System Security Plan. Unix date format. | [optional] |

## Example

```ruby
require 'emass_client'

instance = EmassClient::Ssps.new(
  ssp_name: UC Lab,
  ssp_version: 4.3.0,
  ssp_date: 1638741660
)
```

