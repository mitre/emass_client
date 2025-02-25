# EmassClient::ArtifactsReadOnlyFields

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **is_inherited** | **Boolean** | [Read-only] Indicates whether an artifact is inherited. | [optional] |
| **ccis** | **String** | [Read-Only] CCI mapping for Assessment Procedures associated with the artifact. | [optional] |
| **mime_content_type** | **String** | [Read-Only] Standard MIME content type derived from file extension. | [optional] |
| **file_size** | **String** | [Read-Only] File size of attached artifact. | [optional] |

## Example

```ruby
require 'emass_client'

instance = EmassClient::ArtifactsReadOnlyFields.new(
  is_inherited: true,
  ccis: 000001,000002,
  mime_content_type: application/zip,
  file_size: 4MB
)
```

