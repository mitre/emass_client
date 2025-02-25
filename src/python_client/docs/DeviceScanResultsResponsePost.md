# DeviceScanResultsResponsePost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Response200**](Response200.md) |  | [optional] 
**data** | [**List[DeviceScanResultsResponsePostDataInner]**](DeviceScanResultsResponsePostDataInner.md) |  | [optional] 

## Example

```python
from emass_client.models.device_scan_results_response_post import DeviceScanResultsResponsePost

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceScanResultsResponsePost from a JSON string
device_scan_results_response_post_instance = DeviceScanResultsResponsePost.from_json(json)
# print the JSON string representation of the object
print(DeviceScanResultsResponsePost.to_json())

# convert the object into a dict
device_scan_results_response_post_dict = device_scan_results_response_post_instance.to_dict()
# create an instance of DeviceScanResultsResponsePost from a dict
device_scan_results_response_post_from_dict = DeviceScanResultsResponsePost.from_dict(device_scan_results_response_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


