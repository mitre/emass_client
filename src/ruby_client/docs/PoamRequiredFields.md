# EmassClient::PoamRequiredFields

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **status** | **String** | [Required] The POA&amp;M status | [optional] |
| **vulnerability_description** | **String** | [Required] Provide a description of the POA&amp;M Item. 2000 Characters. | [optional] |
| **source_identifying_vulnerability** | **String** | [Required] Include Source Identifying Vulnerability text. 2000 Characters. | [optional] |
| **poc_organization** | **String** | [Required] Organization/Office represented. 100 Characters. | [optional] |
| **resources** | **String** | [Required] List of resources used. 250 Characters. | [optional] |
| **identified_in_cfo_audit_or_other_review** | **Boolean** | [Required] If not specified, this field will be set to false because it does not accept a null value. VA only | [optional] |

## Example

```ruby
require 'emass_client'

instance = EmassClient::PoamRequiredFields.new(
  status: Completed,
  vulnerability_description: Description text,
  source_identifying_vulnerability: Source Indentifying Vulnerability text,
  poc_organization: Army,
  resources: Resource text,
  identified_in_cfo_audit_or_other_review: true
)
```

