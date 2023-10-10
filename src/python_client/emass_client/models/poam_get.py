# coding: utf-8

## eMASS API v3.12 Specification

The emass_client_api is a Python client that implements the [Enterprise Mission Assurance Support Service (eMASS)](https://disa.mil/~/media/Files/DISA/Fact-Sheets/eMASS.pdf)
Representational State Transfer (REST) Application Programming Interface (API) specifications.


This Python package was generated from the eMASS API specification:

- API version: v3.12
- Package version: 3.11.1
- Build date: 2023-10-10T00:32:11.514559Z[Etc/UTC]

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


from typing import List, Optional, Union
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr, field_validator
from pydantic import Field
from emass_client.models.milestones_get import MilestonesGet
from typing import Dict, Any
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class PoamGet(BaseModel):
    """
    PoamGet
    """
    system_id: Optional[StrictInt] = Field(default=None, description="[Required] Unique eMASS system identifier.", alias="systemId")
    poam_id: Optional[StrictInt] = Field(default=None, description="[Required] Unique item identifier", alias="poamId")
    display_poam_id: Optional[StrictInt] = Field(default=None, description="[Required] Globally unique identifier for individual POA&M Items, seen on the front-end as “ID”.", alias="displayPoamId")
    is_inherited: Optional[StrictBool] = Field(default=None, description="[Read-only] Indicates whether a test result is inherited.", alias="isInherited")
    external_uid: Optional[StrictStr] = Field(default=None, description="[Optional] Unique identifier external to the eMASS application for use with associating POA&Ms. 100 Characters.", alias="externalUid")
    control_acronym: Optional[StrictStr] = Field(default=None, description="[Optional] System acronym name.", alias="controlAcronym")
    cci: Optional[StrictStr] = Field(default=None, description="[Optional] CCI associated with POA&M Item..")
    assessment_procedure: Optional[StrictStr] = Field(default=None, description="[Optional] The Security Control Assessment Procedure being associated with the POA&M Item.", alias="assessmentProcedure")
    status: Optional[StrictStr] = Field(default=None, description="[Required] Values include the following: (Ongoing,Risk Accepted,Completed,Not Applicable")
    review_status: Optional[StrictStr] = Field(default=None, description="[Read-Only] Values include the following options: (Not Approved,Under Review,Approved)", alias="reviewStatus")
    vulnerability_description: Optional[StrictStr] = Field(default=None, description="[Required] Provide a description of the POA&M Item. 2000 Characters.", alias="vulnerabilityDescription")
    source_ident_vuln: Optional[StrictStr] = Field(default=None, description="[Required] Include Source Identifying Vulnerability text. 2000 Characters.", alias="sourceIdentVuln")
    security_checks: Optional[StrictStr] = Field(default=None, description="[Optional] Security Checks that are associated with the POA&M.", alias="securityChecks")
    milestones: Optional[List[MilestonesGet]] = None
    poc_organization: Optional[StrictStr] = Field(default=None, description="[Required] Organization/Office represented. 100 Characters.", alias="pocOrganization")
    poc_first_name: Optional[StrictStr] = Field(default=None, description="[Conditional] First name of POC. 100 Characters.", alias="pocFirstName")
    poc_last_name: Optional[StrictStr] = Field(default=None, description="[Conditional] Last name of POC. 100 Characters.", alias="pocLastName")
    poc_email: Optional[StrictStr] = Field(default=None, description="[Conditional] Email address of POC. 100 Characters.", alias="pocEmail")
    poc_phone_number: Optional[StrictStr] = Field(default=None, description="[Conditional] Phone number of POC. 100 Characters.", alias="pocPhoneNumber")
    severity: Optional[StrictStr] = Field(default=None, description="[Conditional] Required for approved items. Values include the following options (Very Low,Low,Moderate,High,Very High)")
    raw_severity: Optional[StrictStr] = Field(default=None, description="[Optional] Values include the following options (I,II,III)", alias="rawSeverity")
    relevance_of_threat: Optional[StrictStr] = Field(default=None, description="[Optional] Values include the following options: (Very Low,Low,Moderate,High,Very High)", alias="relevanceOfThreat")
    likelihood: Optional[StrictStr] = Field(default=None, description="[Optional] Values include the following options: (Very Low,Low,Moderate,High,Very High)")
    impact: Optional[StrictStr] = Field(default=None, description="[Optional] Values include the following options: (Very Low,Low,Moderate,High,Very High)")
    impact_description: Optional[StrictStr] = Field(default=None, description="[Optional] Include description of Security Control’s impact.", alias="impactDescription")
    residual_risk_level: Optional[StrictStr] = Field(default=None, description="[Optional] Values include the following options: (Very Low,Low,Moderate,High,Very High)", alias="residualRiskLevel")
    recommendations: Optional[StrictStr] = Field(default=None, description="[Optional] Include recommendations. Character Limit = 2,000.")
    resources: Optional[StrictStr] = Field(default=None, description="[Required] List of resources used. 250 Characters.")
    scheduled_completion_date: Optional[StrictInt] = Field(default=None, description="[Conditional] Required for ongoing and completed POA&M items. Unix time format.", alias="scheduledCompletionDate")
    completion_date: Optional[StrictInt] = Field(default=None, description="[Conditional] Field is required for completed POA&M items. Unix time format.", alias="completionDate")
    extension_date: Optional[StrictInt] = Field(default=None, description="[Read-Only] Value returned for a POA&M Item with review status Approved” and has a milestone with a scheduled completion date that extends beyond the POA&M Item’s scheduled completion date. ", alias="extensionDate")
    comments: Optional[StrictStr] = Field(default=None, description="[Conditional] Field is required for completed and risk accepted POA&M items. 2000 Characters")
    mitigation: Optional[StrictStr] = Field(default=None, description="[Optional] Include mitigation explanation. 2000 Characters.")
    is_active: Optional[StrictBool] = Field(default=None, description="[Conditional] Optionally used in PUT to delete milestones when updating a POA&M.", alias="isActive")
    resulting_residual_risk_level_after_proposed_mitigations: Optional[StrictStr] = Field(default=None, description="[Optional] Indicate the risk level expected after any proposed mitigations are implemented. Proposed mitigations should be appropriately documented as POA&M milestones. Navy only.", alias="resultingResidualRiskLevelAfterProposedMitigations")
    predisposing_conditions: Optional[StrictStr] = Field(default=None, description="[Optional] A predisposing condition is a condition existing within an organization, a mission or business process, enterprise architecture, information system/PIT, or environment of operation, which affects (i.e., increases or decreases) the likelihood that threat events, once initiated, result in adverse impacts. Navy only.", alias="predisposingConditions")
    threat_description: Optional[StrictStr] = Field(default=None, description="[Optional] Describe the identified threat(s) and relevance to the information system. Navy only.", alias="threatDescription")
    devices_affected: Optional[StrictStr] = Field(default=None, description="[Optional] List any affected devices by hostname. If all devices in the information system are affected, state 'system' or 'all'. Navy only", alias="devicesAffected")
    identified_in_cfo_audit_or_other_review: Optional[StrictBool] = Field(default=None, description="[Required] If not specified, this field will be set to false because it does not accept a null value. VA only", alias="identifiedInCFOAuditOrOtherReview")
    personnel_resources_funded_base_hours: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="[Conditional] At least one of the following is required and must be completed for each POA&M Item:   Personnel Resources-> Funded Base Hours   Personnel Resources-> Unfunded Base Hours   Non-Personnel Resources-> Funded Amount   Non-Personnel Resources-> Unfunded Amount Displays numbers to the second decimal point (e.g., 100.00). VA only. ", alias="personnelResourcesFundedBaseHours")
    personnel_resources_cost_code: Optional[StrictStr] = Field(default=None, description="[Conditional] Required if Personnel Resources: Funded Base Hours is populated. Only accepts values present in the field's lookup table (modifiable by eMASS System Admins). VA only. ", alias="personnelResourcesCostCode")
    personnel_resources_unfunded_base_hours: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="[Conditional] At least one of the following is required and must be completed for each POA&M Item:   Personnel Resources-> Funded Base Hours   Personnel Resources-> Unfunded Base Hours   Non-Personnel Resources-> Funded Amount   Non-Personnel Resources-> Unfunded Amount Displays numbers to the second decimal point (e.g., 100.00). VA only. ", alias="personnelResourcesUnfundedBaseHours")
    personnel_resources_nonfunding_obstacle: Optional[StrictStr] = Field(default=None, description="[Conditional] Required if Personnel Resources: Unfunded Base Hours is populated. Only accepts values present in the field's lookup table (modifiable by eMASS System Admins). VA only. ", alias="personnelResourcesNonfundingObstacle")
    personnel_resources_nonfunding_obstacle_other_reason: Optional[StrictStr] = Field(default=None, description="[Conditional] Required if the value \"Other\" is populated for the field Personnel Resources: Non-Funding Obstacle. VA only.", alias="personnelResourcesNonfundingObstacleOtherReason")
    non_personnel_resources_funded_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="[Conditional] At least one of the following is required and must be completed for each POA&M Item:   Personnel Resources-> Funded Base Hours   Personnel Resources-> Unfunded Base Hours   Non-Personnel Resources-> Funded Amount   Non-Personnel Resources-> Unfunded Amount Displays numbers to the second decimal point (e.g., 100.00). VA only. ", alias="nonPersonnelResourcesFundedAmount")
    non_personnel_resources_cost_code: Optional[StrictStr] = Field(default=None, description="[Conditional] Required if Non-Personnel Resources: Funded Amount is populated. Only accepts values present in the field's lookup table (modifiable by eMASS System Admins). VA only. ", alias="nonPersonnelResourcesCostCode")
    non_personnel_resources_unfunded_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="[Conditional] At least one of the following is required and must be completed for each POA&M Item:   Personnel Resources-> Funded Base Hours   Personnel Resources-> Unfunded Base Hours   Non-Personnel Resources-> Funded Amount   Non-Personnel Resources-> Unfunded Amount Displays numbers to the second decimal point (e.g., 100.00). VA only. ", alias="nonPersonnelResourcesUnfundedAmount")
    non_personnel_resources_nonfunding_obstacle: Optional[StrictStr] = Field(default=None, description="[Conditional] Required if Non-Personnel Resources: Unfunded Amount is populated. Only accepts values present in the field's lookup table (modifiable by eMASS System Admins). VA only. ", alias="nonPersonnelResourcesNonfundingObstacle")
    non_personnel_resources_nonfunding_obstacle_other_reason: Optional[StrictStr] = Field(default=None, description="[Conditional] Required if the value \"Other\" is populated for the field Non-Personnel Resources: Non-Funding Obstacle. VA only.", alias="nonPersonnelResourcesNonfundingObstacleOtherReason")
    __properties: ClassVar[List[str]] = ["systemId", "poamId", "displayPoamId", "isInherited", "externalUid", "controlAcronym", "cci", "assessmentProcedure", "status", "reviewStatus", "vulnerabilityDescription", "sourceIdentVuln", "securityChecks", "milestones", "pocOrganization", "pocFirstName", "pocLastName", "pocEmail", "pocPhoneNumber", "severity", "rawSeverity", "relevanceOfThreat", "likelihood", "impact", "impactDescription", "residualRiskLevel", "recommendations", "resources", "scheduledCompletionDate", "completionDate", "extensionDate", "comments", "mitigation", "isActive", "resultingResidualRiskLevelAfterProposedMitigations", "predisposingConditions", "threatDescription", "devicesAffected", "identifiedInCFOAuditOrOtherReview", "personnelResourcesFundedBaseHours", "personnelResourcesCostCode", "personnelResourcesUnfundedBaseHours", "personnelResourcesNonfundingObstacle", "personnelResourcesNonfundingObstacleOtherReason", "nonPersonnelResourcesFundedAmount", "nonPersonnelResourcesCostCode", "nonPersonnelResourcesUnfundedAmount", "nonPersonnelResourcesNonfundingObstacle", "nonPersonnelResourcesNonfundingObstacleOtherReason"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Ongoing', 'Risk Accepted', 'Completed', 'Not Applicable', 'Archived'):
            raise ValueError("must be one of enum values ('Ongoing', 'Risk Accepted', 'Completed', 'Not Applicable', 'Archived')")
        return value

    @field_validator('review_status')
    def review_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Not Approved', 'Under Review', 'Approved'):
            raise ValueError("must be one of enum values ('Not Approved', 'Under Review', 'Approved')")
        return value

    @field_validator('severity')
    def severity_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Very Low', 'Low', 'Moderate', 'High', 'Very High'):
            raise ValueError("must be one of enum values ('Very Low', 'Low', 'Moderate', 'High', 'Very High')")
        return value

    @field_validator('raw_severity')
    def raw_severity_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('I', 'II', 'III'):
            raise ValueError("must be one of enum values ('I', 'II', 'III')")
        return value

    @field_validator('relevance_of_threat')
    def relevance_of_threat_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Very Low', 'Low', 'Moderate', 'High', 'Very High'):
            raise ValueError("must be one of enum values ('Very Low', 'Low', 'Moderate', 'High', 'Very High')")
        return value

    @field_validator('likelihood')
    def likelihood_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Very Low', 'Low', 'Moderate', 'High', 'Very High'):
            raise ValueError("must be one of enum values ('Very Low', 'Low', 'Moderate', 'High', 'Very High')")
        return value

    @field_validator('impact')
    def impact_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Very Low', 'Low', 'Moderate', 'High', 'Very High'):
            raise ValueError("must be one of enum values ('Very Low', 'Low', 'Moderate', 'High', 'Very High')")
        return value

    @field_validator('residual_risk_level')
    def residual_risk_level_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Very Low', 'Low', 'Moderate', 'High', 'Very High'):
            raise ValueError("must be one of enum values ('Very Low', 'Low', 'Moderate', 'High', 'Very High')")
        return value

    @field_validator('resulting_residual_risk_level_after_proposed_mitigations')
    def resulting_residual_risk_level_after_proposed_mitigations_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Very Low', 'Low', 'Moderate', 'High', 'Very High'):
            raise ValueError("must be one of enum values ('Very Low', 'Low', 'Moderate', 'High', 'Very High')")
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
        """Create an instance of PoamGet from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in milestones (list)
        _items = []
        if self.milestones:
            for _item in self.milestones:
                if _item:
                    _items.append(_item.to_dict())
            _dict['milestones'] = _items
        # set to None if is_inherited (nullable) is None
        # and model_fields_set contains the field
        if self.is_inherited is None and "is_inherited" in self.model_fields_set:
            _dict['isInherited'] = None

        # set to None if external_uid (nullable) is None
        # and model_fields_set contains the field
        if self.external_uid is None and "external_uid" in self.model_fields_set:
            _dict['externalUid'] = None

        # set to None if control_acronym (nullable) is None
        # and model_fields_set contains the field
        if self.control_acronym is None and "control_acronym" in self.model_fields_set:
            _dict['controlAcronym'] = None

        # set to None if cci (nullable) is None
        # and model_fields_set contains the field
        if self.cci is None and "cci" in self.model_fields_set:
            _dict['cci'] = None

        # set to None if review_status (nullable) is None
        # and model_fields_set contains the field
        if self.review_status is None and "review_status" in self.model_fields_set:
            _dict['reviewStatus'] = None

        # set to None if security_checks (nullable) is None
        # and model_fields_set contains the field
        if self.security_checks is None and "security_checks" in self.model_fields_set:
            _dict['securityChecks'] = None

        # set to None if poc_first_name (nullable) is None
        # and model_fields_set contains the field
        if self.poc_first_name is None and "poc_first_name" in self.model_fields_set:
            _dict['pocFirstName'] = None

        # set to None if poc_last_name (nullable) is None
        # and model_fields_set contains the field
        if self.poc_last_name is None and "poc_last_name" in self.model_fields_set:
            _dict['pocLastName'] = None

        # set to None if poc_email (nullable) is None
        # and model_fields_set contains the field
        if self.poc_email is None and "poc_email" in self.model_fields_set:
            _dict['pocEmail'] = None

        # set to None if poc_phone_number (nullable) is None
        # and model_fields_set contains the field
        if self.poc_phone_number is None and "poc_phone_number" in self.model_fields_set:
            _dict['pocPhoneNumber'] = None

        # set to None if severity (nullable) is None
        # and model_fields_set contains the field
        if self.severity is None and "severity" in self.model_fields_set:
            _dict['severity'] = None

        # set to None if raw_severity (nullable) is None
        # and model_fields_set contains the field
        if self.raw_severity is None and "raw_severity" in self.model_fields_set:
            _dict['rawSeverity'] = None

        # set to None if relevance_of_threat (nullable) is None
        # and model_fields_set contains the field
        if self.relevance_of_threat is None and "relevance_of_threat" in self.model_fields_set:
            _dict['relevanceOfThreat'] = None

        # set to None if likelihood (nullable) is None
        # and model_fields_set contains the field
        if self.likelihood is None and "likelihood" in self.model_fields_set:
            _dict['likelihood'] = None

        # set to None if impact (nullable) is None
        # and model_fields_set contains the field
        if self.impact is None and "impact" in self.model_fields_set:
            _dict['impact'] = None

        # set to None if impact_description (nullable) is None
        # and model_fields_set contains the field
        if self.impact_description is None and "impact_description" in self.model_fields_set:
            _dict['impactDescription'] = None

        # set to None if residual_risk_level (nullable) is None
        # and model_fields_set contains the field
        if self.residual_risk_level is None and "residual_risk_level" in self.model_fields_set:
            _dict['residualRiskLevel'] = None

        # set to None if recommendations (nullable) is None
        # and model_fields_set contains the field
        if self.recommendations is None and "recommendations" in self.model_fields_set:
            _dict['recommendations'] = None

        # set to None if scheduled_completion_date (nullable) is None
        # and model_fields_set contains the field
        if self.scheduled_completion_date is None and "scheduled_completion_date" in self.model_fields_set:
            _dict['scheduledCompletionDate'] = None

        # set to None if completion_date (nullable) is None
        # and model_fields_set contains the field
        if self.completion_date is None and "completion_date" in self.model_fields_set:
            _dict['completionDate'] = None

        # set to None if extension_date (nullable) is None
        # and model_fields_set contains the field
        if self.extension_date is None and "extension_date" in self.model_fields_set:
            _dict['extensionDate'] = None

        # set to None if comments (nullable) is None
        # and model_fields_set contains the field
        if self.comments is None and "comments" in self.model_fields_set:
            _dict['comments'] = None

        # set to None if mitigation (nullable) is None
        # and model_fields_set contains the field
        if self.mitigation is None and "mitigation" in self.model_fields_set:
            _dict['mitigation'] = None

        # set to None if is_active (nullable) is None
        # and model_fields_set contains the field
        if self.is_active is None and "is_active" in self.model_fields_set:
            _dict['isActive'] = None

        # set to None if resulting_residual_risk_level_after_proposed_mitigations (nullable) is None
        # and model_fields_set contains the field
        if self.resulting_residual_risk_level_after_proposed_mitigations is None and "resulting_residual_risk_level_after_proposed_mitigations" in self.model_fields_set:
            _dict['resultingResidualRiskLevelAfterProposedMitigations'] = None

        # set to None if predisposing_conditions (nullable) is None
        # and model_fields_set contains the field
        if self.predisposing_conditions is None and "predisposing_conditions" in self.model_fields_set:
            _dict['predisposingConditions'] = None

        # set to None if threat_description (nullable) is None
        # and model_fields_set contains the field
        if self.threat_description is None and "threat_description" in self.model_fields_set:
            _dict['threatDescription'] = None

        # set to None if devices_affected (nullable) is None
        # and model_fields_set contains the field
        if self.devices_affected is None and "devices_affected" in self.model_fields_set:
            _dict['devicesAffected'] = None

        # set to None if personnel_resources_funded_base_hours (nullable) is None
        # and model_fields_set contains the field
        if self.personnel_resources_funded_base_hours is None and "personnel_resources_funded_base_hours" in self.model_fields_set:
            _dict['personnelResourcesFundedBaseHours'] = None

        # set to None if personnel_resources_cost_code (nullable) is None
        # and model_fields_set contains the field
        if self.personnel_resources_cost_code is None and "personnel_resources_cost_code" in self.model_fields_set:
            _dict['personnelResourcesCostCode'] = None

        # set to None if personnel_resources_unfunded_base_hours (nullable) is None
        # and model_fields_set contains the field
        if self.personnel_resources_unfunded_base_hours is None and "personnel_resources_unfunded_base_hours" in self.model_fields_set:
            _dict['personnelResourcesUnfundedBaseHours'] = None

        # set to None if personnel_resources_nonfunding_obstacle (nullable) is None
        # and model_fields_set contains the field
        if self.personnel_resources_nonfunding_obstacle is None and "personnel_resources_nonfunding_obstacle" in self.model_fields_set:
            _dict['personnelResourcesNonfundingObstacle'] = None

        # set to None if personnel_resources_nonfunding_obstacle_other_reason (nullable) is None
        # and model_fields_set contains the field
        if self.personnel_resources_nonfunding_obstacle_other_reason is None and "personnel_resources_nonfunding_obstacle_other_reason" in self.model_fields_set:
            _dict['personnelResourcesNonfundingObstacleOtherReason'] = None

        # set to None if non_personnel_resources_funded_amount (nullable) is None
        # and model_fields_set contains the field
        if self.non_personnel_resources_funded_amount is None and "non_personnel_resources_funded_amount" in self.model_fields_set:
            _dict['nonPersonnelResourcesFundedAmount'] = None

        # set to None if non_personnel_resources_cost_code (nullable) is None
        # and model_fields_set contains the field
        if self.non_personnel_resources_cost_code is None and "non_personnel_resources_cost_code" in self.model_fields_set:
            _dict['nonPersonnelResourcesCostCode'] = None

        # set to None if non_personnel_resources_unfunded_amount (nullable) is None
        # and model_fields_set contains the field
        if self.non_personnel_resources_unfunded_amount is None and "non_personnel_resources_unfunded_amount" in self.model_fields_set:
            _dict['nonPersonnelResourcesUnfundedAmount'] = None

        # set to None if non_personnel_resources_nonfunding_obstacle (nullable) is None
        # and model_fields_set contains the field
        if self.non_personnel_resources_nonfunding_obstacle is None and "non_personnel_resources_nonfunding_obstacle" in self.model_fields_set:
            _dict['nonPersonnelResourcesNonfundingObstacle'] = None

        # set to None if non_personnel_resources_nonfunding_obstacle_other_reason (nullable) is None
        # and model_fields_set contains the field
        if self.non_personnel_resources_nonfunding_obstacle_other_reason is None and "non_personnel_resources_nonfunding_obstacle_other_reason" in self.model_fields_set:
            _dict['nonPersonnelResourcesNonfundingObstacleOtherReason'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        """Create an instance of PoamGet from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "systemId": obj.get("systemId"),
            "poamId": obj.get("poamId"),
            "displayPoamId": obj.get("displayPoamId"),
            "isInherited": obj.get("isInherited"),
            "externalUid": obj.get("externalUid"),
            "controlAcronym": obj.get("controlAcronym"),
            "cci": obj.get("cci"),
            "assessmentProcedure": obj.get("assessmentProcedure"),
            "status": obj.get("status"),
            "reviewStatus": obj.get("reviewStatus"),
            "vulnerabilityDescription": obj.get("vulnerabilityDescription"),
            "sourceIdentVuln": obj.get("sourceIdentVuln"),
            "securityChecks": obj.get("securityChecks"),
            "milestones": [MilestonesGet.from_dict(_item) for _item in obj.get("milestones")] if obj.get("milestones") is not None else None,
            "pocOrganization": obj.get("pocOrganization"),
            "pocFirstName": obj.get("pocFirstName"),
            "pocLastName": obj.get("pocLastName"),
            "pocEmail": obj.get("pocEmail"),
            "pocPhoneNumber": obj.get("pocPhoneNumber"),
            "severity": obj.get("severity"),
            "rawSeverity": obj.get("rawSeverity"),
            "relevanceOfThreat": obj.get("relevanceOfThreat"),
            "likelihood": obj.get("likelihood"),
            "impact": obj.get("impact"),
            "impactDescription": obj.get("impactDescription"),
            "residualRiskLevel": obj.get("residualRiskLevel"),
            "recommendations": obj.get("recommendations"),
            "resources": obj.get("resources"),
            "scheduledCompletionDate": obj.get("scheduledCompletionDate"),
            "completionDate": obj.get("completionDate"),
            "extensionDate": obj.get("extensionDate"),
            "comments": obj.get("comments"),
            "mitigation": obj.get("mitigation"),
            "isActive": obj.get("isActive"),
            "resultingResidualRiskLevelAfterProposedMitigations": obj.get("resultingResidualRiskLevelAfterProposedMitigations"),
            "predisposingConditions": obj.get("predisposingConditions"),
            "threatDescription": obj.get("threatDescription"),
            "devicesAffected": obj.get("devicesAffected"),
            "identifiedInCFOAuditOrOtherReview": obj.get("identifiedInCFOAuditOrOtherReview"),
            "personnelResourcesFundedBaseHours": obj.get("personnelResourcesFundedBaseHours"),
            "personnelResourcesCostCode": obj.get("personnelResourcesCostCode"),
            "personnelResourcesUnfundedBaseHours": obj.get("personnelResourcesUnfundedBaseHours"),
            "personnelResourcesNonfundingObstacle": obj.get("personnelResourcesNonfundingObstacle"),
            "personnelResourcesNonfundingObstacleOtherReason": obj.get("personnelResourcesNonfundingObstacleOtherReason"),
            "nonPersonnelResourcesFundedAmount": obj.get("nonPersonnelResourcesFundedAmount"),
            "nonPersonnelResourcesCostCode": obj.get("nonPersonnelResourcesCostCode"),
            "nonPersonnelResourcesUnfundedAmount": obj.get("nonPersonnelResourcesUnfundedAmount"),
            "nonPersonnelResourcesNonfundingObstacle": obj.get("nonPersonnelResourcesNonfundingObstacle"),
            "nonPersonnelResourcesNonfundingObstacleOtherReason": obj.get("nonPersonnelResourcesNonfundingObstacleOtherReason")
        })
        return _obj


