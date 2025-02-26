# EmassClient::ArtifactsResponseGetDataInner

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **system_id** | **Integer** | [Required] Unique eMASS system identifier. | [optional] |
| **filename** | **String** | [Required] File name should match exactly one file within the provided zip file. 1000 Characters. or Application/zip file. Max 30MB per artifact.  | [optional] |
| **is_template** | **Boolean** | [Required] Indicates whether an artifact template. | [optional] |
| **type** | **String** | [Required] Artifact type options | [optional] |
| **category** | **String** | [Required] Artifact category options | [optional] |
| **is_inherited** | **Boolean** | [Read-only] Indicates whether an artifact is inherited. | [optional] |
| **ccis** | **String** | [Read-Only] CCI mapping for Assessment Procedures associated with the artifact. | [optional] |
| **mime_content_type** | **String** | [Read-Only] Standard MIME content type derived from file extension. | [optional] |
| **file_size** | **String** | [Read-Only] File size of attached artifact. | [optional] |
| **name** | **String** | [Optional] Artifact name. Character Limit &#x3D; 100. | [optional] |
| **description** | **String** | [Optional] Artifact description. 10,000 Characters. | [optional] |
| **reference_page_number** | **String** | [Optional] Artifact reference page number. 50 Characters. | [optional] |
| **assessment_procedures** | **String** | [Optional] The Security Control Assessment Procedure being associated with the artifact. | [optional] |
| **controls** | **String** | [Optional] Control acronym associated with the artifact. NIST SP 800-53 Revision 4 defined. | [optional] |
| **expiration_date** | **Integer** | [Optional] Date Artifact expires and requires review. In Unix Date format. | [optional] |
| **last_reviewed_date** | **Integer** | [Optional] Date Artifact was last reviewed. Unix time format. | [optional] |
| **signed_date** | **Integer** | [Optional] Date artifact was signed. Unix time format. | [optional] |

## Example

```ruby
require 'emass_client'

instance = EmassClient::ArtifactsResponseGetDataInner.new(
  system_id: 35,
  filename: AutorizationGuidance.pdf,
  is_template: false,
  type: Policy,
  category: Change Request,
  is_inherited: true,
  ccis: 000001,000002,
  mime_content_type: application/zip,
  file_size: 4MB,
  name: E-Authentication Assessment,
  description: Artifact description text,
  reference_page_number: Reference page number,
  assessment_procedures: AC-1.1,
  controls: AC-8,AC-2(4),
  expiration_date: 18089586892,
  last_reviewed_date: 1757409188,
  signed_date: 1767409188
)
```

