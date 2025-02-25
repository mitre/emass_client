# EmassClient::SwBaselineRequiredFields

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **software_vendor** | **String** | [Required] Vendor of the software asset. | [optional] |
| **software_name** | **String** | [Required] Name of the software asset. | [optional] |
| **version** | **String** | [Required] Version of the software asset. | [optional] |

## Example

```ruby
require 'emass_client'

instance = EmassClient::SwBaselineRequiredFields.new(
  software_vendor: Test Vendor,
  software_name: Test Software Name 11,
  version: 1.0
)
```

