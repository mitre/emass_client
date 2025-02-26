# EmassClient::ArtifactsOptionalFields

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
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

instance = EmassClient::ArtifactsOptionalFields.new(
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

