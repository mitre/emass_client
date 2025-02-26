# EmassClient::CmmcGet

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **operation** | **String** | [Read-Only] Indicates the action that should be taken on the assessment record since the provided sinceDate. | [optional] |
| **hq_organization_name** | **String** | [Read-Only] The name of the DIB Company. | [optional] |
| **uei** | **String** | [Read-Only] The Unique Entity Identifier assigned to the DIB Company. | [optional] |
| **osc_name** | **String** | [Read-Only] The name of the Organization Seeking Certification. | [optional] |
| **highest_level_owner_cage_code** | **String** | [Read-Only] Identifies the highest-level CAGE Code associated with a given organization. | [optional] |
| **cage_codes_in_scope** | **String** | [Read-Only] The five position code(s) associated with the Organization Seeking Certification (OSC). | [optional] |
| **number_of_employees** | **Integer** | [Read-Only] The number of employees affiliated with the Organization Seeking Certification. | [optional] |
| **scope** | **String** | [Read-Only] The scope of the OSC assessment. | [optional] |
| **scope_description** | **String** | [Read-Only] Brief description of the scope of the OSC assessment | [optional] |
| **assessment_standard** | **String** | [Read-Only] Version of the CMMC Model used as part of the assessment. | [optional] |
| **assessment_id** | **String** | [Read-Only] Unique identifier for the assessment/certificate. | [optional] |
| **cmmc_uid** | **String** | [Read-Only] Identifies the unique ID that is associated with a given CMMC certification for an organization. | [optional] |
| **overall_score** | **Integer** | [Read-Only] Identifies the overall calculated score for the assessment based on the assigned values to each applicable security requirement. | [optional] |
| **cmmc_status** | **String** | [Read-Only] The status of the CMMC certification. | [optional] |
| **cmmc_status_date** | **Integer** | [Read-Only] Date of the CMMC status. | [optional] |
| **cmmc_status_expiration_date** | **Integer** | [Read-Only] Expiration date of the CMMC status. | [optional] |

## Example

```ruby
require 'emass_client'

instance = EmassClient::CmmcGet.new(
  operation: UPDATED,
  hq_organization_name: Army,
  uei: 9809123,
  osc_name: UC Labs,
  highest_level_owner_cage_code: 99D8B,
  cage_codes_in_scope: 89ED9; 99D8B,
  number_of_employees: 100,
  scope: Enterprise,
  scope_description: Assessment of UC&#39;s Lab,
  assessment_standard: NIST SP 800-171 Revision 2,
  assessment_id: 41b89528-a7a8-470a-90f4-c3fd1267d6f7,
  cmmc_uid: L20000003,
  overall_score: 110,
  cmmc_status: Conditional Level 2 (C3PAO),
  cmmc_status_date: 1715312304,
  cmmc_status_expiration_date: 1715312304
)
```

