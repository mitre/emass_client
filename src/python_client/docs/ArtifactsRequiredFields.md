# ArtifactsRequiredFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filename** | **str** | [Required] File name should match exactly one file within the provided zip file. 1000 Characters. or Application/zip file. Max 30MB per artifact.  | [optional] 
**is_template** | **bool** | [Required] Indicates whether an artifact template. | [optional] 
**type** | **str** | [Required] Artifact type options | [optional] 
**category** | **str** | [Required] Artifact category options | [optional] 

## Example

```python
from emass_client.models.artifacts_required_fields import ArtifactsRequiredFields

# TODO update the JSON string below
json = "{}"
# create an instance of ArtifactsRequiredFields from a JSON string
artifacts_required_fields_instance = ArtifactsRequiredFields.from_json(json)
# print the JSON string representation of the object
print(ArtifactsRequiredFields.to_json())

# convert the object into a dict
artifacts_required_fields_dict = artifacts_required_fields_instance.to_dict()
# create an instance of ArtifactsRequiredFields from a dict
artifacts_required_fields_from_dict = ArtifactsRequiredFields.from_dict(artifacts_required_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


