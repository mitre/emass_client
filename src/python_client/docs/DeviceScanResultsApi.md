# emass_client.DeviceScanResultsApi

All URIs are relative to *http://localhost:4010*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_scan_results_by_system_id**](DeviceScanResultsApi.md#add_scan_results_by_system_id) | **POST** /api/systems/{systemId}/device-scan-results | Add device scans in a system


# **add_scan_results_by_system_id**
> DeviceScanResultsResponsePost add_scan_results_by_system_id(system_id, scan_type, filename, is_baseline=is_baseline)

Add device scans in a system


**Request Body Required Field**
- `scanType`

Scan Type Allow Values:

<ul>
  <li>acasAsrArf (.zip)</li>
  <li>acasNessus</li>
  <li>disaStigViewerCklCklb (.ckl or .cklb)</li>
  <li>disaStigViewerCmrs</li>
  <li>policyAuditor (.zip)</li>       
  <li>scapComplianceChecker</li>
</ul>


<strong>Business Rules</strong><br>

The body of a request through the Device Scan Results POST endpoint accepts a single binary file.
Specific file extensions are expected depending upon the scanType parameter. For example, .ckl or
.cklb files are accepted when using scanType is set to disaStigViewerCklCklb.

When set to acasAsrArf or policyAuditor, a .zip file is expected which should contain a single
scan result (for example, a single pair of .asr and .arf files). Single files are expected for
all other scan types as this endpoint requires files to be uploaded consecutively as opposed to in bulk.

Current scan types that are supported:
<ul>
  <li>ACAS: ASR/ARF</li>
  <li>ACAS: NESSUS</li>
  <li>DISA STIG Viewer: CKL/CKLB</li>
  <li>DISA STIG Viewer: CMRS</li>
  <li>Policy Auditor</li>       
  <li>SCAP Compliance Checker</li>
</ul>

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (mockType):
* Api Key Authentication (userId):

```python
import emass_client
from emass_client.models.device_scan_results_response_post import DeviceScanResultsResponsePost
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
    api_instance = emass_client.DeviceScanResultsApi(api_client)
    system_id = 35 # int | **System Id**: The unique system record identifier.
    scan_type = disaStigViewerCklCklb # str | **Scan Type**: The file scan type to upload (default to disaStigViewerCklCklb)
    filename = None # bytearray | The file to upload. Can be a single file or a .zip file.
    is_baseline = False # bool | **Is Baseline**: Indicates that the imported file represents a baseline scan that includes all findings and results. Importing as a baseline scan, which assumes a common set of scan policies are used when conducting a scan, will replace a device's findings for a specific Benchmark. Applicable to ASR/ARF scans only.  (optional) (default to False)

    try:
        # Add device scans in a system
        api_response = api_instance.add_scan_results_by_system_id(system_id, scan_type, filename, is_baseline=is_baseline)
        print("The response of DeviceScanResultsApi->add_scan_results_by_system_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceScanResultsApi->add_scan_results_by_system_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **int**| **System Id**: The unique system record identifier. | 
 **scan_type** | **str**| **Scan Type**: The file scan type to upload | [default to disaStigViewerCklCklb]
 **filename** | **bytearray**| The file to upload. Can be a single file or a .zip file. | 
 **is_baseline** | **bool**| **Is Baseline**: Indicates that the imported file represents a baseline scan that includes all findings and results. Importing as a baseline scan, which assumes a common set of scan policies are used when conducting a scan, will replace a device&#39;s findings for a specific Benchmark. Applicable to ASR/ARF scans only.  | [optional] [default to False]

### Return type

[**DeviceScanResultsResponsePost**](DeviceScanResultsResponsePost.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

 - **Content-Type**: multipart/form-data
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

