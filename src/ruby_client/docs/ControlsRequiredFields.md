# EmassClient::ControlsRequiredFields

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **acronym** | **String** | [Required] Acronym of the system record. | [optional] |
| **responsible_entities** | **String** | [Required] Include written description of Responsible Entities that are responsible for the Security Control. Character Limit 2,000. | [optional] |
| **control_designation** | **String** | [Required] Control designations | [optional] |
| **estimated_completion_date** | **Integer** | [Required] Field is required for Implementation Plan. Unix time format. | [optional] |
| **implementation_narrative** | **String** | [Required] Includes security control comments. Character Limit 2,000. | [optional] |

## Example

```ruby
require 'emass_client'

instance = EmassClient::ControlsRequiredFields.new(
  acronym: AC-3,
  responsible_entities: Unknown,
  control_designation: Common,
  estimated_completion_date: 1799644800,
  implementation_narrative: Test Imp. Narrative
)
```

