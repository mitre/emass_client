# APIRuleFailedMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [default to 490]
**error_message** | **str** |  | [optional] [default to 'Request has failed because too much data was requested in a single batch. This error is specific to eMASS']

## Example

```python
from emass_client.models.api_rule_failed_meta import APIRuleFailedMeta

# TODO update the JSON string below
json = "{}"
# create an instance of APIRuleFailedMeta from a JSON string
api_rule_failed_meta_instance = APIRuleFailedMeta.from_json(json)
# print the JSON string representation of the object
print(APIRuleFailedMeta.to_json())

# convert the object into a dict
api_rule_failed_meta_dict = api_rule_failed_meta_instance.to_dict()
# create an instance of APIRuleFailedMeta from a dict
api_rule_failed_meta_from_dict = APIRuleFailedMeta.from_dict(api_rule_failed_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


