# EmassClient::HwBaselineConditionalFields

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **public_facing_fqdn** | **String** | [Conditional] Public facing FQDN. Only applicable if Public Facing is set to true. | [optional] |
| **public_facing_ip_address** | **String** | [Conditional] Public facing IP address. Only applicable if Public Facing is set to true. | [optional] |
| **public_facing_urls** | **String** | [Conditional] Public facing URLs. Only applicable if Public Facing is set to true. | [optional] |

## Example

```ruby
require 'emass_client'

instance = EmassClient::HwBaselineConditionalFields.new(
  public_facing_fqdn: test.com,
  public_facing_ip_address: 12.68.239.44,
  public_facing_urls: test.com
)
```

