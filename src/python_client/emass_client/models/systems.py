# coding: utf-8

## eMASS API v3.10 Specification

The emass_client_api is a Python client that implements the [Enterprise Mission Assurance Support Service (eMASS)](https://disa.mil/~/media/Files/DISA/Fact-Sheets/eMASS.pdf)
Representational State Transfer (REST) Application Programming Interface (API) specifications.


This Python package was generated from the eMASS API specification:

- API version: v3.10
- Package version: 3.10.0
- Build date: 2023-06-13T13:46:18.843637Z[Etc/UTC]

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
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conint, conlist, validator
from emass_client.models.connectivity_ccsd import ConnectivityCcsd
from emass_client.models.pac_get import PacGet

class Systems(BaseModel):
    """
    Systems
    """
    registration_completion_date: Optional[StrictInt] = Field(None, alias="registrationCompletionDate", description="[Read-Only] Date the system was registered into eMASS.")
    system_life_cycle_acquisition_phase: Optional[StrictStr] = Field(None, alias="systemLifeCycleAcquisitionPhase", description="[Read-Only] Identifies the current System Acquisition Phase for programs of record.")
    special_type: Optional[StrictStr] = Field(None, alias="specialType", description="[Read-Only] Lists applicable tracking indicator(s).")
    special_type_description: Optional[StrictStr] = Field(None, alias="specialTypeDescription", description="[Read-Only] Provides a brief reason for any tracking indicator(s) selected.")
    mission_portfolio: Optional[StrictStr] = Field(None, alias="missionPortfolio", description="[Read-Only] Identifies the appropriate portfolio or capability area. Navy only.")
    is_nnpi: Optional[StrictBool] = Field(None, alias="isNNPI", description="[Read-Only] Indicates whether Naval Nuclear Propulsion Information (NNPI) is stored, disseminated, or processed through this system. Navy only.")
    is_rbc: Optional[StrictBool] = Field(None, alias="isRBC", description="[Read-Only] Indicates whether the system is pursuing an RBC authorization. Navy only.")
    is_waiver: Optional[StrictBool] = Field(None, alias="isWaiver", description="[Read-Only] Indicates if the system has a waiver from OPNAV N2N6G (DDCIO(N)) to proceed with a DIACAP accreditation. Navy and DIACAP only.")
    program_office: Optional[StrictStr] = Field(None, alias="programOffice", description="[Read-Only] The system record's Program Office. Navy only.")
    vram_id: Optional[StrictStr] = Field(None, alias="vramId", description="[Read-Only] Vulnerability Remediation Asset Manager (VRAM) identification number. \"N/A\" indicates the system record is not currently registered in VRAM.  Navy only.")
    system_id: Optional[StrictInt] = Field(None, alias="systemId", description="[Read-only] Unique system record identifier.")
    policy: Optional[StrictStr] = Field(None, description="[Read-only] RMF/DIACAP Policy identifier for the system record.")
    registration_type: Optional[StrictStr] = Field(None, alias="registrationType", description="[Read-Only] Registration types parameters (assessAndAuthorize, assessOnly, guest, regular, functional, cloudServiceProvider.)")
    name: Optional[StrictStr] = Field(None, description="[Read-only] Name of the system record.")
    acronym: Optional[StrictStr] = Field(None, description="[Read-only] Acronym of the system record.")
    description: Optional[StrictStr] = Field(None, description="[Read-only] Description of the system record.")
    instance: Optional[StrictStr] = Field(None, description="[Read-Only] Name of the top-level component that owns the system.")
    owning_organization: Optional[StrictStr] = Field(None, alias="owningOrganization", description="[Read-Only] Owning organization of the system record. Values match the eMASS instance Organizational Hierarchy.")
    secondary_organization: Optional[StrictStr] = Field(None, alias="secondaryOrganization", description="[Read-only] Secondary organization that owns the system record (i.e. Sub-Organization-level.")
    version_release_no: Optional[StrictStr] = Field(None, alias="versionReleaseNo", description="[Read-only] Version/Release Number of system record.")
    system_type: Optional[StrictStr] = Field(None, alias="systemType", description="[Read-only] Type of the system record. RMF values include the following options (IS Major Application, IS Enclave, Platform IT System). DIACAP values include the following options (Platform IT Interconnection, AIS Application, Outsourced IT-Based Process (DoD-controlled), Enclave, Outsourced IT-Based Process (service provider shared))")
    is_nss: Optional[StrictBool] = Field(None, alias="isNSS", description="[Read-only] Is the system record a National Security System?")
    is_public_facing: Optional[StrictBool] = Field(None, alias="isPublicFacing", description="[Read-only] Does the system record have a public facing component/presence.")
    coams_id: Optional[StrictInt] = Field(None, alias="coamsId", description="[Read-only] Corresponding Cyber Operational Attributes Management System (COAMS) identifier for the system record.")
    is_type_authorization: Optional[StrictBool] = Field(None, alias="isTypeAuthorization", description="[Read-only] Identifies if system is a Type Authorization.")
    ditpr_id: Optional[StrictStr] = Field(None, alias="ditprId", description="[Read-only] DITPR ID of the system record.")
    apms_id: Optional[StrictStr] = Field(None, alias="apmsId", description="[Read-Only] Same field as ditprId but displays as apmsId for Army only.")
    vasi_id: Optional[StrictStr] = Field(None, alias="vasiId", description="[Read-Only] Same field as ditprId but displays as vasiId for VA only.")
    authorization_status: Optional[StrictStr] = Field(None, alias="authorizationStatus", description="[Read-only] Authorization Status of the system record.")
    authorization_date: Optional[StrictInt] = Field(None, alias="authorizationDate", description="[Read-only] Authorization Date of the system record.")
    authorization_termination_date: Optional[StrictInt] = Field(None, alias="authorizationTerminationDate", description="[Read-only] Authorization Termination Date of the system record.")
    authorization_length: Optional[conint(strict=True, le=1825, ge=28)] = Field(None, alias="authorizationLength", description="[Read-only] Length of system's Authorization. Calculated based off of Authorization Date & Authorization Termination Date.")
    terms_for_auth: Optional[StrictStr] = Field(None, alias="termsForAuth", description="[Read-only] Terms/Conditions for receiving and maintaining the system's Authorization. Assigned by the Authorizing Official.")
    security_plan_approval_status: Optional[StrictStr] = Field(None, alias="securityPlanApprovalStatus", description="[Read-only] Status of the approval of the system's RMF Security Plan. Values include the following options (Approved, Denied, Not Yet Approved).")
    security_plan_approval_date: Optional[StrictInt] = Field(None, alias="securityPlanApprovalDate", description="[Read-only] Approval date of the system's RMF Security Plan.")
    mission_criticality: Optional[StrictStr] = Field(None, alias="missionCriticality", description="[Read-only] Mission Criticality of the system record.")
    geographical_association: Optional[StrictStr] = Field(None, alias="geographicalAssociation", description="[Read-only] Geographical Association of the system record.")
    system_ownership: Optional[StrictStr] = Field(None, alias="systemOwnership", description="[Read-only] Ownership of the system record.")
    governing_mission_area: Optional[StrictStr] = Field(None, alias="governingMissionArea", description="[Read-only] Governing Mission Area of the system record.")
    primary_functional_area: Optional[StrictStr] = Field(None, alias="primaryFunctionalArea", description="[Read-only] Primary functional area of the system record.")
    secondary_functional_area: Optional[StrictStr] = Field(None, alias="secondaryFunctionalArea", description="[Read-only] Secondary functional area of the system record.")
    primary_control_set: Optional[StrictStr] = Field(None, alias="primaryControlSet", description="[Read-only] Primary Control Set of the system record. RMF values include the following options (NIST SP 800-53 Revision 4), DIACAP values include the following options (DoDI 8500.2)")
    confidentiality: Optional[StrictStr] = Field(None, description="[Read-only] Confidentiality of the system record. RMF values include the following options (High, Moderate, Low)")
    integrity: Optional[StrictStr] = Field(None, description="[Read-only] Integrity of the system record. RMF values include the following options (High, Moderate, Low)")
    availability: Optional[StrictStr] = Field(None, description="[Read-only] Availability of the system record. RMF values include the following options (High, Moderate, Low)")
    applied_overlays: Optional[StrictStr] = Field(None, alias="appliedOverlays", description="[Read-only] Overlays applied to the system record.")
    rmf_activity: Optional[StrictStr] = Field(None, alias="rmfActivity", description="[Read-only] RMF Activity of the system record.")
    cross_domain_ticket: Optional[StrictStr] = Field(None, alias="crossDomainTicket", description="[Read-only] Cross Domain Tickets of the system record.")
    ditpr_don_id: Optional[StrictStr] = Field(None, alias="ditprDonId", description="[Read-Only] DITPR-DON identifier of the system record.")
    mac: Optional[StrictStr] = Field(None, description="[Read-Only] MAC level of the system record.")
    dod_confidentiality: Optional[StrictStr] = Field(None, alias="dodConfidentiality", description="[Read-Only] DoD Confidentiality level of the system record.")
    contingency_plan_tested: Optional[StrictBool] = Field(None, alias="contingencyPlanTested", description="[Read-only] Has the system record's Contingency Plan been tested?")
    contingency_plan_test_date: Optional[StrictInt] = Field(None, alias="contingencyPlanTestDate", description="[Read-only] Date the system record's Contingency Plan was tested.")
    security_review_date: Optional[StrictInt] = Field(None, alias="securityReviewDate", description="[Read-only] Date the system record's Annual Security Review was conducted.")
    has_open_poam_item: Optional[StrictBool] = Field(None, alias="hasOpenPoamItem", description="[Read-Only] Does the system record have an Ongoing or Risk Accepted POA&M Item?")
    has_open_poam_item90to120_past_scheduled_completion_date: Optional[StrictBool] = Field(None, alias="hasOpenPoamItem90to120PastScheduledCompletionDate", description="[Read-Only] Does the system record have an Ongoing or Risk Accepted POA&M Item 90 to 120 days past its Scheduled Completion Date?")
    has_open_poam_item120_plus_past_scheudled_completion_date: Optional[StrictBool] = Field(None, alias="hasOpenPoamItem120PlusPastScheudledCompletionDate", description="[Read-Only] Does the system record have an Ongoing or Risk Accepted POA&M Item 120 days past its Scheduled Completion Date?")
    impact: Optional[StrictStr] = Field(None, description="[Optional] Values include the following options (Very Low, Low, Moderate,High,Very High)")
    has_cui: Optional[StrictBool] = Field(None, alias="hasCUI", description="[Read-only] Does the system record contain and/or process Controlled Unclassified information?")
    has_pii: Optional[StrictBool] = Field(None, alias="hasPII", description="[Read-only] Does the system record contain and/or process Personally Identifiable Information?")
    has_phi: Optional[StrictBool] = Field(None, alias="hasPHI", description="[Read-only] Does the system record contain and/or process Personal Health Information?")
    ppsm_registry_number: Optional[StrictStr] = Field(None, alias="ppsmRegistryNumber", description="[Read-only] Unique identifier for the DoD’s Ports, Protocols, and Services Management Registry system.")
    interconnected_information_system_and_identifiers: Optional[StrictStr] = Field(None, alias="interconnectedInformationSystemAndIdentifiers", description="[Read-only] Identify the interconnected information systems and corresponding identifiers within control CA-3.")
    is_pia_required: Optional[StrictBool] = Field(None, alias="isPiaRequired", description="[Read-only] Does the system require a Privacy Impact Assessment?")
    pia_status: Optional[StrictStr] = Field(None, alias="piaStatus", description="[Read-only] Status of the PIA, availability values include the following options (Not Started, In Progress, Completed)")
    pia_date: Optional[StrictInt] = Field(None, alias="piaDate", description="[Read-only] Date in which the system's PIA took place.")
    user_defined_field1: Optional[StrictStr] = Field(None, alias="userDefinedField1", description="[Read-only] User-defined field to augment Ad Hoc Reporting.")
    user_defined_field2: Optional[StrictStr] = Field(None, alias="userDefinedField2", description="[Read-only] User-defined field to augment Ad Hoc Reporting.")
    user_defined_field3: Optional[StrictStr] = Field(None, alias="userDefinedField3", description="[Read-only] User-defined field to augment Ad Hoc Reporting.")
    user_defined_field4: Optional[StrictStr] = Field(None, alias="userDefinedField4", description="[Read-only] User-defined field to augment Ad Hoc Reporting.")
    user_defined_field5: Optional[StrictStr] = Field(None, alias="userDefinedField5", description="[Read-only] User-defined field to augment Ad Hoc Reporting.")
    current_rmf_lifecycle_step: Optional[StrictStr] = Field(None, alias="currentRmfLifecycleStep", description="[Read-only] Displays the system's current step within the RMF Lifecycle.")
    other_information: Optional[StrictStr] = Field(None, alias="otherInformation", description="[Read-only] Include any additional information required by the organization.")
    reports_for_scorecard: Optional[StrictBool] = Field(None, alias="reportsForScorecard", description="[Read-only] Indicates if the system reports to the DoD Cyber Hygiene Scorecard.")
    highest_system_data_classification: Optional[StrictStr] = Field(None, alias="highestSystemDataClassification", description="[Read-Only] The overall classification level of information that the System is approved to collect, process, store, and/or distribute.")
    overall_classification: Optional[StrictStr] = Field(None, alias="overallClassification", description="[Read-Only] Same field as highestSystemDataClassification, but displays as overallClassification for NISP only.")
    is_hva: Optional[StrictBool] = Field(None, alias="isHVA", description="[Read-Only] Indicates if the system contains High Value Assets. Does not display if value is null")
    is_financial_management: Optional[StrictBool] = Field(None, alias="isFinancialManagement", description="[Read-Only] Per OMB Circular A-127, a financial management system includes the core financial systems and the financial portions  of mixed systems necessary to support financial management, including automated and manual processes, procedures, and  controls, data, hardware, software, and support personnel dedicated to the operation and maintenance of system functions. The following are examples of financial management systems: core financial systems, procurement systems, loan systems, grants systems, payroll systems, budget formulation systems, billing systems, and travel systems. ")
    is_reciprocity: Optional[StrictBool] = Field(None, alias="isReciprocity", description="[Read-Only] A reciprocity system is any information system that is part of a mutual agreement among participating organizations to accept each other's security assessments in order to reuse information system resources and/or to accept each other's assessed security posture in order to share information. ")
    reciprocity_exemption: Optional[StrictStr] = Field(None, alias="reciprocityExemption", description="[Read-Only] The following justifications are acceptable for exemption from reciprocity: (a) the existence of the system is classified (not the data, but the existence of the system) or (b) the system's authorization to operate is in the process of being pulled (e.g. DATO, Decommission). ")
    cloud_computing: Optional[StrictBool] = Field(None, alias="cloudComputing", description="[Read-Only] Is this a cloud-based IS?")
    cloud_type: Optional[StrictStr] = Field(None, alias="cloudType", description="[Read-Only] Values include the following: (Hybrid, Private, Public)")
    atc_status: Optional[StrictStr] = Field(None, alias="atcStatus", description="[Read-Only] The Authority to Connect decision. Values include the following:  (Authority to Connect (ATC), Denial of Authority to Connect (DATC), Not Yet Connected, Decommissioned) ")
    is_saa_s: Optional[StrictBool] = Field(None, alias="isSaaS", description="[Read-Only] Software as a Service (SaaS) cloud service model.")
    is_paa_s: Optional[StrictBool] = Field(None, alias="isPaaS", description="[Read-Only] Platform as a Service (PaaS) cloud service model.")
    is_iaa_s: Optional[StrictBool] = Field(None, alias="isIaaS", description="[Read-Only] Infrastructure as a Service (IaaS) cloud service model.")
    other_service_models: Optional[StrictStr] = Field(None, alias="otherServiceModels", description="[Read-Only] Free text field to include other cloud service models.")
    need_date: Optional[StrictInt] = Field(None, alias="needDate", description="[Read-Only] Indicates the date by which the System needs to be deployed to a production environment.")
    overall_risk_score: Optional[StrictStr] = Field(None, alias="overallRiskScore", description="[Read-Only] The overall risk score of the system")
    is_hrr: Optional[StrictBool] = Field(None, alias="isHRR", description="[Read-Only] Identifies whether a System has been designated as High Risk Review. USCG and Navy only.")
    atc_date: Optional[StrictInt] = Field(None, alias="atcDate", description="[Read-Only] The Connectivity Authorization Date.")
    atc_termination_date: Optional[StrictInt] = Field(None, alias="atcTerminationDate", description="[Read-Only] The Connectivity Authorization Termination Date.")
    system_development_life_cycle: Optional[StrictStr] = Field(None, alias="systemDevelopmentLifeCycle", description="[Read-Only] Indicate the date by which the System needs to be deployed to a production environment. VA only.")
    is_fisma_reportable: Optional[StrictBool] = Field(None, alias="isFISMAReportable", description="[Read-Only] Is this IS reportable per Federal Information Security Management Act (FISMA) established requirements? VA only")
    group_tagging: Optional[StrictStr] = Field(None, alias="groupTagging", description="[Read-Only] System Tags for enterprise level, to include CIO and CISO, tracking efforts. VA only.")
    group_tag_descriptions: Optional[StrictStr] = Field(None, alias="groupTagDescriptions", description="[Read-Only] System Tag explanation(s) for enterprise level, to include CIO and CISO, tracking efforts. VA only.")
    package: Optional[conlist(PacGet)] = None
    connectivity_ccsd: Optional[conlist(ConnectivityCcsd)] = Field(None, alias="connectivityCcsd")
    __properties = ["registrationCompletionDate", "systemLifeCycleAcquisitionPhase", "specialType", "specialTypeDescription", "missionPortfolio", "isNNPI", "isRBC", "isWaiver", "programOffice", "vramId", "systemId", "policy", "registrationType", "name", "acronym", "description", "instance", "owningOrganization", "secondaryOrganization", "versionReleaseNo", "systemType", "isNSS", "isPublicFacing", "coamsId", "isTypeAuthorization", "ditprId", "apmsId", "vasiId", "authorizationStatus", "authorizationDate", "authorizationTerminationDate", "authorizationLength", "termsForAuth", "securityPlanApprovalStatus", "securityPlanApprovalDate", "missionCriticality", "geographicalAssociation", "systemOwnership", "governingMissionArea", "primaryFunctionalArea", "secondaryFunctionalArea", "primaryControlSet", "confidentiality", "integrity", "availability", "appliedOverlays", "rmfActivity", "crossDomainTicket", "ditprDonId", "mac", "dodConfidentiality", "contingencyPlanTested", "contingencyPlanTestDate", "securityReviewDate", "hasOpenPoamItem", "hasOpenPoamItem90to120PastScheduledCompletionDate", "hasOpenPoamItem120PlusPastScheudledCompletionDate", "impact", "hasCUI", "hasPII", "hasPHI", "ppsmRegistryNumber", "interconnectedInformationSystemAndIdentifiers", "isPiaRequired", "piaStatus", "piaDate", "userDefinedField1", "userDefinedField2", "userDefinedField3", "userDefinedField4", "userDefinedField5", "currentRmfLifecycleStep", "otherInformation", "reportsForScorecard", "highestSystemDataClassification", "overallClassification", "isHVA", "isFinancialManagement", "isReciprocity", "reciprocityExemption", "cloudComputing", "cloudType", "atcStatus", "isSaaS", "isPaaS", "isIaaS", "otherServiceModels", "needDate", "overallRiskScore", "isHRR", "atcDate", "atcTerminationDate", "systemDevelopmentLifeCycle", "isFISMAReportable", "groupTagging", "groupTagDescriptions", "package", "connectivityCcsd"]

    @validator('policy')
    def policy_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('RMF', 'DIACAP'):
            raise ValueError("must be one of enum values ('RMF', 'DIACAP')")
        return value

    @validator('registration_type')
    def registration_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Assess and Authorize', 'Assess Only', 'Guest', 'Regular', 'Functional', 'Cloud Service Provider', 'Common Control Provider'):
            raise ValueError("must be one of enum values ('Assess and Authorize', 'Assess Only', 'Guest', 'Regular', 'Functional', 'Cloud Service Provider', 'Common Control Provider')")
        return value

    @validator('system_type')
    def system_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('IS Major Application', 'IS Enclave', 'Platform IT', 'Platform IT System', 'Platform IT Interconnection', 'AIS Application', 'Outsourced IT-Based Process (DoD-controlled)', 'Enclave', 'Outsourced IT-Based Process (service provider shared)'):
            raise ValueError("must be one of enum values ('IS Major Application', 'IS Enclave', 'Platform IT', 'Platform IT System', 'Platform IT Interconnection', 'AIS Application', 'Outsourced IT-Based Process (DoD-controlled)', 'Enclave', 'Outsourced IT-Based Process (service provider shared)')")
        return value

    @validator('security_plan_approval_status')
    def security_plan_approval_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Approved', 'Not Yet Approved', 'Denied'):
            raise ValueError("must be one of enum values ('Approved', 'Not Yet Approved', 'Denied')")
        return value

    @validator('primary_control_set')
    def primary_control_set_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('NIST SP 800-53 Revision 4', 'DoDI 8500.2'):
            raise ValueError("must be one of enum values ('NIST SP 800-53 Revision 4', 'DoDI 8500.2')")
        return value

    @validator('confidentiality')
    def confidentiality_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('High', 'Moderate', 'Low'):
            raise ValueError("must be one of enum values ('High', 'Moderate', 'Low')")
        return value

    @validator('integrity')
    def integrity_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('High', 'Moderate', 'Low'):
            raise ValueError("must be one of enum values ('High', 'Moderate', 'Low')")
        return value

    @validator('availability')
    def availability_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('High', 'Moderate', 'Low'):
            raise ValueError("must be one of enum values ('High', 'Moderate', 'Low')")
        return value

    @validator('mac')
    def mac_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('I', 'II', 'III'):
            raise ValueError("must be one of enum values ('I', 'II', 'III')")
        return value

    @validator('dod_confidentiality')
    def dod_confidentiality_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Public', 'Sensitive', 'Classified'):
            raise ValueError("must be one of enum values ('Public', 'Sensitive', 'Classified')")
        return value

    @validator('impact')
    def impact_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Low', 'Moderate', 'High'):
            raise ValueError("must be one of enum values ('Low', 'Moderate', 'High')")
        return value

    @validator('pia_status')
    def pia_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Not Started', 'In Progress', 'Completed'):
            raise ValueError("must be one of enum values ('Not Started', 'In Progress', 'Completed')")
        return value

    @validator('current_rmf_lifecycle_step')
    def current_rmf_lifecycle_step_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('1 - Categorize', '2 - Select', '3 - Implement', '4 - Assess', '5 - Authorize', '6 - Monitor'):
            raise ValueError("must be one of enum values ('1 - Categorize', '2 - Select', '3 - Implement', '4 - Assess', '5 - Authorize', '6 - Monitor')")
        return value

    @validator('cloud_type')
    def cloud_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Hybrid', 'Private', 'Public'):
            raise ValueError("must be one of enum values ('Hybrid', 'Private', 'Public')")
        return value

    @validator('atc_status')
    def atc_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Authority to Connect (ATC)', 'Denial of Authority to Connect (DATC)', 'Not Yet Connected', 'Decommissioned'):
            raise ValueError("must be one of enum values ('Authority to Connect (ATC)', 'Denial of Authority to Connect (DATC)', 'Not Yet Connected', 'Decommissioned')")
        return value

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Systems:
        """Create an instance of Systems from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
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
        # and __fields_set__ contains the field
        if self.registration_completion_date is None and "registration_completion_date" in self.__fields_set__:
            _dict['registrationCompletionDate'] = None

        # set to None if system_life_cycle_acquisition_phase (nullable) is None
        # and __fields_set__ contains the field
        if self.system_life_cycle_acquisition_phase is None and "system_life_cycle_acquisition_phase" in self.__fields_set__:
            _dict['systemLifeCycleAcquisitionPhase'] = None

        # set to None if special_type (nullable) is None
        # and __fields_set__ contains the field
        if self.special_type is None and "special_type" in self.__fields_set__:
            _dict['specialType'] = None

        # set to None if special_type_description (nullable) is None
        # and __fields_set__ contains the field
        if self.special_type_description is None and "special_type_description" in self.__fields_set__:
            _dict['specialTypeDescription'] = None

        # set to None if mission_portfolio (nullable) is None
        # and __fields_set__ contains the field
        if self.mission_portfolio is None and "mission_portfolio" in self.__fields_set__:
            _dict['missionPortfolio'] = None

        # set to None if is_nnpi (nullable) is None
        # and __fields_set__ contains the field
        if self.is_nnpi is None and "is_nnpi" in self.__fields_set__:
            _dict['isNNPI'] = None

        # set to None if is_rbc (nullable) is None
        # and __fields_set__ contains the field
        if self.is_rbc is None and "is_rbc" in self.__fields_set__:
            _dict['isRBC'] = None

        # set to None if is_waiver (nullable) is None
        # and __fields_set__ contains the field
        if self.is_waiver is None and "is_waiver" in self.__fields_set__:
            _dict['isWaiver'] = None

        # set to None if program_office (nullable) is None
        # and __fields_set__ contains the field
        if self.program_office is None and "program_office" in self.__fields_set__:
            _dict['programOffice'] = None

        # set to None if vram_id (nullable) is None
        # and __fields_set__ contains the field
        if self.vram_id is None and "vram_id" in self.__fields_set__:
            _dict['vramId'] = None

        # set to None if policy (nullable) is None
        # and __fields_set__ contains the field
        if self.policy is None and "policy" in self.__fields_set__:
            _dict['policy'] = None

        # set to None if registration_type (nullable) is None
        # and __fields_set__ contains the field
        if self.registration_type is None and "registration_type" in self.__fields_set__:
            _dict['registrationType'] = None

        # set to None if name (nullable) is None
        # and __fields_set__ contains the field
        if self.name is None and "name" in self.__fields_set__:
            _dict['name'] = None

        # set to None if acronym (nullable) is None
        # and __fields_set__ contains the field
        if self.acronym is None and "acronym" in self.__fields_set__:
            _dict['acronym'] = None

        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        # set to None if instance (nullable) is None
        # and __fields_set__ contains the field
        if self.instance is None and "instance" in self.__fields_set__:
            _dict['instance'] = None

        # set to None if owning_organization (nullable) is None
        # and __fields_set__ contains the field
        if self.owning_organization is None and "owning_organization" in self.__fields_set__:
            _dict['owningOrganization'] = None

        # set to None if secondary_organization (nullable) is None
        # and __fields_set__ contains the field
        if self.secondary_organization is None and "secondary_organization" in self.__fields_set__:
            _dict['secondaryOrganization'] = None

        # set to None if version_release_no (nullable) is None
        # and __fields_set__ contains the field
        if self.version_release_no is None and "version_release_no" in self.__fields_set__:
            _dict['versionReleaseNo'] = None

        # set to None if system_type (nullable) is None
        # and __fields_set__ contains the field
        if self.system_type is None and "system_type" in self.__fields_set__:
            _dict['systemType'] = None

        # set to None if is_nss (nullable) is None
        # and __fields_set__ contains the field
        if self.is_nss is None and "is_nss" in self.__fields_set__:
            _dict['isNSS'] = None

        # set to None if is_public_facing (nullable) is None
        # and __fields_set__ contains the field
        if self.is_public_facing is None and "is_public_facing" in self.__fields_set__:
            _dict['isPublicFacing'] = None

        # set to None if coams_id (nullable) is None
        # and __fields_set__ contains the field
        if self.coams_id is None and "coams_id" in self.__fields_set__:
            _dict['coamsId'] = None

        # set to None if is_type_authorization (nullable) is None
        # and __fields_set__ contains the field
        if self.is_type_authorization is None and "is_type_authorization" in self.__fields_set__:
            _dict['isTypeAuthorization'] = None

        # set to None if apms_id (nullable) is None
        # and __fields_set__ contains the field
        if self.apms_id is None and "apms_id" in self.__fields_set__:
            _dict['apmsId'] = None

        # set to None if vasi_id (nullable) is None
        # and __fields_set__ contains the field
        if self.vasi_id is None and "vasi_id" in self.__fields_set__:
            _dict['vasiId'] = None

        # set to None if authorization_status (nullable) is None
        # and __fields_set__ contains the field
        if self.authorization_status is None and "authorization_status" in self.__fields_set__:
            _dict['authorizationStatus'] = None

        # set to None if authorization_date (nullable) is None
        # and __fields_set__ contains the field
        if self.authorization_date is None and "authorization_date" in self.__fields_set__:
            _dict['authorizationDate'] = None

        # set to None if authorization_termination_date (nullable) is None
        # and __fields_set__ contains the field
        if self.authorization_termination_date is None and "authorization_termination_date" in self.__fields_set__:
            _dict['authorizationTerminationDate'] = None

        # set to None if authorization_length (nullable) is None
        # and __fields_set__ contains the field
        if self.authorization_length is None and "authorization_length" in self.__fields_set__:
            _dict['authorizationLength'] = None

        # set to None if terms_for_auth (nullable) is None
        # and __fields_set__ contains the field
        if self.terms_for_auth is None and "terms_for_auth" in self.__fields_set__:
            _dict['termsForAuth'] = None

        # set to None if security_plan_approval_status (nullable) is None
        # and __fields_set__ contains the field
        if self.security_plan_approval_status is None and "security_plan_approval_status" in self.__fields_set__:
            _dict['securityPlanApprovalStatus'] = None

        # set to None if security_plan_approval_date (nullable) is None
        # and __fields_set__ contains the field
        if self.security_plan_approval_date is None and "security_plan_approval_date" in self.__fields_set__:
            _dict['securityPlanApprovalDate'] = None

        # set to None if mission_criticality (nullable) is None
        # and __fields_set__ contains the field
        if self.mission_criticality is None and "mission_criticality" in self.__fields_set__:
            _dict['missionCriticality'] = None

        # set to None if geographical_association (nullable) is None
        # and __fields_set__ contains the field
        if self.geographical_association is None and "geographical_association" in self.__fields_set__:
            _dict['geographicalAssociation'] = None

        # set to None if system_ownership (nullable) is None
        # and __fields_set__ contains the field
        if self.system_ownership is None and "system_ownership" in self.__fields_set__:
            _dict['systemOwnership'] = None

        # set to None if governing_mission_area (nullable) is None
        # and __fields_set__ contains the field
        if self.governing_mission_area is None and "governing_mission_area" in self.__fields_set__:
            _dict['governingMissionArea'] = None

        # set to None if primary_functional_area (nullable) is None
        # and __fields_set__ contains the field
        if self.primary_functional_area is None and "primary_functional_area" in self.__fields_set__:
            _dict['primaryFunctionalArea'] = None

        # set to None if secondary_functional_area (nullable) is None
        # and __fields_set__ contains the field
        if self.secondary_functional_area is None and "secondary_functional_area" in self.__fields_set__:
            _dict['secondaryFunctionalArea'] = None

        # set to None if primary_control_set (nullable) is None
        # and __fields_set__ contains the field
        if self.primary_control_set is None and "primary_control_set" in self.__fields_set__:
            _dict['primaryControlSet'] = None

        # set to None if confidentiality (nullable) is None
        # and __fields_set__ contains the field
        if self.confidentiality is None and "confidentiality" in self.__fields_set__:
            _dict['confidentiality'] = None

        # set to None if integrity (nullable) is None
        # and __fields_set__ contains the field
        if self.integrity is None and "integrity" in self.__fields_set__:
            _dict['integrity'] = None

        # set to None if availability (nullable) is None
        # and __fields_set__ contains the field
        if self.availability is None and "availability" in self.__fields_set__:
            _dict['availability'] = None

        # set to None if applied_overlays (nullable) is None
        # and __fields_set__ contains the field
        if self.applied_overlays is None and "applied_overlays" in self.__fields_set__:
            _dict['appliedOverlays'] = None

        # set to None if rmf_activity (nullable) is None
        # and __fields_set__ contains the field
        if self.rmf_activity is None and "rmf_activity" in self.__fields_set__:
            _dict['rmfActivity'] = None

        # set to None if cross_domain_ticket (nullable) is None
        # and __fields_set__ contains the field
        if self.cross_domain_ticket is None and "cross_domain_ticket" in self.__fields_set__:
            _dict['crossDomainTicket'] = None

        # set to None if ditpr_don_id (nullable) is None
        # and __fields_set__ contains the field
        if self.ditpr_don_id is None and "ditpr_don_id" in self.__fields_set__:
            _dict['ditprDonId'] = None

        # set to None if mac (nullable) is None
        # and __fields_set__ contains the field
        if self.mac is None and "mac" in self.__fields_set__:
            _dict['mac'] = None

        # set to None if dod_confidentiality (nullable) is None
        # and __fields_set__ contains the field
        if self.dod_confidentiality is None and "dod_confidentiality" in self.__fields_set__:
            _dict['dodConfidentiality'] = None

        # set to None if contingency_plan_tested (nullable) is None
        # and __fields_set__ contains the field
        if self.contingency_plan_tested is None and "contingency_plan_tested" in self.__fields_set__:
            _dict['contingencyPlanTested'] = None

        # set to None if contingency_plan_test_date (nullable) is None
        # and __fields_set__ contains the field
        if self.contingency_plan_test_date is None and "contingency_plan_test_date" in self.__fields_set__:
            _dict['contingencyPlanTestDate'] = None

        # set to None if security_review_date (nullable) is None
        # and __fields_set__ contains the field
        if self.security_review_date is None and "security_review_date" in self.__fields_set__:
            _dict['securityReviewDate'] = None

        # set to None if has_open_poam_item (nullable) is None
        # and __fields_set__ contains the field
        if self.has_open_poam_item is None and "has_open_poam_item" in self.__fields_set__:
            _dict['hasOpenPoamItem'] = None

        # set to None if has_open_poam_item90to120_past_scheduled_completion_date (nullable) is None
        # and __fields_set__ contains the field
        if self.has_open_poam_item90to120_past_scheduled_completion_date is None and "has_open_poam_item90to120_past_scheduled_completion_date" in self.__fields_set__:
            _dict['hasOpenPoamItem90to120PastScheduledCompletionDate'] = None

        # set to None if has_open_poam_item120_plus_past_scheudled_completion_date (nullable) is None
        # and __fields_set__ contains the field
        if self.has_open_poam_item120_plus_past_scheudled_completion_date is None and "has_open_poam_item120_plus_past_scheudled_completion_date" in self.__fields_set__:
            _dict['hasOpenPoamItem120PlusPastScheudledCompletionDate'] = None

        # set to None if impact (nullable) is None
        # and __fields_set__ contains the field
        if self.impact is None and "impact" in self.__fields_set__:
            _dict['impact'] = None

        # set to None if has_cui (nullable) is None
        # and __fields_set__ contains the field
        if self.has_cui is None and "has_cui" in self.__fields_set__:
            _dict['hasCUI'] = None

        # set to None if has_pii (nullable) is None
        # and __fields_set__ contains the field
        if self.has_pii is None and "has_pii" in self.__fields_set__:
            _dict['hasPII'] = None

        # set to None if has_phi (nullable) is None
        # and __fields_set__ contains the field
        if self.has_phi is None and "has_phi" in self.__fields_set__:
            _dict['hasPHI'] = None

        # set to None if ppsm_registry_number (nullable) is None
        # and __fields_set__ contains the field
        if self.ppsm_registry_number is None and "ppsm_registry_number" in self.__fields_set__:
            _dict['ppsmRegistryNumber'] = None

        # set to None if interconnected_information_system_and_identifiers (nullable) is None
        # and __fields_set__ contains the field
        if self.interconnected_information_system_and_identifiers is None and "interconnected_information_system_and_identifiers" in self.__fields_set__:
            _dict['interconnectedInformationSystemAndIdentifiers'] = None

        # set to None if is_pia_required (nullable) is None
        # and __fields_set__ contains the field
        if self.is_pia_required is None and "is_pia_required" in self.__fields_set__:
            _dict['isPiaRequired'] = None

        # set to None if pia_status (nullable) is None
        # and __fields_set__ contains the field
        if self.pia_status is None and "pia_status" in self.__fields_set__:
            _dict['piaStatus'] = None

        # set to None if pia_date (nullable) is None
        # and __fields_set__ contains the field
        if self.pia_date is None and "pia_date" in self.__fields_set__:
            _dict['piaDate'] = None

        # set to None if user_defined_field1 (nullable) is None
        # and __fields_set__ contains the field
        if self.user_defined_field1 is None and "user_defined_field1" in self.__fields_set__:
            _dict['userDefinedField1'] = None

        # set to None if user_defined_field2 (nullable) is None
        # and __fields_set__ contains the field
        if self.user_defined_field2 is None and "user_defined_field2" in self.__fields_set__:
            _dict['userDefinedField2'] = None

        # set to None if user_defined_field3 (nullable) is None
        # and __fields_set__ contains the field
        if self.user_defined_field3 is None and "user_defined_field3" in self.__fields_set__:
            _dict['userDefinedField3'] = None

        # set to None if user_defined_field4 (nullable) is None
        # and __fields_set__ contains the field
        if self.user_defined_field4 is None and "user_defined_field4" in self.__fields_set__:
            _dict['userDefinedField4'] = None

        # set to None if user_defined_field5 (nullable) is None
        # and __fields_set__ contains the field
        if self.user_defined_field5 is None and "user_defined_field5" in self.__fields_set__:
            _dict['userDefinedField5'] = None

        # set to None if current_rmf_lifecycle_step (nullable) is None
        # and __fields_set__ contains the field
        if self.current_rmf_lifecycle_step is None and "current_rmf_lifecycle_step" in self.__fields_set__:
            _dict['currentRmfLifecycleStep'] = None

        # set to None if other_information (nullable) is None
        # and __fields_set__ contains the field
        if self.other_information is None and "other_information" in self.__fields_set__:
            _dict['otherInformation'] = None

        # set to None if reports_for_scorecard (nullable) is None
        # and __fields_set__ contains the field
        if self.reports_for_scorecard is None and "reports_for_scorecard" in self.__fields_set__:
            _dict['reportsForScorecard'] = None

        # set to None if highest_system_data_classification (nullable) is None
        # and __fields_set__ contains the field
        if self.highest_system_data_classification is None and "highest_system_data_classification" in self.__fields_set__:
            _dict['highestSystemDataClassification'] = None

        # set to None if overall_classification (nullable) is None
        # and __fields_set__ contains the field
        if self.overall_classification is None and "overall_classification" in self.__fields_set__:
            _dict['overallClassification'] = None

        # set to None if is_hva (nullable) is None
        # and __fields_set__ contains the field
        if self.is_hva is None and "is_hva" in self.__fields_set__:
            _dict['isHVA'] = None

        # set to None if is_financial_management (nullable) is None
        # and __fields_set__ contains the field
        if self.is_financial_management is None and "is_financial_management" in self.__fields_set__:
            _dict['isFinancialManagement'] = None

        # set to None if is_reciprocity (nullable) is None
        # and __fields_set__ contains the field
        if self.is_reciprocity is None and "is_reciprocity" in self.__fields_set__:
            _dict['isReciprocity'] = None

        # set to None if reciprocity_exemption (nullable) is None
        # and __fields_set__ contains the field
        if self.reciprocity_exemption is None and "reciprocity_exemption" in self.__fields_set__:
            _dict['reciprocityExemption'] = None

        # set to None if cloud_computing (nullable) is None
        # and __fields_set__ contains the field
        if self.cloud_computing is None and "cloud_computing" in self.__fields_set__:
            _dict['cloudComputing'] = None

        # set to None if cloud_type (nullable) is None
        # and __fields_set__ contains the field
        if self.cloud_type is None and "cloud_type" in self.__fields_set__:
            _dict['cloudType'] = None

        # set to None if atc_status (nullable) is None
        # and __fields_set__ contains the field
        if self.atc_status is None and "atc_status" in self.__fields_set__:
            _dict['atcStatus'] = None

        # set to None if is_saa_s (nullable) is None
        # and __fields_set__ contains the field
        if self.is_saa_s is None and "is_saa_s" in self.__fields_set__:
            _dict['isSaaS'] = None

        # set to None if is_paa_s (nullable) is None
        # and __fields_set__ contains the field
        if self.is_paa_s is None and "is_paa_s" in self.__fields_set__:
            _dict['isPaaS'] = None

        # set to None if is_iaa_s (nullable) is None
        # and __fields_set__ contains the field
        if self.is_iaa_s is None and "is_iaa_s" in self.__fields_set__:
            _dict['isIaaS'] = None

        # set to None if other_service_models (nullable) is None
        # and __fields_set__ contains the field
        if self.other_service_models is None and "other_service_models" in self.__fields_set__:
            _dict['otherServiceModels'] = None

        # set to None if need_date (nullable) is None
        # and __fields_set__ contains the field
        if self.need_date is None and "need_date" in self.__fields_set__:
            _dict['needDate'] = None

        # set to None if overall_risk_score (nullable) is None
        # and __fields_set__ contains the field
        if self.overall_risk_score is None and "overall_risk_score" in self.__fields_set__:
            _dict['overallRiskScore'] = None

        # set to None if is_hrr (nullable) is None
        # and __fields_set__ contains the field
        if self.is_hrr is None and "is_hrr" in self.__fields_set__:
            _dict['isHRR'] = None

        # set to None if atc_date (nullable) is None
        # and __fields_set__ contains the field
        if self.atc_date is None and "atc_date" in self.__fields_set__:
            _dict['atcDate'] = None

        # set to None if atc_termination_date (nullable) is None
        # and __fields_set__ contains the field
        if self.atc_termination_date is None and "atc_termination_date" in self.__fields_set__:
            _dict['atcTerminationDate'] = None

        # set to None if system_development_life_cycle (nullable) is None
        # and __fields_set__ contains the field
        if self.system_development_life_cycle is None and "system_development_life_cycle" in self.__fields_set__:
            _dict['systemDevelopmentLifeCycle'] = None

        # set to None if is_fisma_reportable (nullable) is None
        # and __fields_set__ contains the field
        if self.is_fisma_reportable is None and "is_fisma_reportable" in self.__fields_set__:
            _dict['isFISMAReportable'] = None

        # set to None if group_tagging (nullable) is None
        # and __fields_set__ contains the field
        if self.group_tagging is None and "group_tagging" in self.__fields_set__:
            _dict['groupTagging'] = None

        # set to None if group_tag_descriptions (nullable) is None
        # and __fields_set__ contains the field
        if self.group_tag_descriptions is None and "group_tag_descriptions" in self.__fields_set__:
            _dict['groupTagDescriptions'] = None

        # set to None if package (nullable) is None
        # and __fields_set__ contains the field
        if self.package is None and "package" in self.__fields_set__:
            _dict['package'] = None

        # set to None if connectivity_ccsd (nullable) is None
        # and __fields_set__ contains the field
        if self.connectivity_ccsd is None and "connectivity_ccsd" in self.__fields_set__:
            _dict['connectivityCcsd'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Systems:
        """Create an instance of Systems from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Systems.parse_obj(obj)

        _obj = Systems.parse_obj({
            "registration_completion_date": obj.get("registrationCompletionDate"),
            "system_life_cycle_acquisition_phase": obj.get("systemLifeCycleAcquisitionPhase"),
            "special_type": obj.get("specialType"),
            "special_type_description": obj.get("specialTypeDescription"),
            "mission_portfolio": obj.get("missionPortfolio"),
            "is_nnpi": obj.get("isNNPI"),
            "is_rbc": obj.get("isRBC"),
            "is_waiver": obj.get("isWaiver"),
            "program_office": obj.get("programOffice"),
            "vram_id": obj.get("vramId"),
            "system_id": obj.get("systemId"),
            "policy": obj.get("policy"),
            "registration_type": obj.get("registrationType"),
            "name": obj.get("name"),
            "acronym": obj.get("acronym"),
            "description": obj.get("description"),
            "instance": obj.get("instance"),
            "owning_organization": obj.get("owningOrganization"),
            "secondary_organization": obj.get("secondaryOrganization"),
            "version_release_no": obj.get("versionReleaseNo"),
            "system_type": obj.get("systemType"),
            "is_nss": obj.get("isNSS"),
            "is_public_facing": obj.get("isPublicFacing"),
            "coams_id": obj.get("coamsId"),
            "is_type_authorization": obj.get("isTypeAuthorization"),
            "ditpr_id": obj.get("ditprId"),
            "apms_id": obj.get("apmsId"),
            "vasi_id": obj.get("vasiId"),
            "authorization_status": obj.get("authorizationStatus"),
            "authorization_date": obj.get("authorizationDate"),
            "authorization_termination_date": obj.get("authorizationTerminationDate"),
            "authorization_length": obj.get("authorizationLength"),
            "terms_for_auth": obj.get("termsForAuth"),
            "security_plan_approval_status": obj.get("securityPlanApprovalStatus"),
            "security_plan_approval_date": obj.get("securityPlanApprovalDate"),
            "mission_criticality": obj.get("missionCriticality"),
            "geographical_association": obj.get("geographicalAssociation"),
            "system_ownership": obj.get("systemOwnership"),
            "governing_mission_area": obj.get("governingMissionArea"),
            "primary_functional_area": obj.get("primaryFunctionalArea"),
            "secondary_functional_area": obj.get("secondaryFunctionalArea"),
            "primary_control_set": obj.get("primaryControlSet"),
            "confidentiality": obj.get("confidentiality"),
            "integrity": obj.get("integrity"),
            "availability": obj.get("availability"),
            "applied_overlays": obj.get("appliedOverlays"),
            "rmf_activity": obj.get("rmfActivity"),
            "cross_domain_ticket": obj.get("crossDomainTicket"),
            "ditpr_don_id": obj.get("ditprDonId"),
            "mac": obj.get("mac"),
            "dod_confidentiality": obj.get("dodConfidentiality"),
            "contingency_plan_tested": obj.get("contingencyPlanTested"),
            "contingency_plan_test_date": obj.get("contingencyPlanTestDate"),
            "security_review_date": obj.get("securityReviewDate"),
            "has_open_poam_item": obj.get("hasOpenPoamItem"),
            "has_open_poam_item90to120_past_scheduled_completion_date": obj.get("hasOpenPoamItem90to120PastScheduledCompletionDate"),
            "has_open_poam_item120_plus_past_scheudled_completion_date": obj.get("hasOpenPoamItem120PlusPastScheudledCompletionDate"),
            "impact": obj.get("impact"),
            "has_cui": obj.get("hasCUI"),
            "has_pii": obj.get("hasPII"),
            "has_phi": obj.get("hasPHI"),
            "ppsm_registry_number": obj.get("ppsmRegistryNumber"),
            "interconnected_information_system_and_identifiers": obj.get("interconnectedInformationSystemAndIdentifiers"),
            "is_pia_required": obj.get("isPiaRequired"),
            "pia_status": obj.get("piaStatus"),
            "pia_date": obj.get("piaDate"),
            "user_defined_field1": obj.get("userDefinedField1"),
            "user_defined_field2": obj.get("userDefinedField2"),
            "user_defined_field3": obj.get("userDefinedField3"),
            "user_defined_field4": obj.get("userDefinedField4"),
            "user_defined_field5": obj.get("userDefinedField5"),
            "current_rmf_lifecycle_step": obj.get("currentRmfLifecycleStep"),
            "other_information": obj.get("otherInformation"),
            "reports_for_scorecard": obj.get("reportsForScorecard"),
            "highest_system_data_classification": obj.get("highestSystemDataClassification"),
            "overall_classification": obj.get("overallClassification"),
            "is_hva": obj.get("isHVA"),
            "is_financial_management": obj.get("isFinancialManagement"),
            "is_reciprocity": obj.get("isReciprocity"),
            "reciprocity_exemption": obj.get("reciprocityExemption"),
            "cloud_computing": obj.get("cloudComputing"),
            "cloud_type": obj.get("cloudType"),
            "atc_status": obj.get("atcStatus"),
            "is_saa_s": obj.get("isSaaS"),
            "is_paa_s": obj.get("isPaaS"),
            "is_iaa_s": obj.get("isIaaS"),
            "other_service_models": obj.get("otherServiceModels"),
            "need_date": obj.get("needDate"),
            "overall_risk_score": obj.get("overallRiskScore"),
            "is_hrr": obj.get("isHRR"),
            "atc_date": obj.get("atcDate"),
            "atc_termination_date": obj.get("atcTerminationDate"),
            "system_development_life_cycle": obj.get("systemDevelopmentLifeCycle"),
            "is_fisma_reportable": obj.get("isFISMAReportable"),
            "group_tagging": obj.get("groupTagging"),
            "group_tag_descriptions": obj.get("groupTagDescriptions"),
            "package": [PacGet.from_dict(_item) for _item in obj.get("package")] if obj.get("package") is not None else None,
            "connectivity_ccsd": [ConnectivityCcsd.from_dict(_item) for _item in obj.get("connectivityCcsd")] if obj.get("connectivityCcsd") is not None else None
        })
        return _obj

