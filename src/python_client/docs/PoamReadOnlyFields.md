# PoamReadOnlyFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**condition_id** | **str** | [Read-Only] Unique identifier of the authorization term/condition linked to the POA&amp;M Item. | [optional] 
**is_inherited** | **bool** | [Read-only] Indicates whether a test result is inherited. | [optional] 
**cci** | **str** | [Read-Only] CCI associated with POA&amp;M Item. | [optional] 
**review_status** | **str** | [Read-Only] Values include the following options: (Not Approved,Under Review,Approved) | [optional] 
**created_date** | **int** | [Read-Only] Timestamp representing when the POA&amp;M Item was entered into the database. | [optional] 
**extension_date** | **int** | [Read-Only] Value returned for a POA&amp;M Item with review status \&quot;Approved\&quot; and has a milestone with a scheduled completion date that extends beyond the POA&amp;M Item&#39;s scheduled completion date.  | [optional] 
**pending_extension_date** | **int** | [Read-Only] Value returned for a POA&amp;M Item with a review status of \&quot;Approved\&quot; and an unapproved milestone with a scheduled completion date that extends beyond the POA&amp;M Item&#39;s scheduled completion date.  | [optional] 
**artifacts** | **str** | [Read-Only] Lists the filenames of any artifact files attached to the POA&amp;M Item. Multiple values are separated by “; ”. | [optional] 

## Example

```python
from emass_client.models.poam_read_only_fields import PoamReadOnlyFields

# TODO update the JSON string below
json = "{}"
# create an instance of PoamReadOnlyFields from a JSON string
poam_read_only_fields_instance = PoamReadOnlyFields.from_json(json)
# print the JSON string representation of the object
print(PoamReadOnlyFields.to_json())

# convert the object into a dict
poam_read_only_fields_dict = poam_read_only_fields_instance.to_dict()
# create an instance of PoamReadOnlyFields from a dict
poam_read_only_fields_from_dict = PoamReadOnlyFields.from_dict(poam_read_only_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


