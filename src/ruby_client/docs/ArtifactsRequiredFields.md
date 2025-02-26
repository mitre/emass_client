# EmassClient::ArtifactsRequiredFields

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **filename** | **String** | [Required] File name should match exactly one file within the provided zip file. 1000 Characters. or Application/zip file. Max 30MB per artifact.  | [optional] |
| **is_template** | **Boolean** | [Required] Indicates whether an artifact template. | [optional] |
| **type** | **String** | [Required] Artifact type options | [optional] |
| **category** | **String** | [Required] Artifact category options | [optional] |

## Example

```ruby
require 'emass_client'

instance = EmassClient::ArtifactsRequiredFields.new(
  filename: AutorizationGuidance.pdf,
  is_template: false,
  type: Policy,
  category: Change Request
)
```

