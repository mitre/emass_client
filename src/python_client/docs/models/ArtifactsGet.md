# emass_client.model.artifacts_get.ArtifactsGet

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**systemId** | decimal.Decimal, int,  | decimal.Decimal,  | [Required] Unique eMASS system identifier. | [optional] value must be a 64 bit integer
**filename** | str,  | str,  | [Required] File name should match exactly one file within the provided zip file. 1000 Characters. | [optional] 
**isInherited** | None, bool,  | NoneClass, BoolClass,  | [Read-only] Indicates whether an artifact is inherited. | [optional] 
**isTemplate** | None, bool,  | NoneClass, BoolClass,  | [Required] Indicates whether an artifact template. | [optional] 
**type** | str,  | str,  | [Required] Artifact type options | [optional] 
**category** | str,  | str,  | [Required] Artifact category options | [optional] 
**name** | None, str,  | NoneClass, str,  | [Optional] Artifact name. Character Limit &#x3D; 100. | [optional] 
**description** | None, str,  | NoneClass, str,  | [Optional] Artifact description. 10,000 Characters. | [optional] 
**referencePageNumber** | None, str,  | NoneClass, str,  | [Optional] Artifact reference page number. 50 Characters. | [optional] 
**ccis** | None, str,  | NoneClass, str,  | [Optional] CCI associated with test result. | [optional] 
**controls** | None, str,  | NoneClass, str,  | [Optional] Control acronym associated with the artifact. NIST SP 800-53 Revision 4 defined. | [optional] 
**mimeContentType** | None, str,  | NoneClass, str,  | [Read-Only] Standard MIME content type derived from file extension. | [optional] 
**fileSize** | None, str,  | NoneClass, str,  | [Read-Only] File size of attached artifact. | [optional] 
**expirationDate** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | [Optional] Date Artifact expires and requires review. In Unix Date format. | [optional] value must be a 64 bit integer
**lastReviewedDate** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | [Optional] Date Artifact was last reviewed. Unix time format. | [optional] value must be a 64 bit integer
**signedDate** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | [Optional] Date artifact was signed. Unix time format. | [optional] value must be a 64 bit integer

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

