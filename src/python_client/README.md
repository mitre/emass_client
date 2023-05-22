## eMASS API v3.9 Specification

The emass_client_api is a Python client that implements the [Enterprise Mission Assurance Support Service (eMASS)](https://disa.mil/~/media/Files/DISA/Fact-Sheets/eMASS.pdf)
Representational State Transfer (REST) Application Programming Interface (API) specifications.


This Python package was generated from the eMASS API specification:

- API version: v3.9
- Package version: 3.9.0
- Build date: 2023-05-21T19:48:58.553127800-05:00[America/Chicago]

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

Please follow the [installation procedure](#installation--usage) and then run the following:

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

## Documentation for API Endpoints

All URIs are relative to *http://localhost:4010*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ArtifactsApi* | [**add_artifacts_by_system_id**](docs/apis/tags/ArtifactsApi.md#add_artifacts_by_system_id) | **post** /api/systems/{systemId}/artifacts | Add one or many artifacts in a system
*ArtifactsApi* | [**delete_artifact**](docs/apis/tags/ArtifactsApi.md#delete_artifact) | **delete** /api/systems/{systemId}/artifacts | Remove one or many artifacts in a system
*ArtifactsApi* | [**get_system_artifacts**](docs/apis/tags/ArtifactsApi.md#get_system_artifacts) | **get** /api/systems/{systemId}/artifacts | Get one or many artifacts in a system
*ArtifactsApi* | [**update_artifact_by_system_id**](docs/apis/tags/ArtifactsApi.md#update_artifact_by_system_id) | **put** /api/systems/{systemId}/artifacts | Update one or many artifacts in a system
*ArtifactsExportApi* | [**get_system_artifacts_export**](docs/apis/tags/ArtifactsExportApi.md#get_system_artifacts_export) | **get** /api/systems/{systemId}/artifacts-export | Get the file of an artifact in a system
*CACApi* | [**add_system_cac**](docs/apis/tags/CACApi.md#add_system_cac) | **post** /api/systems/{systemId}/approval/cac | Submit control to second role of CAC
*CACApi* | [**get_system_cac**](docs/apis/tags/CACApi.md#get_system_cac) | **get** /api/systems/{systemId}/approval/cac | Get location of one or many controls in CAC
*CMMCAssessmentsApi* | [**get_cmmc_assessments**](docs/apis/tags/CMMCAssessmentsApi.md#get_cmmc_assessments) | **get** /api/cmmc-assessments | Get CMMC assessment information
*CloudResourceResultsApi* | [**add_cloud_resources_by_system_id**](docs/apis/tags/CloudResourceResultsApi.md#add_cloud_resources_by_system_id) | **post** /api/systems/{systemId}/cloud-resource-results | Add one or many cloud resources and their scan results
*ContainerScanResultsApi* | [**add_container_sans_by_system_id**](docs/apis/tags/ContainerScanResultsApi.md#add_container_sans_by_system_id) | **post** /api/systems/{systemId}/container-scan-results | Add one or many containers and their scan results
*ControlsApi* | [**get_system_controls**](docs/apis/tags/ControlsApi.md#get_system_controls) | **get** /api/systems/{systemId}/controls | Get control information in a system for one or many controls
*ControlsApi* | [**update_control_by_system_id**](docs/apis/tags/ControlsApi.md#update_control_by_system_id) | **put** /api/systems/{systemId}/controls | Update control information in a system for one or many controls
*DashboardsApi* | [**get_system_artifacts_details**](docs/apis/tags/DashboardsApi.md#get_system_artifacts_details) | **get** /api/dashboards/system-artifacts-details | Get dashboard information
*DashboardsApi* | [**get_system_artifacts_summary**](docs/apis/tags/DashboardsApi.md#get_system_artifacts_summary) | **get** /api/dashboards/system-artifacts-summary | Get dashboard information
*DashboardsApi* | [**get_system_assessment_procedures_details**](docs/apis/tags/DashboardsApi.md#get_system_assessment_procedures_details) | **get** /api/dashboards/system-assessment-procedures-details | Get dashboard information
*DashboardsApi* | [**get_system_associations_details**](docs/apis/tags/DashboardsApi.md#get_system_associations_details) | **get** /api/dashboards/system-associations-details | Get dashboard information
*DashboardsApi* | [**get_system_control_compliance_summary**](docs/apis/tags/DashboardsApi.md#get_system_control_compliance_summary) | **get** /api/dashboards/system-control-compliance-summary | Get dashboard information
*DashboardsApi* | [**get_system_hardware_details**](docs/apis/tags/DashboardsApi.md#get_system_hardware_details) | **get** /api/dashboards/system-hardware-details | Get dashboard information
*DashboardsApi* | [**get_system_hardware_summary**](docs/apis/tags/DashboardsApi.md#get_system_hardware_summary) | **get** /api/dashboards/system-hardware-summary | Get dashboard information
*DashboardsApi* | [**get_system_poam_details**](docs/apis/tags/DashboardsApi.md#get_system_poam_details) | **get** /api/dashboards/system-poam-details | Get dashboard information
*DashboardsApi* | [**get_system_poam_summary**](docs/apis/tags/DashboardsApi.md#get_system_poam_summary) | **get** /api/dashboards/system-poam-summary | Get dashboard information
*DashboardsApi* | [**get_system_ports_protocols_details**](docs/apis/tags/DashboardsApi.md#get_system_ports_protocols_details) | **get** /api/dashboards/system-ports-protocols-details | Get dashboard information
*DashboardsApi* | [**get_system_ports_protocols_summary**](docs/apis/tags/DashboardsApi.md#get_system_ports_protocols_summary) | **get** /api/dashboards/system-ports-protocols-summary | Get dashboard information
*DashboardsApi* | [**get_system_privacy_summary**](docs/apis/tags/DashboardsApi.md#get_system_privacy_summary) | **get** /api/dashboards/system-privacy-summary | Get dashboard information
*DashboardsApi* | [**get_system_security_control_details**](docs/apis/tags/DashboardsApi.md#get_system_security_control_details) | **get** /api/dashboards/system-security-controls-details | Get dashboard information
*DashboardsApi* | [**get_system_sensor_hardware_details**](docs/apis/tags/DashboardsApi.md#get_system_sensor_hardware_details) | **get** /api/dashboards/system-sensor-hardware-details | Get dashboard information
*DashboardsApi* | [**get_system_sensor_hardware_summary**](docs/apis/tags/DashboardsApi.md#get_system_sensor_hardware_summary) | **get** /api/dashboards/system-sensor-hardware-summary | Get dashboard information
*DashboardsApi* | [**get_system_status_details**](docs/apis/tags/DashboardsApi.md#get_system_status_details) | **get** /api/dashboards/system-status-details | Get dashboard information
*DashboardsApi* | [**get_user_system_assignments_details**](docs/apis/tags/DashboardsApi.md#get_user_system_assignments_details) | **get** /api/dashboards/user-system-assignments-details | Get dashboard information
*DashboardsApi* | [**get_va_omb_fsma_saop_summary**](docs/apis/tags/DashboardsApi.md#get_va_omb_fsma_saop_summary) | **get** /api/dashboards/va-omb-fisma-saop-summary | Get dashboard information
*DashboardsApi* | [**get_va_system_a2_summary**](docs/apis/tags/DashboardsApi.md#get_va_system_a2_summary) | **get** /api/dashboards/va-system-a2-summary | Get dashboard information
*DashboardsApi* | [**get_va_system_aa_summary**](docs/apis/tags/DashboardsApi.md#get_va_system_aa_summary) | **get** /api/dashboards/va-system-aa-summary | Get dashboard information
*DashboardsApi* | [**get_va_system_fisma_invetory_crypto_summary**](docs/apis/tags/DashboardsApi.md#get_va_system_fisma_invetory_crypto_summary) | **get** /api/dashboards/va-system-fisma-inventory-crypto-summary | Get dashboard information
*DashboardsApi* | [**get_va_system_fisma_invetory_summary**](docs/apis/tags/DashboardsApi.md#get_va_system_fisma_invetory_summary) | **get** /api/dashboards/va-system-fisma-inventory-summary | Get dashboard information
*DashboardsApi* | [**get_va_system_pl109_reporting_summary**](docs/apis/tags/DashboardsApi.md#get_va_system_pl109_reporting_summary) | **get** /api/dashboards/va-system-pl-109-reporting-summary | Get dashboard information
*DashboardsApi* | [**get_va_system_threat_architecture_details**](docs/apis/tags/DashboardsApi.md#get_va_system_threat_architecture_details) | **get** /api/dashboards/va-system-threat-architecture-details | Get dashboard information
*DashboardsApi* | [**get_va_system_threat_risk_summary**](docs/apis/tags/DashboardsApi.md#get_va_system_threat_risk_summary) | **get** /api/dashboards/va-system-threat-risks-summary | Get dashboard information
*DashboardsApi* | [**get_va_system_threat_source_details**](docs/apis/tags/DashboardsApi.md#get_va_system_threat_source_details) | **get** /api/dashboards/va-system-threat-sources-details | Get dashboard information
*MilestonesApi* | [**add_milestone_by_system_id_and_poam_id**](docs/apis/tags/MilestonesApi.md#add_milestone_by_system_id_and_poam_id) | **post** /api/systems/{systemId}/poams/{poamId}/milestones | Add milestones to one or many POA&amp;M items in a system
*MilestonesApi* | [**delete_milestone**](docs/apis/tags/MilestonesApi.md#delete_milestone) | **delete** /api/systems/{systemId}/poams/{poamId}/milestones | Remove milestones in a system for one or many POA&amp;M items
*MilestonesApi* | [**get_system_milestones_by_poam_id**](docs/apis/tags/MilestonesApi.md#get_system_milestones_by_poam_id) | **get** /api/systems/{systemId}/poams/{poamId}/milestones | Get milestones in one or many POA&amp;M items in a system
*MilestonesApi* | [**get_system_milestones_by_poam_id_and_milestone_id**](docs/apis/tags/MilestonesApi.md#get_system_milestones_by_poam_id_and_milestone_id) | **get** /api/systems/{systemId}/poams/{poamId}/milestones/{milestoneId} | Get milestone by ID in POA&amp;M item in a system
*MilestonesApi* | [**update_milestone_by_system_id_and_poam_id**](docs/apis/tags/MilestonesApi.md#update_milestone_by_system_id_and_poam_id) | **put** /api/systems/{systemId}/poams/{poamId}/milestones | Update one or many POA&amp;M items in a system
*PACApi* | [**add_system_pac**](docs/apis/tags/PACApi.md#add_system_pac) | **post** /api/systems/{systemId}/approval/pac | Submit system package for review
*PACApi* | [**get_system_pac**](docs/apis/tags/PACApi.md#get_system_pac) | **get** /api/systems/{systemId}/approval/pac | Get location of system package in PAC
*POAMApi* | [**add_poam_by_system_id**](docs/apis/tags/POAMApi.md#add_poam_by_system_id) | **post** /api/systems/{systemId}/poams | Add one or many POA&amp;M items in a system
*POAMApi* | [**delete_poam**](docs/apis/tags/POAMApi.md#delete_poam) | **delete** /api/systems/{systemId}/poams | Remove one or many POA&amp;M items in a system
*POAMApi* | [**get_system_poams**](docs/apis/tags/POAMApi.md#get_system_poams) | **get** /api/systems/{systemId}/poams | Get one or many POA&amp;M items in a system
*POAMApi* | [**get_system_poams_by_poam_id**](docs/apis/tags/POAMApi.md#get_system_poams_by_poam_id) | **get** /api/systems/{systemId}/poams/{poamId} | Get POA&amp;M item by ID in a system
*POAMApi* | [**update_poam_by_system_id**](docs/apis/tags/POAMApi.md#update_poam_by_system_id) | **put** /api/systems/{systemId}/poams | Update one or many POA&amp;M items in a system
*RegistrationApi* | [**register_user**](docs/apis/tags/RegistrationApi.md#register_user) | **post** /api/api-key | Register user certificate and obtain an API key
*StaticCodeScansApi* | [**add_static_code_scans_by_system_id**](docs/apis/tags/StaticCodeScansApi.md#add_static_code_scans_by_system_id) | **post** /api/systems/{systemId}/static-code-scans | Upload static code scans or Clear static code scans
*SystemRolesApi* | [**get_system_roles**](docs/apis/tags/SystemRolesApi.md#get_system_roles) | **get** /api/system-roles | Get available roles
*SystemRolesApi* | [**get_system_roles_by_category_id**](docs/apis/tags/SystemRolesApi.md#get_system_roles_by_category_id) | **get** /api/system-roles/{roleCategory} | Get system roles
*SystemsApi* | [**get_system**](docs/apis/tags/SystemsApi.md#get_system) | **get** /api/systems/{systemId} | Get system information for a specific system
*SystemsApi* | [**get_systems**](docs/apis/tags/SystemsApi.md#get_systems) | **get** /api/systems | Get system information
*TestApi* | [**test_connection**](docs/apis/tags/TestApi.md#test_connection) | **get** /api | Test connection to the API
*TestResultsApi* | [**add_test_results_by_system_id**](docs/apis/tags/TestResultsApi.md#add_test_results_by_system_id) | **post** /api/systems/{systemId}/test-results | Add one or many test results in a system
*TestResultsApi* | [**get_system_test_results**](docs/apis/tags/TestResultsApi.md#get_system_test_results) | **get** /api/systems/{systemId}/test-results | Get one or many test results in a system
*WorkflowDefinitionsApi* | [**get_workflow_definitions**](docs/apis/tags/WorkflowDefinitionsApi.md#get_workflow_definitions) | **get** /api/workflows/definitions | Get workflow definitions in a site
*WorkflowInstancesApi* | [**get_system_workflow_instances**](docs/apis/tags/WorkflowInstancesApi.md#get_system_workflow_instances) | **get** /api/workflows/instances | Get workflow instances in a site
*WorkflowInstancesApi* | [**get_system_workflow_instances_by_workflow_instance_id**](docs/apis/tags/WorkflowInstancesApi.md#get_system_workflow_instances_by_workflow_instance_id) | **get** /api/workflows/instances/{workflowInstanceId} | Get workflow instance by ID

## Documentation For Models

 - [ArtifactsGet](docs/models/ArtifactsGet.md)
 - [ArtifactsRequestDeleteBody](docs/models/ArtifactsRequestDeleteBody.md)
 - [ArtifactsRequestPutBody](docs/models/ArtifactsRequestPutBody.md)
 - [ArtifactsResponseDel](docs/models/ArtifactsResponseDel.md)
 - [ArtifactsResponseGet](docs/models/ArtifactsResponseGet.md)
 - [ArtifactsResponsePutPost](docs/models/ArtifactsResponsePutPost.md)
 - [CacGet](docs/models/CacGet.md)
 - [CacRequestPostBody](docs/models/CacRequestPostBody.md)
 - [CacResponseGet](docs/models/CacResponseGet.md)
 - [CacResponsePost](docs/models/CacResponsePost.md)
 - [CloudResourcesPost](docs/models/CloudResourcesPost.md)
 - [CloudResourcesRequestPostBody](docs/models/CloudResourcesRequestPostBody.md)
 - [CloudResourcesResponsePost](docs/models/CloudResourcesResponsePost.md)
 - [CmmcGet](docs/models/CmmcGet.md)
 - [CmmcResponseGet](docs/models/CmmcResponseGet.md)
 - [ConnectivityCcsd](docs/models/ConnectivityCcsd.md)
 - [ContainersRequestPostBody](docs/models/ContainersRequestPostBody.md)
 - [ContainersResourcesPost](docs/models/ContainersResourcesPost.md)
 - [ContainersResponsePost](docs/models/ContainersResponsePost.md)
 - [ControlsGet](docs/models/ControlsGet.md)
 - [ControlsPut](docs/models/ControlsPut.md)
 - [ControlsRequestPutBody](docs/models/ControlsRequestPutBody.md)
 - [ControlsResponseGet](docs/models/ControlsResponseGet.md)
 - [ControlsResponsePut](docs/models/ControlsResponsePut.md)
 - [DefinitionTransitions](docs/models/DefinitionTransitions.md)
 - [Errors](docs/models/Errors.md)
 - [InstancesTransitions](docs/models/InstancesTransitions.md)
 - [MilestoneResponseGet](docs/models/MilestoneResponseGet.md)
 - [MilestoneResponseGetMilestone](docs/models/MilestoneResponseGetMilestone.md)
 - [MilestoneResponsePost](docs/models/MilestoneResponsePost.md)
 - [MilestoneResponsePut](docs/models/MilestoneResponsePut.md)
 - [MilestonesGet](docs/models/MilestonesGet.md)
 - [MilestonesPutPostDelete](docs/models/MilestonesPutPostDelete.md)
 - [MilestonesRequestDeleteBody](docs/models/MilestonesRequestDeleteBody.md)
 - [MilestonesRequestPostBody](docs/models/MilestonesRequestPostBody.md)
 - [MilestonesRequestPutBody](docs/models/MilestonesRequestPutBody.md)
 - [MilestonesRequiredPost](docs/models/MilestonesRequiredPost.md)
 - [MilestonesRequiredPut](docs/models/MilestonesRequiredPut.md)
 - [PacGet](docs/models/PacGet.md)
 - [PacPost](docs/models/PacPost.md)
 - [PacRequestPostBody](docs/models/PacRequestPostBody.md)
 - [PacResponseGet](docs/models/PacResponseGet.md)
 - [PacResponsePost](docs/models/PacResponsePost.md)
 - [PoamGet](docs/models/PoamGet.md)
 - [PoamPostPutDel](docs/models/PoamPostPutDel.md)
 - [PoamRequestDeleteBody](docs/models/PoamRequestDeleteBody.md)
 - [PoamRequestPostBody](docs/models/PoamRequestPostBody.md)
 - [PoamRequestPutBody](docs/models/PoamRequestPutBody.md)
 - [PoamResponseDelete](docs/models/PoamResponseDelete.md)
 - [PoamResponseGetPoams](docs/models/PoamResponseGetPoams.md)
 - [PoamResponseGetSystems](docs/models/PoamResponseGetSystems.md)
 - [PoamResponsePost](docs/models/PoamResponsePost.md)
 - [PoamResponsePut](docs/models/PoamResponsePut.md)
 - [Register](docs/models/Register.md)
 - [RegisterUserRequestPostBody](docs/models/RegisterUserRequestPostBody.md)
 - [Response200](docs/models/Response200.md)
 - [Response201](docs/models/Response201.md)
 - [Response400](docs/models/Response400.md)
 - [Response401](docs/models/Response401.md)
 - [Response403](docs/models/Response403.md)
 - [Response404](docs/models/Response404.md)
 - [Response405](docs/models/Response405.md)
 - [Response411](docs/models/Response411.md)
 - [Response490](docs/models/Response490.md)
 - [Response500](docs/models/Response500.md)
 - [RoleCategory](docs/models/RoleCategory.md)
 - [Roles](docs/models/Roles.md)
 - [Ssps](docs/models/Ssps.md)
 - [Stage](docs/models/Stage.md)
 - [StaticCodeApplication](docs/models/StaticCodeApplication.md)
 - [StaticCodePost](docs/models/StaticCodePost.md)
 - [StaticCodeRequestPostBody](docs/models/StaticCodeRequestPostBody.md)
 - [StaticCodeResponsePost](docs/models/StaticCodeResponsePost.md)
 - [Success200Response](docs/models/Success200Response.md)
 - [SystemResponse](docs/models/SystemResponse.md)
 - [SystemRolesCategoryResponse](docs/models/SystemRolesCategoryResponse.md)
 - [SystemRolesResponse](docs/models/SystemRolesResponse.md)
 - [Systems](docs/models/Systems.md)
 - [SystemsResponse](docs/models/SystemsResponse.md)
 - [Test](docs/models/Test.md)
 - [TestResultsGet](docs/models/TestResultsGet.md)
 - [TestResultsPost](docs/models/TestResultsPost.md)
 - [TestResultsRequestPostBody](docs/models/TestResultsRequestPostBody.md)
 - [TestResultsResponseGet](docs/models/TestResultsResponseGet.md)
 - [TestResultsResponsePost](docs/models/TestResultsResponsePost.md)
 - [Users](docs/models/Users.md)
 - [WorkflowDefinitionGet](docs/models/WorkflowDefinitionGet.md)
 - [WorkflowDefinitionResponseGet](docs/models/WorkflowDefinitionResponseGet.md)
 - [WorkflowInstanceGet](docs/models/WorkflowInstanceGet.md)
 - [WorkflowInstanceResponseGet](docs/models/WorkflowInstanceResponseGet.md)
 - [WorkflowInstancesGet](docs/models/WorkflowInstancesGet.md)
 - [WorkflowInstancesResponseGet](docs/models/WorkflowInstancesResponseGet.md)

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
```
