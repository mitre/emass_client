# EmassClient::PacGet

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **system_id** | **Integer** | [Required] Unique eMASS system identifier. | [optional] |
| **workflow** | **String** | [Required] Values include the following:(Assess and Authorize, Assess Only, Security Plan Approval) | [optional] |
| **name** | **String** | [Required] Package name. 100 Characters. | [optional] |
| **current_stage_name** | **String** | [Read-Only] Name of the current stage in the active workflow. | [optional] |
| **current_stage** | **Integer** | [Read-Only] Number of the current stage in the active workflow. | [optional] |
| **total_stages** | **Integer** | [Read-Only] Total number of stages in the active workflow. | [optional] |
| **days_at_current_stage** | **Integer** | [Read-Only] Indicates the number of days at current workflow stage. | [optional] |
| **comments** | **String** | [Required] Comments related to package approval chain. Character Limit &#x3D; 4,000. | [optional] |

## Example

```ruby
require 'emass_client'

instance = EmassClient::PacGet.new(
  system_id: 35,
  workflow: Assess and Authorize,
  name: Package name text,
  current_stage_name: SCA-R,
  current_stage: 4,
  total_stages: 6,
  days_at_current_stage: 2,
  comments: Comments text.
)
```

