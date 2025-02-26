# ControlsOptionalFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**implementation_status** | **str** | [Optional] Implementation Status of the Security Control for the information system. | [optional] 
**severity** | **str** | [Optional] Values include the following options (Very Low, Low, Moderate,High,Very High) | [optional] 
**vulnerabilty_summary** | **str** | [Optional] Include vulnerability summary. Character Limit &#x3D; 2,000. | [optional] 
**recommendations** | **str** | [Optional] Include recommendations. Character Limit &#x3D; 2,000. | [optional] 
**relevance_of_threat** | **str** | [Optional] Values include the following options (Very Low, Low, Moderate,High,Very High) | [optional] 
**likelihood** | **str** | [Optional] Values include the following options (Very Low, Low, Moderate,High,Very High) | [optional] 
**impact** | **str** | [Optional] Values include the following options (Very Low, Low, Moderate,High,Very High) | [optional] 
**impact_description** | **str** | [Optional] Include description of Security Control&#39;s impact. | [optional] 
**residual_risk_level** | **str** | [Optional] Values include the following options (Very Low, Low, Moderate,High,Very High) | [optional] 
**test_method** | **str** | [Optional] Identifies the assessment method / combination that will determine if the security requirements are implemented correctly. | [optional] 
**mitigations** | **str** | [Optional] Identify any mitigations in place for the Non-Compliant Security Control&#39;s vulnerabilities. Character Limit &#x3D; 2,000. | [optional] 
**application_layer** | **str** | [Optional] If the Financial Management (Navy) overlay is applied to the system, this field appears and can be populated. Character Limit &#x3D; 2,000. Navy only. | [optional] 
**database_layer** | **str** | [Optional] If the Financial Management (Navy) overlay is applied to the system, this field appears and can be populated. Navy only. | [optional] 
**operating_system_layer** | **str** | [Optional] If the Financial Management (Navy) overlay is applied to the system, this field appears and can be populated. Navy only. | [optional] 

## Example

```python
from emass_client.models.controls_optional_fields import ControlsOptionalFields

# TODO update the JSON string below
json = "{}"
# create an instance of ControlsOptionalFields from a JSON string
controls_optional_fields_instance = ControlsOptionalFields.from_json(json)
# print the JSON string representation of the object
print(ControlsOptionalFields.to_json())

# convert the object into a dict
controls_optional_fields_dict = controls_optional_fields_instance.to_dict()
# create an instance of ControlsOptionalFields from a dict
controls_optional_fields_from_dict = ControlsOptionalFields.from_dict(controls_optional_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


