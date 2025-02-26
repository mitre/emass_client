# SwBaselineRequiredFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**software_vendor** | **str** | [Required] Vendor of the software asset. | [optional] 
**software_name** | **str** | [Required] Name of the software asset. | [optional] 
**version** | **str** | [Required] Version of the software asset. | [optional] 

## Example

```python
from emass_client.models.sw_baseline_required_fields import SwBaselineRequiredFields

# TODO update the JSON string below
json = "{}"
# create an instance of SwBaselineRequiredFields from a JSON string
sw_baseline_required_fields_instance = SwBaselineRequiredFields.from_json(json)
# print the JSON string representation of the object
print(SwBaselineRequiredFields.to_json())

# convert the object into a dict
sw_baseline_required_fields_dict = sw_baseline_required_fields_instance.to_dict()
# create an instance of SwBaselineRequiredFields from a dict
sw_baseline_required_fields_from_dict = SwBaselineRequiredFields.from_dict(sw_baseline_required_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


