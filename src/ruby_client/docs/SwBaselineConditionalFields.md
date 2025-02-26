# EmassClient::SwBaselineConditionalFields

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **approval_date** | **Integer** | [Conditional] Approval date of the software asset. If Approval Status is set to \&quot;Unapproved\&quot; or \&quot;In Progress\&quot;, Approval Date will be set to null. | [optional] |

## Example

```ruby
require 'emass_client'

instance = EmassClient::SwBaselineConditionalFields.new(
  approval_date: 1715312304
)
```

