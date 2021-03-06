# EmassClient::ArtifactsGet

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **system_id** | **Integer** | [Required] Unique eMASS system identifier. | [optional] |
| **filename** | **String** | [Required] File name should match exactly one file within the provided zip file. 1000 Characters. | [optional] |
| **is_inherited** | **Boolean** | [Read-only] Indicates whether an artifact is inherited. | [optional] |
| **is_template** | **Boolean** | [Required] Indicates whether an artifact template. | [optional] |
| **type** | **String** | [Required] Artifact type options | [optional] |
| **category** | **String** | [Required] Artifact category options | [optional] |
| **description** | **String** | [Optional] Artifact description. 2000 Characters. | [optional] |
| **ref_page_number** | **String** | [Optional] Artifact reference page number. 50 Characters. | [optional] |
| **ccis** | **String** | [Optional] CCI associated with test result. | [optional] |
| **controls** | **String** | [Optional] Control acronym associated with the artifact. NIST SP 800-53 Revision 4 defined. | [optional] |
| **mime_content_type** | **String** | [Read-Only] Standard MIME content type derived from file extension. | [optional] |
| **file_size** | **String** | [Read-Only] File size of attached artifact. | [optional] |
| **artifact_expiration_date** | **Integer** | [Optional] Date Artifact expires and requires review. In Unix Date format. | [optional] |
| **last_reviewed_date** | **Integer** | [Conditional] Date Artifact was last reviewed.. Unix time format. | [optional] |

## Example

```ruby
require 'emass_client'

instance = EmassClient::ArtifactsGet.new(
  system_id: 35,
  filename: AutorizationGuidance.pdf,
  is_inherited: true,
  is_template: false,
  type: Policy,
  category: Change Request,
  description: Artifact description text,
  ref_page_number: Reference page number,
  ccis: 000001,000002,
  controls: AC-8,AC-2(4),
  mime_content_type: application/zip,
  file_size: 4MB,
  artifact_expiration_date: 1549036926,
  last_reviewed_date: 1549036928
)
```

