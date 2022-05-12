# EmassClient::Systems

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **system_id** | **Integer** | [Read-only] Unique system record identifier. | [optional] |
| **policy** | **String** | [Read-only] RMF/DIACAP Policy identifier for the system record. | [optional] |
| **registration_type** | **String** | [Read-Only] Registration types parameters (assessAndAuthorize, assessOnly, guest, regular, functional, cloudServiceProvider.) | [optional] |
| **name** | **String** | [Read-only] Name of the system record. | [optional] |
| **acronym** | **String** | [Read-only] Acronym of the system record. | [optional] |
| **description** | **String** | [Read-only] Description of the system record. | [optional] |
| **system_owner** | **String** | [Read-only] Owning organization of the system record. | [optional] |
| **organization_name** | **String** | [Read-only] Name of the top-level component that owns the system (e.g. Navy, Air Force, Army, etc..). | [optional] |
| **secondary_organization** | **String** | [Read-only] Secondary organization that owns the system record (i.e. Sub-Organization-level. | [optional] |
| **version_release_no** | **String** | [Read-only] Version/Release Number of system record. | [optional] |
| **system_type** | **String** | [Read-only] Type of the system record. RMF values include the following options (IS Major Application, IS Enclave, Platform IT System). DIACAP values include the following options (Platform IT, Interconnection, AIS Application) | [optional] |
| **is_nss** | **Boolean** | [Read-only] Is the system record a National Security System? | [optional] |
| **is_public_facing** | **Boolean** | [Read-only] Does the system record have a public facing component/presence. | [optional] |
| **coams_id** | **Integer** | [Read-only] Corresponding Cyber Operational Attributes Management System (COAMS) identifier for the system record. | [optional] |
| **is_type_authorization** | **Boolean** | [Read-only] Identifies if system is a Type Authorization. | [optional] |
| **ditpr_id** | **String** | [Read-only] DITPR ID of the system record. | [optional] |
| **authorization_status** | **String** | [Read-only] Authorization Status of the system record. | [optional] |
| **authorization_date** | **Integer** | [Read-only] Authorization Date of the system record. | [optional] |
| **authorization_termination_date** | **Integer** | [Read-only] Authorization Termination Date of the system record. | [optional] |
| **authorization_length** | **Integer** | [Read-only] Length of system&#39;s Authorization. Calculated based off of Authorization Date &amp; Authorization Termination Date. | [optional] |
| **terms_for_auth** | **String** | [Read-only] Terms/Conditions for receiving and maintaining the system&#39;s Authorization. Assigned by the Authorizing Official. | [optional] |
| **security_plan_approval_status** | **String** | [Read-only] Status of the approval of the system&#39;s RMF Security Plan. Values include the following options (Approved, Denied, Not Yet Approved). | [optional] |
| **security_plan_approval_date** | **Integer** | [Read-only] Approval date of the system&#39;s RMF Security Plan. | [optional] |
| **mission_criticality** | **String** | [Read-only] Mission Criticality of the system record. Values include the following options (Mission Critical (MC), Mission Essential (ME), Mission Support (MS). | [optional] |
| **geographical_association** | **String** | [Read-only] Geographical Association of the system record (VA only). | [optional] |
| **system_ownership** | **String** | [Read-only] Ownership of the system record (VA only). | [optional] |
| **governing_mission_area** | **String** | [Read-only] Governing Mission Area of the system record. | [optional] |
| **primary_functional_area** | **String** | [Read-only] Primary functional area of the system record. | [optional] |
| **secondary_functional_area** | **String** | [Read-only] Secondary functional area of the system record. | [optional] |
| **primary_control_set** | **String** | [Read-only] Primary Control Set of the system record. RMF values include the following options (NIST SP 800-53 Revision 4), DIACAP values include the following options (DoDI 8500.2) | [optional] |
| **confidentiality** | **String** | [Read-only] Confidentiality of the system record. RMF values include the following options (High, Moderate, Low) | [optional] |
| **integrity** | **String** | [Read-only] Integrity of the system record. RMF values include the following options (High, Moderate, Low) | [optional] |
| **availability** | **String** | [Read-only] Availability of the system record. RMF values include the following options (High, Moderate, Low) | [optional] |
| **applied_overlays** | **String** | [Read-only] Overlays applied to the system record. | [optional] |
| **rmf_activity** | **String** | [Read-only] RMF Activity of the system record. | [optional] |
| **cross_domain_ticket** | **String** | [Read-only] Cross Domain Tickets of the system record. | [optional] |
| **ditpr_don_id** | **String** | [Read-Only] DITPR-DON identifier of the system record. | [optional] |
| **mac** | **String** | [Read-Only] MAC level of the system record. | [optional] |
| **dod_confidentiality** | **String** | [Read-Only] DoD Confidentiality level of the system record. | [optional] |
| **contingency_plan_tested** | **Boolean** | [Read-only] Has the system record&#39;s Contingency Plan been tested? | [optional] |
| **contingency_plan_test_date** | **Integer** | [Read-only] Date the system record&#39;s Contingency Plan was tested. | [optional] |
| **security_review_date** | **Integer** | [Read-only] Date the system record&#39;s Annual Security Review was conducted. | [optional] |
| **has_open_poam_item** | **Boolean** | [Read-Only] Does the system record have an Ongoing or Risk Accepted POA&amp;M Item? | [optional] |
| **has_open_poam_item90to120_past_scheduled_completion_date** | **Boolean** | [Read-Only] Does the system record have an Ongoing or Risk Accepted POA&amp;M Item 90 to 120 days past its Scheduled Completion Date? | [optional] |
| **has_open_poam_item120_plus_past_scheudled_completion_date** | **Boolean** | [Read-Only] Does the system record have an Ongoing or Risk Accepted POA&amp;M Item 120 days past its Scheduled Completion Date? | [optional] |
| **impact** | **String** | [Optional] Values include the following options (Very Low, Low, Moderate,High,Very High) | [optional] |
| **has_cui** | **Boolean** | [Read-only] Does the system record contain and/or process Controlled Unclassified information? | [optional] |
| **has_pii** | **Boolean** | [Read-only] Does the system record contain and/or process Personally Identifiable Information? | [optional] |
| **has_phi** | **Boolean** | [Read-only] Does the system record contain and/or process Personal Health Information? | [optional] |
| **ppsm_registry_number** | **String** | [Read-only] Unique identifier for the DoD’s Ports, Protocols, and Services Management Registry system. | [optional] |
| **interconnected_information_system_and_identifiers** | **String** | [Read-only] Identify the interconnected information systems and corresponding identifiers within control CA-3. | [optional] |
| **is_pia_required** | **Boolean** | [Read-only] Does the system require a Privacy Impact Assessment? | [optional] |
| **pia_status** | **String** | [Read-only] Status of the PIA, availability values include the following options (Not Started, In Progress, Completed) | [optional] |
| **pia_date** | **Integer** | [Read-only] Date in which the system&#39;s PIA took place. | [optional] |
| **user_defined_field1** | **String** | [Read-only] User-defined field to augment Ad Hoc Reporting. | [optional] |
| **user_defined_field2** | **String** | [Read-only] User-defined field to augment Ad Hoc Reporting. | [optional] |
| **user_defined_field3** | **String** | [Read-only] User-defined field to augment Ad Hoc Reporting. | [optional] |
| **user_defined_field4** | **String** | [Read-only] User-defined field to augment Ad Hoc Reporting. | [optional] |
| **user_defined_field5** | **String** | [Read-only] User-defined field to augment Ad Hoc Reporting. | [optional] |
| **current_rmf_lifecycle_step** | **String** | [Read-only] Displays the system&#39;s current step within the RMF Lifecycle. | [optional] |
| **other_information** | **String** | [Read-only] Include any additional information required by the organization. | [optional] |
| **reports_for_scorecard** | **Boolean** | [Read-only] Indicates if the system reports to the DoD Cyber Hygiene Scorecard. | [optional] |
| **package** | [**Array&lt;PacGet&gt;**](PacGet.md) |  | [optional] |
| **connectivity_ccsd** | [**Array&lt;ConnectivityCcsd&gt;**](ConnectivityCcsd.md) |  | [optional] |

## Example

```ruby
require 'emass_client'

instance = EmassClient::Systems.new(
  system_id: 33,
  policy: RMF,
  registration_type: Assess and Authorize,
  name: System XYZ,
  acronym: PM-6,
  description: This is a test system for the eMASS API documentation,
  system_owner: DISA,
  organization_name: Defense Information Systems Agency,
  secondary_organization: ID31,
  version_release_no: V1,
  system_type: IS Major Application,
  is_nss: true,
  is_public_facing: true,
  coams_id: 93054,
  is_type_authorization: true,
  ditpr_id: 30498,
  authorization_status: Authorization to Operate (ATO),
  authorization_date: 1638741660,
  authorization_termination_date: 1638741660,
  authorization_length: 365,
  terms_for_auth: Terms/Conditions to maintain a valid ATO,
  security_plan_approval_status: Approved,
  security_plan_approval_date: 1638741660,
  mission_criticality: Mission Support (MS),
  geographical_association: VA Operated IS,
  system_ownership: Region 1,
  governing_mission_area: DoD portion of the Intelligence MA (DIMA),
  primary_functional_area: Health/Medical,
  secondary_functional_area: Logistics,
  primary_control_set: NIST SP 800-53 Revision 4,
  confidentiality: Low,
  integrity: Moderate,
  availability: High,
  applied_overlays: Classified Information,
  rmf_activity: Maintain ATO and conduct reviews,
  cross_domain_ticket: Cross Domain Ticket test,
  ditpr_don_id: 5910, 1234, 8765,
  mac: II,
  dod_confidentiality: Public,
  contingency_plan_tested: true,
  contingency_plan_test_date: 1426957321,
  security_review_date: 1531958400,
  has_open_poam_item: true,
  has_open_poam_item90to120_past_scheduled_completion_date: false,
  has_open_poam_item120_plus_past_scheudled_completion_date: false,
  impact: Low,
  has_cui: false,
  has_pii: false,
  has_phi: false,
  ppsm_registry_number: Test PPSM Registry Number,
  interconnected_information_system_and_identifiers: Test,
  is_pia_required: true,
  pia_status: Not Started,
  pia_date: 1622048629,
  user_defined_field1: Test User-defined Field 1,
  user_defined_field2: Test User-defined Field 2,
  user_defined_field3: Test User-defined Field 3,
  user_defined_field4: Test User-defined Field 4,
  user_defined_field5: Test User-defined Field 5,
  current_rmf_lifecycle_step: 4 - Assess,
  other_information: Additional Comments,
  reports_for_scorecard: true,
  package: null,
  connectivity_ccsd: null
)
```

