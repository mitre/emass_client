# emass_client.POAMApi

All URIs are relative to *http://localhost:4010*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_poam_by_system_id**](POAMApi.md#add_poam_by_system_id) | **POST** /api/systems/{systemId}/poams | Add one or many POA&amp;M items in a system
[**delete_poam**](POAMApi.md#delete_poam) | **DELETE** /api/systems/{systemId}/poams | Remove one or many POA&amp;M items in a system
[**get_system_poams**](POAMApi.md#get_system_poams) | **GET** /api/systems/{systemId}/poams | Get one or many POA&amp;M items in a system
[**get_system_poams_by_poam_id**](POAMApi.md#get_system_poams_by_poam_id) | **GET** /api/systems/{systemId}/poams/{poamId} | Get POA&amp;M item by ID in a system
[**update_poam_by_system_id**](POAMApi.md#update_poam_by_system_id) | **PUT** /api/systems/{systemId}/poams | Update one or many POA&amp;M items in a system


# **add_poam_by_system_id**
> PoamResponsePostPutDelete add_poam_by_system_id(system_id, poam_required_fields)

Add one or many POA&M items in a system

Add a POA&M for given `systemId`

**Request Body Required Fields**
<table>
  <thead>
    <tr><th><b>Field</b></th><th><b>Require/Condition</b></th></tr>
  </thead>
  <tbody>
    <tr><td><code>status</code></td><td>Always (every POST)</td></tr>
    <tr><td><code>vulnerabilityDescription</code></td><td>Always (every POST)</td></tr>
    <tr><td><code>sourceIdentifyingVulnerability</code></td><td>Always (every POST)</td></tr>
    <tr><td><code>pocOrganization</code></td><td>Always (every POST)</td></tr>
    <tr><td><code>resources</code></td><td>Always (every POST)</td></tr>
    <tr><td><code>identifiedInCFOAuditOrOtherReview</code></td><td>Required for VA. Optional for Army and USCG.</td></tr>
    <tr><td><code>scheduledCompletionDate</code></td><td>Required for ongoing and completed POA&M items</td></tr>
    <tr><td><code>pocFirstName</code></td><td>Only if Last Name, Email, or Phone Number have data</td></tr>
    <tr><td><code>pocLastName</code></td><td>Only if First Name, Email, or Phone Number have data</td></tr>
    <tr><td><code>pocEmail</code></td><td>Only if First Name, Last Name, or Phone Number have data</td></tr>
    <tr><td><code>pocPhoneNumber</code></td><td>Only if First Name, Last Name, or Email have data</td></tr>
    <tr><td><code>completionDate</code></td><td>For completed POA&M Item only</td></tr>
    <tr><td><code>comments</code></td><td>For completed or Risk Accepted POA&M Items only</td></tr>
  </tbody>
</table>

**NOTE**: Certain eMASS instances also require the Risk Analysis fields to be populated:
  - `severity`
  - `relevanceOfThreat`
  - `likelihood`
  - `impact`
  - `residualRiskLevel`
  - `mitigations`

</br>
**Business Rules**

The following rules apply to the Review Status `status` field value:
<table>
  <thead><tr><th><b>Value</b></th><th><b>Rule</b></th></tr></thead>
  <tbody>
    <tr><td><b>Not Approved</b></td><td>POA&M cannot be saved if Milestone Scheduled Completion Date exceeds POA&M Item Scheduled Completion Date</td></tr>
    <tr><td><b>Approved</b></td><td>POA&M can only be saved if Milestone Scheduled Completion Date exceeds POA&M Item Scheduled Completion Date</td></tr>
    <tr><td></td><td>Are required to have a Severity Value assigned</td></tr>
    <tr><td><b>Completed</b> or <b>Ongoing</b></td><td>Cannot be saved without Milestones</td></tr>
    <tr><td><b>Risk Accepted</b></td><td>POA&M Item cannot be saved with a Scheduled Completion Date <code>scheduledCompletionDate</code> or have Milestones</td></tr>
    <tr><td><b>Approved</b> or <b>Completed</b> or <b>Ongoing</b></td><td>Cannot update Scheduled Completion Date</td></tr>
 </tbody>
</table>

**Additional Rules**
- POA&M Item cannot be saved if associated Security Control or AP is inherited.
- Completed POA&M Item cannot be saved if Completion Date (`completionDate`) is in the future.
- POA&M Items cannot be updated if they are included in an active package.
- Archived POA&M Items cannot be updated.
- POA&M Items with a status of "Not Applicable" will be updated through test result creation.
- If the Security Control or Assessment Procedure does not exist in the system, the POA&M Item maybe imported at the System Level.


**Fields Characters Limitation**
- POA&M Item cannot be saved if the Point of Contact (POC) fields exceed 100 characters:
  - `pocOrganization` `pocFirstName`, `pocLastName`, `pocEmail`, `pocPhoneNumber`
- POA&M Item cannot be saved if Resources (`resource`) field exceeds 250 characters
- POA&M Item cannot be saved if the following fields exceeds 2,000 characters:
  - `mitigations`, `sourceIdentifyingVulnerability`, `comments`
  - Milestones Field: `description`
- POA&M Items cannot be saved if Milestone Description (`description`) exceeds 2,000 characters.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (mockType):
* Api Key Authentication (userId):

```python
import emass_client
from emass_client.models.poam_response_post_put_delete import PoamResponsePostPutDelete
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
    api_instance = emass_client.POAMApi(api_client)
    system_id = 35 # int | **System Id**: The unique system record identifier.
    poam_required_fields = [emass_client.PoamRequiredFields()] # List[PoamRequiredFields] | Example request body to add POA&M(s) to a system (systemId)

    try:
        # Add one or many POA&M items in a system
        api_response = api_instance.add_poam_by_system_id(system_id, poam_required_fields)
        print("The response of POAMApi->add_poam_by_system_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling POAMApi->add_poam_by_system_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **int**| **System Id**: The unique system record identifier. | 
 **poam_required_fields** | [**List[PoamRequiredFields]**](PoamRequiredFields.md)| Example request body to add POA&amp;M(s) to a system (systemId) | 

### Return type

[**PoamResponsePostPutDelete**](PoamResponsePostPutDelete.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**405** | Method Not Allowed |  -  |
**411** | Length Required |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_poam**
> PoamResponsePostPutDelete delete_poam(system_id, poam_request_delete_body_inner)

Remove one or many POA&M items in a system

Remove the POA&M matching `systemId` path parameter and `poamId` Request Body<br>

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (mockType):
* Api Key Authentication (userId):

```python
import emass_client
from emass_client.models.poam_request_delete_body_inner import PoamRequestDeleteBodyInner
from emass_client.models.poam_response_post_put_delete import PoamResponsePostPutDelete
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
    api_instance = emass_client.POAMApi(api_client)
    system_id = 35 # int | **System Id**: The unique system record identifier.
    poam_request_delete_body_inner = [emass_client.PoamRequestDeleteBodyInner()] # List[PoamRequestDeleteBodyInner] | Delete the given POA&M Id

    try:
        # Remove one or many POA&M items in a system
        api_response = api_instance.delete_poam(system_id, poam_request_delete_body_inner)
        print("The response of POAMApi->delete_poam:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling POAMApi->delete_poam: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **int**| **System Id**: The unique system record identifier. | 
 **poam_request_delete_body_inner** | [**List[PoamRequestDeleteBodyInner]**](PoamRequestDeleteBodyInner.md)| Delete the given POA&amp;M Id | 

### Return type

[**PoamResponsePostPutDelete**](PoamResponsePostPutDelete.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_poams**
> PoamResponseGetSystems get_system_poams(system_id, scheduled_completion_date_start=scheduled_completion_date_start, scheduled_completion_date_end=scheduled_completion_date_end, control_acronyms=control_acronyms, assessment_procedures=assessment_procedures, ccis=ccis, system_only=system_only)

Get one or many POA&M items in a system

Returns system(s) containing POA&M items for matching parameters.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (mockType):
* Api Key Authentication (userId):

```python
import emass_client
from emass_client.models.poam_response_get_systems import PoamResponseGetSystems
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
    api_instance = emass_client.POAMApi(api_client)
    system_id = 35 # int | **System Id**: The unique system record identifier.
    scheduled_completion_date_start = 'scheduled_completion_date_start_example' # str | **Date Started**: Filter query by the scheduled completion start date (Unix date format). (optional)
    scheduled_completion_date_end = 'scheduled_completion_date_end_example' # str | **Date Ended**: Filter query by the scheduled completion start date (Unix date format). (optional)
    control_acronyms = 'control_acronyms_example' # str | **Control Acronym**: Filter query by given system acronym (single value or comma separated). (optional)
    assessment_procedures = 'assessment_procedures_example' # str | **Assessment Procedure**: Filter query by given Security Control Assessment Procedure (single value or comma separated). (optional)
    ccis = 'ccis_example' # str | **CCI System**: Filter query by Control Correlation Identifiers (CCIs) (single value or comma separated). (optional)
    system_only = True # bool | **Systems Only**: Indicates that only system(s) information is retrieved. (optional) (default to True)

    try:
        # Get one or many POA&M items in a system
        api_response = api_instance.get_system_poams(system_id, scheduled_completion_date_start=scheduled_completion_date_start, scheduled_completion_date_end=scheduled_completion_date_end, control_acronyms=control_acronyms, assessment_procedures=assessment_procedures, ccis=ccis, system_only=system_only)
        print("The response of POAMApi->get_system_poams:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling POAMApi->get_system_poams: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **int**| **System Id**: The unique system record identifier. | 
 **scheduled_completion_date_start** | **str**| **Date Started**: Filter query by the scheduled completion start date (Unix date format). | [optional] 
 **scheduled_completion_date_end** | **str**| **Date Ended**: Filter query by the scheduled completion start date (Unix date format). | [optional] 
 **control_acronyms** | **str**| **Control Acronym**: Filter query by given system acronym (single value or comma separated). | [optional] 
 **assessment_procedures** | **str**| **Assessment Procedure**: Filter query by given Security Control Assessment Procedure (single value or comma separated). | [optional] 
 **ccis** | **str**| **CCI System**: Filter query by Control Correlation Identifiers (CCIs) (single value or comma separated). | [optional] 
 **system_only** | **bool**| **Systems Only**: Indicates that only system(s) information is retrieved. | [optional] [default to True]

### Return type

[**PoamResponseGetSystems**](PoamResponseGetSystems.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**405** | Method Not Allowed |  -  |
**490** | API Rule Failed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_poams_by_poam_id**
> PoamResponseGetPoams get_system_poams_by_poam_id(system_id, poam_id)

Get POA&M item by ID in a system

Returns system(s) containing POA&M items for matching parameters.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (mockType):
* Api Key Authentication (userId):

```python
import emass_client
from emass_client.models.poam_response_get_poams import PoamResponseGetPoams
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
    api_instance = emass_client.POAMApi(api_client)
    system_id = 35 # int | **System Id**: The unique system record identifier.
    poam_id = 45 # int | **POA&M Id**: The unique POA&M record identifier.

    try:
        # Get POA&M item by ID in a system
        api_response = api_instance.get_system_poams_by_poam_id(system_id, poam_id)
        print("The response of POAMApi->get_system_poams_by_poam_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling POAMApi->get_system_poams_by_poam_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **int**| **System Id**: The unique system record identifier. | 
 **poam_id** | **int**| **POA&amp;M Id**: The unique POA&amp;M record identifier. | 

### Return type

[**PoamResponseGetPoams**](PoamResponseGetPoams.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**405** | Method Not Allowed |  -  |
**490** | API Rule Failed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_poam_by_system_id**
> PoamResponsePostPutDelete update_poam_by_system_id(system_id, poam_ids)

Update one or many POA&M items in a system

Update a POA&M for given `systemId`<br>

**Request Body Required Fields**
<table>
  <thead>
    <tr><th><b>Field</b></th><th><b>Require/Condition</b></th></tr>
  </thead>
  <tbody>
    <tr><td><code>poamId</code></td><td>Always (every PUT)</td></tr>
    <tr><td><code>displayPoamId</code></td><td>Always (every PUT)</td></tr>
    <tr><td><code>status</code></td><td>Always (every PUT)</td></tr>
    <tr><td><code>vulnerabilityDescription</code></td><td>Always (every PUT)</td></tr>
    <tr><td><code>sourceIdentifyingVulnerability</code></td><td>Always (every PUT)</td></tr>
    <tr><td><code>pocOrganization</code></td><td>Always (every PUT)</td></tr>
    <tr><td><code>resources</code></td><td>Always (every PUT)</td></tr>
    <tr><td><code>identifiedInCFOAuditOrOtherReview</code></td><td>Required for VA. Optional for Army and USCG.</td></tr>
    <tr><td><code>scheduledCompletionDate</code></td><td>Required for ongoing and completed POA&M items</td></tr>
    <tr><td><code>pocFirstName</code></td><td>Only if Last Name, Email, or Phone Number have data</td></tr>
    <tr><td><code>pocLastName</code></td><td>Only if First Name, Email, or Phone Number have data</td></tr>
    <tr><td><code>pocEmail</code></td><td>Only if First Name, Last Name, or Phone Number have data</td></tr>
    <tr><td><code>pocPhoneNumber</code></td><td>Only if First Name, Last Name, or Email have data</td></tr>
    <tr><td><code>completionDate</code></td><td>For completed POA&M Item only</td></tr>
    <tr><td><code>comments</code></td><td>For completed or Risk Accepted POA&M Items only</td></tr>
  </tbody>
</table>

**NOTES**:
- Certain eMASS instances also require the Risk Analysis fields to be populated:
  - `severity`
  - `relevanceOfThreat`
  - `likelihood`
  - `impact`
  - `residualRiskLevel`
  - `mitigations`
- To prevent uploading duplicate/undesired milestones through the POA&M PUT include an `isActive` field for the milestone and set it to equal to false `(isActive=false)`.
</br>

**Business Rules:** See business rules for the POST endpoint

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (mockType):
* Api Key Authentication (userId):

```python
import emass_client
from emass_client.models.poam_response_post_put_delete import PoamResponsePostPutDelete
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
    api_instance = emass_client.POAMApi(api_client)
    system_id = 35 # int | **System Id**: The unique system record identifier.
    poam_ids = [emass_client.PoamIds()] # List[PoamIds] | Example request body for updating a POA&M for a system (systemId)

    try:
        # Update one or many POA&M items in a system
        api_response = api_instance.update_poam_by_system_id(system_id, poam_ids)
        print("The response of POAMApi->update_poam_by_system_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling POAMApi->update_poam_by_system_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **int**| **System Id**: The unique system record identifier. | 
 **poam_ids** | [**List[PoamIds]**](PoamIds.md)| Example request body for updating a POA&amp;M for a system (systemId) | 

### Return type

[**PoamResponsePostPutDelete**](PoamResponsePostPutDelete.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

