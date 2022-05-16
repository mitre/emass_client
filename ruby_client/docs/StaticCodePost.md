# EmassClient::StaticCodePost

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **application_name** | **String** | [Required] Name of the software application that was assessed. | [optional] |
| **version** | **String** | [Required] The version of the application. | [optional] |
| **success** | **Boolean** |  | [optional] |
| **system_id** | **Integer** |  | [optional] |
| **errors** | **Array&lt;Object&gt;** |  | [optional] |

## Example

```ruby
require 'emass_client'

instance = EmassClient::StaticCodePost.new(
  application_name: Artemis,
  version: Version 5.0,
  success: true,
  system_id: 35,
  errors: null
)
```

