# ArtifactsResponseGet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Response200**](Response200.md) |  | [optional] 
**data** | [**List[ArtifactsResponseGetDataInner]**](ArtifactsResponseGetDataInner.md) |  | [optional] 

## Example

```python
from emass_client.models.artifacts_response_get import ArtifactsResponseGet

# TODO update the JSON string below
json = "{}"
# create an instance of ArtifactsResponseGet from a JSON string
artifacts_response_get_instance = ArtifactsResponseGet.from_json(json)
# print the JSON string representation of the object
print(ArtifactsResponseGet.to_json())

# convert the object into a dict
artifacts_response_get_dict = artifacts_response_get_instance.to_dict()
# create an instance of ArtifactsResponseGet from a dict
artifacts_response_get_from_dict = ArtifactsResponseGet.from_dict(artifacts_response_get_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


