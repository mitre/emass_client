# SystemRolesResponseDataInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_category** | **str** |  | [optional] [default to 'PAC']
**role** | **str** |  | [optional] [default to 'PM/IAM']

## Example

```python
from emass_client.models.system_roles_response_data_inner import SystemRolesResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of SystemRolesResponseDataInner from a JSON string
system_roles_response_data_inner_instance = SystemRolesResponseDataInner.from_json(json)
# print the JSON string representation of the object
print SystemRolesResponseDataInner.to_json()

# convert the object into a dict
system_roles_response_data_inner_dict = system_roles_response_data_inner_instance.to_dict()
# create an instance of SystemRolesResponseDataInner from a dict
system_roles_response_data_inner_form_dict = system_roles_response_data_inner.from_dict(system_roles_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


