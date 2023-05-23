# PacPost


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow** | **str** | [Required] Values include the following:(Assess and Authorize, Assess Only, Security Plan Approval) | [optional] 
**success** | **bool** |  | [optional] 
**system_id** | **int** |  | [optional] 
**errors** | **List[object]** |  | [optional] 

## Example

```python
from emass_client.models.pac_post import PacPost

# TODO update the JSON string below
json = "{}"
# create an instance of PacPost from a JSON string
pac_post_instance = PacPost.from_json(json)
# print the JSON string representation of the object
print PacPost.to_json()

# convert the object into a dict
pac_post_dict = pac_post_instance.to_dict()
# create an instance of PacPost from a dict
pac_post_form_dict = pac_post.from_dict(pac_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


