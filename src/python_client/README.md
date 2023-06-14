## eMASS API v3.10 Specification

The emass_client_api is a Python client that implements the [Enterprise Mission Assurance Support Service (eMASS)](https://disa.mil/~/media/Files/DISA/Fact-Sheets/eMASS.pdf)
Representational State Transfer (REST) Application Programming Interface (API) specifications.


This Python package was generated from the eMASS API specification:

- API version: v3.10
- Package version: 3.10.1
- Build date: 2023-06-14T17:42:15.829833Z[Etc/UTC]

## Requirements.

Python 3.7+

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

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import emass_client
from emass_client.rest import ApiException
from pprint import pprint

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
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: mockType
configuration.api_key['mockType'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['mockType'] = 'Bearer'

# Configure API key authorization: userId
configuration.api_key['userId'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userId'] = 'Bearer'


# Enter a context with an instance of the API client
with emass_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = emass_client.ArtifactsApi(api_client)
    system_id = 35 # int | **System Id**: The unique system record identifier.
    zipper = None # bytearray | 
    is_bulk = False # bool | **Is Bulk**: If no value is specified, the default is false, and an individual artifact file is expected.  When set to true, a .zip file is expected which  can contain multiple artifact files\"  (optional) (default to False)
    is_template = True # bool |  (optional)
    type = 'type_example' # str |  (optional)
    category = 'category_example' # str |  (optional)

    try:
        # Add one or many artifacts in a system
        api_response = api_instance.add_artifacts_by_system_id(system_id, zipper, is_bulk=is_bulk, is_template=is_template, type=type, category=category)
        print("The response of ArtifactsApi->add_artifacts_by_system_id:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ArtifactsApi->add_artifacts_by_system_id: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost:4010*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ArtifactsApi* | [**add_artifacts_by_system_id**](docs/ArtifactsApi.md#add_artifacts_by_system_id) | **POST** /api/systems/{systemId}/artifacts | Add one or many artifacts in a system
*ArtifactsApi* | [**delete_artifact**](docs/ArtifactsApi.md#delete_artifact) | **DELETE** /api/systems/{systemId}/artifacts | Remove one or many artifacts in a system
*ArtifactsApi* | [**get_system_artifacts**](docs/ArtifactsApi.md#get_system_artifacts) | **GET** /api/systems/{systemId}/artifacts | Get one or many artifacts in a system
*ArtifactsApi* | [**update_artifact_by_system_id**](docs/ArtifactsApi.md#update_artifact_by_system_id) | **PUT** /api/systems/{systemId}/artifacts | Update one or many artifacts in a system
*ArtifactsExportApi* | [**get_system_artifacts_export**](docs/ArtifactsExportApi.md#get_system_artifacts_export) | **GET** /api/systems/{systemId}/artifacts-export | Get the file of an artifact in a system
*CACApi* | [**add_system_cac**](docs/CACApi.md#add_system_cac) | **POST** /api/systems/{systemId}/approval/cac | Submit control to second role of CAC
*CACApi* | [**get_system_cac**](docs/CACApi.md#get_system_cac) | **GET** /api/systems/{systemId}/approval/cac | Get location of one or many controls in CAC
*CMMCAssessmentsApi* | [**get_cmmc_assessments**](docs/CMMCAssessmentsApi.md#get_cmmc_assessments) | **GET** /api/cmmc-assessments | Get CMMC assessment information
*CloudResourceResultsApi* | [**add_cloud_resources_by_system_id**](docs/CloudResourceResultsApi.md#add_cloud_resources_by_system_id) | **POST** /api/systems/{systemId}/cloud-resource-results | Add one or many cloud resources and their scan results
*ContainerScanResultsApi* | [**add_container_sans_by_system_id**](docs/ContainerScanResultsApi.md#add_container_sans_by_system_id) | **POST** /api/systems/{systemId}/container-scan-results | Add one or many containers and their scan results
*ControlsApi* | [**get_system_controls**](docs/ControlsApi.md#get_system_controls) | **GET** /api/systems/{systemId}/controls | Get control information in a system for one or many controls
*ControlsApi* | [**update_control_by_system_id**](docs/ControlsApi.md#update_control_by_system_id) | **PUT** /api/systems/{systemId}/controls | Update control information in a system for one or many controls
*DashboardsApi* | [**get_system_artifacts_details**](docs/DashboardsApi.md#get_system_artifacts_details) | **GET** /api/dashboards/system-artifacts-details | System Artifacts Details
*DashboardsApi* | [**get_system_artifacts_summary**](docs/DashboardsApi.md#get_system_artifacts_summary) | **GET** /api/dashboards/system-artifacts-summary | System Artifacts Summary
*DashboardsApi* | [**get_system_assessment_procedures_details**](docs/DashboardsApi.md#get_system_assessment_procedures_details) | **GET** /api/dashboards/system-assessment-procedures-details | System Assessment Procedures Details
*DashboardsApi* | [**get_system_associations_details**](docs/DashboardsApi.md#get_system_associations_details) | **GET** /api/dashboards/system-associations-details | System Associations Details
*DashboardsApi* | [**get_system_common_integration_status_summary**](docs/DashboardsApi.md#get_system_common_integration_status_summary) | **GET** /api/dashboards/system-conmon-integration-status-summary | System CONMON Integration Status
*DashboardsApi* | [**get_system_control_compliance_summary**](docs/DashboardsApi.md#get_system_control_compliance_summary) | **GET** /api/dashboards/system-control-compliance-summary | System Control Compliance Summary
*DashboardsApi* | [**get_system_hardware_details**](docs/DashboardsApi.md#get_system_hardware_details) | **GET** /api/dashboards/system-hardware-details | System Hardware Details
*DashboardsApi* | [**get_system_hardware_summary**](docs/DashboardsApi.md#get_system_hardware_summary) | **GET** /api/dashboards/system-hardware-summary | System Hardware Summary
*DashboardsApi* | [**get_system_poam_details**](docs/DashboardsApi.md#get_system_poam_details) | **GET** /api/dashboards/system-poam-details | System POA&amp;M Details
*DashboardsApi* | [**get_system_poam_summary**](docs/DashboardsApi.md#get_system_poam_summary) | **GET** /api/dashboards/system-poam-summary | System POA&amp;M Summary
*DashboardsApi* | [**get_system_ports_protocols_details**](docs/DashboardsApi.md#get_system_ports_protocols_details) | **GET** /api/dashboards/system-ports-protocols-details | System Ports/Protocols Details
*DashboardsApi* | [**get_system_ports_protocols_summary**](docs/DashboardsApi.md#get_system_ports_protocols_summary) | **GET** /api/dashboards/system-ports-protocols-summary | System Ports/Protocols Summary
*DashboardsApi* | [**get_system_privacy_summary**](docs/DashboardsApi.md#get_system_privacy_summary) | **GET** /api/dashboards/system-privacy-summary | System Privacy Summary
*DashboardsApi* | [**get_system_security_control_details**](docs/DashboardsApi.md#get_system_security_control_details) | **GET** /api/dashboards/system-security-controls-details | System Control Compliance Details
*DashboardsApi* | [**get_system_sensor_hardware_details**](docs/DashboardsApi.md#get_system_sensor_hardware_details) | **GET** /api/dashboards/system-sensor-hardware-details | System Sensor Hardware Details
*DashboardsApi* | [**get_system_sensor_hardware_summary**](docs/DashboardsApi.md#get_system_sensor_hardware_summary) | **GET** /api/dashboards/system-sensor-hardware-summary | System Sensor Hardware Summary
*DashboardsApi* | [**get_system_software_details**](docs/DashboardsApi.md#get_system_software_details) | **GET** /api/dashboards/system-software-details | System Software Details
*DashboardsApi* | [**get_system_software_summary**](docs/DashboardsApi.md#get_system_software_summary) | **GET** /api/dashboards/system-software-summary | System Software Summary
*DashboardsApi* | [**get_system_status_details**](docs/DashboardsApi.md#get_system_status_details) | **GET** /api/dashboards/system-status-details | System Status Details
*DashboardsApi* | [**get_user_system_assignments_details**](docs/DashboardsApi.md#get_user_system_assignments_details) | **GET** /api/dashboards/user-system-assignments-details | User System Assignments Details
*DashboardsApi* | [**get_va_omb_fsma_saop_summary**](docs/DashboardsApi.md#get_va_omb_fsma_saop_summary) | **GET** /api/dashboards/va-omb-fisma-saop-summary | VA OMB FISMA SAOP Summary
*DashboardsApi* | [**get_va_system_a2_summary**](docs/DashboardsApi.md#get_va_system_a2_summary) | **GET** /api/dashboards/va-system-a2-summary | VA System A2.0 Summary
*DashboardsApi* | [**get_va_system_aa_summary**](docs/DashboardsApi.md#get_va_system_aa_summary) | **GET** /api/dashboards/va-system-aa-summary | VA System A&amp;A Summary
*DashboardsApi* | [**get_va_system_fisma_invetory_crypto_summary**](docs/DashboardsApi.md#get_va_system_fisma_invetory_crypto_summary) | **GET** /api/dashboards/va-system-fisma-inventory-crypto-summary | VA System FISMA Inventory Crypto Summary
*DashboardsApi* | [**get_va_system_fisma_invetory_summary**](docs/DashboardsApi.md#get_va_system_fisma_invetory_summary) | **GET** /api/dashboards/va-system-fisma-inventory-summary | VA System FISMA Inventory Summary
*DashboardsApi* | [**get_va_system_pl109_reporting_summary**](docs/DashboardsApi.md#get_va_system_pl109_reporting_summary) | **GET** /api/dashboards/va-system-pl-109-reporting-summary | VA System P.L. 109 Reporting Summary
*DashboardsApi* | [**get_va_system_threat_architecture_details**](docs/DashboardsApi.md#get_va_system_threat_architecture_details) | **GET** /api/dashboards/va-system-threat-architecture-details | VA System Threat Architecture Details
*DashboardsApi* | [**get_va_system_threat_risk_summary**](docs/DashboardsApi.md#get_va_system_threat_risk_summary) | **GET** /api/dashboards/va-system-threat-risks-summary | VA System Threat Risks Summary
*DashboardsApi* | [**get_va_system_threat_source_details**](docs/DashboardsApi.md#get_va_system_threat_source_details) | **GET** /api/dashboards/va-system-threat-sources-details | VA System Threat Sources Details
*MilestonesApi* | [**add_milestone_by_system_id_and_poam_id**](docs/MilestonesApi.md#add_milestone_by_system_id_and_poam_id) | **POST** /api/systems/{systemId}/poams/{poamId}/milestones | Add milestones to one or many POA&amp;M items in a system
*MilestonesApi* | [**delete_milestone**](docs/MilestonesApi.md#delete_milestone) | **DELETE** /api/systems/{systemId}/poams/{poamId}/milestones | Remove milestones in a system for one or many POA&amp;M items
*MilestonesApi* | [**get_system_milestones_by_poam_id**](docs/MilestonesApi.md#get_system_milestones_by_poam_id) | **GET** /api/systems/{systemId}/poams/{poamId}/milestones | Get milestones in one or many POA&amp;M items in a system
*MilestonesApi* | [**get_system_milestones_by_poam_id_and_milestone_id**](docs/MilestonesApi.md#get_system_milestones_by_poam_id_and_milestone_id) | **GET** /api/systems/{systemId}/poams/{poamId}/milestones/{milestoneId} | Get milestone by ID in POA&amp;M item in a system
*MilestonesApi* | [**update_milestone_by_system_id_and_poam_id**](docs/MilestonesApi.md#update_milestone_by_system_id_and_poam_id) | **PUT** /api/systems/{systemId}/poams/{poamId}/milestones | Update one or many POA&amp;M items in a system
*PACApi* | [**add_system_pac**](docs/PACApi.md#add_system_pac) | **POST** /api/systems/{systemId}/approval/pac | Submit system package for review
*PACApi* | [**get_system_pac**](docs/PACApi.md#get_system_pac) | **GET** /api/systems/{systemId}/approval/pac | Get location of system package in PAC
*POAMApi* | [**add_poam_by_system_id**](docs/POAMApi.md#add_poam_by_system_id) | **POST** /api/systems/{systemId}/poams | Add one or many POA&amp;M items in a system
*POAMApi* | [**delete_poam**](docs/POAMApi.md#delete_poam) | **DELETE** /api/systems/{systemId}/poams | Remove one or many POA&amp;M items in a system
*POAMApi* | [**get_system_poams**](docs/POAMApi.md#get_system_poams) | **GET** /api/systems/{systemId}/poams | Get one or many POA&amp;M items in a system
*POAMApi* | [**get_system_poams_by_poam_id**](docs/POAMApi.md#get_system_poams_by_poam_id) | **GET** /api/systems/{systemId}/poams/{poamId} | Get POA&amp;M item by ID in a system
*POAMApi* | [**update_poam_by_system_id**](docs/POAMApi.md#update_poam_by_system_id) | **PUT** /api/systems/{systemId}/poams | Update one or many POA&amp;M items in a system
*RegistrationApi* | [**register_user**](docs/RegistrationApi.md#register_user) | **POST** /api/api-key | Register user certificate and obtain an API key
*StaticCodeScansApi* | [**add_static_code_scans_by_system_id**](docs/StaticCodeScansApi.md#add_static_code_scans_by_system_id) | **POST** /api/systems/{systemId}/static-code-scans | Upload static code scans or Clear static code scans
*SystemRolesApi* | [**get_system_roles**](docs/SystemRolesApi.md#get_system_roles) | **GET** /api/system-roles | Get available roles
*SystemRolesApi* | [**get_system_roles_by_category_id**](docs/SystemRolesApi.md#get_system_roles_by_category_id) | **GET** /api/system-roles/{roleCategory} | Get system roles
*SystemsApi* | [**get_system**](docs/SystemsApi.md#get_system) | **GET** /api/systems/{systemId} | Get system information for a specific system
*SystemsApi* | [**get_systems**](docs/SystemsApi.md#get_systems) | **GET** /api/systems | Get system information
*TestApi* | [**test_connection**](docs/TestApi.md#test_connection) | **GET** /api | Test connection to the API
*TestResultsApi* | [**add_test_results_by_system_id**](docs/TestResultsApi.md#add_test_results_by_system_id) | **POST** /api/systems/{systemId}/test-results | Add one or many test results in a system
*TestResultsApi* | [**get_system_test_results**](docs/TestResultsApi.md#get_system_test_results) | **GET** /api/systems/{systemId}/test-results | Get one or many test results in a system
*WorkflowDefinitionsApi* | [**get_workflow_definitions**](docs/WorkflowDefinitionsApi.md#get_workflow_definitions) | **GET** /api/workflows/definitions | Get workflow definitions in a site
*WorkflowInstancesApi* | [**get_system_workflow_instances**](docs/WorkflowInstancesApi.md#get_system_workflow_instances) | **GET** /api/workflows/instances | Get workflow instances in a site
*WorkflowInstancesApi* | [**get_system_workflow_instances_by_workflow_instance_id**](docs/WorkflowInstancesApi.md#get_system_workflow_instances_by_workflow_instance_id) | **GET** /api/workflows/instances/{workflowInstanceId} | Get workflow instance by ID


## Documentation For Models

 - [ArtifactsGet](docs/ArtifactsGet.md)
 - [ArtifactsRequestDeleteBodyInner](docs/ArtifactsRequestDeleteBodyInner.md)
 - [ArtifactsResponseDel](docs/ArtifactsResponseDel.md)
 - [ArtifactsResponseDelDataInner](docs/ArtifactsResponseDelDataInner.md)
 - [ArtifactsResponseGet](docs/ArtifactsResponseGet.md)
 - [ArtifactsResponsePutPost](docs/ArtifactsResponsePutPost.md)
 - [ArtifactsResponsePutPostDataInner](docs/ArtifactsResponsePutPostDataInner.md)
 - [CacGet](docs/CacGet.md)
 - [CacResponseGet](docs/CacResponseGet.md)
 - [CacResponsePost](docs/CacResponsePost.md)
 - [CacResponsePostDataInner](docs/CacResponsePostDataInner.md)
 - [CloudResourcesPost](docs/CloudResourcesPost.md)
 - [CloudResourcesResponsePost](docs/CloudResourcesResponsePost.md)
 - [CmmcGet](docs/CmmcGet.md)
 - [CmmcResponseGet](docs/CmmcResponseGet.md)
 - [ConnectivityCcsd](docs/ConnectivityCcsd.md)
 - [ContainersResourcesPost](docs/ContainersResourcesPost.md)
 - [ContainersResponsePost](docs/ContainersResponsePost.md)
 - [ControlsGet](docs/ControlsGet.md)
 - [ControlsPut](docs/ControlsPut.md)
 - [ControlsResponseGet](docs/ControlsResponseGet.md)
 - [ControlsResponsePut](docs/ControlsResponsePut.md)
 - [DashboardMockResponse](docs/DashboardMockResponse.md)
 - [DashboardMockResponsePagination](docs/DashboardMockResponsePagination.md)
 - [DefinitionTransitions](docs/DefinitionTransitions.md)
 - [InstancesTransitions](docs/InstancesTransitions.md)
 - [MilestoneResponseGet](docs/MilestoneResponseGet.md)
 - [MilestoneResponseGetMilestone](docs/MilestoneResponseGetMilestone.md)
 - [MilestoneResponsePost](docs/MilestoneResponsePost.md)
 - [MilestoneResponsePut](docs/MilestoneResponsePut.md)
 - [MilestonesGet](docs/MilestonesGet.md)
 - [MilestonesPutPostDelete](docs/MilestonesPutPostDelete.md)
 - [MilestonesRequestDeleteBodyInner](docs/MilestonesRequestDeleteBodyInner.md)
 - [MilestonesRequiredPost](docs/MilestonesRequiredPost.md)
 - [MilestonesRequiredPut](docs/MilestonesRequiredPut.md)
 - [MockObject](docs/MockObject.md)
 - [PacGet](docs/PacGet.md)
 - [PacPost](docs/PacPost.md)
 - [PacResponseGet](docs/PacResponseGet.md)
 - [PacResponsePost](docs/PacResponsePost.md)
 - [PoamGet](docs/PoamGet.md)
 - [PoamPostPutDel](docs/PoamPostPutDel.md)
 - [PoamRequestDeleteBodyInner](docs/PoamRequestDeleteBodyInner.md)
 - [PoamResponseDelete](docs/PoamResponseDelete.md)
 - [PoamResponseGetPoams](docs/PoamResponseGetPoams.md)
 - [PoamResponseGetSystems](docs/PoamResponseGetSystems.md)
 - [PoamResponsePost](docs/PoamResponsePost.md)
 - [PoamResponsePut](docs/PoamResponsePut.md)
 - [Register](docs/Register.md)
 - [RegisterData](docs/RegisterData.md)
 - [RegisterUserRequestPostBody](docs/RegisterUserRequestPostBody.md)
 - [Response200](docs/Response200.md)
 - [Response201](docs/Response201.md)
 - [Response201Meta](docs/Response201Meta.md)
 - [Response400](docs/Response400.md)
 - [Response400Meta](docs/Response400Meta.md)
 - [Response401](docs/Response401.md)
 - [Response401Meta](docs/Response401Meta.md)
 - [Response403](docs/Response403.md)
 - [Response403Meta](docs/Response403Meta.md)
 - [Response404](docs/Response404.md)
 - [Response405](docs/Response405.md)
 - [Response405Meta](docs/Response405Meta.md)
 - [Response411](docs/Response411.md)
 - [Response411Meta](docs/Response411Meta.md)
 - [Response490](docs/Response490.md)
 - [Response490Meta](docs/Response490Meta.md)
 - [Response500](docs/Response500.md)
 - [Response500Meta](docs/Response500Meta.md)
 - [RoleCategory](docs/RoleCategory.md)
 - [Roles](docs/Roles.md)
 - [Ssps](docs/Ssps.md)
 - [Stage](docs/Stage.md)
 - [StaticCodeApplication](docs/StaticCodeApplication.md)
 - [StaticCodePost](docs/StaticCodePost.md)
 - [StaticCodeRequestPostBody](docs/StaticCodeRequestPostBody.md)
 - [StaticCodeRequestPostBodyApplication](docs/StaticCodeRequestPostBodyApplication.md)
 - [StaticCodeResponsePost](docs/StaticCodeResponsePost.md)
 - [Success200Response](docs/Success200Response.md)
 - [Success200ResponseDataInner](docs/Success200ResponseDataInner.md)
 - [SystemResponse](docs/SystemResponse.md)
 - [SystemRolesCategoryResponse](docs/SystemRolesCategoryResponse.md)
 - [SystemRolesResponse](docs/SystemRolesResponse.md)
 - [SystemRolesResponseDataInner](docs/SystemRolesResponseDataInner.md)
 - [Systems](docs/Systems.md)
 - [SystemsResponse](docs/SystemsResponse.md)
 - [Test](docs/Test.md)
 - [TestData](docs/TestData.md)
 - [TestResultsGet](docs/TestResultsGet.md)
 - [TestResultsPost](docs/TestResultsPost.md)
 - [TestResultsResponseGet](docs/TestResultsResponseGet.md)
 - [TestResultsResponsePost](docs/TestResultsResponsePost.md)
 - [Users](docs/Users.md)
 - [WorkflowDefinitionGet](docs/WorkflowDefinitionGet.md)
 - [WorkflowDefinitionResponseGet](docs/WorkflowDefinitionResponseGet.md)
 - [WorkflowInstanceGet](docs/WorkflowInstanceGet.md)
 - [WorkflowInstanceResponseGet](docs/WorkflowInstanceResponseGet.md)
 - [WorkflowInstancesGet](docs/WorkflowInstancesGet.md)
 - [WorkflowInstancesResponseGet](docs/WorkflowInstancesResponseGet.md)
 - [WorkflowInstancesResponseGetPagination](docs/WorkflowInstancesResponseGetPagination.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization

Authentication information is documented in the [emass_client specification GitHub page](https://mitre.github.io/emass_client/docs/redoc/)

