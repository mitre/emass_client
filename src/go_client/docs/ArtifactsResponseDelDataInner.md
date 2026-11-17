# ArtifactsResponseDelDataInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Filename** | Pointer to **string** | [Required] File name should match exactly one file within the provided zip file. 1000 Characters. | [optional] 
**Success** | Pointer to **bool** |  | [optional] 
**SystemId** | Pointer to **int64** |  | [optional] 

## Methods

### NewArtifactsResponseDelDataInner

`func NewArtifactsResponseDelDataInner() *ArtifactsResponseDelDataInner`

NewArtifactsResponseDelDataInner instantiates a new ArtifactsResponseDelDataInner object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewArtifactsResponseDelDataInnerWithDefaults

`func NewArtifactsResponseDelDataInnerWithDefaults() *ArtifactsResponseDelDataInner`

NewArtifactsResponseDelDataInnerWithDefaults instantiates a new ArtifactsResponseDelDataInner object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetFilename

`func (o *ArtifactsResponseDelDataInner) GetFilename() string`

GetFilename returns the Filename field if non-nil, zero value otherwise.

### GetFilenameOk

`func (o *ArtifactsResponseDelDataInner) GetFilenameOk() (*string, bool)`

GetFilenameOk returns a tuple with the Filename field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFilename

`func (o *ArtifactsResponseDelDataInner) SetFilename(v string)`

SetFilename sets Filename field to given value.

### HasFilename

`func (o *ArtifactsResponseDelDataInner) HasFilename() bool`

HasFilename returns a boolean if a field has been set.

### GetSuccess

`func (o *ArtifactsResponseDelDataInner) GetSuccess() bool`

GetSuccess returns the Success field if non-nil, zero value otherwise.

### GetSuccessOk

`func (o *ArtifactsResponseDelDataInner) GetSuccessOk() (*bool, bool)`

GetSuccessOk returns a tuple with the Success field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSuccess

`func (o *ArtifactsResponseDelDataInner) SetSuccess(v bool)`

SetSuccess sets Success field to given value.

### HasSuccess

`func (o *ArtifactsResponseDelDataInner) HasSuccess() bool`

HasSuccess returns a boolean if a field has been set.

### GetSystemId

`func (o *ArtifactsResponseDelDataInner) GetSystemId() int64`

GetSystemId returns the SystemId field if non-nil, zero value otherwise.

### GetSystemIdOk

`func (o *ArtifactsResponseDelDataInner) GetSystemIdOk() (*int64, bool)`

GetSystemIdOk returns a tuple with the SystemId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSystemId

`func (o *ArtifactsResponseDelDataInner) SetSystemId(v int64)`

SetSystemId sets SystemId field to given value.

### HasSystemId

`func (o *ArtifactsResponseDelDataInner) HasSystemId() bool`

HasSystemId returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


