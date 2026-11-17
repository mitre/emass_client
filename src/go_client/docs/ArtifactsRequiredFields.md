# ArtifactsRequiredFields

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Filename** | Pointer to **string** | [Required] File name should match exactly one file within the provided zip file. 1000 Characters. or Application/zip file. Max 30MB per artifact.  | [optional] 
**IsTemplate** | Pointer to **NullableBool** | [Required] Indicates whether an artifact template. | [optional] 
**Type** | Pointer to **string** | [Required] Artifact type options | [optional] 
**Category** | Pointer to **string** | [Required] Artifact category options | [optional] 

## Methods

### NewArtifactsRequiredFields

`func NewArtifactsRequiredFields() *ArtifactsRequiredFields`

NewArtifactsRequiredFields instantiates a new ArtifactsRequiredFields object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewArtifactsRequiredFieldsWithDefaults

`func NewArtifactsRequiredFieldsWithDefaults() *ArtifactsRequiredFields`

NewArtifactsRequiredFieldsWithDefaults instantiates a new ArtifactsRequiredFields object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetFilename

`func (o *ArtifactsRequiredFields) GetFilename() string`

GetFilename returns the Filename field if non-nil, zero value otherwise.

### GetFilenameOk

`func (o *ArtifactsRequiredFields) GetFilenameOk() (*string, bool)`

GetFilenameOk returns a tuple with the Filename field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFilename

`func (o *ArtifactsRequiredFields) SetFilename(v string)`

SetFilename sets Filename field to given value.

### HasFilename

`func (o *ArtifactsRequiredFields) HasFilename() bool`

HasFilename returns a boolean if a field has been set.

### GetIsTemplate

`func (o *ArtifactsRequiredFields) GetIsTemplate() bool`

GetIsTemplate returns the IsTemplate field if non-nil, zero value otherwise.

### GetIsTemplateOk

`func (o *ArtifactsRequiredFields) GetIsTemplateOk() (*bool, bool)`

GetIsTemplateOk returns a tuple with the IsTemplate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsTemplate

`func (o *ArtifactsRequiredFields) SetIsTemplate(v bool)`

SetIsTemplate sets IsTemplate field to given value.

### HasIsTemplate

`func (o *ArtifactsRequiredFields) HasIsTemplate() bool`

HasIsTemplate returns a boolean if a field has been set.

### SetIsTemplateNil

`func (o *ArtifactsRequiredFields) SetIsTemplateNil(b bool)`

 SetIsTemplateNil sets the value for IsTemplate to be an explicit nil

### UnsetIsTemplate
`func (o *ArtifactsRequiredFields) UnsetIsTemplate()`

UnsetIsTemplate ensures that no value is present for IsTemplate, not even an explicit nil
### GetType

`func (o *ArtifactsRequiredFields) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *ArtifactsRequiredFields) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *ArtifactsRequiredFields) SetType(v string)`

SetType sets Type field to given value.

### HasType

`func (o *ArtifactsRequiredFields) HasType() bool`

HasType returns a boolean if a field has been set.

### GetCategory

`func (o *ArtifactsRequiredFields) GetCategory() string`

GetCategory returns the Category field if non-nil, zero value otherwise.

### GetCategoryOk

`func (o *ArtifactsRequiredFields) GetCategoryOk() (*string, bool)`

GetCategoryOk returns a tuple with the Category field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCategory

`func (o *ArtifactsRequiredFields) SetCategory(v string)`

SetCategory sets Category field to given value.

### HasCategory

`func (o *ArtifactsRequiredFields) HasCategory() bool`

HasCategory returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


