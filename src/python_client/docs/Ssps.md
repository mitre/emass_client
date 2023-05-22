# Ssps


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ssp_name** | **str** | [Read-Only] Name of the System Security Plan. | [optional] 
**ssp_version** | **str** | [Read-Only] Version of the System Security Plan. | [optional] 
**ssp_date** | **int** | [Read-Only] Date of the System Security Plan. Unix date format. | [optional] 

## Example

```python
from emass_client.models.ssps import Ssps

# TODO update the JSON string below
json = "{}"
# create an instance of Ssps from a JSON string
ssps_instance = Ssps.from_json(json)
# print the JSON string representation of the object
print Ssps.to_json()

# convert the object into a dict
ssps_dict = ssps_instance.to_dict()
# create an instance of Ssps from a dict
ssps_form_dict = ssps.from_dict(ssps_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


