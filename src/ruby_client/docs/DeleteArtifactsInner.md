# EmassClient::DeleteArtifactsInner

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **filename** | **String** | [Required] File name should match exactly one file within the provided zip file. 1000 Characters. | [optional] |

## Example

```ruby
require 'emass_client'

instance = EmassClient::DeleteArtifactsInner.new(
  filename: AutorizationGuidance.pdf
)
```

