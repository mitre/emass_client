# MilestonesFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**milestones** | [**List[MilestonesGet]**](MilestonesGet.md) |  | [optional] 

## Example

```python
from emass_client.models.milestones_fields import MilestonesFields

# TODO update the JSON string below
json = "{}"
# create an instance of MilestonesFields from a JSON string
milestones_fields_instance = MilestonesFields.from_json(json)
# print the JSON string representation of the object
print(MilestonesFields.to_json())

# convert the object into a dict
milestones_fields_dict = milestones_fields_instance.to_dict()
# create an instance of MilestonesFields from a dict
milestones_fields_from_dict = MilestonesFields.from_dict(milestones_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


