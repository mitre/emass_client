# ArtifactsOptionalFields

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | Pointer to **NullableString** | [Optional] Artifact name. Character Limit &#x3D; 100. | [optional] 
**Description** | Pointer to **NullableString** | [Optional] Artifact description. 10,000 Characters. | [optional] 
**ReferencePageNumber** | Pointer to **NullableString** | [Optional] Artifact reference page number. 50 Characters. | [optional] 
**AssessmentProcedures** | Pointer to **string** | [Optional] The Security Control Assessment Procedure being associated with the artifact. | [optional] 
**Controls** | Pointer to **NullableString** | [Optional] Control acronym associated with the artifact. NIST SP 800-53 Revision 4 defined. | [optional] 
**ExpirationDate** | Pointer to **NullableInt64** | [Optional] Date Artifact expires and requires review. In Unix Date format. | [optional] 
**LastReviewedDate** | Pointer to **NullableInt64** | [Optional] Date Artifact was last reviewed. Unix time format. | [optional] 
**SignedDate** | Pointer to **NullableInt64** | [Optional] Date artifact was signed. Unix time format. | [optional] 

## Methods

### NewArtifactsOptionalFields

`func NewArtifactsOptionalFields() *ArtifactsOptionalFields`

NewArtifactsOptionalFields instantiates a new ArtifactsOptionalFields object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewArtifactsOptionalFieldsWithDefaults

`func NewArtifactsOptionalFieldsWithDefaults() *ArtifactsOptionalFields`

NewArtifactsOptionalFieldsWithDefaults instantiates a new ArtifactsOptionalFields object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *ArtifactsOptionalFields) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *ArtifactsOptionalFields) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *ArtifactsOptionalFields) SetName(v string)`

SetName sets Name field to given value.

### HasName

`func (o *ArtifactsOptionalFields) HasName() bool`

HasName returns a boolean if a field has been set.

### SetNameNil

`func (o *ArtifactsOptionalFields) SetNameNil(b bool)`

 SetNameNil sets the value for Name to be an explicit nil

### UnsetName
`func (o *ArtifactsOptionalFields) UnsetName()`

UnsetName ensures that no value is present for Name, not even an explicit nil
### GetDescription

`func (o *ArtifactsOptionalFields) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *ArtifactsOptionalFields) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *ArtifactsOptionalFields) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *ArtifactsOptionalFields) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### SetDescriptionNil

`func (o *ArtifactsOptionalFields) SetDescriptionNil(b bool)`

 SetDescriptionNil sets the value for Description to be an explicit nil

### UnsetDescription
`func (o *ArtifactsOptionalFields) UnsetDescription()`

UnsetDescription ensures that no value is present for Description, not even an explicit nil
### GetReferencePageNumber

`func (o *ArtifactsOptionalFields) GetReferencePageNumber() string`

GetReferencePageNumber returns the ReferencePageNumber field if non-nil, zero value otherwise.

### GetReferencePageNumberOk

`func (o *ArtifactsOptionalFields) GetReferencePageNumberOk() (*string, bool)`

GetReferencePageNumberOk returns a tuple with the ReferencePageNumber field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetReferencePageNumber

`func (o *ArtifactsOptionalFields) SetReferencePageNumber(v string)`

SetReferencePageNumber sets ReferencePageNumber field to given value.

### HasReferencePageNumber

`func (o *ArtifactsOptionalFields) HasReferencePageNumber() bool`

HasReferencePageNumber returns a boolean if a field has been set.

### SetReferencePageNumberNil

`func (o *ArtifactsOptionalFields) SetReferencePageNumberNil(b bool)`

 SetReferencePageNumberNil sets the value for ReferencePageNumber to be an explicit nil

### UnsetReferencePageNumber
`func (o *ArtifactsOptionalFields) UnsetReferencePageNumber()`

UnsetReferencePageNumber ensures that no value is present for ReferencePageNumber, not even an explicit nil
### GetAssessmentProcedures

`func (o *ArtifactsOptionalFields) GetAssessmentProcedures() string`

GetAssessmentProcedures returns the AssessmentProcedures field if non-nil, zero value otherwise.

### GetAssessmentProceduresOk

`func (o *ArtifactsOptionalFields) GetAssessmentProceduresOk() (*string, bool)`

GetAssessmentProceduresOk returns a tuple with the AssessmentProcedures field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAssessmentProcedures

`func (o *ArtifactsOptionalFields) SetAssessmentProcedures(v string)`

