# ArtifactsResponseDelDataInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filename** | **str** | [Required] File name should match exactly one file within the provided zip file. 1000 Characters. | [optional] 
**success** | **bool** |  | [optional] 
**system_id** | **int** |  | [optional] 

## Example

```python
from emass_client.models.artifacts_response_del_data_inner import ArtifactsResponseDelDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of ArtifactsResponseDelDataInner from a JSON string
artifacts_response_del_data_inner_instance = ArtifactsResponseDelDataInner.from_json(json)
# print the JSON string representation of the object
print ArtifactsResponseDelDataInner.to_json()

# convert the object into a dict
artifacts_response_del_data_inner_dict = artifacts_response_del_data_inner_instance.to_dict()
# create an instance of ArtifactsResponseDelDataInner from a dict
artifacts_response_del_data_inner_form_dict = artifacts_response_del_data_inner.from_dict(artifacts_response_del_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


