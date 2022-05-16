# EmassClient::PoamPostPutDel

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **system_id** | **Integer** | The system identifier for the system being updated. | [optional] |
| **poam_id** | **Integer** | The newly created POAM identifier | [optional] |
| **external_uid** | **String** | The unique identifier external to the eMASS application for use with associating POA&amp;Ms. 100 Characters. | [optional] |
| **success** | **Boolean** | Indicates if operations result (success/fail) | [optional] |
| **errors** | **Array&lt;Object&gt;** |  | [optional] |

## Example

```ruby
require 'emass_client'

instance = EmassClient::PoamPostPutDel.new(
  system_id: 33,
  poam_id: 45,
  external_uid: d6d98b88-c866-4496-9bd4-de7ba48d0f52,
  success: true,
  errors: null
)
```

