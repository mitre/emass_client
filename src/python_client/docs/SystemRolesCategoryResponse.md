# SystemRolesCategoryResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Response200**](Response200.md) |  | [optional] 
**data** | [**List[RoleCategory]**](RoleCategory.md) |  | [optional] 

## Example

```python
from emass_client.models.system_roles_category_response import SystemRolesCategoryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SystemRolesCategoryResponse from a JSON string
system_roles_category_response_instance = SystemRolesCategoryResponse.from_json(json)
# print the JSON string representation of the object
print SystemRolesCategoryResponse.to_json()

# convert the object into a dict
system_roles_category_response_dict = system_roles_category_response_instance.to_dict()
# create an instance of SystemRolesCategoryResponse from a dict
system_roles_category_response_form_dict = system_roles_category_response.from_dict(system_roles_category_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


