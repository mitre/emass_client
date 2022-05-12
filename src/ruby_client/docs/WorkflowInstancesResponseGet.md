# EmassClient::WorkflowInstancesResponseGet

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **meta** | [**Model200**](Model200.md) |  | [optional] |
| **data** | [**Array&lt;WorkflowInstancesGet&gt;**](WorkflowInstancesGet.md) |  | [optional] |
| **pagination** | [**WorkflowInstancesResponseGetPagination**](WorkflowInstancesResponseGetPagination.md) |  | [optional] |

## Example

```ruby
require 'emass_client'

instance = EmassClient::WorkflowInstancesResponseGet.new(
  meta: null,
  data: null,
  pagination: null
)
```

