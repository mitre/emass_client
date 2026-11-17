# ArtifactsResponseGetDataInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**SystemId** | Pointer to **int64** | [Required] Unique eMASS system identifier. | [optional] 
**Filename** | Pointer to **string** | [Required] File name should match exactly one file within the provided zip file. 1000 Characters. or Application/zip file. Max 30MB per artifact.  | [optional] 
**IsTemplate** | Pointer to **NullableBool** | [Required] Indicates whether an artifact template. | [optional] 
**Type** | Pointer to **string** | [Required] Artifact type options | [optional] 
**Category** | Pointer to **string** | [Required] Artifact category options | [optional] 
**IsInherited** | Pointer to **NullableBool** | [Read-only] Indicates whether an artifact is inherited. | [optional] 
**Ccis** | Pointer to **NullableString** | [Read-Only] CCI mapping for Assessment Procedures associated with the artifact. | [optional] 
**MimeContentType** | Pointer to **NullableString** | [Read-Only] Standard MIME content type derived from file extension. | [optional] 
**FileSize** | Pointer to **NullableString** | [Read-Only] File size of attached artifact. | [optional] 
**Name** | Pointer to **NullableString** | [Optional] Artifact name. Character Limit &#x3D; 100. | [optional] 
**Description** | Pointer to **NullableString** | [Optional] Artifact description. 10,000 Characters. | [optional] 
**ReferencePageNumber** | Pointer to **NullableString** | [Optional] Artifact reference page number. 50 Characters. | [optional] 
**AssessmentProcedures** | Pointer to **string** | [Optional] The Security Control Assessment Procedure being associated with the artifact. | [optional] 
**Controls** | Pointer to **NullableString** | [Optional] Control acronym associated with the artifact. NIST SP 800-53 Revision 4 defined. | [optional] 
**ExpirationDate** | Pointer to **NullableInt64** | [Optional] Date Artifact expires and requires review. In Unix Date format. | [optional] 
**LastReviewedDate** | Pointer to **NullableInt64** | [Optional] Date Artifact was last reviewed. Unix time format. | [optional] 
**SignedDate** | Pointer to **NullableInt64** | [Optional] Date artifact was signed. Unix time format. | [optional] 

## Methods

### NewArtifactsResponseGetDataInner

`func NewArtifactsResponseGetDataInner() *ArtifactsResponseGetDataInner`

NewArtifactsResponseGetDataInner instantiates a new ArtifactsResponseGetDataInner object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewArtifactsResponseGetDataInnerWithDefaults

`func NewArtifactsResponseGetDataInnerWithDefaults() *ArtifactsResponseGetDataInner`

NewArtifactsResponseGetDataInnerWithDefaults instantiates a new ArtifactsResponseGetDataInner object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetSystemId

`func (o *ArtifactsResponseGetDataInner) GetSystemId() int64`

GetSystemId returns the SystemId field if non-nil, zero value otherwise.

### GetSystemIdOk

`func (o *ArtifactsResponseGetDataInner) GetSystemIdOk() (*int64, bool)`

GetSystemIdOk returns a tuple with the SystemId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSystemId

`func (o *ArtifactsResponseGetDataInner) SetSystemId(v int64)`

SetSystemId sets SystemId field to given value.

### HasSystemId

`func (o *ArtifactsResponseGetDataInner) HasSystemId() bool`

HasSystemId returns a boolean if a field has been set.

### GetFilename

`func (o *ArtifactsResponseGetDataInner) GetFilename() string`

GetFilename returns the Filename field if non-nil, zero value otherwise.

### GetFilenameOk

`func (o *ArtifactsResponseGetDataInner) GetFilenameOk() (*string, bool)`

GetFilenameOk returns a tuple with the Filename field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFilename

`func (o *ArtifactsResponseGetDataInner) SetFilename(v string)`

SetFilename sets Filename field to given value.

### HasFilename

`func (o *ArtifactsResponseGetDataInner) HasFilename() bool`

HasFilename returns a boolean if a field has been set.

### GetIsTemplate

`func (o *ArtifactsResponseGetDataInner) GetIsTemplate() bool`

GetIsTemplate returns the IsTemplate field if non-nil, zero value otherwise.

### GetIsTemplateOk

`func (o *ArtifactsResponseGetDataInner) GetIsTemplateOk() (*bool, bool)`

GetIsTemplateOk returns a tuple with the IsTemplate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsTemplate

`func (o *ArtifactsResponseGetDataInner) SetIsTemplate(v bool)`

