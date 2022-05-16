# EmassClient::Response490Meta

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **code** | **Integer** |  | [optional][default to 490] |
| **error_message** | **String** |  | [optional][default to &#39;Request has failed because too much data was requested in a single batch. This error is specific to eMASS&#39;] |

## Example

```ruby
require 'emass_client'

instance = EmassClient::Response490Meta.new(
  code: null,
  error_message: null
)
```

