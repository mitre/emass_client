# StaticCodeRequestPostBodyApplication


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_name** | **str** | [Required] Name of the software application that was assessed. | [optional] 
**version** | **str** | [Required] The version of the application. | [optional] 

## Example

```python
from emass_client.models.static_code_request_post_body_application import StaticCodeRequestPostBodyApplication

# TODO update the JSON string below
json = "{}"
# create an instance of StaticCodeRequestPostBodyApplication from a JSON string
static_code_request_post_body_application_instance = StaticCodeRequestPostBodyApplication.from_json(json)
# print the JSON string representation of the object
print StaticCodeRequestPostBodyApplication.to_json()

# convert the object into a dict
static_code_request_post_body_application_dict = static_code_request_post_body_application_instance.to_dict()
# create an instance of StaticCodeRequestPostBodyApplication from a dict
static_code_request_post_body_application_form_dict = static_code_request_post_body_application.from_dict(static_code_request_post_body_application_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


