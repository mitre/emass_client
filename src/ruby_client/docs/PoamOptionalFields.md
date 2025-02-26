# EmassClient::PoamOptionalFields

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **external_uid** | **String** | [Optional] Unique identifier external to the eMASS application for use with associating POA&amp;Ms. 100 Characters. | [optional] |
| **control_acronym** | **String** | [Optional] Control acronym associated with the POA&amp;M Item. NIST SP 800-53 Revision 4 defined. | [optional] |
| **assessment_procedure** | **String** | [Optional] The Security Control Assessment Procedure being associated with the POA&amp;M Item. | [optional] |
| **security_checks** | **String** | [Optional] Security Checks that are associated with the POA&amp;M. | [optional] |
| **raw_severity** | **String** | [Optional] Scan vulnerability ratting Values include the following options: (Very Low, Low, Moderate,High,Very High) | [optional] |
| **relevance_of_threat** | **String** | [Optional] Values include the following options (Very Low, Low, Moderate,High,Very High) | [optional] |
| **likelihood** | **String** | [Optional] Values include the following options (Very Low, Low, Moderate,High,Very High) | [optional] |
| **impact** | **String** | [Optional] Values include the following options (Very Low, Low, Moderate,High,Very High) | [optional] |
| **impact_description** | **String** | [Optional] Include description of Security Control&#39;s impact. | [optional] |
| **residual_risk_level** | **String** | [Optional] Values include the following options (Very Low, Low, Moderate,High,Very High) | [optional] |
| **recommendations** | **String** | [Optional] Include recommendations. Character Limit &#x3D; 2,000. | [optional] |
| **mitigations** | **String** | [Optional] Include mitigation explanation. 2000 Characters. | [optional] |
| **resulting_residual_risk_level_after_proposed_mitigations** | **String** | [Optional] Indicate the risk level expected after any proposed mitigations are implemented. Proposed mitigations should be appropriately documented as POA&amp;M milestones. Navy only. | [optional] |
| **predisposing_conditions** | **String** | [Optional] A predisposing condition is a condition existing within an organization, a mission or business process, enterprise architecture, information system/PIT, or environment of operation, which affects (i.e., increases or decreases) the likelihood that threat events, once initiated, result in adverse impacts. Navy only. | [optional] |
| **threat_description** | **String** | [Optional] Describe the identified threat(s) and relevance to the information system. Navy only. | [optional] |
| **devices_affected** | **String** | [Optional] List any affected devices by hostname. If all devices in the information system are affected, state &#39;system&#39; or &#39;all&#39;. Navy only | [optional] |

## Example

```ruby
require 'emass_client'

instance = EmassClient::PoamOptionalFields.new(
  external_uid: d6d98b88-c866-4496-9bd4-de7ba48d0f52,
  control_acronym: AC-3,
  assessment_procedure: AC-1.4,
  security_checks: SV-25123r1_rule,2016-A-0279,
  raw_severity: Moderate,
  relevance_of_threat: Low,
  likelihood: Low,
  impact: Low,
  impact_description: Impact text,
  residual_risk_level: Low,
  recommendations: Recommendations text,
  mitigations: Mitigation text,
  resulting_residual_risk_level_after_proposed_mitigations: Low,
  predisposing_conditions: The predisposing condition justification,
  threat_description: The identified threat(s) description,
  devices_affected: system
)
```

