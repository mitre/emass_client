# coding: utf-8

from setuptools import setup, find_packages  # noqa: H301

NAME = "emass_client_api"
VERSION = "3.8.2"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "certifi >= 14.5.14",
    "frozendict ~= 2.3.4",
    "python-dateutil ~= 2.7.0",
    "setuptools >= 21.0.0",
    "typing_extensions ~= 4.3.0",
    "urllib3 ~= 1.26.7",
]

setup(
    name=NAME,
    version=VERSION,
    description="Enterprise Mission Assurance Support Service (eMASS)",
    author="eMASS Tier III support",
    author_email="disa.meade.id.mbx.emass-tier-iii-support@mail.mil",
    url="https://github.com/mitre/emass_client",
    keywords=["OpenAPI", "OpenAPI-Generator", "Enterprise Mission Assurance Support Service (eMASS)"],
    python_requires=">=3.7",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="Apache-2.0",
    long_description="""\
    ## eMASS API v3.9 Specification

The emass_client_api is a Python client that implements the [Enterprise Mission Assurance Support Service (eMASS)](https://disa.mil/~/media/Files/DISA/Fact-Sheets/eMASS.pdf)
Representational State Transfer (REST) Application Programming Interface (API) specifications.


This Python package was generated from the eMASS API specification:

- API version: v3.9
- Package version: 3.9.0
- Build date: 2023-05-21T19:09:41.124219800-05:00[America/Chicago]

## Requirements.

Python &gt;&#x3D;3.7

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
from emass_client.apis.tags import artifacts_api
from emass_client.model.artifacts_request_delete_body import ArtifactsRequestDeleteBody
from emass_client.model.artifacts_request_put_body import ArtifactsRequestPutBody
from emass_client.model.artifacts_response_del import ArtifactsResponseDel
from emass_client.model.artifacts_response_get import ArtifactsResponseGet
from emass_client.model.artifacts_response_put_post import ArtifactsResponsePutPost
from emass_client.model.response201 import Response201
from emass_client.model.response400 import Response400
from emass_client.model.response401 import Response401
from emass_client.model.response403 import Response403
from emass_client.model.response404 import Response404
from emass_client.model.response405 import Response405
from emass_client.model.response411 import Response411
from emass_client.model.response490 import Response490
from emass_client.model.response500 import Response500
# Defining the host is optional and defaults to http://localhost:4010
# See configuration.py for a list of all supported configuration parameters.
configuration = emass_client.Configuration(
    host = "http://localhost:4010"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: mockType
configuration.api_key['mockType'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['mockType'] = 'Bearer'

# Configure API key authorization: userId
configuration.api_key['userId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userId'] = 'Bearer'

# Enter a context with an instance of the API client
with emass_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = artifacts_api.ArtifactsApi(api_client)
    system_id = 35 # int | **System Id**: The unique system record identifier.
is_bulk = False # bool | **Is Bulk**: If no value is specified, the default is false, and an individual artifact file is expected.  When set to true, a .zip file is expected which  can contain multiple artifact files\"  (optional) (default to CodegenParameter{isFormParam=false, isQueryParam=true, isPathParam=false, isHeaderParam=false, isCookieParam=false, isBodyParam=false, isContainer=false, isCollectionFormatMulti=false, isPrimitiveType=true, isModel=false, isExplode=true, baseName='isBulk', paramName='is_bulk', dataType='bool', datatypeWithEnum='null', dataFormat='null', collectionFormat='null', description='**Is Bulk**: If no value is specified, the default is false, and an individual artifact file is expected.  When set to true, a .zip file is expected which  can contain multiple artifact files\" ', unescapedDescription='**Is Bulk**: If no value is specified, the default is false,
and an individual artifact file is expected.

When set to true, a .zip file is expected which 
can contain multiple artifact files"
', baseType='null', defaultValue='False', enumDefaultValue='null', enumName='null', style='FORM', deepObject='false', allowEmptyValue='false', example='False', jsonSchema='{
  "name" : "isBulk",
  "in" : "query",
  "description" : "**Is Bulk**: If no value is specified, the default is false,\nand an individual artifact file is expected.\n\nWhen set to true, a .zip file is expected which \ncan contain multiple artifact files\"\n",
  "required" : false,
  "style" : "form",
  "explode" : true,
  "schema" : {
    "type" : "boolean",
    "default" : false,
    "x-faker" : "random.boolean"
  }
}', isString=false, isNumeric=false, isInteger=false, isShort=false, isLong=false, isUnboundedInteger=false, isNumber=false, isFloat=false, isDouble=false, isDecimal=false, isByteArray=false, isBinary=false, isBoolean=true, isDate=false, isDateTime=false, isUuid=false, isUri=false, isEmail=false, isPassword=false, isFreeFormObject=false, isAnyType=false, isArray=false, isMap=false, isFile=false, isEnum=false, isEnumRef=false, _enum=null, allowableValues=null, items=null, mostInnerItems=null, additionalProperties=null, vars=[], requiredVars=[], vendorExtensions={}, hasValidation=false, maxProperties=null, minProperties=null, isNullable=false, isDeprecated=false, required=false, maximum='null', exclusiveMaximum=false, minimum='null', exclusiveMinimum=false, maxLength=null, minLength=null, pattern='null', maxItems=null, minItems=null, uniqueItems=false, uniqueItemsBoolean=null, contentType=null, multipleOf=null, isNull=false, isVoid=false, getAdditionalPropertiesIsAnyType=false, getHasVars=false, getHasRequired=false, getHasDiscriminatorWithNonEmptyMapping=false, composedSchemas=null, hasMultipleTypes=false, schema=CodegenProperty{openApiType='boolean', baseName='IsBulkSchema', complexType='null', getter='getIsBulk', setter='setIsBulk', description='null', dataType='bool', datatypeWithEnum='bool', dataFormat='null', name='is_bulk', min='null', max='null', defaultValue='False', defaultValueWithParam=' = data.isBulk;', baseType='bool', containerType='null', title='null', unescapedDescription='null', maxLength=null, minLength=null, pattern='null', example='False', jsonSchema='{
  "type" : "boolean",
  "default" : false,
  "x-faker" : "random.boolean"
}', minimum='null', maximum='null', exclusiveMinimum=false, exclusiveMaximum=false, required=false, deprecated=false, hasMoreNonReadOnly=false, isPrimitiveType=true, isModel=false, isContainer=false, isString=false, isNumeric=false, isInteger=false, isShort=false, isLong=false, isUnboundedInteger=false, isNumber=false, isFloat=false, isDouble=false, isDecimal=false, isByteArray=false, isBinary=false, isFile=false, isBoolean=true, isDate=false, isDateTime=false, isUuid=false, isUri=false, isEmail=false, isPassword=false, isFreeFormObject=false, isArray=false, isMap=false, isEnum=false, isInnerEnum=false, isEnumRef=false, isAnyType=false, isReadOnly=false, isWriteOnly=false, isNullable=false, isSelfReference=false, isCircularReference=false, isDiscriminator=false, isNew=false, isOverridden=null, _enum=null, allowableValues=null, items=null, additionalProperties=null, vars=[], requiredVars=[], mostInnerItems=null, vendorExtensions={x-faker=random.boolean}, hasValidation=false, isInherited=false, discriminatorValue='null', nameInCamelCase='IsBulk', nameInSnakeCase='null', enumName='null', maxItems=null, minItems=null, maxProperties=null, minProperties=null, uniqueItems=false, uniqueItemsBoolean=null, multipleOf=null, isXmlAttribute=false, xmlPrefix='null', xmlName='null', xmlNamespace='null', isXmlWrapped=false, isNull=false, isVoid=false, getAdditionalPropertiesIsAnyType=false, getHasVars=false, getHasRequired=false, getHasDiscriminatorWithNonEmptyMapping=false, composedSchemas=null, hasMultipleTypes=false, requiredVarsMap=null, ref=null, schemaIsFromAdditionalProperties=false, isBooleanSchemaTrue=false, isBooleanSchemaFalse=false, format=null, dependentRequired=null, contains=null}, content=null, requiredVarsMap=null, ref=null, schemaIsFromAdditionalProperties=false})
body = dict(
        is_template=False,
        type="Other",
        category="Evidence",
        zipper=open('/path/to/file', 'rb'),
    ) # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} |  (optional)

    try:
        # Add one or many artifacts in a system
        api_response = api_instance.add_artifacts_by_system_id(system_idis_bulk=is_bulkbody=body)
        pprint(api_response)
    except emass_client.ApiException as e:
        print("Exception when calling ArtifactsApi->add_artifacts_by_system_id: %s\n" % e)
```
## Documentation For Authorization

Authentication information is documented in the [emass_client specification GitHub page](https://mitre.github.io/emass_client/docs/redoc/)

## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in emass_client.apis and emass_client.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from emass_client.apis.default_api import DefaultApi`
- `from emass_client.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import emass_client
from emass_client.apis import *
from emass_client.models import *
```  # noqa: E501
    """,
	long_description_content_type="text/markdown"
)
