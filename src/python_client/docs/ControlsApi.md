# emass_client.ControlsApi

All URIs are relative to *http://localhost:4010*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_system_controls**](ControlsApi.md#get_system_controls) | **GET** /api/systems/{systemId}/controls | Get control information in a system for one or many controls
[**update_control_by_system_id**](ControlsApi.md#update_control_by_system_id) | **PUT** /api/systems/{systemId}/controls | Update control information in a system for one or many controls


# **get_system_controls**
> ControlsResponseGet get_system_controls(system_id, acronyms=acronyms)

Get control information in a system for one or many controls

Returns system control information for matching `systemId` path parameter

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (mockType):
* Api Key Authentication (userId):

```python
import emass_client
from emass_client.models.controls_response_get import ControlsResponseGet
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
    api_instance = emass_client.ControlsApi(api_client)
    system_id = 35 # int | **System Id**: The unique system record identifier.
    acronyms = 'PM-6' # str | **Acronym**: The system acronym(s) being queried (single value or comma delimited values). (optional) (default to 'PM-6')

    try:
        # Get control information in a system for one or many controls
        api_response = api_instance.get_system_controls(system_id, acronyms=acronyms)
        print("The response of ControlsApi->get_system_controls:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ControlsApi->get_system_controls: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **int**| **System Id**: The unique system record identifier. | 
 **acronyms** | **str**| **Acronym**: The system acronym(s) being queried (single value or comma delimited values). | [optional] [default to &#39;PM-6&#39;]

### Return type

[**ControlsResponseGet**](ControlsResponseGet.md)

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

# **update_control_by_system_id**
> ControlsResponsePut update_control_by_system_id(system_id, controls_required_fields)

Update control information in a system for one or many controls

Update a Control for given `systemId`<br>

**Request Body Required Fields**
- `acronym`
- `responsibleEntities`
- `controlDesignation`
- `estimatedCompletionDate`
- `implementationNarrative`

<br>
**Business Rules**

The following **optional fields** (plus the **Request Body Required Fields**) are required based on the Implementation Status (`implementationStatus`) field value:<br>

<table>
  <thead>
    <tr><th><b>Status</b></th><th><b>Required Fields</b></th></tr>
  </thead>
  <tbody>
    <tr><td><b>Planned</b> or <b>Implemented</b></td><td><code>slcmCriticality, slcmFrequency, slcmMethod, slcmReporting, slcmTracking, slcmComments</code></td></tr>
    <tr><td><b>Not Applicable</b></td><td><code>naJustification</code></td></tr>
    <tr><td><b>Manually Inherited</b></td><td><code>commonControlProvider, slcmCriticality, slcmFrequency, slcmMethod, slcmReporting, slcmTracking, slcmComments</code></td></tr>
  </tbody>
</table>


**NOTES:**
- Risk Assessment information cannot be updated if a Security Control is `Inherited`.
- Risk Assessment information cannot be updated for a DIACAP system record.
- Implementation Plan information cannot be saved if the these fields exceed 2,000 character limits:
  - `naJustification`,`responsibleEntities`,`implementationNarrative`,`slcmCriticality`
  - `slcmFrequency`,`slcmMethod`,`slcmReporting`,`slcmTracking`,`slcmComments`
- Implementation Plan or Risk Assessment information cannot be updated if Security Control does not exist in the system record.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (mockType):
* Api Key Authentication (userId):

```python
import emass_client
from emass_client.models.controls_response_put import ControlsResponsePut
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
    api_instance = emass_client.ControlsApi(api_client)
    system_id = 35 # int | **System Id**: The unique system record identifier.
    controls_required_fields = [emass_client.ControlsRequiredFields()] # List[ControlsRequiredFields] | Example request body for updating an existing control for a given system.

    try:
        # Update control information in a system for one or many controls
        api_response = api_instance.update_control_by_system_id(system_id, controls_required_fields)
        print("The response of ControlsApi->update_control_by_system_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ControlsApi->update_control_by_system_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **int**| **System Id**: The unique system record identifier. | 
 **controls_required_fields** | [**List[ControlsRequiredFields]**](ControlsRequiredFields.md)| Example request body for updating an existing control for a given system. | 

### Return type

[**ControlsResponsePut**](ControlsResponsePut.md)

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

