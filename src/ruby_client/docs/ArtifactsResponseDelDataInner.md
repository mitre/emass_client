# EmassClient::ArtifactsResponseDelDataInner

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **filename** | **String** | [Required] File name should match exactly one file within the provided zip file. 1000 Characters. | [optional] |
| **success** | **Boolean** |  | [optional] |
| **system_id** | **Integer** |  | [optional] |

## Example

```ruby
require 'emass_client'

instance = EmassClient::ArtifactsResponseDelDataInner.new(
  filename: AutorizationGuidance.pdf,
  success: true,
  system_id: 35
)
```

