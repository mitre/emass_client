# EmassClient::NotFound

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **code** | **Integer** |  | [optional][default to 404] |
| **error_message** | **String** |  | [optional][default to &#39;Request has failed because the URL provided in the request did not match any available endpoint locations&#39;] |

## Example

```ruby
require 'emass_client'

instance = EmassClient::NotFound.new(
  code: null,
  error_message: null
)
```

