# emass_client

EmassClient - the Ruby gem for the Enterprise Mission Assurance Support Service (eMASS)

The Enterprise Mission Assurance Support Service (eMASS) Representational State
Transfer (REST) Application Programming Interface (API) enables users to perform
assessments and complete actions associated with system records. 

<strong>Register External Application (that use the eMASS API)</strong></br>
New users will need to [register](https://nisp.emass.apps.mil/Content/Help/jobaids/eMASS_OT_NewUser_Job_Aid.pdf)
an API key with the eMASS development team prior to accessing the site for the first time. The eMASS REST API 
requires a client certificate (SSL/TLS, DoD PKI only). Use the `Registration` endpoint to register the client
certificate.</br></br>

Every call to the eMASS REST API will require the use of the agreed upon public key certificate and API key. 
The API key must be provided in the request header for all endpoint calls (api-key). If the service receives
an untrusted certificate or API key, a 401 error response code will be returned along with an error message.</br></br>

<strong>Available Request Headers</strong></br>
<table>
  <tr>
    <th align=left>key</th>
    <th align=left>Example Value</th>
    <th align=left>Description</th>
  </tr>
  <tr>
    <td>`api-key`</td>
    <td>api-key-provided-by-emass</td>
    <td>This API key must be provided in the request header for all endpoint calls</td>
  </tr>
  <tr>
    <td>`user-uid`</td>
    <td>USER.UID.KEY</td>
    <td>This User unique identifier key must be provided in the request header for all PUT, POST, and DELETE endpoint calls</td>
  </tr>
  <tr>
    <td></td><td></td>
    <td>
      Note: For DoD users this is the DoD ID Number (EIDIPI) on their DoD CAC
    </td>
  </tr>
</table>

</br><strong>Approve API Client for Actionable Requests</strong></br>
Users are required to log-in to eMASS and grant permissions for a client to update data
within eMASS on their behalf. This is only required for actionable requests (PUT, POST,
DELETE). The Registration Endpoint and all GET requests can be accessed without completing
this process with the correct permissions. Please note that leaving a field parameter blank
(for PUT/POST requests) has the potential to clear information in the active eMASS records.

To establish an account with eMASS and/or acquire an api-key/user-uid, contact one of the listed POC:


This SDK is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v3.3
- Package version: 1.0.6
- Build package: org.openapitools.codegen.languages.RubyClientCodegen
For more information, please visit [https://www.dcsa.mil/is/emass/](https://www.dcsa.mil/is/emass/)

## Installation

### Build a gem

To build the Ruby code into a gem:

```shell
gem build emass_client.gemspec
```

Then either install the gem locally:

```shell
gem install ./emass_client-1.0.6.gem
```

(for development, run `gem install --dev ./emass_client-1.0.6.gem` to install the development dependencies)

or publish the gem to a gem hosting service, e.g. [RubyGems](https://rubygems.org/).

Finally add this to the Gemfile:

    gem 'emass_client', '~> 1.0.6'

### Install from Git

If the Ruby gem is hosted at a git repository: https://github.com/GIT_USER_ID/GIT_REPO_ID, then add the following in the Gemfile:

    gem 'emass_client', :git => 'https://github.com/GIT_USER_ID/GIT_REPO_ID.git'

### Include the Ruby code directly

Include the Ruby code directly using `-I` as follows:

```shell
ruby -Ilib script.rb
```

## Getting Started

Please follow the [installation](#installation) procedure and then run the following code:

```ruby
# Load the gem
require 'emass_client'

# Setup authorization
EmassClient.configure do |config|
  # Configure API key authorization: apiKey
  config.api_key['apiKey'] = 'YOUR API KEY'
  # Uncomment the following line to set a prefix for the API key, e.g. 'Bearer' (defaults to nil)
  # config.api_key_prefix['apiKey'] = 'Bearer'

  # Configure API key authorization: mockType
  config.api_key['mockType'] = 'YOUR API KEY'
  # Uncomment the following line to set a prefix for the API key, e.g. 'Bearer' (defaults to nil)
  # config.api_key_prefix['mockType'] = 'Bearer'

  # Configure API key authorization: userId
  config.api_key['userId'] = 'YOUR API KEY'
  # Uncomment the following line to set a prefix for the API key, e.g. 'Bearer' (defaults to nil)
  # config.api_key_prefix['userId'] = 'Bearer'
end

api_instance = EmassClient::ArtifactsApi.new
system_id = 35 # Integer | **System Id**: The unique system record identifier.
zipper = File.new('/path/to/some/file') # File | 
opts = {
  is_template: true, # Boolean | 
  type: 'Procedure', # String | 
  category: 'Implementation Guidance' # String | 
}

begin
  #Add one or many artifacts in a system
  result = api_instance.add_artifacts_by_system_id(system_id, zipper, opts)
  p result
rescue EmassClient::ApiError => e
  puts "Exception when calling ArtifactsApi->add_artifacts_by_system_id: #{e}"
end

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost:4010*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*EmassClient::ArtifactsApi* | [**add_artifacts_by_system_id**](docs/ArtifactsApi.md#add_artifacts_by_system_id) | **POST** /api/systems/{systemId}/artifacts | Add one or many artifacts in a system
*EmassClient::ArtifactsApi* | [**delete_artifact**](docs/ArtifactsApi.md#delete_artifact) | **DELETE** /api/systems/{systemId}/artifacts | Remove one or many artifacts in a system
*EmassClient::ArtifactsApi* | [**get_system_artifacts**](docs/ArtifactsApi.md#get_system_artifacts) | **GET** /api/systems/{systemId}/artifacts | Get one or many artifacts in a system
*EmassClient::ArtifactsApi* | [**update_artifact_by_system_id**](docs/ArtifactsApi.md#update_artifact_by_system_id) | **PUT** /api/systems/{systemId}/artifacts | Update one or many artifacts in a system
*EmassClient::ArtifactsExportApi* | [**get_system_artifacts_export**](docs/ArtifactsExportApi.md#get_system_artifacts_export) | **GET** /api/systems/{systemId}/artifacts-export | Get the file of an artifact in a system
*EmassClient::CACApi* | [**add_system_cac**](docs/CACApi.md#add_system_cac) | **POST** /api/systems/{systemId}/approval/cac | Submit control to second role of CAC
*EmassClient::CACApi* | [**get_system_cac**](docs/CACApi.md#get_system_cac) | **GET** /api/systems/{systemId}/approval/cac | Get location of one or many controls in CAC
*EmassClient::CMMCAssessmentsApi* | [**get_cmmc_assessments**](docs/CMMCAssessmentsApi.md#get_cmmc_assessments) | **GET** /api/cmmc-assessments | Get CMMC assessment information
*EmassClient::CloudResourcesApi* | [**add_cloud_resources_by_system_id**](docs/CloudResourcesApi.md#add_cloud_resources_by_system_id) | **POST** /api/systems/{systemId}/cloud-resource-results | Add one or many cloud resources and their scan results
*EmassClient::ContainersApi* | [**add_container_sans_by_system_id**](docs/ContainersApi.md#add_container_sans_by_system_id) | **POST** /api/systems/{systemId}/container-scan-results | Add one or many containers and their scan results
*EmassClient::ControlsApi* | [**get_system_controls**](docs/ControlsApi.md#get_system_controls) | **GET** /api/systems/{systemId}/controls | Get control information in a system for one or many controls
*EmassClient::ControlsApi* | [**update_control_by_system_id**](docs/ControlsApi.md#update_control_by_system_id) | **PUT** /api/systems/{systemId}/controls | Update control information in a system for one or many controls
*EmassClient::MilestonesApi* | [**add_milestone_by_system_id_and_poam_id**](docs/MilestonesApi.md#add_milestone_by_system_id_and_poam_id) | **POST** /api/systems/{systemId}/poams/{poamId}/milestones | Add milestones to one or many POA&M items in a system
*EmassClient::MilestonesApi* | [**delete_milestone**](docs/MilestonesApi.md#delete_milestone) | **DELETE** /api/systems/{systemId}/poams/{poamId}/milestones | Remove milestones in a system for one or many POA&M items
*EmassClient::MilestonesApi* | [**get_system_milestones_by_poam_id**](docs/MilestonesApi.md#get_system_milestones_by_poam_id) | **GET** /api/systems/{systemId}/poams/{poamId}/milestones | Get milestones in one or many POA&M items in a system
*EmassClient::MilestonesApi* | [**get_system_milestones_by_poam_id_and_milestone_id**](docs/MilestonesApi.md#get_system_milestones_by_poam_id_and_milestone_id) | **GET** /api/systems/{systemId}/poams/{poamId}/milestones/{milestoneId} | Get milestone by ID in POA&M item in a system
*EmassClient::MilestonesApi* | [**update_milestone_by_system_id_and_poam_id**](docs/MilestonesApi.md#update_milestone_by_system_id_and_poam_id) | **PUT** /api/systems/{systemId}/poams/{poamId}/milestones | Update one or many POA&M items in a system
*EmassClient::PACApi* | [**add_system_pac**](docs/PACApi.md#add_system_pac) | **POST** /api/systems/{systemId}/approval/pac | Submit system package for review
*EmassClient::PACApi* | [**get_system_pac**](docs/PACApi.md#get_system_pac) | **GET** /api/systems/{systemId}/approval/pac | Get location of system package in PAC
*EmassClient::POAMApi* | [**add_poam_by_system_id**](docs/POAMApi.md#add_poam_by_system_id) | **POST** /api/systems/{systemId}/poams | Add one or many POA&M items in a system
*EmassClient::POAMApi* | [**delete_poam**](docs/POAMApi.md#delete_poam) | **DELETE** /api/systems/{systemId}/poams | Remove one or many POA&M items in a system
*EmassClient::POAMApi* | [**get_system_poams**](docs/POAMApi.md#get_system_poams) | **GET** /api/systems/{systemId}/poams | Get one or many POA&M items in a system
*EmassClient::POAMApi* | [**get_system_poams_by_poam_id**](docs/POAMApi.md#get_system_poams_by_poam_id) | **GET** /api/systems/{systemId}/poams/{poamId} | Get POA&M item by ID in a system
*EmassClient::POAMApi* | [**update_poam_by_system_id**](docs/POAMApi.md#update_poam_by_system_id) | **PUT** /api/systems/{systemId}/poams | Update one or many POA&M items in a system
*EmassClient::RegistrationApi* | [**register_user**](docs/RegistrationApi.md#register_user) | **POST** /api/api-key | Register user certificate and obtain an API key
*EmassClient::StaticCodeScansApi* | [**add_static_code_scans_by_system_id**](docs/StaticCodeScansApi.md#add_static_code_scans_by_system_id) | **POST** /api/systems/{systemId}/static-code-scans | Upload static code scans or Clear static code scans
*EmassClient::SystemRolesApi* | [**get_system_roles**](docs/SystemRolesApi.md#get_system_roles) | **GET** /api/system-roles | Get available roles
*EmassClient::SystemRolesApi* | [**get_system_roles_by_category_id**](docs/SystemRolesApi.md#get_system_roles_by_category_id) | **GET** /api/system-roles/{roleCategory} | Get system roles
*EmassClient::SystemsApi* | [**get_system**](docs/SystemsApi.md#get_system) | **GET** /api/systems/{systemId} | Get system information for a specific system
*EmassClient::SystemsApi* | [**get_systems**](docs/SystemsApi.md#get_systems) | **GET** /api/systems | Get system information
*EmassClient::TestApi* | [**test_connection**](docs/TestApi.md#test_connection) | **GET** /api | Test connection to the API
*EmassClient::TestResultsApi* | [**add_test_results_by_system_id**](docs/TestResultsApi.md#add_test_results_by_system_id) | **POST** /api/systems/{systemId}/test-results | Add one or many test results in a system
*EmassClient::TestResultsApi* | [**get_system_test_results**](docs/TestResultsApi.md#get_system_test_results) | **GET** /api/systems/{systemId}/test-results | Get one or many test results in a system
*EmassClient::WorkflowDefinitionsApi* | [**get_workflow_definitions**](docs/WorkflowDefinitionsApi.md#get_workflow_definitions) | **GET** /api/workflows/definitions | Get workflow definitions in a site
*EmassClient::WorkflowInstancesApi* | [**get_system_workflow_instances**](docs/WorkflowInstancesApi.md#get_system_workflow_instances) | **GET** /api/workflows/instances | Get workflow instances in a site
*EmassClient::WorkflowInstancesApi* | [**get_system_workflow_instances_by_workflow_instance_id**](docs/WorkflowInstancesApi.md#get_system_workflow_instances_by_workflow_instance_id) | **GET** /api/workflows/instances/{workflowInstanceId} | Get workflow instance by ID


## Documentation for Models

 - [EmassClient::ArtifactsGet](docs/ArtifactsGet.md)
 - [EmassClient::ArtifactsRequestDeleteBodyInner](docs/ArtifactsRequestDeleteBodyInner.md)
 - [EmassClient::ArtifactsResponseDel](docs/ArtifactsResponseDel.md)
 - [EmassClient::ArtifactsResponseDelDataInner](docs/ArtifactsResponseDelDataInner.md)
 - [EmassClient::ArtifactsResponseGet](docs/ArtifactsResponseGet.md)
 - [EmassClient::ArtifactsResponsePutPost](docs/ArtifactsResponsePutPost.md)
 - [EmassClient::ArtifactsResponsePutPostDataInner](docs/ArtifactsResponsePutPostDataInner.md)
 - [EmassClient::CacGet](docs/CacGet.md)
 - [EmassClient::CacResponseGet](docs/CacResponseGet.md)
 - [EmassClient::CacResponsePost](docs/CacResponsePost.md)
 - [EmassClient::CacResponsePostDataInner](docs/CacResponsePostDataInner.md)
 - [EmassClient::CloudResourcesPost](docs/CloudResourcesPost.md)
 - [EmassClient::CloudResourcesResponsePost](docs/CloudResourcesResponsePost.md)
 - [EmassClient::CmmcGet](docs/CmmcGet.md)
 - [EmassClient::CmmcResponseGet](docs/CmmcResponseGet.md)
 - [EmassClient::ConnectivityCcsd](docs/ConnectivityCcsd.md)
 - [EmassClient::ContainersResourcesPost](docs/ContainersResourcesPost.md)
 - [EmassClient::ContainersResponsePost](docs/ContainersResponsePost.md)
 - [EmassClient::ControlsGet](docs/ControlsGet.md)
 - [EmassClient::ControlsPut](docs/ControlsPut.md)
 - [EmassClient::ControlsResponseGet](docs/ControlsResponseGet.md)
 - [EmassClient::ControlsResponsePut](docs/ControlsResponsePut.md)
 - [EmassClient::DefinitionTransitions](docs/DefinitionTransitions.md)
 - [EmassClient::InstancesTransitions](docs/InstancesTransitions.md)
 - [EmassClient::MilestoneResponseGet](docs/MilestoneResponseGet.md)
 - [EmassClient::MilestoneResponseGetMilestone](docs/MilestoneResponseGetMilestone.md)
 - [EmassClient::MilestoneResponsePost](docs/MilestoneResponsePost.md)
 - [EmassClient::MilestoneResponsePut](docs/MilestoneResponsePut.md)
 - [EmassClient::MilestonesGet](docs/MilestonesGet.md)
 - [EmassClient::MilestonesPutPostDelete](docs/MilestonesPutPostDelete.md)
 - [EmassClient::MilestonesRequestDeleteBodyInner](docs/MilestonesRequestDeleteBodyInner.md)
 - [EmassClient::MilestonesRequiredPost](docs/MilestonesRequiredPost.md)
 - [EmassClient::MilestonesRequiredPut](docs/MilestonesRequiredPut.md)
 - [EmassClient::PacGet](docs/PacGet.md)
 - [EmassClient::PacPost](docs/PacPost.md)
 - [EmassClient::PacResponseGet](docs/PacResponseGet.md)
 - [EmassClient::PacResponsePost](docs/PacResponsePost.md)
 - [EmassClient::PoamGet](docs/PoamGet.md)
 - [EmassClient::PoamPostPutDel](docs/PoamPostPutDel.md)
 - [EmassClient::PoamRequestDeleteBodyInner](docs/PoamRequestDeleteBodyInner.md)
 - [EmassClient::PoamResponseDelete](docs/PoamResponseDelete.md)
 - [EmassClient::PoamResponseGetPoams](docs/PoamResponseGetPoams.md)
 - [EmassClient::PoamResponseGetSystems](docs/PoamResponseGetSystems.md)
 - [EmassClient::PoamResponsePost](docs/PoamResponsePost.md)
 - [EmassClient::PoamResponsePut](docs/PoamResponsePut.md)
 - [EmassClient::Register](docs/Register.md)
 - [EmassClient::RegisterData](docs/RegisterData.md)
 - [EmassClient::RegisterUserRequestPostBody](docs/RegisterUserRequestPostBody.md)
 - [EmassClient::Response200](docs/Response200.md)
 - [EmassClient::Response201](docs/Response201.md)
 - [EmassClient::Response201Meta](docs/Response201Meta.md)
 - [EmassClient::Response400](docs/Response400.md)
 - [EmassClient::Response400Meta](docs/Response400Meta.md)
 - [EmassClient::Response401](docs/Response401.md)
 - [EmassClient::Response401Meta](docs/Response401Meta.md)
 - [EmassClient::Response403](docs/Response403.md)
 - [EmassClient::Response403Meta](docs/Response403Meta.md)
 - [EmassClient::Response404](docs/Response404.md)
 - [EmassClient::Response405](docs/Response405.md)
 - [EmassClient::Response405Meta](docs/Response405Meta.md)
 - [EmassClient::Response411](docs/Response411.md)
 - [EmassClient::Response411Meta](docs/Response411Meta.md)
 - [EmassClient::Response490](docs/Response490.md)
 - [EmassClient::Response490Meta](docs/Response490Meta.md)
 - [EmassClient::Response500](docs/Response500.md)
 - [EmassClient::Response500Meta](docs/Response500Meta.md)
 - [EmassClient::RoleCategory](docs/RoleCategory.md)
 - [EmassClient::Roles](docs/Roles.md)
 - [EmassClient::Ssps](docs/Ssps.md)
 - [EmassClient::Stage](docs/Stage.md)
 - [EmassClient::StaticCodeApplication](docs/StaticCodeApplication.md)
 - [EmassClient::StaticCodePost](docs/StaticCodePost.md)
 - [EmassClient::StaticCodeRequestPostBody](docs/StaticCodeRequestPostBody.md)
 - [EmassClient::StaticCodeRequestPostBodyApplication](docs/StaticCodeRequestPostBodyApplication.md)
 - [EmassClient::StaticCodeResponsePost](docs/StaticCodeResponsePost.md)
 - [EmassClient::Success200Response](docs/Success200Response.md)
 - [EmassClient::Success200ResponseDataInner](docs/Success200ResponseDataInner.md)
 - [EmassClient::SystemResponse](docs/SystemResponse.md)
 - [EmassClient::SystemRolesCategoryResponse](docs/SystemRolesCategoryResponse.md)
 - [EmassClient::SystemRolesResponse](docs/SystemRolesResponse.md)
 - [EmassClient::SystemRolesResponseDataInner](docs/SystemRolesResponseDataInner.md)
 - [EmassClient::Systems](docs/Systems.md)
 - [EmassClient::SystemsResponse](docs/SystemsResponse.md)
 - [EmassClient::Test](docs/Test.md)
 - [EmassClient::TestData](docs/TestData.md)
 - [EmassClient::TestResultsGet](docs/TestResultsGet.md)
 - [EmassClient::TestResultsPost](docs/TestResultsPost.md)
 - [EmassClient::TestResultsResponseGet](docs/TestResultsResponseGet.md)
 - [EmassClient::TestResultsResponsePost](docs/TestResultsResponsePost.md)
 - [EmassClient::Users](docs/Users.md)
 - [EmassClient::WorkflowDefinitionGet](docs/WorkflowDefinitionGet.md)
 - [EmassClient::WorkflowDefinitionResponseGet](docs/WorkflowDefinitionResponseGet.md)
 - [EmassClient::WorkflowInstanceGet](docs/WorkflowInstanceGet.md)
 - [EmassClient::WorkflowInstanceResponseGet](docs/WorkflowInstanceResponseGet.md)
 - [EmassClient::WorkflowInstancesGet](docs/WorkflowInstancesGet.md)
 - [EmassClient::WorkflowInstancesResponseGet](docs/WorkflowInstancesResponseGet.md)
 - [EmassClient::WorkflowInstancesResponseGetPagination](docs/WorkflowInstancesResponseGetPagination.md)


## Documentation for Authorization


### apiKey


- **Type**: API key
- **API key parameter name**: api-key
- **Location**: HTTP header

### mockType


- **Type**: API key
- **API key parameter name**: Prefer
- **Location**: HTTP header

### userId


- **Type**: API key
- **API key parameter name**: user-uid
- **Location**: HTTP header
