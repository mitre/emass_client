# PoamConditionalFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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

## Example

```python
from emass_client.models.poam_conditional_fields import PoamConditionalFields

# TODO update the JSON string below
json = "{}"
# create an instance of PoamConditionalFields from a JSON string
poam_conditional_fields_instance = PoamConditionalFields.from_json(json)
# print the JSON string representation of the object
print(PoamConditionalFields.to_json())

# convert the object into a dict
poam_conditional_fields_dict = poam_conditional_fields_instance.to_dict()
# create an instance of PoamConditionalFields from a dict
poam_conditional_fields_from_dict = PoamConditionalFields.from_dict(poam_conditional_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


