# EmassClient::MilestonesPutPostDelete

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **system_id** | **Integer** | The system identifier that the POAM was added. | [optional] |
| **poam_id** | **Integer** | The newly created POAM identifier | [optional] |
| **milestone_id** | **Integer** | The Milestone unique item identifier | [optional] |
| **external_uid** | **String** | The unique identifier external to the eMASS application for use with associating POA&amp;Ms. 100 Characters. | [optional] |
| **success** | **Boolean** | Indicates if operations result (success/fail) | [optional] |
| **errors** | **Array&lt;Object&gt;** |  | [optional] |

## Example

```ruby
require 'emass_client'

instance = EmassClient::MilestonesPutPostDelete.new(
  system_id: 35,
  poam_id: 45,
  milestone_id: 77,
  external_uid: d6d98b88-c866-4496-9bd4-de7ba48d0f52,
  success: true,
  errors: null
)
```

