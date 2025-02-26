# EmassClient::PoamIds

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **system_id** | **Integer** | [Required] Unique eMASS system identifier. | [optional] |
| **poam_id** | **Integer** | [Required] Unique item identifier | [optional] |
| **display_poam_id** | **Integer** | [Required] Globally unique identifier for individual POA&amp;M Items, seen on the front-end as ID. | [optional] |

## Example

```ruby
require 'emass_client'

instance = EmassClient::PoamIds.new(
  system_id: 830,
  poam_id: 45,
  display_poam_id: 100000010
)
```

