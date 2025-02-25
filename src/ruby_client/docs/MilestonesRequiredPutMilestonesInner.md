# EmassClient::MilestonesRequiredPutMilestonesInner

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **description** | **String** | [Required] Include milestone description. |  |
| **scheduled_completion_date** | **Integer** | [Required] Required for ongoing and completed POA&amp;M items. Unix time format. |  |
| **is_active** | **Boolean** | [Conditional] Optionally used in PUT to delete milestones when updating a POA&amp;M. |  |

## Example

```ruby
require 'emass_client'

instance = EmassClient::MilestonesRequiredPutMilestonesInner.new(
  description: Description text,
  scheduled_completion_date: 1599644800,
  is_active: true
)
```

