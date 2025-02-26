# EmassClient::LengthRequiredMeta

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **code** | **Integer** |  | [optional][default to 411] |
| **error_message** | **String** |  | [optional][default to &#39;Request was of type POST and failed to provide the server information about the data/content length being submitted&#39;] |

## Example

```ruby
require 'emass_client'

instance = EmassClient::LengthRequiredMeta.new(
  code: null,
  error_message: null
)
```

