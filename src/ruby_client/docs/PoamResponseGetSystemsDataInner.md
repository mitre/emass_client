# EmassClient::PoamResponseGetSystemsDataInner

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **system_id** | **Integer** | [Required] Unique eMASS system identifier. | [optional] |
| **poam_id** | **Integer** | [Required] Unique item identifier | [optional] |
| **display_poam_id** | **Integer** | [Required] Globally unique identifier for individual POA&amp;M Items, seen on the front-end as ID. | [optional] |
| **status** | **String** | [Required] The POA&amp;M status | [optional] |
| **vulnerability_description** | **String** | [Required] Provide a description of the POA&amp;M Item. 2000 Characters. | [optional] |
| **source_identifying_vulnerability** | **String** | [Required] Include Source Identifying Vulnerability text. 2000 Characters. | [optional] |
| **poc_organization** | **String** | [Required] Organization/Office represented. 100 Characters. | [optional] |
| **resources** | **String** | [Required] List of resources used. 250 Characters. | [optional] |
| **identified_in_cfo_audit_or_other_review** | **Boolean** | [Required] If not specified, this field will be set to false because it does not accept a null value. VA only | [optional] |
| **poc_first_name** | **String** | [Conditional] First name of POC. 100 Characters. | [optional] |
| **poc_last_name** | **String** | [Conditional] Last name of POC. 100 Characters. | [optional] |
| **poc_email** | **String** | [Conditional] Email address of POC. 100 Characters. | [optional] |
| **poc_phone_number** | **String** | [Conditional] Phone number of POC (area code) ***-**** format. 100 Characters. | [optional] |
| **severity** | **String** | [Conditional] Required for approved items. Values include the following options: (Very Low, Low, Moderate,High,Very High) | [optional] |
| **scheduled_completion_date** | **Integer** | [Conditional] Required for ongoing and completed POA&amp;M items. Unix time format. | [optional] |
| **completion_date** | **Integer** | [Conditional] Field is required for completed POA&amp;M items. Unix time format. | [optional] |
| **comments** | **String** | [Conditional] Field is required for completed and risk accepted POA&amp;M items. 2000 Characters | [optional] |
| **personnel_resources_funded_base_hours** | **Float** | [Conditional] At least one of the following is required and must be completed for each POA&amp;M Item:   Personnel Resources-&gt; Funded Base Hours   Personnel Resources-&gt; Unfunded Base Hours   Non-Personnel Resources-&gt; Funded Amount   Non-Personnel Resources-&gt; Unfunded Amount Displays numbers to the second decimal point (e.g., 100.00). VA only.  | [optional] |
| **personnel_resources_cost_code** | **String** | [Conditional] Required if Personnel Resources: Funded Base Hours is populated. Only accepts values present in the field&#39;s lookup table (modifiable by eMASS System Admins). VA only.  | [optional] |
| **personnel_resources_unfunded_base_hours** | **Float** | [Conditional] At least one of the following is required and must be completed for each POA&amp;M Item:   Personnel Resources-&gt; Funded Base Hours   Personnel Resources-&gt; Unfunded Base Hours   Non-Personnel Resources-&gt; Funded Amount   Non-Personnel Resources-&gt; Unfunded Amount Displays numbers to the second decimal point (e.g., 100.00). VA only.  | [optional] |
| **personnel_resources_nonfunding_obstacle** | **String** | [Conditional] Required if Personnel Resources: Unfunded Base Hours is populated. Only accepts values present in the field&#39;s lookup table (modifiable by eMASS System Admins). VA only.  | [optional] |
| **personnel_resources_nonfunding_obstacle_other_reason** | **String** | [Conditional] Required if the value \&quot;Other\&quot; is populated for the field Personnel Resources: Non-Funding Obstacle. VA only. | [optional] |
| **non_personnel_resources_funded_amount** | **Float** | [Conditional] At least one of the following is required and must be completed for each POA&amp;M Item:   Personnel Resources-&gt; Funded Base Hours   Personnel Resources-&gt; Unfunded Base Hours   Non-Personnel Resources-&gt; Funded Amount   Non-Personnel Resources-&gt; Unfunded Amount Displays numbers to the second decimal point (e.g., 100.00). VA only.  | [optional] |
| **non_personnel_resources_cost_code** | **String** | [Conditional] Required if Non-Personnel Resources: Funded Amount is populated. Only accepts values present in the field&#39;s lookup table (modifiable by eMASS System Admins). VA only.  | [optional] |
| **non_personnel_resources_unfunded_amount** | **Float** | [Conditional] At least one of the following is required and must be completed for each POA&amp;M Item:   Personnel Resources-&gt; Funded Base Hours   Personnel Resources-&gt; Unfunded Base Hours   Non-Personnel Resources-&gt; Funded Amount   Non-Personnel Resources-&gt; Unfunded Amount Displays numbers to the second decimal point (e.g., 100.00). VA only.  | [optional] |
| **non_personnel_resources_nonfunding_obstacle** | **String** | [Conditional] Required if Non-Personnel Resources: Unfunded Amount is populated. Only accepts values present in the field&#39;s lookup table (modifiable by eMASS System Admins). VA only.  | [optional] |
| **non_personnel_resources_nonfunding_obstacle_other_reason** | **String** | [Conditional] Required if the value \&quot;Other\&quot; is populated for the field Non-Personnel Resources: Non-Funding Obstacle. VA only. | [optional] |
| **milestones** | [**Array&lt;MilestonesGet&gt;**](MilestonesGet.md) |  | [optional] |
| **external_uid** | **String** | [Optional] Unique identifier external to the eMASS application for use with associating POA&amp;Ms. 100 Characters. | [optional] |
| **control_acronym** | **String** | [Optional] Control acronym associated with the POA&amp;M Item. NIST SP 800-53 Revision 4 defined. | [optional] |
| **assessment_procedure** | **String** | [Optional] The Security Control Assessment Procedure being associated with the POA&amp;M Item. | [optional] |
| **security_checks** | **String** | [Optional] Security Checks that are associated with the POA&amp;M. | [optional] |
| **raw_severity** | **String** | [Optional] Scan vulnerability ratting Values include the following options: (Very Low, Low, Moderate,High,Very High) | [optional] |
| **relevance_of_threat** | **String** | [Optional] Values include the following options (Very Low, Low, Moderate,High,Very High) | [optional] |
| **likelihood** | **String** | [Optional] Values include the following options (Very Low, Low, Moderate,High,Very High) | [optional] |
| **impact** | **String** | [Optional] Values include the following options (Very Low, Low, Moderate,High,Very High) | [optional] |
| **impact_description** | **String** | [Optional] Include description of Security Control&#39;s impact. | [optional] |
| **residual_risk_level** | **String** | [Optional] Values include the following options (Very Low, Low, Moderate,High,Very High) | [optional] |
| **recommendations** | **String** | [Optional] Include recommendations. Character Limit &#x3D; 2,000. | [optional] |
| **mitigations** | **String** | [Optional] Include mitigation explanation. 2000 Characters. | [optional] |
| **resulting_residual_risk_level_after_proposed_mitigations** | **String** | [Optional] Indicate the risk level expected after any proposed mitigations are implemented. Proposed mitigations should be appropriately documented as POA&amp;M milestones. Navy only. | [optional] |
| **predisposing_conditions** | **String** | [Optional] A predisposing condition is a condition existing within an organization, a mission or business process, enterprise architecture, information system/PIT, or environment of operation, which affects (i.e., increases or decreases) the likelihood that threat events, once initiated, result in adverse impacts. Navy only. | [optional] |
| **threat_description** | **String** | [Optional] Describe the identified threat(s) and relevance to the information system. Navy only. | [optional] |
| **devices_affected** | **String** | [Optional] List any affected devices by hostname. If all devices in the information system are affected, state &#39;system&#39; or &#39;all&#39;. Navy only | [optional] |
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

