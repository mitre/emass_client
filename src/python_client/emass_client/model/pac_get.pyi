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


class PacGet(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            systemId = schemas.Int64Schema
            
            
            class workflow(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def ASSESS_AND_AUTHORIZE(cls):
                    return cls("Assess and Authorize")
                
                @schemas.classproperty
                def ASSESS_ONLY(cls):
                    return cls("Assess Only")
                
                @schemas.classproperty
                def SECURITY_PLAN_APPROVAL(cls):
                    return cls("Security Plan Approval")
            name = schemas.StrSchema
            
            
            class currentStageName(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'currentStageName':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class currentStage(
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'currentStage':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class totalStages(
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'totalStages':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class daysAtCurrentStage(
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'daysAtCurrentStage':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            comments = schemas.StrSchema
            __annotations__ = {
                "systemId": systemId,
                "workflow": workflow,
                "name": name,
                "currentStageName": currentStageName,
                "currentStage": currentStage,
                "totalStages": totalStages,
                "daysAtCurrentStage": daysAtCurrentStage,
                "comments": comments,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["systemId"]) -> MetaOapg.properties.systemId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["workflow"]) -> MetaOapg.properties.workflow: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currentStageName"]) -> MetaOapg.properties.currentStageName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currentStage"]) -> MetaOapg.properties.currentStage: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["totalStages"]) -> MetaOapg.properties.totalStages: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["daysAtCurrentStage"]) -> MetaOapg.properties.daysAtCurrentStage: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["comments"]) -> MetaOapg.properties.comments: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["systemId", "workflow", "name", "currentStageName", "currentStage", "totalStages", "daysAtCurrentStage", "comments", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["systemId"]) -> typing.Union[MetaOapg.properties.systemId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["workflow"]) -> typing.Union[MetaOapg.properties.workflow, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currentStageName"]) -> typing.Union[MetaOapg.properties.currentStageName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currentStage"]) -> typing.Union[MetaOapg.properties.currentStage, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["totalStages"]) -> typing.Union[MetaOapg.properties.totalStages, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["daysAtCurrentStage"]) -> typing.Union[MetaOapg.properties.daysAtCurrentStage, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["comments"]) -> typing.Union[MetaOapg.properties.comments, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["systemId", "workflow", "name", "currentStageName", "currentStage", "totalStages", "daysAtCurrentStage", "comments", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        systemId: typing.Union[MetaOapg.properties.systemId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        workflow: typing.Union[MetaOapg.properties.workflow, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        currentStageName: typing.Union[MetaOapg.properties.currentStageName, None, str, schemas.Unset] = schemas.unset,
        currentStage: typing.Union[MetaOapg.properties.currentStage, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        totalStages: typing.Union[MetaOapg.properties.totalStages, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        daysAtCurrentStage: typing.Union[MetaOapg.properties.daysAtCurrentStage, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        comments: typing.Union[MetaOapg.properties.comments, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PacGet':
        return super().__new__(
            cls,
            *_args,
            systemId=systemId,
            workflow=workflow,
            name=name,
            currentStageName=currentStageName,
            currentStage=currentStage,
            totalStages=totalStages,
            daysAtCurrentStage=daysAtCurrentStage,
            comments=comments,
            _configuration=_configuration,
            **kwargs,
        )