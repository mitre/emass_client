# EmassClient::Response405Meta

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **code** | **Integer** |  | [optional][default to 405] |
| **error_message** | **String** |  | [optional][default to &#39;Request was made with a verb (GET, POST, etc.) that is not permitted for the endpoint&#39;] |

## Example

```ruby
require 'emass_client'

instance = EmassClient::Response405Meta.new(
  code: null,
  error_message: null
)
```

