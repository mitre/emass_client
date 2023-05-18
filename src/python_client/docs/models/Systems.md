# emass_client.model.systems.Systems

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**registrationCompletionDate** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | [Read-Only] Date the system was registered into eMASS. | [optional] 
**systemLifeCycleAcquisitionPhase** | None, str,  | NoneClass, str,  | [Read-Only] Identifies the current System Acquisition Phase for programs of record. | [optional] 
**specialType** | None, str,  | NoneClass, str,  | [Read-Only] Lists applicable tracking indicator(s). | [optional] 
**specialTypeDescription** | None, str,  | NoneClass, str,  | [Read-Only] Provides a brief reason for any tracking indicator(s) selected. | [optional] 
**missionPortfolio** | None, str,  | NoneClass, str,  | [Read-Only] Identifies the appropriate portfolio or capability area. Navy only. | [optional] 
**isNNPI** | None, bool,  | NoneClass, BoolClass,  | [Read-Only] Indicates whether Naval Nuclear Propulsion Information (NNPI) is stored, disseminated, or processed through this system. Navy only. | [optional] 
**isRBC** | None, bool,  | NoneClass, BoolClass,  | [Read-Only] Indicates whether the system is pursuing an RBC authorization. Navy only. | [optional] 
**isWaiver** | None, bool,  | NoneClass, BoolClass,  | [Read-Only] Indicates if the system has a waiver from OPNAV N2N6G (DDCIO(N)) to proceed with a DIACAP accreditation. Navy and DIACAP only. | [optional] 
**programOffice** | None, str,  | NoneClass, str,  | [Read-Only] The system record&#x27;s Program Office. Navy only. | [optional] 
**vramId** | None, str,  | NoneClass, str,  | [Read-Only] Vulnerability Remediation Asset Manager (VRAM) identification number. \&quot;N/A\&quot; indicates the system record is not currently registered in VRAM.  Navy only. | [optional] 
**systemId** | decimal.Decimal, int,  | decimal.Decimal,  | [Read-only] Unique system record identifier. | [optional] value must be a 64 bit integer
**policy** | None, str,  | NoneClass, str,  | [Read-only] RMF/DIACAP Policy identifier for the system record. | [optional] must be one of ["RMF", "DIACAP", ] 
**registrationType** | None, str,  | NoneClass, str,  | [Read-Only] Registration types parameters (assessAndAuthorize, assessOnly, guest, regular, functional, cloudServiceProvider.) | [optional] must be one of ["Assess and Authorize", "Assess Only", "Guest", "Regular", "Functional", "Cloud Service Provider", "Common Control Provider", ] 
**name** | None, str,  | NoneClass, str,  | [Read-only] Name of the system record. | [optional] 
**acronym** | None, str,  | NoneClass, str,  | [Read-only] Acronym of the system record. | [optional] 
**description** | None, str,  | NoneClass, str,  | [Read-only] Description of the system record. | [optional] 
**instance** | None, str,  | NoneClass, str,  | [Read-Only] Name of the top-level component that owns the system. | [optional] 
**owningOrganization** | None, str,  | NoneClass, str,  | [Read-Only] Owning organization of the system record. Values match the eMASS instance Organizational Hierarchy. | [optional] 
**secondaryOrganization** | None, str,  | NoneClass, str,  | [Read-only] Secondary organization that owns the system record (i.e. Sub-Organization-level. | [optional] 
**versionReleaseNo** | None, str,  | NoneClass, str,  | [Read-only] Version/Release Number of system record. | [optional] 
**systemType** | None, str,  | NoneClass, str,  | [Read-only] Type of the system record. RMF values include the following options (IS Major Application, IS Enclave, Platform IT System). DIACAP values include the following options (Platform IT Interconnection, AIS Application, Outsourced IT-Based Process (DoD-controlled), Enclave, Outsourced IT-Based Process (service provider shared)) | [optional] must be one of ["IS Major Application", "IS Enclave", "Platform IT", "Platform IT System", "Platform IT Interconnection", "AIS Application", "Outsourced IT-Based Process (DoD-controlled)", "Enclave", "Outsourced IT-Based Process (service provider shared)", ] 
**isNSS** | None, bool,  | NoneClass, BoolClass,  | [Read-only] Is the system record a National Security System? | [optional] 
**isPublicFacing** | None, bool,  | NoneClass, BoolClass,  | [Read-only] Does the system record have a public facing component/presence. | [optional] 
**coamsId** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | [Read-only] Corresponding Cyber Operational Attributes Management System (COAMS) identifier for the system record. | [optional] value must be a 64 bit integer
**isTypeAuthorization** | None, bool,  | NoneClass, BoolClass,  | [Read-only] Identifies if system is a Type Authorization. | [optional] 
**ditprId** | str,  | str,  | [Read-only] DITPR ID of the system record. | [optional] 
**apmsId** | None, str,  | NoneClass, str,  | [Read-Only] Same field as ditprId but displays as apmsId for Army only. | [optional] 
**vasiId** | None, str,  | NoneClass, str,  | [Read-Only] Same field as ditprId but displays as vasiId for VA only. | [optional] 
**authorizationStatus** | None, str,  | NoneClass, str,  | [Read-only] Authorization Status of the system record. | [optional] 
**authorizationDate** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | [Read-only] Authorization Date of the system record. | [optional] 
**authorizationTerminationDate** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | [Read-only] Authorization Termination Date of the system record. | [optional] 
**authorizationLength** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | [Read-only] Length of system&#x27;s Authorization. Calculated based off of Authorization Date &amp; Authorization Termination Date. | [optional] 
**termsForAuth** | None, str,  | NoneClass, str,  | [Read-only] Terms/Conditions for receiving and maintaining the system&#x27;s Authorization. Assigned by the Authorizing Official. | [optional] 
**securityPlanApprovalStatus** | None, str,  | NoneClass, str,  | [Read-only] Status of the approval of the system&#x27;s RMF Security Plan. Values include the following options (Approved, Denied, Not Yet Approved). | [optional] must be one of ["Approved", "Not Yet Approved", "Denied", ] 
**securityPlanApprovalDate** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | [Read-only] Approval date of the system&#x27;s RMF Security Plan. | [optional] 
**missionCriticality** | None, str,  | NoneClass, str,  | [Read-only] Mission Criticality of the system record. | [optional] 
**geographicalAssociation** | None, str,  | NoneClass, str,  | [Read-only] Geographical Association of the system record. | [optional] 
**systemOwnership** | None, str,  | NoneClass, str,  | [Read-only] Ownership of the system record. | [optional] 
**governingMissionArea** | None, str,  | NoneClass, str,  | [Read-only] Governing Mission Area of the system record. | [optional] 
**primaryFunctionalArea** | None, str,  | NoneClass, str,  | [Read-only] Primary functional area of the system record. | [optional] 
**secondaryFunctionalArea** | None, str,  | NoneClass, str,  | [Read-only] Secondary functional area of the system record. | [optional] 
**primaryControlSet** | None, str,  | NoneClass, str,  | [Read-only] Primary Control Set of the system record. RMF values include the following options (NIST SP 800-53 Revision 4), DIACAP values include the following options (DoDI 8500.2) | [optional] must be one of ["NIST SP 800-53 Revision 4", "DoDI 8500.2", ] 
**confidentiality** | None, str,  | NoneClass, str,  | [Read-only] Confidentiality of the system record. RMF values include the following options (High, Moderate, Low) | [optional] must be one of ["High", "Moderate", "Low", ] 
**integrity** | None, str,  | NoneClass, str,  | [Read-only] Integrity of the system record. RMF values include the following options (High, Moderate, Low) | [optional] must be one of ["High", "Moderate", "Low", ] 
**availability** | None, str,  | NoneClass, str,  | [Read-only] Availability of the system record. RMF values include the following options (High, Moderate, Low) | [optional] must be one of ["High", "Moderate", "Low", ] 
**appliedOverlays** | None, str,  | NoneClass, str,  | [Read-only] Overlays applied to the system record. | [optional] 
**rmfActivity** | None, str,  | NoneClass, str,  | [Read-only] RMF Activity of the system record. | [optional] 
**crossDomainTicket** | None, str,  | NoneClass, str,  | [Read-only] Cross Domain Tickets of the system record. | [optional] 
**ditprDonId** | None, str,  | NoneClass, str,  | [Read-Only] DITPR-DON identifier of the system record. | [optional] 
**mac** | None, str,  | NoneClass, str,  | [Read-Only] MAC level of the system record. | [optional] must be one of ["I", "II", "III", ] 
**dodConfidentiality** | None, str,  | NoneClass, str,  | [Read-Only] DoD Confidentiality level of the system record. | [optional] must be one of ["Public", "Sensitive", "Classified", ] 
**contingencyPlanTested** | None, bool,  | NoneClass, BoolClass,  | [Read-only] Has the system record&#x27;s Contingency Plan been tested? | [optional] 
**contingencyPlanTestDate** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | [Read-only] Date the system record&#x27;s Contingency Plan was tested. | [optional] 
**securityReviewDate** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | [Read-only] Date the system record&#x27;s Annual Security Review was conducted. | [optional] 
**hasOpenPoamItem** | None, bool,  | NoneClass, BoolClass,  | [Read-Only] Does the system record have an Ongoing or Risk Accepted POA&amp;M Item? | [optional] 
**hasOpenPoamItem90to120PastScheduledCompletionDate** | None, bool,  | NoneClass, BoolClass,  | [Read-Only] Does the system record have an Ongoing or Risk Accepted POA&amp;M Item 90 to 120 days past its Scheduled Completion Date? | [optional] 
**hasOpenPoamItem120PlusPastScheudledCompletionDate** | None, bool,  | NoneClass, BoolClass,  | [Read-Only] Does the system record have an Ongoing or Risk Accepted POA&amp;M Item 120 days past its Scheduled Completion Date? | [optional] 
**impact** | None, str,  | NoneClass, str,  | [Optional] Values include the following options (Very Low, Low, Moderate,High,Very High) | [optional] must be one of ["Low", "Moderate", "High", ] 
**hasCUI** | None, bool,  | NoneClass, BoolClass,  | [Read-only] Does the system record contain and/or process Controlled Unclassified information? | [optional] 
**hasPII** | None, bool,  | NoneClass, BoolClass,  | [Read-only] Does the system record contain and/or process Personally Identifiable Information? | [optional] 
**hasPHI** | None, bool,  | NoneClass, BoolClass,  | [Read-only] Does the system record contain and/or process Personal Health Information? | [optional] 
**ppsmRegistryNumber** | None, str,  | NoneClass, str,  | [Read-only] Unique identifier for the DoD’s Ports, Protocols, and Services Management Registry system. | [optional] 
**interconnectedInformationSystemAndIdentifiers** | None, str,  | NoneClass, str,  | [Read-only] Identify the interconnected information systems and corresponding identifiers within control CA-3. | [optional] 
**isPiaRequired** | None, bool,  | NoneClass, BoolClass,  | [Read-only] Does the system require a Privacy Impact Assessment? | [optional] 
**piaStatus** | None, str,  | NoneClass, str,  | [Read-only] Status of the PIA, availability values include the following options (Not Started, In Progress, Completed) | [optional] must be one of ["Not Started", "In Progress", "Completed", ] 
**piaDate** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | [Read-only] Date in which the system&#x27;s PIA took place. | [optional] 
**userDefinedField1** | None, str,  | NoneClass, str,  | [Read-only] User-defined field to augment Ad Hoc Reporting. | [optional] 
**userDefinedField2** | None, str,  | NoneClass, str,  | [Read-only] User-defined field to augment Ad Hoc Reporting. | [optional] 
**userDefinedField3** | None, str,  | NoneClass, str,  | [Read-only] User-defined field to augment Ad Hoc Reporting. | [optional] 
**userDefinedField4** | None, str,  | NoneClass, str,  | [Read-only] User-defined field to augment Ad Hoc Reporting. | [optional] 
**userDefinedField5** | None, str,  | NoneClass, str,  | [Read-only] User-defined field to augment Ad Hoc Reporting. | [optional] 
**currentRmfLifecycleStep** | None, str,  | NoneClass, str,  | [Read-only] Displays the system&#x27;s current step within the RMF Lifecycle. | [optional] must be one of ["1 - Categorize", "2 - Select", "3 - Implement", "4 - Assess", "5 - Authorize", "6 - Monitor", ] 
**otherInformation** | None, str,  | NoneClass, str,  | [Read-only] Include any additional information required by the organization. | [optional] 
**reportsForScorecard** | None, bool,  | NoneClass, BoolClass,  | [Read-only] Indicates if the system reports to the DoD Cyber Hygiene Scorecard. | [optional] 
**highestSystemDataClassification** | None, str,  | NoneClass, str,  | [Read-Only] The overall classification level of information that the System is approved to collect, process, store, and/or distribute. | [optional] 
**overallClassification** | None, str,  | NoneClass, str,  | [Read-Only] Same field as highestSystemDataClassification, but displays as overallClassification for NISP only. | [optional] 
**isHVA** | None, bool,  | NoneClass, BoolClass,  | [Read-Only] Indicates if the system contains High Value Assets. Does not display if value is null | [optional] 
**isFinancialManagement** | None, bool,  | NoneClass, BoolClass,  | [Read-Only] Per OMB Circular A-127, a financial management system includes the core financial systems and the financial portions  of mixed systems necessary to support financial management, including automated and manual processes, procedures, and  controls, data, hardware, software, and support personnel dedicated to the operation and maintenance of system functions. The following are examples of financial management systems: core financial systems, procurement systems, loan systems, grants systems, payroll systems, budget formulation systems, billing systems, and travel systems.  | [optional] 
**isReciprocity** | None, bool,  | NoneClass, BoolClass,  | [Read-Only] A reciprocity system is any information system that is part of a mutual agreement among participating organizations to accept each other&#x27;s security assessments in order to reuse information system resources and/or to accept each other&#x27;s assessed security posture in order to share information.  | [optional] 
**reciprocityExemption** | None, str,  | NoneClass, str,  | [Read-Only] The following justifications are acceptable for exemption from reciprocity: (a) the existence of the system is classified (not the data, but the existence of the system) or (b) the system&#x27;s authorization to operate is in the process of being pulled (e.g. DATO, Decommission).  | [optional] 
**cloudComputing** | None, bool,  | NoneClass, BoolClass,  | [Read-Only] Is this a cloud-based IS? | [optional] 
**cloudType** | None, str,  | NoneClass, str,  | [Read-Only] Values include the following: (Hybrid, Private, Public) | [optional] must be one of ["Hybrid", "Private", "Public", ] 
**atcStatus** | None, str,  | NoneClass, str,  | [Read-Only] The Authority to Connect decision. Values include the following:  (Authority to Connect (ATC), Denial of Authority to Connect (DATC), Not Yet Connected, Decommissioned)  | [optional] must be one of ["Authority to Connect (ATC)", "Denial of Authority to Connect (DATC)", "Not Yet Connected", "Decommissioned", ] 
**isSaaS** | None, bool,  | NoneClass, BoolClass,  | [Read-Only] Software as a Service (SaaS) cloud service model. | [optional] 
**isPaaS** | None, bool,  | NoneClass, BoolClass,  | [Read-Only] Platform as a Service (PaaS) cloud service model. | [optional] 
**isIaaS** | None, bool,  | NoneClass, BoolClass,  | [Read-Only] Infrastructure as a Service (IaaS) cloud service model. | [optional] 
**otherServiceModels** | None, str,  | NoneClass, str,  | [Read-Only] Free text field to include other cloud service models. | [optional] 
**needDate** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | [Read-Only] Indicates the date by which the System needs to be deployed to a production environment. | [optional] 
**overallRiskScore** | None, str,  | NoneClass, str,  | [Read-Only] The overall risk score of the system | [optional] 
**isHRR** | None, bool,  | NoneClass, BoolClass,  | [Read-Only] Identifies whether a System has been designated as High Risk Review. USCG and Navy only. | [optional] 
**atcDate** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | [Read-Only] The Connectivity Authorization Date. | [optional] 
**atcTerminationDate** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | [Read-Only] The Connectivity Authorization Termination Date. | [optional] 
**systemDevelopmentLifeCycle** | None, str,  | NoneClass, str,  | [Read-Only] Indicate the date by which the System needs to be deployed to a production environment. VA only. | [optional] 
**isFISMAReportable** | None, bool,  | NoneClass, BoolClass,  | [Read-Only] Is this IS reportable per Federal Information Security Management Act (FISMA) established requirements? VA only | [optional] 
**[package](#package)** | list, tuple, None,  | tuple, NoneClass,  |  | [optional] 
**[connectivityCcsd](#connectivityCcsd)** | list, tuple, None,  | tuple, NoneClass,  |  | [optional] 

# package

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**PacGet**](PacGet.md) | [**PacGet**](PacGet.md) | [**PacGet**](PacGet.md) |  | 

# connectivityCcsd

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ConnectivityCcsd**](ConnectivityCcsd.md) | [**ConnectivityCcsd**](ConnectivityCcsd.md) | [**ConnectivityCcsd**](ConnectivityCcsd.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

