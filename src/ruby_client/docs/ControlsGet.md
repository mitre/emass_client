# EmassClient::ControlsGet

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **system_id** | **Integer** | [Required] Unique system record identifier. | [optional] |
| **name** | **String** | [Read-only] Name of the system record. | [optional] |
| **acronym** | **String** | [Required] Acronym of the system record. | [optional] |
| **ccis** | **String** | [Read-only] Comma separated list of CCIs associated with the control. | [optional] |
| **is_inherited** | **Boolean** | [Read-only] Indicates whether a control is inherited. | [optional] |
| **modified_by_overlays** | **String** | [Read-only] List of overlays that affect the control. | [optional] |
| **included_status** | **String** | [Read-only] Indicates the manner by which a control was included in the system&#39;s categorization. | [optional] |
| **compliance_status** | **String** | [Read-only] Compliance of the control. | [optional] |
| **responsible_entities** | **String** | [Required] Include written description of Responsible Entities that are responsible for the Security Control. Character Limit &#x3D; 2,000. | [optional] |
| **implementation_status** | **String** | [Optional] Implementation Status of the Security Control for the information system. | [optional] |
| **common_control_provider** | **String** | [Conditional] Indicate the type of Common Control Provider for an “Inherited” Security Control. | [optional] |
| **na_justification** | **String** | [Conditional] Provide justification for Security Controls deemed Not Applicable to the system. | [optional] |
| **control_designation** | **String** | [Required] Control designations | [optional] |
| **estimated_completion_date** | **Integer** | [Required] Field is required for Implementation Plan. | [optional] |
| **implementation_narrative** | **String** | [Required] Includes security control comments. Character Limit &#x3D; 2,000. | [optional] |
| **slcm_criticality** | **String** | [Conditional] Criticality of Security Control regarding SLCM. Character Limit &#x3D; 2,000. | [optional] |
| **slcm_frequency** | **String** | [Conditional] SLCM frequency | [optional] |
| **slcm_method** | **String** | [Conditional] SLCM method utilized | [optional] |
| **slcm_reporting** | **String** | [Conditional] Method for reporting Security Control for SLCM. Character Limit &#x3D; 2,000. | [optional] |
| **slcm_tracking** | **String** | [Conditional] How Non-Compliant Security Controls will be tracked for SLCM. Character Limit &#x3D; 2,000. | [optional] |
| **slcm_comments** | **String** | [Conditional] Additional comments for Security Control regarding SLCM. Character Limit &#x3D; 4,000. | [optional] |
| **severity** | **String** | [Optional] Values include the following options (Very Low, Low, Moderate,High,Very High) | [optional] |
| **vulnerabilty_summary** | **String** | [Optional] Include vulnerability summary. Character Limit &#x3D; 2,000. | [optional] |
| **recommendations** | **String** | [Optional] Include recommendations. Character Limit &#x3D; 2,000. | [optional] |
| **relevance_of_threat** | **String** | [Optional] Values include the following options (Very Low, Low, Moderate,High,Very High) | [optional] |
| **likelihood** | **String** | [Optional] Values include the following options (Very Low, Low, Moderate,High,Very High) | [optional] |
| **impact** | **String** | [Optional] Values include the following options (Very Low, Low, Moderate,High,Very High) | [optional] |
| **impact_description** | **String** | [Optional] Include description of Security Control&#39;s impact. | [optional] |
| **residual_risk_level** | **String** | [Optional] Values include the following options (Very Low, Low, Moderate,High,Very High) | [optional] |
| **test_method** | **String** | [Optional] Identifies the assessment method / combination that will determine if the security requirements are implemented correctly. | [optional] |
| **mitigations** | **String** | [Optional] Identify any mitigations in place for the Non-Compliant Security Control&#39;s vulnerabilities. Character Limit &#x3D; 2,000. | [optional] |
| **application_layer** | **String** | [Optional] If the Financial Management (Navy) overlay is applied to the system, this field appears and can be populated. Character Limit &#x3D; 2,000. Navy only. | [optional] |
| **database_layer** | **String** | [Read-Only] Identify the primary computing environment for where the information system is deployed. Navy only. | [optional] |
| **operating_system_layer** | **String** | [Read-Only] Identify the primary computing environment for where the information system is deployed. Navy only. | [optional] |

## Example

```ruby
require 'emass_client'

instance = EmassClient::ControlsGet.new(
  system_id: 35,
  name: System XYZ,
  acronym: AC-3,
  ccis: 000001,000002,
  is_inherited: true,
  modified_by_overlays: Requirements,
  included_status: Manually,
  compliance_status: Status,
  responsible_entities: Unknown,
  implementation_status: Planned,
  common_control_provider: DoD,
  na_justification: System EOL within 120 days,
  control_designation: Common,
  estimated_completion_date: 1638741660,
  implementation_narrative: Test Imp. Narrative,
  slcm_criticality: Test Criticality,
  slcm_frequency: Annually,
  slcm_method: Automated,
  slcm_reporting: Test Reporting,
  slcm_tracking: Test Tracking,
  slcm_comments: Test SLCM Comments,
  severity: Low,
  vulnerabilty_summary: Test Vulnerability Summary,
  recommendations: Test Recommendations,
  relevance_of_threat: Low,
  likelihood: Low,
  impact: Low,
  impact_description: Impact text,
  residual_risk_level: Low,
  test_method: Test,
  mitigations: Test Mitigations,
  application_layer: Cloud Computing,
  database_layer: Time Sharing Computing,
  operating_system_layer: Time Sharing Computing
)
```

