# coding: utf-8

## eMASS API v3.9 Specification

The emass_client_api is a Python client that implements the [Enterprise Mission Assurance Support Service (eMASS)](https://disa.mil/~/media/Files/DISA/Fact-Sheets/eMASS.pdf)
Representational State Transfer (REST) Application Programming Interface (API) specifications.


This Python package was generated from the eMASS API specification:

- API version: v3.9
- Package version: 3.9.1
- Build date: 2023-05-23T01:07:18.461999Z[Etc/UTC]

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


from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, validator

class ControlsGet(BaseModel):
    """
    ControlsGet
    """
    system_id: Optional[StrictInt] = Field(None, alias="systemId", description="[Required] Unique system record identifier.")
    name: Optional[StrictStr] = Field(None, description="[Read-only] Name of the system record.")
    acronym: Optional[StrictStr] = Field(None, description="[Required] Acronym of the system record.")
    ccis: Optional[StrictStr] = Field(None, description="[Read-only] Comma separated list of CCIs associated with the control.")
    is_inherited: Optional[StrictBool] = Field(None, alias="isInherited", description="[Read-only] Indicates whether a control is inherited.")
    modified_by_overlays: Optional[StrictStr] = Field(None, alias="modifiedByOverlays", description="[Read-only] List of overlays that affect the control.")
    included_status: Optional[StrictStr] = Field(None, alias="includedStatus", description="[Read-only] Indicates the manner by which a control was included in the system’s categorization.")
    compliance_status: Optional[StrictStr] = Field(None, alias="complianceStatus", description="[Read-only] Compliance of the control.")
    responsible_entities: Optional[StrictStr] = Field(None, alias="responsibleEntities", description="[Required] Include written description of Responsible Entities that are responsible for the Security Control. Character Limit = 2,000.")
    implementation_status: Optional[StrictStr] = Field(None, alias="implementationStatus", description="[Optional] Implementation Status of the Security Control for the information system.")
    common_control_provider: Optional[StrictStr] = Field(None, alias="commonControlProvider", description="[Conditional] Indicate the type of Common Control Provider for an “Inherited” Security Control.")
    na_justification: Optional[StrictStr] = Field(None, alias="naJustification", description="[Conditional] Provide justification for Security Controls deemed Not Applicable to the system.")
    control_designation: Optional[StrictStr] = Field(None, alias="controlDesignation", description="[Required] Control designations")
    estimated_completion_date: Optional[StrictInt] = Field(None, alias="estimatedCompletionDate", description="[Required] Field is required for Implementation Plan.")
    implementation_narrative: Optional[StrictStr] = Field(None, alias="implementationNarrative", description="[Required] Includes security control comments. Character Limit = 2,000.")
    slcm_criticality: Optional[StrictStr] = Field(None, alias="slcmCriticality", description="[Conditional] Criticality of Security Control regarding SLCM. Character Limit = 2,000.")
    slcm_frequency: Optional[StrictStr] = Field(None, alias="slcmFrequency", description="[Conditional] SLCM frequency")
    slcm_method: Optional[StrictStr] = Field(None, alias="slcmMethod", description="[Conditional] SLCM method utilized")
    slcm_reporting: Optional[StrictStr] = Field(None, alias="slcmReporting", description="[Conditional] Method for reporting Security Control for SLCM. Character Limit = 2,000.")
    slcm_tracking: Optional[StrictStr] = Field(None, alias="slcmTracking", description="[Conditional] How Non-Compliant Security Controls will be tracked for SLCM. Character Limit = 2,000.")
    slcm_comments: Optional[StrictStr] = Field(None, alias="slcmComments", description="[Conditional] Additional comments for Security Control regarding SLCM. Character Limit = 4,000.")
    severity: Optional[StrictStr] = Field(None, description="[Optional] Values include the following options (Very Low, Low, Moderate,High,Very High)")
    vulnerabilty_summary: Optional[StrictStr] = Field(None, alias="vulnerabiltySummary", description="[Optional] Include vulnerability summary. Character Limit = 2,000.")
    recommendations: Optional[StrictStr] = Field(None, description="[Optional] Include recommendations. Character Limit = 2,000.")
    relevance_of_threat: Optional[StrictStr] = Field(None, alias="relevanceOfThreat", description="[Optional] Values include the following options (Very Low, Low, Moderate,High,Very High)")
    likelihood: Optional[StrictStr] = Field(None, description="[Optional] Values include the following options (Very Low, Low, Moderate,High,Very High)")
    impact: Optional[StrictStr] = Field(None, description="[Optional] Values include the following options (Very Low, Low, Moderate,High,Very High)")
    impact_description: Optional[StrictStr] = Field(None, alias="impactDescription", description="[Optional] Include description of Security Control’s impact.")
    residual_risk_level: Optional[StrictStr] = Field(None, alias="residualRiskLevel", description="[Optional] Values include the following options (Very Low, Low, Moderate,High,Very High)")
    test_method: Optional[StrictStr] = Field(None, alias="testMethod", description="[Optional] Identifies the assessment method / combination that will determine if the security requirements are implemented correctly.")
    __properties = ["systemId", "name", "acronym", "ccis", "isInherited", "modifiedByOverlays", "includedStatus", "complianceStatus", "responsibleEntities", "implementationStatus", "commonControlProvider", "naJustification", "controlDesignation", "estimatedCompletionDate", "implementationNarrative", "slcmCriticality", "slcmFrequency", "slcmMethod", "slcmReporting", "slcmTracking", "slcmComments", "severity", "vulnerabiltySummary", "recommendations", "relevanceOfThreat", "likelihood", "impact", "impactDescription", "residualRiskLevel", "testMethod"]

    @validator('modified_by_overlays')
    def modified_by_overlays_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Privacy', 'Requirements', 'Concurrency'):
            raise ValueError("must be one of enum values ('Privacy', 'Requirements', 'Concurrency')")
        return value

    @validator('implementation_status')
    def implementation_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Planned', 'Implemented', 'Inherited', 'Not Applicable', 'Manually Inherited'):
            raise ValueError("must be one of enum values ('Planned', 'Implemented', 'Inherited', 'Not Applicable', 'Manually Inherited')")
        return value

    @validator('common_control_provider')
    def common_control_provider_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('DoD', 'Component', 'Enclave'):
            raise ValueError("must be one of enum values ('DoD', 'Component', 'Enclave')")
        return value

    @validator('control_designation')
    def control_designation_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Common', 'System-Specific', 'Hybrid'):
            raise ValueError("must be one of enum values ('Common', 'System-Specific', 'Hybrid')")
        return value

    @validator('slcm_frequency')
    def slcm_frequency_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Constantly', 'Daily', 'Weekly', 'Monthly', 'Quarterly', 'Semi-Annually', 'Annually', 'Every Two Years', 'Every Three Years', 'Undetermined'):
            raise ValueError("must be one of enum values ('Constantly', 'Daily', 'Weekly', 'Monthly', 'Quarterly', 'Semi-Annually', 'Annually', 'Every Two Years', 'Every Three Years', 'Undetermined')")
        return value

    @validator('slcm_method')
    def slcm_method_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Automated', 'Semi-Automated', 'Manual', 'Undetermined'):
            raise ValueError("must be one of enum values ('Automated', 'Semi-Automated', 'Manual', 'Undetermined')")
        return value

    @validator('severity')
    def severity_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Very Low', 'Low', 'Moderate', 'High', 'Very High'):
            raise ValueError("must be one of enum values ('Very Low', 'Low', 'Moderate', 'High', 'Very High')")
        return value

    @validator('relevance_of_threat')
    def relevance_of_threat_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Very Low', 'Low', 'Moderate', 'High', 'Very High'):
            raise ValueError("must be one of enum values ('Very Low', 'Low', 'Moderate', 'High', 'Very High')")
        return value

    @validator('likelihood')
    def likelihood_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Very Low', 'Low', 'Moderate', 'High', 'Very High'):
            raise ValueError("must be one of enum values ('Very Low', 'Low', 'Moderate', 'High', 'Very High')")
        return value

    @validator('impact')
    def impact_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Very Low', 'Low', 'Moderate', 'High', 'Very High'):
            raise ValueError("must be one of enum values ('Very Low', 'Low', 'Moderate', 'High', 'Very High')")
        return value

    @validator('residual_risk_level')
    def residual_risk_level_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Very Low', 'Low', 'Moderate', 'High', 'Very High'):
            raise ValueError("must be one of enum values ('Very Low', 'Low', 'Moderate', 'High', 'Very High')")
        return value

    @validator('test_method')
    def test_method_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Test', 'Interview', 'Examine', 'Test, Interview', 'Test, Examine', 'Interview, Examine', 'Test, Interview, Examine'):
            raise ValueError("must be one of enum values ('Test', 'Interview', 'Examine', 'Test, Interview', 'Test, Examine', 'Interview, Examine', 'Test, Interview, Examine')")
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
    def from_json(cls, json_str: str) -> ControlsGet:
        """Create an instance of ControlsGet from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if name (nullable) is None
        # and __fields_set__ contains the field
        if self.name is None and "name" in self.__fields_set__:
            _dict['name'] = None

        # set to None if ccis (nullable) is None
        # and __fields_set__ contains the field
        if self.ccis is None and "ccis" in self.__fields_set__:
            _dict['ccis'] = None

        # set to None if is_inherited (nullable) is None
        # and __fields_set__ contains the field
        if self.is_inherited is None and "is_inherited" in self.__fields_set__:
            _dict['isInherited'] = None

        # set to None if modified_by_overlays (nullable) is None
        # and __fields_set__ contains the field
        if self.modified_by_overlays is None and "modified_by_overlays" in self.__fields_set__:
            _dict['modifiedByOverlays'] = None

        # set to None if included_status (nullable) is None
        # and __fields_set__ contains the field
        if self.included_status is None and "included_status" in self.__fields_set__:
            _dict['includedStatus'] = None

        # set to None if compliance_status (nullable) is None
        # and __fields_set__ contains the field
        if self.compliance_status is None and "compliance_status" in self.__fields_set__:
            _dict['complianceStatus'] = None

        # set to None if implementation_status (nullable) is None
        # and __fields_set__ contains the field
        if self.implementation_status is None and "implementation_status" in self.__fields_set__:
            _dict['implementationStatus'] = None

        # set to None if common_control_provider (nullable) is None
        # and __fields_set__ contains the field
        if self.common_control_provider is None and "common_control_provider" in self.__fields_set__:
            _dict['commonControlProvider'] = None

        # set to None if na_justification (nullable) is None
        # and __fields_set__ contains the field
        if self.na_justification is None and "na_justification" in self.__fields_set__:
            _dict['naJustification'] = None

        # set to None if slcm_criticality (nullable) is None
        # and __fields_set__ contains the field
        if self.slcm_criticality is None and "slcm_criticality" in self.__fields_set__:
            _dict['slcmCriticality'] = None

        # set to None if slcm_frequency (nullable) is None
        # and __fields_set__ contains the field
        if self.slcm_frequency is None and "slcm_frequency" in self.__fields_set__:
            _dict['slcmFrequency'] = None

        # set to None if slcm_method (nullable) is None
        # and __fields_set__ contains the field
        if self.slcm_method is None and "slcm_method" in self.__fields_set__:
            _dict['slcmMethod'] = None

        # set to None if slcm_reporting (nullable) is None
        # and __fields_set__ contains the field
        if self.slcm_reporting is None and "slcm_reporting" in self.__fields_set__:
            _dict['slcmReporting'] = None

        # set to None if slcm_tracking (nullable) is None
        # and __fields_set__ contains the field
        if self.slcm_tracking is None and "slcm_tracking" in self.__fields_set__:
            _dict['slcmTracking'] = None

        # set to None if slcm_comments (nullable) is None
        # and __fields_set__ contains the field
        if self.slcm_comments is None and "slcm_comments" in self.__fields_set__:
            _dict['slcmComments'] = None

        # set to None if severity (nullable) is None
        # and __fields_set__ contains the field
        if self.severity is None and "severity" in self.__fields_set__:
            _dict['severity'] = None

        # set to None if vulnerabilty_summary (nullable) is None
        # and __fields_set__ contains the field
        if self.vulnerabilty_summary is None and "vulnerabilty_summary" in self.__fields_set__:
            _dict['vulnerabiltySummary'] = None

        # set to None if recommendations (nullable) is None
        # and __fields_set__ contains the field
        if self.recommendations is None and "recommendations" in self.__fields_set__:
            _dict['recommendations'] = None

        # set to None if relevance_of_threat (nullable) is None
        # and __fields_set__ contains the field
        if self.relevance_of_threat is None and "relevance_of_threat" in self.__fields_set__:
            _dict['relevanceOfThreat'] = None

        # set to None if likelihood (nullable) is None
        # and __fields_set__ contains the field
        if self.likelihood is None and "likelihood" in self.__fields_set__:
            _dict['likelihood'] = None

        # set to None if impact (nullable) is None
        # and __fields_set__ contains the field
        if self.impact is None and "impact" in self.__fields_set__:
            _dict['impact'] = None

        # set to None if impact_description (nullable) is None
        # and __fields_set__ contains the field
        if self.impact_description is None and "impact_description" in self.__fields_set__:
            _dict['impactDescription'] = None

        # set to None if residual_risk_level (nullable) is None
        # and __fields_set__ contains the field
        if self.residual_risk_level is None and "residual_risk_level" in self.__fields_set__:
            _dict['residualRiskLevel'] = None

        # set to None if test_method (nullable) is None
        # and __fields_set__ contains the field
        if self.test_method is None and "test_method" in self.__fields_set__:
            _dict['testMethod'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ControlsGet:
        """Create an instance of ControlsGet from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ControlsGet.parse_obj(obj)

        _obj = ControlsGet.parse_obj({
            "system_id": obj.get("systemId"),
            "name": obj.get("name"),
            "acronym": obj.get("acronym"),
            "ccis": obj.get("ccis"),
            "is_inherited": obj.get("isInherited"),
            "modified_by_overlays": obj.get("modifiedByOverlays"),
            "included_status": obj.get("includedStatus"),
            "compliance_status": obj.get("complianceStatus"),
            "responsible_entities": obj.get("responsibleEntities"),
            "implementation_status": obj.get("implementationStatus"),
            "common_control_provider": obj.get("commonControlProvider"),
            "na_justification": obj.get("naJustification"),
            "control_designation": obj.get("controlDesignation"),
            "estimated_completion_date": obj.get("estimatedCompletionDate"),
            "implementation_narrative": obj.get("implementationNarrative"),
            "slcm_criticality": obj.get("slcmCriticality"),
            "slcm_frequency": obj.get("slcmFrequency"),
            "slcm_method": obj.get("slcmMethod"),
            "slcm_reporting": obj.get("slcmReporting"),
            "slcm_tracking": obj.get("slcmTracking"),
            "slcm_comments": obj.get("slcmComments"),
            "severity": obj.get("severity"),
            "vulnerabilty_summary": obj.get("vulnerabiltySummary"),
            "recommendations": obj.get("recommendations"),
            "relevance_of_threat": obj.get("relevanceOfThreat"),
            "likelihood": obj.get("likelihood"),
            "impact": obj.get("impact"),
            "impact_description": obj.get("impactDescription"),
            "residual_risk_level": obj.get("residualRiskLevel"),
            "test_method": obj.get("testMethod")
        })
        return _obj

