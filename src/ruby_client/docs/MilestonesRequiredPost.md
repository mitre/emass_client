# EmassClient::MilestonesRequiredPost

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **description** | **String** | [Required] Include milestone description. |  |
| **scheduled_completion_date** | **Integer** | [Required] Required for ongoing and completed POA&amp;M items. Unix time format. |  |

## Example

```ruby
require 'emass_client'

instance = EmassClient::MilestonesRequiredPost.new(
  description: Description text,
  scheduled_completion_date: 1599644800
)
```

