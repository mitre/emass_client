# RegisterUserRequestPostBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_uid** | **str** |  | 

## Example

```python
from emass_client.models.register_user_request_post_body import RegisterUserRequestPostBody

# TODO update the JSON string below
json = "{}"
# create an instance of RegisterUserRequestPostBody from a JSON string
register_user_request_post_body_instance = RegisterUserRequestPostBody.from_json(json)
# print the JSON string representation of the object
print(RegisterUserRequestPostBody.to_json())

# convert the object into a dict
register_user_request_post_body_dict = register_user_request_post_body_instance.to_dict()
# create an instance of RegisterUserRequestPostBody from a dict
register_user_request_post_body_from_dict = RegisterUserRequestPostBody.from_dict(register_user_request_post_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


