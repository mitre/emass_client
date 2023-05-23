# CmmcResponseGet


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Response200**](Response200.md) |  | [optional] 
**data** | [**List[CmmcGet]**](CmmcGet.md) |  | [optional] 

## Example

```python
from emass_client.models.cmmc_response_get import CmmcResponseGet

# TODO update the JSON string below
json = "{}"
# create an instance of CmmcResponseGet from a JSON string
cmmc_response_get_instance = CmmcResponseGet.from_json(json)
# print the JSON string representation of the object
print CmmcResponseGet.to_json()

# convert the object into a dict
cmmc_response_get_dict = cmmc_response_get_instance.to_dict()
# create an instance of CmmcResponseGet from a dict
cmmc_response_get_form_dict = cmmc_response_get.from_dict(cmmc_response_get_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