SetIsTemplate sets IsTemplate field to given value.

### HasIsTemplate

`func (o *ArtifactsResponseGetDataInner) HasIsTemplate() bool`

HasIsTemplate returns a boolean if a field has been set.

### SetIsTemplateNil

`func (o *ArtifactsResponseGetDataInner) SetIsTemplateNil(b bool)`

 SetIsTemplateNil sets the value for IsTemplate to be an explicit nil

### UnsetIsTemplate
`func (o *ArtifactsResponseGetDataInner) UnsetIsTemplate()`

UnsetIsTemplate ensures that no value is present for IsTemplate, not even an explicit nil
### GetType

`func (o *ArtifactsResponseGetDataInner) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *ArtifactsResponseGetDataInner) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *ArtifactsResponseGetDataInner) SetType(v string)`

SetType sets Type field to given value.

### HasType

`func (o *ArtifactsResponseGetDataInner) HasType() bool`

HasType returns a boolean if a field has been set.

### GetCategory

`func (o *ArtifactsResponseGetDataInner) GetCategory() string`

GetCategory returns the Category field if non-nil, zero value otherwise.

### GetCategoryOk

`func (o *ArtifactsResponseGetDataInner) GetCategoryOk() (*string, bool)`

GetCategoryOk returns a tuple with the Category field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCategory

`func (o *ArtifactsResponseGetDataInner) SetCategory(v string)`

SetCategory sets Category field to given value.

### HasCategory

`func (o *ArtifactsResponseGetDataInner) HasCategory() bool`

HasCategory returns a boolean if a field has been set.

### GetIsInherited

`func (o *ArtifactsResponseGetDataInner) GetIsInherited() bool`

GetIsInherited returns the IsInherited field if non-nil, zero value otherwise.

### GetIsInheritedOk

`func (o *ArtifactsResponseGetDataInner) GetIsInheritedOk() (*bool, bool)`

GetIsInheritedOk returns a tuple with the IsInherited field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsInherited

`func (o *ArtifactsResponseGetDataInner) SetIsInherited(v bool)`

SetIsInherited sets IsInherited field to given value.

### HasIsInherited

`func (o *ArtifactsResponseGetDataInner) HasIsInherited() bool`

HasIsInherited returns a boolean if a field has been set.

### SetIsInheritedNil

`func (o *ArtifactsResponseGetDataInner) SetIsInheritedNil(b bool)`

 SetIsInheritedNil sets the value for IsInherited to be an explicit nil

### UnsetIsInherited
`func (o *ArtifactsResponseGetDataInner) UnsetIsInherited()`

UnsetIsInherited ensures that no value is present for IsInherited, not even an explicit nil
### GetCcis

`func (o *ArtifactsResponseGetDataInner) GetCcis() string`

GetCcis returns the Ccis field if non-nil, zero value otherwise.

### GetCcisOk

`func (o *ArtifactsResponseGetDataInner) GetCcisOk() (*string, bool)`

GetCcisOk returns a tuple with the Ccis field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCcis

`func (o *ArtifactsResponseGetDataInner) SetCcis(v string)`

SetCcis sets Ccis field to given value.

### HasCcis

`func (o *ArtifactsResponseGetDataInner) HasCcis() bool`

HasCcis returns a boolean if a field has been set.

### SetCcisNil

`func (o *ArtifactsResponseGetDataInner) SetCcisNil(b bool)`

 SetCcisNil sets the value for Ccis to be an explicit nil

### UnsetCcis
`func (o *ArtifactsResponseGetDataInner) UnsetCcis()`

UnsetCcis ensures that no value is present for Ccis, not even an explicit nil
### GetMimeContentType

`func (o *ArtifactsResponseGetDataInner) GetMimeContentType() string`

GetMimeContentType returns the MimeContentType field if non-nil, zero value otherwise.

### GetMimeContentTypeOk

`func (o *ArtifactsResponseGetDataInner) GetMimeContentTypeOk() (*string, bool)`

GetMimeContentTypeOk returns a tuple with the MimeContentType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMimeContentType

`func (o *ArtifactsResponseGetDataInner) SetMimeContentType(v string)`

SetMimeContentType sets MimeContentType field to given value.

### HasMimeContentType

`func (o *ArtifactsResponseGetDataInner) HasMimeContentType() bool`

HasMimeContentType returns a boolean if a field has been set.

### SetMimeContentTypeNil

`func (o *ArtifactsResponseGetDataInner) SetMimeContentTypeNil(b bool)`

 SetMimeContentTypeNil sets the value for MimeContentType to be an explicit nil