SetAssessmentProcedures sets AssessmentProcedures field to given value.

### HasAssessmentProcedures

`func (o *ArtifactsOptionalFields) HasAssessmentProcedures() bool`

HasAssessmentProcedures returns a boolean if a field has been set.

### GetControls

`func (o *ArtifactsOptionalFields) GetControls() string`

GetControls returns the Controls field if non-nil, zero value otherwise.

### GetControlsOk

`func (o *ArtifactsOptionalFields) GetControlsOk() (*string, bool)`

GetControlsOk returns a tuple with the Controls field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetControls

`func (o *ArtifactsOptionalFields) SetControls(v string)`

SetControls sets Controls field to given value.

### HasControls

`func (o *ArtifactsOptionalFields) HasControls() bool`

HasControls returns a boolean if a field has been set.

### SetControlsNil

`func (o *ArtifactsOptionalFields) SetControlsNil(b bool)`

 SetControlsNil sets the value for Controls to be an explicit nil

### UnsetControls
`func (o *ArtifactsOptionalFields) UnsetControls()`

UnsetControls ensures that no value is present for Controls, not even an explicit nil
### GetExpirationDate

`func (o *ArtifactsOptionalFields) GetExpirationDate() int64`

GetExpirationDate returns the ExpirationDate field if non-nil, zero value otherwise.

### GetExpirationDateOk

`func (o *ArtifactsOptionalFields) GetExpirationDateOk() (*int64, bool)`

GetExpirationDateOk returns a tuple with the ExpirationDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExpirationDate

`func (o *ArtifactsOptionalFields) SetExpirationDate(v int64)`

SetExpirationDate sets ExpirationDate field to given value.

### HasExpirationDate

`func (o *ArtifactsOptionalFields) HasExpirationDate() bool`

HasExpirationDate returns a boolean if a field has been set.

### SetExpirationDateNil

`func (o *ArtifactsOptionalFields) SetExpirationDateNil(b bool)`

 SetExpirationDateNil sets the value for ExpirationDate to be an explicit nil

### UnsetExpirationDate
`func (o *ArtifactsOptionalFields) UnsetExpirationDate()`

UnsetExpirationDate ensures that no value is present for ExpirationDate, not even an explicit nil
### GetLastReviewedDate

`func (o *ArtifactsOptionalFields) GetLastReviewedDate() int64`

GetLastReviewedDate returns the LastReviewedDate field if non-nil, zero value otherwise.

### GetLastReviewedDateOk

`func (o *ArtifactsOptionalFields) GetLastReviewedDateOk() (*int64, bool)`

GetLastReviewedDateOk returns a tuple with the LastReviewedDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLastReviewedDate

`func (o *ArtifactsOptionalFields) SetLastReviewedDate(v int64)`

SetLastReviewedDate sets LastReviewedDate field to given value.

### HasLastReviewedDate

`func (o *ArtifactsOptionalFields) HasLastReviewedDate() bool`

HasLastReviewedDate returns a boolean if a field has been set.

### SetLastReviewedDateNil

`func (o *ArtifactsOptionalFields) SetLastReviewedDateNil(b bool)`

 SetLastReviewedDateNil sets the value for LastReviewedDate to be an explicit nil

### UnsetLastReviewedDate
`func (o *ArtifactsOptionalFields) UnsetLastReviewedDate()`

UnsetLastReviewedDate ensures that no value is present for LastReviewedDate, not even an explicit nil
### GetSignedDate

`func (o *ArtifactsOptionalFields) GetSignedDate() int64`

GetSignedDate returns the SignedDate field if non-nil, zero value otherwise.

### GetSignedDateOk

`func (o *ArtifactsOptionalFields) GetSignedDateOk() (*int64, bool)`

GetSignedDateOk returns a tuple with the SignedDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSignedDate

`func (o *ArtifactsOptionalFields) SetSignedDate(v int64)`

SetSignedDate sets SignedDate field to given value.

### HasSignedDate

`func (o *ArtifactsOptionalFields) HasSignedDate() bool`

HasSignedDate returns a boolean if a field has been set.

### SetSignedDateNil

`func (o *ArtifactsOptionalFields) SetSignedDateNil(b bool)`

 SetSignedDateNil sets the value for SignedDate to be an explicit nil

### UnsetSignedDate
`func (o *ArtifactsOptionalFields) UnsetSignedDate()`

UnsetSignedDate ensures that no value is present for SignedDate, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


