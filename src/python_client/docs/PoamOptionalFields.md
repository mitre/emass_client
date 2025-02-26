# PoamOptionalFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_uid** | **str** | [Optional] Unique identifier external to the eMASS application for use with associating POA&amp;Ms. 100 Characters. | [optional] 
**control_acronym** | **str** | [Optional] Control acronym associated with the POA&amp;M Item. NIST SP 800-53 Revision 4 defined. | [optional] 
**assessment_procedure** | **str** | [Optional] The Security Control Assessment Procedure being associated with the POA&amp;M Item. | [optional] 
**security_checks** | **str** | [Optional] Security Checks that are associated with the POA&amp;M. | [optional] 
**raw_severity** | **str** | [Optional] Scan vulnerability ratting Values include the following options: (Very Low, Low, Moderate,High,Very High) | [optional] 
**relevance_of_threat** | **str** | [Optional] Values include the following options (Very Low, Low, Moderate,High,Very High) | [optional] 
**likelihood** | **str** | [Optional] Values include the following options (Very Low, Low, Moderate,High,Very High) | [optional] 
**impact** | **str** | [Optional] Values include the following options (Very Low, Low, Moderate,High,Very High) | [optional] 
**impact_description** | **str** | [Optional] Include description of Security Control&#39;s impact. | [optional] 
**residual_risk_level** | **str** | [Optional] Values include the following options (Very Low, Low, Moderate,High,Very High) | [optional] 
**recommendations** | **str** | [Optional] Include recommendations. Character Limit &#x3D; 2,000. | [optional] 
**mitigations** | **str** | [Optional] Include mitigation explanation. 2000 Characters. | [optional] 
**resulting_residual_risk_level_after_proposed_mitigations** | **str** | [Optional] Indicate the risk level expected after any proposed mitigations are implemented. Proposed mitigations should be appropriately documented as POA&amp;M milestones. Navy only. | [optional] 
**predisposing_conditions** | **str** | [Optional] A predisposing condition is a condition existing within an organization, a mission or business process, enterprise architecture, information system/PIT, or environment of operation, which affects (i.e., increases or decreases) the likelihood that threat events, once initiated, result in adverse impacts. Navy only. | [optional] 
**threat_description** | **str** | [Optional] Describe the identified threat(s) and relevance to the information system. Navy only. | [optional] 
**devices_affected** | **str** | [Optional] List any affected devices by hostname. If all devices in the information system are affected, state &#39;system&#39; or &#39;all&#39;. Navy only | [optional] 

## Example

```python
from emass_client.models.poam_optional_fields import PoamOptionalFields

# TODO update the JSON string below
json = "{}"
# create an instance of PoamOptionalFields from a JSON string
poam_optional_fields_instance = PoamOptionalFields.from_json(json)
# print the JSON string representation of the object
print(PoamOptionalFields.to_json())

# convert the object into a dict
poam_optional_fields_dict = poam_optional_fields_instance.to_dict()
# create an instance of PoamOptionalFields from a dict
poam_optional_fields_from_dict = PoamOptionalFields.from_dict(poam_optional_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


