# EmassClient::WorkflowInstancesResponseGet

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **meta** | [**Response200**](Response200.md) |  | [optional] |
| **data** | [**Array&lt;WorkflowInstanceGet&gt;**](WorkflowInstanceGet.md) |  | [optional] |
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

