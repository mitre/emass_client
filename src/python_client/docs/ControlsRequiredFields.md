# ControlsRequiredFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acronym** | **str** | [Required] Acronym of the system record. | [optional] 
**responsible_entities** | **str** | [Required] Include written description of Responsible Entities that are responsible for the Security Control. Character Limit 2,000. | [optional] 
**control_designation** | **str** | [Required] Control designations | [optional] 
**estimated_completion_date** | **int** | [Required] Field is required for Implementation Plan. Unix time format. | [optional] 
**implementation_narrative** | **str** | [Required] Includes security control comments. Character Limit 2,000. | [optional] 

## Example

```python
from emass_client.models.controls_required_fields import ControlsRequiredFields

# TODO update the JSON string below
json = "{}"
# create an instance of ControlsRequiredFields from a JSON string
controls_required_fields_instance = ControlsRequiredFields.from_json(json)
# print the JSON string representation of the object
print(ControlsRequiredFields.to_json())

# convert the object into a dict
controls_required_fields_dict = controls_required_fields_instance.to_dict()
# create an instance of ControlsRequiredFields from a dict
controls_required_fields_from_dict = ControlsRequiredFields.from_dict(controls_required_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


