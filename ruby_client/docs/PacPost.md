# EmassClient::PacPost

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **workflow** | **String** | [Required] Values include the following:(Assess and Authorize, Assess Only, Security Plan Approval) | [optional] |
| **success** | **Boolean** |  | [optional] |
| **system_id** | **Integer** |  | [optional] |
| **errors** | **Array&lt;Object&gt;** |  | [optional] |

## Example

```ruby
require 'emass_client'

instance = EmassClient::PacPost.new(
  workflow: Assess and Authorize,
  success: true,
  system_id: 35,
  errors: null
)
```

