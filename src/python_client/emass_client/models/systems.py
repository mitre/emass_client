# coding: utf-8

## eMASS API v3.12 Specification

The emass_client_api is a Python client that implements the [Enterprise Mission Assurance Support Service (eMASS)](https://disa.mil/~/media/Files/DISA/Fact-Sheets/eMASS.pdf)
Representational State Transfer (REST) Application Programming Interface (API) specifications.


This Python package was generated from the eMASS API specification:

- API version: v3.12
- Package version: 3.11.0
- Build date: 2023-10-10T00:19:35.596959Z[Etc/UTC]

## Requirements.

Python 

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import emass_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import emass_client
```

### Tests

Execute `pytest` to run the tests.

from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr, field_validator
from pydantic import Field
from typing_extensions import Annotated
from emass_client.models.connectivity_ccsd import ConnectivityCcsd
from emass_client.models.pac_get import PacGet
from typing import Dict, Any
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class Systems(BaseModel):
    """
    Systems
    """
    registration_completion_date: Optional[StrictInt] = Field(default=None, description="[Read-Only] Date the system was registered into eMASS.", alias="registrationCompletionDate")
    system_life_cycle_acquisition_phase: Optional[StrictStr] = Field(default=None, description="[Read-Only] Identifies the current System Acquisition Phase for programs of record.", alias="systemLifeCycleAcquisitionPhase")
    special_type: Optional[StrictStr] = Field(default=None, description="[Read-Only] Lists applicable tracking indicator(s).", alias="specialType")
    special_type_description: Optional[StrictStr] = Field(default=None, description="[Read-Only] Provides a brief reason for any tracking indicator(s) selected.", alias="specialTypeDescription")
    mission_portfolio: Optional[StrictStr] = Field(default=None, description="[Read-Only] Identifies the appropriate portfolio or capability area. Navy only.", alias="missionPortfolio")
    is_nnpi: Optional[StrictBool] = Field(default=None, description="[Read-Only] Indicates whether Naval Nuclear Propulsion Information (NNPI) is stored, disseminated, or processed through this system. Navy only.", alias="isNNPI")
    is_rbc: Optional[StrictBool] = Field(default=None, description="[Read-Only] Indicates whether the system is pursuing an RBC authorization. Navy only.", alias="isRBC")
    is_waiver: Optional[StrictBool] = Field(default=None, description="[Read-Only] Indicates if the system has a waiver from OPNAV N2N6G (DDCIO(N)) to proceed with a DIACAP accreditation. Navy and DIACAP only.", alias="isWaiver")
    program_office: Optional[StrictStr] = Field(default=None, description="[Read-Only] The system record's Program Office. Navy only.", alias="programOffice")
    vram_id: Optional[StrictStr] = Field(default=None, description="[Read-Only] Vulnerability Remediation Asset Manager (VRAM) identification number. \"N/A\" indicates the system record is not currently registered in VRAM.  Navy only.", alias="vramId")
    system_id: Optional[StrictInt] = Field(default=None, description="[Read-only] Unique system record identifier.", alias="systemId")
    policy: Optional[StrictStr] = Field(default=None, description="[Read-only] RMF/DIACAP Policy identifier for the system record.")
    registration_type: Optional[StrictStr] = Field(default=None, description="[Read-Only] Registration type of the system record. Values include (assessAndAuthorize, assessOnly, guest, regular, functional, cloudServiceProvider.)", alias="registrationType")
    name: Optional[StrictStr] = Field(default=None, description="[Read-only] Name of the system record.")
    acronym: Optional[StrictStr] = Field(default=None, description="[Read-only] Acronym of the system record.")
    description: Optional[StrictStr] = Field(default=None, description="[Read-only] Description of the system record.")
    instance: Optional[StrictStr] = Field(default=None, description="[Read-Only] Name of the top-level component that owns the system.")
    owning_organization: Optional[StrictStr] = Field(default=None, description="[Read-Only] Owning organization of the system record. Values match the eMASS instance Organizational Hierarchy.", alias="owningOrganization")
    secondary_organization: Optional[StrictStr] = Field(default=None, description="[Read-only] Secondary organization that owns the system record (i.e. Sub-Organization-level.", alias="secondaryOrganization")
    version_release_no: Optional[StrictStr] = Field(default=None, description="[Read-only] Version/Release Number of system record.", alias="versionReleaseNo")
    system_type: Optional[StrictStr] = Field(default=None, description="[Read-only] Type of the system record. RMF values include the following options (IS Major Application, IS Enclave, Platform IT System). DIACAP values include the following options (Platform IT Interconnection, AIS Application, Outsourced IT-Based Process (DoD-controlled), Enclave, Outsourced IT-Based Process (service provider shared))", alias="systemType")
    is_nss: Optional[StrictBool] = Field(default=None, description="[Read-only] Is the system record a National Security System?", alias="isNSS")
    is_public_facing: Optional[StrictBool] = Field(default=None, description="[Read-only] Does the system record have a public facing component/presence.", alias="isPublicFacing")
    coams_id: Optional[StrictInt] = Field(default=None, description="[Read-only] Corresponding Cyber Operational Attributes Management System (COAMS) identifier for the system record.", alias="coamsId")
    is_type_authorization: Optional[StrictBool] = Field(default=None, description="[Read-only] Identifies if system is a Type Authorization.", alias="isTypeAuthorization")
    ditpr_id: Optional[StrictStr] = Field(default=None, description="[Read-only] DITPR ID of the system record.", alias="ditprId")
    apms_id: Optional[StrictStr] = Field(default=None, description="[Read-Only] Same field as ditprId but displays as apmsId for Army only.", alias="apmsId")
    vasi_id: Optional[StrictStr] = Field(default=None, description="[Read-Only] Same field as ditprId but displays as vasiId for VA only.", alias="vasiId")
    authorization_status: Optional[StrictStr] = Field(default=None, description="[Read-only] Authorization Status of the system record.", alias="authorizationStatus")
    authorization_date: Optional[StrictInt] = Field(default=None, description="[Read-only] Authorization Date of the system record.", alias="authorizationDate")
    authorization_termination_date: Optional[StrictInt] = Field(default=None, description="[Read-only] Authorization Termination Date of the system record.", alias="authorizationTerminationDate")
    authorization_length: Optional[Annotated[int, Field(le=1825, strict=True, ge=28)]] = Field(default=None, description="[Read-only] Length of system's Authorization. Calculated based off of Authorization Date & Authorization Termination Date.", alias="authorizationLength")
    terms_for_auth: Optional[StrictStr] = Field(default=None, description="[Read-only] Terms/Conditions for receiving and maintaining the system's Authorization. Assigned by the Authorizing Official.", alias="termsForAuth")
    security_plan_approval_status: Optional[StrictStr] = Field(default=None, description="[Read-only] Status of the approval of the system's RMF Security Plan. Values include the following options (Approved, Denied, Not Yet Approved).", alias="securityPlanApprovalStatus")
    security_plan_approval_date: Optional[StrictInt] = Field(default=None, description="[Read-only] Approval date of the system's RMF Security Plan.", alias="securityPlanApprovalDate")
    mission_criticality: Optional[StrictStr] = Field(default=None, description="[Read-only] Mission Criticality of the system record.", alias="missionCriticality")
    geographical_association: Optional[StrictStr] = Field(default=None, description="[Read-only] Geographical Association of the system record.", alias="geographicalAssociation")
    system_ownership: Optional[StrictStr] = Field(default=None, description="[Read-only] Ownership of the system record.", alias="systemOwnership")
    governing_mission_area: Optional[StrictStr] = Field(default=None, description="[Read-only] Governing Mission Area of the system record.", alias="governingMissionArea")
    primary_functional_area: Optional[StrictStr] = Field(default=None, description="[Read-only] Primary functional area of the system record.", alias="primaryFunctionalArea")
    secondary_functional_area: Optional[StrictStr] = Field(default=None, description="[Read-only] Secondary functional area of the system record.", alias="secondaryFunctionalArea")
    primary_control_set: Optional[StrictStr] = Field(default=None, description="[Read-only] Primary Control Set of the system record. RMF values include the following options (NIST SP 800-53 Revision 4), DIACAP values include the following options (DoDI 8500.2)", alias="primaryControlSet")
    confidentiality: Optional[StrictStr] = Field(default=None, description="[Read-only] Confidentiality of the system record. RMF values include the following options (High, Moderate, Low)")
    integrity: Optional[StrictStr] = Field(default=None, description="[Read-only] Integrity of the system record. RMF values include the following options (High, Moderate, Low)")
    availability: Optional[StrictStr] = Field(default=None, description="[Read-only] Availability of the system record. RMF values include the following options (High, Moderate, Low)")
    applied_overlays: Optional[StrictStr] = Field(default=None, description="[Read-only] Overlays applied to the system record.", alias="appliedOverlays")
    rmf_activity: Optional[StrictStr] = Field(default=None, description="[Read-only] RMF Activity of the system record.", alias="rmfActivity")
    cross_domain_ticket: Optional[StrictStr] = Field(default=None, description="[Read-only] Cross Domain Tickets of the system record.", alias="crossDomainTicket")
    ditpr_don_id: Optional[StrictStr] = Field(default=None, description="[Read-Only] DITPR-DON identifier of the system record.", alias="ditprDonId")
    mac: Optional[StrictStr] = Field(default=None, description="[Read-Only] MAC level of the system record.")
    dod_confidentiality: Optional[StrictStr] = Field(default=None, description="[Read-Only] DoD Confidentiality level of the system record.", alias="dodConfidentiality")
    contingency_plan_tested: Optional[StrictBool] = Field(default=None, description="[Read-only] Has the system record's Contingency Plan been tested?", alias="contingencyPlanTested")
    contingency_plan_test_date: Optional[StrictInt] = Field(default=None, description="[Read-only] Date the system record's Contingency Plan was tested.", alias="contingencyPlanTestDate")
    security_review_required: Optional[StrictBool] = Field(default=None, description="[Read-Only] Is the system required to complete a Security Review?", alias="securityReviewRequired")
    security_review_completed: Optional[StrictBool] = Field(default=None, description="[Read-Only] Has a Security Review been completed for this system?", alias="securityReviewCompleted")
    security_review_completion_date: Optional[StrictInt] = Field(default=None, description="[Read-Only] Date of the system's latest security review or annual assessment.", alias="securityReviewCompletionDate")
    next_security_review_due_date: Optional[StrictInt] = Field(default=None, description="[Read-Only] Date when the system's next security review or annual assessment is due by.", alias="nextSecurityReviewDueDate")
    has_open_poam_item: Optional[StrictBool] = Field(default=None, description="[Read-Only] Does the system record have an Ongoing or Risk Accepted POA&M Item?", alias="hasOpenPoamItem")
    has_open_poam_item90to120_past_scheduled_completion_date: Optional[StrictBool] = Field(default=None, description="[Read-Only] Does the system record have an Ongoing or Risk Accepted POA&M Item 90 to 120 days past its Scheduled Completion Date?", alias="hasOpenPoamItem90to120PastScheduledCompletionDate")
    has_open_poam_item120_plus_past_scheudled_completion_date: Optional[StrictBool] = Field(default=None, description="[Read-Only] Does the system record have an Ongoing or Risk Accepted POA&M Item 120 days past its Scheduled Completion Date?", alias="hasOpenPoamItem120PlusPastScheudledCompletionDate")
    impact: Optional[StrictStr] = Field(default=None, description="[Optional] Values include the following options (Very Low, Low, Moderate,High,Very High)")
    has_cui: Optional[StrictBool] = Field(default=None, description="[Read-only] Does the system record contain and/or process Controlled Unclassified information?", alias="hasCUI")
    has_pii: Optional[StrictBool] = Field(default=None, description="[Read-only] Does the system record contain and/or process Personally Identifiable Information?", alias="hasPII")
    has_phi: Optional[StrictBool] = Field(default=None, description="[Read-only] Does the system record contain and/or process Personal Health Information?", alias="hasPHI")
    ppsm_registration_required: Optional[StrictStr] = Field(default=None, description="[Read-Only] Determine if a PPSM registration is required.", alias="ppsmRegistrationRequired")
    ppsm_registry_number: Optional[StrictStr] = Field(default=None, description="[Read-only] Unique identifier for the DoD's Ports, Protocols, and Services Management Registry system.", alias="ppsmRegistryNumber")
    ppsm_registration_exemption_justification: Optional[StrictStr] = Field(default=None, description="[Read-Only] Clarify why a PPSM registraiton is not necessary.", alias="ppsmRegistrationExemptionJustification")
    interconnected_information_system_and_identifiers: Optional[StrictStr] = Field(default=None, description="[Read-only] Identify the interconnected information systems and corresponding identifiers within control CA-3.", alias="interconnectedInformationSystemAndIdentifiers")
    is_pia_required: Optional[StrictBool] = Field(default=None, description="[Read-only] Does the system require a Privacy Impact Assessment?", alias="isPiaRequired")
    pia_status: Optional[StrictStr] = Field(default=None, description="[Read-only] Status of the PIA, availability values include the following options (Not Started, In Progress, Completed)", alias="piaStatus")
    pia_date: Optional[StrictInt] = Field(default=None, description="[Read-only] Date in which the system's PIA took place.", alias="piaDate")
    user_defined_field1: Optional[StrictStr] = Field(default=None, description="[Read-only] User-defined field to augment Ad Hoc Reporting.", alias="userDefinedField1")
    user_defined_field2: Optional[StrictStr] = Field(default=None, description="[Read-only] User-defined field to augment Ad Hoc Reporting.", alias="userDefinedField2")
    user_defined_field3: Optional[StrictStr] = Field(default=None, description="[Read-only] User-defined field to augment Ad Hoc Reporting.", alias="userDefinedField3")
    user_defined_field4: Optional[StrictStr] = Field(default=None, description="[Read-only] User-defined field to augment Ad Hoc Reporting.", alias="userDefinedField4")
    user_defined_field5: Optional[StrictStr] = Field(default=None, description="[Read-only] User-defined field to augment Ad Hoc Reporting.", alias="userDefinedField5")
    current_rmf_lifecycle_step: Optional[StrictStr] = Field(default=None, description="[Read-only] Displays the system's current step within the RMF Lifecycle.", alias="currentRmfLifecycleStep")
    other_information: Optional[StrictStr] = Field(default=None, description="[Read-only] Include any additional information required by the organization.", alias="otherInformation")
    reports_for_scorecard: Optional[StrictBool] = Field(default=None, description="[Read-only] Indicates if the system reports to the DoD Cyber Hygiene Scorecard.", alias="reportsForScorecard")
    highest_system_data_classification: Optional[StrictStr] = Field(default=None, description="[Read-Only] The overall classification level of information that the System is approved to collect, process, store, and/or distribute.", alias="highestSystemDataClassification")
    overall_classification: Optional[StrictStr] = Field(default=None, description="[Read-Only] Same field as highestSystemDataClassification, but displays as overallClassification for NISP only.", alias="overallClassification")
    is_hva: Optional[StrictBool] = Field(default=None, description="[Read-Only] Indicates if the system contains High Value Assets. Does not display if value is null", alias="isHVA")
    is_financial_management: Optional[StrictBool] = Field(default=None, description="[Read-Only] Per OMB Circular A-127, a financial management system includes the core financial systems and the financial portions  of mixed systems necessary to support financial management, including automated and manual processes, procedures, and  controls, data, hardware, software, and support personnel dedicated to the operation and maintenance of system functions. The following are examples of financial management systems: core financial systems, procurement systems, loan systems, grants systems, payroll systems, budget formulation systems, billing systems, and travel systems. ", alias="isFinancialManagement")
    is_reciprocity: Optional[StrictBool] = Field(default=None, description="[Read-Only] A reciprocity system is any information system that is part of a mutual agreement among participating organizations to accept each other's security assessments in order to reuse information system resources and/or to accept each other's assessed security posture in order to share information. ", alias="isReciprocity")
    reciprocity_exemption: Optional[StrictStr] = Field(default=None, description="[Read-Only] The following justifications are acceptable for exemption from reciprocity: (a) the existence of the system is classified (not the data, but the existence of the system) or (b) the system's authorization to operate is in the process of being pulled (e.g. DATO, Decommission). ", alias="reciprocityExemption")
    cloud_computing: Optional[StrictBool] = Field(default=None, description="[Read-Only] Is this a cloud-based IS?", alias="cloudComputing")
    cloud_type: Optional[StrictStr] = Field(default=None, description="[Read-Only] Values include the following: (Hybrid, Private, Public)", alias="cloudType")
    atc_status: Optional[StrictStr] = Field(default=None, description="[Read-Only] The Authority to Connect decision. Values include the following:  (Authority to Connect (ATC), Denial of Authority to Connect (DATC), Not Yet Connected, Decommissioned) ", alias="atcStatus")
    is_saa_s: Optional[StrictBool] = Field(default=None, description="[Read-Only] Software as a Service (SaaS) cloud service model.", alias="isSaaS")
    is_paa_s: Optional[StrictBool] = Field(default=None, description="[Read-Only] Platform as a Service (PaaS) cloud service model.", alias="isPaaS")
    is_iaa_s: Optional[StrictBool] = Field(default=None, description="[Read-Only] Infrastructure as a Service (IaaS) cloud service model.", alias="isIaaS")
    other_service_models: Optional[StrictStr] = Field(default=None, description="[Read-Only] Free text field to include other cloud service models.", alias="otherServiceModels")
    need_date: Optional[StrictInt] = Field(default=None, description="[Read-Only] Indicates the date by which the System needs to be deployed to a production environment.", alias="needDate")
    overall_risk_score: Optional[StrictStr] = Field(default=None, description="[Read-Only] The overall risk score of the system", alias="overallRiskScore")
    is_hrr: Optional[StrictBool] = Field(default=None, description="[Read-Only] Identifies whether a System has been designated as High Risk Review. USCG and Navy only.", alias="isHRR")
    atc_date: Optional[StrictInt] = Field(default=None, description="[Read-Only] The Connectivity Authorization Date.", alias="atcDate")
    atc_termination_date: Optional[StrictInt] = Field(default=None, description="[Read-Only] The Connectivity Authorization Termination Date.", alias="atcTerminationDate")
    system_development_life_cycle: Optional[StrictStr] = Field(default=None, description="[Read-Only] Indicate the date by which the System needs to be deployed to a production environment. VA only.", alias="systemDevelopmentLifeCycle")
    is_fisma_reportable: Optional[StrictBool] = Field(default=None, description="[Read-Only] Is this IS reportable per Federal Information Security Management Act (FISMA) established requirements? VA only", alias="isFISMAReportable")
    group_tagging: Optional[StrictStr] = Field(default=None, description="[Read-Only] System Tags for enterprise level, to include CIO and CISO, tracking efforts. VA only.", alias="groupTagging")
    group_tag_descriptions: Optional[StrictStr] = Field(default=None, description="[Read-Only] System Tag explanation(s) for enterprise level, to include CIO and CISO, tracking efforts. VA only.", alias="groupTagDescriptions")
    dadms_id: Optional[StrictStr] = Field(default=None, description="[Read-Only] The system's DADMS ID. USMC only.", alias="dadmsId")
    dadms_expiration_date: Optional[StrictInt] = Field(default=None, description="[Read-Only] Date the system expires in DADMS. USMC only.", alias="dadmsExpirationDate")
    enclave_connectivity: Optional[StrictStr] = Field(default=None, description="[Read-Only] Identify the type of connectivity for the network/enclave, e.g., DISA circuit (NIPR, SIPR) or HPCMP circuit (DREN, SDREN, Outreach). Navy only.", alias="enclaveConnectivity")
    environment_type: Optional[StrictStr] = Field(default=None, description="[Read-Only] Identify the primary computing environment for where the information system is deployed. Navy only.", alias="environmentType")
    navy_common_control_provider: Optional[StrictBool] = Field(default=None, description="[Read-Only] Indicate whether the information system provides inheritable controls. Navy only", alias="navyCommonControlProvider")
    navy_cloud_broker: Optional[StrictStr] = Field(default=None, description="[Read-Only] Identify the broker responsible for the delivery of commercial cloud services and capabilities. Refer to Navy Commercial Cloud Brokerage Policy. Navy Only", alias="navyCloudBroker")
    cloud_broker_emass_id: Optional[StrictInt] = Field(default=None, description="[Read-Only] The eMASS ID of the identified cloud broker. Navy only.", alias="cloudBrokerEmassId")
    cloud_broker_provisional_authorization_atd: Optional[StrictInt] = Field(default=None, description="[Read-Only] The provisional authorization termination date of the identified cloud broker. Navy only", alias="cloudBrokerProvisionalAuthorizationAtd")
    navy_joint_authorization: Optional[StrictBool] = Field(default=None, description="[Read-Only] Indicate whether this is a joint authorization being issued by two or more Authorizing Officials. Navy only", alias="navyJointAuthorization")
    nmci_ngen_clins: Optional[StrictStr] = Field(default=None, description="[Read-Only] Provide all NMCI CLINs associated to the system/services within the authorization boundary. Navy only", alias="nmciNgenClins")
    enterprise_locations: Optional[StrictStr] = Field(default=None, description="[Read-Only] Identify the Navy enterprise network where the information system is deployed. Navy only", alias="enterpriseLocations")
    whitelist_id: Optional[StrictStr] = Field(default=None, description="[Read-Only] Systems that have public-facing components/presences are typically required to be documented and registered as part of Organzationally-approved whitelisting processes.", alias="whitelistId")
    whitelist_inventory: Optional[StrictStr] = Field(default=None, description="[Read-Only] Provide/upload the documentation that identifies or describes the components or aspects of the System that are public-facing (whitelisted).", alias="whitelistInventory")
    cybersecurity_service_provider: Optional[StrictStr] = Field(default=None, description="[Read-Only] Name of the system's Cybersecurity Service Provider.", alias="cybersecurityServiceProvider")
    cybersecurity_service_provider_exception_justification: Optional[StrictStr] = Field(default=None, description="[Read-Only] If Not Applicable, provide the exception justification.", alias="cybersecurityServiceProviderExceptionJustification")
    package: Optional[List[PacGet]] = None
    connectivity_ccsd: Optional[List[ConnectivityCcsd]] = Field(default=None, alias="connectivityCcsd")
    __properties: ClassVar[List[str]] = ["registrationCompletionDate", "systemLifeCycleAcquisitionPhase", "specialType", "specialTypeDescription", "missionPortfolio", "isNNPI", "isRBC", "isWaiver", "programOffice", "vramId", "systemId", "policy", "registrationType", "name", "acronym", "description", "instance", "owningOrganization", "secondaryOrganization", "versionReleaseNo", "systemType", "isNSS", "isPublicFacing", "coamsId", "isTypeAuthorization", "ditprId", "apmsId", "vasiId", "authorizationStatus", "authorizationDate", "authorizationTerminationDate", "authorizationLength", "termsForAuth", "securityPlanApprovalStatus", "securityPlanApprovalDate", "missionCriticality", "geographicalAssociation", "systemOwnership", "governingMissionArea", "primaryFunctionalArea", "secondaryFunctionalArea", "primaryControlSet", "confidentiality", "integrity", "availability", "appliedOverlays", "rmfActivity", "crossDomainTicket", "ditprDonId", "mac", "dodConfidentiality", "contingencyPlanTested", "contingencyPlanTestDate", "securityReviewRequired", "securityReviewCompleted", "securityReviewCompletionDate", "nextSecurityReviewDueDate", "hasOpenPoamItem", "hasOpenPoamItem90to120PastScheduledCompletionDate", "hasOpenPoamItem120PlusPastScheudledCompletionDate", "impact", "hasCUI", "hasPII", "hasPHI", "ppsmRegistrationRequired", "ppsmRegistryNumber", "ppsmRegistrationExemptionJustification", "interconnectedInformationSystemAndIdentifiers", "isPiaRequired", "piaStatus", "piaDate", "userDefinedField1", "userDefinedField2", "userDefinedField3", "userDefinedField4", "userDefinedField5", "currentRmfLifecycleStep", "otherInformation", "reportsForScorecard", "highestSystemDataClassification", "overallClassification", "isHVA", "isFinancialManagement", "isReciprocity", "reciprocityExemption", "cloudComputing", "cloudType", "atcStatus", "isSaaS", "isPaaS", "isIaaS", "otherServiceModels", "needDate", "overallRiskScore", "isHRR", "atcDate", "atcTerminationDate", "systemDevelopmentLifeCycle", "isFISMAReportable", "groupTagging", "groupTagDescriptions", "dadmsId", "dadmsExpirationDate", "enclaveConnectivity", "environmentType", "navyCommonControlProvider", "navyCloudBroker", "cloudBrokerEmassId", "cloudBrokerProvisionalAuthorizationAtd", "navyJointAuthorization", "nmciNgenClins", "enterpriseLocations", "whitelistId", "whitelistInventory", "cybersecurityServiceProvider", "cybersecurityServiceProviderExceptionJustification", "package", "connectivityCcsd"]

    @field_validator('policy')
    def policy_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('RMF', 'DIACAP'):
            raise ValueError("must be one of enum values ('RMF', 'DIACAP')")
        return value

    @field_validator('registration_type')
    def registration_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Assess and Authorize', 'Assess Only', 'Guest', 'Regular', 'Functional', 'Cloud Service Provider'):
            raise ValueError("must be one of enum values ('Assess and Authorize', 'Assess Only', 'Guest', 'Regular', 'Functional', 'Cloud Service Provider')")
        return value

    @field_validator('system_type')
    def system_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('IS Major Application', 'IS Enclave', 'Platform IT', 'Platform IT System', 'Platform IT Interconnection', 'AIS Application', 'Outsourced IT-Based Process (DoD-controlled)', 'Enclave', 'Outsourced IT-Based Process (service provider shared)'):
            raise ValueError("must be one of enum values ('IS Major Application', 'IS Enclave', 'Platform IT', 'Platform IT System', 'Platform IT Interconnection', 'AIS Application', 'Outsourced IT-Based Process (DoD-controlled)', 'Enclave', 'Outsourced IT-Based Process (service provider shared)')")
        return value

    @field_validator('security_plan_approval_status')
    def security_plan_approval_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Approved', 'Not Yet Approved', 'Denied'):
            raise ValueError("must be one of enum values ('Approved', 'Not Yet Approved', 'Denied')")
        return value

    @field_validator('primary_control_set')
    def primary_control_set_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('NIST SP 800-53 Revision 4', 'DoDI 8500.2'):
            raise ValueError("must be one of enum values ('NIST SP 800-53 Revision 4', 'DoDI 8500.2')")
        return value

    @field_validator('confidentiality')
    def confidentiality_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('High', 'Moderate', 'Low'):
            raise ValueError("must be one of enum values ('High', 'Moderate', 'Low')")
        return value

    @field_validator('integrity')
    def integrity_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('High', 'Moderate', 'Low'):
            raise ValueError("must be one of enum values ('High', 'Moderate', 'Low')")
        return value

    @field_validator('availability')
    def availability_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('High', 'Moderate', 'Low'):
            raise ValueError("must be one of enum values ('High', 'Moderate', 'Low')")
        return value

    @field_validator('mac')
    def mac_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('I', 'II', 'III'):
            raise ValueError("must be one of enum values ('I', 'II', 'III')")
        return value

    @field_validator('dod_confidentiality')
    def dod_confidentiality_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Public', 'Sensitive', 'Classified'):
            raise ValueError("must be one of enum values ('Public', 'Sensitive', 'Classified')")
        return value

    @field_validator('impact')
    def impact_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Low', 'Moderate', 'High'):
            raise ValueError("must be one of enum values ('Low', 'Moderate', 'High')")
        return value

    @field_validator('pia_status')
    def pia_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Not Started', 'In Progress', 'Completed'):
            raise ValueError("must be one of enum values ('Not Started', 'In Progress', 'Completed')")
        return value

    @field_validator('current_rmf_lifecycle_step')
    def current_rmf_lifecycle_step_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('1 - Categorize', '2 - Select', '3 - Implement', '4 - Assess', '5 - Authorize', '6 - Monitor'):
            raise ValueError("must be one of enum values ('1 - Categorize', '2 - Select', '3 - Implement', '4 - Assess', '5 - Authorize', '6 - Monitor')")
        return value

    @field_validator('cloud_type')
    def cloud_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Hybrid', 'Private', 'Public'):
            raise ValueError("must be one of enum values ('Hybrid', 'Private', 'Public')")
        return value

    @field_validator('atc_status')
    def atc_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Authority to Connect (ATC)', 'Denial of Authority to Connect (DATC)', 'Not Yet Connected', 'Decommissioned'):
            raise ValueError("must be one of enum values ('Authority to Connect (ATC)', 'Denial of Authority to Connect (DATC)', 'Not Yet Connected', 'Decommissioned')")
        return value

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of Systems from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in package (list)
        _items = []
        if self.package:
            for _item in self.package:
                if _item:
                    _items.append(_item.to_dict())
            _dict['package'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in connectivity_ccsd (list)
        _items = []
        if self.connectivity_ccsd:
            for _item in self.connectivity_ccsd:
                if _item:
                    _items.append(_item.to_dict())
            _dict['connectivityCcsd'] = _items
        # set to None if registration_completion_date (nullable) is None
        # and model_fields_set contains the field
        if self.registration_completion_date is None and "registration_completion_date" in self.model_fields_set:
            _dict['registrationCompletionDate'] = None

        # set to None if system_life_cycle_acquisition_phase (nullable) is None
        # and model_fields_set contains the field
        if self.system_life_cycle_acquisition_phase is None and "system_life_cycle_acquisition_phase" in self.model_fields_set:
            _dict['systemLifeCycleAcquisitionPhase'] = None

        # set to None if special_type (nullable) is None
        # and model_fields_set contains the field
        if self.special_type is None and "special_type" in self.model_fields_set:
            _dict['specialType'] = None

        # set to None if special_type_description (nullable) is None
        # and model_fields_set contains the field
        if self.special_type_description is None and "special_type_description" in self.model_fields_set:
            _dict['specialTypeDescription'] = None

        # set to None if mission_portfolio (nullable) is None
        # and model_fields_set contains the field
        if self.mission_portfolio is None and "mission_portfolio" in self.model_fields_set:
            _dict['missionPortfolio'] = None

        # set to None if is_nnpi (nullable) is None
        # and model_fields_set contains the field
        if self.is_nnpi is None and "is_nnpi" in self.model_fields_set:
            _dict['isNNPI'] = None

        # set to None if is_rbc (nullable) is None
        # and model_fields_set contains the field
        if self.is_rbc is None and "is_rbc" in self.model_fields_set:
            _dict['isRBC'] = None

        # set to None if is_waiver (nullable) is None
        # and model_fields_set contains the field
        if self.is_waiver is None and "is_waiver" in self.model_fields_set:
            _dict['isWaiver'] = None

        # set to None if program_office (nullable) is None
        # and model_fields_set contains the field
        if self.program_office is None and "program_office" in self.model_fields_set:
            _dict['programOffice'] = None

        # set to None if vram_id (nullable) is None
        # and model_fields_set contains the field
        if self.vram_id is None and "vram_id" in self.model_fields_set:
            _dict['vramId'] = None

        # set to None if policy (nullable) is None
        # and model_fields_set contains the field
        if self.policy is None and "policy" in self.model_fields_set:
            _dict['policy'] = None

        # set to None if registration_type (nullable) is None
        # and model_fields_set contains the field
        if self.registration_type is None and "registration_type" in self.model_fields_set:
            _dict['registrationType'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if acronym (nullable) is None
        # and model_fields_set contains the field
        if self.acronym is None and "acronym" in self.model_fields_set:
            _dict['acronym'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if instance (nullable) is None
        # and model_fields_set contains the field
        if self.instance is None and "instance" in self.model_fields_set:
            _dict['instance'] = None

        # set to None if owning_organization (nullable) is None
        # and model_fields_set contains the field
        if self.owning_organization is None and "owning_organization" in self.model_fields_set:
            _dict['owningOrganization'] = None

        # set to None if secondary_organization (nullable) is None
        # and model_fields_set contains the field
        if self.secondary_organization is None and "secondary_organization" in self.model_fields_set:
            _dict['secondaryOrganization'] = None

        # set to None if version_release_no (nullable) is None
        # and model_fields_set contains the field
        if self.version_release_no is None and "version_release_no" in self.model_fields_set:
            _dict['versionReleaseNo'] = None

        # set to None if system_type (nullable) is None
        # and model_fields_set contains the field
        if self.system_type is None and "system_type" in self.model_fields_set:
            _dict['systemType'] = None

        # set to None if is_nss (nullable) is None
        # and model_fields_set contains the field
        if self.is_nss is None and "is_nss" in self.model_fields_set:
            _dict['isNSS'] = None

        # set to None if is_public_facing (nullable) is None
        # and model_fields_set contains the field
        if self.is_public_facing is None and "is_public_facing" in self.model_fields_set:
            _dict['isPublicFacing'] = None

        # set to None if coams_id (nullable) is None
        # and model_fields_set contains the field
        if self.coams_id is None and "coams_id" in self.model_fields_set:
            _dict['coamsId'] = None

        # set to None if is_type_authorization (nullable) is None
        # and model_fields_set contains the field
        if self.is_type_authorization is None and "is_type_authorization" in self.model_fields_set:
            _dict['isTypeAuthorization'] = None

        # set to None if apms_id (nullable) is None
        # and model_fields_set contains the field
        if self.apms_id is None and "apms_id" in self.model_fields_set:
            _dict['apmsId'] = None

        # set to None if vasi_id (nullable) is None
        # and model_fields_set contains the field
        if self.vasi_id is None and "vasi_id" in self.model_fields_set:
            _dict['vasiId'] = None

        # set to None if authorization_status (nullable) is None
        # and model_fields_set contains the field
        if self.authorization_status is None and "authorization_status" in self.model_fields_set:
            _dict['authorizationStatus'] = None

        # set to None if authorization_date (nullable) is None
        # and model_fields_set contains the field
        if self.authorization_date is None and "authorization_date" in self.model_fields_set:
            _dict['authorizationDate'] = None

        # set to None if authorization_termination_date (nullable) is None
        # and model_fields_set contains the field
        if self.authorization_termination_date is None and "authorization_termination_date" in self.model_fields_set:
            _dict['authorizationTerminationDate'] = None

        # set to None if authorization_length (nullable) is None
        # and model_fields_set contains the field
        if self.authorization_length is None and "authorization_length" in self.model_fields_set:
            _dict['authorizationLength'] = None

        # set to None if terms_for_auth (nullable) is None
        # and model_fields_set contains the field
        if self.terms_for_auth is None and "terms_for_auth" in self.model_fields_set:
            _dict['termsForAuth'] = None

        # set to None if security_plan_approval_status (nullable) is None
        # and model_fields_set contains the field
        if self.security_plan_approval_status is None and "security_plan_approval_status" in self.model_fields_set:
            _dict['securityPlanApprovalStatus'] = None

        # set to None if security_plan_approval_date (nullable) is None
        # and model_fields_set contains the field
        if self.security_plan_approval_date is None and "security_plan_approval_date" in self.model_fields_set:
            _dict['securityPlanApprovalDate'] = None

        # set to None if mission_criticality (nullable) is None
        # and model_fields_set contains the field
        if self.mission_criticality is None and "mission_criticality" in self.model_fields_set:
            _dict['missionCriticality'] = None

        # set to None if geographical_association (nullable) is None
        # and model_fields_set contains the field
        if self.geographical_association is None and "geographical_association" in self.model_fields_set:
            _dict['geographicalAssociation'] = None

        # set to None if system_ownership (nullable) is None
        # and model_fields_set contains the field
        if self.system_ownership is None and "system_ownership" in self.model_fields_set:
            _dict['systemOwnership'] = None

        # set to None if governing_mission_area (nullable) is None
        # and model_fields_set contains the field
        if self.governing_mission_area is None and "governing_mission_area" in self.model_fields_set:
            _dict['governingMissionArea'] = None

        # set to None if primary_functional_area (nullable) is None
        # and model_fields_set contains the field
        if self.primary_functional_area is None and "primary_functional_area" in self.model_fields_set:
            _dict['primaryFunctionalArea'] = None

        # set to None if secondary_functional_area (nullable) is None
        # and model_fields_set contains the field
        if self.secondary_functional_area is None and "secondary_functional_area" in self.model_fields_set:
            _dict['secondaryFunctionalArea'] = None

        # set to None if primary_control_set (nullable) is None
        # and model_fields_set contains the field
        if self.primary_control_set is None and "primary_control_set" in self.model_fields_set:
            _dict['primaryControlSet'] = None

        # set to None if confidentiality (nullable) is None
        # and model_fields_set contains the field
        if self.confidentiality is None and "confidentiality" in self.model_fields_set:
            _dict['confidentiality'] = None

        # set to None if integrity (nullable) is None
        # and model_fields_set contains the field
        if self.integrity is None and "integrity" in self.model_fields_set:
            _dict['integrity'] = None

        # set to None if availability (nullable) is None
        # and model_fields_set contains the field
        if self.availability is None and "availability" in self.model_fields_set:
            _dict['availability'] = None

        # set to None if applied_overlays (nullable) is None
        # and model_fields_set contains the field
        if self.applied_overlays is None and "applied_overlays" in self.model_fields_set:
            _dict['appliedOverlays'] = None

        # set to None if rmf_activity (nullable) is None
        # and model_fields_set contains the field
        if self.rmf_activity is None and "rmf_activity" in self.model_fields_set:
            _dict['rmfActivity'] = None

        # set to None if cross_domain_ticket (nullable) is None
        # and model_fields_set contains the field
        if self.cross_domain_ticket is None and "cross_domain_ticket" in self.model_fields_set:
            _dict['crossDomainTicket'] = None

        # set to None if ditpr_don_id (nullable) is None
        # and model_fields_set contains the field
        if self.ditpr_don_id is None and "ditpr_don_id" in self.model_fields_set:
            _dict['ditprDonId'] = None

        # set to None if mac (nullable) is None
        # and model_fields_set contains the field
        if self.mac is None and "mac" in self.model_fields_set:
            _dict['mac'] = None

        # set to None if dod_confidentiality (nullable) is None
        # and model_fields_set contains the field
        if self.dod_confidentiality is None and "dod_confidentiality" in self.model_fields_set:
            _dict['dodConfidentiality'] = None

        # set to None if contingency_plan_tested (nullable) is None
        # and model_fields_set contains the field
        if self.contingency_plan_tested is None and "contingency_plan_tested" in self.model_fields_set:
            _dict['contingencyPlanTested'] = None

        # set to None if contingency_plan_test_date (nullable) is None
        # and model_fields_set contains the field
        if self.contingency_plan_test_date is None and "contingency_plan_test_date" in self.model_fields_set:
            _dict['contingencyPlanTestDate'] = None

        # set to None if security_review_required (nullable) is None
        # and model_fields_set contains the field
        if self.security_review_required is None and "security_review_required" in self.model_fields_set:
            _dict['securityReviewRequired'] = None

        # set to None if security_review_completed (nullable) is None
        # and model_fields_set contains the field
        if self.security_review_completed is None and "security_review_completed" in self.model_fields_set:
            _dict['securityReviewCompleted'] = None

        # set to None if security_review_completion_date (nullable) is None
        # and model_fields_set contains the field
        if self.security_review_completion_date is None and "security_review_completion_date" in self.model_fields_set:
            _dict['securityReviewCompletionDate'] = None

        # set to None if next_security_review_due_date (nullable) is None
        # and model_fields_set contains the field
        if self.next_security_review_due_date is None and "next_security_review_due_date" in self.model_fields_set:
            _dict['nextSecurityReviewDueDate'] = None

        # set to None if has_open_poam_item (nullable) is None
        # and model_fields_set contains the field
        if self.has_open_poam_item is None and "has_open_poam_item" in self.model_fields_set:
            _dict['hasOpenPoamItem'] = None

        # set to None if has_open_poam_item90to120_past_scheduled_completion_date (nullable) is None
        # and model_fields_set contains the field
        if self.has_open_poam_item90to120_past_scheduled_completion_date is None and "has_open_poam_item90to120_past_scheduled_completion_date" in self.model_fields_set:
            _dict['hasOpenPoamItem90to120PastScheduledCompletionDate'] = None

        # set to None if has_open_poam_item120_plus_past_scheudled_completion_date (nullable) is None
        # and model_fields_set contains the field
        if self.has_open_poam_item120_plus_past_scheudled_completion_date is None and "has_open_poam_item120_plus_past_scheudled_completion_date" in self.model_fields_set:
            _dict['hasOpenPoamItem120PlusPastScheudledCompletionDate'] = None

        # set to None if impact (nullable) is None
        # and model_fields_set contains the field
        if self.impact is None and "impact" in self.model_fields_set:
            _dict['impact'] = None

        # set to None if has_cui (nullable) is None
        # and model_fields_set contains the field
        if self.has_cui is None and "has_cui" in self.model_fields_set:
            _dict['hasCUI'] = None

        # set to None if has_pii (nullable) is None
        # and model_fields_set contains the field
        if self.has_pii is None and "has_pii" in self.model_fields_set:
            _dict['hasPII'] = None

        # set to None if has_phi (nullable) is None
        # and model_fields_set contains the field
        if self.has_phi is None and "has_phi" in self.model_fields_set:
            _dict['hasPHI'] = None

        # set to None if ppsm_registration_required (nullable) is None
        # and model_fields_set contains the field
        if self.ppsm_registration_required is None and "ppsm_registration_required" in self.model_fields_set:
            _dict['ppsmRegistrationRequired'] = None

        # set to None if ppsm_registry_number (nullable) is None
        # and model_fields_set contains the field
        if self.ppsm_registry_number is None and "ppsm_registry_number" in self.model_fields_set:
            _dict['ppsmRegistryNumber'] = None

        # set to None if ppsm_registration_exemption_justification (nullable) is None
        # and model_fields_set contains the field
        if self.ppsm_registration_exemption_justification is None and "ppsm_registration_exemption_justification" in self.model_fields_set:
            _dict['ppsmRegistrationExemptionJustification'] = None

        # set to None if interconnected_information_system_and_identifiers (nullable) is None
        # and model_fields_set contains the field
        if self.interconnected_information_system_and_identifiers is None and "interconnected_information_system_and_identifiers" in self.model_fields_set:
            _dict['interconnectedInformationSystemAndIdentifiers'] = None

        # set to None if is_pia_required (nullable) is None
        # and model_fields_set contains the field
        if self.is_pia_required is None and "is_pia_required" in self.model_fields_set:
            _dict['isPiaRequired'] = None

        # set to None if pia_status (nullable) is None
        # and model_fields_set contains the field
        if self.pia_status is None and "pia_status" in self.model_fields_set:
            _dict['piaStatus'] = None

        # set to None if pia_date (nullable) is None
        # and model_fields_set contains the field
        if self.pia_date is None and "pia_date" in self.model_fields_set:
            _dict['piaDate'] = None

        # set to None if user_defined_field1 (nullable) is None
        # and model_fields_set contains the field
        if self.user_defined_field1 is None and "user_defined_field1" in self.model_fields_set:
            _dict['userDefinedField1'] = None

        # set to None if user_defined_field2 (nullable) is None
        # and model_fields_set contains the field
        if self.user_defined_field2 is None and "user_defined_field2" in self.model_fields_set:
            _dict['userDefinedField2'] = None

        # set to None if user_defined_field3 (nullable) is None
        # and model_fields_set contains the field
        if self.user_defined_field3 is None and "user_defined_field3" in self.model_fields_set:
            _dict['userDefinedField3'] = None

        # set to None if user_defined_field4 (nullable) is None
        # and model_fields_set contains the field
        if self.user_defined_field4 is None and "user_defined_field4" in self.model_fields_set:
            _dict['userDefinedField4'] = None

        # set to None if user_defined_field5 (nullable) is None
        # and model_fields_set contains the field
        if self.user_defined_field5 is None and "user_defined_field5" in self.model_fields_set:
            _dict['userDefinedField5'] = None

        # set to None if current_rmf_lifecycle_step (nullable) is None
        # and model_fields_set contains the field
        if self.current_rmf_lifecycle_step is None and "current_rmf_lifecycle_step" in self.model_fields_set:
            _dict['currentRmfLifecycleStep'] = None

        # set to None if other_information (nullable) is None
        # and model_fields_set contains the field
        if self.other_information is None and "other_information" in self.model_fields_set:
            _dict['otherInformation'] = None

        # set to None if reports_for_scorecard (nullable) is None
        # and model_fields_set contains the field
        if self.reports_for_scorecard is None and "reports_for_scorecard" in self.model_fields_set:
            _dict['reportsForScorecard'] = None

        # set to None if highest_system_data_classification (nullable) is None
        # and model_fields_set contains the field
        if self.highest_system_data_classification is None and "highest_system_data_classification" in self.model_fields_set:
            _dict['highestSystemDataClassification'] = None

        # set to None if overall_classification (nullable) is None
        # and model_fields_set contains the field
        if self.overall_classification is None and "overall_classification" in self.model_fields_set:
            _dict['overallClassification'] = None

        # set to None if is_hva (nullable) is None
        # and model_fields_set contains the field
        if self.is_hva is None and "is_hva" in self.model_fields_set:
            _dict['isHVA'] = None

        # set to None if is_financial_management (nullable) is None
        # and model_fields_set contains the field
        if self.is_financial_management is None and "is_financial_management" in self.model_fields_set:
            _dict['isFinancialManagement'] = None

        # set to None if is_reciprocity (nullable) is None
        # and model_fields_set contains the field
        if self.is_reciprocity is None and "is_reciprocity" in self.model_fields_set:
            _dict['isReciprocity'] = None

        # set to None if reciprocity_exemption (nullable) is None
        # and model_fields_set contains the field
        if self.reciprocity_exemption is None and "reciprocity_exemption" in self.model_fields_set:
            _dict['reciprocityExemption'] = None

        # set to None if cloud_computing (nullable) is None
        # and model_fields_set contains the field
        if self.cloud_computing is None and "cloud_computing" in self.model_fields_set:
            _dict['cloudComputing'] = None

        # set to None if cloud_type (nullable) is None
        # and model_fields_set contains the field
        if self.cloud_type is None and "cloud_type" in self.model_fields_set:
            _dict['cloudType'] = None

        # set to None if atc_status (nullable) is None
        # and model_fields_set contains the field
        if self.atc_status is None and "atc_status" in self.model_fields_set:
            _dict['atcStatus'] = None

        # set to None if is_saa_s (nullable) is None
        # and model_fields_set contains the field
        if self.is_saa_s is None and "is_saa_s" in self.model_fields_set:
            _dict['isSaaS'] = None

        # set to None if is_paa_s (nullable) is None
        # and model_fields_set contains the field
        if self.is_paa_s is None and "is_paa_s" in self.model_fields_set:
            _dict['isPaaS'] = None

        # set to None if is_iaa_s (nullable) is None
        # and model_fields_set contains the field
        if self.is_iaa_s is None and "is_iaa_s" in self.model_fields_set:
            _dict['isIaaS'] = None

        # set to None if other_service_models (nullable) is None
        # and model_fields_set contains the field
        if self.other_service_models is None and "other_service_models" in self.model_fields_set:
            _dict['otherServiceModels'] = None

        # set to None if need_date (nullable) is None
        # and model_fields_set contains the field
        if self.need_date is None and "need_date" in self.model_fields_set:
            _dict['needDate'] = None

        # set to None if overall_risk_score (nullable) is None
        # and model_fields_set contains the field
        if self.overall_risk_score is None and "overall_risk_score" in self.model_fields_set:
            _dict['overallRiskScore'] = None

        # set to None if is_hrr (nullable) is None
        # and model_fields_set contains the field
        if self.is_hrr is None and "is_hrr" in self.model_fields_set:
            _dict['isHRR'] = None

        # set to None if atc_date (nullable) is None
        # and model_fields_set contains the field
        if self.atc_date is None and "atc_date" in self.model_fields_set:
            _dict['atcDate'] = None

        # set to None if atc_termination_date (nullable) is None
        # and model_fields_set contains the field
        if self.atc_termination_date is None and "atc_termination_date" in self.model_fields_set:
            _dict['atcTerminationDate'] = None

        # set to None if system_development_life_cycle (nullable) is None
        # and model_fields_set contains the field
        if self.system_development_life_cycle is None and "system_development_life_cycle" in self.model_fields_set:
            _dict['systemDevelopmentLifeCycle'] = None

        # set to None if is_fisma_reportable (nullable) is None
        # and model_fields_set contains the field
        if self.is_fisma_reportable is None and "is_fisma_reportable" in self.model_fields_set:
            _dict['isFISMAReportable'] = None

        # set to None if group_tagging (nullable) is None
        # and model_fields_set contains the field
        if self.group_tagging is None and "group_tagging" in self.model_fields_set:
            _dict['groupTagging'] = None

        # set to None if group_tag_descriptions (nullable) is None
        # and model_fields_set contains the field
        if self.group_tag_descriptions is None and "group_tag_descriptions" in self.model_fields_set:
            _dict['groupTagDescriptions'] = None

        # set to None if dadms_id (nullable) is None
        # and model_fields_set contains the field
        if self.dadms_id is None and "dadms_id" in self.model_fields_set:
            _dict['dadmsId'] = None

        # set to None if dadms_expiration_date (nullable) is None
        # and model_fields_set contains the field
        if self.dadms_expiration_date is None and "dadms_expiration_date" in self.model_fields_set:
            _dict['dadmsExpirationDate'] = None

        # set to None if enclave_connectivity (nullable) is None
        # and model_fields_set contains the field
        if self.enclave_connectivity is None and "enclave_connectivity" in self.model_fields_set:
            _dict['enclaveConnectivity'] = None

        # set to None if environment_type (nullable) is None
        # and model_fields_set contains the field
        if self.environment_type is None and "environment_type" in self.model_fields_set:
            _dict['environmentType'] = None

        # set to None if navy_common_control_provider (nullable) is None
        # and model_fields_set contains the field
        if self.navy_common_control_provider is None and "navy_common_control_provider" in self.model_fields_set:
            _dict['navyCommonControlProvider'] = None

        # set to None if navy_cloud_broker (nullable) is None
        # and model_fields_set contains the field
        if self.navy_cloud_broker is None and "navy_cloud_broker" in self.model_fields_set:
            _dict['navyCloudBroker'] = None

        # set to None if cloud_broker_emass_id (nullable) is None
        # and model_fields_set contains the field
        if self.cloud_broker_emass_id is None and "cloud_broker_emass_id" in self.model_fields_set:
            _dict['cloudBrokerEmassId'] = None

        # set to None if cloud_broker_provisional_authorization_atd (nullable) is None
        # and model_fields_set contains the field
        if self.cloud_broker_provisional_authorization_atd is None and "cloud_broker_provisional_authorization_atd" in self.model_fields_set:
            _dict['cloudBrokerProvisionalAuthorizationAtd'] = None

        # set to None if navy_joint_authorization (nullable) is None
        # and model_fields_set contains the field
        if self.navy_joint_authorization is None and "navy_joint_authorization" in self.model_fields_set:
            _dict['navyJointAuthorization'] = None

        # set to None if nmci_ngen_clins (nullable) is None
        # and model_fields_set contains the field
        if self.nmci_ngen_clins is None and "nmci_ngen_clins" in self.model_fields_set:
            _dict['nmciNgenClins'] = None

        # set to None if enterprise_locations (nullable) is None
        # and model_fields_set contains the field
        if self.enterprise_locations is None and "enterprise_locations" in self.model_fields_set:
            _dict['enterpriseLocations'] = None

        # set to None if whitelist_id (nullable) is None
        # and model_fields_set contains the field
        if self.whitelist_id is None and "whitelist_id" in self.model_fields_set:
            _dict['whitelistId'] = None

        # set to None if whitelist_inventory (nullable) is None
        # and model_fields_set contains the field
        if self.whitelist_inventory is None and "whitelist_inventory" in self.model_fields_set:
            _dict['whitelistInventory'] = None

        # set to None if cybersecurity_service_provider (nullable) is None
        # and model_fields_set contains the field
        if self.cybersecurity_service_provider is None and "cybersecurity_service_provider" in self.model_fields_set:
            _dict['cybersecurityServiceProvider'] = None

        # set to None if cybersecurity_service_provider_exception_justification (nullable) is None
        # and model_fields_set contains the field
        if self.cybersecurity_service_provider_exception_justification is None and "cybersecurity_service_provider_exception_justification" in self.model_fields_set:
            _dict['cybersecurityServiceProviderExceptionJustification'] = None

        # set to None if package (nullable) is None
        # and model_fields_set contains the field
        if self.package is None and "package" in self.model_fields_set:
            _dict['package'] = None

        # set to None if connectivity_ccsd (nullable) is None
        # and model_fields_set contains the field
        if self.connectivity_ccsd is None and "connectivity_ccsd" in self.model_fields_set:
            _dict['connectivityCcsd'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        """Create an instance of Systems from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "registrationCompletionDate": obj.get("registrationCompletionDate"),
            "systemLifeCycleAcquisitionPhase": obj.get("systemLifeCycleAcquisitionPhase"),
            "specialType": obj.get("specialType"),
            "specialTypeDescription": obj.get("specialTypeDescription"),
            "missionPortfolio": obj.get("missionPortfolio"),
            "isNNPI": obj.get("isNNPI"),
            "isRBC": obj.get("isRBC"),
            "isWaiver": obj.get("isWaiver"),
            "programOffice": obj.get("programOffice"),
            "vramId": obj.get("vramId"),
            "systemId": obj.get("systemId"),
            "policy": obj.get("policy"),
            "registrationType": obj.get("registrationType"),
            "name": obj.get("name"),
            "acronym": obj.get("acronym"),
            "description": obj.get("description"),
            "instance": obj.get("instance"),
            "owningOrganization": obj.get("owningOrganization"),
            "secondaryOrganization": obj.get("secondaryOrganization"),
            "versionReleaseNo": obj.get("versionReleaseNo"),
            "systemType": obj.get("systemType"),
            "isNSS": obj.get("isNSS"),
            "isPublicFacing": obj.get("isPublicFacing"),
            "coamsId": obj.get("coamsId"),
            "isTypeAuthorization": obj.get("isTypeAuthorization"),
            "ditprId": obj.get("ditprId"),
            "apmsId": obj.get("apmsId"),
            "vasiId": obj.get("vasiId"),
            "authorizationStatus": obj.get("authorizationStatus"),
            "authorizationDate": obj.get("authorizationDate"),
            "authorizationTerminationDate": obj.get("authorizationTerminationDate"),
            "authorizationLength": obj.get("authorizationLength"),
            "termsForAuth": obj.get("termsForAuth"),
            "securityPlanApprovalStatus": obj.get("securityPlanApprovalStatus"),
            "securityPlanApprovalDate": obj.get("securityPlanApprovalDate"),
            "missionCriticality": obj.get("missionCriticality"),
            "geographicalAssociation": obj.get("geographicalAssociation"),
            "systemOwnership": obj.get("systemOwnership"),
            "governingMissionArea": obj.get("governingMissionArea"),
            "primaryFunctionalArea": obj.get("primaryFunctionalArea"),
            "secondaryFunctionalArea": obj.get("secondaryFunctionalArea"),
            "primaryControlSet": obj.get("primaryControlSet"),
            "confidentiality": obj.get("confidentiality"),
            "integrity": obj.get("integrity"),
            "availability": obj.get("availability"),
            "appliedOverlays": obj.get("appliedOverlays"),
            "rmfActivity": obj.get("rmfActivity"),
            "crossDomainTicket": obj.get("crossDomainTicket"),
            "ditprDonId": obj.get("ditprDonId"),
            "mac": obj.get("mac"),
            "dodConfidentiality": obj.get("dodConfidentiality"),
            "contingencyPlanTested": obj.get("contingencyPlanTested"),
            "contingencyPlanTestDate": obj.get("contingencyPlanTestDate"),
            "securityReviewRequired": obj.get("securityReviewRequired"),
            "securityReviewCompleted": obj.get("securityReviewCompleted"),
            "securityReviewCompletionDate": obj.get("securityReviewCompletionDate"),
            "nextSecurityReviewDueDate": obj.get("nextSecurityReviewDueDate"),
            "hasOpenPoamItem": obj.get("hasOpenPoamItem"),
            "hasOpenPoamItem90to120PastScheduledCompletionDate": obj.get("hasOpenPoamItem90to120PastScheduledCompletionDate"),
            "hasOpenPoamItem120PlusPastScheudledCompletionDate": obj.get("hasOpenPoamItem120PlusPastScheudledCompletionDate"),
            "impact": obj.get("impact"),
            "hasCUI": obj.get("hasCUI"),
            "hasPII": obj.get("hasPII"),
            "hasPHI": obj.get("hasPHI"),
            "ppsmRegistrationRequired": obj.get("ppsmRegistrationRequired"),
            "ppsmRegistryNumber": obj.get("ppsmRegistryNumber"),
            "ppsmRegistrationExemptionJustification": obj.get("ppsmRegistrationExemptionJustification"),
            "interconnectedInformationSystemAndIdentifiers": obj.get("interconnectedInformationSystemAndIdentifiers"),
            "isPiaRequired": obj.get("isPiaRequired"),
            "piaStatus": obj.get("piaStatus"),
            "piaDate": obj.get("piaDate"),
            "userDefinedField1": obj.get("userDefinedField1"),
            "userDefinedField2": obj.get("userDefinedField2"),
            "userDefinedField3": obj.get("userDefinedField3"),
            "userDefinedField4": obj.get("userDefinedField4"),
            "userDefinedField5": obj.get("userDefinedField5"),
            "currentRmfLifecycleStep": obj.get("currentRmfLifecycleStep"),
            "otherInformation": obj.get("otherInformation"),
            "reportsForScorecard": obj.get("reportsForScorecard"),
            "highestSystemDataClassification": obj.get("highestSystemDataClassification"),
            "overallClassification": obj.get("overallClassification"),
            "isHVA": obj.get("isHVA"),
            "isFinancialManagement": obj.get("isFinancialManagement"),
            "isReciprocity": obj.get("isReciprocity"),
            "reciprocityExemption": obj.get("reciprocityExemption"),
            "cloudComputing": obj.get("cloudComputing"),
            "cloudType": obj.get("cloudType"),
            "atcStatus": obj.get("atcStatus"),
            "isSaaS": obj.get("isSaaS"),
            "isPaaS": obj.get("isPaaS"),
            "isIaaS": obj.get("isIaaS"),
            "otherServiceModels": obj.get("otherServiceModels"),
            "needDate": obj.get("needDate"),
            "overallRiskScore": obj.get("overallRiskScore"),
            "isHRR": obj.get("isHRR"),
            "atcDate": obj.get("atcDate"),
            "atcTerminationDate": obj.get("atcTerminationDate"),
            "systemDevelopmentLifeCycle": obj.get("systemDevelopmentLifeCycle"),
            "isFISMAReportable": obj.get("isFISMAReportable"),
            "groupTagging": obj.get("groupTagging"),
            "groupTagDescriptions": obj.get("groupTagDescriptions"),
            "dadmsId": obj.get("dadmsId"),
            "dadmsExpirationDate": obj.get("dadmsExpirationDate"),
            "enclaveConnectivity": obj.get("enclaveConnectivity"),
            "environmentType": obj.get("environmentType"),
            "navyCommonControlProvider": obj.get("navyCommonControlProvider"),
            "navyCloudBroker": obj.get("navyCloudBroker"),
            "cloudBrokerEmassId": obj.get("cloudBrokerEmassId"),
            "cloudBrokerProvisionalAuthorizationAtd": obj.get("cloudBrokerProvisionalAuthorizationAtd"),
            "navyJointAuthorization": obj.get("navyJointAuthorization"),
            "nmciNgenClins": obj.get("nmciNgenClins"),
            "enterpriseLocations": obj.get("enterpriseLocations"),
            "whitelistId": obj.get("whitelistId"),
            "whitelistInventory": obj.get("whitelistInventory"),
            "cybersecurityServiceProvider": obj.get("cybersecurityServiceProvider"),
            "cybersecurityServiceProviderExceptionJustification": obj.get("cybersecurityServiceProviderExceptionJustification"),
            "package": [PacGet.from_dict(_item) for _item in obj.get("package")] if obj.get("package") is not None else None,
            "connectivityCcsd": [ConnectivityCcsd.from_dict(_item) for _item in obj.get("connectivityCcsd")] if obj.get("connectivityCcsd") is not None else None
        })
        return _obj


