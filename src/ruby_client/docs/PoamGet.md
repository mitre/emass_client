# EmassClient::PoamGet

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **external_uid** | **String** | [Optional] Unique identifier external to the eMASS application for use with associating POA&amp;Ms. 100 Characters. | [optional] |
| **system_id** | **Integer** | [Required] Unique eMASS system identifier. | [optional] |
| **poam_id** | **Integer** | [Required] Unique item identifier | [optional] |
| **display_poam_id** | **Integer** | [Required] Globally unique identifier for individual POA&amp;M Items, seen on the front-end as “ID”. | [optional] |
| **is_inherited** | **Boolean** | [Read-only] Indicates whether a test result is inherited. | [optional] |
| **control_acronym** | **String** | [Optional] System acronym name. | [optional] |
| **cci** | **String** | [Optional] CCI associated with POA&amp;M Item.. | [optional] |
| **status** | **String** | [Required] Values include the following: (Ongoing,Risk Accepted,Completed,Not Applicable | [optional] |
| **review_status** | **String** | [Read-Only] Values include the following options: (Not Approved,Under Review,Approved) | [optional] |
| **vulnerability_description** | **String** | [Required] Provide a description of the POA&amp;M Item. 2000 Characters. | [optional] |
| **source_ident_vuln** | **String** | [Required] Include Source Identifying Vulnerability text. 2000 Characters. | [optional] |
| **security_checks** | **String** | [Optional] Security Checks that are associated with the POA&amp;M. | [optional] |
| **milestones** | [**Array&lt;MilestonesGet&gt;**](MilestonesGet.md) |  | [optional] |
| **poc_organization** | **String** | [Required] Organization/Office represented. 100 Characters. | [optional] |
| **poc_first_name** | **String** | [Conditional] First name of POC. 100 Characters. | [optional] |
| **poc_last_name** | **String** | [Conditional] Last name of POC. 100 Characters. | [optional] |
| **poc_email** | **String** | [Conditional] Email address of POC. 100 Characters. | [optional] |
| **poc_phone_number** | **String** | [Conditional] Phone number of POC. 100 Characters. | [optional] |
| **severity** | **String** | [Conditional] Required for approved items. Values include the following options (Very Low,Low,Moderate,High,Very High) | [optional] |
| **raw_severity** | **String** | [Optional] Values include the following options (I,II,III) | [optional] |
| **relevance_of_threat** | **String** | [Optional] Values include the following options: (Very Low,Low,Moderate,High,Very High) | [optional] |
| **likelihood** | **String** | [Optional] Values include the following options: (Very Low,Low,Moderate,High,Very High) | [optional] |
| **impact** | **String** | [Optional] Values include the following options: (Very Low,Low,Moderate,High,Very High) | [optional] |
| **impact_description** | **String** | [Optional] Include description of Security Control’s impact. | [optional] |
| **residual_risk_level** | **String** | [Optional] Values include the following options: (Very Low,Low,Moderate,High,Very High) | [optional] |
| **recommendations** | **String** | [Optional] Include recommendations. Character Limit &#x3D; 2,000. | [optional] |
| **resources** | **String** | [Required] List of resources used. 250 Characters. | [optional] |
| **scheduled_completion_date** | **Integer** | [Conditional] Required for ongoing and completed POA&amp;M items. Unix time format. | [optional] |
| **completion_date** | **Integer** | [Conditional] Field is required for completed POA&amp;M items. Unix time format. | [optional] |
| **extension_date** | **Integer** | [Read-Only] Value returned for a POA&amp;M Item with review status Approved” and has a milestone with a scheduled completion date that extends beyond the POA&amp;M Item’s scheduled completion date.  | [optional] |
| **comments** | **String** | [Conditional] Field is required for completed and risk accepted POA&amp;M items. 2000 Characters | [optional] |
| **mitigation** | **String** | [Optional] Include mitigation explanation. 2000 Characters. | [optional] |
| **is_active** | **Boolean** | [Conditional] Optionally used in PUT to delete milestones when updating a POA&amp;M. | [optional] |

## Example

```ruby
require 'emass_client'

instance = EmassClient::PoamGet.new(
  external_uid: d6d98b88-c866-4496-9bd4-de7ba48d0f52,
  system_id: 830,
  poam_id: 45,
  display_poam_id: 100000010,
  is_inherited: true,
  control_acronym: “AC-3”,
  cci: 000001,000002,
  status: Completed,
  review_status: Under Review,
  vulnerability_description: Description text,
  source_ident_vuln: Source Indentifying Vulnerability text,
  security_checks: SV-25123r1_rule,2016-A-0279,
  milestones: null,
  poc_organization: Army,
  poc_first_name: John,
  poc_last_name: Smith,
  poc_email: smith@ah.com,
  poc_phone_number: 555-555-5555,
  severity: Low,
  raw_severity: I,
  relevance_of_threat: Low,
  likelihood: Moderate,
  impact: High,
  impact_description: Impact Description text,
  residual_risk_level: Very Low,
  recommendations: Recommendations text,
  resources: Resource text.,
  scheduled_completion_date: 1599644800,
  completion_date: 1505916276,
  extension_date: 1505916298,
  comments: Comments text.,
  mitigation: Mitigation text,
  is_active: true
)
```

