# EmassClient::InstanceTransitions

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **comments** | **String** | [Read-Only] Comments entered by the user when performing the transition. | [optional] |
| **created_by** | **String** | [Read-Only] User that performed the workflow transition. | [optional] |
| **created_date** | **Integer** | [Read-Only] Date the workflow instance or the workflow transition was created. | [optional] |
| **description** | **String** | [Read-Only] Description of the stage transition. This matches the action dropdown that appears for PAC users. | [optional] |
| **end_stage** | **String** | [Read-Only] The landing stage that is active after performing a transition. | [optional] |
| **start_stage** | **String** | [Read-Only] The beginning stage that is active before performing a transition. | [optional] |

## Example

```ruby
require 'emass_client'

instance = EmassClient::InstanceTransitions.new(
  comments: Approved the categorization,
  created_by: john.doe.ctr@mail.mil,
  created_date: 1636124623,
  description: Submit New Package,
  end_stage: Submit Categorization,
  start_stage: Not Started
)
```

