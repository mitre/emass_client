# coding: utf-8

## eMASS API v3.9 Specification

The emass_client_api is a Python client that implements the [Enterprise Mission Assurance Support Service (eMASS)](https://disa.mil/~/media/Files/DISA/Fact-Sheets/eMASS.pdf)
Representational State Transfer (REST) Application Programming Interface (API) specifications.


This Python package was generated from the eMASS API specification:

- API version: v3.9
- Package version: 3.9.0
- Build date: 2023-05-21T19:48:58.553127800-05:00[America/Chicago]

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

## Getting Started

In your own code, to use this library to connect and interact with emass_client_api,
you can run the following:

```python

import time
import emass_client
from pprint import pprint
```
## Documentation For Authorization

Authentication information is documented in the [emass_client specification GitHub page](https://mitre.github.io/emass_client/docs/redoc/)

## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in emass_client.apis and emass_client.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from emass_client..default_api import DefaultApi`
- `from emass_client.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import emass_client
from emass_client.apis import *
from emass_client.models import *
```
from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from emass_client import schemas  # noqa: F401


class PoamRequestPutBody(
    schemas.ListSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        
        class items(
            schemas.AnyTypeSchema,
        ):
        
        
            class MetaOapg:
                
                class properties:
                    poamId = schemas.Int64Schema
                    displayPoamId = schemas.Int64Schema
                    
                    
                    class status(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "Ongoing": "ONGOING",
                                "Risk Accepted": "RISK_ACCEPTED",
                                "Completed": "COMPLETED",
                                "Not Applicable": "NOT_APPLICABLE",
                            }
                        
                        @schemas.classproperty
                        def ONGOING(cls):
                            return cls("Ongoing")
                        
                        @schemas.classproperty
                        def RISK_ACCEPTED(cls):
                            return cls("Risk Accepted")
                        
                        @schemas.classproperty
                        def COMPLETED(cls):
                            return cls("Completed")
                        
                        @schemas.classproperty
                        def NOT_APPLICABLE(cls):
                            return cls("Not Applicable")
                    vulnerabilityDescription = schemas.StrSchema
                    sourceIdentVuln = schemas.StrSchema
                    pocOrganization = schemas.StrSchema
                    resources = schemas.StrSchema
                    externalUid = schemas.StrSchema
                    controlAcronym = schemas.StrSchema
                    cci = schemas.StrSchema
                    securityChecks = schemas.StrSchema
                    rawSeverity = schemas.StrSchema
                    relevanceOfThreat = schemas.StrSchema
                    likelihood = schemas.StrSchema
                    impact = schemas.StrSchema
                    impactDescription = schemas.StrSchema
                    residualRiskLevel = schemas.StrSchema
                    recommendations = schemas.StrSchema
                    mitigation = schemas.StrSchema
                    pocFirstName = schemas.StrSchema
                    pocLastName = schemas.StrSchema
                    pocEmail = schemas.StrSchema
                    pocPhoneNumber = schemas.StrSchema
                    severity = schemas.StrSchema
                    
                    
                    class scheduledCompletionDate(
                        schemas.Int64Base,
                        schemas.IntBase,
                        schemas.NoneBase,
                        schemas.Schema,
                        schemas.NoneDecimalMixin
                    ):
                    
                    
                        class MetaOapg:
                            format = 'int64'
                    
                    
                        def __new__(
                            cls,
                            *_args: typing.Union[None, decimal.Decimal, int, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'scheduledCompletionDate':
                            return super().__new__(
                                cls,
                                *_args,
                                _configuration=_configuration,
                            )
                    completionDate = schemas.Int64Schema
                    comments = schemas.StrSchema
                    isActive = schemas.BoolSchema
                    
                    
                    class milestones(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            @staticmethod
                            def items() -> typing.Type['MilestonesRequiredPut']:
                                return MilestonesRequiredPut
                    
                        def __new__(
                            cls,
                            _arg: typing.Union[typing.Tuple['MilestonesRequiredPut'], typing.List['MilestonesRequiredPut']],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'milestones':
                            return super().__new__(
                                cls,
                                _arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> 'MilestonesRequiredPut':
                            return super().__getitem__(i)
                    __annotations__ = {
                        "poamId": poamId,
                        "displayPoamId": displayPoamId,
                        "status": status,
                        "vulnerabilityDescription": vulnerabilityDescription,
                        "sourceIdentVuln": sourceIdentVuln,
                        "pocOrganization": pocOrganization,
                        "resources": resources,
                        "externalUid": externalUid,
                        "controlAcronym": controlAcronym,
                        "cci": cci,
                        "securityChecks": securityChecks,
                        "rawSeverity": rawSeverity,
                        "relevanceOfThreat": relevanceOfThreat,
                        "likelihood": likelihood,
                        "impact": impact,
                        "impactDescription": impactDescription,
                        "residualRiskLevel": residualRiskLevel,
                        "recommendations": recommendations,
                        "mitigation": mitigation,
                        "pocFirstName": pocFirstName,
                        "pocLastName": pocLastName,
                        "pocEmail": pocEmail,
                        "pocPhoneNumber": pocPhoneNumber,
                        "severity": severity,
                        "scheduledCompletionDate": scheduledCompletionDate,
                        "completionDate": completionDate,
                        "comments": comments,
                        "isActive": isActive,
                        "milestones": milestones,
                    }
        
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["poamId"]) -> MetaOapg.properties.poamId: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["displayPoamId"]) -> MetaOapg.properties.displayPoamId: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["vulnerabilityDescription"]) -> MetaOapg.properties.vulnerabilityDescription: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["sourceIdentVuln"]) -> MetaOapg.properties.sourceIdentVuln: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["pocOrganization"]) -> MetaOapg.properties.pocOrganization: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["resources"]) -> MetaOapg.properties.resources: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["externalUid"]) -> MetaOapg.properties.externalUid: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["controlAcronym"]) -> MetaOapg.properties.controlAcronym: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["cci"]) -> MetaOapg.properties.cci: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["securityChecks"]) -> MetaOapg.properties.securityChecks: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["rawSeverity"]) -> MetaOapg.properties.rawSeverity: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["relevanceOfThreat"]) -> MetaOapg.properties.relevanceOfThreat: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["likelihood"]) -> MetaOapg.properties.likelihood: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["impact"]) -> MetaOapg.properties.impact: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["impactDescription"]) -> MetaOapg.properties.impactDescription: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["residualRiskLevel"]) -> MetaOapg.properties.residualRiskLevel: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["recommendations"]) -> MetaOapg.properties.recommendations: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["mitigation"]) -> MetaOapg.properties.mitigation: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["pocFirstName"]) -> MetaOapg.properties.pocFirstName: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["pocLastName"]) -> MetaOapg.properties.pocLastName: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["pocEmail"]) -> MetaOapg.properties.pocEmail: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["pocPhoneNumber"]) -> MetaOapg.properties.pocPhoneNumber: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["severity"]) -> MetaOapg.properties.severity: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["scheduledCompletionDate"]) -> MetaOapg.properties.scheduledCompletionDate: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["completionDate"]) -> MetaOapg.properties.completionDate: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["comments"]) -> MetaOapg.properties.comments: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["isActive"]) -> MetaOapg.properties.isActive: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["milestones"]) -> MetaOapg.properties.milestones: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["poamId", "displayPoamId", "status", "vulnerabilityDescription", "sourceIdentVuln", "pocOrganization", "resources", "externalUid", "controlAcronym", "cci", "securityChecks", "rawSeverity", "relevanceOfThreat", "likelihood", "impact", "impactDescription", "residualRiskLevel", "recommendations", "mitigation", "pocFirstName", "pocLastName", "pocEmail", "pocPhoneNumber", "severity", "scheduledCompletionDate", "completionDate", "comments", "isActive", "milestones", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["poamId"]) -> typing.Union[MetaOapg.properties.poamId, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["displayPoamId"]) -> typing.Union[MetaOapg.properties.displayPoamId, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["vulnerabilityDescription"]) -> typing.Union[MetaOapg.properties.vulnerabilityDescription, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["sourceIdentVuln"]) -> typing.Union[MetaOapg.properties.sourceIdentVuln, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["pocOrganization"]) -> typing.Union[MetaOapg.properties.pocOrganization, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["resources"]) -> typing.Union[MetaOapg.properties.resources, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["externalUid"]) -> typing.Union[MetaOapg.properties.externalUid, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["controlAcronym"]) -> typing.Union[MetaOapg.properties.controlAcronym, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["cci"]) -> typing.Union[MetaOapg.properties.cci, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["securityChecks"]) -> typing.Union[MetaOapg.properties.securityChecks, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["rawSeverity"]) -> typing.Union[MetaOapg.properties.rawSeverity, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["relevanceOfThreat"]) -> typing.Union[MetaOapg.properties.relevanceOfThreat, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["likelihood"]) -> typing.Union[MetaOapg.properties.likelihood, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["impact"]) -> typing.Union[MetaOapg.properties.impact, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["impactDescription"]) -> typing.Union[MetaOapg.properties.impactDescription, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["residualRiskLevel"]) -> typing.Union[MetaOapg.properties.residualRiskLevel, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["recommendations"]) -> typing.Union[MetaOapg.properties.recommendations, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["mitigation"]) -> typing.Union[MetaOapg.properties.mitigation, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["pocFirstName"]) -> typing.Union[MetaOapg.properties.pocFirstName, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["pocLastName"]) -> typing.Union[MetaOapg.properties.pocLastName, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["pocEmail"]) -> typing.Union[MetaOapg.properties.pocEmail, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["pocPhoneNumber"]) -> typing.Union[MetaOapg.properties.pocPhoneNumber, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["severity"]) -> typing.Union[MetaOapg.properties.severity, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["scheduledCompletionDate"]) -> typing.Union[MetaOapg.properties.scheduledCompletionDate, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["completionDate"]) -> typing.Union[MetaOapg.properties.completionDate, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["comments"]) -> typing.Union[MetaOapg.properties.comments, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["isActive"]) -> typing.Union[MetaOapg.properties.isActive, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["milestones"]) -> typing.Union[MetaOapg.properties.milestones, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["poamId", "displayPoamId", "status", "vulnerabilityDescription", "sourceIdentVuln", "pocOrganization", "resources", "externalUid", "controlAcronym", "cci", "securityChecks", "rawSeverity", "relevanceOfThreat", "likelihood", "impact", "impactDescription", "residualRiskLevel", "recommendations", "mitigation", "pocFirstName", "pocLastName", "pocEmail", "pocPhoneNumber", "severity", "scheduledCompletionDate", "completionDate", "comments", "isActive", "milestones", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                poamId: typing.Union[MetaOapg.properties.poamId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                displayPoamId: typing.Union[MetaOapg.properties.displayPoamId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
                vulnerabilityDescription: typing.Union[MetaOapg.properties.vulnerabilityDescription, str, schemas.Unset] = schemas.unset,
                sourceIdentVuln: typing.Union[MetaOapg.properties.sourceIdentVuln, str, schemas.Unset] = schemas.unset,
                pocOrganization: typing.Union[MetaOapg.properties.pocOrganization, str, schemas.Unset] = schemas.unset,
                resources: typing.Union[MetaOapg.properties.resources, str, schemas.Unset] = schemas.unset,
                externalUid: typing.Union[MetaOapg.properties.externalUid, str, schemas.Unset] = schemas.unset,
                controlAcronym: typing.Union[MetaOapg.properties.controlAcronym, str, schemas.Unset] = schemas.unset,
                cci: typing.Union[MetaOapg.properties.cci, str, schemas.Unset] = schemas.unset,
                securityChecks: typing.Union[MetaOapg.properties.securityChecks, str, schemas.Unset] = schemas.unset,
                rawSeverity: typing.Union[MetaOapg.properties.rawSeverity, str, schemas.Unset] = schemas.unset,
                relevanceOfThreat: typing.Union[MetaOapg.properties.relevanceOfThreat, str, schemas.Unset] = schemas.unset,
                likelihood: typing.Union[MetaOapg.properties.likelihood, str, schemas.Unset] = schemas.unset,
                impact: typing.Union[MetaOapg.properties.impact, str, schemas.Unset] = schemas.unset,
                impactDescription: typing.Union[MetaOapg.properties.impactDescription, str, schemas.Unset] = schemas.unset,
                residualRiskLevel: typing.Union[MetaOapg.properties.residualRiskLevel, str, schemas.Unset] = schemas.unset,
                recommendations: typing.Union[MetaOapg.properties.recommendations, str, schemas.Unset] = schemas.unset,
                mitigation: typing.Union[MetaOapg.properties.mitigation, str, schemas.Unset] = schemas.unset,
                pocFirstName: typing.Union[MetaOapg.properties.pocFirstName, str, schemas.Unset] = schemas.unset,
                pocLastName: typing.Union[MetaOapg.properties.pocLastName, str, schemas.Unset] = schemas.unset,
                pocEmail: typing.Union[MetaOapg.properties.pocEmail, str, schemas.Unset] = schemas.unset,
                pocPhoneNumber: typing.Union[MetaOapg.properties.pocPhoneNumber, str, schemas.Unset] = schemas.unset,
                severity: typing.Union[MetaOapg.properties.severity, str, schemas.Unset] = schemas.unset,
                scheduledCompletionDate: typing.Union[MetaOapg.properties.scheduledCompletionDate, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                completionDate: typing.Union[MetaOapg.properties.completionDate, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                comments: typing.Union[MetaOapg.properties.comments, str, schemas.Unset] = schemas.unset,
                isActive: typing.Union[MetaOapg.properties.isActive, bool, schemas.Unset] = schemas.unset,
                milestones: typing.Union[MetaOapg.properties.milestones, list, tuple, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'items':
                return super().__new__(
                    cls,
                    *_args,
                    poamId=poamId,
                    displayPoamId=displayPoamId,
                    status=status,
                    vulnerabilityDescription=vulnerabilityDescription,
                    sourceIdentVuln=sourceIdentVuln,
                    pocOrganization=pocOrganization,
                    resources=resources,
                    externalUid=externalUid,
                    controlAcronym=controlAcronym,
                    cci=cci,
                    securityChecks=securityChecks,
                    rawSeverity=rawSeverity,
                    relevanceOfThreat=relevanceOfThreat,
                    likelihood=likelihood,
                    impact=impact,
                    impactDescription=impactDescription,
                    residualRiskLevel=residualRiskLevel,
                    recommendations=recommendations,
                    mitigation=mitigation,
                    pocFirstName=pocFirstName,
                    pocLastName=pocLastName,
                    pocEmail=pocEmail,
                    pocPhoneNumber=pocPhoneNumber,
                    severity=severity,
                    scheduledCompletionDate=scheduledCompletionDate,
                    completionDate=completionDate,
                    comments=comments,
                    isActive=isActive,
                    milestones=milestones,
                    _configuration=_configuration,
                    **kwargs,
                )

    def __new__(
        cls,
        _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'PoamRequestPutBody':
        return super().__new__(
            cls,
            _arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)

from emass_client.model.milestones_required_put import MilestonesRequiredPut