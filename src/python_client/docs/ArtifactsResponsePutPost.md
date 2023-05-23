# ArtifactsResponsePutPost


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Response200**](Response200.md) |  | [optional] 
**data** | [**List[ArtifactsResponsePutPostDataInner]**](ArtifactsResponsePutPostDataInner.md) |  | [optional] 

## Example

```python
from emass_client.models.artifacts_response_put_post import ArtifactsResponsePutPost

# TODO update the JSON string below
json = "{}"
# create an instance of ArtifactsResponsePutPost from a JSON string
artifacts_response_put_post_instance = ArtifactsResponsePutPost.from_json(json)
# print the JSON string representation of the object
print ArtifactsResponsePutPost.to_json()

# convert the object into a dict
artifacts_response_put_post_dict = artifacts_response_put_post_instance.to_dict()
# create an instance of ArtifactsResponsePutPost from a dict
artifacts_response_put_post_form_dict = artifacts_response_put_post.from_dict(artifacts_response_put_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


