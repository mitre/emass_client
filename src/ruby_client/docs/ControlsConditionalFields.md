# EmassClient::ControlsConditionalFields

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **common_control_provider** | **String** | [Conditional] Indicate the type of Common Control Provider for an Inherited Security Control. | [optional] |
| **na_justification** | **String** | [Conditional] Provide justification for Security Controls deemed Not Applicable to the system. | [optional] |
| **slcm_criticality** | **String** | [Conditional] Criticality of Security Control regarding SLCM. Character Limit &#x3D; 2,000. | [optional] |
| **slcm_frequency** | **String** | [Conditional] SLCM frequency | [optional] |
| **slcm_method** | **String** | [Conditional] SLCM method utilized | [optional] |
| **slcm_reporting** | **String** | [Conditional] Method for reporting Security Control for SLCM. Character Limit &#x3D; 2,000. | [optional] |
| **slcm_tracking** | **String** | [Conditional] How Non-Compliant Security Controls will be tracked for SLCM. Character Limit &#x3D; 2,000. | [optional] |
| **slcm_comments** | **String** | [Conditional] Additional comments for Security Control regarding SLCM. Character Limit &#x3D; 4,000. | [optional] |

## Example

```ruby
require 'emass_client'

instance = EmassClient::ControlsConditionalFields.new(
  common_control_provider: DoD,
  na_justification: System EOL within 120 days,
  slcm_criticality: Test Criticality,
  slcm_frequency: Annually,
  slcm_method: Automated,
  slcm_reporting: Test Reporting,
  slcm_tracking: Test Tracking,
  slcm_comments: Test SLCM Comments
)
```

