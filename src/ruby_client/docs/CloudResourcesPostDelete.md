# EmassClient::CloudResourcesPostDelete

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **resource_id** | **String** | [Required] Unique identifier/resource namespace for policy compliance result | [optional] |
| **success** | **Boolean** |  | [optional] |
| **system_id** | **Integer** |  | [optional] |
| **errors** | **Array&lt;Object&gt;** |  | [optional] |

## Example

```ruby
require 'emass_client'

instance = EmassClient::CloudResourcesPostDelete.new(
  resource_id: /subscriptions/123456789/sample/resource/namespace/default,
  success: true,
  system_id: 35,
  errors: null
)
```

