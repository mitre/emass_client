# EmassClient::StaticCodeRequestPostBody

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **application** | [**StaticCodeRequestPostBodyApplication**](StaticCodeRequestPostBodyApplication.md) |  | [optional] |
| **application_findings** | [**Array&lt;StaticCodeApplicationPost&gt;**](StaticCodeApplicationPost.md) |  | [optional] |

## Example

```ruby
require 'emass_client'

instance = EmassClient::StaticCodeRequestPostBody.new(
  application: null,
  application_findings: null
)
```

