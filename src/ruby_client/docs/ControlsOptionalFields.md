# EmassClient::ControlsOptionalFields

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **implementation_status** | **String** | [Optional] Implementation Status of the Security Control for the information system. | [optional] |
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
| **database_layer** | **String** | [Optional] If the Financial Management (Navy) overlay is applied to the system, this field appears and can be populated. Navy only. | [optional] |
| **operating_system_layer** | **String** | [Optional] If the Financial Management (Navy) overlay is applied to the system, this field appears and can be populated. Navy only. | [optional] |

## Example

```ruby
require 'emass_client'

instance = EmassClient::ControlsOptionalFields.new(
  implementation_status: Planned,
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
  operating_system_layer: Client Server Computing
)
```

