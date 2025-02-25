# ControlsReadOnlyFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | [Read-only] Name of the system record. | [optional] 
**ccis** | **str** | [Read-only] Comma separated list of CCIs associated with the control. | [optional] 
**is_inherited** | **bool** | [Read-only] Indicates whether a control is inherited. | [optional] 
**modified_by_overlays** | **str** | [Read-only] List of overlays that affect the control. | [optional] 
**included_status** | **str** | [Read-only] Indicates the manner by which a control was included in the system&#39;s categorization. | [optional] 
**compliance_status** | **str** | [Read-only] Compliance of the control. | [optional] 

## Example

```python
from emass_client.models.controls_read_only_fields import ControlsReadOnlyFields

# TODO update the JSON string below
json = "{}"
# create an instance of ControlsReadOnlyFields from a JSON string
controls_read_only_fields_instance = ControlsReadOnlyFields.from_json(json)
# print the JSON string representation of the object
print(ControlsReadOnlyFields.to_json())

# convert the object into a dict
controls_read_only_fields_dict = controls_read_only_fields_instance.to_dict()
# create an instance of ControlsReadOnlyFields from a dict
controls_read_only_fields_from_dict = ControlsReadOnlyFields.from_dict(controls_read_only_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


