# ArtifactsGet


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**system_id** | **int** | [Required] Unique eMASS system identifier. | [optional] 
**filename** | **str** | [Required] File name should match exactly one file within the provided zip file. 1000 Characters. | [optional] 
**is_inherited** | **bool** | [Read-only] Indicates whether an artifact is inherited. | [optional] 
**is_template** | **bool** | [Required] Indicates whether an artifact template. | [optional] 
**type** | **str** | [Required] Artifact type options | [optional] 
**category** | **str** | [Required] Artifact category options | [optional] 
**name** | **str** | [Optional] Artifact name. Character Limit &#x3D; 100. | [optional] 
**description** | **str** | [Optional] Artifact description. 10,000 Characters. | [optional] 
**reference_page_number** | **str** | [Optional] Artifact reference page number. 50 Characters. | [optional] 
**ccis** | **str** | [Optional] CCI associated with test result. | [optional] 
**controls** | **str** | [Optional] Control acronym associated with the artifact. NIST SP 800-53 Revision 4 defined. | [optional] 
**mime_content_type** | **str** | [Read-Only] Standard MIME content type derived from file extension. | [optional] 
**file_size** | **str** | [Read-Only] File size of attached artifact. | [optional] 
**expiration_date** | **int** | [Optional] Date Artifact expires and requires review. In Unix Date format. | [optional] 
**last_reviewed_date** | **int** | [Optional] Date Artifact was last reviewed. Unix time format. | [optional] 
**signed_date** | **int** | [Optional] Date artifact was signed. Unix time format. | [optional] 

## Example

```python
from emass_client.models.artifacts_get import ArtifactsGet

# TODO update the JSON string below
json = "{}"
# create an instance of ArtifactsGet from a JSON string
artifacts_get_instance = ArtifactsGet.from_json(json)
# print the JSON string representation of the object
print ArtifactsGet.to_json()

# convert the object into a dict
artifacts_get_dict = artifacts_get_instance.to_dict()
# create an instance of ArtifactsGet from a dict
artifacts_get_form_dict = artifacts_get.from_dict(artifacts_get_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


