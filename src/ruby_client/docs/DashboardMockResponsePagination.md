# EmassClient::DashboardMockResponsePagination

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **total_count** | **Integer** |  | [optional] |
| **total_pages** | **Integer** |  | [optional] |
| **page_index** | **Integer** |  | [optional] |
| **page_size** | **Integer** |  | [optional] |
| **prev_page_url** | **String** |  | [optional] |
| **next_page_url** | **String** |  | [optional] |

## Example

```ruby
require 'emass_client'

instance = EmassClient::DashboardMockResponsePagination.new(
  total_count: 2,
  total_pages: 1,
  page_index: 2,
  page_size: 20000,
  prev_page_url: https://myfakeurl.reponse.page.com?PreviousPage,
  next_page_url: https://myfakeurl.reponse.page.com?NextPage
)
```

