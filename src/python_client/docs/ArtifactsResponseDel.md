# ArtifactsResponseDel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Response200**](Response200.md) |  | [optional] 
**data** | [**List[ArtifactsResponseDelDataInner]**](ArtifactsResponseDelDataInner.md) |  | [optional] 

## Example

```python
from emass_client.models.artifacts_response_del import ArtifactsResponseDel

# TODO update the JSON string below
json = "{}"
# create an instance of ArtifactsResponseDel from a JSON string
artifacts_response_del_instance = ArtifactsResponseDel.from_json(json)
# print the JSON string representation of the object
print ArtifactsResponseDel.to_json()

# convert the object into a dict
artifacts_response_del_dict = artifacts_response_del_instance.to_dict()
# create an instance of ArtifactsResponseDel from a dict
artifacts_response_del_form_dict = artifacts_response_del.from_dict(artifacts_response_del_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


