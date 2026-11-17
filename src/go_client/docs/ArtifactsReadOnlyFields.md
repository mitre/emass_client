# ArtifactsReadOnlyFields

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**IsInherited** | Pointer to **NullableBool** | [Read-only] Indicates whether an artifact is inherited. | [optional] 
**Ccis** | Pointer to **NullableString** | [Read-Only] CCI mapping for Assessment Procedures associated with the artifact. | [optional] 
**MimeContentType** | Pointer to **NullableString** | [Read-Only] Standard MIME content type derived from file extension. | [optional] 
**FileSize** | Pointer to **NullableString** | [Read-Only] File size of attached artifact. | [optional] 

## Methods

### NewArtifactsReadOnlyFields

`func NewArtifactsReadOnlyFields() *ArtifactsReadOnlyFields`

NewArtifactsReadOnlyFields instantiates a new ArtifactsReadOnlyFields object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewArtifactsReadOnlyFieldsWithDefaults

`func NewArtifactsReadOnlyFieldsWithDefaults() *ArtifactsReadOnlyFields`

NewArtifactsReadOnlyFieldsWithDefaults instantiates a new ArtifactsReadOnlyFields object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetIsInherited

`func (o *ArtifactsReadOnlyFields) GetIsInherited() bool`

GetIsInherited returns the IsInherited field if non-nil, zero value otherwise.

### GetIsInheritedOk

`func (o *ArtifactsReadOnlyFields) GetIsInheritedOk() (*bool, bool)`

GetIsInheritedOk returns a tuple with the IsInherited field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsInherited

`func (o *ArtifactsReadOnlyFields) SetIsInherited(v bool)`

SetIsInherited sets IsInherited field to given value.

### HasIsInherited

`func (o *ArtifactsReadOnlyFields) HasIsInherited() bool`

HasIsInherited returns a boolean if a field has been set.

### SetIsInheritedNil

`func (o *ArtifactsReadOnlyFields) SetIsInheritedNil(b bool)`

 SetIsInheritedNil sets the value for IsInherited to be an explicit nil

### UnsetIsInherited
`func (o *ArtifactsReadOnlyFields) UnsetIsInherited()`

UnsetIsInherited ensures that no value is present for IsInherited, not even an explicit nil
### GetCcis

`func (o *ArtifactsReadOnlyFields) GetCcis() string`

GetCcis returns the Ccis field if non-nil, zero value otherwise.

### GetCcisOk

`func (o *ArtifactsReadOnlyFields) GetCcisOk() (*string, bool)`

GetCcisOk returns a tuple with the Ccis field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCcis

`func (o *ArtifactsReadOnlyFields) SetCcis(v string)`

SetCcis sets Ccis field to given value.

### HasCcis

`func (o *ArtifactsReadOnlyFields) HasCcis() bool`

HasCcis returns a boolean if a field has been set.

### SetCcisNil

`func (o *ArtifactsReadOnlyFields) SetCcisNil(b bool)`

 SetCcisNil sets the value for Ccis to be an explicit nil

### UnsetCcis
`func (o *ArtifactsReadOnlyFields) UnsetCcis()`

UnsetCcis ensures that no value is present for Ccis, not even an explicit nil
### GetMimeContentType

`func (o *ArtifactsReadOnlyFields) GetMimeContentType() string`

GetMimeContentType returns the MimeContentType field if non-nil, zero value otherwise.

### GetMimeContentTypeOk

`func (o *ArtifactsReadOnlyFields) GetMimeContentTypeOk() (*string, bool)`

GetMimeContentTypeOk returns a tuple with the MimeContentType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMimeContentType

`func (o *ArtifactsReadOnlyFields) SetMimeContentType(v string)`

SetMimeContentType sets MimeContentType field to given value.

### HasMimeContentType

`func (o *ArtifactsReadOnlyFields) HasMimeContentType() bool`

HasMimeContentType returns a boolean if a field has been set.

### SetMimeContentTypeNil

`func (o *ArtifactsReadOnlyFields) SetMimeContentTypeNil(b bool)`

 SetMimeContentTypeNil sets the value for MimeContentType to be an explicit nil

### UnsetMimeContentType
`func (o *ArtifactsReadOnlyFields) UnsetMimeContentType()`

UnsetMimeContentType ensures that no value is present for MimeContentType, not even an explicit nil
### GetFileSize

`func (o *ArtifactsReadOnlyFields) GetFileSize() string`

GetFileSize returns the FileSize field if non-nil, zero value otherwise.

### GetFileSizeOk

`func (o *ArtifactsReadOnlyFields) GetFileSizeOk() (*string, bool)`

GetFileSizeOk returns a tuple with the FileSize field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFileSize

`func (o *ArtifactsReadOnlyFields) SetFileSize(v string)`

SetFileSize sets FileSize field to given value.

### HasFileSize

`func (o *ArtifactsReadOnlyFields) HasFileSize() bool`

HasFileSize returns a boolean if a field has been set.

### SetFileSizeNil

`func (o *ArtifactsReadOnlyFields) SetFileSizeNil(b bool)`

 SetFileSizeNil sets the value for FileSize to be an explicit nil

### UnsetFileSize
`func (o *ArtifactsReadOnlyFields) UnsetFileSize()`

UnsetFileSize ensures that no value is present for FileSize, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


