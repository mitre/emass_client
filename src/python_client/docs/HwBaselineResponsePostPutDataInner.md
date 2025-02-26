# HwBaselineResponsePostPutDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**system_id** | **int** |  | [optional] 
**hardware_id** | **str** |  | [optional] 
**success** | **bool** |  | [optional] 
**errors** | **List[object]** |  | [optional] 

## Example

```python
from emass_client.models.hw_baseline_response_post_put_data_inner import HwBaselineResponsePostPutDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of HwBaselineResponsePostPutDataInner from a JSON string
hw_baseline_response_post_put_data_inner_instance = HwBaselineResponsePostPutDataInner.from_json(json)
# print the JSON string representation of the object
print(HwBaselineResponsePostPutDataInner.to_json())

# convert the object into a dict
hw_baseline_response_post_put_data_inner_dict = hw_baseline_response_post_put_data_inner_instance.to_dict()
# create an instance of HwBaselineResponsePostPutDataInner from a dict
hw_baseline_response_post_put_data_inner_from_dict = HwBaselineResponsePostPutDataInner.from_dict(hw_baseline_response_post_put_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


