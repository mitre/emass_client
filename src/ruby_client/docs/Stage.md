# EmassClient::Stage

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **name** | **String** | [Read-Only] Name of the stage. For older workflows, this will match the user assigned to the stage. | [optional] |
| **transitions** | [**Array&lt;DefinitionTransitions&gt;**](DefinitionTransitions.md) |  | [optional] |

## Example

```ruby
require 'emass_client'

instance = EmassClient::Stage.new(
  name: Not Started,
  transitions: null
)
```

