# Roles


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_category** | **str** | [Required] System role categories | [optional] 
**role** | **str** | [Required] System role description | [optional] 
**users** | [**List[Users]**](Users.md) |  | [optional] 

## Example

```python
from emass_client.models.roles import Roles

# TODO update the JSON string below
json = "{}"
# create an instance of Roles from a JSON string
roles_instance = Roles.from_json(json)
# print the JSON string representation of the object
print Roles.to_json()

# convert the object into a dict
roles_dict = roles_instance.to_dict()
# create an instance of Roles from a dict
roles_form_dict = roles.from_dict(roles_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


