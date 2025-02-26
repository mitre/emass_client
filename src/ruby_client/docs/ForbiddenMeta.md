# EmassClient::ForbiddenMeta

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **code** | **Integer** |  | [optional][default to 403] |
| **error_message** | **String** |  | [optional][default to &#39;Request was blocked by the application due to a lack of client permissions to the API or to a specific endpoint&#39;] |

## Example

```ruby
require 'emass_client'

instance = EmassClient::ForbiddenMeta.new(
  code: null,
  error_message: null
)
```

