# APIRuleFailed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**APIRuleFailedMeta**](APIRuleFailedMeta.md) |  | [optional] 

## Example

```python
from emass_client.models.api_rule_failed import APIRuleFailed

# TODO update the JSON string below
json = "{}"
# create an instance of APIRuleFailed from a JSON string
api_rule_failed_instance = APIRuleFailed.from_json(json)
# print the JSON string representation of the object
print(APIRuleFailed.to_json())

# convert the object into a dict
api_rule_failed_dict = api_rule_failed_instance.to_dict()
# create an instance of APIRuleFailed from a dict
api_rule_failed_from_dict = APIRuleFailed.from_dict(api_rule_failed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


