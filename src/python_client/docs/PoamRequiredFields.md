# PoamRequiredFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | [Required] The POA&amp;M status | [optional] 
**vulnerability_description** | **str** | [Required] Provide a description of the POA&amp;M Item. 2000 Characters. | [optional] 
**source_identifying_vulnerability** | **str** | [Required] Include Source Identifying Vulnerability text. 2000 Characters. | [optional] 
**poc_organization** | **str** | [Required] Organization/Office represented. 100 Characters. | [optional] 
**resources** | **str** | [Required] List of resources used. 250 Characters. | [optional] 
**identified_in_cfo_audit_or_other_review** | **bool** | [Required] If not specified, this field will be set to false because it does not accept a null value. VA only | [optional] 

## Example

```python
from emass_client.models.poam_required_fields import PoamRequiredFields

# TODO update the JSON string below
json = "{}"
# create an instance of PoamRequiredFields from a JSON string
poam_required_fields_instance = PoamRequiredFields.from_json(json)
# print the JSON string representation of the object
print(PoamRequiredFields.to_json())

# convert the object into a dict
poam_required_fields_dict = poam_required_fields_instance.to_dict()
# create an instance of PoamRequiredFields from a dict
poam_required_fields_from_dict = PoamRequiredFields.from_dict(poam_required_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


