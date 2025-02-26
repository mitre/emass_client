# StaticCodePost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_name** | **str** | [Required] Name of the software application that was assessed. | [optional] 
**version** | **str** | [Required] The version of the application. | [optional] 
**success** | **bool** |  | [optional] 
**system_id** | **int** |  | [optional] 
**errors** | **List[object]** |  | [optional] 

## Example

```python
from emass_client.models.static_code_post import StaticCodePost

# TODO update the JSON string below
json = "{}"
# create an instance of StaticCodePost from a JSON string
static_code_post_instance = StaticCodePost.from_json(json)
# print the JSON string representation of the object
print(StaticCodePost.to_json())

# convert the object into a dict
static_code_post_dict = static_code_post_instance.to_dict()
# create an instance of StaticCodePost from a dict
static_code_post_from_dict = StaticCodePost.from_dict(static_code_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


