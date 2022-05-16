# EmassClient::MilestonesGet

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **system_id** | **Integer** | [Required] Unique eMASS system identifier. | [optional] |
| **milestone_id** | **Integer** | [Required] Unique item identifier | [optional] |
| **poam_id** | **Integer** | [Required] Unique item identifier | [optional] |
| **description** | **String** | [Required] Include milestone description. | [optional] |
| **scheduled_completion_date** | **Integer** | [Required] Required for ongoing and completed POA&amp;M items. Unix time format. | [optional] |
| **review_status** | **String** | [Read-Only] Values include the following options: (Not Approved,Under Review,Approved) | [optional] |

## Example

```ruby
require 'emass_client'

instance = EmassClient::MilestonesGet.new(
  system_id: 830,
  milestone_id: 19,
  poam_id: 45,
  description: Description text,
  scheduled_completion_date: 1599644800,
  review_status: Under Review
)
```

