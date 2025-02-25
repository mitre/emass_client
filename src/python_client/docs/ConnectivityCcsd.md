# ConnectivityCcsd


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ccsd_number** | **str** | [Read-Only] Identifier for specific connections to the system. | [optional] 
**connectivity** | **str** | [Read-Only] Choose connection type for the system. | [optional] 

## Example

```python
from emass_client.models.connectivity_ccsd import ConnectivityCcsd

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectivityCcsd from a JSON string
connectivity_ccsd_instance = ConnectivityCcsd.from_json(json)
# print the JSON string representation of the object
print(ConnectivityCcsd.to_json())

# convert the object into a dict
connectivity_ccsd_dict = connectivity_ccsd_instance.to_dict()
# create an instance of ConnectivityCcsd from a dict
connectivity_ccsd_from_dict = ConnectivityCcsd.from_dict(connectivity_ccsd_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


