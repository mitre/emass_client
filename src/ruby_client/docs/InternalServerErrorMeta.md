# EmassClient::InternalServerErrorMeta

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **code** | **Integer** |  | [optional][default to 500] |
| **error_message** | **String** |  | [optional][default to &#39;Server encountered an unexpected condition which prevented it from fulfilling the request&#39;] |

## Example

```ruby
require 'emass_client'

instance = EmassClient::InternalServerErrorMeta.new(
  code: null,
  error_message: null
)
```

