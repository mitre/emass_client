# ArtifactsResponseGetDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**system_id** | **int** | [Required] Unique eMASS system identifier. | [optional] 
**filename** | **str** | [Required] File name should match exactly one file within the provided zip file. 1000 Characters. or Application/zip file. Max 30MB per artifact.  | [optional] 
**is_template** | **bool** | [Required] Indicates whether an artifact template. | [optional] 
**type** | **str** | [Required] Artifact type options | [optional] 
**category** | **str** | [Required] Artifact category options | [optional] 
**is_inherited** | **bool** | [Read-only] Indicates whether an artifact is inherited. | [optional] 
**ccis** | **str** | [Read-Only] CCI mapping for Assessment Procedures associated with the artifact. | [optional] 
**mime_content_type** | **str** | [Read-Only] Standard MIME content type derived from file extension. | [optional] 
**file_size** | **str** | [Read-Only] File size of attached artifact. | [optional] 
**name** | **str** | [Optional] Artifact name. Character Limit &#x3D; 100. | [optional] 
**description** | **str** | [Optional] Artifact description. 10,000 Characters. | [optional] 
**reference_page_number** | **str** | [Optional] Artifact reference page number. 50 Characters. | [optional] 
**assessment_procedures** | **str** | [Optional] The Security Control Assessment Procedure being associated with the artifact. | [optional] 
**controls** | **str** | [Optional] Control acronym associated with the artifact. NIST SP 800-53 Revision 4 defined. | [optional] 
**expiration_date** | **int** | [Optional] Date Artifact expires and requires review. In Unix Date format. | [optional] 
**last_reviewed_date** | **int** | [Optional] Date Artifact was last reviewed. Unix time format. | [optional] 
**signed_date** | **int** | [Optional] Date artifact was signed. Unix time format. | [optional] 

## Example

```python
from emass_client.models.artifacts_response_get_data_inner import ArtifactsResponseGetDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of ArtifactsResponseGetDataInner from a JSON string
artifacts_response_get_data_inner_instance = ArtifactsResponseGetDataInner.from_json(json)
# print the JSON string representation of the object
print(ArtifactsResponseGetDataInner.to_json())

# convert the object into a dict
artifacts_response_get_data_inner_dict = artifacts_response_get_data_inner_instance.to_dict()
# create an instance of ArtifactsResponseGetDataInner from a dict
artifacts_response_get_data_inner_from_dict = ArtifactsResponseGetDataInner.from_dict(artifacts_response_get_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