### UnsetMimeContentType
`func (o *ArtifactsResponseGetDataInner) UnsetMimeContentType()`

UnsetMimeContentType ensures that no value is present for MimeContentType, not even an explicit nil
### GetFileSize

`func (o *ArtifactsResponseGetDataInner) GetFileSize() string`

GetFileSize returns the FileSize field if non-nil, zero value otherwise.

### GetFileSizeOk

`func (o *ArtifactsResponseGetDataInner) GetFileSizeOk() (*string, bool)`

GetFileSizeOk returns a tuple with the FileSize field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFileSize

`func (o *ArtifactsResponseGetDataInner) SetFileSize(v string)`

SetFileSize sets FileSize field to given value.

### HasFileSize

`func (o *ArtifactsResponseGetDataInner) HasFileSize() bool`

HasFileSize returns a boolean if a field has been set.

### SetFileSizeNil

`func (o *ArtifactsResponseGetDataInner) SetFileSizeNil(b bool)`

 SetFileSizeNil sets the value for FileSize to be an explicit nil

### UnsetFileSize
`func (o *ArtifactsResponseGetDataInner) UnsetFileSize()`

UnsetFileSize ensures that no value is present for FileSize, not even an explicit nil
### GetName

`func (o *ArtifactsResponseGetDataInner) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *ArtifactsResponseGetDataInner) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *ArtifactsResponseGetDataInner) SetName(v string)`

SetName sets Name field to given value.

### HasName

`func (o *ArtifactsResponseGetDataInner) HasName() bool`

HasName returns a boolean if a field has been set.

### SetNameNil

`func (o *ArtifactsResponseGetDataInner) SetNameNil(b bool)`

 SetNameNil sets the value for Name to be an explicit nil

### UnsetName
`func (o *ArtifactsResponseGetDataInner) UnsetName()`

UnsetName ensures that no value is present for Name, not even an explicit nil
### GetDescription

