# EmassClient::ContainersResourcesPost

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **container_id** | **String** | [Required] Unique identifier of the container | [optional] |
| **success** | **Boolean** |  | [optional] |
| **system_id** | **Integer** |  | [optional] |
| **errors** | **Array&lt;Object&gt;** |  | [optional] |

## Example

```ruby
require 'emass_client'

instance = EmassClient::ContainersResourcesPost.new(
  container_id: command-control,
  success: true,
  system_id: 35,
  errors: null
)
```

