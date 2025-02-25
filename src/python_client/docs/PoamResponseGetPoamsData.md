# PoamResponseGetPoamsData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**system_id** | **int** | [Required] Unique eMASS system identifier. | [optional] 
**poam_id** | **int** | [Required] Unique item identifier | [optional] 
**display_poam_id** | **int** | [Required] Globally unique identifier for individual POA&amp;M Items, seen on the front-end as ID. | [optional] 
**status** | **str** | [Required] The POA&amp;M status | [optional] 
**vulnerability_description** | **str** | [Required] Provide a description of the POA&amp;M Item. 2000 Characters. | [optional] 
**source_identifying_vulnerability** | **str** | [Required] Include Source Identifying Vulnerability text. 2000 Characters. | [optional] 
**poc_organization** | **str** | [Required] Organization/Office represented. 100 Characters. | [optional] 
**resources** | **str** | [Required] List of resources used. 250 Characters. | [optional] 
**identified_in_cfo_audit_or_other_review** | **bool** | [Required] If not specified, this field will be set to false because it does not accept a null value. VA only | [optional] 
**condition_id** | **str** | [Read-Only] Unique identifier of the authorization term/condition linked to the POA&amp;M Item. | [optional] 
**is_inherited** | **bool** | [Read-only] Indicates whether a test result is inherited. | [optional] 
**cci** | **str** | [Read-Only] CCI associated with POA&amp;M Item. | [optional] 
**review_status** | **str** | [Read-Only] Values include the following options: (Not Approved,Under Review,Approved) | [optional] 
**created_date** | **int** | [Read-Only] Timestamp representing when the POA&amp;M Item was entered into the database. | [optional] 
**extension_date** | **int** | [Read-Only] Value returned for a POA&amp;M Item with review status \&quot;Approved\&quot; and has a milestone with a scheduled completion date that extends beyond the POA&amp;M Item&#39;s scheduled completion date.  | [optional] 
**pending_extension_date** | **int** | [Read-Only] Value returned for a POA&amp;M Item with a review status of \&quot;Approved\&quot; and an unapproved milestone with a scheduled completion date that extends beyond the POA&amp;M Item&#39;s scheduled completion date.  | [optional] 
**artifacts** | **str** | [Read-Only] Lists the filenames of any artifact files attached to the POA&amp;M Item. Multiple values are separated by “; ”. | [optional] 
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
**poc_first_name** | **str** | [Conditional] First name of POC. 100 Characters. | [optional] 
**poc_last_name** | **str** | [Conditional] Last name of POC. 100 Characters. | [optional] 
**poc_email** | **str** | [Conditional] Email address of POC. 100 Characters. | [optional] 
**poc_phone_number** | **str** | [Conditional] Phone number of POC (area code) ***-**** format. 100 Characters. | [optional] 
**severity** | **str** | [Conditional] Required for approved items. Values include the following options: (Very Low, Low, Moderate,High,Very High) | [optional] 
**scheduled_completion_date** | **int** | [Conditional] Required for ongoing and completed POA&amp;M items. Unix time format. | [optional] 
**completion_date** | **int** | [Conditional] Field is required for completed POA&amp;M items. Unix time format. | [optional] 
**comments** | **str** | [Conditional] Field is required for completed and risk accepted POA&amp;M items. 2000 Characters | [optional] 
**personnel_resources_funded_base_hours** | **float** | [Conditional] At least one of the following is required and must be completed for each POA&amp;M Item:   Personnel Resources-&gt; Funded Base Hours   Personnel Resources-&gt; Unfunded Base Hours   Non-Personnel Resources-&gt; Funded Amount   Non-Personnel Resources-&gt; Unfunded Amount Displays numbers to the second decimal point (e.g., 100.00). VA only.  | [optional] 
**personnel_resources_cost_code** | **str** | [Conditional] Required if Personnel Resources: Funded Base Hours is populated. Only accepts values present in the field&#39;s lookup table (modifiable by eMASS System Admins). VA only.  | [optional] 
**personnel_resources_unfunded_base_hours** | **float** | [Conditional] At least one of the following is required and must be completed for each POA&amp;M Item:   Personnel Resources-&gt; Funded Base Hours   Personnel Resources-&gt; Unfunded Base Hours   Non-Personnel Resources-&gt; Funded Amount   Non-Personnel Resources-&gt; Unfunded Amount Displays numbers to the second decimal point (e.g., 100.00). VA only.  | [optional] 
**personnel_resources_nonfunding_obstacle** | **str** | [Conditional] Required if Personnel Resources: Unfunded Base Hours is populated. Only accepts values present in the field&#39;s lookup table (modifiable by eMASS System Admins). VA only.  | [optional] 
**personnel_resources_nonfunding_obstacle_other_reason** | **str** | [Conditional] Required if the value \&quot;Other\&quot; is populated for the field Personnel Resources: Non-Funding Obstacle. VA only. | [optional] 
**non_personnel_resources_funded_amount** | **float** | [Conditional] At least one of the following is required and must be completed for each POA&amp;M Item:   Personnel Resources-&gt; Funded Base Hours   Personnel Resources-&gt; Unfunded Base Hours   Non-Personnel Resources-&gt; Funded Amount   Non-Personnel Resources-&gt; Unfunded Amount Displays numbers to the second decimal point (e.g., 100.00). VA only.  | [optional] 
**non_personnel_resources_cost_code** | **str** | [Conditional] Required if Non-Personnel Resources: Funded Amount is populated. Only accepts values present in the field&#39;s lookup table (modifiable by eMASS System Admins). VA only.  | [optional] 
**non_personnel_resources_unfunded_amount** | **float** | [Conditional] At least one of the following is required and must be completed for each POA&amp;M Item:   Personnel Resources-&gt; Funded Base Hours   Personnel Resources-&gt; Unfunded Base Hours   Non-Personnel Resources-&gt; Funded Amount   Non-Personnel Resources-&gt; Unfunded Amount Displays numbers to the second decimal point (e.g., 100.00). VA only.  | [optional] 
**non_personnel_resources_nonfunding_obstacle** | **str** | [Conditional] Required if Non-Personnel Resources: Unfunded Amount is populated. Only accepts values present in the field&#39;s lookup table (modifiable by eMASS System Admins). VA only.  | [optional] 
**non_personnel_resources_nonfunding_obstacle_other_reason** | **str** | [Conditional] Required if the value \&quot;Other\&quot; is populated for the field Non-Personnel Resources: Non-Funding Obstacle. VA only. | [optional] 
**milestones** | [**List[MilestonesGet]**](MilestonesGet.md) |  | [optional] 

## Example

```python
from emass_client.models.poam_response_get_poams_data import PoamResponseGetPoamsData

# TODO update the JSON string below
json = "{}"
# create an instance of PoamResponseGetPoamsData from a JSON string
poam_response_get_poams_data_instance = PoamResponseGetPoamsData.from_json(json)
# print the JSON string representation of the object
print(PoamResponseGetPoamsData.to_json())

# convert the object into a dict
poam_response_get_poams_data_dict = poam_response_get_poams_data_instance.to_dict()
# create an instance of PoamResponseGetPoamsData from a dict
poam_response_get_poams_data_from_dict = PoamResponseGetPoamsData.from_dict(poam_response_get_poams_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


