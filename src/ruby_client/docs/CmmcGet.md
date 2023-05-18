# EmassClient::CmmcGet

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **operation** | **String** | [Read-Only] Indicates the action that should be taken on the assessment record since the provided sinceDate. | [optional] |
| **hq_organization_name** | **String** | [Read-Only] The name of the DIB Company. | [optional] |
| **uei** | **String** | [Read-Only] The Unique Entity Identifier assigned to the DIB Company. | [optional] |
| **cage_codes_in_scope** | **String** | [Read-Only] The five position code(s) associated with the Organization Seeking Certification (OSC). | [optional] |
| **osc_name** | **String** | [Read-Only] The name of the Organization Seeking Certification. | [optional] |
| **scope** | **String** | [Read-Only] The scope of the OSC assessment. | [optional] |
| **scope_description** | **String** | [Read-Only] Brief description of the scope of the OSC assessment | [optional] |
| **awarded_cmmc_level** | **String** | [Read-Only] The CMMC award level. | [optional] |
| **expiration_date** | **Integer** | [Read-Only] Expiration date of the awarded CMMC certification. | [optional] |
| **assessment_id** | **String** | [Read-Only] Unique identifier for the assessment/certificate. | [optional] |
| **model_version** | **String** | [Read-Only] Version of the CMMC Model used as part of the assessment. | [optional] |
| **highest_level_cage_code** | **String** | [Read-Only] Identifies the highest-level CAGE Code associated with a given organization. | [optional] |
| **certification_unique_id** | **String** | [Read-Only] Identifies the unique ID that is associated with a given CMMC certification for an organization. | [optional] |
| **poam** | **Boolean** | [Read-Only] Identifies whether any security requirements received a POA&amp;M during the assessment. | [optional] |
| **overall_score** | **Integer** | [Read-Only] Identifies the overall calculated score for the assessment based on the assigned values to each applicable security requirement. | [optional] |
| **osc_assessment_official_last_name** | **String** | [Read-Only] Last name of the company official contracting with the C3PAO for the assessment. | [optional] |
| **osc_assessment_official_first_name** | **String** | [Read-Only] First name of the company official contracting with the C3PAO for the assessment. | [optional] |
| **osc_assessment_official_email** | **String** | [Read-Only] Email of the company official contracting with the C3PAO for the assessment. | [optional] |
| **osc_assessment_official_title** | **String** | [Read-Only] Title of the company official contracting with the C3PAO for the assessment. | [optional] |
| **ssps** | [**Array&lt;Ssps&gt;**](Ssps.md) |  | [optional] |

## Example

```ruby
require 'emass_client'

instance = EmassClient::CmmcGet.new(
  operation: UPDATED,
  hq_organization_name: Army,
  uei: 9809123,
  cage_codes_in_scope: 89ED9; 99D8B,
  osc_name: UC Labs,
  scope: Enterprise,
  scope_description: Assessment of UC&#39;s Lab,
  awarded_cmmc_level: Not Certified,
  expiration_date: 1638741660,
  assessment_id: 41b89528-a7a8-470a-90f4-c3fd1267d6f7,
  model_version: 1.12,
  highest_level_cage_code: 99D8B,
  certification_unique_id: L20000003,
  poam: false,
  overall_score: 110,
  osc_assessment_official_last_name: Smith,
  osc_assessment_official_first_name: John,
  osc_assessment_official_email: john.smith6.ctr@mail.mil,
  osc_assessment_official_title: The Boss,
  ssps: null
)
```

