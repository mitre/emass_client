# EmassClient::ControlsReadOnlyFields

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **name** | **String** | [Read-only] Name of the system record. | [optional] |
| **ccis** | **String** | [Read-only] Comma separated list of CCIs associated with the control. | [optional] |
| **is_inherited** | **Boolean** | [Read-only] Indicates whether a control is inherited. | [optional] |
| **modified_by_overlays** | **String** | [Read-only] List of overlays that affect the control. | [optional] |
| **included_status** | **String** | [Read-only] Indicates the manner by which a control was included in the system&#39;s categorization. | [optional] |
| **compliance_status** | **String** | [Read-only] Compliance of the control. | [optional] |

## Example

```ruby
require 'emass_client'

instance = EmassClient::ControlsReadOnlyFields.new(
  name: System XYZ,
  ccis: 000001,000002,
  is_inherited: true,
  modified_by_overlays: Requirements,
  included_status: Manually,
  compliance_status: Status
)
```

