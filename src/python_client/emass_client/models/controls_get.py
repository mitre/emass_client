# coding: utf-8

### eMASS API v3.12 Specification
#The emass_client_api is a Python client that implements the [Enterprise Mission Assurance Support Service (eMASS)](https://disa.mil/~/media/Files/DISA/Fact-Sheets/eMASS.pdf)Representational State Transfer (REST) Application Programming Interface (API) specifications.


#This Python package was generated from the eMASS API specification:
#- API version: v3.12- Package version: 3.12.0
#- Build date: 2023-10-10T14:36:02.975730Z[Etc/UTC]
### Requirements.
#Python 
### Installation & Usage### pip install

#If the python package is hosted on a repository, you can install directly using:
#```shpip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
#```(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

#Then import the package:```python
#import emass_client#```
#### Setuptools
#Install via [Setuptools](http://pypi.python.org/pypi/setuptools).
#```shpython setup.py install --user
#```(or `sudo python setup.py install` to install the package for all users)

#Then import the package:```python
#import emass_client#```
#### Tests
#Execute `pytest` to run the tests.
from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr, field_validator
from pydantic import Field
from typing import Dict, Any
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ControlsGet(BaseModel):
    """
    ControlsGet
    """
    system_id: Optional[StrictInt] = Field(default=None, description="[Required] Unique system record identifier.", alias="systemId")
    name: Optional[StrictStr] = Field(default=None, description="[Read-only] Name of the system record.")
    acronym: Optional[StrictStr] = Field(default=None, description="[Required] Acronym of the system record.")
    ccis: Optional[StrictStr] = Field(default=None, description="[Read-only] Comma separated list of CCIs associated with the control.")
    is_inherited: Optional[StrictBool] = Field(default=None, description="[Read-only] Indicates whether a control is inherited.", alias="isInherited")
    modified_by_overlays: Optional[StrictStr] = Field(default=None, description="[Read-only] List of overlays that affect the control.", alias="modifiedByOverlays")
    included_status: Optional[StrictStr] = Field(default=None, description="[Read-only] Indicates the manner by which a control was included in the system's categorization.", alias="includedStatus")
    compliance_status: Optional[StrictStr] = Field(default=None, description="[Read-only] Compliance of the control.", alias="complianceStatus")
    responsible_entities: Optional[StrictStr] = Field(default=None, description="[Required] Include written description of Responsible Entities that are responsible for the Security Control. Character Limit = 2,000.", alias="responsibleEntities")
    implementation_status: Optional[StrictStr] = Field(default=None, description="[Optional] Implementation Status of the Security Control for the information system.", alias="implementationStatus")
    common_control_provider: Optional[StrictStr] = Field(default=None, description="[Conditional] Indicate the type of Common Control Provider for an “Inherited” Security Control.", alias="commonControlProvider")
    na_justification: Optional[StrictStr] = Field(default=None, description="[Conditional] Provide justification for Security Controls deemed Not Applicable to the system.", alias="naJustification")
    control_designation: Optional[StrictStr] = Field(default=None, description="[Required] Control designations", alias="controlDesignation")
    estimated_completion_date: Optional[StrictInt] = Field(default=None, description="[Required] Field is required for Implementation Plan.", alias="estimatedCompletionDate")
    implementation_narrative: Optional[StrictStr] = Field(default=None, description="[Required] Includes security control comments. Character Limit = 2,000.", alias="implementationNarrative")
    slcm_criticality: Optional[StrictStr] = Field(default=None, description="[Conditional] Criticality of Security Control regarding SLCM. Character Limit = 2,000.", alias="slcmCriticality")
    slcm_frequency: Optional[StrictStr] = Field(default=None, description="[Conditional] SLCM frequency", alias="slcmFrequency")
    slcm_method: Optional[StrictStr] = Field(default=None, description="[Conditional] SLCM method utilized", alias="slcmMethod")
    slcm_reporting: Optional[StrictStr] = Field(default=None, description="[Conditional] Method for reporting Security Control for SLCM. Character Limit = 2,000.", alias="slcmReporting")
    slcm_tracking: Optional[StrictStr] = Field(default=None, description="[Conditional] How Non-Compliant Security Controls will be tracked for SLCM. Character Limit = 2,000.", alias="slcmTracking")
    slcm_comments: Optional[StrictStr] = Field(default=None, description="[Conditional] Additional comments for Security Control regarding SLCM. Character Limit = 4,000.", alias="slcmComments")
    severity: Optional[StrictStr] = Field(default=None, description="[Optional] Values include the following options (Very Low, Low, Moderate,High,Very High)")
    vulnerabilty_summary: Optional[StrictStr] = Field(default=None, description="[Optional] Include vulnerability summary. Character Limit = 2,000.", alias="vulnerabiltySummary")
    recommendations: Optional[StrictStr] = Field(default=None, description="[Optional] Include recommendations. Character Limit = 2,000.")
    relevance_of_threat: Optional[StrictStr] = Field(default=None, description="[Optional] Values include the following options (Very Low, Low, Moderate,High,Very High)", alias="relevanceOfThreat")
    likelihood: Optional[StrictStr] = Field(default=None, description="[Optional] Values include the following options (Very Low, Low, Moderate,High,Very High)")
    impact: Optional[StrictStr] = Field(default=None, description="[Optional] Values include the following options (Very Low, Low, Moderate,High,Very High)")
    impact_description: Optional[StrictStr] = Field(default=None, description="[Optional] Include description of Security Control's impact.", alias="impactDescription")
    residual_risk_level: Optional[StrictStr] = Field(default=None, description="[Optional] Values include the following options (Very Low, Low, Moderate,High,Very High)", alias="residualRiskLevel")
    test_method: Optional[StrictStr] = Field(default=None, description="[Optional] Identifies the assessment method / combination that will determine if the security requirements are implemented correctly.", alias="testMethod")
    mitigations: Optional[StrictStr] = Field(default=None, description="[Optional] Identify any mitigations in place for the Non-Compliant Security Control's vulnerabilities. Character Limit = 2,000.")
    application_layer: Optional[StrictStr] = Field(default=None, description="[Optional] If the Financial Management (Navy) overlay is applied to the system, this field appears and can be populated. Character Limit = 2,000. Navy only.", alias="applicationLayer")
    database_layer: Optional[StrictStr] = Field(default=None, description="[Read-Only] Identify the primary computing environment for where the information system is deployed. Navy only.", alias="databaseLayer")
    operating_system_layer: Optional[StrictStr] = Field(default=None, description="[Read-Only] Identify the primary computing environment for where the information system is deployed. Navy only.", alias="operatingSystemLayer")
    __properties: ClassVar[List[str]] = ["systemId", "name", "acronym", "ccis", "isInherited", "modifiedByOverlays", "includedStatus", "complianceStatus", "responsibleEntities", "implementationStatus", "commonControlProvider", "naJustification", "controlDesignation", "estimatedCompletionDate", "implementationNarrative", "slcmCriticality", "slcmFrequency", "slcmMethod", "slcmReporting", "slcmTracking", "slcmComments", "severity", "vulnerabiltySummary", "recommendations", "relevanceOfThreat", "likelihood", "impact", "impactDescription", "residualRiskLevel", "testMethod", "mitigations", "applicationLayer", "databaseLayer", "operatingSystemLayer"]

    @field_validator('implementation_status')
    def implementation_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Planned', 'Implemented', 'Inherited', 'Not Applicable', 'Manually Inherited'):
            raise ValueError("must be one of enum values ('Planned', 'Implemented', 'Inherited', 'Not Applicable', 'Manually Inherited')")
        return value

    @field_validator('common_control_provider')
    def common_control_provider_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('DoD', 'Component', 'Enclave'):
            raise ValueError("must be one of enum values ('DoD', 'Component', 'Enclave')")
        return value

    @field_validator('control_designation')
    def control_designation_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Common', 'System-Specific', 'Hybrid'):
            raise ValueError("must be one of enum values ('Common', 'System-Specific', 'Hybrid')")
        return value

    @field_validator('slcm_frequency')
    def slcm_frequency_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Constantly', 'Daily', 'Weekly', 'Monthly', 'Quarterly', 'Semi-Annually', 'Annually', 'Every Two Years', 'Every Three Years', 'Undetermined'):
            raise ValueError("must be one of enum values ('Constantly', 'Daily', 'Weekly', 'Monthly', 'Quarterly', 'Semi-Annually', 'Annually', 'Every Two Years', 'Every Three Years', 'Undetermined')")
        return value

    @field_validator('slcm_method')
    def slcm_method_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Automated', 'Semi-Automated', 'Manual', 'Undetermined'):
            raise ValueError("must be one of enum values ('Automated', 'Semi-Automated', 'Manual', 'Undetermined')")
        return value

    @field_validator('severity')
    def severity_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Very Low', 'Low', 'Moderate', 'High', 'Very High'):
            raise ValueError("must be one of enum values ('Very Low', 'Low', 'Moderate', 'High', 'Very High')")
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

    @field_validator('test_method')
    def test_method_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Test', 'Interview', 'Examine', 'Test, Interview', 'Test, Examine', 'Interview, Examine', 'Test, Interview, Examine'):
            raise ValueError("must be one of enum values ('Test', 'Interview', 'Examine', 'Test, Interview', 'Test, Examine', 'Interview, Examine', 'Test, Interview, Examine')")
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
        """Create an instance of ControlsGet from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if ccis (nullable) is None
        # and model_fields_set contains the field
        if self.ccis is None and "ccis" in self.model_fields_set:
            _dict['ccis'] = None

        # set to None if is_inherited (nullable) is None
        # and model_fields_set contains the field
        if self.is_inherited is None and "is_inherited" in self.model_fields_set:
            _dict['isInherited'] = None

        # set to None if modified_by_overlays (nullable) is None
        # and model_fields_set contains the field
        if self.modified_by_overlays is None and "modified_by_overlays" in self.model_fields_set:
            _dict['modifiedByOverlays'] = None

        # set to None if included_status (nullable) is None
        # and model_fields_set contains the field
        if self.included_status is None and "included_status" in self.model_fields_set:
            _dict['includedStatus'] = None

        # set to None if compliance_status (nullable) is None
        # and model_fields_set contains the field
        if self.compliance_status is None and "compliance_status" in self.model_fields_set:
            _dict['complianceStatus'] = None

        # set to None if implementation_status (nullable) is None
        # and model_fields_set contains the field
        if self.implementation_status is None and "implementation_status" in self.model_fields_set:
            _dict['implementationStatus'] = None

        # set to None if common_control_provider (nullable) is None
        # and model_fields_set contains the field
        if self.common_control_provider is None and "common_control_provider" in self.model_fields_set:
            _dict['commonControlProvider'] = None

        # set to None if na_justification (nullable) is None
        # and model_fields_set contains the field
        if self.na_justification is None and "na_justification" in self.model_fields_set:
            _dict['naJustification'] = None

        # set to None if slcm_criticality (nullable) is None
        # and model_fields_set contains the field
        if self.slcm_criticality is None and "slcm_criticality" in self.model_fields_set:
            _dict['slcmCriticality'] = None

        # set to None if slcm_frequency (nullable) is None
        # and model_fields_set contains the field
        if self.slcm_frequency is None and "slcm_frequency" in self.model_fields_set:
            _dict['slcmFrequency'] = None

        # set to None if slcm_method (nullable) is None
        # and model_fields_set contains the field
        if self.slcm_method is None and "slcm_method" in self.model_fields_set:
            _dict['slcmMethod'] = None

        # set to None if slcm_reporting (nullable) is None
        # and model_fields_set contains the field
        if self.slcm_reporting is None and "slcm_reporting" in self.model_fields_set:
            _dict['slcmReporting'] = None

        # set to None if slcm_tracking (nullable) is None
        # and model_fields_set contains the field
        if self.slcm_tracking is None and "slcm_tracking" in self.model_fields_set:
            _dict['slcmTracking'] = None

        # set to None if slcm_comments (nullable) is None
        # and model_fields_set contains the field
        if self.slcm_comments is None and "slcm_comments" in self.model_fields_set:
            _dict['slcmComments'] = None

        # set to None if severity (nullable) is None
        # and model_fields_set contains the field
        if self.severity is None and "severity" in self.model_fields_set:
            _dict['severity'] = None

        # set to None if vulnerabilty_summary (nullable) is None
        # and model_fields_set contains the field
        if self.vulnerabilty_summary is None and "vulnerabilty_summary" in self.model_fields_set:
            _dict['vulnerabiltySummary'] = None

        # set to None if recommendations (nullable) is None
        # and model_fields_set contains the field
        if self.recommendations is None and "recommendations" in self.model_fields_set:
            _dict['recommendations'] = None

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

        # set to None if test_method (nullable) is None
        # and model_fields_set contains the field
        if self.test_method is None and "test_method" in self.model_fields_set:
            _dict['testMethod'] = None

        # set to None if mitigations (nullable) is None
        # and model_fields_set contains the field
        if self.mitigations is None and "mitigations" in self.model_fields_set:
            _dict['mitigations'] = None

        # set to None if application_layer (nullable) is None
        # and model_fields_set contains the field
        if self.application_layer is None and "application_layer" in self.model_fields_set:
            _dict['applicationLayer'] = None

        # set to None if database_layer (nullable) is None
        # and model_fields_set contains the field
        if self.database_layer is None and "database_layer" in self.model_fields_set:
            _dict['databaseLayer'] = None

        # set to None if operating_system_layer (nullable) is None
        # and model_fields_set contains the field
        if self.operating_system_layer is None and "operating_system_layer" in self.model_fields_set:
            _dict['operatingSystemLayer'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        """Create an instance of ControlsGet from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "systemId": obj.get("systemId"),
            "name": obj.get("name"),
            "acronym": obj.get("acronym"),
            "ccis": obj.get("ccis"),
            "isInherited": obj.get("isInherited"),
            "modifiedByOverlays": obj.get("modifiedByOverlays"),
            "includedStatus": obj.get("includedStatus"),
            "complianceStatus": obj.get("complianceStatus"),
            "responsibleEntities": obj.get("responsibleEntities"),
            "implementationStatus": obj.get("implementationStatus"),
            "commonControlProvider": obj.get("commonControlProvider"),
            "naJustification": obj.get("naJustification"),
            "controlDesignation": obj.get("controlDesignation"),
            "estimatedCompletionDate": obj.get("estimatedCompletionDate"),
            "implementationNarrative": obj.get("implementationNarrative"),
            "slcmCriticality": obj.get("slcmCriticality"),
            "slcmFrequency": obj.get("slcmFrequency"),
            "slcmMethod": obj.get("slcmMethod"),
            "slcmReporting": obj.get("slcmReporting"),
            "slcmTracking": obj.get("slcmTracking"),
            "slcmComments": obj.get("slcmComments"),
            "severity": obj.get("severity"),
            "vulnerabiltySummary": obj.get("vulnerabiltySummary"),
            "recommendations": obj.get("recommendations"),
            "relevanceOfThreat": obj.get("relevanceOfThreat"),
            "likelihood": obj.get("likelihood"),
            "impact": obj.get("impact"),
            "impactDescription": obj.get("impactDescription"),
            "residualRiskLevel": obj.get("residualRiskLevel"),
            "testMethod": obj.get("testMethod"),
            "mitigations": obj.get("mitigations"),
            "applicationLayer": obj.get("applicationLayer"),
            "databaseLayer": obj.get("databaseLayer"),
            "operatingSystemLayer": obj.get("operatingSystemLayer")
        })
        return _obj