`func (o *ArtifactsResponseGetDataInner) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *ArtifactsResponseGetDataInner) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *ArtifactsResponseGetDataInner) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *ArtifactsResponseGetDataInner) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### SetDescriptionNil

`func (o *ArtifactsResponseGetDataInner) SetDescriptionNil(b bool)`

 SetDescriptionNil sets the value for Description to be an explicit nil

### UnsetDescription
`func (o *ArtifactsResponseGetDataInner) UnsetDescription()`

UnsetDescription ensures that no value is present for Description, not even an explicit nil
### GetReferencePageNumber

`func (o *ArtifactsResponseGetDataInner) GetReferencePageNumber() string`

GetReferencePageNumber returns the ReferencePageNumber field if non-nil, zero value otherwise.

### GetReferencePageNumberOk

`func (o *ArtifactsResponseGetDataInner) GetReferencePageNumberOk() (*string, bool)`

GetReferencePageNumberOk returns a tuple with the ReferencePageNumber field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetReferencePageNumber

`func (o *ArtifactsResponseGetDataInner) SetReferencePageNumber(v string)`

SetReferencePageNumber sets ReferencePageNumber field to given value.

### HasReferencePageNumber

`func (o *ArtifactsResponseGetDataInner) HasReferencePageNumber() bool`

HasReferencePageNumber returns a boolean if a field has been set.

### SetReferencePageNumberNil

`func (o *ArtifactsResponseGetDataInner) SetReferencePageNumberNil(b bool)`

 SetReferencePageNumberNil sets the value for ReferencePageNumber to be an explicit nil

### UnsetReferencePageNumber
`func (o *ArtifactsResponseGetDataInner) UnsetReferencePageNumber()`

UnsetReferencePageNumber ensures that no value is present for ReferencePageNumber, not even an explicit nil
### GetAssessmentProcedures

`func (o *ArtifactsResponseGetDataInner) GetAssessmentProcedures() string`

GetAssessmentProcedures returns the AssessmentProcedures field if non-nil, zero value otherwise.

### GetAssessmentProceduresOk

`func (o *ArtifactsResponseGetDataInner) GetAssessmentProceduresOk() (*string, bool)`

GetAssessmentProceduresOk returns a tuple with the AssessmentProcedures field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAssessmentProcedures

`func (o *ArtifactsResponseGetDataInner) SetAssessmentProcedures(v string)`

SetAssessmentProcedures sets AssessmentProcedures field to given value.

### HasAssessmentProcedures

`func (o *ArtifactsResponseGetDataInner) HasAssessmentProcedures() bool`

HasAssessmentProcedures returns a boolean if a field has been set.

### GetControls

`func (o *ArtifactsResponseGetDataInner) GetControls() string`

GetControls returns the Controls field if non-nil, zero value otherwise.

### GetControlsOk

`func (o *ArtifactsResponseGetDataInner) GetControlsOk() (*string, bool)`

GetControlsOk returns a tuple with the Controls field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetControls

`func (o *ArtifactsResponseGetDataInner) SetControls(v string)`

SetControls sets Controls field to given value.

### HasControls

`func (o *ArtifactsResponseGetDataInner) HasControls() bool`

HasControls returns a boolean if a field has been set.

### SetControlsNil

`func (o *ArtifactsResponseGetDataInner) SetControlsNil(b bool)`

 SetControlsNil sets the value for Controls to be an explicit nil

### UnsetControls
`func (o *ArtifactsResponseGetDataInner) UnsetControls()`

UnsetControls ensures that no value is present for Controls, not even an explicit nil
### GetExpirationDate

`func (o *ArtifactsResponseGetDataInner) GetExpirationDate() int64`

GetExpirationDate returns the ExpirationDate field if non-nil, zero value otherwise.

### GetExpirationDateOk

`func (o *ArtifactsResponseGetDataInner) GetExpirationDateOk() (*int64, bool)`

GetExpirationDateOk returns a tuple with the ExpirationDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExpirationDate

`func (o *ArtifactsResponseGetDataInner) SetExpirationDate(v int64)`

SetExpirationDate sets ExpirationDate field to given value.

### HasExpirationDate

`func (o *ArtifactsResponseGetDataInner) HasExpirationDate() bool`

HasExpirationDate returns a boolean if a field has been set.

### SetExpirationDateNil

`func (o *ArtifactsResponseGetDataInner) SetExpirationDateNil(b bool)`

 SetExpirationDateNil sets the value for ExpirationDate to be an explicit nil

### UnsetExpirationDate
`func (o *ArtifactsResponseGetDataInner) UnsetExpirationDate()`

UnsetExpirationDate ensures that no value is present for ExpirationDate, not even an explicit nil
### GetLastReviewedDate

`func (o *ArtifactsResponseGetDataInner) GetLastReviewedDate() int64`

GetLastReviewedDate returns the LastReviewedDate field if non-nil, zero value otherwise.

### GetLastReviewedDateOk

`func (o *ArtifactsResponseGetDataInner) GetLastReviewedDateOk() (*int64, bool)`

GetLastReviewedDateOk returns a tuple with the LastReviewedDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLastReviewedDate

`func (o *ArtifactsResponseGetDataInner) SetLastReviewedDate(v int64)`

SetLastReviewedDate sets LastReviewedDate field to given value.

### HasLastReviewedDate

`func (o *ArtifactsResponseGetDataInner) HasLastReviewedDate() bool`

HasLastReviewedDate returns a boolean if a field has been set.

### SetLastReviewedDateNil

`func (o *ArtifactsResponseGetDataInner) SetLastReviewedDateNil(b bool)`

 SetLastReviewedDateNil sets the value for LastReviewedDate to be an explicit nil

### UnsetLastReviewedDate
`func (o *ArtifactsResponseGetDataInner) UnsetLastReviewedDate()`

UnsetLastReviewedDate ensures that no value is present for LastReviewedDate, not even an explicit nil
### GetSignedDate

`func (o *ArtifactsResponseGetDataInner) GetSignedDate() int64`

GetSignedDate returns the SignedDate field if non-nil, zero value otherwise.

### GetSignedDateOk

`func (o *ArtifactsResponseGetDataInner) GetSignedDateOk() (*int64, bool)`

GetSignedDateOk returns a tuple with the SignedDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSignedDate

`func (o *ArtifactsResponseGetDataInner) SetSignedDate(v int64)`

SetSignedDate sets SignedDate field to given value.

### HasSignedDate

`func (o *ArtifactsResponseGetDataInner) HasSignedDate() bool`

HasSignedDate returns a boolean if a field has been set.

### SetSignedDateNil

`func (o *ArtifactsResponseGetDataInner) SetSignedDateNil(b bool)`

 SetSignedDateNil sets the value for SignedDate to be an explicit nil

### UnsetSignedDate
`func (o *ArtifactsResponseGetDataInner) UnsetSignedDate()`

UnsetSignedDate ensures that no value is present for SignedDate, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


