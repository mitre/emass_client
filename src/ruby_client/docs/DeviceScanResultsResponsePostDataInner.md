# EmassClient::DeviceScanResultsResponsePostDataInner

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **filename** | **String** | [Required] single binary file. Specific file extensions are expected depending upon the scanType parameter. | [optional] |
| **assets_imported** | **Integer** | Number of assets imported from the scan file. | [optional] |
| **success** | **Boolean** |  | [optional] |
| **system_id** | **Integer** |  | [optional] |
| **errors** | **Array&lt;Object&gt;** |  | [optional] |

## Example

```ruby
require 'emass_client'

instance = EmassClient::DeviceScanResultsResponsePostDataInner.new(
  filename: MySystemEntityScan.ckl,
  assets_imported: 1,
  success: true,
  system_id: 35,
  errors: null
)
```

