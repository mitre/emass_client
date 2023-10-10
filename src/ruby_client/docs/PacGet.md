# EmassClient::PacGet

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **workflow** | **String** | [Required] Values include the following:(Assess and Authorize, Assess Only, Security Plan Approval) | [optional] |
| **name** | **String** | [Required] Package name. 100 Characters. | [optional] |
| **current_stage_name** | **String** | [Read-Only] Name of the current stage in the active workflow. | [optional] |
| **current_stage** | **Integer** | [Read-Only] Number of the current stage in the active workflow. | [optional] |
| **total_stages** | **Integer** | [Read-Only] Total number of stages in the active workflow. | [optional] |
| **days_at_current_stage** | **Integer** | [Read-Only] Indicates the number of days at current workflow stage. | [optional] |

## Example

```ruby
require 'emass_client'

instance = EmassClient::PacGet.new(
  workflow: Assess and Authorize,
  name: Package name text,
  current_stage_name: SCA-R,
  current_stage: 4,
  total_stages: 6,
  days_at_current_stage: 2
)
```

