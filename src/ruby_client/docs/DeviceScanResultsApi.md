# EmassClient::DeviceScanResultsApi

All URIs are relative to *http://localhost:4010*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**add_scan_results_by_system_id**](DeviceScanResultsApi.md#add_scan_results_by_system_id) | **POST** /api/systems/{systemId}/device-scan-results | Add device scans in a system |


## add_scan_results_by_system_id

> <DeviceScanResultsResponsePost> add_scan_results_by_system_id(system_id, scan_type, filename, opts)

Add device scans in a system

 **Request Body Required Field** - `scanType`  Scan Type Allow Values:  <ul>   <li>acasAsrArf (.zip)</li>   <li>acasNessus</li>   <li>disaStigViewerCklCklb (.ckl or .cklb)</li>   <li>disaStigViewerCmrs</li>   <li>policyAuditor (.zip)</li>          <li>scapComplianceChecker</li> </ul>   <strong>Business Rules</strong><br>  The body of a request through the Device Scan Results POST endpoint accepts a single binary file. Specific file extensions are expected depending upon the scanType parameter. For example, .ckl or .cklb files are accepted when using scanType is set to disaStigViewerCklCklb.  When set to acasAsrArf or policyAuditor, a .zip file is expected which should contain a single scan result (for example, a single pair of .asr and .arf files). Single files are expected for all other scan types as this endpoint requires files to be uploaded consecutively as opposed to in bulk.  Current scan types that are supported: <ul>   <li>ACAS: ASR/ARF</li>   <li>ACAS: NESSUS</li>   <li>DISA STIG Viewer: CKL/CKLB</li>   <li>DISA STIG Viewer: CMRS</li>   <li>Policy Auditor</li>          <li>SCAP Compliance Checker</li> </ul>

### Examples

```ruby
require 'time'
require 'emass_client'
# setup authorization
EmassClient.configure do |config|
  # Configure API key authorization: apiKey
  config.api_key['api-key'] = 'YOUR API KEY'
  # Uncomment the following line to set a prefix for the API key, e.g. 'Bearer' (defaults to nil)
  # config.api_key_prefix['api-key'] = 'Bearer'

  # Configure API key authorization: mockType
  config.api_key['Prefer'] = 'YOUR API KEY'
  # Uncomment the following line to set a prefix for the API key, e.g. 'Bearer' (defaults to nil)
  # config.api_key_prefix['Prefer'] = 'Bearer'

  # Configure API key authorization: userId
  config.api_key['user-uid'] = 'YOUR API KEY'
  # Uncomment the following line to set a prefix for the API key, e.g. 'Bearer' (defaults to nil)
  # config.api_key_prefix['user-uid'] = 'Bearer'
end

api_instance = EmassClient::DeviceScanResultsApi.new
system_id = 35 # Integer | **System Id**: The unique system record identifier.
scan_type = 'acasAsrArf' # String | **Scan Type**: The file scan type to upload
filename = File.new('/path/to/some/file') # File | The file to upload. Can be a single file or a .zip file.
opts = {
  is_baseline: true # Boolean | **Is Baseline**: Indicates that the imported file represents a baseline scan that includes all findings and results. Importing as a baseline scan, which assumes a common set of scan policies are used when conducting a scan, will replace a device's findings for a specific Benchmark. Applicable to ASR/ARF scans only. 
}

begin
  # Add device scans in a system
  result = api_instance.add_scan_results_by_system_id(system_id, scan_type, filename, opts)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling DeviceScanResultsApi->add_scan_results_by_system_id: #{e}"
end
```

#### Using the add_scan_results_by_system_id_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<DeviceScanResultsResponsePost>, Integer, Hash)> add_scan_results_by_system_id_with_http_info(system_id, scan_type, filename, opts)

```ruby
begin
  # Add device scans in a system
  data, status_code, headers = api_instance.add_scan_results_by_system_id_with_http_info(system_id, scan_type, filename, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <DeviceScanResultsResponsePost>
rescue EmassClient::ApiError => e
  puts "Error when calling DeviceScanResultsApi->add_scan_results_by_system_id_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **system_id** | **Integer** | **System Id**: The unique system record identifier. |  |
| **scan_type** | **String** | **Scan Type**: The file scan type to upload | [default to &#39;disaStigViewerCklCklb&#39;] |
| **filename** | **File** | The file to upload. Can be a single file or a .zip file. |  |
| **is_baseline** | **Boolean** | **Is Baseline**: Indicates that the imported file represents a baseline scan that includes all findings and results. Importing as a baseline scan, which assumes a common set of scan policies are used when conducting a scan, will replace a device&#39;s findings for a specific Benchmark. Applicable to ASR/ARF scans only.  | [optional][default to false] |

### Return type

[**DeviceScanResultsResponsePost**](DeviceScanResultsResponsePost.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

