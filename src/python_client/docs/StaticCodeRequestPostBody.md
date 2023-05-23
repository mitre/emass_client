# StaticCodeRequestPostBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application** | [**StaticCodeRequestPostBodyApplication**](StaticCodeRequestPostBodyApplication.md) |  | [optional] 
**application_findings** | [**List[StaticCodeApplication]**](StaticCodeApplication.md) |  | [optional] 

## Example

```python
from emass_client.models.static_code_request_post_body import StaticCodeRequestPostBody

# TODO update the JSON string below
json = "{}"
# create an instance of StaticCodeRequestPostBody from a JSON string
static_code_request_post_body_instance = StaticCodeRequestPostBody.from_json(json)
# print the JSON string representation of the object
print StaticCodeRequestPostBody.to_json()

# convert the object into a dict
static_code_request_post_body_dict = static_code_request_post_body_instance.to_dict()
# create an instance of StaticCodeRequestPostBody from a dict
static_code_request_post_body_form_dict = static_code_request_post_body.from_dict(static_code_request_post_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


