# EmassClient::Users

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **first_name** | **String** |  | [optional] |
| **last_name** | **String** |  | [optional] |
| **email** | **String** |  | [optional] |

## Example

```ruby
require 'emass_client'

instance = EmassClient::Users.new(
  first_name: John,
  last_name: Smith,
  email: John.Smith@hb.com
)
```

