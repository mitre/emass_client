# ArtifactsReadOnlyFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_inherited** | **bool** | [Read-only] Indicates whether an artifact is inherited. | [optional] 
**ccis** | **str** | [Read-Only] CCI mapping for Assessment Procedures associated with the artifact. | [optional] 
**mime_content_type** | **str** | [Read-Only] Standard MIME content type derived from file extension. | [optional] 
**file_size** | **str** | [Read-Only] File size of attached artifact. | [optional] 

## Example

```python
from emass_client.models.artifacts_read_only_fields import ArtifactsReadOnlyFields

# TODO update the JSON string below
json = "{}"
# create an instance of ArtifactsReadOnlyFields from a JSON string
artifacts_read_only_fields_instance = ArtifactsReadOnlyFields.from_json(json)
# print the JSON string representation of the object
print(ArtifactsReadOnlyFields.to_json())

# convert the object into a dict
artifacts_read_only_fields_dict = artifacts_read_only_fields_instance.to_dict()
# create an instance of ArtifactsReadOnlyFields from a dict
artifacts_read_only_fields_from_dict = ArtifactsReadOnlyFields.from_dict(artifacts_read_only_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