instance = EmassClient::PoamResponseGetSystemsDataInner.new(
  system_id: 830,
  poam_id: 45,
  display_poam_id: 100000010,
  status: Completed,
  vulnerability_description: Description text,
  source_identifying_vulnerability: Source Indentifying Vulnerability text,
  poc_organization: Army,
  resources: Resource text,
  identified_in_cfo_audit_or_other_review: true,
  poc_first_name: John,
  poc_last_name: Smith,
  poc_email: smith@ah.com,
  poc_phone_number: 555-555-5555,
  severity: Low,
  scheduled_completion_date: 1799644800,
  completion_date: 1745916276,
  comments: Comments text.,
  personnel_resources_funded_base_hours: 100,
  personnel_resources_cost_code: 123456,
  personnel_resources_unfunded_base_hours: 100,
  personnel_resources_nonfunding_obstacle: Not an system of interest,
  personnel_resources_nonfunding_obstacle_other_reason: Not an system of interest,
  non_personnel_resources_funded_amount: null,
  non_personnel_resources_cost_code: null,
  non_personnel_resources_unfunded_amount: null,
  non_personnel_resources_nonfunding_obstacle: Not an system of interest,
  non_personnel_resources_nonfunding_obstacle_other_reason: Not an system of interest,
  milestones: null,
  external_uid: d6d98b88-c866-4496-9bd4-de7ba48d0f52,
  control_acronym: AC-3,
  assessment_procedure: AC-1.4,
  security_checks: SV-25123r1_rule,2016-A-0279,
  raw_severity: Moderate,
  relevance_of_threat: Low,
  likelihood: Low,
  impact: Low,
  impact_description: Impact text,
  residual_risk_level: Low,
  recommendations: Recommendations text,
  mitigations: Mitigation text,
  resulting_residual_risk_level_after_proposed_mitigations: Low,
  predisposing_conditions: The predisposing condition justification,
  threat_description: The identified threat(s) description,
  devices_affected: system,
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

