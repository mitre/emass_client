# EmassClient::Response401Meta

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **code** | **Integer** |  | [optional][default to 401] |
| **error_message** | **String** |  | [optional][default to &#39;Request has failed to provide suitable authentication from the client&#39;] |

## Example

```ruby
require 'emass_client'

instance = EmassClient::Response401Meta.new(
  code: null,
  error_message: null
)
```

