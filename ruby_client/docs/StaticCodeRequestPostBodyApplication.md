# EmassClient::StaticCodeRequestPostBodyApplication

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **application_name** | **String** | [Required] Name of the software application that was assessed. | [optional] |
| **version** | **String** | [Required] The version of the application. | [optional] |

## Example

```ruby
require 'emass_client'

instance = EmassClient::StaticCodeRequestPostBodyApplication.new(
  application_name: Artemis,
  version: Version 5.0
)
```

