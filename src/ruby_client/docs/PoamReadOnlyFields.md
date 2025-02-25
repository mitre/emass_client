# EmassClient::PoamReadOnlyFields

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **condition_id** | **String** | [Read-Only] Unique identifier of the authorization term/condition linked to the POA&amp;M Item. | [optional] |
| **is_inherited** | **Boolean** | [Read-only] Indicates whether a test result is inherited. | [optional] |
| **cci** | **String** | [Read-Only] CCI associated with POA&amp;M Item. | [optional] |
| **review_status** | **String** | [Read-Only] Values include the following options: (Not Approved,Under Review,Approved) | [optional] |
| **created_date** | **Integer** | [Read-Only] Timestamp representing when the POA&amp;M Item was entered into the database. | [optional] |
| **extension_date** | **Integer** | [Read-Only] Value returned for a POA&amp;M Item with review status \&quot;Approved\&quot; and has a milestone with a scheduled completion date that extends beyond the POA&amp;M Item&#39;s scheduled completion date.  | [optional] |
| **pending_extension_date** | **Integer** | [Read-Only] Value returned for a POA&amp;M Item with a review status of \&quot;Approved\&quot; and an unapproved milestone with a scheduled completion date that extends beyond the POA&amp;M Item&#39;s scheduled completion date.  | [optional] |
| **artifacts** | **String** | [Read-Only] Lists the filenames of any artifact files attached to the POA&amp;M Item. Multiple values are separated by “; ”. | [optional] |

## Example

```ruby
require 'emass_client'

instance = EmassClient::PoamReadOnlyFields.new(
  condition_id: TC-10100292,
  is_inherited: true,
  cci: 000001,000002,
  review_status: Under Review,
  created_date: 1715312304,
  extension_date: 1715312304,
  pending_extension_date: 1715312304,
  artifacts: Test1.docx; Test2.xlsx
)
```

