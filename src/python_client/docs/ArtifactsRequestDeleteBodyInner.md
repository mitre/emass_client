# ArtifactsRequestDeleteBodyInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filename** | **str** | [Required] File name should match exactly one file within the provided zip file. 1000 Characters. | [optional] 

## Example

```python
from emass_client.models.artifacts_request_delete_body_inner import ArtifactsRequestDeleteBodyInner

# TODO update the JSON string below
json = "{}"
# create an instance of ArtifactsRequestDeleteBodyInner from a JSON string
artifacts_request_delete_body_inner_instance = ArtifactsRequestDeleteBodyInner.from_json(json)
# print the JSON string representation of the object
print(ArtifactsRequestDeleteBodyInner.to_json())

# convert the object into a dict
artifacts_request_delete_body_inner_dict = artifacts_request_delete_body_inner_instance.to_dict()
# create an instance of ArtifactsRequestDeleteBodyInner from a dict
artifacts_request_delete_body_inner_from_dict = ArtifactsRequestDeleteBodyInner.from_dict(artifacts_request_delete_body_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


