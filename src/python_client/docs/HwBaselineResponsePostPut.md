# HwBaselineResponsePostPut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Response200**](Response200.md) |  | [optional] 
**data** | [**List[HwBaselineResponsePostPutDataInner]**](HwBaselineResponsePostPutDataInner.md) |  | [optional] 

## Example

```python
from emass_client.models.hw_baseline_response_post_put import HwBaselineResponsePostPut

# TODO update the JSON string below
json = "{}"
# create an instance of HwBaselineResponsePostPut from a JSON string
hw_baseline_response_post_put_instance = HwBaselineResponsePostPut.from_json(json)
# print the JSON string representation of the object
print(HwBaselineResponsePostPut.to_json())

# convert the object into a dict
hw_baseline_response_post_put_dict = hw_baseline_response_post_put_instance.to_dict()
# create an instance of HwBaselineResponsePostPut from a dict
hw_baseline_response_post_put_from_dict = HwBaselineResponsePostPut.from_dict(hw_baseline_response_post_put_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


