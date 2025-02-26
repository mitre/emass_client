# ControlsConditionalFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**common_control_provider** | **str** | [Conditional] Indicate the type of Common Control Provider for an Inherited Security Control. | [optional] 
**na_justification** | **str** | [Conditional] Provide justification for Security Controls deemed Not Applicable to the system. | [optional] 
**slcm_criticality** | **str** | [Conditional] Criticality of Security Control regarding SLCM. Character Limit &#x3D; 2,000. | [optional] 
**slcm_frequency** | **str** | [Conditional] SLCM frequency | [optional] 
**slcm_method** | **str** | [Conditional] SLCM method utilized | [optional] 
**slcm_reporting** | **str** | [Conditional] Method for reporting Security Control for SLCM. Character Limit &#x3D; 2,000. | [optional] 
**slcm_tracking** | **str** | [Conditional] How Non-Compliant Security Controls will be tracked for SLCM. Character Limit &#x3D; 2,000. | [optional] 
**slcm_comments** | **str** | [Conditional] Additional comments for Security Control regarding SLCM. Character Limit &#x3D; 4,000. | [optional] 

## Example

```python
from emass_client.models.controls_conditional_fields import ControlsConditionalFields

# TODO update the JSON string below
json = "{}"
# create an instance of ControlsConditionalFields from a JSON string
controls_conditional_fields_instance = ControlsConditionalFields.from_json(json)
# print the JSON string representation of the object
print(ControlsConditionalFields.to_json())

# convert the object into a dict
controls_conditional_fields_dict = controls_conditional_fields_instance.to_dict()
# create an instance of ControlsConditionalFields from a dict
controls_conditional_fields_from_dict = ControlsConditionalFields.from_dict(controls_conditional_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


