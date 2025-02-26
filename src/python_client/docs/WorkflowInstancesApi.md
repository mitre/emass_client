# emass_client.WorkflowInstancesApi

All URIs are relative to *http://localhost:4010*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_system_workflow_instances**](WorkflowInstancesApi.md#get_system_workflow_instances) | **GET** /api/workflows/instances | Get workflow instances in a site
[**get_system_workflow_instances_by_workflow_instance_id**](WorkflowInstancesApi.md#get_system_workflow_instances_by_workflow_instance_id) | **GET** /api/workflows/instances/{workflowInstanceId} | Get workflow instance by ID


# **get_system_workflow_instances**
> WorkflowInstancesResponseGet get_system_workflow_instances(include_comments=include_comments, include_decommission_systems=include_decommission_systems, page_index=page_index, since_date=since_date, status=status)

Get workflow instances in a site

View detailed information on all active and historical workflows filtered by provided parameters.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (mockType):
* Api Key Authentication (userId):

```python
import emass_client
from emass_client.models.workflow_instances_response_get import WorkflowInstancesResponseGet
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
    api_instance = emass_client.WorkflowInstancesApi(api_client)
    include_comments = True # bool | **Include Comments**: If no value is specified, the default returns true to not include transition comments. Note: Corresponds to the Comments textbox that is required at most workflow transitions. Does not include other text input fields such as Terms / Conditions for Authorization.  (optional) (default to True)
    include_decommission_systems = False # bool | **Include Decommission Systems**: If no value is specified, the default returns false to exclude decommissioned systems.  (optional) (default to False)
    page_index = 0 # int | **Page Index**: If no value is specified, the default returns results from the first page with an index of 0. **Note:** Pages contain 1000 workflow instances.  (optional) (default to 0)
    since_date = '1638764040' # str | **Date**: Filter on authorization/assessment date (Unix date format). Note: Filters off the lastEditedDate field. Note: The authorization/assessment decisions on completed workflows can be edited for up to 30 days after the initial decision is made.  (optional)
    status = all # str | **Status**: Filter by status. If no value is specified, the default returns all to include both active and inactive workflows. Note: Any workflows at a current stage of Complete or Cancelled are inactive. Ongoing workflows currently at other stages are active.  (optional) (default to all)

    try:
        # Get workflow instances in a site
        api_response = api_instance.get_system_workflow_instances(include_comments=include_comments, include_decommission_systems=include_decommission_systems, page_index=page_index, since_date=since_date, status=status)
        print("The response of WorkflowInstancesApi->get_system_workflow_instances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowInstancesApi->get_system_workflow_instances: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_comments** | **bool**| **Include Comments**: If no value is specified, the default returns true to not include transition comments. Note: Corresponds to the Comments textbox that is required at most workflow transitions. Does not include other text input fields such as Terms / Conditions for Authorization.  | [optional] [default to True]
 **include_decommission_systems** | **bool**| **Include Decommission Systems**: If no value is specified, the default returns false to exclude decommissioned systems.  | [optional] [default to False]
 **page_index** | **int**| **Page Index**: If no value is specified, the default returns results from the first page with an index of 0. **Note:** Pages contain 1000 workflow instances.  | [optional] [default to 0]
 **since_date** | **str**| **Date**: Filter on authorization/assessment date (Unix date format). Note: Filters off the lastEditedDate field. Note: The authorization/assessment decisions on completed workflows can be edited for up to 30 days after the initial decision is made.  | [optional] 
 **status** | **str**| **Status**: Filter by status. If no value is specified, the default returns all to include both active and inactive workflows. Note: Any workflows at a current stage of Complete or Cancelled are inactive. Ongoing workflows currently at other stages are active.  | [optional] [default to all]

### Return type

[**WorkflowInstancesResponseGet**](WorkflowInstancesResponseGet.md)

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

# **get_system_workflow_instances_by_workflow_instance_id**
> WorkflowInstanceResponseGet get_system_workflow_instances_by_workflow_instance_id(workflow_instance_id)

Get workflow instance by ID

View detailed historical workflow information for `workflowInstanceId`.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (mockType):
* Api Key Authentication (userId):

```python
import emass_client
from emass_client.models.workflow_instance_response_get import WorkflowInstanceResponseGet
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
    api_instance = emass_client.WorkflowInstancesApi(api_client)
    workflow_instance_id = 123 # int | **Workflow Instance Id**: The unique workflow definition identifier.

    try:
        # Get workflow instance by ID
        api_response = api_instance.get_system_workflow_instances_by_workflow_instance_id(workflow_instance_id)
        print("The response of WorkflowInstancesApi->get_system_workflow_instances_by_workflow_instance_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowInstancesApi->get_system_workflow_instances_by_workflow_instance_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_instance_id** | **int**| **Workflow Instance Id**: The unique workflow definition identifier. | 

### Return type

[**WorkflowInstanceResponseGet**](WorkflowInstanceResponseGet.md)

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

