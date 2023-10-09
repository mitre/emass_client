# ControlsGet


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**system_id** | **int** | [Required] Unique system record identifier. | [optional] 
**name** | **str** | [Read-only] Name of the system record. | [optional] 
**acronym** | **str** | [Required] Acronym of the system record. | [optional] 
**ccis** | **str** | [Read-only] Comma separated list of CCIs associated with the control. | [optional] 
**is_inherited** | **bool** | [Read-only] Indicates whether a control is inherited. | [optional] 
**modified_by_overlays** | **str** | [Read-only] List of overlays that affect the control. | [optional] 
**included_status** | **str** | [Read-only] Indicates the manner by which a control was included in the system&#39;s categorization. | [optional] 
**compliance_status** | **str** | [Read-only] Compliance of the control. | [optional] 
**responsible_entities** | **str** | [Required] Include written description of Responsible Entities that are responsible for the Security Control. Character Limit &#x3D; 2,000. | [optional] 
**implementation_status** | **str** | [Optional] Implementation Status of the Security Control for the information system. | [optional] 
**common_control_provider** | **str** | [Conditional] Indicate the type of Common Control Provider for an “Inherited” Security Control. | [optional] 
**na_justification** | **str** | [Conditional] Provide justification for Security Controls deemed Not Applicable to the system. | [optional] 
**control_designation** | **str** | [Required] Control designations | [optional] 
**estimated_completion_date** | **int** | [Required] Field is required for Implementation Plan. | [optional] 
**implementation_narrative** | **str** | [Required] Includes security control comments. Character Limit &#x3D; 2,000. | [optional] 
**slcm_criticality** | **str** | [Conditional] Criticality of Security Control regarding SLCM. Character Limit &#x3D; 2,000. | [optional] 
**slcm_frequency** | **str** | [Conditional] SLCM frequency | [optional] 
**slcm_method** | **str** | [Conditional] SLCM method utilized | [optional] 
**slcm_reporting** | **str** | [Conditional] Method for reporting Security Control for SLCM. Character Limit &#x3D; 2,000. | [optional] 
**slcm_tracking** | **str** | [Conditional] How Non-Compliant Security Controls will be tracked for SLCM. Character Limit &#x3D; 2,000. | [optional] 
**slcm_comments** | **str** | [Conditional] Additional comments for Security Control regarding SLCM. Character Limit &#x3D; 4,000. | [optional] 
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
**database_layer** | **str** | [Read-Only] Identify the primary computing environment for where the information system is deployed. Navy only. | [optional] 
**operating_system_layer** | **str** | [Read-Only] Identify the primary computing environment for where the information system is deployed. Navy only. | [optional] 

## Example

```python
from emass_client.models.controls_get import ControlsGet

# TODO update the JSON string below
json = "{}"
# create an instance of ControlsGet from a JSON string
controls_get_instance = ControlsGet.from_json(json)
# print the JSON string representation of the object
print ControlsGet.to_json()

# convert the object into a dict
controls_get_dict = controls_get_instance.to_dict()
# create an instance of ControlsGet from a dict
controls_get_form_dict = controls_get.from_dict(controls_get_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


