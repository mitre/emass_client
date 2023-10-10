# TestResultsGet


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**system_id** | **int** | [Required] Unique eMASS identifier. Will need to provide correct number | [optional] 
**control** | **str** | [Read-Only] Control acronym associated with the test result. NIST SP 800-53 Revision 4 defined. | [optional] 
**cci** | **str** | [Required] CCI associated with test result. | [optional] 
**assessment_procedure** | **str** | [Required] The Security Control Assessment Procedure being assessed. | [optional] 
**is_inherited** | **bool** | [Read-only] Indicates whether a test result is inherited. | [optional] 
**tested_by** | **str** | [Required] Last Name, First Name. 100 Characters. | [optional] 
**test_date** | **int** | [Required] Unix time format. | [optional] 
**description** | **str** | [Required] Include description of test result. 4000 Characters. | [optional] 
**type** | **str** | [Read-Only] Indicates the location in the Control Approval Chain when the test result is submitted. | [optional] 
**compliance_status** | **str** | [Required] Test result compliance status | [optional] 

## Example

```python
from emass_client.models.test_results_get import TestResultsGet

# TODO update the JSON string below
json = "{}"
# create an instance of TestResultsGet from a JSON string
test_results_get_instance = TestResultsGet.from_json(json)
# print the JSON string representation of the object
print TestResultsGet.to_json()

# convert the object into a dict
test_results_get_dict = test_results_get_instance.to_dict()
# create an instance of TestResultsGet from a dict
test_results_get_form_dict = test_results_get.from_dict(test_results_get_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


