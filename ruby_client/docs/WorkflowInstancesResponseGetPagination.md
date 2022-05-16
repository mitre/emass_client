# EmassClient::WorkflowInstancesResponseGetPagination

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **total_count** | **Integer** |  | [optional] |
| **total_pages** | **Integer** |  | [optional] |
| **prev_page_url** | **String** |  | [optional] |
| **next_page_url** | **String** |  | [optional] |

## Example

```ruby
require 'emass_client'

instance = EmassClient::WorkflowInstancesResponseGetPagination.new(
  total_count: 12,
  total_pages: 2,
  prev_page_url: https://my.endpoint.url.org/previousPage,
  next_page_url: https://my.endpoint.url.org/nextPage
)
```

