# EmassClient::StaticCodeApplicationPost

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **raw_severity** | **String** | [Optional] Scan vulnerability ratting | [optional] |
| **code_check_name** | **String** | [Required] Name of the software vulnerability or weakness. | [optional] |
| **count** | **Integer** | [Required] Number of instances observed for a specified finding. | [optional] |
| **scan_date** | **Integer** | [Required] The date of the scan. Unix date format. | [optional] |
| **cwe_id** | **String** | [Required] The Common Weakness Enumerator (CWE) identifier. | [optional] |
| **clear_findings** | **Boolean** | [Optional] When used by itself, can clear out all application findings for a single application/version pairing. | [optional] |

## Example

```ruby
require 'emass_client'

instance = EmassClient::StaticCodeApplicationPost.new(
  raw_severity: Moderate,
  code_check_name: Hidden Field,
  count: 14,
  scan_date: 1625070000,
  cwe_id: 155,
  clear_findings: false
)
```

