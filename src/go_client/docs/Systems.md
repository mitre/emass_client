# Systems

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**RegistrationCompletionDate** | Pointer to **NullableInt32** | [Read-Only] Date the system was registered into eMASS. | [optional] 
**SystemLifeCycleAcquisitionPhase** | Pointer to **NullableString** | [Read-Only] Identifies the current System Acquisition Phase for programs of record. | [optional] 
**SpecialType** | Pointer to **NullableString** | [Read-Only] Lists applicable tracking indicator(s). | [optional] 
**SpecialTypeDescription** | Pointer to **NullableString** | [Read-Only] Provides a brief reason for any tracking indicator(s) selected. | [optional] 
**MissionPortfolio** | Pointer to **NullableString** | [Read-Only] Identifies the appropriate portfolio or capability area. Navy only. | [optional] 
**IsNNPI** | Pointer to **NullableBool** | [Read-Only] Indicates whether Naval Nuclear Propulsion Information (NNPI) is stored, disseminated, or processed through this system. Navy only. | [optional] 
**IsRBC** | Pointer to **NullableBool** | [Read-Only] Indicates whether the system is pursuing an RBC authorization. Navy only. | [optional] 
**IsWaiver** | Pointer to **NullableBool** | [Read-Only] Indicates if the system has a waiver from OPNAV N2N6G (DDCIO(N)) to proceed with a DIACAP accreditation. Navy and DIACAP only. | [optional] 
**ProgramOffice** | Pointer to **NullableString** | [Read-Only] The system record&#39;s Program Office. Navy only. | [optional] 
**VramId** | Pointer to **NullableString** | [Read-Only] Vulnerability Remediation Asset Manager (VRAM) identification number. \&quot;N/A\&quot; indicates the system record is not currently registered in VRAM.  Navy only. | [optional] 
**SystemId** | Pointer to **int64** | [Read-only] Unique system record identifier. | [optional] 
**Policy** | Pointer to **NullableString** | [Read-only] RMF/DIACAP Policy identifier for the system record. | [optional] 
**RegistrationType** | Pointer to **NullableString** | [Read-Only] Registration type of the system record. Values include (assessAndAuthorize, assessOnly, guest, regular, functional, cloudServiceProvider.) | [optional] 
**Name** | Pointer to **NullableString** | [Read-only] Name of the system record. | [optional] 
**Acronym** | Pointer to **NullableString** | [Read-only] Acronym of the system record. | [optional] 
**Description** | Pointer to **NullableString** | [Read-only] Description of the system record. | [optional] 
**Instance** | Pointer to **NullableString** | [Read-Only] Name of the top-level component that owns the system. | [optional] 
**OwningOrganization** | Pointer to **NullableString** | [Read-Only] Owning organization of the system record. Values match the eMASS instance Organizational Hierarchy. | [optional] 
**SecondaryOrganization** | Pointer to **NullableString** | [Read-only] Secondary organization that owns the system record (i.e. Sub-Organization-level. | [optional] 
**VersionReleaseNo** | Pointer to **NullableString** | [Read-only] Version/Release Number of system record. | [optional] 
**SystemType** | Pointer to **NullableString** | [Read-only] Type of the system record. RMF values include the following options (IS Major Application, IS Enclave, Platform IT System). DIACAP values include the following options (Platform IT Interconnection, AIS Application, Outsourced IT-Based Process (DoD-controlled), Enclave, Outsourced IT-Based Process (service provider shared)) | [optional] 
**IsNSS** | Pointer to **NullableBool** | [Read-only] Is the system record a National Security System? | [optional] 
**IsPublicFacing** | Pointer to **NullableBool** | [Read-only] Does the system record have a public facing component/presence. | [optional] 
**CoamsId** | Pointer to **NullableInt64** | [Read-only] Corresponding Cyber Operational Attributes Management System (COAMS) identifier for the system record. | [optional] 
**IsTypeAuthorization** | Pointer to **NullableBool** | [Read-only] Identifies if system is a Type Authorization. | [optional] 
**DitprId** | Pointer to **string** | [Read-only] DITPR ID of the system record. | [optional] 
**ApmsId** | Pointer to **NullableString** | [Read-Only] Same field as ditprId but displays as apmsId for Army only. | [optional] 
**VasiId** | Pointer to **NullableString** | [Read-Only] Same field as ditprId but displays as vasiId for VA only. | [optional] 
**AuthorizationStatus** | Pointer to **NullableString** | [Read-only] Authorization Status of the system record. | [optional] 
**AuthorizationDate** | Pointer to **NullableInt32** | [Read-only] Authorization Date of the system record. | [optional] 
**AuthorizationTerminationDate** | Pointer to **NullableInt32** | [Read-only] Authorization Termination Date of the system record. | [optional] 
**AuthorizationLength** | Pointer to **NullableInt32** | [Read-only] Length of system&#39;s Authorization. Calculated based off of Authorization Date &amp; Authorization Termination Date. | [optional] 
**SecurityControlsAssessorExecutiveSummary** | Pointer to **NullableString** | [Read-Only] Document an assessment of overall cybersecurity risk (Very Low, Low, Moderate, High, Very High) and identify the key drivers for assessment. | [optional] 
**RiskReviewExecutiveSummary** | Pointer to **NullableString** | [Read-Only] Document an assessment of overall cybersecurity risk (Very Low, Low, Moderate, High, Very High) and identify the key drivers for assessment. VA only | [optional] 
**TermsForAuth** | Pointer to **NullableString** | [Read-only] Terms/Conditions for receiving and maintaining the system&#39;s Authorization. Assigned by the Authorizing Official. | [optional] 
**SecurityPlanApprovalStatus** | Pointer to **NullableString** | [Read-only] Status of the approval of the system&#39;s RMF Security Plan. Values include the following options (Approved, Denied, Not Yet Approved). | [optional] 
**SecurityPlanApprovalDate** | Pointer to **NullableInt32** | [Read-only] Approval date of the system&#39;s RMF Security Plan. | [optional] 
**MissionCriticality** | Pointer to **NullableString** | [Read-only] Mission Criticality of the system record. | [optional] 
**GeographicalAssociation** | Pointer to **NullableString** | [Read-only] Geographical Association of the system record. | [optional] 
**SystemOwnershipControlled** | Pointer to **NullableString** | [Read-only] Ownership of the system record. | [optional] 
**GoverningMissionArea** | Pointer to **NullableString** | [Read-only] Governing Mission Area of the system record. | [optional] 
**PrimaryFunctionalArea** | Pointer to **NullableString** | [Read-only] Primary functional area of the system record. | [optional] 
**SecondaryFunctionalArea** | Pointer to **NullableString** | [Read-only] Secondary functional area of the system record. | [optional] 
**PrimaryControlSet** | Pointer to **NullableString** | [Read-only] Primary Control Set of the system record. RMF values include the following options (NIST SP 800-53 Revision 4), DIACAP values include the following options (DoDI 8500.2) | [optional] 
**Confidentiality** | Pointer to **NullableString** | [Read-only] Confidentiality of the system record. RMF values include the following options (High, Moderate, Low) | [optional] 
**Integrity** | Pointer to **NullableString** | [Read-only] Integrity of the system record. RMF values include the following options (High, Moderate, Low) | [optional] 
**Availability** | Pointer to **NullableString** | [Read-only] Availability of the system record. RMF values include the following options (High, Moderate, Low) | [optional] 
**AppliedOverlays** | Pointer to **NullableString** | [Read-only] Overlays applied to the system record. Multiple values are separated by semi-colon &#39;;&#39;. | [optional] 
**AppliedStigs** | Pointer to **NullableString** | [Read-only] The STIG&#39;s applied to the system record. | [optional] 
**RmfActivity** | Pointer to **NullableString** | [Read-only] RMF Activity of the system record. | [optional] 
**CrossDomainTicket** | Pointer to **NullableString** | [Read-only] Cross Domain Tickets of the system record. | [optional] 
**DitprDonId** | Pointer to **NullableString** | [Read-Only] DITPR-DON identifier of the system record. | [optional] 
**Mac** | Pointer to **NullableString** | [Read-Only] MAC level of the system record. | [optional] 
**DodConfidentiality** | Pointer to **NullableString** | [Read-Only] DoD Confidentiality level of the system record. | [optional] 
**ContingencyPlanRequired** | Pointer to **NullableBool** | [Read-Only] Is there a Contingency Plan in place for this system that addresses disruptions in operations? | [optional] 
**ContingencyPlanArtifact** | Pointer to **NullableString** | [Read-Only] Filename of the system&#39;s Contingency Plan artifact. | [optional] 
**ContingencyPlanTested** | Pointer to **NullableBool** | [Read-only] Has the system record&#39;s Contingency Plan been tested? | [optional] 
**ContingencyPlanTestDate** | Pointer to **NullableInt32** | [Read-only] Date the system record&#39;s Contingency Plan was tested. | [optional] 
**SecurityReviewRequired** | Pointer to **NullableBool** | [Read-Only] Is the system required to complete a Security Review? | [optional] 
**SecurityReviewCompleted** | Pointer to **NullableBool** | [Read-Only] Has a Security Review been completed for this system? | [optional] 
**SecurityReviewCompletionDate** | Pointer to **NullableInt32** | [Read-Only] Date of the system&#39;s latest security review or annual assessment. | [optional] 
**NextSecurityReviewDueDate** | Pointer to **NullableInt32** | [Read-Only] Date when the system&#39;s next security review or annual assessment is due by. | [optional] 
**HasOpenPoamItem** | Pointer to **NullableBool** | [Read-Only] Does the system record have an Ongoing or Risk Accepted POA&amp;M Item? | [optional] 
**HasOpenPoamItem90to120PastScheduledCompletionDate** | Pointer to **NullableBool** | [Read-Only] Does the system record have an Ongoing or Risk Accepted POA&amp;M Item 90 to 120 days past its Scheduled Completion Date? | [optional] 
**HasOpenPoamItem120PlusPastScheudledCompletionDate** | Pointer to **NullableBool** | [Read-Only] Does the system record have an Ongoing or Risk Accepted POA&amp;M Item 120 days past its Scheduled Completion Date? | [optional] 
**Impact** | Pointer to **NullableString** | [Optional] Values include the following options (Very Low, Low, Moderate,High,Very High) | [optional] 
**HasCUI** | Pointer to **NullableBool** | [Read-only] Does the system record contain and/or process Controlled Unclassified information? | [optional] 
**HasPII** | Pointer to **NullableBool** | [Read-only] Does the system record contain and/or process Personally Identifiable Information? | [optional] 
**HasPHI** | Pointer to **NullableBool** | [Read-only] Does the system record contain and/or process Personal Health Information? | [optional] 
**PpsmRegistrationRequired** | Pointer to **NullableString** | [Read-Only] Determine if a PPSM registration is required. | [optional] 
**PpsmRegistryNumber** | Pointer to **NullableString** | [Read-only] Unique identifier for the DoD&#39;s Ports, Protocols, and Services Management Registry system. | [optional] 
**PpsmRegistrationExemptionJustification** | Pointer to **NullableString** | [Read-Only] Clarify why a PPSM registraiton is not necessary. | [optional] 
**InterconnectedInformationSystemAndIdentifiers** | Pointer to **NullableString** | [Read-only] Identify the interconnected information systems and corresponding identifiers within control CA-3. | [optional] 
**PrivacyImpactAssessmentRequired** | Pointer to **NullableBool** | [Read-only] Does the system require a Privacy Impact Assessment? | [optional] 
**PrivacyImpactAssessmentStatus** | Pointer to **NullableString** | [Read-only] Status of the PIA, availability values include the following options (Not Started, In Progress, Completed) | [optional] 
**PrivacyImpactAssessmentDate** | Pointer to **NullableInt32** | [Read-only] Date in which the system&#39;s PIA took place. | [optional] 
**PrivacyImpactAssessmentArtifact** | Pointer to **NullableString** | [Read-Only] Filename of the system&#39;s PIA artifact. | [optional] 
**UserDefinedField1** | Pointer to **NullableString** | [Read-only] User-defined field to augment Ad Hoc Reporting. | [optional] 
**UserDefinedField2** | Pointer to **NullableString** | [Read-only] User-defined field to augment Ad Hoc Reporting. | [optional] 
**UserDefinedField3** | Pointer to **NullableString** | [Read-only] User-defined field to augment Ad Hoc Reporting. | [optional] 
**UserDefinedField4** | Pointer to **NullableString** | [Read-only] User-defined field to augment Ad Hoc Reporting. | [optional] 
**UserDefinedField5** | Pointer to **NullableString** | [Read-only] User-defined field to augment Ad Hoc Reporting. | [optional] 
**CurrentRmfLifecycleStep** | Pointer to **NullableString** | [Read-only] Displays the system&#39;s current step within the RMF Lifecycle. | [optional] 
**OtherInformation** | Pointer to **NullableString** | [Read-only] Include any additional information required by the organization. | [optional] 
**ReportsForScorecard** | Pointer to **NullableBool** | [Read-only] Indicates if the system reports to the DoD Cyber Hygiene Scorecard. | [optional] 
**HighestSystemDataClassification** | Pointer to **NullableString** | [Read-Only] The overall classification level of information that the System is approved to collect, process, store, and/or distribute. | [optional] 
**OverallClassification** | Pointer to **NullableString** | [Read-Only] Same field as highestSystemDataClassification, but displays as overallClassification for NISP only. | [optional] 
**IsHVA** | Pointer to **NullableBool** | [Read-Only] Indicates if the system contains High Value Assets. Does not display if value is null | [optional] 
**IsFinancialManagement** | Pointer to **NullableBool** | [Read-Only] Per OMB Circular A-127, a financial management system includes the core financial systems and the financial portions of mixed systems necessary to support financial management, including automated and manual processes, procedures, and controls, data, hardware, software, and support personnel dedicated to the operation and maintenance of system functions. The following are examples of financial management systems: core financial systems, procurement systems, loan systems, grants systems, payroll systems, budget formulation systems, billing systems, and travel systems.  | [optional] 
**IsReciprocity** | Pointer to **NullableBool** | [Read-Only] A reciprocity system is any information system that is part of a mutual agreement among participating organizations to accept each other&#39;s security assessments in order to reuse information system resources and/or to accept each other&#39;s assessed security posture in order to share information.  | [optional] 
**ReciprocityExemption** | Pointer to **NullableString** | [Read-Only] The following justifications are acceptable for exemption from reciprocity: (a) the existence of the system is classified (not the data, but the existence of the system) or (b) the system&#39;s authorization to operate is in the process of being pulled (e.g. DATO, Decommission).  | [optional] 
**CloudComputing** | Pointer to **NullableBool** | [Read-Only] Is this a cloud-based IS? | [optional] 
**CloudType** | Pointer to **NullableString** | [Read-Only] Values include the following: (Hybrid, Private, Public) | [optional] 
**AuthorizationToConnectStatus** | Pointer to **NullableString** | [Read-Only] The Authority to Connect decision. Values include the following: (Authority to Connect (ATC), Denial of Authority to Connect (DATC), Not Yet Connected, Decommissioned)  | [optional] 
**IsSaaS** | Pointer to **NullableBool** | [Read-Only] Software as a Service (SaaS) cloud service model. | [optional] 
**IsPaaS** | Pointer to **NullableBool** | [Read-Only] Platform as a Service (PaaS) cloud service model. | [optional] 
**IsIaaS** | Pointer to **NullableBool** | [Read-Only] Infrastructure as a Service (IaaS) cloud service model. | [optional] 
**OtherServiceModels** | Pointer to **NullableString** | [Read-Only] Free text field to include other cloud service models. | [optional] 
**NeedDate** | Pointer to **NullableInt32** | [Read-Only] Indicates the date by which the System needs to be deployed to a production environment. | [optional] 
**OverallRiskScore** | Pointer to **NullableString** | [Read-Only] The overall risk score of the system | [optional] 
**IsHRR** | Pointer to **NullableBool** | [Read-Only] Identifies whether a System has been designated as High Risk Review. USCG and Navy only. | [optional] 
**ConnectivityAuthorizationDate** | Pointer to **NullableInt32** | [Read-Only] The Connectivity Authorization Date. | [optional] 
**ConnectivityAuthorizationTerminationDate** | Pointer to **NullableInt32** | [Read-Only] The Connectivity Authorization Termination Date. | [optional] 
**SystemDevelopmentLifeCycle** | Pointer to **NullableString** | [Read-Only] Indicate the date by which the System needs to be deployed to a production environment. VA only. | [optional] 
**IsFISMAReportable** | Pointer to **NullableBool** | [Read-Only] Is this IS reportable per Federal Information Security Management Act (FISMA) established requirements? VA only | [optional] 
**GroupTagging** | Pointer to **NullableString** | [Read-Only] System Tags for enterprise level, to include CIO and CISO, tracking efforts. VA only. | [optional] 
**GroupTagDescriptions** | Pointer to **NullableString** | [Read-Only] System Tag explanation(s) for enterprise level, to include CIO and CISO, tracking efforts. VA only. | [optional] 
**DadmsId** | Pointer to **NullableString** | [Read-Only] The system&#39;s DADMS ID. USMC only. | [optional] 
**DadmsExpirationDate** | Pointer to **NullableInt32** | [Read-Only] Date the system expires in DADMS. USMC only. | [optional] 
**EnclaveConnectivity** | Pointer to **NullableString** | [Read-Only] Identify the type of connectivity for the network/enclave, e.g., DISA circuit (NIPR, SIPR) or HPCMP circuit (DREN, SDREN, Outreach). Navy only. | [optional] 
**EnvironmentType** | Pointer to **NullableString** | [Read-Only] Identify the primary computing environment for where the information system is deployed. Navy only. | [optional] 
**NavyCommonControlProvider** | Pointer to **NullableBool** | [Read-Only] Indicate whether the information system provides inheritable controls. Navy only | [optional] 
**NavyCloudBroker** | Pointer to **NullableString** | [Read-Only] Identify the broker responsible for the delivery of commercial cloud services and capabilities. Refer to Navy Commercial Cloud Brokerage Policy. Navy Only | [optional] 
**CloudBrokerEmassId** | Pointer to **NullableInt32** | [Read-Only] The eMASS ID of the identified cloud broker. Navy only. | [optional] 
**CloudBrokerProvisionalAuthorizationAtd** | Pointer to **NullableInt32** | [Read-Only] The provisional authorization termination date of the identified cloud broker. Navy only | [optional] 
**NavyJointAuthorization** | Pointer to **NullableBool** | [Read-Only] Indicate whether this is a joint authorization being issued by two or more Authorizing Officials. Navy only | [optional] 
**NmciNgenClins** | Pointer to **NullableString** | [Read-Only] Provide all NMCI CLINs associated to the system/services within the authorization boundary. Navy only | [optional] 
**EnterpriseLocations** | Pointer to **NullableString** | [Read-Only] Identify the Navy enterprise network where the information system is deployed. Navy only | [optional] 
**WhitelistId** | Pointer to **NullableString** | [Read-Only] Systems that have public-facing components/presences are typically required to be documented and registered as part of Organzationally-approved whitelisting processes. | [optional] 
**WhitelistInventory** | Pointer to **NullableString** | [Read-Only] Provide/upload the documentation that identifies or describes the components or aspects of the System that are public-facing (whitelisted). | [optional] 
**AcquisitionCategory** | Pointer to **NullableString** | [Read-Only] Values include the following options (I,II,III) | [optional] 
**SoftwareCategory** | Pointer to **NullableString** | [Read-Only] Lists the software category. | [optional] 
**CybersecurityServiceProvider** | Pointer to **NullableString** | [Read-Only] Name of the system&#39;s Cybersecurity Service Provider. | [optional] 
**CybersecurityServiceProviderExceptionJustification** | Pointer to **NullableString** | [Read-Only] If Not Applicable, provide the exception justification. | [optional] 
**MaximumTolerableDowntime** | Pointer to **NullableString** | [Read-Only] MTD represents the total amount of time leaders/managers are willing to accept for a process outage or disruption. | [optional] 
**RecoveryTimeObjective** | Pointer to **NullableString** | [Read-Only] RTO defines the maximum amount of time a system can remain unavailable before there is an unacceptable impact on other systems, supported business processes, and the MTD. | [optional] 
**RecoveryPointObjective** | Pointer to **NullableString** | [Read-Only] RPO represents the point in time, prior to a disruption or system outage, to which mission/business data can be recovered (given the most recent backup copy of the data) after an outage. The system data/information owner determines an acceptable RPO in terms of amount of tolerable data loss before unacceptable impact occurs. | [optional] 
**BusinessImpactAnalysisRequired** | Pointer to **NullableBool** | [Read-Only] Is a Business Impact Analysis in place that identifies critical business processes, MTD, RTO, and RPO? | [optional] 
**BusinessImpactAnalysisArtifact** | Pointer to **NullableString** | [Read-Only] Filename of the system&#39;s Business Impact Analysis artifact. | [optional] 
**IncidentResponsePlanRequired** | Pointer to **NullableBool** | [Read-Only] Is there a Incident Response Plan in place for this system that provides the roadmap for implementing the incident response capability? | [optional] 
**IncidentResponsePlanArtifact** | Pointer to **NullableString** | [Read-Only] Filename of the system&#39;s Incident Response Plan artifact. | [optional] 
**DisasterRecoveryPlanRequired** | Pointer to **NullableBool** | [Read-Only] Is there a Disaster Recovery Plan in place for this system that addresses information system disruptions that require relocation? | [optional] 
**DisasterRecoveryPlanArtifact** | Pointer to **NullableString** | [Read-Only] Filename of the system&#39;s Disaster Recovery Plan artifact. | [optional] 
**PrivacyThresholdAnalysisCompleted** | Pointer to **NullableBool** | [Read-Only] Indicate whether a Privacy Threshold Analysis (PTA) has been performed for this IS. | [optional] 
**PrivacyThresholdAnalysisDate** | Pointer to **NullableInt32** | [Read-Only] Date in which this sytem&#39;s Privacy Threshold Analysis took place. | [optional] 
**PrivacyThresholdAnalysisArtifact** | Pointer to **NullableString** | [Read-Only] Filename of the system&#39;s Privacy Threshold Analysis artifact. | [optional] 
**PrivacyActSystemOfRecordsNoticeRequired** | Pointer to **NullableBool** | [Read-Only] Does this system require a Privacy Act System of Record Notice per DoD 5400.11-R? | [optional] 
**EAuthenticationRiskAssessmentRequired** | Pointer to **NullableBool** | [Read-Only] Indicate whether an E-Authentication Risk Assessment has been performed for the system in accordance with OMB M-04-04. | [optional] 
**EAuthenticationRiskAssessmentDate** | Pointer to **NullableInt32** | [Read-Only] Date this system&#39;s EAuthentication Risk Assessment took place. | [optional] 
**EAuthenticationRiskAssessmentArtifact** | Pointer to **NullableString** | [Read-Only] Filename of the system&#39;s Privacy Threshold Analysis artifact. | [optional] 
**Ipv4OnlyAssets** | Pointer to **NullableInt32** | [Read-Only] Identify the total number of assets associated with this boundary that are only on IPv4. | [optional] 
**Ipv6OnlyAssets** | Pointer to **NullableInt32** | [Read-Only] Identify the total number of assets associated with this boundary that are only on IPv6. | [optional] 
**Ipv4Ipv6DualStackAssets** | Pointer to **NullableInt32** | [Read-Only] Identify the total number of assets associated with this boundary that are operating on IPv4/IPv6 dual-stack. | [optional] 
**TotalIpAssets** | Pointer to **NullableInt32** | [Read-Only] Total number of IPv4, IPv6, and dual-stack assets identified. Value calculated upon Save action | [optional] 
**OriginatingOrganization** | Pointer to **NullableString** | [Read-Only] Identify the organization that generated the existing authorization package, including (where applicable) individual points of contact. | [optional] 
**SystemUseJustification** | Pointer to **NullableString** | [Read-Only] Provide a detailed justification as to why this system should be deployed and used within the requesting organization. | [optional] 
**SystemUseJustificationArtifact** | Pointer to **NullableString** | [Read-Only] Filename of the System Use Justification Artifact, including the file extension. | [optional] 
**AuthorizationToUseStatus** | Pointer to **NullableString** | [Read-Only] The system&#39;s Authority to Use Status. | [optional] 
**ReciprocityAcceptanceStatus** | Pointer to **NullableString** | [Read-Only] The system&#39;s Reciprocity Acceptance Status. Army IC only. | [optional] 
**UseAuthorizationDate** | Pointer to **NullableInt32** | [Read-Only] The system&#39;s Use Authorization Date. | [optional] 
**ReciprocityAcceptanceDate** | Pointer to **NullableInt32** | [Read-Only] The system&#39;s Reciprocity Acceptance Date. Army IC only. | [optional] 
**UseAuthorizationTerminationDate** | Pointer to **NullableInt32** | [Read-Only] The system&#39;s Use Authorization Termination Date. | [optional] 
**ReciprocityAcceptanceTerminationDate** | Pointer to **NullableInt32** | [Read-Only] The system&#39;s Reciprocity Acceptance Termination Date. Army IC only. | [optional] 
**TermsConditionsForUseSummary** | Pointer to **NullableString** | [Read-Only] The system&#39;s Terms / Conditions for Use Summary. | [optional] 
**TermsConditionsForReciprocitySummary** | Pointer to **NullableString** | [Read-Only] The system&#39;s Terms / Conditions for Reciprocity Summary. Army IC only. | [optional] 
**PrimaryMissionEssentialFunction** | Pointer to **NullableBool** | [Read-Only] Annotate &#39;Yes&#39; if your system performs a Primary Mission Essential Function. VA only | [optional] 
**PmefDescription** | Pointer to **NullableString** | [Read-Only] The FIPS category \&quot;Availability\&quot; of this system must be marked \&quot;High\&quot; if the system is listed as a PMEF, and the RTO must be 12 hours or shorter. VA only | [optional] 
**MissionEssentialFunction** | Pointer to **NullableBool** | [Read-Only] Annotate \&quot;Yes\&quot; if your system performs a Mission Essential Function. VA only. | [optional] 
**MefDescription** | Pointer to **NullableString** | [Read-Only] MEFs are listed in the OIT Continuity Plan. VA Handbook 0322 will be updated with these MEFs. VA only. | [optional] 
**Administration** | Pointer to **NullableString** | [Read-Only] Identify the administration that this information system supports. VA only. | [optional] 
**AdministrationOtherJustification** | Pointer to **NullableString** | [Read-Only] If the Administration field is set to \&quot;Other\&quot;, this free-text field becomes required. VA only. | [optional] 
**AtcIatcGrantedDate** | Pointer to **NullableInt32** | [Read-Only] The date the Authority to Connect (ATC) or Interim Authority to Connect (IATC) was granted. | [optional] 
**AtcIatcExpirationDate** | Pointer to **NullableInt32** | [Read-Only] The date the Authority to Connect (ATC) or Interim Authority to Connect (IATC) expires. | [optional] 
**AtcIatcPendingItems** | Pointer to **NullableString** | [Read-Only] List of pending items required for the Authority to Connect (ATC) or Interim Authority to Connect (IATC). | [optional] 
**PendingItemsDueDate** | Pointer to **NullableInt32** | [Read-Only] The date the pending items are due. | [optional] 
**DodinnSystemId** | Pointer to **NullableBool** | [Read-Only] A DoDIN-N system is all encompassing for the following: Navy networks, systems, sites, corporate assets, centrally managed programs, programs of record, standalone, excepted, enterprise, non-enterprise, cloud, NIPRNET, SIPRNET, GENSER Classified, Defense Research Engineering Network (DREN), Secret DREN (SDREN), connected to the DoDIN or through commercial lines that are owned, operated, leased, contracted, maintained, managed, administered, house Navy data, house Navy personally identifiable information, house Navy protected health information, or controlled unclassified information. The DoDIN-N also includes commercial information technology, weapons systems/program manager/program of record/platform information technology, and operational technology. Navy only. | [optional] 
**AuthorizationToUseConnectStatus** | Pointer to **NullableString** | [Read-Only] FCC CRMA/NAO approval for DoDIN-N operations. Navy only. | [optional] 
**UseConnectAuthorizationDate** | Pointer to **NullableInt32** | [Read-Only] The Use/Connect Authorization Date. Navy only. | [optional] 
**UseConnectAuthorizationTerminationDate** | Pointer to **NullableInt32** | [Read-Only] The Use/Connect Authorization Termination Date Navy only. | [optional] 
**TermsConditionsForUseConnectSummary** | Pointer to **NullableString** | [Read-Only] Provide a description (if applicable) of any specific limitations or restrictions placed on the operation of the information system as part of the authorization to use/connect decision. Navy only. | [optional] 
**Workstations** | Pointer to **NullableInt32** | [Read-Only] Identify the number of System Workstations. This data will be used for the National Industrial Security System (NISS) facility categorization. If field is not applicable enter \&quot;0\&quot;. NISP only. | [optional] 
**Servers** | Pointer to **NullableInt32** | [Read-Only] Identify the number of System Servers. This data will be used for the National Industrial Security System (NISS) facility categorization. If field is not applicable enter \&quot;0\&quot;. NISP only. | [optional] 
**ConnectivityCcsd** | Pointer to [**[]ConnectivityCcsd**](ConnectivityCcsd.md) |  | [optional] 

## Methods

### NewSystems

`func NewSystems() *Systems`

NewSystems instantiates a new Systems object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSystemsWithDefaults

`func NewSystemsWithDefaults() *Systems`

NewSystemsWithDefaults instantiates a new Systems object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetRegistrationCompletionDate

`func (o *Systems) GetRegistrationCompletionDate() int32`

GetRegistrationCompletionDate returns the RegistrationCompletionDate field if non-nil, zero value otherwise.

### GetRegistrationCompletionDateOk

`func (o *Systems) GetRegistrationCompletionDateOk() (*int32, bool)`

GetRegistrationCompletionDateOk returns a tuple with the RegistrationCompletionDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRegistrationCompletionDate

`func (o *Systems) SetRegistrationCompletionDate(v int32)`

SetRegistrationCompletionDate sets RegistrationCompletionDate field to given value.

### HasRegistrationCompletionDate

`func (o *Systems) HasRegistrationCompletionDate() bool`

HasRegistrationCompletionDate returns a boolean if a field has been set.

### SetRegistrationCompletionDateNil

`func (o *Systems) SetRegistrationCompletionDateNil(b bool)`

 SetRegistrationCompletionDateNil sets the value for RegistrationCompletionDate to be an explicit nil

### UnsetRegistrationCompletionDate
`func (o *Systems) UnsetRegistrationCompletionDate()`

UnsetRegistrationCompletionDate ensures that no value is present for RegistrationCompletionDate, not even an explicit nil
### GetSystemLifeCycleAcquisitionPhase

`func (o *Systems) GetSystemLifeCycleAcquisitionPhase() string`

GetSystemLifeCycleAcquisitionPhase returns the SystemLifeCycleAcquisitionPhase field if non-nil, zero value otherwise.

### GetSystemLifeCycleAcquisitionPhaseOk

`func (o *Systems) GetSystemLifeCycleAcquisitionPhaseOk() (*string, bool)`

GetSystemLifeCycleAcquisitionPhaseOk returns a tuple with the SystemLifeCycleAcquisitionPhase field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSystemLifeCycleAcquisitionPhase

`func (o *Systems) SetSystemLifeCycleAcquisitionPhase(v string)`

SetSystemLifeCycleAcquisitionPhase sets SystemLifeCycleAcquisitionPhase field to given value.

### HasSystemLifeCycleAcquisitionPhase

`func (o *Systems) HasSystemLifeCycleAcquisitionPhase() bool`

HasSystemLifeCycleAcquisitionPhase returns a boolean if a field has been set.

### SetSystemLifeCycleAcquisitionPhaseNil

`func (o *Systems) SetSystemLifeCycleAcquisitionPhaseNil(b bool)`

 SetSystemLifeCycleAcquisitionPhaseNil sets the value for SystemLifeCycleAcquisitionPhase to be an explicit nil

### UnsetSystemLifeCycleAcquisitionPhase
`func (o *Systems) UnsetSystemLifeCycleAcquisitionPhase()`

UnsetSystemLifeCycleAcquisitionPhase ensures that no value is present for SystemLifeCycleAcquisitionPhase, not even an explicit nil
### GetSpecialType

`func (o *Systems) GetSpecialType() string`

GetSpecialType returns the SpecialType field if non-nil, zero value otherwise.

### GetSpecialTypeOk

`func (o *Systems) GetSpecialTypeOk() (*string, bool)`

GetSpecialTypeOk returns a tuple with the SpecialType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSpecialType

`func (o *Systems) SetSpecialType(v string)`

SetSpecialType sets SpecialType field to given value.

### HasSpecialType

`func (o *Systems) HasSpecialType() bool`

HasSpecialType returns a boolean if a field has been set.

### SetSpecialTypeNil

`func (o *Systems) SetSpecialTypeNil(b bool)`

 SetSpecialTypeNil sets the value for SpecialType to be an explicit nil

### UnsetSpecialType
`func (o *Systems) UnsetSpecialType()`

UnsetSpecialType ensures that no value is present for SpecialType, not even an explicit nil
### GetSpecialTypeDescription

`func (o *Systems) GetSpecialTypeDescription() string`

GetSpecialTypeDescription returns the SpecialTypeDescription field if non-nil, zero value otherwise.

### GetSpecialTypeDescriptionOk

`func (o *Systems) GetSpecialTypeDescriptionOk() (*string, bool)`

GetSpecialTypeDescriptionOk returns a tuple with the SpecialTypeDescription field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSpecialTypeDescription

`func (o *Systems) SetSpecialTypeDescription(v string)`

SetSpecialTypeDescription sets SpecialTypeDescription field to given value.

### HasSpecialTypeDescription

`func (o *Systems) HasSpecialTypeDescription() bool`

HasSpecialTypeDescription returns a boolean if a field has been set.

### SetSpecialTypeDescriptionNil

`func (o *Systems) SetSpecialTypeDescriptionNil(b bool)`

 SetSpecialTypeDescriptionNil sets the value for SpecialTypeDescription to be an explicit nil

### UnsetSpecialTypeDescription
`func (o *Systems) UnsetSpecialTypeDescription()`

UnsetSpecialTypeDescription ensures that no value is present for SpecialTypeDescription, not even an explicit nil
### GetMissionPortfolio

`func (o *Systems) GetMissionPortfolio() string`

GetMissionPortfolio returns the MissionPortfolio field if non-nil, zero value otherwise.

### GetMissionPortfolioOk

`func (o *Systems) GetMissionPortfolioOk() (*string, bool)`

GetMissionPortfolioOk returns a tuple with the MissionPortfolio field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMissionPortfolio

`func (o *Systems) SetMissionPortfolio(v string)`

SetMissionPortfolio sets MissionPortfolio field to given value.

### HasMissionPortfolio

`func (o *Systems) HasMissionPortfolio() bool`

HasMissionPortfolio returns a boolean if a field has been set.

### SetMissionPortfolioNil

`func (o *Systems) SetMissionPortfolioNil(b bool)`

 SetMissionPortfolioNil sets the value for MissionPortfolio to be an explicit nil

### UnsetMissionPortfolio
`func (o *Systems) UnsetMissionPortfolio()`

UnsetMissionPortfolio ensures that no value is present for MissionPortfolio, not even an explicit nil
### GetIsNNPI

`func (o *Systems) GetIsNNPI() bool`

GetIsNNPI returns the IsNNPI field if non-nil, zero value otherwise.

### GetIsNNPIOk

`func (o *Systems) GetIsNNPIOk() (*bool, bool)`

GetIsNNPIOk returns a tuple with the IsNNPI field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsNNPI

`func (o *Systems) SetIsNNPI(v bool)`

SetIsNNPI sets IsNNPI field to given value.

### HasIsNNPI

`func (o *Systems) HasIsNNPI() bool`

HasIsNNPI returns a boolean if a field has been set.

### SetIsNNPINil

`func (o *Systems) SetIsNNPINil(b bool)`

 SetIsNNPINil sets the value for IsNNPI to be an explicit nil

### UnsetIsNNPI
`func (o *Systems) UnsetIsNNPI()`

UnsetIsNNPI ensures that no value is present for IsNNPI, not even an explicit nil
### GetIsRBC

`func (o *Systems) GetIsRBC() bool`

GetIsRBC returns the IsRBC field if non-nil, zero value otherwise.

### GetIsRBCOk

`func (o *Systems) GetIsRBCOk() (*bool, bool)`

GetIsRBCOk returns a tuple with the IsRBC field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsRBC

`func (o *Systems) SetIsRBC(v bool)`

SetIsRBC sets IsRBC field to given value.

### HasIsRBC

`func (o *Systems) HasIsRBC() bool`

HasIsRBC returns a boolean if a field has been set.

### SetIsRBCNil

`func (o *Systems) SetIsRBCNil(b bool)`

 SetIsRBCNil sets the value for IsRBC to be an explicit nil

### UnsetIsRBC
`func (o *Systems) UnsetIsRBC()`

UnsetIsRBC ensures that no value is present for IsRBC, not even an explicit nil
### GetIsWaiver

`func (o *Systems) GetIsWaiver() bool`

GetIsWaiver returns the IsWaiver field if non-nil, zero value otherwise.

### GetIsWaiverOk

`func (o *Systems) GetIsWaiverOk() (*bool, bool)`

GetIsWaiverOk returns a tuple with the IsWaiver field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsWaiver

`func (o *Systems) SetIsWaiver(v bool)`

SetIsWaiver sets IsWaiver field to given value.

### HasIsWaiver

`func (o *Systems) HasIsWaiver() bool`

HasIsWaiver returns a boolean if a field has been set.

### SetIsWaiverNil

`func (o *Systems) SetIsWaiverNil(b bool)`

 SetIsWaiverNil sets the value for IsWaiver to be an explicit nil

### UnsetIsWaiver
`func (o *Systems) UnsetIsWaiver()`

UnsetIsWaiver ensures that no value is present for IsWaiver, not even an explicit nil
### GetProgramOffice

`func (o *Systems) GetProgramOffice() string`

GetProgramOffice returns the ProgramOffice field if non-nil, zero value otherwise.

### GetProgramOfficeOk

`func (o *Systems) GetProgramOfficeOk() (*string, bool)`

GetProgramOfficeOk returns a tuple with the ProgramOffice field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProgramOffice

`func (o *Systems) SetProgramOffice(v string)`

SetProgramOffice sets ProgramOffice field to given value.

### HasProgramOffice

`func (o *Systems) HasProgramOffice() bool`

HasProgramOffice returns a boolean if a field has been set.

### SetProgramOfficeNil

`func (o *Systems) SetProgramOfficeNil(b bool)`

 SetProgramOfficeNil sets the value for ProgramOffice to be an explicit nil

### UnsetProgramOffice
`func (o *Systems) UnsetProgramOffice()`

UnsetProgramOffice ensures that no value is present for ProgramOffice, not even an explicit nil
### GetVramId

`func (o *Systems) GetVramId() string`

GetVramId returns the VramId field if non-nil, zero value otherwise.

### GetVramIdOk

`func (o *Systems) GetVramIdOk() (*string, bool)`

GetVramIdOk returns a tuple with the VramId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVramId

`func (o *Systems) SetVramId(v string)`

SetVramId sets VramId field to given value.

### HasVramId

`func (o *Systems) HasVramId() bool`

HasVramId returns a boolean if a field has been set.

### SetVramIdNil

`func (o *Systems) SetVramIdNil(b bool)`

 SetVramIdNil sets the value for VramId to be an explicit nil

### UnsetVramId
`func (o *Systems) UnsetVramId()`

UnsetVramId ensures that no value is present for VramId, not even an explicit nil
### GetSystemId

`func (o *Systems) GetSystemId() int64`

GetSystemId returns the SystemId field if non-nil, zero value otherwise.

### GetSystemIdOk

`func (o *Systems) GetSystemIdOk() (*int64, bool)`

GetSystemIdOk returns a tuple with the SystemId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSystemId

`func (o *Systems) SetSystemId(v int64)`

SetSystemId sets SystemId field to given value.

### HasSystemId

`func (o *Systems) HasSystemId() bool`

HasSystemId returns a boolean if a field has been set.

### GetPolicy

`func (o *Systems) GetPolicy() string`

GetPolicy returns the Policy field if non-nil, zero value otherwise.

### GetPolicyOk

`func (o *Systems) GetPolicyOk() (*string, bool)`

GetPolicyOk returns a tuple with the Policy field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPolicy

`func (o *Systems) SetPolicy(v string)`

SetPolicy sets Policy field to given value.

### HasPolicy

`func (o *Systems) HasPolicy() bool`

HasPolicy returns a boolean if a field has been set.

### SetPolicyNil

`func (o *Systems) SetPolicyNil(b bool)`

 SetPolicyNil sets the value for Policy to be an explicit nil

### UnsetPolicy
`func (o *Systems) UnsetPolicy()`

UnsetPolicy ensures that no value is present for Policy, not even an explicit nil
### GetRegistrationType

`func (o *Systems) GetRegistrationType() string`

GetRegistrationType returns the RegistrationType field if non-nil, zero value otherwise.

### GetRegistrationTypeOk

`func (o *Systems) GetRegistrationTypeOk() (*string, bool)`

GetRegistrationTypeOk returns a tuple with the RegistrationType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRegistrationType

`func (o *Systems) SetRegistrationType(v string)`

SetRegistrationType sets RegistrationType field to given value.

### HasRegistrationType

`func (o *Systems) HasRegistrationType() bool`

HasRegistrationType returns a boolean if a field has been set.

### SetRegistrationTypeNil

`func (o *Systems) SetRegistrationTypeNil(b bool)`

 SetRegistrationTypeNil sets the value for RegistrationType to be an explicit nil

### UnsetRegistrationType
`func (o *Systems) UnsetRegistrationType()`

UnsetRegistrationType ensures that no value is present for RegistrationType, not even an explicit nil
### GetName

`func (o *Systems) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *Systems) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *Systems) SetName(v string)`

SetName sets Name field to given value.

### HasName

`func (o *Systems) HasName() bool`

HasName returns a boolean if a field has been set.

### SetNameNil

`func (o *Systems) SetNameNil(b bool)`

 SetNameNil sets the value for Name to be an explicit nil

### UnsetName
`func (o *Systems) UnsetName()`

UnsetName ensures that no value is present for Name, not even an explicit nil
### GetAcronym

`func (o *Systems) GetAcronym() string`

GetAcronym returns the Acronym field if non-nil, zero value otherwise.

### GetAcronymOk

`func (o *Systems) GetAcronymOk() (*string, bool)`

GetAcronymOk returns a tuple with the Acronym field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAcronym

`func (o *Systems) SetAcronym(v string)`

SetAcronym sets Acronym field to given value.

### HasAcronym

`func (o *Systems) HasAcronym() bool`

HasAcronym returns a boolean if a field has been set.

### SetAcronymNil

`func (o *Systems) SetAcronymNil(b bool)`

 SetAcronymNil sets the value for Acronym to be an explicit nil

### UnsetAcronym
`func (o *Systems) UnsetAcronym()`

UnsetAcronym ensures that no value is present for Acronym, not even an explicit nil
### GetDescription

`func (o *Systems) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *Systems) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *Systems) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *Systems) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### SetDescriptionNil

`func (o *Systems) SetDescriptionNil(b bool)`

 SetDescriptionNil sets the value for Description to be an explicit nil

### UnsetDescription
`func (o *Systems) UnsetDescription()`

UnsetDescription ensures that no value is present for Description, not even an explicit nil
### GetInstance

`func (o *Systems) GetInstance() string`

GetInstance returns the Instance field if non-nil, zero value otherwise.

### GetInstanceOk

`func (o *Systems) GetInstanceOk() (*string, bool)`

GetInstanceOk returns a tuple with the Instance field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetInstance

`func (o *Systems) SetInstance(v string)`

SetInstance sets Instance field to given value.

### HasInstance

`func (o *Systems) HasInstance() bool`

HasInstance returns a boolean if a field has been set.

### SetInstanceNil

`func (o *Systems) SetInstanceNil(b bool)`

 SetInstanceNil sets the value for Instance to be an explicit nil

### UnsetInstance
`func (o *Systems) UnsetInstance()`

UnsetInstance ensures that no value is present for Instance, not even an explicit nil
### GetOwningOrganization

`func (o *Systems) GetOwningOrganization() string`

GetOwningOrganization returns the OwningOrganization field if non-nil, zero value otherwise.

### GetOwningOrganizationOk

`func (o *Systems) GetOwningOrganizationOk() (*string, bool)`

GetOwningOrganizationOk returns a tuple with the OwningOrganization field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOwningOrganization

`func (o *Systems) SetOwningOrganization(v string)`

SetOwningOrganization sets OwningOrganization field to given value.

### HasOwningOrganization

`func (o *Systems) HasOwningOrganization() bool`

HasOwningOrganization returns a boolean if a field has been set.

### SetOwningOrganizationNil

`func (o *Systems) SetOwningOrganizationNil(b bool)`

 SetOwningOrganizationNil sets the value for OwningOrganization to be an explicit nil

### UnsetOwningOrganization
`func (o *Systems) UnsetOwningOrganization()`

UnsetOwningOrganization ensures that no value is present for OwningOrganization, not even an explicit nil
### GetSecondaryOrganization

`func (o *Systems) GetSecondaryOrganization() string`

GetSecondaryOrganization returns the SecondaryOrganization field if non-nil, zero value otherwise.

### GetSecondaryOrganizationOk

`func (o *Systems) GetSecondaryOrganizationOk() (*string, bool)`

GetSecondaryOrganizationOk returns a tuple with the SecondaryOrganization field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSecondaryOrganization

`func (o *Systems) SetSecondaryOrganization(v string)`

SetSecondaryOrganization sets SecondaryOrganization field to given value.

### HasSecondaryOrganization

`func (o *Systems) HasSecondaryOrganization() bool`

HasSecondaryOrganization returns a boolean if a field has been set.

### SetSecondaryOrganizationNil

`func (o *Systems) SetSecondaryOrganizationNil(b bool)`

 SetSecondaryOrganizationNil sets the value for SecondaryOrganization to be an explicit nil

### UnsetSecondaryOrganization
`func (o *Systems) UnsetSecondaryOrganization()`

UnsetSecondaryOrganization ensures that no value is present for SecondaryOrganization, not even an explicit nil
### GetVersionReleaseNo

`func (o *Systems) GetVersionReleaseNo() string`

GetVersionReleaseNo returns the VersionReleaseNo field if non-nil, zero value otherwise.

### GetVersionReleaseNoOk

`func (o *Systems) GetVersionReleaseNoOk() (*string, bool)`

GetVersionReleaseNoOk returns a tuple with the VersionReleaseNo field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVersionReleaseNo

`func (o *Systems) SetVersionReleaseNo(v string)`

SetVersionReleaseNo sets VersionReleaseNo field to given value.

### HasVersionReleaseNo

`func (o *Systems) HasVersionReleaseNo() bool`

HasVersionReleaseNo returns a boolean if a field has been set.

### SetVersionReleaseNoNil

`func (o *Systems) SetVersionReleaseNoNil(b bool)`

 SetVersionReleaseNoNil sets the value for VersionReleaseNo to be an explicit nil

### UnsetVersionReleaseNo
`func (o *Systems) UnsetVersionReleaseNo()`

UnsetVersionReleaseNo ensures that no value is present for VersionReleaseNo, not even an explicit nil
### GetSystemType

`func (o *Systems) GetSystemType() string`

GetSystemType returns the SystemType field if non-nil, zero value otherwise.

### GetSystemTypeOk

`func (o *Systems) GetSystemTypeOk() (*string, bool)`

GetSystemTypeOk returns a tuple with the SystemType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSystemType

`func (o *Systems) SetSystemType(v string)`

SetSystemType sets SystemType field to given value.

### HasSystemType

`func (o *Systems) HasSystemType() bool`

HasSystemType returns a boolean if a field has been set.

### SetSystemTypeNil

`func (o *Systems) SetSystemTypeNil(b bool)`

 SetSystemTypeNil sets the value for SystemType to be an explicit nil

### UnsetSystemType
`func (o *Systems) UnsetSystemType()`

UnsetSystemType ensures that no value is present for SystemType, not even an explicit nil
### GetIsNSS

`func (o *Systems) GetIsNSS() bool`

GetIsNSS returns the IsNSS field if non-nil, zero value otherwise.

### GetIsNSSOk

`func (o *Systems) GetIsNSSOk() (*bool, bool)`

GetIsNSSOk returns a tuple with the IsNSS field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsNSS

`func (o *Systems) SetIsNSS(v bool)`

SetIsNSS sets IsNSS field to given value.

### HasIsNSS

`func (o *Systems) HasIsNSS() bool`

HasIsNSS returns a boolean if a field has been set.

### SetIsNSSNil

`func (o *Systems) SetIsNSSNil(b bool)`

 SetIsNSSNil sets the value for IsNSS to be an explicit nil

### UnsetIsNSS
`func (o *Systems) UnsetIsNSS()`

UnsetIsNSS ensures that no value is present for IsNSS, not even an explicit nil
### GetIsPublicFacing

`func (o *Systems) GetIsPublicFacing() bool`

GetIsPublicFacing returns the IsPublicFacing field if non-nil, zero value otherwise.

### GetIsPublicFacingOk

`func (o *Systems) GetIsPublicFacingOk() (*bool, bool)`

GetIsPublicFacingOk returns a tuple with the IsPublicFacing field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsPublicFacing

`func (o *Systems) SetIsPublicFacing(v bool)`

SetIsPublicFacing sets IsPublicFacing field to given value.

### HasIsPublicFacing

`func (o *Systems) HasIsPublicFacing() bool`

HasIsPublicFacing returns a boolean if a field has been set.

### SetIsPublicFacingNil

`func (o *Systems) SetIsPublicFacingNil(b bool)`

 SetIsPublicFacingNil sets the value for IsPublicFacing to be an explicit nil

### UnsetIsPublicFacing
`func (o *Systems) UnsetIsPublicFacing()`

UnsetIsPublicFacing ensures that no value is present for IsPublicFacing, not even an explicit nil
### GetCoamsId

`func (o *Systems) GetCoamsId() int64`

GetCoamsId returns the CoamsId field if non-nil, zero value otherwise.

### GetCoamsIdOk

`func (o *Systems) GetCoamsIdOk() (*int64, bool)`

GetCoamsIdOk returns a tuple with the CoamsId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCoamsId

`func (o *Systems) SetCoamsId(v int64)`

SetCoamsId sets CoamsId field to given value.

### HasCoamsId

`func (o *Systems) HasCoamsId() bool`

HasCoamsId returns a boolean if a field has been set.

### SetCoamsIdNil

`func (o *Systems) SetCoamsIdNil(b bool)`

 SetCoamsIdNil sets the value for CoamsId to be an explicit nil

### UnsetCoamsId
`func (o *Systems) UnsetCoamsId()`

UnsetCoamsId ensures that no value is present for CoamsId, not even an explicit nil
### GetIsTypeAuthorization

`func (o *Systems) GetIsTypeAuthorization() bool`

GetIsTypeAuthorization returns the IsTypeAuthorization field if non-nil, zero value otherwise.

### GetIsTypeAuthorizationOk

`func (o *Systems) GetIsTypeAuthorizationOk() (*bool, bool)`

GetIsTypeAuthorizationOk returns a tuple with the IsTypeAuthorization field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsTypeAuthorization

`func (o *Systems) SetIsTypeAuthorization(v bool)`

SetIsTypeAuthorization sets IsTypeAuthorization field to given value.

### HasIsTypeAuthorization

`func (o *Systems) HasIsTypeAuthorization() bool`

HasIsTypeAuthorization returns a boolean if a field has been set.

### SetIsTypeAuthorizationNil

`func (o *Systems) SetIsTypeAuthorizationNil(b bool)`

 SetIsTypeAuthorizationNil sets the value for IsTypeAuthorization to be an explicit nil

### UnsetIsTypeAuthorization
`func (o *Systems) UnsetIsTypeAuthorization()`

UnsetIsTypeAuthorization ensures that no value is present for IsTypeAuthorization, not even an explicit nil
### GetDitprId

`func (o *Systems) GetDitprId() string`

GetDitprId returns the DitprId field if non-nil, zero value otherwise.

### GetDitprIdOk

`func (o *Systems) GetDitprIdOk() (*string, bool)`

GetDitprIdOk returns a tuple with the DitprId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDitprId

`func (o *Systems) SetDitprId(v string)`

SetDitprId sets DitprId field to given value.

### HasDitprId

`func (o *Systems) HasDitprId() bool`

HasDitprId returns a boolean if a field has been set.

### GetApmsId

`func (o *Systems) GetApmsId() string`

GetApmsId returns the ApmsId field if non-nil, zero value otherwise.

### GetApmsIdOk

`func (o *Systems) GetApmsIdOk() (*string, bool)`

GetApmsIdOk returns a tuple with the ApmsId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetApmsId

`func (o *Systems) SetApmsId(v string)`

SetApmsId sets ApmsId field to given value.

### HasApmsId

`func (o *Systems) HasApmsId() bool`

HasApmsId returns a boolean if a field has been set.

### SetApmsIdNil

`func (o *Systems) SetApmsIdNil(b bool)`

 SetApmsIdNil sets the value for ApmsId to be an explicit nil

### UnsetApmsId
`func (o *Systems) UnsetApmsId()`

UnsetApmsId ensures that no value is present for ApmsId, not even an explicit nil
### GetVasiId

`func (o *Systems) GetVasiId() string`

GetVasiId returns the VasiId field if non-nil, zero value otherwise.

### GetVasiIdOk

`func (o *Systems) GetVasiIdOk() (*string, bool)`

GetVasiIdOk returns a tuple with the VasiId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVasiId

`func (o *Systems) SetVasiId(v string)`

SetVasiId sets VasiId field to given value.

### HasVasiId

`func (o *Systems) HasVasiId() bool`

HasVasiId returns a boolean if a field has been set.

### SetVasiIdNil

`func (o *Systems) SetVasiIdNil(b bool)`

 SetVasiIdNil sets the value for VasiId to be an explicit nil

### UnsetVasiId
`func (o *Systems) UnsetVasiId()`

UnsetVasiId ensures that no value is present for VasiId, not even an explicit nil
### GetAuthorizationStatus

`func (o *Systems) GetAuthorizationStatus() string`

GetAuthorizationStatus returns the AuthorizationStatus field if non-nil, zero value otherwise.

### GetAuthorizationStatusOk

`func (o *Systems) GetAuthorizationStatusOk() (*string, bool)`

GetAuthorizationStatusOk returns a tuple with the AuthorizationStatus field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAuthorizationStatus

`func (o *Systems) SetAuthorizationStatus(v string)`

SetAuthorizationStatus sets AuthorizationStatus field to given value.

### HasAuthorizationStatus

`func (o *Systems) HasAuthorizationStatus() bool`

HasAuthorizationStatus returns a boolean if a field has been set.

### SetAuthorizationStatusNil

`func (o *Systems) SetAuthorizationStatusNil(b bool)`

 SetAuthorizationStatusNil sets the value for AuthorizationStatus to be an explicit nil

### UnsetAuthorizationStatus
`func (o *Systems) UnsetAuthorizationStatus()`

UnsetAuthorizationStatus ensures that no value is present for AuthorizationStatus, not even an explicit nil
### GetAuthorizationDate

`func (o *Systems) GetAuthorizationDate() int32`

GetAuthorizationDate returns the AuthorizationDate field if non-nil, zero value otherwise.

### GetAuthorizationDateOk

`func (o *Systems) GetAuthorizationDateOk() (*int32, bool)`

GetAuthorizationDateOk returns a tuple with the AuthorizationDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAuthorizationDate

`func (o *Systems) SetAuthorizationDate(v int32)`

SetAuthorizationDate sets AuthorizationDate field to given value.

### HasAuthorizationDate

`func (o *Systems) HasAuthorizationDate() bool`

HasAuthorizationDate returns a boolean if a field has been set.

### SetAuthorizationDateNil

`func (o *Systems) SetAuthorizationDateNil(b bool)`

 SetAuthorizationDateNil sets the value for AuthorizationDate to be an explicit nil

### UnsetAuthorizationDate
`func (o *Systems) UnsetAuthorizationDate()`

UnsetAuthorizationDate ensures that no value is present for AuthorizationDate, not even an explicit nil
### GetAuthorizationTerminationDate

`func (o *Systems) GetAuthorizationTerminationDate() int32`

GetAuthorizationTerminationDate returns the AuthorizationTerminationDate field if non-nil, zero value otherwise.

### GetAuthorizationTerminationDateOk

`func (o *Systems) GetAuthorizationTerminationDateOk() (*int32, bool)`

GetAuthorizationTerminationDateOk returns a tuple with the AuthorizationTerminationDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAuthorizationTerminationDate

`func (o *Systems) SetAuthorizationTerminationDate(v int32)`

SetAuthorizationTerminationDate sets AuthorizationTerminationDate field to given value.

### HasAuthorizationTerminationDate

`func (o *Systems) HasAuthorizationTerminationDate() bool`

HasAuthorizationTerminationDate returns a boolean if a field has been set.

### SetAuthorizationTerminationDateNil

`func (o *Systems) SetAuthorizationTerminationDateNil(b bool)`

 SetAuthorizationTerminationDateNil sets the value for AuthorizationTerminationDate to be an explicit nil

### UnsetAuthorizationTerminationDate
`func (o *Systems) UnsetAuthorizationTerminationDate()`

UnsetAuthorizationTerminationDate ensures that no value is present for AuthorizationTerminationDate, not even an explicit nil
### GetAuthorizationLength

`func (o *Systems) GetAuthorizationLength() int32`

GetAuthorizationLength returns the AuthorizationLength field if non-nil, zero value otherwise.

### GetAuthorizationLengthOk

`func (o *Systems) GetAuthorizationLengthOk() (*int32, bool)`

GetAuthorizationLengthOk returns a tuple with the AuthorizationLength field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAuthorizationLength

`func (o *Systems) SetAuthorizationLength(v int32)`

SetAuthorizationLength sets AuthorizationLength field to given value.

### HasAuthorizationLength

`func (o *Systems) HasAuthorizationLength() bool`

HasAuthorizationLength returns a boolean if a field has been set.

### SetAuthorizationLengthNil

`func (o *Systems) SetAuthorizationLengthNil(b bool)`

 SetAuthorizationLengthNil sets the value for AuthorizationLength to be an explicit nil

### UnsetAuthorizationLength
`func (o *Systems) UnsetAuthorizationLength()`

UnsetAuthorizationLength ensures that no value is present for AuthorizationLength, not even an explicit nil
### GetSecurityControlsAssessorExecutiveSummary

`func (o *Systems) GetSecurityControlsAssessorExecutiveSummary() string`

GetSecurityControlsAssessorExecutiveSummary returns the SecurityControlsAssessorExecutiveSummary field if non-nil, zero value otherwise.

### GetSecurityControlsAssessorExecutiveSummaryOk

`func (o *Systems) GetSecurityControlsAssessorExecutiveSummaryOk() (*string, bool)`

GetSecurityControlsAssessorExecutiveSummaryOk returns a tuple with the SecurityControlsAssessorExecutiveSummary field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSecurityControlsAssessorExecutiveSummary

`func (o *Systems) SetSecurityControlsAssessorExecutiveSummary(v string)`

SetSecurityControlsAssessorExecutiveSummary sets SecurityControlsAssessorExecutiveSummary field to given value.

### HasSecurityControlsAssessorExecutiveSummary

`func (o *Systems) HasSecurityControlsAssessorExecutiveSummary() bool`

HasSecurityControlsAssessorExecutiveSummary returns a boolean if a field has been set.

### SetSecurityControlsAssessorExecutiveSummaryNil

`func (o *Systems) SetSecurityControlsAssessorExecutiveSummaryNil(b bool)`

 SetSecurityControlsAssessorExecutiveSummaryNil sets the value for SecurityControlsAssessorExecutiveSummary to be an explicit nil

### UnsetSecurityControlsAssessorExecutiveSummary
`func (o *Systems) UnsetSecurityControlsAssessorExecutiveSummary()`

UnsetSecurityControlsAssessorExecutiveSummary ensures that no value is present for SecurityControlsAssessorExecutiveSummary, not even an explicit nil
### GetRiskReviewExecutiveSummary

`func (o *Systems) GetRiskReviewExecutiveSummary() string`

GetRiskReviewExecutiveSummary returns the RiskReviewExecutiveSummary field if non-nil, zero value otherwise.

### GetRiskReviewExecutiveSummaryOk

`func (o *Systems) GetRiskReviewExecutiveSummaryOk() (*string, bool)`

GetRiskReviewExecutiveSummaryOk returns a tuple with the RiskReviewExecutiveSummary field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRiskReviewExecutiveSummary

`func (o *Systems) SetRiskReviewExecutiveSummary(v string)`

SetRiskReviewExecutiveSummary sets RiskReviewExecutiveSummary field to given value.

### HasRiskReviewExecutiveSummary

`func (o *Systems) HasRiskReviewExecutiveSummary() bool`

HasRiskReviewExecutiveSummary returns a boolean if a field has been set.

### SetRiskReviewExecutiveSummaryNil

`func (o *Systems) SetRiskReviewExecutiveSummaryNil(b bool)`

 SetRiskReviewExecutiveSummaryNil sets the value for RiskReviewExecutiveSummary to be an explicit nil

### UnsetRiskReviewExecutiveSummary
`func (o *Systems) UnsetRiskReviewExecutiveSummary()`

UnsetRiskReviewExecutiveSummary ensures that no value is present for RiskReviewExecutiveSummary, not even an explicit nil
### GetTermsForAuth

`func (o *Systems) GetTermsForAuth() string`

GetTermsForAuth returns the TermsForAuth field if non-nil, zero value otherwise.

### GetTermsForAuthOk

`func (o *Systems) GetTermsForAuthOk() (*string, bool)`

GetTermsForAuthOk returns a tuple with the TermsForAuth field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTermsForAuth

`func (o *Systems) SetTermsForAuth(v string)`

SetTermsForAuth sets TermsForAuth field to given value.

### HasTermsForAuth

`func (o *Systems) HasTermsForAuth() bool`

HasTermsForAuth returns a boolean if a field has been set.

### SetTermsForAuthNil

`func (o *Systems) SetTermsForAuthNil(b bool)`

 SetTermsForAuthNil sets the value for TermsForAuth to be an explicit nil

### UnsetTermsForAuth
`func (o *Systems) UnsetTermsForAuth()`

UnsetTermsForAuth ensures that no value is present for TermsForAuth, not even an explicit nil
### GetSecurityPlanApprovalStatus

`func (o *Systems) GetSecurityPlanApprovalStatus() string`

GetSecurityPlanApprovalStatus returns the SecurityPlanApprovalStatus field if non-nil, zero value otherwise.

### GetSecurityPlanApprovalStatusOk

`func (o *Systems) GetSecurityPlanApprovalStatusOk() (*string, bool)`

GetSecurityPlanApprovalStatusOk returns a tuple with the SecurityPlanApprovalStatus field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSecurityPlanApprovalStatus

`func (o *Systems) SetSecurityPlanApprovalStatus(v string)`

SetSecurityPlanApprovalStatus sets SecurityPlanApprovalStatus field to given value.

### HasSecurityPlanApprovalStatus

`func (o *Systems) HasSecurityPlanApprovalStatus() bool`

HasSecurityPlanApprovalStatus returns a boolean if a field has been set.

### SetSecurityPlanApprovalStatusNil

`func (o *Systems) SetSecurityPlanApprovalStatusNil(b bool)`

 SetSecurityPlanApprovalStatusNil sets the value for SecurityPlanApprovalStatus to be an explicit nil

### UnsetSecurityPlanApprovalStatus
`func (o *Systems) UnsetSecurityPlanApprovalStatus()`

UnsetSecurityPlanApprovalStatus ensures that no value is present for SecurityPlanApprovalStatus, not even an explicit nil
### GetSecurityPlanApprovalDate

`func (o *Systems) GetSecurityPlanApprovalDate() int32`

GetSecurityPlanApprovalDate returns the SecurityPlanApprovalDate field if non-nil, zero value otherwise.

### GetSecurityPlanApprovalDateOk

`func (o *Systems) GetSecurityPlanApprovalDateOk() (*int32, bool)`

GetSecurityPlanApprovalDateOk returns a tuple with the SecurityPlanApprovalDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSecurityPlanApprovalDate

`func (o *Systems) SetSecurityPlanApprovalDate(v int32)`

SetSecurityPlanApprovalDate sets SecurityPlanApprovalDate field to given value.

### HasSecurityPlanApprovalDate

`func (o *Systems) HasSecurityPlanApprovalDate() bool`

HasSecurityPlanApprovalDate returns a boolean if a field has been set.

### SetSecurityPlanApprovalDateNil

`func (o *Systems) SetSecurityPlanApprovalDateNil(b bool)`

 SetSecurityPlanApprovalDateNil sets the value for SecurityPlanApprovalDate to be an explicit nil

### UnsetSecurityPlanApprovalDate
`func (o *Systems) UnsetSecurityPlanApprovalDate()`

UnsetSecurityPlanApprovalDate ensures that no value is present for SecurityPlanApprovalDate, not even an explicit nil
### GetMissionCriticality

`func (o *Systems) GetMissionCriticality() string`

GetMissionCriticality returns the MissionCriticality field if non-nil, zero value otherwise.

### GetMissionCriticalityOk

`func (o *Systems) GetMissionCriticalityOk() (*string, bool)`

GetMissionCriticalityOk returns a tuple with the MissionCriticality field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMissionCriticality

`func (o *Systems) SetMissionCriticality(v string)`

SetMissionCriticality sets MissionCriticality field to given value.

### HasMissionCriticality

`func (o *Systems) HasMissionCriticality() bool`

HasMissionCriticality returns a boolean if a field has been set.

### SetMissionCriticalityNil

`func (o *Systems) SetMissionCriticalityNil(b bool)`

 SetMissionCriticalityNil sets the value for MissionCriticality to be an explicit nil

### UnsetMissionCriticality
`func (o *Systems) UnsetMissionCriticality()`

UnsetMissionCriticality ensures that no value is present for MissionCriticality, not even an explicit nil
### GetGeographicalAssociation

`func (o *Systems) GetGeographicalAssociation() string`

GetGeographicalAssociation returns the GeographicalAssociation field if non-nil, zero value otherwise.

### GetGeographicalAssociationOk

`func (o *Systems) GetGeographicalAssociationOk() (*string, bool)`

GetGeographicalAssociationOk returns a tuple with the GeographicalAssociation field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGeographicalAssociation

`func (o *Systems) SetGeographicalAssociation(v string)`

SetGeographicalAssociation sets GeographicalAssociation field to given value.

### HasGeographicalAssociation

`func (o *Systems) HasGeographicalAssociation() bool`

HasGeographicalAssociation returns a boolean if a field has been set.

### SetGeographicalAssociationNil

`func (o *Systems) SetGeographicalAssociationNil(b bool)`

 SetGeographicalAssociationNil sets the value for GeographicalAssociation to be an explicit nil

### UnsetGeographicalAssociation
`func (o *Systems) UnsetGeographicalAssociation()`

UnsetGeographicalAssociation ensures that no value is present for GeographicalAssociation, not even an explicit nil
### GetSystemOwnershipControlled

`func (o *Systems) GetSystemOwnershipControlled() string`

GetSystemOwnershipControlled returns the SystemOwnershipControlled field if non-nil, zero value otherwise.

### GetSystemOwnershipControlledOk

`func (o *Systems) GetSystemOwnershipControlledOk() (*string, bool)`

GetSystemOwnershipControlledOk returns a tuple with the SystemOwnershipControlled field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSystemOwnershipControlled

`func (o *Systems) SetSystemOwnershipControlled(v string)`

SetSystemOwnershipControlled sets SystemOwnershipControlled field to given value.

### HasSystemOwnershipControlled

`func (o *Systems) HasSystemOwnershipControlled() bool`

HasSystemOwnershipControlled returns a boolean if a field has been set.

### SetSystemOwnershipControlledNil

`func (o *Systems) SetSystemOwnershipControlledNil(b bool)`

 SetSystemOwnershipControlledNil sets the value for SystemOwnershipControlled to be an explicit nil

### UnsetSystemOwnershipControlled
`func (o *Systems) UnsetSystemOwnershipControlled()`

UnsetSystemOwnershipControlled ensures that no value is present for SystemOwnershipControlled, not even an explicit nil
### GetGoverningMissionArea

`func (o *Systems) GetGoverningMissionArea() string`

GetGoverningMissionArea returns the GoverningMissionArea field if non-nil, zero value otherwise.

### GetGoverningMissionAreaOk

`func (o *Systems) GetGoverningMissionAreaOk() (*string, bool)`

GetGoverningMissionAreaOk returns a tuple with the GoverningMissionArea field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGoverningMissionArea

`func (o *Systems) SetGoverningMissionArea(v string)`

SetGoverningMissionArea sets GoverningMissionArea field to given value.

### HasGoverningMissionArea

`func (o *Systems) HasGoverningMissionArea() bool`

HasGoverningMissionArea returns a boolean if a field has been set.

### SetGoverningMissionAreaNil

`func (o *Systems) SetGoverningMissionAreaNil(b bool)`

 SetGoverningMissionAreaNil sets the value for GoverningMissionArea to be an explicit nil

### UnsetGoverningMissionArea
`func (o *Systems) UnsetGoverningMissionArea()`

UnsetGoverningMissionArea ensures that no value is present for GoverningMissionArea, not even an explicit nil
### GetPrimaryFunctionalArea

`func (o *Systems) GetPrimaryFunctionalArea() string`

GetPrimaryFunctionalArea returns the PrimaryFunctionalArea field if non-nil, zero value otherwise.

### GetPrimaryFunctionalAreaOk

`func (o *Systems) GetPrimaryFunctionalAreaOk() (*string, bool)`

GetPrimaryFunctionalAreaOk returns a tuple with the PrimaryFunctionalArea field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPrimaryFunctionalArea

`func (o *Systems) SetPrimaryFunctionalArea(v string)`

SetPrimaryFunctionalArea sets PrimaryFunctionalArea field to given value.

### HasPrimaryFunctionalArea

`func (o *Systems) HasPrimaryFunctionalArea() bool`

HasPrimaryFunctionalArea returns a boolean if a field has been set.

### SetPrimaryFunctionalAreaNil

`func (o *Systems) SetPrimaryFunctionalAreaNil(b bool)`

 SetPrimaryFunctionalAreaNil sets the value for PrimaryFunctionalArea to be an explicit nil

### UnsetPrimaryFunctionalArea
`func (o *Systems) UnsetPrimaryFunctionalArea()`

UnsetPrimaryFunctionalArea ensures that no value is present for PrimaryFunctionalArea, not even an explicit nil
### GetSecondaryFunctionalArea

`func (o *Systems) GetSecondaryFunctionalArea() string`

GetSecondaryFunctionalArea returns the SecondaryFunctionalArea field if non-nil, zero value otherwise.

### GetSecondaryFunctionalAreaOk

`func (o *Systems) GetSecondaryFunctionalAreaOk() (*string, bool)`

GetSecondaryFunctionalAreaOk returns a tuple with the SecondaryFunctionalArea field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSecondaryFunctionalArea

`func (o *Systems) SetSecondaryFunctionalArea(v string)`

SetSecondaryFunctionalArea sets SecondaryFunctionalArea field to given value.

### HasSecondaryFunctionalArea

`func (o *Systems) HasSecondaryFunctionalArea() bool`

HasSecondaryFunctionalArea returns a boolean if a field has been set.

### SetSecondaryFunctionalAreaNil

`func (o *Systems) SetSecondaryFunctionalAreaNil(b bool)`

 SetSecondaryFunctionalAreaNil sets the value for SecondaryFunctionalArea to be an explicit nil

### UnsetSecondaryFunctionalArea
`func (o *Systems) UnsetSecondaryFunctionalArea()`

UnsetSecondaryFunctionalArea ensures that no value is present for SecondaryFunctionalArea, not even an explicit nil
### GetPrimaryControlSet

`func (o *Systems) GetPrimaryControlSet() string`

GetPrimaryControlSet returns the PrimaryControlSet field if non-nil, zero value otherwise.

### GetPrimaryControlSetOk

`func (o *Systems) GetPrimaryControlSetOk() (*string, bool)`

GetPrimaryControlSetOk returns a tuple with the PrimaryControlSet field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPrimaryControlSet

`func (o *Systems) SetPrimaryControlSet(v string)`

SetPrimaryControlSet sets PrimaryControlSet field to given value.

### HasPrimaryControlSet

`func (o *Systems) HasPrimaryControlSet() bool`

HasPrimaryControlSet returns a boolean if a field has been set.

### SetPrimaryControlSetNil

`func (o *Systems) SetPrimaryControlSetNil(b bool)`

 SetPrimaryControlSetNil sets the value for PrimaryControlSet to be an explicit nil

### UnsetPrimaryControlSet
`func (o *Systems) UnsetPrimaryControlSet()`

UnsetPrimaryControlSet ensures that no value is present for PrimaryControlSet, not even an explicit nil
### GetConfidentiality

`func (o *Systems) GetConfidentiality() string`

GetConfidentiality returns the Confidentiality field if non-nil, zero value otherwise.

### GetConfidentialityOk

`func (o *Systems) GetConfidentialityOk() (*string, bool)`

GetConfidentialityOk returns a tuple with the Confidentiality field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetConfidentiality

`func (o *Systems) SetConfidentiality(v string)`

SetConfidentiality sets Confidentiality field to given value.

### HasConfidentiality

`func (o *Systems) HasConfidentiality() bool`

HasConfidentiality returns a boolean if a field has been set.

### SetConfidentialityNil

`func (o *Systems) SetConfidentialityNil(b bool)`

 SetConfidentialityNil sets the value for Confidentiality to be an explicit nil

### UnsetConfidentiality
`func (o *Systems) UnsetConfidentiality()`

UnsetConfidentiality ensures that no value is present for Confidentiality, not even an explicit nil
### GetIntegrity

`func (o *Systems) GetIntegrity() string`

GetIntegrity returns the Integrity field if non-nil, zero value otherwise.

### GetIntegrityOk

`func (o *Systems) GetIntegrityOk() (*string, bool)`

GetIntegrityOk returns a tuple with the Integrity field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIntegrity

`func (o *Systems) SetIntegrity(v string)`

SetIntegrity sets Integrity field to given value.

### HasIntegrity

`func (o *Systems) HasIntegrity() bool`

HasIntegrity returns a boolean if a field has been set.

### SetIntegrityNil

`func (o *Systems) SetIntegrityNil(b bool)`

 SetIntegrityNil sets the value for Integrity to be an explicit nil

### UnsetIntegrity
`func (o *Systems) UnsetIntegrity()`

UnsetIntegrity ensures that no value is present for Integrity, not even an explicit nil
### GetAvailability

`func (o *Systems) GetAvailability() string`

GetAvailability returns the Availability field if non-nil, zero value otherwise.

### GetAvailabilityOk

`func (o *Systems) GetAvailabilityOk() (*string, bool)`

GetAvailabilityOk returns a tuple with the Availability field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAvailability

`func (o *Systems) SetAvailability(v string)`

SetAvailability sets Availability field to given value.

### HasAvailability

`func (o *Systems) HasAvailability() bool`

HasAvailability returns a boolean if a field has been set.

### SetAvailabilityNil

`func (o *Systems) SetAvailabilityNil(b bool)`

 SetAvailabilityNil sets the value for Availability to be an explicit nil

### UnsetAvailability
`func (o *Systems) UnsetAvailability()`

UnsetAvailability ensures that no value is present for Availability, not even an explicit nil
### GetAppliedOverlays

`func (o *Systems) GetAppliedOverlays() string`

GetAppliedOverlays returns the AppliedOverlays field if non-nil, zero value otherwise.

### GetAppliedOverlaysOk

`func (o *Systems) GetAppliedOverlaysOk() (*string, bool)`

GetAppliedOverlaysOk returns a tuple with the AppliedOverlays field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAppliedOverlays

`func (o *Systems) SetAppliedOverlays(v string)`

SetAppliedOverlays sets AppliedOverlays field to given value.

### HasAppliedOverlays

`func (o *Systems) HasAppliedOverlays() bool`

HasAppliedOverlays returns a boolean if a field has been set.

### SetAppliedOverlaysNil

`func (o *Systems) SetAppliedOverlaysNil(b bool)`

 SetAppliedOverlaysNil sets the value for AppliedOverlays to be an explicit nil

### UnsetAppliedOverlays
`func (o *Systems) UnsetAppliedOverlays()`

UnsetAppliedOverlays ensures that no value is present for AppliedOverlays, not even an explicit nil
### GetAppliedStigs

`func (o *Systems) GetAppliedStigs() string`

GetAppliedStigs returns the AppliedStigs field if non-nil, zero value otherwise.

### GetAppliedStigsOk

`func (o *Systems) GetAppliedStigsOk() (*string, bool)`

GetAppliedStigsOk returns a tuple with the AppliedStigs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAppliedStigs

`func (o *Systems) SetAppliedStigs(v string)`

SetAppliedStigs sets AppliedStigs field to given value.

### HasAppliedStigs

`func (o *Systems) HasAppliedStigs() bool`

HasAppliedStigs returns a boolean if a field has been set.

### SetAppliedStigsNil

`func (o *Systems) SetAppliedStigsNil(b bool)`

 SetAppliedStigsNil sets the value for AppliedStigs to be an explicit nil

### UnsetAppliedStigs
`func (o *Systems) UnsetAppliedStigs()`

UnsetAppliedStigs ensures that no value is present for AppliedStigs, not even an explicit nil
### GetRmfActivity

`func (o *Systems) GetRmfActivity() string`

GetRmfActivity returns the RmfActivity field if non-nil, zero value otherwise.

### GetRmfActivityOk

`func (o *Systems) GetRmfActivityOk() (*string, bool)`

GetRmfActivityOk returns a tuple with the RmfActivity field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRmfActivity

`func (o *Systems) SetRmfActivity(v string)`

SetRmfActivity sets RmfActivity field to given value.

### HasRmfActivity

`func (o *Systems) HasRmfActivity() bool`

HasRmfActivity returns a boolean if a field has been set.

### SetRmfActivityNil

`func (o *Systems) SetRmfActivityNil(b bool)`

 SetRmfActivityNil sets the value for RmfActivity to be an explicit nil

### UnsetRmfActivity
`func (o *Systems) UnsetRmfActivity()`

UnsetRmfActivity ensures that no value is present for RmfActivity, not even an explicit nil
### GetCrossDomainTicket

`func (o *Systems) GetCrossDomainTicket() string`

GetCrossDomainTicket returns the CrossDomainTicket field if non-nil, zero value otherwise.

### GetCrossDomainTicketOk

`func (o *Systems) GetCrossDomainTicketOk() (*string, bool)`

GetCrossDomainTicketOk returns a tuple with the CrossDomainTicket field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCrossDomainTicket

`func (o *Systems) SetCrossDomainTicket(v string)`

SetCrossDomainTicket sets CrossDomainTicket field to given value.

### HasCrossDomainTicket

`func (o *Systems) HasCrossDomainTicket() bool`

HasCrossDomainTicket returns a boolean if a field has been set.

### SetCrossDomainTicketNil

`func (o *Systems) SetCrossDomainTicketNil(b bool)`

 SetCrossDomainTicketNil sets the value for CrossDomainTicket to be an explicit nil

### UnsetCrossDomainTicket
`func (o *Systems) UnsetCrossDomainTicket()`

UnsetCrossDomainTicket ensures that no value is present for CrossDomainTicket, not even an explicit nil
### GetDitprDonId

`func (o *Systems) GetDitprDonId() string`

GetDitprDonId returns the DitprDonId field if non-nil, zero value otherwise.

### GetDitprDonIdOk

`func (o *Systems) GetDitprDonIdOk() (*string, bool)`

GetDitprDonIdOk returns a tuple with the DitprDonId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDitprDonId

`func (o *Systems) SetDitprDonId(v string)`

SetDitprDonId sets DitprDonId field to given value.

### HasDitprDonId

`func (o *Systems) HasDitprDonId() bool`

HasDitprDonId returns a boolean if a field has been set.

### SetDitprDonIdNil

`func (o *Systems) SetDitprDonIdNil(b bool)`

 SetDitprDonIdNil sets the value for DitprDonId to be an explicit nil

### UnsetDitprDonId
`func (o *Systems) UnsetDitprDonId()`

UnsetDitprDonId ensures that no value is present for DitprDonId, not even an explicit nil
### GetMac

`func (o *Systems) GetMac() string`

GetMac returns the Mac field if non-nil, zero value otherwise.

### GetMacOk

`func (o *Systems) GetMacOk() (*string, bool)`

GetMacOk returns a tuple with the Mac field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMac

`func (o *Systems) SetMac(v string)`

SetMac sets Mac field to given value.

### HasMac

`func (o *Systems) HasMac() bool`

HasMac returns a boolean if a field has been set.

### SetMacNil

`func (o *Systems) SetMacNil(b bool)`

 SetMacNil sets the value for Mac to be an explicit nil

### UnsetMac
`func (o *Systems) UnsetMac()`

UnsetMac ensures that no value is present for Mac, not even an explicit nil
### GetDodConfidentiality

`func (o *Systems) GetDodConfidentiality() string`

GetDodConfidentiality returns the DodConfidentiality field if non-nil, zero value otherwise.

### GetDodConfidentialityOk

`func (o *Systems) GetDodConfidentialityOk() (*string, bool)`

GetDodConfidentialityOk returns a tuple with the DodConfidentiality field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDodConfidentiality

`func (o *Systems) SetDodConfidentiality(v string)`

SetDodConfidentiality sets DodConfidentiality field to given value.

### HasDodConfidentiality

`func (o *Systems) HasDodConfidentiality() bool`

HasDodConfidentiality returns a boolean if a field has been set.

### SetDodConfidentialityNil

`func (o *Systems) SetDodConfidentialityNil(b bool)`

 SetDodConfidentialityNil sets the value for DodConfidentiality to be an explicit nil

### UnsetDodConfidentiality
`func (o *Systems) UnsetDodConfidentiality()`

UnsetDodConfidentiality ensures that no value is present for DodConfidentiality, not even an explicit nil
### GetContingencyPlanRequired

`func (o *Systems) GetContingencyPlanRequired() bool`

GetContingencyPlanRequired returns the ContingencyPlanRequired field if non-nil, zero value otherwise.

### GetContingencyPlanRequiredOk

`func (o *Systems) GetContingencyPlanRequiredOk() (*bool, bool)`

GetContingencyPlanRequiredOk returns a tuple with the ContingencyPlanRequired field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContingencyPlanRequired

`func (o *Systems) SetContingencyPlanRequired(v bool)`

SetContingencyPlanRequired sets ContingencyPlanRequired field to given value.

### HasContingencyPlanRequired

`func (o *Systems) HasContingencyPlanRequired() bool`

HasContingencyPlanRequired returns a boolean if a field has been set.

### SetContingencyPlanRequiredNil

`func (o *Systems) SetContingencyPlanRequiredNil(b bool)`

 SetContingencyPlanRequiredNil sets the value for ContingencyPlanRequired to be an explicit nil

### UnsetContingencyPlanRequired
`func (o *Systems) UnsetContingencyPlanRequired()`

UnsetContingencyPlanRequired ensures that no value is present for ContingencyPlanRequired, not even an explicit nil
### GetContingencyPlanArtifact

`func (o *Systems) GetContingencyPlanArtifact() string`

GetContingencyPlanArtifact returns the ContingencyPlanArtifact field if non-nil, zero value otherwise.

### GetContingencyPlanArtifactOk

`func (o *Systems) GetContingencyPlanArtifactOk() (*string, bool)`

GetContingencyPlanArtifactOk returns a tuple with the ContingencyPlanArtifact field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContingencyPlanArtifact

`func (o *Systems) SetContingencyPlanArtifact(v string)`

SetContingencyPlanArtifact sets ContingencyPlanArtifact field to given value.

### HasContingencyPlanArtifact

`func (o *Systems) HasContingencyPlanArtifact() bool`

HasContingencyPlanArtifact returns a boolean if a field has been set.

### SetContingencyPlanArtifactNil

`func (o *Systems) SetContingencyPlanArtifactNil(b bool)`

 SetContingencyPlanArtifactNil sets the value for ContingencyPlanArtifact to be an explicit nil

### UnsetContingencyPlanArtifact
`func (o *Systems) UnsetContingencyPlanArtifact()`

UnsetContingencyPlanArtifact ensures that no value is present for ContingencyPlanArtifact, not even an explicit nil
### GetContingencyPlanTested

`func (o *Systems) GetContingencyPlanTested() bool`

GetContingencyPlanTested returns the ContingencyPlanTested field if non-nil, zero value otherwise.

### GetContingencyPlanTestedOk

`func (o *Systems) GetContingencyPlanTestedOk() (*bool, bool)`

GetContingencyPlanTestedOk returns a tuple with the ContingencyPlanTested field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContingencyPlanTested

`func (o *Systems) SetContingencyPlanTested(v bool)`

SetContingencyPlanTested sets ContingencyPlanTested field to given value.

### HasContingencyPlanTested

`func (o *Systems) HasContingencyPlanTested() bool`

HasContingencyPlanTested returns a boolean if a field has been set.

### SetContingencyPlanTestedNil

`func (o *Systems) SetContingencyPlanTestedNil(b bool)`

 SetContingencyPlanTestedNil sets the value for ContingencyPlanTested to be an explicit nil

### UnsetContingencyPlanTested
`func (o *Systems) UnsetContingencyPlanTested()`

UnsetContingencyPlanTested ensures that no value is present for ContingencyPlanTested, not even an explicit nil
### GetContingencyPlanTestDate

`func (o *Systems) GetContingencyPlanTestDate() int32`

GetContingencyPlanTestDate returns the ContingencyPlanTestDate field if non-nil, zero value otherwise.

### GetContingencyPlanTestDateOk

`func (o *Systems) GetContingencyPlanTestDateOk() (*int32, bool)`

GetContingencyPlanTestDateOk returns a tuple with the ContingencyPlanTestDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContingencyPlanTestDate

`func (o *Systems) SetContingencyPlanTestDate(v int32)`

SetContingencyPlanTestDate sets ContingencyPlanTestDate field to given value.

### HasContingencyPlanTestDate

`func (o *Systems) HasContingencyPlanTestDate() bool`

HasContingencyPlanTestDate returns a boolean if a field has been set.

### SetContingencyPlanTestDateNil

`func (o *Systems) SetContingencyPlanTestDateNil(b bool)`

 SetContingencyPlanTestDateNil sets the value for ContingencyPlanTestDate to be an explicit nil

### UnsetContingencyPlanTestDate
`func (o *Systems) UnsetContingencyPlanTestDate()`

UnsetContingencyPlanTestDate ensures that no value is present for ContingencyPlanTestDate, not even an explicit nil
### GetSecurityReviewRequired

`func (o *Systems) GetSecurityReviewRequired() bool`

GetSecurityReviewRequired returns the SecurityReviewRequired field if non-nil, zero value otherwise.

### GetSecurityReviewRequiredOk

`func (o *Systems) GetSecurityReviewRequiredOk() (*bool, bool)`

GetSecurityReviewRequiredOk returns a tuple with the SecurityReviewRequired field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSecurityReviewRequired

`func (o *Systems) SetSecurityReviewRequired(v bool)`

SetSecurityReviewRequired sets SecurityReviewRequired field to given value.

### HasSecurityReviewRequired

`func (o *Systems) HasSecurityReviewRequired() bool`

HasSecurityReviewRequired returns a boolean if a field has been set.

### SetSecurityReviewRequiredNil

`func (o *Systems) SetSecurityReviewRequiredNil(b bool)`

 SetSecurityReviewRequiredNil sets the value for SecurityReviewRequired to be an explicit nil

### UnsetSecurityReviewRequired
`func (o *Systems) UnsetSecurityReviewRequired()`

UnsetSecurityReviewRequired ensures that no value is present for SecurityReviewRequired, not even an explicit nil
### GetSecurityReviewCompleted

`func (o *Systems) GetSecurityReviewCompleted() bool`

GetSecurityReviewCompleted returns the SecurityReviewCompleted field if non-nil, zero value otherwise.

### GetSecurityReviewCompletedOk

`func (o *Systems) GetSecurityReviewCompletedOk() (*bool, bool)`

GetSecurityReviewCompletedOk returns a tuple with the SecurityReviewCompleted field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSecurityReviewCompleted

`func (o *Systems) SetSecurityReviewCompleted(v bool)`

SetSecurityReviewCompleted sets SecurityReviewCompleted field to given value.

### HasSecurityReviewCompleted

`func (o *Systems) HasSecurityReviewCompleted() bool`

HasSecurityReviewCompleted returns a boolean if a field has been set.

### SetSecurityReviewCompletedNil

`func (o *Systems) SetSecurityReviewCompletedNil(b bool)`

 SetSecurityReviewCompletedNil sets the value for SecurityReviewCompleted to be an explicit nil

### UnsetSecurityReviewCompleted
`func (o *Systems) UnsetSecurityReviewCompleted()`

UnsetSecurityReviewCompleted ensures that no value is present for SecurityReviewCompleted, not even an explicit nil
### GetSecurityReviewCompletionDate

`func (o *Systems) GetSecurityReviewCompletionDate() int32`

GetSecurityReviewCompletionDate returns the SecurityReviewCompletionDate field if non-nil, zero value otherwise.

### GetSecurityReviewCompletionDateOk

`func (o *Systems) GetSecurityReviewCompletionDateOk() (*int32, bool)`

GetSecurityReviewCompletionDateOk returns a tuple with the SecurityReviewCompletionDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSecurityReviewCompletionDate

`func (o *Systems) SetSecurityReviewCompletionDate(v int32)`

SetSecurityReviewCompletionDate sets SecurityReviewCompletionDate field to given value.

### HasSecurityReviewCompletionDate

`func (o *Systems) HasSecurityReviewCompletionDate() bool`

HasSecurityReviewCompletionDate returns a boolean if a field has been set.

### SetSecurityReviewCompletionDateNil

`func (o *Systems) SetSecurityReviewCompletionDateNil(b bool)`

 SetSecurityReviewCompletionDateNil sets the value for SecurityReviewCompletionDate to be an explicit nil

### UnsetSecurityReviewCompletionDate
`func (o *Systems) UnsetSecurityReviewCompletionDate()`

UnsetSecurityReviewCompletionDate ensures that no value is present for SecurityReviewCompletionDate, not even an explicit nil
### GetNextSecurityReviewDueDate

`func (o *Systems) GetNextSecurityReviewDueDate() int32`

GetNextSecurityReviewDueDate returns the NextSecurityReviewDueDate field if non-nil, zero value otherwise.

### GetNextSecurityReviewDueDateOk

`func (o *Systems) GetNextSecurityReviewDueDateOk() (*int32, bool)`

GetNextSecurityReviewDueDateOk returns a tuple with the NextSecurityReviewDueDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNextSecurityReviewDueDate

`func (o *Systems) SetNextSecurityReviewDueDate(v int32)`

SetNextSecurityReviewDueDate sets NextSecurityReviewDueDate field to given value.

### HasNextSecurityReviewDueDate

`func (o *Systems) HasNextSecurityReviewDueDate() bool`

HasNextSecurityReviewDueDate returns a boolean if a field has been set.

### SetNextSecurityReviewDueDateNil

`func (o *Systems) SetNextSecurityReviewDueDateNil(b bool)`

 SetNextSecurityReviewDueDateNil sets the value for NextSecurityReviewDueDate to be an explicit nil

### UnsetNextSecurityReviewDueDate
`func (o *Systems) UnsetNextSecurityReviewDueDate()`

UnsetNextSecurityReviewDueDate ensures that no value is present for NextSecurityReviewDueDate, not even an explicit nil
### GetHasOpenPoamItem

`func (o *Systems) GetHasOpenPoamItem() bool`

GetHasOpenPoamItem returns the HasOpenPoamItem field if non-nil, zero value otherwise.

### GetHasOpenPoamItemOk

`func (o *Systems) GetHasOpenPoamItemOk() (*bool, bool)`

GetHasOpenPoamItemOk returns a tuple with the HasOpenPoamItem field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHasOpenPoamItem

`func (o *Systems) SetHasOpenPoamItem(v bool)`

SetHasOpenPoamItem sets HasOpenPoamItem field to given value.

### HasHasOpenPoamItem

`func (o *Systems) HasHasOpenPoamItem() bool`

HasHasOpenPoamItem returns a boolean if a field has been set.

### SetHasOpenPoamItemNil

`func (o *Systems) SetHasOpenPoamItemNil(b bool)`

 SetHasOpenPoamItemNil sets the value for HasOpenPoamItem to be an explicit nil

### UnsetHasOpenPoamItem
`func (o *Systems) UnsetHasOpenPoamItem()`

UnsetHasOpenPoamItem ensures that no value is present for HasOpenPoamItem, not even an explicit nil
### GetHasOpenPoamItem90to120PastScheduledCompletionDate

`func (o *Systems) GetHasOpenPoamItem90to120PastScheduledCompletionDate() bool`

GetHasOpenPoamItem90to120PastScheduledCompletionDate returns the HasOpenPoamItem90to120PastScheduledCompletionDate field if non-nil, zero value otherwise.

### GetHasOpenPoamItem90to120PastScheduledCompletionDateOk

`func (o *Systems) GetHasOpenPoamItem90to120PastScheduledCompletionDateOk() (*bool, bool)`

GetHasOpenPoamItem90to120PastScheduledCompletionDateOk returns a tuple with the HasOpenPoamItem90to120PastScheduledCompletionDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHasOpenPoamItem90to120PastScheduledCompletionDate

`func (o *Systems) SetHasOpenPoamItem90to120PastScheduledCompletionDate(v bool)`

SetHasOpenPoamItem90to120PastScheduledCompletionDate sets HasOpenPoamItem90to120PastScheduledCompletionDate field to given value.

### HasHasOpenPoamItem90to120PastScheduledCompletionDate

`func (o *Systems) HasHasOpenPoamItem90to120PastScheduledCompletionDate() bool`

HasHasOpenPoamItem90to120PastScheduledCompletionDate returns a boolean if a field has been set.

### SetHasOpenPoamItem90to120PastScheduledCompletionDateNil

`func (o *Systems) SetHasOpenPoamItem90to120PastScheduledCompletionDateNil(b bool)`

 SetHasOpenPoamItem90to120PastScheduledCompletionDateNil sets the value for HasOpenPoamItem90to120PastScheduledCompletionDate to be an explicit nil

### UnsetHasOpenPoamItem90to120PastScheduledCompletionDate
`func (o *Systems) UnsetHasOpenPoamItem90to120PastScheduledCompletionDate()`

UnsetHasOpenPoamItem90to120PastScheduledCompletionDate ensures that no value is present for HasOpenPoamItem90to120PastScheduledCompletionDate, not even an explicit nil
### GetHasOpenPoamItem120PlusPastScheudledCompletionDate

`func (o *Systems) GetHasOpenPoamItem120PlusPastScheudledCompletionDate() bool`

GetHasOpenPoamItem120PlusPastScheudledCompletionDate returns the HasOpenPoamItem120PlusPastScheudledCompletionDate field if non-nil, zero value otherwise.

### GetHasOpenPoamItem120PlusPastScheudledCompletionDateOk

`func (o *Systems) GetHasOpenPoamItem120PlusPastScheudledCompletionDateOk() (*bool, bool)`

GetHasOpenPoamItem120PlusPastScheudledCompletionDateOk returns a tuple with the HasOpenPoamItem120PlusPastScheudledCompletionDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHasOpenPoamItem120PlusPastScheudledCompletionDate

`func (o *Systems) SetHasOpenPoamItem120PlusPastScheudledCompletionDate(v bool)`

SetHasOpenPoamItem120PlusPastScheudledCompletionDate sets HasOpenPoamItem120PlusPastScheudledCompletionDate field to given value.

### HasHasOpenPoamItem120PlusPastScheudledCompletionDate

`func (o *Systems) HasHasOpenPoamItem120PlusPastScheudledCompletionDate() bool`

HasHasOpenPoamItem120PlusPastScheudledCompletionDate returns a boolean if a field has been set.

### SetHasOpenPoamItem120PlusPastScheudledCompletionDateNil

`func (o *Systems) SetHasOpenPoamItem120PlusPastScheudledCompletionDateNil(b bool)`

 SetHasOpenPoamItem120PlusPastScheudledCompletionDateNil sets the value for HasOpenPoamItem120PlusPastScheudledCompletionDate to be an explicit nil

### UnsetHasOpenPoamItem120PlusPastScheudledCompletionDate
`func (o *Systems) UnsetHasOpenPoamItem120PlusPastScheudledCompletionDate()`

UnsetHasOpenPoamItem120PlusPastScheudledCompletionDate ensures that no value is present for HasOpenPoamItem120PlusPastScheudledCompletionDate, not even an explicit nil
### GetImpact

`func (o *Systems) GetImpact() string`

GetImpact returns the Impact field if non-nil, zero value otherwise.

### GetImpactOk

`func (o *Systems) GetImpactOk() (*string, bool)`

GetImpactOk returns a tuple with the Impact field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetImpact

`func (o *Systems) SetImpact(v string)`

SetImpact sets Impact field to given value.

### HasImpact

`func (o *Systems) HasImpact() bool`

HasImpact returns a boolean if a field has been set.

### SetImpactNil

`func (o *Systems) SetImpactNil(b bool)`

 SetImpactNil sets the value for Impact to be an explicit nil

### UnsetImpact
`func (o *Systems) UnsetImpact()`

UnsetImpact ensures that no value is present for Impact, not even an explicit nil
### GetHasCUI

`func (o *Systems) GetHasCUI() bool`

GetHasCUI returns the HasCUI field if non-nil, zero value otherwise.

### GetHasCUIOk

`func (o *Systems) GetHasCUIOk() (*bool, bool)`

GetHasCUIOk returns a tuple with the HasCUI field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHasCUI

`func (o *Systems) SetHasCUI(v bool)`

SetHasCUI sets HasCUI field to given value.

### HasHasCUI

`func (o *Systems) HasHasCUI() bool`

HasHasCUI returns a boolean if a field has been set.

### SetHasCUINil

`func (o *Systems) SetHasCUINil(b bool)`

 SetHasCUINil sets the value for HasCUI to be an explicit nil

### UnsetHasCUI
`func (o *Systems) UnsetHasCUI()`

UnsetHasCUI ensures that no value is present for HasCUI, not even an explicit nil
### GetHasPII

`func (o *Systems) GetHasPII() bool`

GetHasPII returns the HasPII field if non-nil, zero value otherwise.

### GetHasPIIOk

`func (o *Systems) GetHasPIIOk() (*bool, bool)`

GetHasPIIOk returns a tuple with the HasPII field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHasPII

`func (o *Systems) SetHasPII(v bool)`

SetHasPII sets HasPII field to given value.

### HasHasPII

`func (o *Systems) HasHasPII() bool`

HasHasPII returns a boolean if a field has been set.

### SetHasPIINil

`func (o *Systems) SetHasPIINil(b bool)`

 SetHasPIINil sets the value for HasPII to be an explicit nil

### UnsetHasPII
`func (o *Systems) UnsetHasPII()`

UnsetHasPII ensures that no value is present for HasPII, not even an explicit nil
### GetHasPHI

`func (o *Systems) GetHasPHI() bool`

GetHasPHI returns the HasPHI field if non-nil, zero value otherwise.

### GetHasPHIOk

`func (o *Systems) GetHasPHIOk() (*bool, bool)`

GetHasPHIOk returns a tuple with the HasPHI field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHasPHI

`func (o *Systems) SetHasPHI(v bool)`

SetHasPHI sets HasPHI field to given value.

### HasHasPHI

`func (o *Systems) HasHasPHI() bool`

HasHasPHI returns a boolean if a field has been set.

### SetHasPHINil

`func (o *Systems) SetHasPHINil(b bool)`

 SetHasPHINil sets the value for HasPHI to be an explicit nil

### UnsetHasPHI
`func (o *Systems) UnsetHasPHI()`

UnsetHasPHI ensures that no value is present for HasPHI, not even an explicit nil
### GetPpsmRegistrationRequired

`func (o *Systems) GetPpsmRegistrationRequired() string`

GetPpsmRegistrationRequired returns the PpsmRegistrationRequired field if non-nil, zero value otherwise.

### GetPpsmRegistrationRequiredOk

`func (o *Systems) GetPpsmRegistrationRequiredOk() (*string, bool)`

GetPpsmRegistrationRequiredOk returns a tuple with the PpsmRegistrationRequired field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPpsmRegistrationRequired

`func (o *Systems) SetPpsmRegistrationRequired(v string)`

SetPpsmRegistrationRequired sets PpsmRegistrationRequired field to given value.

### HasPpsmRegistrationRequired

`func (o *Systems) HasPpsmRegistrationRequired() bool`

HasPpsmRegistrationRequired returns a boolean if a field has been set.

### SetPpsmRegistrationRequiredNil

`func (o *Systems) SetPpsmRegistrationRequiredNil(b bool)`

 SetPpsmRegistrationRequiredNil sets the value for PpsmRegistrationRequired to be an explicit nil

### UnsetPpsmRegistrationRequired
`func (o *Systems) UnsetPpsmRegistrationRequired()`

UnsetPpsmRegistrationRequired ensures that no value is present for PpsmRegistrationRequired, not even an explicit nil
### GetPpsmRegistryNumber

`func (o *Systems) GetPpsmRegistryNumber() string`

GetPpsmRegistryNumber returns the PpsmRegistryNumber field if non-nil, zero value otherwise.

### GetPpsmRegistryNumberOk

`func (o *Systems) GetPpsmRegistryNumberOk() (*string, bool)`

GetPpsmRegistryNumberOk returns a tuple with the PpsmRegistryNumber field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPpsmRegistryNumber

`func (o *Systems) SetPpsmRegistryNumber(v string)`

SetPpsmRegistryNumber sets PpsmRegistryNumber field to given value.

### HasPpsmRegistryNumber

`func (o *Systems) HasPpsmRegistryNumber() bool`

HasPpsmRegistryNumber returns a boolean if a field has been set.

### SetPpsmRegistryNumberNil

`func (o *Systems) SetPpsmRegistryNumberNil(b bool)`

 SetPpsmRegistryNumberNil sets the value for PpsmRegistryNumber to be an explicit nil

### UnsetPpsmRegistryNumber
`func (o *Systems) UnsetPpsmRegistryNumber()`

UnsetPpsmRegistryNumber ensures that no value is present for PpsmRegistryNumber, not even an explicit nil
### GetPpsmRegistrationExemptionJustification

`func (o *Systems) GetPpsmRegistrationExemptionJustification() string`

GetPpsmRegistrationExemptionJustification returns the PpsmRegistrationExemptionJustification field if non-nil, zero value otherwise.

### GetPpsmRegistrationExemptionJustificationOk

`func (o *Systems) GetPpsmRegistrationExemptionJustificationOk() (*string, bool)`

GetPpsmRegistrationExemptionJustificationOk returns a tuple with the PpsmRegistrationExemptionJustification field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPpsmRegistrationExemptionJustification

`func (o *Systems) SetPpsmRegistrationExemptionJustification(v string)`

SetPpsmRegistrationExemptionJustification sets PpsmRegistrationExemptionJustification field to given value.

### HasPpsmRegistrationExemptionJustification

`func (o *Systems) HasPpsmRegistrationExemptionJustification() bool`

HasPpsmRegistrationExemptionJustification returns a boolean if a field has been set.

### SetPpsmRegistrationExemptionJustificationNil

`func (o *Systems) SetPpsmRegistrationExemptionJustificationNil(b bool)`

 SetPpsmRegistrationExemptionJustificationNil sets the value for PpsmRegistrationExemptionJustification to be an explicit nil

### UnsetPpsmRegistrationExemptionJustification
`func (o *Systems) UnsetPpsmRegistrationExemptionJustification()`

UnsetPpsmRegistrationExemptionJustification ensures that no value is present for PpsmRegistrationExemptionJustification, not even an explicit nil
### GetInterconnectedInformationSystemAndIdentifiers

`func (o *Systems) GetInterconnectedInformationSystemAndIdentifiers() string`

GetInterconnectedInformationSystemAndIdentifiers returns the InterconnectedInformationSystemAndIdentifiers field if non-nil, zero value otherwise.

### GetInterconnectedInformationSystemAndIdentifiersOk

`func (o *Systems) GetInterconnectedInformationSystemAndIdentifiersOk() (*string, bool)`

GetInterconnectedInformationSystemAndIdentifiersOk returns a tuple with the InterconnectedInformationSystemAndIdentifiers field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetInterconnectedInformationSystemAndIdentifiers

`func (o *Systems) SetInterconnectedInformationSystemAndIdentifiers(v string)`

SetInterconnectedInformationSystemAndIdentifiers sets InterconnectedInformationSystemAndIdentifiers field to given value.

### HasInterconnectedInformationSystemAndIdentifiers

`func (o *Systems) HasInterconnectedInformationSystemAndIdentifiers() bool`

HasInterconnectedInformationSystemAndIdentifiers returns a boolean if a field has been set.

### SetInterconnectedInformationSystemAndIdentifiersNil

`func (o *Systems) SetInterconnectedInformationSystemAndIdentifiersNil(b bool)`

 SetInterconnectedInformationSystemAndIdentifiersNil sets the value for InterconnectedInformationSystemAndIdentifiers to be an explicit nil

### UnsetInterconnectedInformationSystemAndIdentifiers
`func (o *Systems) UnsetInterconnectedInformationSystemAndIdentifiers()`

UnsetInterconnectedInformationSystemAndIdentifiers ensures that no value is present for InterconnectedInformationSystemAndIdentifiers, not even an explicit nil
### GetPrivacyImpactAssessmentRequired

`func (o *Systems) GetPrivacyImpactAssessmentRequired() bool`

GetPrivacyImpactAssessmentRequired returns the PrivacyImpactAssessmentRequired field if non-nil, zero value otherwise.

### GetPrivacyImpactAssessmentRequiredOk

`func (o *Systems) GetPrivacyImpactAssessmentRequiredOk() (*bool, bool)`

GetPrivacyImpactAssessmentRequiredOk returns a tuple with the PrivacyImpactAssessmentRequired field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPrivacyImpactAssessmentRequired

`func (o *Systems) SetPrivacyImpactAssessmentRequired(v bool)`

SetPrivacyImpactAssessmentRequired sets PrivacyImpactAssessmentRequired field to given value.

### HasPrivacyImpactAssessmentRequired

`func (o *Systems) HasPrivacyImpactAssessmentRequired() bool`

HasPrivacyImpactAssessmentRequired returns a boolean if a field has been set.

### SetPrivacyImpactAssessmentRequiredNil

`func (o *Systems) SetPrivacyImpactAssessmentRequiredNil(b bool)`

 SetPrivacyImpactAssessmentRequiredNil sets the value for PrivacyImpactAssessmentRequired to be an explicit nil

### UnsetPrivacyImpactAssessmentRequired
`func (o *Systems) UnsetPrivacyImpactAssessmentRequired()`

UnsetPrivacyImpactAssessmentRequired ensures that no value is present for PrivacyImpactAssessmentRequired, not even an explicit nil
### GetPrivacyImpactAssessmentStatus

`func (o *Systems) GetPrivacyImpactAssessmentStatus() string`

GetPrivacyImpactAssessmentStatus returns the PrivacyImpactAssessmentStatus field if non-nil, zero value otherwise.

### GetPrivacyImpactAssessmentStatusOk

`func (o *Systems) GetPrivacyImpactAssessmentStatusOk() (*string, bool)`

GetPrivacyImpactAssessmentStatusOk returns a tuple with the PrivacyImpactAssessmentStatus field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPrivacyImpactAssessmentStatus

`func (o *Systems) SetPrivacyImpactAssessmentStatus(v string)`

SetPrivacyImpactAssessmentStatus sets PrivacyImpactAssessmentStatus field to given value.

### HasPrivacyImpactAssessmentStatus

`func (o *Systems) HasPrivacyImpactAssessmentStatus() bool`

HasPrivacyImpactAssessmentStatus returns a boolean if a field has been set.

### SetPrivacyImpactAssessmentStatusNil

`func (o *Systems) SetPrivacyImpactAssessmentStatusNil(b bool)`

 SetPrivacyImpactAssessmentStatusNil sets the value for PrivacyImpactAssessmentStatus to be an explicit nil

### UnsetPrivacyImpactAssessmentStatus
`func (o *Systems) UnsetPrivacyImpactAssessmentStatus()`

UnsetPrivacyImpactAssessmentStatus ensures that no value is present for PrivacyImpactAssessmentStatus, not even an explicit nil
### GetPrivacyImpactAssessmentDate

`func (o *Systems) GetPrivacyImpactAssessmentDate() int32`

GetPrivacyImpactAssessmentDate returns the PrivacyImpactAssessmentDate field if non-nil, zero value otherwise.

### GetPrivacyImpactAssessmentDateOk

`func (o *Systems) GetPrivacyImpactAssessmentDateOk() (*int32, bool)`

GetPrivacyImpactAssessmentDateOk returns a tuple with the PrivacyImpactAssessmentDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPrivacyImpactAssessmentDate

`func (o *Systems) SetPrivacyImpactAssessmentDate(v int32)`

SetPrivacyImpactAssessmentDate sets PrivacyImpactAssessmentDate field to given value.

### HasPrivacyImpactAssessmentDate

`func (o *Systems) HasPrivacyImpactAssessmentDate() bool`

HasPrivacyImpactAssessmentDate returns a boolean if a field has been set.

### SetPrivacyImpactAssessmentDateNil

`func (o *Systems) SetPrivacyImpactAssessmentDateNil(b bool)`

 SetPrivacyImpactAssessmentDateNil sets the value for PrivacyImpactAssessmentDate to be an explicit nil

### UnsetPrivacyImpactAssessmentDate
`func (o *Systems) UnsetPrivacyImpactAssessmentDate()`

UnsetPrivacyImpactAssessmentDate ensures that no value is present for PrivacyImpactAssessmentDate, not even an explicit nil
### GetPrivacyImpactAssessmentArtifact

`func (o *Systems) GetPrivacyImpactAssessmentArtifact() string`

GetPrivacyImpactAssessmentArtifact returns the PrivacyImpactAssessmentArtifact field if non-nil, zero value otherwise.

### GetPrivacyImpactAssessmentArtifactOk

`func (o *Systems) GetPrivacyImpactAssessmentArtifactOk() (*string, bool)`

GetPrivacyImpactAssessmentArtifactOk returns a tuple with the PrivacyImpactAssessmentArtifact field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPrivacyImpactAssessmentArtifact

`func (o *Systems) SetPrivacyImpactAssessmentArtifact(v string)`

SetPrivacyImpactAssessmentArtifact sets PrivacyImpactAssessmentArtifact field to given value.

### HasPrivacyImpactAssessmentArtifact

`func (o *Systems) HasPrivacyImpactAssessmentArtifact() bool`

HasPrivacyImpactAssessmentArtifact returns a boolean if a field has been set.

### SetPrivacyImpactAssessmentArtifactNil

`func (o *Systems) SetPrivacyImpactAssessmentArtifactNil(b bool)`

 SetPrivacyImpactAssessmentArtifactNil sets the value for PrivacyImpactAssessmentArtifact to be an explicit nil

### UnsetPrivacyImpactAssessmentArtifact
`func (o *Systems) UnsetPrivacyImpactAssessmentArtifact()`

UnsetPrivacyImpactAssessmentArtifact ensures that no value is present for PrivacyImpactAssessmentArtifact, not even an explicit nil
### GetUserDefinedField1

`func (o *Systems) GetUserDefinedField1() string`

GetUserDefinedField1 returns the UserDefinedField1 field if non-nil, zero value otherwise.

### GetUserDefinedField1Ok

`func (o *Systems) GetUserDefinedField1Ok() (*string, bool)`

GetUserDefinedField1Ok returns a tuple with the UserDefinedField1 field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUserDefinedField1

`func (o *Systems) SetUserDefinedField1(v string)`

SetUserDefinedField1 sets UserDefinedField1 field to given value.

### HasUserDefinedField1

`func (o *Systems) HasUserDefinedField1() bool`

HasUserDefinedField1 returns a boolean if a field has been set.

### SetUserDefinedField1Nil

`func (o *Systems) SetUserDefinedField1Nil(b bool)`

 SetUserDefinedField1Nil sets the value for UserDefinedField1 to be an explicit nil

### UnsetUserDefinedField1
`func (o *Systems) UnsetUserDefinedField1()`

UnsetUserDefinedField1 ensures that no value is present for UserDefinedField1, not even an explicit nil
### GetUserDefinedField2

`func (o *Systems) GetUserDefinedField2() string`

GetUserDefinedField2 returns the UserDefinedField2 field if non-nil, zero value otherwise.

### GetUserDefinedField2Ok

`func (o *Systems) GetUserDefinedField2Ok() (*string, bool)`

GetUserDefinedField2Ok returns a tuple with the UserDefinedField2 field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUserDefinedField2

`func (o *Systems) SetUserDefinedField2(v string)`

SetUserDefinedField2 sets UserDefinedField2 field to given value.

### HasUserDefinedField2

`func (o *Systems) HasUserDefinedField2() bool`

HasUserDefinedField2 returns a boolean if a field has been set.

### SetUserDefinedField2Nil

`func (o *Systems) SetUserDefinedField2Nil(b bool)`

 SetUserDefinedField2Nil sets the value for UserDefinedField2 to be an explicit nil

### UnsetUserDefinedField2
`func (o *Systems) UnsetUserDefinedField2()`

UnsetUserDefinedField2 ensures that no value is present for UserDefinedField2, not even an explicit nil
### GetUserDefinedField3

`func (o *Systems) GetUserDefinedField3() string`

GetUserDefinedField3 returns the UserDefinedField3 field if non-nil, zero value otherwise.

### GetUserDefinedField3Ok

`func (o *Systems) GetUserDefinedField3Ok() (*string, bool)`

GetUserDefinedField3Ok returns a tuple with the UserDefinedField3 field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUserDefinedField3

`func (o *Systems) SetUserDefinedField3(v string)`

SetUserDefinedField3 sets UserDefinedField3 field to given value.

### HasUserDefinedField3

`func (o *Systems) HasUserDefinedField3() bool`

HasUserDefinedField3 returns a boolean if a field has been set.

### SetUserDefinedField3Nil

`func (o *Systems) SetUserDefinedField3Nil(b bool)`

 SetUserDefinedField3Nil sets the value for UserDefinedField3 to be an explicit nil

### UnsetUserDefinedField3
`func (o *Systems) UnsetUserDefinedField3()`

UnsetUserDefinedField3 ensures that no value is present for UserDefinedField3, not even an explicit nil
### GetUserDefinedField4

`func (o *Systems) GetUserDefinedField4() string`

GetUserDefinedField4 returns the UserDefinedField4 field if non-nil, zero value otherwise.

### GetUserDefinedField4Ok

`func (o *Systems) GetUserDefinedField4Ok() (*string, bool)`

GetUserDefinedField4Ok returns a tuple with the UserDefinedField4 field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUserDefinedField4

`func (o *Systems) SetUserDefinedField4(v string)`

SetUserDefinedField4 sets UserDefinedField4 field to given value.

### HasUserDefinedField4

`func (o *Systems) HasUserDefinedField4() bool`

HasUserDefinedField4 returns a boolean if a field has been set.

### SetUserDefinedField4Nil

`func (o *Systems) SetUserDefinedField4Nil(b bool)`

 SetUserDefinedField4Nil sets the value for UserDefinedField4 to be an explicit nil

### UnsetUserDefinedField4
`func (o *Systems) UnsetUserDefinedField4()`

UnsetUserDefinedField4 ensures that no value is present for UserDefinedField4, not even an explicit nil
### GetUserDefinedField5

`func (o *Systems) GetUserDefinedField5() string`

GetUserDefinedField5 returns the UserDefinedField5 field if non-nil, zero value otherwise.

### GetUserDefinedField5Ok

`func (o *Systems) GetUserDefinedField5Ok() (*string, bool)`

GetUserDefinedField5Ok returns a tuple with the UserDefinedField5 field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUserDefinedField5

`func (o *Systems) SetUserDefinedField5(v string)`

SetUserDefinedField5 sets UserDefinedField5 field to given value.

### HasUserDefinedField5

`func (o *Systems) HasUserDefinedField5() bool`

HasUserDefinedField5 returns a boolean if a field has been set.

### SetUserDefinedField5Nil

`func (o *Systems) SetUserDefinedField5Nil(b bool)`

 SetUserDefinedField5Nil sets the value for UserDefinedField5 to be an explicit nil

### UnsetUserDefinedField5
`func (o *Systems) UnsetUserDefinedField5()`

UnsetUserDefinedField5 ensures that no value is present for UserDefinedField5, not even an explicit nil
### GetCurrentRmfLifecycleStep

`func (o *Systems) GetCurrentRmfLifecycleStep() string`

GetCurrentRmfLifecycleStep returns the CurrentRmfLifecycleStep field if non-nil, zero value otherwise.

### GetCurrentRmfLifecycleStepOk

`func (o *Systems) GetCurrentRmfLifecycleStepOk() (*string, bool)`

GetCurrentRmfLifecycleStepOk returns a tuple with the CurrentRmfLifecycleStep field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCurrentRmfLifecycleStep

`func (o *Systems) SetCurrentRmfLifecycleStep(v string)`

SetCurrentRmfLifecycleStep sets CurrentRmfLifecycleStep field to given value.

### HasCurrentRmfLifecycleStep

`func (o *Systems) HasCurrentRmfLifecycleStep() bool`

HasCurrentRmfLifecycleStep returns a boolean if a field has been set.

### SetCurrentRmfLifecycleStepNil

`func (o *Systems) SetCurrentRmfLifecycleStepNil(b bool)`

 SetCurrentRmfLifecycleStepNil sets the value for CurrentRmfLifecycleStep to be an explicit nil

### UnsetCurrentRmfLifecycleStep
`func (o *Systems) UnsetCurrentRmfLifecycleStep()`

UnsetCurrentRmfLifecycleStep ensures that no value is present for CurrentRmfLifecycleStep, not even an explicit nil
### GetOtherInformation

`func (o *Systems) GetOtherInformation() string`

GetOtherInformation returns the OtherInformation field if non-nil, zero value otherwise.

### GetOtherInformationOk

`func (o *Systems) GetOtherInformationOk() (*string, bool)`

GetOtherInformationOk returns a tuple with the OtherInformation field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOtherInformation

`func (o *Systems) SetOtherInformation(v string)`

SetOtherInformation sets OtherInformation field to given value.

### HasOtherInformation

`func (o *Systems) HasOtherInformation() bool`

HasOtherInformation returns a boolean if a field has been set.

### SetOtherInformationNil

`func (o *Systems) SetOtherInformationNil(b bool)`

 SetOtherInformationNil sets the value for OtherInformation to be an explicit nil

### UnsetOtherInformation
`func (o *Systems) UnsetOtherInformation()`

UnsetOtherInformation ensures that no value is present for OtherInformation, not even an explicit nil
### GetReportsForScorecard

`func (o *Systems) GetReportsForScorecard() bool`

GetReportsForScorecard returns the ReportsForScorecard field if non-nil, zero value otherwise.

### GetReportsForScorecardOk

`func (o *Systems) GetReportsForScorecardOk() (*bool, bool)`

GetReportsForScorecardOk returns a tuple with the ReportsForScorecard field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetReportsForScorecard

`func (o *Systems) SetReportsForScorecard(v bool)`

SetReportsForScorecard sets ReportsForScorecard field to given value.

### HasReportsForScorecard

`func (o *Systems) HasReportsForScorecard() bool`

HasReportsForScorecard returns a boolean if a field has been set.

### SetReportsForScorecardNil

`func (o *Systems) SetReportsForScorecardNil(b bool)`

 SetReportsForScorecardNil sets the value for ReportsForScorecard to be an explicit nil

### UnsetReportsForScorecard
`func (o *Systems) UnsetReportsForScorecard()`

UnsetReportsForScorecard ensures that no value is present for ReportsForScorecard, not even an explicit nil
### GetHighestSystemDataClassification

`func (o *Systems) GetHighestSystemDataClassification() string`

GetHighestSystemDataClassification returns the HighestSystemDataClassification field if non-nil, zero value otherwise.

### GetHighestSystemDataClassificationOk

`func (o *Systems) GetHighestSystemDataClassificationOk() (*string, bool)`

GetHighestSystemDataClassificationOk returns a tuple with the HighestSystemDataClassification field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHighestSystemDataClassification

`func (o *Systems) SetHighestSystemDataClassification(v string)`

SetHighestSystemDataClassification sets HighestSystemDataClassification field to given value.

### HasHighestSystemDataClassification

`func (o *Systems) HasHighestSystemDataClassification() bool`

HasHighestSystemDataClassification returns a boolean if a field has been set.

### SetHighestSystemDataClassificationNil

`func (o *Systems) SetHighestSystemDataClassificationNil(b bool)`

 SetHighestSystemDataClassificationNil sets the value for HighestSystemDataClassification to be an explicit nil

### UnsetHighestSystemDataClassification
`func (o *Systems) UnsetHighestSystemDataClassification()`

UnsetHighestSystemDataClassification ensures that no value is present for HighestSystemDataClassification, not even an explicit nil
### GetOverallClassification

`func (o *Systems) GetOverallClassification() string`

GetOverallClassification returns the OverallClassification field if non-nil, zero value otherwise.

### GetOverallClassificationOk

`func (o *Systems) GetOverallClassificationOk() (*string, bool)`

GetOverallClassificationOk returns a tuple with the OverallClassification field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOverallClassification

`func (o *Systems) SetOverallClassification(v string)`

SetOverallClassification sets OverallClassification field to given value.

### HasOverallClassification

`func (o *Systems) HasOverallClassification() bool`

HasOverallClassification returns a boolean if a field has been set.

### SetOverallClassificationNil

`func (o *Systems) SetOverallClassificationNil(b bool)`

 SetOverallClassificationNil sets the value for OverallClassification to be an explicit nil

### UnsetOverallClassification
`func (o *Systems) UnsetOverallClassification()`

UnsetOverallClassification ensures that no value is present for OverallClassification, not even an explicit nil
### GetIsHVA

`func (o *Systems) GetIsHVA() bool`

GetIsHVA returns the IsHVA field if non-nil, zero value otherwise.

### GetIsHVAOk

`func (o *Systems) GetIsHVAOk() (*bool, bool)`

GetIsHVAOk returns a tuple with the IsHVA field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsHVA

`func (o *Systems) SetIsHVA(v bool)`

SetIsHVA sets IsHVA field to given value.

### HasIsHVA

`func (o *Systems) HasIsHVA() bool`

HasIsHVA returns a boolean if a field has been set.

### SetIsHVANil

`func (o *Systems) SetIsHVANil(b bool)`

 SetIsHVANil sets the value for IsHVA to be an explicit nil

### UnsetIsHVA
`func (o *Systems) UnsetIsHVA()`

UnsetIsHVA ensures that no value is present for IsHVA, not even an explicit nil
### GetIsFinancialManagement

`func (o *Systems) GetIsFinancialManagement() bool`

GetIsFinancialManagement returns the IsFinancialManagement field if non-nil, zero value otherwise.

### GetIsFinancialManagementOk

`func (o *Systems) GetIsFinancialManagementOk() (*bool, bool)`

GetIsFinancialManagementOk returns a tuple with the IsFinancialManagement field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsFinancialManagement

`func (o *Systems) SetIsFinancialManagement(v bool)`

SetIsFinancialManagement sets IsFinancialManagement field to given value.

### HasIsFinancialManagement

`func (o *Systems) HasIsFinancialManagement() bool`

HasIsFinancialManagement returns a boolean if a field has been set.

### SetIsFinancialManagementNil

`func (o *Systems) SetIsFinancialManagementNil(b bool)`

 SetIsFinancialManagementNil sets the value for IsFinancialManagement to be an explicit nil

### UnsetIsFinancialManagement
`func (o *Systems) UnsetIsFinancialManagement()`

UnsetIsFinancialManagement ensures that no value is present for IsFinancialManagement, not even an explicit nil
### GetIsReciprocity

`func (o *Systems) GetIsReciprocity() bool`

GetIsReciprocity returns the IsReciprocity field if non-nil, zero value otherwise.

### GetIsReciprocityOk

`func (o *Systems) GetIsReciprocityOk() (*bool, bool)`

GetIsReciprocityOk returns a tuple with the IsReciprocity field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsReciprocity

`func (o *Systems) SetIsReciprocity(v bool)`

SetIsReciprocity sets IsReciprocity field to given value.

### HasIsReciprocity

`func (o *Systems) HasIsReciprocity() bool`

HasIsReciprocity returns a boolean if a field has been set.

### SetIsReciprocityNil

`func (o *Systems) SetIsReciprocityNil(b bool)`

 SetIsReciprocityNil sets the value for IsReciprocity to be an explicit nil

### UnsetIsReciprocity
`func (o *Systems) UnsetIsReciprocity()`

UnsetIsReciprocity ensures that no value is present for IsReciprocity, not even an explicit nil
### GetReciprocityExemption

`func (o *Systems) GetReciprocityExemption() string`

GetReciprocityExemption returns the ReciprocityExemption field if non-nil, zero value otherwise.

### GetReciprocityExemptionOk

`func (o *Systems) GetReciprocityExemptionOk() (*string, bool)`

GetReciprocityExemptionOk returns a tuple with the ReciprocityExemption field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetReciprocityExemption

`func (o *Systems) SetReciprocityExemption(v string)`

SetReciprocityExemption sets ReciprocityExemption field to given value.

### HasReciprocityExemption

`func (o *Systems) HasReciprocityExemption() bool`

HasReciprocityExemption returns a boolean if a field has been set.

### SetReciprocityExemptionNil

`func (o *Systems) SetReciprocityExemptionNil(b bool)`

 SetReciprocityExemptionNil sets the value for ReciprocityExemption to be an explicit nil

### UnsetReciprocityExemption
`func (o *Systems) UnsetReciprocityExemption()`

UnsetReciprocityExemption ensures that no value is present for ReciprocityExemption, not even an explicit nil
### GetCloudComputing

`func (o *Systems) GetCloudComputing() bool`

GetCloudComputing returns the CloudComputing field if non-nil, zero value otherwise.

### GetCloudComputingOk

`func (o *Systems) GetCloudComputingOk() (*bool, bool)`

GetCloudComputingOk returns a tuple with the CloudComputing field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCloudComputing

`func (o *Systems) SetCloudComputing(v bool)`

SetCloudComputing sets CloudComputing field to given value.

### HasCloudComputing

`func (o *Systems) HasCloudComputing() bool`

HasCloudComputing returns a boolean if a field has been set.

### SetCloudComputingNil

`func (o *Systems) SetCloudComputingNil(b bool)`

 SetCloudComputingNil sets the value for CloudComputing to be an explicit nil

### UnsetCloudComputing
`func (o *Systems) UnsetCloudComputing()`

UnsetCloudComputing ensures that no value is present for CloudComputing, not even an explicit nil
### GetCloudType

`func (o *Systems) GetCloudType() string`

GetCloudType returns the CloudType field if non-nil, zero value otherwise.

### GetCloudTypeOk

`func (o *Systems) GetCloudTypeOk() (*string, bool)`

GetCloudTypeOk returns a tuple with the CloudType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCloudType

`func (o *Systems) SetCloudType(v string)`

SetCloudType sets CloudType field to given value.

### HasCloudType

`func (o *Systems) HasCloudType() bool`

HasCloudType returns a boolean if a field has been set.

### SetCloudTypeNil

`func (o *Systems) SetCloudTypeNil(b bool)`

 SetCloudTypeNil sets the value for CloudType to be an explicit nil

### UnsetCloudType
`func (o *Systems) UnsetCloudType()`

UnsetCloudType ensures that no value is present for CloudType, not even an explicit nil
### GetAuthorizationToConnectStatus

`func (o *Systems) GetAuthorizationToConnectStatus() string`

GetAuthorizationToConnectStatus returns the AuthorizationToConnectStatus field if non-nil, zero value otherwise.

### GetAuthorizationToConnectStatusOk

`func (o *Systems) GetAuthorizationToConnectStatusOk() (*string, bool)`

GetAuthorizationToConnectStatusOk returns a tuple with the AuthorizationToConnectStatus field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAuthorizationToConnectStatus

`func (o *Systems) SetAuthorizationToConnectStatus(v string)`

SetAuthorizationToConnectStatus sets AuthorizationToConnectStatus field to given value.

### HasAuthorizationToConnectStatus

`func (o *Systems) HasAuthorizationToConnectStatus() bool`

HasAuthorizationToConnectStatus returns a boolean if a field has been set.

### SetAuthorizationToConnectStatusNil

`func (o *Systems) SetAuthorizationToConnectStatusNil(b bool)`

 SetAuthorizationToConnectStatusNil sets the value for AuthorizationToConnectStatus to be an explicit nil

### UnsetAuthorizationToConnectStatus
`func (o *Systems) UnsetAuthorizationToConnectStatus()`

UnsetAuthorizationToConnectStatus ensures that no value is present for AuthorizationToConnectStatus, not even an explicit nil
### GetIsSaaS

`func (o *Systems) GetIsSaaS() bool`

GetIsSaaS returns the IsSaaS field if non-nil, zero value otherwise.

### GetIsSaaSOk

`func (o *Systems) GetIsSaaSOk() (*bool, bool)`

GetIsSaaSOk returns a tuple with the IsSaaS field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsSaaS

`func (o *Systems) SetIsSaaS(v bool)`

SetIsSaaS sets IsSaaS field to given value.

### HasIsSaaS

`func (o *Systems) HasIsSaaS() bool`

HasIsSaaS returns a boolean if a field has been set.

### SetIsSaaSNil

`func (o *Systems) SetIsSaaSNil(b bool)`

 SetIsSaaSNil sets the value for IsSaaS to be an explicit nil

### UnsetIsSaaS
`func (o *Systems) UnsetIsSaaS()`

UnsetIsSaaS ensures that no value is present for IsSaaS, not even an explicit nil
### GetIsPaaS

`func (o *Systems) GetIsPaaS() bool`

GetIsPaaS returns the IsPaaS field if non-nil, zero value otherwise.

### GetIsPaaSOk

`func (o *Systems) GetIsPaaSOk() (*bool, bool)`

GetIsPaaSOk returns a tuple with the IsPaaS field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsPaaS

`func (o *Systems) SetIsPaaS(v bool)`

SetIsPaaS sets IsPaaS field to given value.

### HasIsPaaS

`func (o *Systems) HasIsPaaS() bool`

HasIsPaaS returns a boolean if a field has been set.

### SetIsPaaSNil

`func (o *Systems) SetIsPaaSNil(b bool)`

 SetIsPaaSNil sets the value for IsPaaS to be an explicit nil

### UnsetIsPaaS
`func (o *Systems) UnsetIsPaaS()`

UnsetIsPaaS ensures that no value is present for IsPaaS, not even an explicit nil
### GetIsIaaS

`func (o *Systems) GetIsIaaS() bool`

GetIsIaaS returns the IsIaaS field if non-nil, zero value otherwise.

### GetIsIaaSOk

`func (o *Systems) GetIsIaaSOk() (*bool, bool)`

GetIsIaaSOk returns a tuple with the IsIaaS field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsIaaS

`func (o *Systems) SetIsIaaS(v bool)`

SetIsIaaS sets IsIaaS field to given value.

### HasIsIaaS

`func (o *Systems) HasIsIaaS() bool`

HasIsIaaS returns a boolean if a field has been set.

### SetIsIaaSNil

`func (o *Systems) SetIsIaaSNil(b bool)`

 SetIsIaaSNil sets the value for IsIaaS to be an explicit nil

### UnsetIsIaaS
`func (o *Systems) UnsetIsIaaS()`

UnsetIsIaaS ensures that no value is present for IsIaaS, not even an explicit nil
### GetOtherServiceModels

`func (o *Systems) GetOtherServiceModels() string`

GetOtherServiceModels returns the OtherServiceModels field if non-nil, zero value otherwise.

### GetOtherServiceModelsOk

`func (o *Systems) GetOtherServiceModelsOk() (*string, bool)`

GetOtherServiceModelsOk returns a tuple with the OtherServiceModels field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOtherServiceModels

`func (o *Systems) SetOtherServiceModels(v string)`

SetOtherServiceModels sets OtherServiceModels field to given value.

### HasOtherServiceModels

`func (o *Systems) HasOtherServiceModels() bool`

HasOtherServiceModels returns a boolean if a field has been set.

### SetOtherServiceModelsNil

`func (o *Systems) SetOtherServiceModelsNil(b bool)`

 SetOtherServiceModelsNil sets the value for OtherServiceModels to be an explicit nil

### UnsetOtherServiceModels
`func (o *Systems) UnsetOtherServiceModels()`

UnsetOtherServiceModels ensures that no value is present for OtherServiceModels, not even an explicit nil
### GetNeedDate

`func (o *Systems) GetNeedDate() int32`

GetNeedDate returns the NeedDate field if non-nil, zero value otherwise.

### GetNeedDateOk

`func (o *Systems) GetNeedDateOk() (*int32, bool)`

GetNeedDateOk returns a tuple with the NeedDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNeedDate

`func (o *Systems) SetNeedDate(v int32)`

SetNeedDate sets NeedDate field to given value.

### HasNeedDate

`func (o *Systems) HasNeedDate() bool`

HasNeedDate returns a boolean if a field has been set.

### SetNeedDateNil

`func (o *Systems) SetNeedDateNil(b bool)`

 SetNeedDateNil sets the value for NeedDate to be an explicit nil

### UnsetNeedDate
`func (o *Systems) UnsetNeedDate()`

UnsetNeedDate ensures that no value is present for NeedDate, not even an explicit nil
### GetOverallRiskScore

`func (o *Systems) GetOverallRiskScore() string`

GetOverallRiskScore returns the OverallRiskScore field if non-nil, zero value otherwise.

### GetOverallRiskScoreOk

`func (o *Systems) GetOverallRiskScoreOk() (*string, bool)`

GetOverallRiskScoreOk returns a tuple with the OverallRiskScore field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOverallRiskScore

`func (o *Systems) SetOverallRiskScore(v string)`

SetOverallRiskScore sets OverallRiskScore field to given value.

### HasOverallRiskScore

`func (o *Systems) HasOverallRiskScore() bool`

HasOverallRiskScore returns a boolean if a field has been set.

### SetOverallRiskScoreNil

`func (o *Systems) SetOverallRiskScoreNil(b bool)`

 SetOverallRiskScoreNil sets the value for OverallRiskScore to be an explicit nil

### UnsetOverallRiskScore
`func (o *Systems) UnsetOverallRiskScore()`

UnsetOverallRiskScore ensures that no value is present for OverallRiskScore, not even an explicit nil
### GetIsHRR

`func (o *Systems) GetIsHRR() bool`

GetIsHRR returns the IsHRR field if non-nil, zero value otherwise.

### GetIsHRROk

`func (o *Systems) GetIsHRROk() (*bool, bool)`

GetIsHRROk returns a tuple with the IsHRR field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsHRR

`func (o *Systems) SetIsHRR(v bool)`

SetIsHRR sets IsHRR field to given value.

### HasIsHRR

`func (o *Systems) HasIsHRR() bool`

HasIsHRR returns a boolean if a field has been set.

### SetIsHRRNil

`func (o *Systems) SetIsHRRNil(b bool)`

 SetIsHRRNil sets the value for IsHRR to be an explicit nil

### UnsetIsHRR
`func (o *Systems) UnsetIsHRR()`

UnsetIsHRR ensures that no value is present for IsHRR, not even an explicit nil
### GetConnectivityAuthorizationDate

`func (o *Systems) GetConnectivityAuthorizationDate() int32`

GetConnectivityAuthorizationDate returns the ConnectivityAuthorizationDate field if non-nil, zero value otherwise.

### GetConnectivityAuthorizationDateOk

`func (o *Systems) GetConnectivityAuthorizationDateOk() (*int32, bool)`

GetConnectivityAuthorizationDateOk returns a tuple with the ConnectivityAuthorizationDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetConnectivityAuthorizationDate

`func (o *Systems) SetConnectivityAuthorizationDate(v int32)`

SetConnectivityAuthorizationDate sets ConnectivityAuthorizationDate field to given value.

### HasConnectivityAuthorizationDate

`func (o *Systems) HasConnectivityAuthorizationDate() bool`

HasConnectivityAuthorizationDate returns a boolean if a field has been set.

### SetConnectivityAuthorizationDateNil

`func (o *Systems) SetConnectivityAuthorizationDateNil(b bool)`

 SetConnectivityAuthorizationDateNil sets the value for ConnectivityAuthorizationDate to be an explicit nil

### UnsetConnectivityAuthorizationDate
`func (o *Systems) UnsetConnectivityAuthorizationDate()`

UnsetConnectivityAuthorizationDate ensures that no value is present for ConnectivityAuthorizationDate, not even an explicit nil
### GetConnectivityAuthorizationTerminationDate

`func (o *Systems) GetConnectivityAuthorizationTerminationDate() int32`

GetConnectivityAuthorizationTerminationDate returns the ConnectivityAuthorizationTerminationDate field if non-nil, zero value otherwise.

### GetConnectivityAuthorizationTerminationDateOk

`func (o *Systems) GetConnectivityAuthorizationTerminationDateOk() (*int32, bool)`

GetConnectivityAuthorizationTerminationDateOk returns a tuple with the ConnectivityAuthorizationTerminationDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetConnectivityAuthorizationTerminationDate

`func (o *Systems) SetConnectivityAuthorizationTerminationDate(v int32)`

SetConnectivityAuthorizationTerminationDate sets ConnectivityAuthorizationTerminationDate field to given value.

### HasConnectivityAuthorizationTerminationDate

`func (o *Systems) HasConnectivityAuthorizationTerminationDate() bool`

HasConnectivityAuthorizationTerminationDate returns a boolean if a field has been set.

### SetConnectivityAuthorizationTerminationDateNil

`func (o *Systems) SetConnectivityAuthorizationTerminationDateNil(b bool)`

 SetConnectivityAuthorizationTerminationDateNil sets the value for ConnectivityAuthorizationTerminationDate to be an explicit nil

### UnsetConnectivityAuthorizationTerminationDate
`func (o *Systems) UnsetConnectivityAuthorizationTerminationDate()`

UnsetConnectivityAuthorizationTerminationDate ensures that no value is present for ConnectivityAuthorizationTerminationDate, not even an explicit nil
### GetSystemDevelopmentLifeCycle

`func (o *Systems) GetSystemDevelopmentLifeCycle() string`

GetSystemDevelopmentLifeCycle returns the SystemDevelopmentLifeCycle field if non-nil, zero value otherwise.

### GetSystemDevelopmentLifeCycleOk

`func (o *Systems) GetSystemDevelopmentLifeCycleOk() (*string, bool)`

GetSystemDevelopmentLifeCycleOk returns a tuple with the SystemDevelopmentLifeCycle field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSystemDevelopmentLifeCycle

`func (o *Systems) SetSystemDevelopmentLifeCycle(v string)`

SetSystemDevelopmentLifeCycle sets SystemDevelopmentLifeCycle field to given value.

### HasSystemDevelopmentLifeCycle

`func (o *Systems) HasSystemDevelopmentLifeCycle() bool`

HasSystemDevelopmentLifeCycle returns a boolean if a field has been set.

### SetSystemDevelopmentLifeCycleNil

`func (o *Systems) SetSystemDevelopmentLifeCycleNil(b bool)`

 SetSystemDevelopmentLifeCycleNil sets the value for SystemDevelopmentLifeCycle to be an explicit nil

### UnsetSystemDevelopmentLifeCycle
`func (o *Systems) UnsetSystemDevelopmentLifeCycle()`

UnsetSystemDevelopmentLifeCycle ensures that no value is present for SystemDevelopmentLifeCycle, not even an explicit nil
### GetIsFISMAReportable

`func (o *Systems) GetIsFISMAReportable() bool`

GetIsFISMAReportable returns the IsFISMAReportable field if non-nil, zero value otherwise.

### GetIsFISMAReportableOk

`func (o *Systems) GetIsFISMAReportableOk() (*bool, bool)`

GetIsFISMAReportableOk returns a tuple with the IsFISMAReportable field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsFISMAReportable

`func (o *Systems) SetIsFISMAReportable(v bool)`

SetIsFISMAReportable sets IsFISMAReportable field to given value.

### HasIsFISMAReportable

`func (o *Systems) HasIsFISMAReportable() bool`

HasIsFISMAReportable returns a boolean if a field has been set.

### SetIsFISMAReportableNil

`func (o *Systems) SetIsFISMAReportableNil(b bool)`

 SetIsFISMAReportableNil sets the value for IsFISMAReportable to be an explicit nil

### UnsetIsFISMAReportable
`func (o *Systems) UnsetIsFISMAReportable()`

UnsetIsFISMAReportable ensures that no value is present for IsFISMAReportable, not even an explicit nil
### GetGroupTagging

`func (o *Systems) GetGroupTagging() string`

GetGroupTagging returns the GroupTagging field if non-nil, zero value otherwise.

### GetGroupTaggingOk

`func (o *Systems) GetGroupTaggingOk() (*string, bool)`

GetGroupTaggingOk returns a tuple with the GroupTagging field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGroupTagging

`func (o *Systems) SetGroupTagging(v string)`

SetGroupTagging sets GroupTagging field to given value.

### HasGroupTagging

`func (o *Systems) HasGroupTagging() bool`

HasGroupTagging returns a boolean if a field has been set.

### SetGroupTaggingNil

`func (o *Systems) SetGroupTaggingNil(b bool)`

 SetGroupTaggingNil sets the value for GroupTagging to be an explicit nil

### UnsetGroupTagging
`func (o *Systems) UnsetGroupTagging()`

UnsetGroupTagging ensures that no value is present for GroupTagging, not even an explicit nil
### GetGroupTagDescriptions

`func (o *Systems) GetGroupTagDescriptions() string`

GetGroupTagDescriptions returns the GroupTagDescriptions field if non-nil, zero value otherwise.

### GetGroupTagDescriptionsOk

`func (o *Systems) GetGroupTagDescriptionsOk() (*string, bool)`

GetGroupTagDescriptionsOk returns a tuple with the GroupTagDescriptions field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGroupTagDescriptions

`func (o *Systems) SetGroupTagDescriptions(v string)`

SetGroupTagDescriptions sets GroupTagDescriptions field to given value.

### HasGroupTagDescriptions

`func (o *Systems) HasGroupTagDescriptions() bool`

HasGroupTagDescriptions returns a boolean if a field has been set.

### SetGroupTagDescriptionsNil

`func (o *Systems) SetGroupTagDescriptionsNil(b bool)`

 SetGroupTagDescriptionsNil sets the value for GroupTagDescriptions to be an explicit nil

### UnsetGroupTagDescriptions
`func (o *Systems) UnsetGroupTagDescriptions()`

UnsetGroupTagDescriptions ensures that no value is present for GroupTagDescriptions, not even an explicit nil
### GetDadmsId

`func (o *Systems) GetDadmsId() string`

GetDadmsId returns the DadmsId field if non-nil, zero value otherwise.

### GetDadmsIdOk

`func (o *Systems) GetDadmsIdOk() (*string, bool)`

GetDadmsIdOk returns a tuple with the DadmsId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDadmsId

`func (o *Systems) SetDadmsId(v string)`

SetDadmsId sets DadmsId field to given value.

### HasDadmsId

`func (o *Systems) HasDadmsId() bool`

HasDadmsId returns a boolean if a field has been set.

### SetDadmsIdNil

`func (o *Systems) SetDadmsIdNil(b bool)`

 SetDadmsIdNil sets the value for DadmsId to be an explicit nil

### UnsetDadmsId
`func (o *Systems) UnsetDadmsId()`

UnsetDadmsId ensures that no value is present for DadmsId, not even an explicit nil
### GetDadmsExpirationDate

`func (o *Systems) GetDadmsExpirationDate() int32`

GetDadmsExpirationDate returns the DadmsExpirationDate field if non-nil, zero value otherwise.

### GetDadmsExpirationDateOk

`func (o *Systems) GetDadmsExpirationDateOk() (*int32, bool)`

GetDadmsExpirationDateOk returns a tuple with the DadmsExpirationDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDadmsExpirationDate

`func (o *Systems) SetDadmsExpirationDate(v int32)`

SetDadmsExpirationDate sets DadmsExpirationDate field to given value.

### HasDadmsExpirationDate

`func (o *Systems) HasDadmsExpirationDate() bool`

HasDadmsExpirationDate returns a boolean if a field has been set.

### SetDadmsExpirationDateNil

`func (o *Systems) SetDadmsExpirationDateNil(b bool)`

 SetDadmsExpirationDateNil sets the value for DadmsExpirationDate to be an explicit nil

### UnsetDadmsExpirationDate
`func (o *Systems) UnsetDadmsExpirationDate()`

UnsetDadmsExpirationDate ensures that no value is present for DadmsExpirationDate, not even an explicit nil
### GetEnclaveConnectivity

`func (o *Systems) GetEnclaveConnectivity() string`

GetEnclaveConnectivity returns the EnclaveConnectivity field if non-nil, zero value otherwise.

### GetEnclaveConnectivityOk

`func (o *Systems) GetEnclaveConnectivityOk() (*string, bool)`

GetEnclaveConnectivityOk returns a tuple with the EnclaveConnectivity field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnclaveConnectivity

`func (o *Systems) SetEnclaveConnectivity(v string)`

SetEnclaveConnectivity sets EnclaveConnectivity field to given value.

### HasEnclaveConnectivity

`func (o *Systems) HasEnclaveConnectivity() bool`

HasEnclaveConnectivity returns a boolean if a field has been set.

### SetEnclaveConnectivityNil

`func (o *Systems) SetEnclaveConnectivityNil(b bool)`

 SetEnclaveConnectivityNil sets the value for EnclaveConnectivity to be an explicit nil

### UnsetEnclaveConnectivity
`func (o *Systems) UnsetEnclaveConnectivity()`

UnsetEnclaveConnectivity ensures that no value is present for EnclaveConnectivity, not even an explicit nil
### GetEnvironmentType

`func (o *Systems) GetEnvironmentType() string`

GetEnvironmentType returns the EnvironmentType field if non-nil, zero value otherwise.

### GetEnvironmentTypeOk

`func (o *Systems) GetEnvironmentTypeOk() (*string, bool)`

GetEnvironmentTypeOk returns a tuple with the EnvironmentType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnvironmentType

`func (o *Systems) SetEnvironmentType(v string)`

SetEnvironmentType sets EnvironmentType field to given value.

### HasEnvironmentType

`func (o *Systems) HasEnvironmentType() bool`

HasEnvironmentType returns a boolean if a field has been set.

### SetEnvironmentTypeNil

`func (o *Systems) SetEnvironmentTypeNil(b bool)`

 SetEnvironmentTypeNil sets the value for EnvironmentType to be an explicit nil

### UnsetEnvironmentType
`func (o *Systems) UnsetEnvironmentType()`

UnsetEnvironmentType ensures that no value is present for EnvironmentType, not even an explicit nil
### GetNavyCommonControlProvider

`func (o *Systems) GetNavyCommonControlProvider() bool`

GetNavyCommonControlProvider returns the NavyCommonControlProvider field if non-nil, zero value otherwise.

### GetNavyCommonControlProviderOk

`func (o *Systems) GetNavyCommonControlProviderOk() (*bool, bool)`

GetNavyCommonControlProviderOk returns a tuple with the NavyCommonControlProvider field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNavyCommonControlProvider

`func (o *Systems) SetNavyCommonControlProvider(v bool)`

SetNavyCommonControlProvider sets NavyCommonControlProvider field to given value.

### HasNavyCommonControlProvider

`func (o *Systems) HasNavyCommonControlProvider() bool`

HasNavyCommonControlProvider returns a boolean if a field has been set.

### SetNavyCommonControlProviderNil

`func (o *Systems) SetNavyCommonControlProviderNil(b bool)`

 SetNavyCommonControlProviderNil sets the value for NavyCommonControlProvider to be an explicit nil

### UnsetNavyCommonControlProvider
`func (o *Systems) UnsetNavyCommonControlProvider()`

UnsetNavyCommonControlProvider ensures that no value is present for NavyCommonControlProvider, not even an explicit nil
### GetNavyCloudBroker

`func (o *Systems) GetNavyCloudBroker() string`

GetNavyCloudBroker returns the NavyCloudBroker field if non-nil, zero value otherwise.

### GetNavyCloudBrokerOk

`func (o *Systems) GetNavyCloudBrokerOk() (*string, bool)`

GetNavyCloudBrokerOk returns a tuple with the NavyCloudBroker field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNavyCloudBroker

`func (o *Systems) SetNavyCloudBroker(v string)`

SetNavyCloudBroker sets NavyCloudBroker field to given value.

### HasNavyCloudBroker

`func (o *Systems) HasNavyCloudBroker() bool`

HasNavyCloudBroker returns a boolean if a field has been set.

### SetNavyCloudBrokerNil

`func (o *Systems) SetNavyCloudBrokerNil(b bool)`

 SetNavyCloudBrokerNil sets the value for NavyCloudBroker to be an explicit nil

### UnsetNavyCloudBroker
`func (o *Systems) UnsetNavyCloudBroker()`

UnsetNavyCloudBroker ensures that no value is present for NavyCloudBroker, not even an explicit nil
### GetCloudBrokerEmassId

`func (o *Systems) GetCloudBrokerEmassId() int32`

GetCloudBrokerEmassId returns the CloudBrokerEmassId field if non-nil, zero value otherwise.

### GetCloudBrokerEmassIdOk

`func (o *Systems) GetCloudBrokerEmassIdOk() (*int32, bool)`

GetCloudBrokerEmassIdOk returns a tuple with the CloudBrokerEmassId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCloudBrokerEmassId

`func (o *Systems) SetCloudBrokerEmassId(v int32)`

SetCloudBrokerEmassId sets CloudBrokerEmassId field to given value.

### HasCloudBrokerEmassId

`func (o *Systems) HasCloudBrokerEmassId() bool`

HasCloudBrokerEmassId returns a boolean if a field has been set.

### SetCloudBrokerEmassIdNil

`func (o *Systems) SetCloudBrokerEmassIdNil(b bool)`

 SetCloudBrokerEmassIdNil sets the value for CloudBrokerEmassId to be an explicit nil

### UnsetCloudBrokerEmassId
`func (o *Systems) UnsetCloudBrokerEmassId()`

UnsetCloudBrokerEmassId ensures that no value is present for CloudBrokerEmassId, not even an explicit nil
### GetCloudBrokerProvisionalAuthorizationAtd

`func (o *Systems) GetCloudBrokerProvisionalAuthorizationAtd() int32`

GetCloudBrokerProvisionalAuthorizationAtd returns the CloudBrokerProvisionalAuthorizationAtd field if non-nil, zero value otherwise.

### GetCloudBrokerProvisionalAuthorizationAtdOk

`func (o *Systems) GetCloudBrokerProvisionalAuthorizationAtdOk() (*int32, bool)`

GetCloudBrokerProvisionalAuthorizationAtdOk returns a tuple with the CloudBrokerProvisionalAuthorizationAtd field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCloudBrokerProvisionalAuthorizationAtd

`func (o *Systems) SetCloudBrokerProvisionalAuthorizationAtd(v int32)`

SetCloudBrokerProvisionalAuthorizationAtd sets CloudBrokerProvisionalAuthorizationAtd field to given value.

### HasCloudBrokerProvisionalAuthorizationAtd

`func (o *Systems) HasCloudBrokerProvisionalAuthorizationAtd() bool`

HasCloudBrokerProvisionalAuthorizationAtd returns a boolean if a field has been set.

### SetCloudBrokerProvisionalAuthorizationAtdNil

`func (o *Systems) SetCloudBrokerProvisionalAuthorizationAtdNil(b bool)`

 SetCloudBrokerProvisionalAuthorizationAtdNil sets the value for CloudBrokerProvisionalAuthorizationAtd to be an explicit nil

### UnsetCloudBrokerProvisionalAuthorizationAtd
`func (o *Systems) UnsetCloudBrokerProvisionalAuthorizationAtd()`

UnsetCloudBrokerProvisionalAuthorizationAtd ensures that no value is present for CloudBrokerProvisionalAuthorizationAtd, not even an explicit nil
### GetNavyJointAuthorization

`func (o *Systems) GetNavyJointAuthorization() bool`

GetNavyJointAuthorization returns the NavyJointAuthorization field if non-nil, zero value otherwise.

### GetNavyJointAuthorizationOk

`func (o *Systems) GetNavyJointAuthorizationOk() (*bool, bool)`

GetNavyJointAuthorizationOk returns a tuple with the NavyJointAuthorization field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNavyJointAuthorization

`func (o *Systems) SetNavyJointAuthorization(v bool)`

SetNavyJointAuthorization sets NavyJointAuthorization field to given value.

### HasNavyJointAuthorization

`func (o *Systems) HasNavyJointAuthorization() bool`

HasNavyJointAuthorization returns a boolean if a field has been set.

### SetNavyJointAuthorizationNil

`func (o *Systems) SetNavyJointAuthorizationNil(b bool)`

 SetNavyJointAuthorizationNil sets the value for NavyJointAuthorization to be an explicit nil

### UnsetNavyJointAuthorization
`func (o *Systems) UnsetNavyJointAuthorization()`

UnsetNavyJointAuthorization ensures that no value is present for NavyJointAuthorization, not even an explicit nil
### GetNmciNgenClins

`func (o *Systems) GetNmciNgenClins() string`

GetNmciNgenClins returns the NmciNgenClins field if non-nil, zero value otherwise.

### GetNmciNgenClinsOk

`func (o *Systems) GetNmciNgenClinsOk() (*string, bool)`

GetNmciNgenClinsOk returns a tuple with the NmciNgenClins field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNmciNgenClins

`func (o *Systems) SetNmciNgenClins(v string)`

SetNmciNgenClins sets NmciNgenClins field to given value.

### HasNmciNgenClins

`func (o *Systems) HasNmciNgenClins() bool`

HasNmciNgenClins returns a boolean if a field has been set.

### SetNmciNgenClinsNil

`func (o *Systems) SetNmciNgenClinsNil(b bool)`

 SetNmciNgenClinsNil sets the value for NmciNgenClins to be an explicit nil

### UnsetNmciNgenClins
`func (o *Systems) UnsetNmciNgenClins()`

UnsetNmciNgenClins ensures that no value is present for NmciNgenClins, not even an explicit nil
### GetEnterpriseLocations

`func (o *Systems) GetEnterpriseLocations() string`

GetEnterpriseLocations returns the EnterpriseLocations field if non-nil, zero value otherwise.

### GetEnterpriseLocationsOk

`func (o *Systems) GetEnterpriseLocationsOk() (*string, bool)`

GetEnterpriseLocationsOk returns a tuple with the EnterpriseLocations field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnterpriseLocations

`func (o *Systems) SetEnterpriseLocations(v string)`

SetEnterpriseLocations sets EnterpriseLocations field to given value.

### HasEnterpriseLocations

`func (o *Systems) HasEnterpriseLocations() bool`

HasEnterpriseLocations returns a boolean if a field has been set.

### SetEnterpriseLocationsNil

`func (o *Systems) SetEnterpriseLocationsNil(b bool)`

 SetEnterpriseLocationsNil sets the value for EnterpriseLocations to be an explicit nil

### UnsetEnterpriseLocations
`func (o *Systems) UnsetEnterpriseLocations()`

UnsetEnterpriseLocations ensures that no value is present for EnterpriseLocations, not even an explicit nil
### GetWhitelistId

`func (o *Systems) GetWhitelistId() string`

GetWhitelistId returns the WhitelistId field if non-nil, zero value otherwise.

### GetWhitelistIdOk

`func (o *Systems) GetWhitelistIdOk() (*string, bool)`

GetWhitelistIdOk returns a tuple with the WhitelistId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWhitelistId

`func (o *Systems) SetWhitelistId(v string)`

SetWhitelistId sets WhitelistId field to given value.

### HasWhitelistId

`func (o *Systems) HasWhitelistId() bool`

HasWhitelistId returns a boolean if a field has been set.

### SetWhitelistIdNil

`func (o *Systems) SetWhitelistIdNil(b bool)`

 SetWhitelistIdNil sets the value for WhitelistId to be an explicit nil

### UnsetWhitelistId
`func (o *Systems) UnsetWhitelistId()`

UnsetWhitelistId ensures that no value is present for WhitelistId, not even an explicit nil
### GetWhitelistInventory

`func (o *Systems) GetWhitelistInventory() string`

GetWhitelistInventory returns the WhitelistInventory field if non-nil, zero value otherwise.

### GetWhitelistInventoryOk

`func (o *Systems) GetWhitelistInventoryOk() (*string, bool)`

GetWhitelistInventoryOk returns a tuple with the WhitelistInventory field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWhitelistInventory

`func (o *Systems) SetWhitelistInventory(v string)`

SetWhitelistInventory sets WhitelistInventory field to given value.

### HasWhitelistInventory

`func (o *Systems) HasWhitelistInventory() bool`

HasWhitelistInventory returns a boolean if a field has been set.

### SetWhitelistInventoryNil

`func (o *Systems) SetWhitelistInventoryNil(b bool)`

 SetWhitelistInventoryNil sets the value for WhitelistInventory to be an explicit nil

### UnsetWhitelistInventory
`func (o *Systems) UnsetWhitelistInventory()`

UnsetWhitelistInventory ensures that no value is present for WhitelistInventory, not even an explicit nil
### GetAcquisitionCategory

`func (o *Systems) GetAcquisitionCategory() string`

GetAcquisitionCategory returns the AcquisitionCategory field if non-nil, zero value otherwise.

### GetAcquisitionCategoryOk

`func (o *Systems) GetAcquisitionCategoryOk() (*string, bool)`

GetAcquisitionCategoryOk returns a tuple with the AcquisitionCategory field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAcquisitionCategory

`func (o *Systems) SetAcquisitionCategory(v string)`

SetAcquisitionCategory sets AcquisitionCategory field to given value.

### HasAcquisitionCategory

`func (o *Systems) HasAcquisitionCategory() bool`

HasAcquisitionCategory returns a boolean if a field has been set.

### SetAcquisitionCategoryNil

`func (o *Systems) SetAcquisitionCategoryNil(b bool)`

 SetAcquisitionCategoryNil sets the value for AcquisitionCategory to be an explicit nil

### UnsetAcquisitionCategory
`func (o *Systems) UnsetAcquisitionCategory()`

UnsetAcquisitionCategory ensures that no value is present for AcquisitionCategory, not even an explicit nil
### GetSoftwareCategory

`func (o *Systems) GetSoftwareCategory() string`

GetSoftwareCategory returns the SoftwareCategory field if non-nil, zero value otherwise.

### GetSoftwareCategoryOk

`func (o *Systems) GetSoftwareCategoryOk() (*string, bool)`

GetSoftwareCategoryOk returns a tuple with the SoftwareCategory field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSoftwareCategory

`func (o *Systems) SetSoftwareCategory(v string)`

SetSoftwareCategory sets SoftwareCategory field to given value.

### HasSoftwareCategory

`func (o *Systems) HasSoftwareCategory() bool`

HasSoftwareCategory returns a boolean if a field has been set.

### SetSoftwareCategoryNil

`func (o *Systems) SetSoftwareCategoryNil(b bool)`

 SetSoftwareCategoryNil sets the value for SoftwareCategory to be an explicit nil

### UnsetSoftwareCategory
`func (o *Systems) UnsetSoftwareCategory()`

UnsetSoftwareCategory ensures that no value is present for SoftwareCategory, not even an explicit nil
### GetCybersecurityServiceProvider

`func (o *Systems) GetCybersecurityServiceProvider() string`

GetCybersecurityServiceProvider returns the CybersecurityServiceProvider field if non-nil, zero value otherwise.

### GetCybersecurityServiceProviderOk

`func (o *Systems) GetCybersecurityServiceProviderOk() (*string, bool)`

GetCybersecurityServiceProviderOk returns a tuple with the CybersecurityServiceProvider field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCybersecurityServiceProvider

`func (o *Systems) SetCybersecurityServiceProvider(v string)`

SetCybersecurityServiceProvider sets CybersecurityServiceProvider field to given value.

### HasCybersecurityServiceProvider

`func (o *Systems) HasCybersecurityServiceProvider() bool`

HasCybersecurityServiceProvider returns a boolean if a field has been set.

### SetCybersecurityServiceProviderNil

`func (o *Systems) SetCybersecurityServiceProviderNil(b bool)`

 SetCybersecurityServiceProviderNil sets the value for CybersecurityServiceProvider to be an explicit nil

### UnsetCybersecurityServiceProvider
`func (o *Systems) UnsetCybersecurityServiceProvider()`

UnsetCybersecurityServiceProvider ensures that no value is present for CybersecurityServiceProvider, not even an explicit nil
### GetCybersecurityServiceProviderExceptionJustification

`func (o *Systems) GetCybersecurityServiceProviderExceptionJustification() string`

GetCybersecurityServiceProviderExceptionJustification returns the CybersecurityServiceProviderExceptionJustification field if non-nil, zero value otherwise.

### GetCybersecurityServiceProviderExceptionJustificationOk

`func (o *Systems) GetCybersecurityServiceProviderExceptionJustificationOk() (*string, bool)`

GetCybersecurityServiceProviderExceptionJustificationOk returns a tuple with the CybersecurityServiceProviderExceptionJustification field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCybersecurityServiceProviderExceptionJustification

`func (o *Systems) SetCybersecurityServiceProviderExceptionJustification(v string)`

SetCybersecurityServiceProviderExceptionJustification sets CybersecurityServiceProviderExceptionJustification field to given value.

### HasCybersecurityServiceProviderExceptionJustification

`func (o *Systems) HasCybersecurityServiceProviderExceptionJustification() bool`

HasCybersecurityServiceProviderExceptionJustification returns a boolean if a field has been set.

### SetCybersecurityServiceProviderExceptionJustificationNil

`func (o *Systems) SetCybersecurityServiceProviderExceptionJustificationNil(b bool)`

 SetCybersecurityServiceProviderExceptionJustificationNil sets the value for CybersecurityServiceProviderExceptionJustification to be an explicit nil

### UnsetCybersecurityServiceProviderExceptionJustification
`func (o *Systems) UnsetCybersecurityServiceProviderExceptionJustification()`

UnsetCybersecurityServiceProviderExceptionJustification ensures that no value is present for CybersecurityServiceProviderExceptionJustification, not even an explicit nil
### GetMaximumTolerableDowntime

`func (o *Systems) GetMaximumTolerableDowntime() string`

GetMaximumTolerableDowntime returns the MaximumTolerableDowntime field if non-nil, zero value otherwise.

### GetMaximumTolerableDowntimeOk

`func (o *Systems) GetMaximumTolerableDowntimeOk() (*string, bool)`

GetMaximumTolerableDowntimeOk returns a tuple with the MaximumTolerableDowntime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMaximumTolerableDowntime

`func (o *Systems) SetMaximumTolerableDowntime(v string)`

SetMaximumTolerableDowntime sets MaximumTolerableDowntime field to given value.

### HasMaximumTolerableDowntime

`func (o *Systems) HasMaximumTolerableDowntime() bool`

HasMaximumTolerableDowntime returns a boolean if a field has been set.

### SetMaximumTolerableDowntimeNil

`func (o *Systems) SetMaximumTolerableDowntimeNil(b bool)`

 SetMaximumTolerableDowntimeNil sets the value for MaximumTolerableDowntime to be an explicit nil

### UnsetMaximumTolerableDowntime
`func (o *Systems) UnsetMaximumTolerableDowntime()`

UnsetMaximumTolerableDowntime ensures that no value is present for MaximumTolerableDowntime, not even an explicit nil
### GetRecoveryTimeObjective

`func (o *Systems) GetRecoveryTimeObjective() string`

GetRecoveryTimeObjective returns the RecoveryTimeObjective field if non-nil, zero value otherwise.

### GetRecoveryTimeObjectiveOk

`func (o *Systems) GetRecoveryTimeObjectiveOk() (*string, bool)`

GetRecoveryTimeObjectiveOk returns a tuple with the RecoveryTimeObjective field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRecoveryTimeObjective

`func (o *Systems) SetRecoveryTimeObjective(v string)`

SetRecoveryTimeObjective sets RecoveryTimeObjective field to given value.

### HasRecoveryTimeObjective

`func (o *Systems) HasRecoveryTimeObjective() bool`

HasRecoveryTimeObjective returns a boolean if a field has been set.

### SetRecoveryTimeObjectiveNil

`func (o *Systems) SetRecoveryTimeObjectiveNil(b bool)`

 SetRecoveryTimeObjectiveNil sets the value for RecoveryTimeObjective to be an explicit nil

### UnsetRecoveryTimeObjective
`func (o *Systems) UnsetRecoveryTimeObjective()`

UnsetRecoveryTimeObjective ensures that no value is present for RecoveryTimeObjective, not even an explicit nil
### GetRecoveryPointObjective

`func (o *Systems) GetRecoveryPointObjective() string`

GetRecoveryPointObjective returns the RecoveryPointObjective field if non-nil, zero value otherwise.

### GetRecoveryPointObjectiveOk

`func (o *Systems) GetRecoveryPointObjectiveOk() (*string, bool)`

GetRecoveryPointObjectiveOk returns a tuple with the RecoveryPointObjective field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRecoveryPointObjective

`func (o *Systems) SetRecoveryPointObjective(v string)`

SetRecoveryPointObjective sets RecoveryPointObjective field to given value.

### HasRecoveryPointObjective

`func (o *Systems) HasRecoveryPointObjective() bool`

HasRecoveryPointObjective returns a boolean if a field has been set.

### SetRecoveryPointObjectiveNil

`func (o *Systems) SetRecoveryPointObjectiveNil(b bool)`

 SetRecoveryPointObjectiveNil sets the value for RecoveryPointObjective to be an explicit nil

### UnsetRecoveryPointObjective
`func (o *Systems) UnsetRecoveryPointObjective()`

UnsetRecoveryPointObjective ensures that no value is present for RecoveryPointObjective, not even an explicit nil
### GetBusinessImpactAnalysisRequired

`func (o *Systems) GetBusinessImpactAnalysisRequired() bool`

GetBusinessImpactAnalysisRequired returns the BusinessImpactAnalysisRequired field if non-nil, zero value otherwise.

### GetBusinessImpactAnalysisRequiredOk

`func (o *Systems) GetBusinessImpactAnalysisRequiredOk() (*bool, bool)`

GetBusinessImpactAnalysisRequiredOk returns a tuple with the BusinessImpactAnalysisRequired field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBusinessImpactAnalysisRequired

`func (o *Systems) SetBusinessImpactAnalysisRequired(v bool)`

SetBusinessImpactAnalysisRequired sets BusinessImpactAnalysisRequired field to given value.

### HasBusinessImpactAnalysisRequired

`func (o *Systems) HasBusinessImpactAnalysisRequired() bool`

HasBusinessImpactAnalysisRequired returns a boolean if a field has been set.

### SetBusinessImpactAnalysisRequiredNil

`func (o *Systems) SetBusinessImpactAnalysisRequiredNil(b bool)`

 SetBusinessImpactAnalysisRequiredNil sets the value for BusinessImpactAnalysisRequired to be an explicit nil

### UnsetBusinessImpactAnalysisRequired
`func (o *Systems) UnsetBusinessImpactAnalysisRequired()`

UnsetBusinessImpactAnalysisRequired ensures that no value is present for BusinessImpactAnalysisRequired, not even an explicit nil
### GetBusinessImpactAnalysisArtifact

`func (o *Systems) GetBusinessImpactAnalysisArtifact() string`

GetBusinessImpactAnalysisArtifact returns the BusinessImpactAnalysisArtifact field if non-nil, zero value otherwise.

### GetBusinessImpactAnalysisArtifactOk

`func (o *Systems) GetBusinessImpactAnalysisArtifactOk() (*string, bool)`

GetBusinessImpactAnalysisArtifactOk returns a tuple with the BusinessImpactAnalysisArtifact field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBusinessImpactAnalysisArtifact

`func (o *Systems) SetBusinessImpactAnalysisArtifact(v string)`

SetBusinessImpactAnalysisArtifact sets BusinessImpactAnalysisArtifact field to given value.

### HasBusinessImpactAnalysisArtifact

`func (o *Systems) HasBusinessImpactAnalysisArtifact() bool`

HasBusinessImpactAnalysisArtifact returns a boolean if a field has been set.

### SetBusinessImpactAnalysisArtifactNil

`func (o *Systems) SetBusinessImpactAnalysisArtifactNil(b bool)`

 SetBusinessImpactAnalysisArtifactNil sets the value for BusinessImpactAnalysisArtifact to be an explicit nil

### UnsetBusinessImpactAnalysisArtifact
`func (o *Systems) UnsetBusinessImpactAnalysisArtifact()`

UnsetBusinessImpactAnalysisArtifact ensures that no value is present for BusinessImpactAnalysisArtifact, not even an explicit nil
### GetIncidentResponsePlanRequired

`func (o *Systems) GetIncidentResponsePlanRequired() bool`

GetIncidentResponsePlanRequired returns the IncidentResponsePlanRequired field if non-nil, zero value otherwise.

### GetIncidentResponsePlanRequiredOk

`func (o *Systems) GetIncidentResponsePlanRequiredOk() (*bool, bool)`

GetIncidentResponsePlanRequiredOk returns a tuple with the IncidentResponsePlanRequired field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIncidentResponsePlanRequired

`func (o *Systems) SetIncidentResponsePlanRequired(v bool)`

SetIncidentResponsePlanRequired sets IncidentResponsePlanRequired field to given value.

### HasIncidentResponsePlanRequired

`func (o *Systems) HasIncidentResponsePlanRequired() bool`

HasIncidentResponsePlanRequired returns a boolean if a field has been set.

### SetIncidentResponsePlanRequiredNil

`func (o *Systems) SetIncidentResponsePlanRequiredNil(b bool)`

 SetIncidentResponsePlanRequiredNil sets the value for IncidentResponsePlanRequired to be an explicit nil

### UnsetIncidentResponsePlanRequired
`func (o *Systems) UnsetIncidentResponsePlanRequired()`

UnsetIncidentResponsePlanRequired ensures that no value is present for IncidentResponsePlanRequired, not even an explicit nil
### GetIncidentResponsePlanArtifact

`func (o *Systems) GetIncidentResponsePlanArtifact() string`

GetIncidentResponsePlanArtifact returns the IncidentResponsePlanArtifact field if non-nil, zero value otherwise.

### GetIncidentResponsePlanArtifactOk

`func (o *Systems) GetIncidentResponsePlanArtifactOk() (*string, bool)`

GetIncidentResponsePlanArtifactOk returns a tuple with the IncidentResponsePlanArtifact field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIncidentResponsePlanArtifact

`func (o *Systems) SetIncidentResponsePlanArtifact(v string)`

SetIncidentResponsePlanArtifact sets IncidentResponsePlanArtifact field to given value.

### HasIncidentResponsePlanArtifact

`func (o *Systems) HasIncidentResponsePlanArtifact() bool`

HasIncidentResponsePlanArtifact returns a boolean if a field has been set.

### SetIncidentResponsePlanArtifactNil

`func (o *Systems) SetIncidentResponsePlanArtifactNil(b bool)`

 SetIncidentResponsePlanArtifactNil sets the value for IncidentResponsePlanArtifact to be an explicit nil

### UnsetIncidentResponsePlanArtifact
`func (o *Systems) UnsetIncidentResponsePlanArtifact()`

UnsetIncidentResponsePlanArtifact ensures that no value is present for IncidentResponsePlanArtifact, not even an explicit nil
### GetDisasterRecoveryPlanRequired

`func (o *Systems) GetDisasterRecoveryPlanRequired() bool`

GetDisasterRecoveryPlanRequired returns the DisasterRecoveryPlanRequired field if non-nil, zero value otherwise.

### GetDisasterRecoveryPlanRequiredOk

`func (o *Systems) GetDisasterRecoveryPlanRequiredOk() (*bool, bool)`

GetDisasterRecoveryPlanRequiredOk returns a tuple with the DisasterRecoveryPlanRequired field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDisasterRecoveryPlanRequired

`func (o *Systems) SetDisasterRecoveryPlanRequired(v bool)`

SetDisasterRecoveryPlanRequired sets DisasterRecoveryPlanRequired field to given value.

### HasDisasterRecoveryPlanRequired

`func (o *Systems) HasDisasterRecoveryPlanRequired() bool`

HasDisasterRecoveryPlanRequired returns a boolean if a field has been set.

### SetDisasterRecoveryPlanRequiredNil

`func (o *Systems) SetDisasterRecoveryPlanRequiredNil(b bool)`

 SetDisasterRecoveryPlanRequiredNil sets the value for DisasterRecoveryPlanRequired to be an explicit nil

### UnsetDisasterRecoveryPlanRequired
`func (o *Systems) UnsetDisasterRecoveryPlanRequired()`

UnsetDisasterRecoveryPlanRequired ensures that no value is present for DisasterRecoveryPlanRequired, not even an explicit nil
### GetDisasterRecoveryPlanArtifact

`func (o *Systems) GetDisasterRecoveryPlanArtifact() string`

GetDisasterRecoveryPlanArtifact returns the DisasterRecoveryPlanArtifact field if non-nil, zero value otherwise.

### GetDisasterRecoveryPlanArtifactOk

`func (o *Systems) GetDisasterRecoveryPlanArtifactOk() (*string, bool)`

GetDisasterRecoveryPlanArtifactOk returns a tuple with the DisasterRecoveryPlanArtifact field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDisasterRecoveryPlanArtifact

`func (o *Systems) SetDisasterRecoveryPlanArtifact(v string)`

SetDisasterRecoveryPlanArtifact sets DisasterRecoveryPlanArtifact field to given value.

### HasDisasterRecoveryPlanArtifact

`func (o *Systems) HasDisasterRecoveryPlanArtifact() bool`

HasDisasterRecoveryPlanArtifact returns a boolean if a field has been set.

### SetDisasterRecoveryPlanArtifactNil

`func (o *Systems) SetDisasterRecoveryPlanArtifactNil(b bool)`

 SetDisasterRecoveryPlanArtifactNil sets the value for DisasterRecoveryPlanArtifact to be an explicit nil

### UnsetDisasterRecoveryPlanArtifact
`func (o *Systems) UnsetDisasterRecoveryPlanArtifact()`

UnsetDisasterRecoveryPlanArtifact ensures that no value is present for DisasterRecoveryPlanArtifact, not even an explicit nil
### GetPrivacyThresholdAnalysisCompleted

`func (o *Systems) GetPrivacyThresholdAnalysisCompleted() bool`

GetPrivacyThresholdAnalysisCompleted returns the PrivacyThresholdAnalysisCompleted field if non-nil, zero value otherwise.

### GetPrivacyThresholdAnalysisCompletedOk

`func (o *Systems) GetPrivacyThresholdAnalysisCompletedOk() (*bool, bool)`

GetPrivacyThresholdAnalysisCompletedOk returns a tuple with the PrivacyThresholdAnalysisCompleted field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPrivacyThresholdAnalysisCompleted

`func (o *Systems) SetPrivacyThresholdAnalysisCompleted(v bool)`

SetPrivacyThresholdAnalysisCompleted sets PrivacyThresholdAnalysisCompleted field to given value.

### HasPrivacyThresholdAnalysisCompleted

`func (o *Systems) HasPrivacyThresholdAnalysisCompleted() bool`

HasPrivacyThresholdAnalysisCompleted returns a boolean if a field has been set.

### SetPrivacyThresholdAnalysisCompletedNil

`func (o *Systems) SetPrivacyThresholdAnalysisCompletedNil(b bool)`

 SetPrivacyThresholdAnalysisCompletedNil sets the value for PrivacyThresholdAnalysisCompleted to be an explicit nil

### UnsetPrivacyThresholdAnalysisCompleted
`func (o *Systems) UnsetPrivacyThresholdAnalysisCompleted()`

UnsetPrivacyThresholdAnalysisCompleted ensures that no value is present for PrivacyThresholdAnalysisCompleted, not even an explicit nil
### GetPrivacyThresholdAnalysisDate

`func (o *Systems) GetPrivacyThresholdAnalysisDate() int32`

GetPrivacyThresholdAnalysisDate returns the PrivacyThresholdAnalysisDate field if non-nil, zero value otherwise.

### GetPrivacyThresholdAnalysisDateOk

`func (o *Systems) GetPrivacyThresholdAnalysisDateOk() (*int32, bool)`

GetPrivacyThresholdAnalysisDateOk returns a tuple with the PrivacyThresholdAnalysisDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPrivacyThresholdAnalysisDate

`func (o *Systems) SetPrivacyThresholdAnalysisDate(v int32)`

SetPrivacyThresholdAnalysisDate sets PrivacyThresholdAnalysisDate field to given value.

### HasPrivacyThresholdAnalysisDate

`func (o *Systems) HasPrivacyThresholdAnalysisDate() bool`

HasPrivacyThresholdAnalysisDate returns a boolean if a field has been set.

### SetPrivacyThresholdAnalysisDateNil

`func (o *Systems) SetPrivacyThresholdAnalysisDateNil(b bool)`

 SetPrivacyThresholdAnalysisDateNil sets the value for PrivacyThresholdAnalysisDate to be an explicit nil

### UnsetPrivacyThresholdAnalysisDate
`func (o *Systems) UnsetPrivacyThresholdAnalysisDate()`

UnsetPrivacyThresholdAnalysisDate ensures that no value is present for PrivacyThresholdAnalysisDate, not even an explicit nil
### GetPrivacyThresholdAnalysisArtifact

`func (o *Systems) GetPrivacyThresholdAnalysisArtifact() string`

GetPrivacyThresholdAnalysisArtifact returns the PrivacyThresholdAnalysisArtifact field if non-nil, zero value otherwise.

### GetPrivacyThresholdAnalysisArtifactOk

`func (o *Systems) GetPrivacyThresholdAnalysisArtifactOk() (*string, bool)`

GetPrivacyThresholdAnalysisArtifactOk returns a tuple with the PrivacyThresholdAnalysisArtifact field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPrivacyThresholdAnalysisArtifact

`func (o *Systems) SetPrivacyThresholdAnalysisArtifact(v string)`

SetPrivacyThresholdAnalysisArtifact sets PrivacyThresholdAnalysisArtifact field to given value.

### HasPrivacyThresholdAnalysisArtifact

`func (o *Systems) HasPrivacyThresholdAnalysisArtifact() bool`

HasPrivacyThresholdAnalysisArtifact returns a boolean if a field has been set.

### SetPrivacyThresholdAnalysisArtifactNil

`func (o *Systems) SetPrivacyThresholdAnalysisArtifactNil(b bool)`

 SetPrivacyThresholdAnalysisArtifactNil sets the value for PrivacyThresholdAnalysisArtifact to be an explicit nil

### UnsetPrivacyThresholdAnalysisArtifact
`func (o *Systems) UnsetPrivacyThresholdAnalysisArtifact()`

UnsetPrivacyThresholdAnalysisArtifact ensures that no value is present for PrivacyThresholdAnalysisArtifact, not even an explicit nil
### GetPrivacyActSystemOfRecordsNoticeRequired

`func (o *Systems) GetPrivacyActSystemOfRecordsNoticeRequired() bool`

GetPrivacyActSystemOfRecordsNoticeRequired returns the PrivacyActSystemOfRecordsNoticeRequired field if non-nil, zero value otherwise.

### GetPrivacyActSystemOfRecordsNoticeRequiredOk

`func (o *Systems) GetPrivacyActSystemOfRecordsNoticeRequiredOk() (*bool, bool)`

GetPrivacyActSystemOfRecordsNoticeRequiredOk returns a tuple with the PrivacyActSystemOfRecordsNoticeRequired field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPrivacyActSystemOfRecordsNoticeRequired

`func (o *Systems) SetPrivacyActSystemOfRecordsNoticeRequired(v bool)`

SetPrivacyActSystemOfRecordsNoticeRequired sets PrivacyActSystemOfRecordsNoticeRequired field to given value.

### HasPrivacyActSystemOfRecordsNoticeRequired

`func (o *Systems) HasPrivacyActSystemOfRecordsNoticeRequired() bool`

HasPrivacyActSystemOfRecordsNoticeRequired returns a boolean if a field has been set.

### SetPrivacyActSystemOfRecordsNoticeRequiredNil

`func (o *Systems) SetPrivacyActSystemOfRecordsNoticeRequiredNil(b bool)`

 SetPrivacyActSystemOfRecordsNoticeRequiredNil sets the value for PrivacyActSystemOfRecordsNoticeRequired to be an explicit nil

### UnsetPrivacyActSystemOfRecordsNoticeRequired
`func (o *Systems) UnsetPrivacyActSystemOfRecordsNoticeRequired()`

UnsetPrivacyActSystemOfRecordsNoticeRequired ensures that no value is present for PrivacyActSystemOfRecordsNoticeRequired, not even an explicit nil
### GetEAuthenticationRiskAssessmentRequired

`func (o *Systems) GetEAuthenticationRiskAssessmentRequired() bool`

GetEAuthenticationRiskAssessmentRequired returns the EAuthenticationRiskAssessmentRequired field if non-nil, zero value otherwise.

### GetEAuthenticationRiskAssessmentRequiredOk

`func (o *Systems) GetEAuthenticationRiskAssessmentRequiredOk() (*bool, bool)`

GetEAuthenticationRiskAssessmentRequiredOk returns a tuple with the EAuthenticationRiskAssessmentRequired field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEAuthenticationRiskAssessmentRequired

`func (o *Systems) SetEAuthenticationRiskAssessmentRequired(v bool)`

SetEAuthenticationRiskAssessmentRequired sets EAuthenticationRiskAssessmentRequired field to given value.

### HasEAuthenticationRiskAssessmentRequired

`func (o *Systems) HasEAuthenticationRiskAssessmentRequired() bool`

HasEAuthenticationRiskAssessmentRequired returns a boolean if a field has been set.

### SetEAuthenticationRiskAssessmentRequiredNil

`func (o *Systems) SetEAuthenticationRiskAssessmentRequiredNil(b bool)`

 SetEAuthenticationRiskAssessmentRequiredNil sets the value for EAuthenticationRiskAssessmentRequired to be an explicit nil

### UnsetEAuthenticationRiskAssessmentRequired
`func (o *Systems) UnsetEAuthenticationRiskAssessmentRequired()`

UnsetEAuthenticationRiskAssessmentRequired ensures that no value is present for EAuthenticationRiskAssessmentRequired, not even an explicit nil
### GetEAuthenticationRiskAssessmentDate

`func (o *Systems) GetEAuthenticationRiskAssessmentDate() int32`

GetEAuthenticationRiskAssessmentDate returns the EAuthenticationRiskAssessmentDate field if non-nil, zero value otherwise.

### GetEAuthenticationRiskAssessmentDateOk

`func (o *Systems) GetEAuthenticationRiskAssessmentDateOk() (*int32, bool)`

GetEAuthenticationRiskAssessmentDateOk returns a tuple with the EAuthenticationRiskAssessmentDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEAuthenticationRiskAssessmentDate

`func (o *Systems) SetEAuthenticationRiskAssessmentDate(v int32)`

SetEAuthenticationRiskAssessmentDate sets EAuthenticationRiskAssessmentDate field to given value.

### HasEAuthenticationRiskAssessmentDate

`func (o *Systems) HasEAuthenticationRiskAssessmentDate() bool`

HasEAuthenticationRiskAssessmentDate returns a boolean if a field has been set.

### SetEAuthenticationRiskAssessmentDateNil

`func (o *Systems) SetEAuthenticationRiskAssessmentDateNil(b bool)`

 SetEAuthenticationRiskAssessmentDateNil sets the value for EAuthenticationRiskAssessmentDate to be an explicit nil

### UnsetEAuthenticationRiskAssessmentDate
`func (o *Systems) UnsetEAuthenticationRiskAssessmentDate()`

UnsetEAuthenticationRiskAssessmentDate ensures that no value is present for EAuthenticationRiskAssessmentDate, not even an explicit nil
### GetEAuthenticationRiskAssessmentArtifact

`func (o *Systems) GetEAuthenticationRiskAssessmentArtifact() string`

GetEAuthenticationRiskAssessmentArtifact returns the EAuthenticationRiskAssessmentArtifact field if non-nil, zero value otherwise.

### GetEAuthenticationRiskAssessmentArtifactOk

`func (o *Systems) GetEAuthenticationRiskAssessmentArtifactOk() (*string, bool)`

GetEAuthenticationRiskAssessmentArtifactOk returns a tuple with the EAuthenticationRiskAssessmentArtifact field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEAuthenticationRiskAssessmentArtifact

`func (o *Systems) SetEAuthenticationRiskAssessmentArtifact(v string)`

SetEAuthenticationRiskAssessmentArtifact sets EAuthenticationRiskAssessmentArtifact field to given value.

### HasEAuthenticationRiskAssessmentArtifact

`func (o *Systems) HasEAuthenticationRiskAssessmentArtifact() bool`

HasEAuthenticationRiskAssessmentArtifact returns a boolean if a field has been set.

### SetEAuthenticationRiskAssessmentArtifactNil

`func (o *Systems) SetEAuthenticationRiskAssessmentArtifactNil(b bool)`

 SetEAuthenticationRiskAssessmentArtifactNil sets the value for EAuthenticationRiskAssessmentArtifact to be an explicit nil

### UnsetEAuthenticationRiskAssessmentArtifact
`func (o *Systems) UnsetEAuthenticationRiskAssessmentArtifact()`

UnsetEAuthenticationRiskAssessmentArtifact ensures that no value is present for EAuthenticationRiskAssessmentArtifact, not even an explicit nil
### GetIpv4OnlyAssets

`func (o *Systems) GetIpv4OnlyAssets() int32`

GetIpv4OnlyAssets returns the Ipv4OnlyAssets field if non-nil, zero value otherwise.

### GetIpv4OnlyAssetsOk

`func (o *Systems) GetIpv4OnlyAssetsOk() (*int32, bool)`

GetIpv4OnlyAssetsOk returns a tuple with the Ipv4OnlyAssets field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIpv4OnlyAssets

`func (o *Systems) SetIpv4OnlyAssets(v int32)`

SetIpv4OnlyAssets sets Ipv4OnlyAssets field to given value.

### HasIpv4OnlyAssets

`func (o *Systems) HasIpv4OnlyAssets() bool`

HasIpv4OnlyAssets returns a boolean if a field has been set.

### SetIpv4OnlyAssetsNil

`func (o *Systems) SetIpv4OnlyAssetsNil(b bool)`

 SetIpv4OnlyAssetsNil sets the value for Ipv4OnlyAssets to be an explicit nil

### UnsetIpv4OnlyAssets
`func (o *Systems) UnsetIpv4OnlyAssets()`

UnsetIpv4OnlyAssets ensures that no value is present for Ipv4OnlyAssets, not even an explicit nil
### GetIpv6OnlyAssets

`func (o *Systems) GetIpv6OnlyAssets() int32`

GetIpv6OnlyAssets returns the Ipv6OnlyAssets field if non-nil, zero value otherwise.

### GetIpv6OnlyAssetsOk

`func (o *Systems) GetIpv6OnlyAssetsOk() (*int32, bool)`

GetIpv6OnlyAssetsOk returns a tuple with the Ipv6OnlyAssets field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIpv6OnlyAssets

`func (o *Systems) SetIpv6OnlyAssets(v int32)`

SetIpv6OnlyAssets sets Ipv6OnlyAssets field to given value.

### HasIpv6OnlyAssets

`func (o *Systems) HasIpv6OnlyAssets() bool`

HasIpv6OnlyAssets returns a boolean if a field has been set.

### SetIpv6OnlyAssetsNil

`func (o *Systems) SetIpv6OnlyAssetsNil(b bool)`

 SetIpv6OnlyAssetsNil sets the value for Ipv6OnlyAssets to be an explicit nil

### UnsetIpv6OnlyAssets
`func (o *Systems) UnsetIpv6OnlyAssets()`

UnsetIpv6OnlyAssets ensures that no value is present for Ipv6OnlyAssets, not even an explicit nil
### GetIpv4Ipv6DualStackAssets

`func (o *Systems) GetIpv4Ipv6DualStackAssets() int32`

GetIpv4Ipv6DualStackAssets returns the Ipv4Ipv6DualStackAssets field if non-nil, zero value otherwise.

### GetIpv4Ipv6DualStackAssetsOk

`func (o *Systems) GetIpv4Ipv6DualStackAssetsOk() (*int32, bool)`

GetIpv4Ipv6DualStackAssetsOk returns a tuple with the Ipv4Ipv6DualStackAssets field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIpv4Ipv6DualStackAssets

`func (o *Systems) SetIpv4Ipv6DualStackAssets(v int32)`

SetIpv4Ipv6DualStackAssets sets Ipv4Ipv6DualStackAssets field to given value.

### HasIpv4Ipv6DualStackAssets

`func (o *Systems) HasIpv4Ipv6DualStackAssets() bool`

HasIpv4Ipv6DualStackAssets returns a boolean if a field has been set.

### SetIpv4Ipv6DualStackAssetsNil

`func (o *Systems) SetIpv4Ipv6DualStackAssetsNil(b bool)`

 SetIpv4Ipv6DualStackAssetsNil sets the value for Ipv4Ipv6DualStackAssets to be an explicit nil

### UnsetIpv4Ipv6DualStackAssets
`func (o *Systems) UnsetIpv4Ipv6DualStackAssets()`

UnsetIpv4Ipv6DualStackAssets ensures that no value is present for Ipv4Ipv6DualStackAssets, not even an explicit nil
### GetTotalIpAssets

`func (o *Systems) GetTotalIpAssets() int32`

GetTotalIpAssets returns the TotalIpAssets field if non-nil, zero value otherwise.

### GetTotalIpAssetsOk

`func (o *Systems) GetTotalIpAssetsOk() (*int32, bool)`

GetTotalIpAssetsOk returns a tuple with the TotalIpAssets field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotalIpAssets

`func (o *Systems) SetTotalIpAssets(v int32)`

SetTotalIpAssets sets TotalIpAssets field to given value.

### HasTotalIpAssets

`func (o *Systems) HasTotalIpAssets() bool`

HasTotalIpAssets returns a boolean if a field has been set.

### SetTotalIpAssetsNil

`func (o *Systems) SetTotalIpAssetsNil(b bool)`

 SetTotalIpAssetsNil sets the value for TotalIpAssets to be an explicit nil

### UnsetTotalIpAssets
`func (o *Systems) UnsetTotalIpAssets()`

UnsetTotalIpAssets ensures that no value is present for TotalIpAssets, not even an explicit nil
### GetOriginatingOrganization

`func (o *Systems) GetOriginatingOrganization() string`

GetOriginatingOrganization returns the OriginatingOrganization field if non-nil, zero value otherwise.

### GetOriginatingOrganizationOk

`func (o *Systems) GetOriginatingOrganizationOk() (*string, bool)`

GetOriginatingOrganizationOk returns a tuple with the OriginatingOrganization field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOriginatingOrganization

`func (o *Systems) SetOriginatingOrganization(v string)`

SetOriginatingOrganization sets OriginatingOrganization field to given value.

### HasOriginatingOrganization

`func (o *Systems) HasOriginatingOrganization() bool`

HasOriginatingOrganization returns a boolean if a field has been set.

### SetOriginatingOrganizationNil

`func (o *Systems) SetOriginatingOrganizationNil(b bool)`

 SetOriginatingOrganizationNil sets the value for OriginatingOrganization to be an explicit nil

### UnsetOriginatingOrganization
`func (o *Systems) UnsetOriginatingOrganization()`

UnsetOriginatingOrganization ensures that no value is present for OriginatingOrganization, not even an explicit nil
### GetSystemUseJustification

`func (o *Systems) GetSystemUseJustification() string`

GetSystemUseJustification returns the SystemUseJustification field if non-nil, zero value otherwise.

### GetSystemUseJustificationOk

`func (o *Systems) GetSystemUseJustificationOk() (*string, bool)`

GetSystemUseJustificationOk returns a tuple with the SystemUseJustification field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSystemUseJustification

`func (o *Systems) SetSystemUseJustification(v string)`

SetSystemUseJustification sets SystemUseJustification field to given value.

### HasSystemUseJustification

`func (o *Systems) HasSystemUseJustification() bool`

HasSystemUseJustification returns a boolean if a field has been set.

### SetSystemUseJustificationNil

`func (o *Systems) SetSystemUseJustificationNil(b bool)`

 SetSystemUseJustificationNil sets the value for SystemUseJustification to be an explicit nil

### UnsetSystemUseJustification
`func (o *Systems) UnsetSystemUseJustification()`

UnsetSystemUseJustification ensures that no value is present for SystemUseJustification, not even an explicit nil
### GetSystemUseJustificationArtifact

`func (o *Systems) GetSystemUseJustificationArtifact() string`

GetSystemUseJustificationArtifact returns the SystemUseJustificationArtifact field if non-nil, zero value otherwise.

### GetSystemUseJustificationArtifactOk

`func (o *Systems) GetSystemUseJustificationArtifactOk() (*string, bool)`

GetSystemUseJustificationArtifactOk returns a tuple with the SystemUseJustificationArtifact field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSystemUseJustificationArtifact

`func (o *Systems) SetSystemUseJustificationArtifact(v string)`

SetSystemUseJustificationArtifact sets SystemUseJustificationArtifact field to given value.

### HasSystemUseJustificationArtifact

`func (o *Systems) HasSystemUseJustificationArtifact() bool`

HasSystemUseJustificationArtifact returns a boolean if a field has been set.

### SetSystemUseJustificationArtifactNil

`func (o *Systems) SetSystemUseJustificationArtifactNil(b bool)`

 SetSystemUseJustificationArtifactNil sets the value for SystemUseJustificationArtifact to be an explicit nil

### UnsetSystemUseJustificationArtifact
`func (o *Systems) UnsetSystemUseJustificationArtifact()`

UnsetSystemUseJustificationArtifact ensures that no value is present for SystemUseJustificationArtifact, not even an explicit nil
### GetAuthorizationToUseStatus

`func (o *Systems) GetAuthorizationToUseStatus() string`

GetAuthorizationToUseStatus returns the AuthorizationToUseStatus field if non-nil, zero value otherwise.

### GetAuthorizationToUseStatusOk

`func (o *Systems) GetAuthorizationToUseStatusOk() (*string, bool)`

GetAuthorizationToUseStatusOk returns a tuple with the AuthorizationToUseStatus field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAuthorizationToUseStatus

`func (o *Systems) SetAuthorizationToUseStatus(v string)`

SetAuthorizationToUseStatus sets AuthorizationToUseStatus field to given value.

### HasAuthorizationToUseStatus

`func (o *Systems) HasAuthorizationToUseStatus() bool`

HasAuthorizationToUseStatus returns a boolean if a field has been set.

### SetAuthorizationToUseStatusNil

`func (o *Systems) SetAuthorizationToUseStatusNil(b bool)`

 SetAuthorizationToUseStatusNil sets the value for AuthorizationToUseStatus to be an explicit nil

### UnsetAuthorizationToUseStatus
`func (o *Systems) UnsetAuthorizationToUseStatus()`

UnsetAuthorizationToUseStatus ensures that no value is present for AuthorizationToUseStatus, not even an explicit nil
### GetReciprocityAcceptanceStatus

`func (o *Systems) GetReciprocityAcceptanceStatus() string`

GetReciprocityAcceptanceStatus returns the ReciprocityAcceptanceStatus field if non-nil, zero value otherwise.

### GetReciprocityAcceptanceStatusOk

`func (o *Systems) GetReciprocityAcceptanceStatusOk() (*string, bool)`

GetReciprocityAcceptanceStatusOk returns a tuple with the ReciprocityAcceptanceStatus field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetReciprocityAcceptanceStatus

`func (o *Systems) SetReciprocityAcceptanceStatus(v string)`

SetReciprocityAcceptanceStatus sets ReciprocityAcceptanceStatus field to given value.

### HasReciprocityAcceptanceStatus

`func (o *Systems) HasReciprocityAcceptanceStatus() bool`

HasReciprocityAcceptanceStatus returns a boolean if a field has been set.

### SetReciprocityAcceptanceStatusNil

`func (o *Systems) SetReciprocityAcceptanceStatusNil(b bool)`

 SetReciprocityAcceptanceStatusNil sets the value for ReciprocityAcceptanceStatus to be an explicit nil

### UnsetReciprocityAcceptanceStatus
`func (o *Systems) UnsetReciprocityAcceptanceStatus()`

UnsetReciprocityAcceptanceStatus ensures that no value is present for ReciprocityAcceptanceStatus, not even an explicit nil
### GetUseAuthorizationDate

`func (o *Systems) GetUseAuthorizationDate() int32`

GetUseAuthorizationDate returns the UseAuthorizationDate field if non-nil, zero value otherwise.

### GetUseAuthorizationDateOk

`func (o *Systems) GetUseAuthorizationDateOk() (*int32, bool)`

GetUseAuthorizationDateOk returns a tuple with the UseAuthorizationDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUseAuthorizationDate

`func (o *Systems) SetUseAuthorizationDate(v int32)`

SetUseAuthorizationDate sets UseAuthorizationDate field to given value.

### HasUseAuthorizationDate

`func (o *Systems) HasUseAuthorizationDate() bool`

HasUseAuthorizationDate returns a boolean if a field has been set.

### SetUseAuthorizationDateNil

`func (o *Systems) SetUseAuthorizationDateNil(b bool)`

 SetUseAuthorizationDateNil sets the value for UseAuthorizationDate to be an explicit nil

### UnsetUseAuthorizationDate
`func (o *Systems) UnsetUseAuthorizationDate()`

UnsetUseAuthorizationDate ensures that no value is present for UseAuthorizationDate, not even an explicit nil
### GetReciprocityAcceptanceDate

`func (o *Systems) GetReciprocityAcceptanceDate() int32`

GetReciprocityAcceptanceDate returns the ReciprocityAcceptanceDate field if non-nil, zero value otherwise.

### GetReciprocityAcceptanceDateOk

`func (o *Systems) GetReciprocityAcceptanceDateOk() (*int32, bool)`

GetReciprocityAcceptanceDateOk returns a tuple with the ReciprocityAcceptanceDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetReciprocityAcceptanceDate

`func (o *Systems) SetReciprocityAcceptanceDate(v int32)`

SetReciprocityAcceptanceDate sets ReciprocityAcceptanceDate field to given value.

### HasReciprocityAcceptanceDate

`func (o *Systems) HasReciprocityAcceptanceDate() bool`

HasReciprocityAcceptanceDate returns a boolean if a field has been set.

### SetReciprocityAcceptanceDateNil

`func (o *Systems) SetReciprocityAcceptanceDateNil(b bool)`

 SetReciprocityAcceptanceDateNil sets the value for ReciprocityAcceptanceDate to be an explicit nil

### UnsetReciprocityAcceptanceDate
`func (o *Systems) UnsetReciprocityAcceptanceDate()`

UnsetReciprocityAcceptanceDate ensures that no value is present for ReciprocityAcceptanceDate, not even an explicit nil
### GetUseAuthorizationTerminationDate

`func (o *Systems) GetUseAuthorizationTerminationDate() int32`

GetUseAuthorizationTerminationDate returns the UseAuthorizationTerminationDate field if non-nil, zero value otherwise.

### GetUseAuthorizationTerminationDateOk

`func (o *Systems) GetUseAuthorizationTerminationDateOk() (*int32, bool)`

GetUseAuthorizationTerminationDateOk returns a tuple with the UseAuthorizationTerminationDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUseAuthorizationTerminationDate

`func (o *Systems) SetUseAuthorizationTerminationDate(v int32)`

SetUseAuthorizationTerminationDate sets UseAuthorizationTerminationDate field to given value.

### HasUseAuthorizationTerminationDate

`func (o *Systems) HasUseAuthorizationTerminationDate() bool`

HasUseAuthorizationTerminationDate returns a boolean if a field has been set.

### SetUseAuthorizationTerminationDateNil

`func (o *Systems) SetUseAuthorizationTerminationDateNil(b bool)`

 SetUseAuthorizationTerminationDateNil sets the value for UseAuthorizationTerminationDate to be an explicit nil

### UnsetUseAuthorizationTerminationDate
`func (o *Systems) UnsetUseAuthorizationTerminationDate()`

UnsetUseAuthorizationTerminationDate ensures that no value is present for UseAuthorizationTerminationDate, not even an explicit nil
### GetReciprocityAcceptanceTerminationDate

`func (o *Systems) GetReciprocityAcceptanceTerminationDate() int32`

GetReciprocityAcceptanceTerminationDate returns the ReciprocityAcceptanceTerminationDate field if non-nil, zero value otherwise.

### GetReciprocityAcceptanceTerminationDateOk

`func (o *Systems) GetReciprocityAcceptanceTerminationDateOk() (*int32, bool)`

GetReciprocityAcceptanceTerminationDateOk returns a tuple with the ReciprocityAcceptanceTerminationDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetReciprocityAcceptanceTerminationDate

`func (o *Systems) SetReciprocityAcceptanceTerminationDate(v int32)`

SetReciprocityAcceptanceTerminationDate sets ReciprocityAcceptanceTerminationDate field to given value.

### HasReciprocityAcceptanceTerminationDate

`func (o *Systems) HasReciprocityAcceptanceTerminationDate() bool`

HasReciprocityAcceptanceTerminationDate returns a boolean if a field has been set.

### SetReciprocityAcceptanceTerminationDateNil

`func (o *Systems) SetReciprocityAcceptanceTerminationDateNil(b bool)`

 SetReciprocityAcceptanceTerminationDateNil sets the value for ReciprocityAcceptanceTerminationDate to be an explicit nil

### UnsetReciprocityAcceptanceTerminationDate
`func (o *Systems) UnsetReciprocityAcceptanceTerminationDate()`

UnsetReciprocityAcceptanceTerminationDate ensures that no value is present for ReciprocityAcceptanceTerminationDate, not even an explicit nil
### GetTermsConditionsForUseSummary

`func (o *Systems) GetTermsConditionsForUseSummary() string`

GetTermsConditionsForUseSummary returns the TermsConditionsForUseSummary field if non-nil, zero value otherwise.

### GetTermsConditionsForUseSummaryOk

`func (o *Systems) GetTermsConditionsForUseSummaryOk() (*string, bool)`

GetTermsConditionsForUseSummaryOk returns a tuple with the TermsConditionsForUseSummary field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTermsConditionsForUseSummary

`func (o *Systems) SetTermsConditionsForUseSummary(v string)`

SetTermsConditionsForUseSummary sets TermsConditionsForUseSummary field to given value.

### HasTermsConditionsForUseSummary

`func (o *Systems) HasTermsConditionsForUseSummary() bool`

HasTermsConditionsForUseSummary returns a boolean if a field has been set.

### SetTermsConditionsForUseSummaryNil

`func (o *Systems) SetTermsConditionsForUseSummaryNil(b bool)`

 SetTermsConditionsForUseSummaryNil sets the value for TermsConditionsForUseSummary to be an explicit nil

### UnsetTermsConditionsForUseSummary
`func (o *Systems) UnsetTermsConditionsForUseSummary()`

UnsetTermsConditionsForUseSummary ensures that no value is present for TermsConditionsForUseSummary, not even an explicit nil
### GetTermsConditionsForReciprocitySummary

`func (o *Systems) GetTermsConditionsForReciprocitySummary() string`

GetTermsConditionsForReciprocitySummary returns the TermsConditionsForReciprocitySummary field if non-nil, zero value otherwise.

### GetTermsConditionsForReciprocitySummaryOk

`func (o *Systems) GetTermsConditionsForReciprocitySummaryOk() (*string, bool)`

GetTermsConditionsForReciprocitySummaryOk returns a tuple with the TermsConditionsForReciprocitySummary field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTermsConditionsForReciprocitySummary

`func (o *Systems) SetTermsConditionsForReciprocitySummary(v string)`

SetTermsConditionsForReciprocitySummary sets TermsConditionsForReciprocitySummary field to given value.

### HasTermsConditionsForReciprocitySummary

`func (o *Systems) HasTermsConditionsForReciprocitySummary() bool`

HasTermsConditionsForReciprocitySummary returns a boolean if a field has been set.

### SetTermsConditionsForReciprocitySummaryNil

`func (o *Systems) SetTermsConditionsForReciprocitySummaryNil(b bool)`

 SetTermsConditionsForReciprocitySummaryNil sets the value for TermsConditionsForReciprocitySummary to be an explicit nil

### UnsetTermsConditionsForReciprocitySummary
`func (o *Systems) UnsetTermsConditionsForReciprocitySummary()`

UnsetTermsConditionsForReciprocitySummary ensures that no value is present for TermsConditionsForReciprocitySummary, not even an explicit nil
### GetPrimaryMissionEssentialFunction

`func (o *Systems) GetPrimaryMissionEssentialFunction() bool`

GetPrimaryMissionEssentialFunction returns the PrimaryMissionEssentialFunction field if non-nil, zero value otherwise.

### GetPrimaryMissionEssentialFunctionOk

`func (o *Systems) GetPrimaryMissionEssentialFunctionOk() (*bool, bool)`

GetPrimaryMissionEssentialFunctionOk returns a tuple with the PrimaryMissionEssentialFunction field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPrimaryMissionEssentialFunction

`func (o *Systems) SetPrimaryMissionEssentialFunction(v bool)`

SetPrimaryMissionEssentialFunction sets PrimaryMissionEssentialFunction field to given value.

### HasPrimaryMissionEssentialFunction

`func (o *Systems) HasPrimaryMissionEssentialFunction() bool`

HasPrimaryMissionEssentialFunction returns a boolean if a field has been set.

### SetPrimaryMissionEssentialFunctionNil

`func (o *Systems) SetPrimaryMissionEssentialFunctionNil(b bool)`

 SetPrimaryMissionEssentialFunctionNil sets the value for PrimaryMissionEssentialFunction to be an explicit nil

### UnsetPrimaryMissionEssentialFunction
`func (o *Systems) UnsetPrimaryMissionEssentialFunction()`

UnsetPrimaryMissionEssentialFunction ensures that no value is present for PrimaryMissionEssentialFunction, not even an explicit nil
### GetPmefDescription

`func (o *Systems) GetPmefDescription() string`

GetPmefDescription returns the PmefDescription field if non-nil, zero value otherwise.

### GetPmefDescriptionOk

`func (o *Systems) GetPmefDescriptionOk() (*string, bool)`

GetPmefDescriptionOk returns a tuple with the PmefDescription field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPmefDescription

`func (o *Systems) SetPmefDescription(v string)`

SetPmefDescription sets PmefDescription field to given value.

### HasPmefDescription

`func (o *Systems) HasPmefDescription() bool`

HasPmefDescription returns a boolean if a field has been set.

### SetPmefDescriptionNil

`func (o *Systems) SetPmefDescriptionNil(b bool)`

 SetPmefDescriptionNil sets the value for PmefDescription to be an explicit nil

### UnsetPmefDescription
`func (o *Systems) UnsetPmefDescription()`

UnsetPmefDescription ensures that no value is present for PmefDescription, not even an explicit nil
### GetMissionEssentialFunction

`func (o *Systems) GetMissionEssentialFunction() bool`

GetMissionEssentialFunction returns the MissionEssentialFunction field if non-nil, zero value otherwise.

### GetMissionEssentialFunctionOk

`func (o *Systems) GetMissionEssentialFunctionOk() (*bool, bool)`

GetMissionEssentialFunctionOk returns a tuple with the MissionEssentialFunction field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMissionEssentialFunction

`func (o *Systems) SetMissionEssentialFunction(v bool)`

SetMissionEssentialFunction sets MissionEssentialFunction field to given value.

### HasMissionEssentialFunction

`func (o *Systems) HasMissionEssentialFunction() bool`

HasMissionEssentialFunction returns a boolean if a field has been set.

### SetMissionEssentialFunctionNil

`func (o *Systems) SetMissionEssentialFunctionNil(b bool)`

 SetMissionEssentialFunctionNil sets the value for MissionEssentialFunction to be an explicit nil

### UnsetMissionEssentialFunction
`func (o *Systems) UnsetMissionEssentialFunction()`

UnsetMissionEssentialFunction ensures that no value is present for MissionEssentialFunction, not even an explicit nil
### GetMefDescription

`func (o *Systems) GetMefDescription() string`

GetMefDescription returns the MefDescription field if non-nil, zero value otherwise.

### GetMefDescriptionOk

`func (o *Systems) GetMefDescriptionOk() (*string, bool)`

GetMefDescriptionOk returns a tuple with the MefDescription field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMefDescription

`func (o *Systems) SetMefDescription(v string)`

SetMefDescription sets MefDescription field to given value.

### HasMefDescription

`func (o *Systems) HasMefDescription() bool`

HasMefDescription returns a boolean if a field has been set.

### SetMefDescriptionNil

`func (o *Systems) SetMefDescriptionNil(b bool)`

 SetMefDescriptionNil sets the value for MefDescription to be an explicit nil

### UnsetMefDescription
`func (o *Systems) UnsetMefDescription()`

UnsetMefDescription ensures that no value is present for MefDescription, not even an explicit nil
### GetAdministration

`func (o *Systems) GetAdministration() string`

GetAdministration returns the Administration field if non-nil, zero value otherwise.

### GetAdministrationOk

`func (o *Systems) GetAdministrationOk() (*string, bool)`

GetAdministrationOk returns a tuple with the Administration field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAdministration

`func (o *Systems) SetAdministration(v string)`

SetAdministration sets Administration field to given value.

### HasAdministration

`func (o *Systems) HasAdministration() bool`

HasAdministration returns a boolean if a field has been set.

### SetAdministrationNil

`func (o *Systems) SetAdministrationNil(b bool)`

 SetAdministrationNil sets the value for Administration to be an explicit nil

### UnsetAdministration
`func (o *Systems) UnsetAdministration()`

UnsetAdministration ensures that no value is present for Administration, not even an explicit nil
### GetAdministrationOtherJustification

`func (o *Systems) GetAdministrationOtherJustification() string`

GetAdministrationOtherJustification returns the AdministrationOtherJustification field if non-nil, zero value otherwise.

### GetAdministrationOtherJustificationOk

`func (o *Systems) GetAdministrationOtherJustificationOk() (*string, bool)`

GetAdministrationOtherJustificationOk returns a tuple with the AdministrationOtherJustification field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAdministrationOtherJustification

`func (o *Systems) SetAdministrationOtherJustification(v string)`

SetAdministrationOtherJustification sets AdministrationOtherJustification field to given value.

### HasAdministrationOtherJustification

`func (o *Systems) HasAdministrationOtherJustification() bool`

HasAdministrationOtherJustification returns a boolean if a field has been set.

### SetAdministrationOtherJustificationNil

`func (o *Systems) SetAdministrationOtherJustificationNil(b bool)`

 SetAdministrationOtherJustificationNil sets the value for AdministrationOtherJustification to be an explicit nil

### UnsetAdministrationOtherJustification
`func (o *Systems) UnsetAdministrationOtherJustification()`

UnsetAdministrationOtherJustification ensures that no value is present for AdministrationOtherJustification, not even an explicit nil
### GetAtcIatcGrantedDate

`func (o *Systems) GetAtcIatcGrantedDate() int32`

GetAtcIatcGrantedDate returns the AtcIatcGrantedDate field if non-nil, zero value otherwise.

### GetAtcIatcGrantedDateOk

`func (o *Systems) GetAtcIatcGrantedDateOk() (*int32, bool)`

GetAtcIatcGrantedDateOk returns a tuple with the AtcIatcGrantedDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAtcIatcGrantedDate

`func (o *Systems) SetAtcIatcGrantedDate(v int32)`

SetAtcIatcGrantedDate sets AtcIatcGrantedDate field to given value.

### HasAtcIatcGrantedDate

`func (o *Systems) HasAtcIatcGrantedDate() bool`

HasAtcIatcGrantedDate returns a boolean if a field has been set.

### SetAtcIatcGrantedDateNil

`func (o *Systems) SetAtcIatcGrantedDateNil(b bool)`

 SetAtcIatcGrantedDateNil sets the value for AtcIatcGrantedDate to be an explicit nil

### UnsetAtcIatcGrantedDate
`func (o *Systems) UnsetAtcIatcGrantedDate()`

UnsetAtcIatcGrantedDate ensures that no value is present for AtcIatcGrantedDate, not even an explicit nil
### GetAtcIatcExpirationDate

`func (o *Systems) GetAtcIatcExpirationDate() int32`

GetAtcIatcExpirationDate returns the AtcIatcExpirationDate field if non-nil, zero value otherwise.

### GetAtcIatcExpirationDateOk

`func (o *Systems) GetAtcIatcExpirationDateOk() (*int32, bool)`

GetAtcIatcExpirationDateOk returns a tuple with the AtcIatcExpirationDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAtcIatcExpirationDate

`func (o *Systems) SetAtcIatcExpirationDate(v int32)`

SetAtcIatcExpirationDate sets AtcIatcExpirationDate field to given value.

### HasAtcIatcExpirationDate

`func (o *Systems) HasAtcIatcExpirationDate() bool`

HasAtcIatcExpirationDate returns a boolean if a field has been set.

### SetAtcIatcExpirationDateNil

`func (o *Systems) SetAtcIatcExpirationDateNil(b bool)`

 SetAtcIatcExpirationDateNil sets the value for AtcIatcExpirationDate to be an explicit nil

### UnsetAtcIatcExpirationDate
`func (o *Systems) UnsetAtcIatcExpirationDate()`

UnsetAtcIatcExpirationDate ensures that no value is present for AtcIatcExpirationDate, not even an explicit nil
### GetAtcIatcPendingItems

`func (o *Systems) GetAtcIatcPendingItems() string`

GetAtcIatcPendingItems returns the AtcIatcPendingItems field if non-nil, zero value otherwise.

### GetAtcIatcPendingItemsOk

`func (o *Systems) GetAtcIatcPendingItemsOk() (*string, bool)`

GetAtcIatcPendingItemsOk returns a tuple with the AtcIatcPendingItems field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAtcIatcPendingItems

`func (o *Systems) SetAtcIatcPendingItems(v string)`

SetAtcIatcPendingItems sets AtcIatcPendingItems field to given value.

### HasAtcIatcPendingItems

`func (o *Systems) HasAtcIatcPendingItems() bool`

HasAtcIatcPendingItems returns a boolean if a field has been set.

### SetAtcIatcPendingItemsNil

`func (o *Systems) SetAtcIatcPendingItemsNil(b bool)`

 SetAtcIatcPendingItemsNil sets the value for AtcIatcPendingItems to be an explicit nil

### UnsetAtcIatcPendingItems
`func (o *Systems) UnsetAtcIatcPendingItems()`

UnsetAtcIatcPendingItems ensures that no value is present for AtcIatcPendingItems, not even an explicit nil
### GetPendingItemsDueDate

`func (o *Systems) GetPendingItemsDueDate() int32`

GetPendingItemsDueDate returns the PendingItemsDueDate field if non-nil, zero value otherwise.

### GetPendingItemsDueDateOk

`func (o *Systems) GetPendingItemsDueDateOk() (*int32, bool)`

GetPendingItemsDueDateOk returns a tuple with the PendingItemsDueDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPendingItemsDueDate

`func (o *Systems) SetPendingItemsDueDate(v int32)`

SetPendingItemsDueDate sets PendingItemsDueDate field to given value.

### HasPendingItemsDueDate

`func (o *Systems) HasPendingItemsDueDate() bool`

HasPendingItemsDueDate returns a boolean if a field has been set.

### SetPendingItemsDueDateNil

`func (o *Systems) SetPendingItemsDueDateNil(b bool)`

 SetPendingItemsDueDateNil sets the value for PendingItemsDueDate to be an explicit nil

### UnsetPendingItemsDueDate
`func (o *Systems) UnsetPendingItemsDueDate()`

UnsetPendingItemsDueDate ensures that no value is present for PendingItemsDueDate, not even an explicit nil
### GetDodinnSystemId

`func (o *Systems) GetDodinnSystemId() bool`

GetDodinnSystemId returns the DodinnSystemId field if non-nil, zero value otherwise.

### GetDodinnSystemIdOk

`func (o *Systems) GetDodinnSystemIdOk() (*bool, bool)`

GetDodinnSystemIdOk returns a tuple with the DodinnSystemId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDodinnSystemId

`func (o *Systems) SetDodinnSystemId(v bool)`

SetDodinnSystemId sets DodinnSystemId field to given value.

### HasDodinnSystemId

`func (o *Systems) HasDodinnSystemId() bool`

HasDodinnSystemId returns a boolean if a field has been set.

### SetDodinnSystemIdNil

`func (o *Systems) SetDodinnSystemIdNil(b bool)`

 SetDodinnSystemIdNil sets the value for DodinnSystemId to be an explicit nil

### UnsetDodinnSystemId
`func (o *Systems) UnsetDodinnSystemId()`

UnsetDodinnSystemId ensures that no value is present for DodinnSystemId, not even an explicit nil
### GetAuthorizationToUseConnectStatus

`func (o *Systems) GetAuthorizationToUseConnectStatus() string`

GetAuthorizationToUseConnectStatus returns the AuthorizationToUseConnectStatus field if non-nil, zero value otherwise.

### GetAuthorizationToUseConnectStatusOk

`func (o *Systems) GetAuthorizationToUseConnectStatusOk() (*string, bool)`

GetAuthorizationToUseConnectStatusOk returns a tuple with the AuthorizationToUseConnectStatus field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAuthorizationToUseConnectStatus

`func (o *Systems) SetAuthorizationToUseConnectStatus(v string)`

SetAuthorizationToUseConnectStatus sets AuthorizationToUseConnectStatus field to given value.

### HasAuthorizationToUseConnectStatus

`func (o *Systems) HasAuthorizationToUseConnectStatus() bool`

HasAuthorizationToUseConnectStatus returns a boolean if a field has been set.

### SetAuthorizationToUseConnectStatusNil

`func (o *Systems) SetAuthorizationToUseConnectStatusNil(b bool)`

 SetAuthorizationToUseConnectStatusNil sets the value for AuthorizationToUseConnectStatus to be an explicit nil

### UnsetAuthorizationToUseConnectStatus
`func (o *Systems) UnsetAuthorizationToUseConnectStatus()`

UnsetAuthorizationToUseConnectStatus ensures that no value is present for AuthorizationToUseConnectStatus, not even an explicit nil
### GetUseConnectAuthorizationDate

`func (o *Systems) GetUseConnectAuthorizationDate() int32`

GetUseConnectAuthorizationDate returns the UseConnectAuthorizationDate field if non-nil, zero value otherwise.

### GetUseConnectAuthorizationDateOk

`func (o *Systems) GetUseConnectAuthorizationDateOk() (*int32, bool)`

GetUseConnectAuthorizationDateOk returns a tuple with the UseConnectAuthorizationDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUseConnectAuthorizationDate

`func (o *Systems) SetUseConnectAuthorizationDate(v int32)`

SetUseConnectAuthorizationDate sets UseConnectAuthorizationDate field to given value.

### HasUseConnectAuthorizationDate

`func (o *Systems) HasUseConnectAuthorizationDate() bool`

HasUseConnectAuthorizationDate returns a boolean if a field has been set.

### SetUseConnectAuthorizationDateNil

`func (o *Systems) SetUseConnectAuthorizationDateNil(b bool)`

 SetUseConnectAuthorizationDateNil sets the value for UseConnectAuthorizationDate to be an explicit nil

### UnsetUseConnectAuthorizationDate
`func (o *Systems) UnsetUseConnectAuthorizationDate()`

UnsetUseConnectAuthorizationDate ensures that no value is present for UseConnectAuthorizationDate, not even an explicit nil
### GetUseConnectAuthorizationTerminationDate

`func (o *Systems) GetUseConnectAuthorizationTerminationDate() int32`

GetUseConnectAuthorizationTerminationDate returns the UseConnectAuthorizationTerminationDate field if non-nil, zero value otherwise.

### GetUseConnectAuthorizationTerminationDateOk

`func (o *Systems) GetUseConnectAuthorizationTerminationDateOk() (*int32, bool)`

GetUseConnectAuthorizationTerminationDateOk returns a tuple with the UseConnectAuthorizationTerminationDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUseConnectAuthorizationTerminationDate

`func (o *Systems) SetUseConnectAuthorizationTerminationDate(v int32)`

SetUseConnectAuthorizationTerminationDate sets UseConnectAuthorizationTerminationDate field to given value.

### HasUseConnectAuthorizationTerminationDate

`func (o *Systems) HasUseConnectAuthorizationTerminationDate() bool`

HasUseConnectAuthorizationTerminationDate returns a boolean if a field has been set.

### SetUseConnectAuthorizationTerminationDateNil

`func (o *Systems) SetUseConnectAuthorizationTerminationDateNil(b bool)`

 SetUseConnectAuthorizationTerminationDateNil sets the value for UseConnectAuthorizationTerminationDate to be an explicit nil

### UnsetUseConnectAuthorizationTerminationDate
`func (o *Systems) UnsetUseConnectAuthorizationTerminationDate()`

UnsetUseConnectAuthorizationTerminationDate ensures that no value is present for UseConnectAuthorizationTerminationDate, not even an explicit nil
### GetTermsConditionsForUseConnectSummary

`func (o *Systems) GetTermsConditionsForUseConnectSummary() string`

GetTermsConditionsForUseConnectSummary returns the TermsConditionsForUseConnectSummary field if non-nil, zero value otherwise.

### GetTermsConditionsForUseConnectSummaryOk

`func (o *Systems) GetTermsConditionsForUseConnectSummaryOk() (*string, bool)`

GetTermsConditionsForUseConnectSummaryOk returns a tuple with the TermsConditionsForUseConnectSummary field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTermsConditionsForUseConnectSummary

`func (o *Systems) SetTermsConditionsForUseConnectSummary(v string)`

SetTermsConditionsForUseConnectSummary sets TermsConditionsForUseConnectSummary field to given value.

### HasTermsConditionsForUseConnectSummary

`func (o *Systems) HasTermsConditionsForUseConnectSummary() bool`

HasTermsConditionsForUseConnectSummary returns a boolean if a field has been set.

### SetTermsConditionsForUseConnectSummaryNil

`func (o *Systems) SetTermsConditionsForUseConnectSummaryNil(b bool)`

 SetTermsConditionsForUseConnectSummaryNil sets the value for TermsConditionsForUseConnectSummary to be an explicit nil

### UnsetTermsConditionsForUseConnectSummary
`func (o *Systems) UnsetTermsConditionsForUseConnectSummary()`

UnsetTermsConditionsForUseConnectSummary ensures that no value is present for TermsConditionsForUseConnectSummary, not even an explicit nil
### GetWorkstations

`func (o *Systems) GetWorkstations() int32`

GetWorkstations returns the Workstations field if non-nil, zero value otherwise.

### GetWorkstationsOk

`func (o *Systems) GetWorkstationsOk() (*int32, bool)`

GetWorkstationsOk returns a tuple with the Workstations field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWorkstations

`func (o *Systems) SetWorkstations(v int32)`

SetWorkstations sets Workstations field to given value.

### HasWorkstations

`func (o *Systems) HasWorkstations() bool`

HasWorkstations returns a boolean if a field has been set.

### SetWorkstationsNil

`func (o *Systems) SetWorkstationsNil(b bool)`

 SetWorkstationsNil sets the value for Workstations to be an explicit nil

### UnsetWorkstations
`func (o *Systems) UnsetWorkstations()`

UnsetWorkstations ensures that no value is present for Workstations, not even an explicit nil
### GetServers

`func (o *Systems) GetServers() int32`

GetServers returns the Servers field if non-nil, zero value otherwise.

### GetServersOk

`func (o *Systems) GetServersOk() (*int32, bool)`

GetServersOk returns a tuple with the Servers field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetServers

`func (o *Systems) SetServers(v int32)`

SetServers sets Servers field to given value.

### HasServers

`func (o *Systems) HasServers() bool`

HasServers returns a boolean if a field has been set.

### SetServersNil

`func (o *Systems) SetServersNil(b bool)`

 SetServersNil sets the value for Servers to be an explicit nil

### UnsetServers
`func (o *Systems) UnsetServers()`

UnsetServers ensures that no value is present for Servers, not even an explicit nil
### GetConnectivityCcsd

`func (o *Systems) GetConnectivityCcsd() []ConnectivityCcsd`

GetConnectivityCcsd returns the ConnectivityCcsd field if non-nil, zero value otherwise.

### GetConnectivityCcsdOk

`func (o *Systems) GetConnectivityCcsdOk() (*[]ConnectivityCcsd, bool)`

GetConnectivityCcsdOk returns a tuple with the ConnectivityCcsd field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetConnectivityCcsd

`func (o *Systems) SetConnectivityCcsd(v []ConnectivityCcsd)`

SetConnectivityCcsd sets ConnectivityCcsd field to given value.

### HasConnectivityCcsd

`func (o *Systems) HasConnectivityCcsd() bool`

HasConnectivityCcsd returns a boolean if a field has been set.

### SetConnectivityCcsdNil

`func (o *Systems) SetConnectivityCcsdNil(b bool)`

 SetConnectivityCcsdNil sets the value for ConnectivityCcsd to be an explicit nil

### UnsetConnectivityCcsd
`func (o *Systems) UnsetConnectivityCcsd()`

UnsetConnectivityCcsd ensures that no value is present for ConnectivityCcsd, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


