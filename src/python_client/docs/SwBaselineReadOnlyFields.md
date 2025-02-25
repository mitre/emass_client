# SwBaselineReadOnlyFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**software_id** | **str** | [Read-Only] GUID identifying the specific software asset. | [optional] 

## Example

```python
from emass_client.models.sw_baseline_read_only_fields import SwBaselineReadOnlyFields

# TODO update the JSON string below
json = "{}"
# create an instance of SwBaselineReadOnlyFields from a JSON string
sw_baseline_read_only_fields_instance = SwBaselineReadOnlyFields.from_json(json)
# print the JSON string representation of the object
print(SwBaselineReadOnlyFields.to_json())

# convert the object into a dict
sw_baseline_read_only_fields_dict = sw_baseline_read_only_fields_instance.to_dict()
# create an instance of SwBaselineReadOnlyFields from a dict
sw_baseline_read_only_fields_from_dict = SwBaselineReadOnlyFields.from_dict(sw_baseline_read_only_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


