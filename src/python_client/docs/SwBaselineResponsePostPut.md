# SwBaselineResponsePostPut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Response200**](Response200.md) |  | [optional] 
**data** | [**List[SwBaselineResponsePostPutDataInner]**](SwBaselineResponsePostPutDataInner.md) |  | [optional] 

## Example

```python
from emass_client.models.sw_baseline_response_post_put import SwBaselineResponsePostPut

# TODO update the JSON string below
json = "{}"
# create an instance of SwBaselineResponsePostPut from a JSON string
sw_baseline_response_post_put_instance = SwBaselineResponsePostPut.from_json(json)
# print the JSON string representation of the object
print(SwBaselineResponsePostPut.to_json())

# convert the object into a dict
sw_baseline_response_post_put_dict = sw_baseline_response_post_put_instance.to_dict()
# create an instance of SwBaselineResponsePostPut from a dict
sw_baseline_response_post_put_from_dict = SwBaselineResponsePostPut.from_dict(sw_baseline_response_post_put_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


