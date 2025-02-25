# EmassClient::Systems

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **registration_completion_date** | **Integer** | [Read-Only] Date the system was registered into eMASS. | [optional] |
| **system_life_cycle_acquisition_phase** | **String** | [Read-Only] Identifies the current System Acquisition Phase for programs of record. | [optional] |
| **special_type** | **String** | [Read-Only] Lists applicable tracking indicator(s). | [optional] |
| **special_type_description** | **String** | [Read-Only] Provides a brief reason for any tracking indicator(s) selected. | [optional] |
| **mission_portfolio** | **String** | [Read-Only] Identifies the appropriate portfolio or capability area. Navy only. | [optional] |
| **is_nnpi** | **Boolean** | [Read-Only] Indicates whether Naval Nuclear Propulsion Information (NNPI) is stored, disseminated, or processed through this system. Navy only. | [optional] |
| **is_rbc** | **Boolean** | [Read-Only] Indicates whether the system is pursuing an RBC authorization. Navy only. | [optional] |
| **is_waiver** | **Boolean** | [Read-Only] Indicates if the system has a waiver from OPNAV N2N6G (DDCIO(N)) to proceed with a DIACAP accreditation. Navy and DIACAP only. | [optional] |
| **program_office** | **String** | [Read-Only] The system record&#39;s Program Office. Navy only. | [optional] |
| **vram_id** | **String** | [Read-Only] Vulnerability Remediation Asset Manager (VRAM) identification number. \&quot;N/A\&quot; indicates the system record is not currently registered in VRAM.  Navy only. | [optional] |
| **system_id** | **Integer** | [Read-only] Unique system record identifier. | [optional] |
| **policy** | **String** | [Read-only] RMF/DIACAP Policy identifier for the system record. | [optional] |
| **registration_type** | **String** | [Read-Only] Registration type of the system record. Values include (assessAndAuthorize, assessOnly, guest, regular, functional, cloudServiceProvider.) | [optional] |
| **name** | **String** | [Read-only] Name of the system record. | [optional] |
| **acronym** | **String** | [Read-only] Acronym of the system record. | [optional] |
| **description** | **String** | [Read-only] Description of the system record. | [optional] |
| **instance** | **String** | [Read-Only] Name of the top-level component that owns the system. | [optional] |
| **owning_organization** | **String** | [Read-Only] Owning organization of the system record. Values match the eMASS instance Organizational Hierarchy. | [optional] |
| **secondary_organization** | **String** | [Read-only] Secondary organization that owns the system record (i.e. Sub-Organization-level. | [optional] |
| **version_release_no** | **String** | [Read-only] Version/Release Number of system record. | [optional] |
| **system_type** | **String** | [Read-only] Type of the system record. RMF values include the following options (IS Major Application, IS Enclave, Platform IT System). DIACAP values include the following options (Platform IT Interconnection, AIS Application, Outsourced IT-Based Process (DoD-controlled), Enclave, Outsourced IT-Based Process (service provider shared)) | [optional] |
| **is_nss** | **Boolean** | [Read-only] Is the system record a National Security System? | [optional] |
| **is_public_facing** | **Boolean** | [Read-only] Does the system record have a public facing component/presence. | [optional] |
| **coams_id** | **Integer** | [Read-only] Corresponding Cyber Operational Attributes Management System (COAMS) identifier for the system record. | [optional] |
| **is_type_authorization** | **Boolean** | [Read-only] Identifies if system is a Type Authorization. | [optional] |
| **ditpr_id** | **String** | [Read-only] DITPR ID of the system record. | [optional] |
| **apms_id** | **String** | [Read-Only] Same field as ditprId but displays as apmsId for Army only. | [optional] |
| **vasi_id** | **String** | [Read-Only] Same field as ditprId but displays as vasiId for VA only. | [optional] |
| **authorization_status** | **String** | [Read-only] Authorization Status of the system record. | [optional] |
| **authorization_date** | **Integer** | [Read-only] Authorization Date of the system record. | [optional] |
| **authorization_termination_date** | **Integer** | [Read-only] Authorization Termination Date of the system record. | [optional] |
| **authorization_length** | **Integer** | [Read-only] Length of system&#39;s Authorization. Calculated based off of Authorization Date &amp; Authorization Termination Date. | [optional] |
| **security_controls_assessor_executive_summary** | **String** | [Read-Only] Document an assessment of overall cybersecurity risk (Very Low, Low, Moderate, High, Very High) and identify the key drivers for assessment. | [optional] |
| **risk_review_executive_summary** | **String** | [Read-Only] Document an assessment of overall cybersecurity risk (Very Low, Low, Moderate, High, Very High) and identify the key drivers for assessment. VA only | [optional] |
| **terms_for_auth** | **String** | [Read-only] Terms/Conditions for receiving and maintaining the system&#39;s Authorization. Assigned by the Authorizing Official. | [optional] |
| **security_plan_approval_status** | **String** | [Read-only] Status of the approval of the system&#39;s RMF Security Plan. Values include the following options (Approved, Denied, Not Yet Approved). | [optional] |
| **security_plan_approval_date** | **Integer** | [Read-only] Approval date of the system&#39;s RMF Security Plan. | [optional] |
| **mission_criticality** | **String** | [Read-only] Mission Criticality of the system record. | [optional] |
| **geographical_association** | **String** | [Read-only] Geographical Association of the system record. | [optional] |
| **system_ownership_controlled** | **String** | [Read-only] Ownership of the system record. | [optional] |
| **governing_mission_area** | **String** | [Read-only] Governing Mission Area of the system record. | [optional] |
| **primary_functional_area** | **String** | [Read-only] Primary functional area of the system record. | [optional] |
| **secondary_functional_area** | **String** | [Read-only] Secondary functional area of the system record. | [optional] |
| **primary_control_set** | **String** | [Read-only] Primary Control Set of the system record. RMF values include the following options (NIST SP 800-53 Revision 4), DIACAP values include the following options (DoDI 8500.2) | [optional] |
| **confidentiality** | **String** | [Read-only] Confidentiality of the system record. RMF values include the following options (High, Moderate, Low) | [optional] |
| **integrity** | **String** | [Read-only] Integrity of the system record. RMF values include the following options (High, Moderate, Low) | [optional] |
| **availability** | **String** | [Read-only] Availability of the system record. RMF values include the following options (High, Moderate, Low) | [optional] |
| **applied_overlays** | **String** | [Read-only] Overlays applied to the system record. Multiple values are separated by semi-colon &#39;;&#39;. | [optional] |
| **applied_stigs** | **String** | [Read-only] The STIG&#39;s applied to the system record. | [optional] |
| **rmf_activity** | **String** | [Read-only] RMF Activity of the system record. | [optional] |
| **cross_domain_ticket** | **String** | [Read-only] Cross Domain Tickets of the system record. | [optional] |
| **ditpr_don_id** | **String** | [Read-Only] DITPR-DON identifier of the system record. | [optional] |
| **mac** | **String** | [Read-Only] MAC level of the system record. | [optional] |
| **dod_confidentiality** | **String** | [Read-Only] DoD Confidentiality level of the system record. | [optional] |
| **contingency_plan_required** | **Boolean** | [Read-Only] Is there a Contingency Plan in place for this system that addresses disruptions in operations? | [optional] |
| **contingency_plan_artifact** | **String** | [Read-Only] Filename of the system&#39;s Contingency Plan artifact. | [optional] |
| **contingency_plan_tested** | **Boolean** | [Read-only] Has the system record&#39;s Contingency Plan been tested? | [optional] |
| **contingency_plan_test_date** | **Integer** | [Read-only] Date the system record&#39;s Contingency Plan was tested. | [optional] |
| **security_review_required** | **Boolean** | [Read-Only] Is the system required to complete a Security Review? | [optional] |
| **security_review_completed** | **Boolean** | [Read-Only] Has a Security Review been completed for this system? | [optional] |
| **security_review_completion_date** | **Integer** | [Read-Only] Date of the system&#39;s latest security review or annual assessment. | [optional] |
| **next_security_review_due_date** | **Integer** | [Read-Only] Date when the system&#39;s next security review or annual assessment is due by. | [optional] |
| **has_open_poam_item** | **Boolean** | [Read-Only] Does the system record have an Ongoing or Risk Accepted POA&amp;M Item? | [optional] |
| **has_open_poam_item90to120_past_scheduled_completion_date** | **Boolean** | [Read-Only] Does the system record have an Ongoing or Risk Accepted POA&amp;M Item 90 to 120 days past its Scheduled Completion Date? | [optional] |
| **has_open_poam_item120_plus_past_scheudled_completion_date** | **Boolean** | [Read-Only] Does the system record have an Ongoing or Risk Accepted POA&amp;M Item 120 days past its Scheduled Completion Date? | [optional] |
| **impact** | **String** | [Optional] Values include the following options (Very Low, Low, Moderate,High,Very High) | [optional] |
| **has_cui** | **Boolean** | [Read-only] Does the system record contain and/or process Controlled Unclassified information? | [optional] |
| **has_pii** | **Boolean** | [Read-only] Does the system record contain and/or process Personally Identifiable Information? | [optional] |
| **has_phi** | **Boolean** | [Read-only] Does the system record contain and/or process Personal Health Information? | [optional] |
| **ppsm_registration_required** | **String** | [Read-Only] Determine if a PPSM registration is required. | [optional] |
| **ppsm_registry_number** | **String** | [Read-only] Unique identifier for the DoD&#39;s Ports, Protocols, and Services Management Registry system. | [optional] |
| **ppsm_registration_exemption_justification** | **String** | [Read-Only] Clarify why a PPSM registraiton is not necessary. | [optional] |
| **interconnected_information_system_and_identifiers** | **String** | [Read-only] Identify the interconnected information systems and corresponding identifiers within control CA-3. | [optional] |
| **privacy_impact_assessment_required** | **Boolean** | [Read-only] Does the system require a Privacy Impact Assessment? | [optional] |
| **privacy_impact_assessment_status** | **String** | [Read-only] Status of the PIA, availability values include the following options (Not Started, In Progress, Completed) | [optional] |
| **privacy_impact_assessment_date** | **Integer** | [Read-only] Date in which the system&#39;s PIA took place. | [optional] |
| **privacy_impact_assessment_artifact** | **String** | [Read-Only] Filename of the system&#39;s PIA artifact. | [optional] |
| **user_defined_field1** | **String** | [Read-only] User-defined field to augment Ad Hoc Reporting. | [optional] |
| **user_defined_field2** | **String** | [Read-only] User-defined field to augment Ad Hoc Reporting. | [optional] |
| **user_defined_field3** | **String** | [Read-only] User-defined field to augment Ad Hoc Reporting. | [optional] |
| **user_defined_field4** | **String** | [Read-only] User-defined field to augment Ad Hoc Reporting. | [optional] |
| **user_defined_field5** | **String** | [Read-only] User-defined field to augment Ad Hoc Reporting. | [optional] |
| **current_rmf_lifecycle_step** | **String** | [Read-only] Displays the system&#39;s current step within the RMF Lifecycle. | [optional] |
| **other_information** | **String** | [Read-only] Include any additional information required by the organization. | [optional] |
| **reports_for_scorecard** | **Boolean** | [Read-only] Indicates if the system reports to the DoD Cyber Hygiene Scorecard. | [optional] |
| **highest_system_data_classification** | **String** | [Read-Only] The overall classification level of information that the System is approved to collect, process, store, and/or distribute. | [optional] |
| **overall_classification** | **String** | [Read-Only] Same field as highestSystemDataClassification, but displays as overallClassification for NISP only. | [optional] |
| **is_hva** | **Boolean** | [Read-Only] Indicates if the system contains High Value Assets. Does not display if value is null | [optional] |
| **is_financial_management** | **Boolean** | [Read-Only] Per OMB Circular A-127, a financial management system includes the core financial systems and the financial portions of mixed systems necessary to support financial management, including automated and manual processes, procedures, and controls, data, hardware, software, and support personnel dedicated to the operation and maintenance of system functions. The following are examples of financial management systems: core financial systems, procurement systems, loan systems, grants systems, payroll systems, budget formulation systems, billing systems, and travel systems.  | [optional] |
| **is_reciprocity** | **Boolean** | [Read-Only] A reciprocity system is any information system that is part of a mutual agreement among participating organizations to accept each other&#39;s security assessments in order to reuse information system resources and/or to accept each other&#39;s assessed security posture in order to share information.  | [optional] |
| **reciprocity_exemption** | **String** | [Read-Only] The following justifications are acceptable for exemption from reciprocity: (a) the existence of the system is classified (not the data, but the existence of the system) or (b) the system&#39;s authorization to operate is in the process of being pulled (e.g. DATO, Decommission).  | [optional] |
| **cloud_computing** | **Boolean** | [Read-Only] Is this a cloud-based IS? | [optional] |
| **cloud_type** | **String** | [Read-Only] Values include the following: (Hybrid, Private, Public) | [optional] |
| **authorization_to_connect_status** | **String** | [Read-Only] The Authority to Connect decision. Values include the following: (Authority to Connect (ATC), Denial of Authority to Connect (DATC), Not Yet Connected, Decommissioned)  | [optional] |
| **is_saa_s** | **Boolean** | [Read-Only] Software as a Service (SaaS) cloud service model. | [optional] |
| **is_paa_s** | **Boolean** | [Read-Only] Platform as a Service (PaaS) cloud service model. | [optional] |
| **is_iaa_s** | **Boolean** | [Read-Only] Infrastructure as a Service (IaaS) cloud service model. | [optional] |
| **other_service_models** | **String** | [Read-Only] Free text field to include other cloud service models. | [optional] |
| **need_date** | **Integer** | [Read-Only] Indicates the date by which the System needs to be deployed to a production environment. | [optional] |
| **overall_risk_score** | **String** | [Read-Only] The overall risk score of the system | [optional] |
| **is_hrr** | **Boolean** | [Read-Only] Identifies whether a System has been designated as High Risk Review. USCG and Navy only. | [optional] |
| **connectivity_authorization_date** | **Integer** | [Read-Only] The Connectivity Authorization Date. | [optional] |
| **connectivity_authorization_termination_date** | **Integer** | [Read-Only] The Connectivity Authorization Termination Date. | [optional] |
| **system_development_life_cycle** | **String** | [Read-Only] Indicate the date by which the System needs to be deployed to a production environment. VA only. | [optional] |
| **is_fisma_reportable** | **Boolean** | [Read-Only] Is this IS reportable per Federal Information Security Management Act (FISMA) established requirements? VA only | [optional] |
| **group_tagging** | **String** | [Read-Only] System Tags for enterprise level, to include CIO and CISO, tracking efforts. VA only. | [optional] |
| **group_tag_descriptions** | **String** | [Read-Only] System Tag explanation(s) for enterprise level, to include CIO and CISO, tracking efforts. VA only. | [optional] |
| **dadms_id** | **String** | [Read-Only] The system&#39;s DADMS ID. USMC only. | [optional] |
| **dadms_expiration_date** | **Integer** | [Read-Only] Date the system expires in DADMS. USMC only. | [optional] |
| **enclave_connectivity** | **String** | [Read-Only] Identify the type of connectivity for the network/enclave, e.g., DISA circuit (NIPR, SIPR) or HPCMP circuit (DREN, SDREN, Outreach). Navy only. | [optional] |
| **environment_type** | **String** | [Read-Only] Identify the primary computing environment for where the information system is deployed. Navy only. | [optional] |
| **navy_common_control_provider** | **Boolean** | [Read-Only] Indicate whether the information system provides inheritable controls. Navy only | [optional] |
| **navy_cloud_broker** | **String** | [Read-Only] Identify the broker responsible for the delivery of commercial cloud services and capabilities. Refer to Navy Commercial Cloud Brokerage Policy. Navy Only | [optional] |
| **cloud_broker_emass_id** | **Integer** | [Read-Only] The eMASS ID of the identified cloud broker. Navy only. | [optional] |
| **cloud_broker_provisional_authorization_atd** | **Integer** | [Read-Only] The provisional authorization termination date of the identified cloud broker. Navy only | [optional] |
| **navy_joint_authorization** | **Boolean** | [Read-Only] Indicate whether this is a joint authorization being issued by two or more Authorizing Officials. Navy only | [optional] |
| **nmci_ngen_clins** | **String** | [Read-Only] Provide all NMCI CLINs associated to the system/services within the authorization boundary. Navy only | [optional] |
| **enterprise_locations** | **String** | [Read-Only] Identify the Navy enterprise network where the information system is deployed. Navy only | [optional] |
| **whitelist_id** | **String** | [Read-Only] Systems that have public-facing components/presences are typically required to be documented and registered as part of Organzationally-approved whitelisting processes. | [optional] |
| **whitelist_inventory** | **String** | [Read-Only] Provide/upload the documentation that identifies or describes the components or aspects of the System that are public-facing (whitelisted). | [optional] |
| **acquisition_category** | **String** | [Read-Only] Values include the following options (I,II,III) | [optional] |
| **software_category** | **String** | [Read-Only] Lists the software category. | [optional] |
| **cybersecurity_service_provider** | **String** | [Read-Only] Name of the system&#39;s Cybersecurity Service Provider. | [optional] |
| **cybersecurity_service_provider_exception_justification** | **String** | [Read-Only] If Not Applicable, provide the exception justification. | [optional] |
| **maximum_tolerable_downtime** | **String** | [Read-Only] MTD represents the total amount of time leaders/managers are willing to accept for a process outage or disruption. | [optional] |
| **recovery_time_objective** | **String** | [Read-Only] RTO defines the maximum amount of time a system can remain unavailable before there is an unacceptable impact on other systems, supported business processes, and the MTD. | [optional] |
| **recovery_point_objective** | **String** | [Read-Only] RPO represents the point in time, prior to a disruption or system outage, to which mission/business data can be recovered (given the most recent backup copy of the data) after an outage. The system data/information owner determines an acceptable RPO in terms of amount of tolerable data loss before unacceptable impact occurs. | [optional] |
| **business_impact_analysis_required** | **Boolean** | [Read-Only] Is a Business Impact Analysis in place that identifies critical business processes, MTD, RTO, and RPO? | [optional] |
| **business_impact_analysis_artifact** | **String** | [Read-Only] Filename of the system&#39;s Business Impact Analysis artifact. | [optional] |
| **incident_response_plan_required** | **Boolean** | [Read-Only] Is there a Incident Response Plan in place for this system that provides the roadmap for implementing the incident response capability? | [optional] |
| **incident_response_plan_artifact** | **String** | [Read-Only] Filename of the system&#39;s Incident Response Plan artifact. | [optional] |
| **disaster_recovery_plan_required** | **Boolean** | [Read-Only] Is there a Disaster Recovery Plan in place for this system that addresses information system disruptions that require relocation? | [optional] |
| **disaster_recovery_plan_artifact** | **String** | [Read-Only] Filename of the system&#39;s Disaster Recovery Plan artifact. | [optional] |
| **privacy_threshold_analysis_completed** | **Boolean** | [Read-Only] Indicate whether a Privacy Threshold Analysis (PTA) has been performed for this IS. | [optional] |
| **privacy_threshold_analysis_date** | **Integer** | [Read-Only] Date in which this sytem&#39;s Privacy Threshold Analysis took place. | [optional] |
| **privacy_threshold_analysis_artifact** | **String** | [Read-Only] Filename of the system&#39;s Privacy Threshold Analysis artifact. | [optional] |
| **privacy_act_system_of_records_notice_required** | **Boolean** | [Read-Only] Does this system require a Privacy Act System of Record Notice per DoD 5400.11-R? | [optional] |
| **e_authentication_risk_assessment_required** | **Boolean** | [Read-Only] Indicate whether an E-Authentication Risk Assessment has been performed for the system in accordance with OMB M-04-04. | [optional] |
| **e_authentication_risk_assessment_date** | **Integer** | [Read-Only] Date this system&#39;s EAuthentication Risk Assessment took place. | [optional] |
| **e_authentication_risk_assessment_artifact** | **String** | [Read-Only] Filename of the system&#39;s Privacy Threshold Analysis artifact. | [optional] |
| **ipv4_only_assets** | **Integer** | [Read-Only] Identify the total number of assets associated with this boundary that are only on IPv4. | [optional] |
| **ipv6_only_assets** | **Integer** | [Read-Only] Identify the total number of assets associated with this boundary that are only on IPv6. | [optional] |
| **ipv4_ipv6_dual_stack_assets** | **Integer** | [Read-Only] Identify the total number of assets associated with this boundary that are operating on IPv4/IPv6 dual-stack. | [optional] |
| **total_ip_assets** | **Integer** | [Read-Only] Total number of IPv4, IPv6, and dual-stack assets identified. Value calculated upon Save action | [optional] |
| **originating_organization** | **String** | [Read-Only] Identify the organization that generated the existing authorization package, including (where applicable) individual points of contact. | [optional] |
| **system_use_justification** | **String** | [Read-Only] Provide a detailed justification as to why this system should be deployed and used within the requesting organization. | [optional] |
| **system_use_justification_artifact** | **String** | [Read-Only] Filename of the System Use Justification Artifact, including the file extension. | [optional] |
| **authorization_to_use_status** | **String** | [Read-Only] The system&#39;s Authority to Use Status. | [optional] |
| **reciprocity_acceptance_status** | **String** | [Read-Only] The system&#39;s Reciprocity Acceptance Status. Army IC only. | [optional] |
| **use_authorization_date** | **Integer** | [Read-Only] The system&#39;s Use Authorization Date. | [optional] |
| **reciprocity_acceptance_date** | **Integer** | [Read-Only] The system&#39;s Reciprocity Acceptance Date. Army IC only. | [optional] |
| **use_authorization_termination_date** | **Integer** | [Read-Only] The system&#39;s Use Authorization Termination Date. | [optional] |
| **reciprocity_acceptance_termination_date** | **Integer** | [Read-Only] The system&#39;s Reciprocity Acceptance Termination Date. Army IC only. | [optional] |
| **terms_conditions_for_use_summary** | **String** | [Read-Only] The system&#39;s Terms / Conditions for Use Summary. | [optional] |
| **terms_conditions_for_reciprocity_summary** | **String** | [Read-Only] The system&#39;s Terms / Conditions for Reciprocity Summary. Army IC only. | [optional] |
| **primary_mission_essential_function** | **Boolean** | [Read-Only] Annotate &#39;Yes&#39; if your system performs a Primary Mission Essential Function. VA only | [optional] |
| **pmef_description** | **String** | [Read-Only] The FIPS category \&quot;Availability\&quot; of this system must be marked \&quot;High\&quot; if the system is listed as a PMEF, and the RTO must be 12 hours or shorter. VA only | [optional] |
| **mission_essential_function** | **Boolean** | [Read-Only] Annotate \&quot;Yes\&quot; if your system performs a Mission Essential Function. VA only. | [optional] |
| **mef_description** | **String** | [Read-Only] MEFs are listed in the OIT Continuity Plan. VA Handbook 0322 will be updated with these MEFs. VA only. | [optional] |
| **administration** | **String** | [Read-Only] Identify the administration that this information system supports. VA only. | [optional] |
| **administration_other_justification** | **String** | [Read-Only] If the Administration field is set to \&quot;Other\&quot;, this free-text field becomes required. VA only. | [optional] |
| **atc_iatc_granted_date** | **Integer** | [Read-Only] The date the Authority to Connect (ATC) or Interim Authority to Connect (IATC) was granted. | [optional] |
| **atc_iatc_expiration_date** | **Integer** | [Read-Only] The date the Authority to Connect (ATC) or Interim Authority to Connect (IATC) expires. | [optional] |
| **atc_iatc_pending_items** | **String** | [Read-Only] List of pending items required for the Authority to Connect (ATC) or Interim Authority to Connect (IATC). | [optional] |
| **pending_items_due_date** | **Integer** | [Read-Only] The date the pending items are due. | [optional] |
| **dodinn_system_id** | **Boolean** | [Read-Only] A DoDIN-N system is all encompassing for the following: Navy networks, systems, sites, corporate assets, centrally managed programs, programs of record, standalone, excepted, enterprise, non-enterprise, cloud, NIPRNET, SIPRNET, GENSER Classified, Defense Research Engineering Network (DREN), Secret DREN (SDREN), connected to the DoDIN or through commercial lines that are owned, operated, leased, contracted, maintained, managed, administered, house Navy data, house Navy personally identifiable information, house Navy protected health information, or controlled unclassified information. The DoDIN-N also includes commercial information technology, weapons systems/program manager/program of record/platform information technology, and operational technology. Navy only. | [optional] |
| **authorization_to_use_connect_status** | **String** | [Read-Only] FCC CRMA/NAO approval for DoDIN-N operations. Navy only. | [optional] |
| **use_connect_authorization_date** | **Integer** | [Read-Only] The Use/Connect Authorization Date. Navy only. | [optional] |
| **use_connect_authorization_termination_date** | **Integer** | [Read-Only] The Use/Connect Authorization Termination Date Navy only. | [optional] |
| **terms_conditions_for_use_connect_summary** | **String** | [Read-Only] Provide a description (if applicable) of any specific limitations or restrictions placed on the operation of the information system as part of the authorization to use/connect decision. Navy only. | [optional] |
| **workstations** | **Integer** | [Read-Only] Identify the number of System Workstations. This data will be used for the National Industrial Security System (NISS) facility categorization. If field is not applicable enter \&quot;0\&quot;. NISP only. | [optional] |
| **servers** | **Integer** | [Read-Only] Identify the number of System Servers. This data will be used for the National Industrial Security System (NISS) facility categorization. If field is not applicable enter \&quot;0\&quot;. NISP only. | [optional] |
| **connectivity_ccsd** | [**Array&lt;ConnectivityCcsd&gt;**](ConnectivityCcsd.md) |  | [optional] |

## Example

```ruby
require 'emass_client'

instance = EmassClient::Systems.new(
  registration_completion_date: 1638741770,
  system_life_cycle_acquisition_phase: Pre-Milestone A,
  special_type: Special Type 1,
  special_type_description: Test Special Type Description,
  mission_portfolio: Not Applicable,
  is_nnpi: false,
  is_rbc: false,
  is_waiver: true,
  program_office: Test Program Office,
  vram_id: 12345,
  system_id: 33,
  policy: RMF,
  registration_type: Assess and Authorize,
  name: System XYZ,
  acronym: PM-6,
  description: This is a test system for the eMASS API documentation,
  instance: Navy,
  owning_organization: Defense Information Systems Agency,
  secondary_organization: ID31,
  version_release_no: V1,
  system_type: IS Major Application,
  is_nss: true,
  is_public_facing: true,
  coams_id: 93054,
  is_type_authorization: true,
  ditpr_id: 30498,
  apms_id: 30498,
  vasi_id: 30498,
  authorization_status: Not Yet Authorized,
  authorization_date: 1638741660,
  authorization_termination_date: 1638741660,
  authorization_length: 365,
  security_controls_assessor_executive_summary: Executive Summary of the system&#39;s Security Controls Assessor,
  risk_review_executive_summary: Executive Summary of the system&#39;s Risk Review,
  terms_for_auth: Terms/Conditions to maintain a valid ATO,
  security_plan_approval_status: Approved,
  security_plan_approval_date: 1638741660,
  mission_criticality: Mission Support (MS),
  geographical_association: VA Operated IS,
  system_ownership_controlled: Region 1,
  governing_mission_area: DoD portion of the Intelligence MA (DIMA),
  primary_functional_area: Health/Medical,
  secondary_functional_area: Logistics,
  primary_control_set: NIST SP 800-53 Revision 4,
  confidentiality: Low,
  integrity: Moderate,
  availability: High,
  applied_overlays: Classified Information; Privacy,
  applied_stigs: Active_Directory_Domain,
  rmf_activity: Maintain ATO and conduct reviews,
  cross_domain_ticket: Cross Domain Ticket test,
  ditpr_don_id: 5910, 1234, 8765,
  mac: II,
  dod_confidentiality: Public,
  contingency_plan_required: true,
  contingency_plan_artifact: ContingencyPlanTest.pdf,
  contingency_plan_tested: true,
  contingency_plan_test_date: 1426957321,
  security_review_required: true,
  security_review_completed: true,
  security_review_completion_date: 1531958400,
  next_security_review_due_date: 1526957321,
  has_open_poam_item: true,
  has_open_poam_item90to120_past_scheduled_completion_date: false,
  has_open_poam_item120_plus_past_scheudled_completion_date: false,
  impact: Low,
  has_cui: false,
  has_pii: false,
  has_phi: false,
  ppsm_registration_required: PPSM registration required,
  ppsm_registry_number: Test PPSM Registry Number,
  ppsm_registration_exemption_justification: Exemption justification,
  interconnected_information_system_and_identifiers: Test,
  privacy_impact_assessment_required: true,
  privacy_impact_assessment_status: Not Started,
  privacy_impact_assessment_date: 1622048629,
  privacy_impact_assessment_artifact: PIATest.pdf,
  user_defined_field1: Test User-defined Field 1,
  user_defined_field2: Test User-defined Field 2,
  user_defined_field3: Test User-defined Field 3,
  user_defined_field4: Test User-defined Field 4,
  user_defined_field5: Test User-defined Field 5,
  current_rmf_lifecycle_step: 4 - Assess,
  other_information: Additional Comments,
  reports_for_scorecard: true,
  highest_system_data_classification: Unclassified,
  overall_classification: Unclassified,
  is_hva: true,
  is_financial_management: true,
  is_reciprocity: true,
  reciprocity_exemption: Decommission,
  cloud_computing: false,
  cloud_type: Public,
  authorization_to_connect_status: Decommissioned,
  is_saa_s: true,
  is_paa_s: false,
  is_iaa_s: true,
  other_service_models: Test Other Service,
  need_date: 1638741660,
  overall_risk_score: Moderate,
  is_hrr: false,
  connectivity_authorization_date: 1638741660,
  connectivity_authorization_termination_date: 1638741660,
  system_development_life_cycle: Test Other Service,
  is_fisma_reportable: false,
  group_tagging: Group Tag 1,
  group_tag_descriptions: Group Tag 1 explanation,
  dadms_id: DADMS-1,
  dadms_expiration_date: 1638751730,
  enclave_connectivity: NIPR,
  environment_type: Cloud Computing,
  navy_common_control_provider: false,
  navy_cloud_broker: AWS IL 5,
  cloud_broker_emass_id: 2349,
  cloud_broker_provisional_authorization_atd: 1638741660,
  navy_joint_authorization: false,
  nmci_ngen_clins: NMCI CLIN,
  enterprise_locations: All Navy Networks,
  whitelist_id: DoD DMZ Whitelist,
  whitelist_inventory: Whitelist document,
  acquisition_category: I,
  software_category: Government Off-The-Shelf Software (GOTS),
  cybersecurity_service_provider: NIPR,
  cybersecurity_service_provider_exception_justification: Exception justification,
  maximum_tolerable_downtime: Immediate,
  recovery_time_objective: Mission Critical: 12 hours,
  recovery_point_objective: Mission Critical: 12 hours,
  business_impact_analysis_required: true,
  business_impact_analysis_artifact: BIATest.pdf,
  incident_response_plan_required: true,
  incident_response_plan_artifact: IRPlanTest.pdf,
  disaster_recovery_plan_required: true,
  disaster_recovery_plan_artifact: DRPlanTest.pdf,
  privacy_threshold_analysis_completed: true,
  privacy_threshold_analysis_date: 1715312304,
  privacy_threshold_analysis_artifact: PTATest.pdf,
  privacy_act_system_of_records_notice_required: true,
  e_authentication_risk_assessment_required: true,
  e_authentication_risk_assessment_date: 1715312304,
  e_authentication_risk_assessment_artifact: EAuthRisk.pdf,
  ipv4_only_assets: 10,
  ipv6_only_assets: 5,
  ipv4_ipv6_dual_stack_assets: 15,
  total_ip_assets: 30,
  originating_organization: Originating Organization,
  system_use_justification: System EOL within 120 days,
  system_use_justification_artifact: SystemUseJustification.pdf&quot;,
  authorization_to_use_status: Authority to Use (ATU),
  reciprocity_acceptance_status: Acceptance status content,
  use_authorization_date: 1715312304,
  reciprocity_acceptance_date: 1715312304,
  use_authorization_termination_date: 1715312304,
  reciprocity_acceptance_termination_date: 1715312304,
  terms_conditions_for_use_summary: Test ATU Summary,
  terms_conditions_for_reciprocity_summary: Test ATU Summary,
  primary_mission_essential_function: false,
  pmef_description: Test PMEF Description,
  mission_essential_function: false,
  mef_description: Test MEF Description,
  administration: Test Administration,
  administration_other_justification: Test Administration Justification,
  atc_iatc_granted_date: 1715312304,
  atc_iatc_expiration_date: 1715312304,
  atc_iatc_pending_items: Test ATC/IATC Pending Items,
  pending_items_due_date: 1715312304,
  dodinn_system_id: false,
  authorization_to_use_connect_status: Authorization,
  use_connect_authorization_date: 1715312304,
  use_connect_authorization_termination_date: 1715312304,
  terms_conditions_for_use_connect_summary: Test ATU Summary,
  workstations: 10,
  servers: 5,
  connectivity_ccsd: null
)
```

