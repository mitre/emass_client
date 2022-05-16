# EmassClient::MilestonesRequiredPut

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **milestone_id** | **Integer** | [Required] Unique item identifier |  |
| **description** | **String** | [Required] Include milestone description. |  |
| **scheduled_completion_date** | **Integer** | [Required] Shecdule completion date. Unix time format. |  |

## Example

```ruby
require 'emass_client'

instance = EmassClient::MilestonesRequiredPut.new(
  milestone_id: 19,
  description: Description text,
  scheduled_completion_date: 1599644800
)
```

