# SwBaselineConditionalFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approval_date** | **int** | [Conditional] Approval date of the software asset. If Approval Status is set to \&quot;Unapproved\&quot; or \&quot;In Progress\&quot;, Approval Date will be set to null. | [optional] 

## Example

```python
from emass_client.models.sw_baseline_conditional_fields import SwBaselineConditionalFields

# TODO update the JSON string below
json = "{}"
# create an instance of SwBaselineConditionalFields from a JSON string
sw_baseline_conditional_fields_instance = SwBaselineConditionalFields.from_json(json)
# print the JSON string representation of the object
print(SwBaselineConditionalFields.to_json())

# convert the object into a dict
sw_baseline_conditional_fields_dict = sw_baseline_conditional_fields_instance.to_dict()
# create an instance of SwBaselineConditionalFields from a dict
sw_baseline_conditional_fields_from_dict = SwBaselineConditionalFields.from_dict(sw_baseline_conditional_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


