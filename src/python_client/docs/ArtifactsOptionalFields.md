# ArtifactsOptionalFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
from emass_client.models.artifacts_optional_fields import ArtifactsOptionalFields

# TODO update the JSON string below
json = "{}"
# create an instance of ArtifactsOptionalFields from a JSON string
artifacts_optional_fields_instance = ArtifactsOptionalFields.from_json(json)
# print the JSON string representation of the object
print(ArtifactsOptionalFields.to_json())

# convert the object into a dict
artifacts_optional_fields_dict = artifacts_optional_fields_instance.to_dict()
# create an instance of ArtifactsOptionalFields from a dict
artifacts_optional_fields_from_dict = ArtifactsOptionalFields.from_dict(artifacts_optional_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


