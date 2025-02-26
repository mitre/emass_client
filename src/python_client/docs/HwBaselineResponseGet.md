# HwBaselineResponseGet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Response200**](Response200.md) |  | [optional] 
**data** | [**List[HwBaselineResponseGetDataInner]**](HwBaselineResponseGetDataInner.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from emass_client.models.hw_baseline_response_get import HwBaselineResponseGet

# TODO update the JSON string below
json = "{}"
# create an instance of HwBaselineResponseGet from a JSON string
hw_baseline_response_get_instance = HwBaselineResponseGet.from_json(json)
# print the JSON string representation of the object
print(HwBaselineResponseGet.to_json())

# convert the object into a dict
hw_baseline_response_get_dict = hw_baseline_response_get_instance.to_dict()
# create an instance of HwBaselineResponseGet from a dict
hw_baseline_response_get_from_dict = HwBaselineResponseGet.from_dict(hw_baseline_response_get_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


