# EmassClient::MockObject

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **poc_organization** | **String** | [Required] Organization/Office represented. 100 Characters. | [optional] |
| **resources** | **String** | [Required] List of resources used. 250 Characters. | [optional] |
| **owning_organization** | **String** | [Read-Only] Owning organization of the system record. Values match the eMASS instance Organizational Hierarchy. | [optional] |
| **secondary_organization** | **String** | [Read-only] Secondary organization that owns the system record (i.e. Sub-Organization-level. | [optional] |
| **poc_first_name** | **String** | [Conditional] First name of POC. 100 Characters. | [optional] |
| **poc_last_name** | **String** | [Conditional] Last name of POC. 100 Characters. | [optional] |
| **poc_email** | **String** | [Conditional] Email address of POC. 100 Characters. | [optional] |
| **poc_phone_number** | **String** | [Conditional] Phone number of POC (area code) ***-**** format. 100 Characters. | [optional] |
| **severity** | **String** | [Conditional] Required for approved items. Values include the following options: (Very Low, Low, Moderate,High,Very High) | [optional] |
| **scheduled_completion_date** | **Integer** | [Conditional] Required for ongoing and completed POA&amp;M items. Unix time format. | [optional] |
| **completion_date** | **Integer** | [Conditional] Field is required for completed POA&amp;M items. Unix time format. | [optional] |
| **comments** | **String** | [Conditional] Field is required for completed and risk accepted POA&amp;M items. 2000 Characters | [optional] |
| **is_active** | **Boolean** | [Conditional] Optionally used in PUT to delete milestones when updating a POA&amp;M. | [optional] |

## Example

```ruby
require 'emass_client'

instance = EmassClient::MockObject.new(
  poc_organization: Army,
  resources: Resource text.,
  owning_organization: Defense Information Systems Agency,
  secondary_organization: ID31,
  poc_first_name: John,
  poc_last_name: Smith,
  poc_email: smith@ah.com,
  poc_phone_number: 555-555-5555,
  severity: Low,
  scheduled_completion_date: 1599644800,
  completion_date: 1505916276,
  comments: Comments text.,
  is_active: true
)
```

