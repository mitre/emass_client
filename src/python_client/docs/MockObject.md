# MockObject


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**poc_organization** | **str** | [Required] Organization/Office represented. 100 Characters. | [optional] 
**resources** | **str** | [Required] List of resources used. 250 Characters. | [optional] 
**owning_organization** | **str** | [Read-Only] Owning organization of the system record. Values match the eMASS instance Organizational Hierarchy. | [optional] 
**secondary_organization** | **str** | [Read-only] Secondary organization that owns the system record (i.e. Sub-Organization-level. | [optional] 
**poc_first_name** | **str** | [Conditional] First name of POC. 100 Characters. | [optional] 
**poc_last_name** | **str** | [Conditional] Last name of POC. 100 Characters. | [optional] 
**poc_email** | **str** | [Conditional] Email address of POC. 100 Characters. | [optional] 
**poc_phone_number** | **str** | [Conditional] Phone number of POC (area code) ***-**** format. 100 Characters. | [optional] 
**severity** | **str** | [Conditional] Required for approved items. Values include the following options: (Very Low, Low, Moderate,High,Very High) | [optional] 
**scheduled_completion_date** | **int** | [Conditional] Required for ongoing and completed POA&amp;M items. Unix time format. | [optional] 
**completion_date** | **int** | [Conditional] Field is required for completed POA&amp;M items. Unix time format. | [optional] 
**comments** | **str** | [Conditional] Field is required for completed and risk accepted POA&amp;M items. 2000 Characters | [optional] 
**is_active** | **bool** | [Conditional] Optionally used in PUT to delete milestones when updating a POA&amp;M. | [optional] 

## Example

```python
from emass_client.models.mock_object import MockObject

# TODO update the JSON string below
json = "{}"
# create an instance of MockObject from a JSON string
mock_object_instance = MockObject.from_json(json)
# print the JSON string representation of the object
print MockObject.to_json()

# convert the object into a dict
mock_object_dict = mock_object_instance.to_dict()
# create an instance of MockObject from a dict
mock_object_form_dict = mock_object.from_dict(mock_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


