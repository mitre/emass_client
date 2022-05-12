# EmassClient::TestResultsPost

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **cci** | **String** | CCI associated with test result. | [optional] |
| **success** | **Boolean** | Indicates if operations result (success/fail) | [optional] |
| **system_id** | **Integer** | The system identifier for the system being updated. | [optional] |
| **errors** | **Array&lt;Object&gt;** |  | [optional] |

## Example

```ruby
require 'emass_client'

instance = EmassClient::TestResultsPost.new(
  cci: 000001,000002,
  success: true,
  system_id: 35,
  errors: null
)
```

