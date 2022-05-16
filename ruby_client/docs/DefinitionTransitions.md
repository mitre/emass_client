# EmassClient::DefinitionTransitions

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **end_stage** | **String** | [Read-Only] The landing stage that is active after performing a transition. | [optional] |
| **description** | **String** | [Read-Only] Description that matches the action dropdown that appears for PAC users. | [optional] |
| **roles** | **Array&lt;Object&gt;** |  | [optional] |

## Example

```ruby
require 'emass_client'

instance = EmassClient::DefinitionTransitions.new(
  end_stage: Submit Categorization,
  description: Initiate Workflow,
  roles: null
)
```

