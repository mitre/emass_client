# RoleCategory


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**system_id** | **int** | [Read-only] Unique system record identifier. | [optional] 
**system_name** | **str** | [Read-only] Name of the system record. | [optional] 
**system_acronym** | **str** | [Read-only] Acronym of the system record. | [optional] 
**roles** | [**List[Roles]**](Roles.md) |  | [optional] 

## Example

```python
from emass_client.models.role_category import RoleCategory

# TODO update the JSON string below
json = "{}"
# create an instance of RoleCategory from a JSON string
role_category_instance = RoleCategory.from_json(json)
# print the JSON string representation of the object
print RoleCategory.to_json()

# convert the object into a dict
role_category_dict = role_category_instance.to_dict()
# create an instance of RoleCategory from a dict
role_category_form_dict = role_category.from_dict(role_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


