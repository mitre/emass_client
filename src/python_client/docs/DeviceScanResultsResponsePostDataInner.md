# DeviceScanResultsResponsePostDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filename** | **str** | [Required] single binary file. Specific file extensions are expected depending upon the scanType parameter. | [optional] 
**assets_imported** | **int** | Number of assets imported from the scan file. | [optional] 
**success** | **bool** |  | [optional] 
**system_id** | **int** |  | [optional] 
**errors** | **List[object]** |  | [optional] 

## Example

```python
from emass_client.models.device_scan_results_response_post_data_inner import DeviceScanResultsResponsePostDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceScanResultsResponsePostDataInner from a JSON string
device_scan_results_response_post_data_inner_instance = DeviceScanResultsResponsePostDataInner.from_json(json)
# print the JSON string representation of the object
print(DeviceScanResultsResponsePostDataInner.to_json())

# convert the object into a dict
device_scan_results_response_post_data_inner_dict = device_scan_results_response_post_data_inner_instance.to_dict()
# create an instance of DeviceScanResultsResponsePostDataInner from a dict
device_scan_results_response_post_data_inner_from_dict = DeviceScanResultsResponsePostDataInner.from_dict(device_scan_results_response_post_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


