# EmassClient::Pagination

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **page_index** | **Integer** |  | [optional] |
| **page_size** | **Integer** |  | [optional] |
| **total_count** | **Integer** |  | [optional] |
| **total_pages** | **Integer** |  | [optional] |
| **prev_page_url** | **String** |  | [optional] |
| **next_page_url** | **String** |  | [optional] |

## Example

```ruby
require 'emass_client'

instance = EmassClient::Pagination.new(
  page_index: 1,
  page_size: 20000,
  total_count: 4,
  total_pages: 1,
  prev_page_url: https://myfakeurl.reponse.page.com?PreviousPage,
  next_page_url: https://myfakeurl.reponse.page.com?NextPage
)
```

