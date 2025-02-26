# ArtifactsResponsePutPostDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filename** | **str** | [Required] File name should match exactly one file within the provided zip file. 1000 Characters. | [optional] 
**success** | **bool** |  | [optional] 
**system_id** | **int** |  | [optional] 
**errors** | **List[object]** |  | [optional] 

## Example

```python
from emass_client.models.artifacts_response_put_post_data_inner import ArtifactsResponsePutPostDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of ArtifactsResponsePutPostDataInner from a JSON string
artifacts_response_put_post_data_inner_instance = ArtifactsResponsePutPostDataInner.from_json(json)
# print the JSON string representation of the object
print(ArtifactsResponsePutPostDataInner.to_json())

# convert the object into a dict
artifacts_response_put_post_data_inner_dict = artifacts_response_put_post_data_inner_instance.to_dict()
# create an instance of ArtifactsResponsePutPostDataInner from a dict
artifacts_response_put_post_data_inner_from_dict = ArtifactsResponsePutPostDataInner.from_dict(artifacts_response_put_post_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


