# EmassClient::BadRequestMeta

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **code** | **Integer** |  | [optional][default to 400] |
| **error_message** | **String** |  | [optional][default to &#39;Request could not be understood by the server due to incorrect syntax or an unexpected format&#39;] |

## Example

```ruby
require 'emass_client'

instance = EmassClient::BadRequestMeta.new(
  code: null,
  error_message: null
)
```

