# ArtifactsResponsePutPostDataInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Filename** | Pointer to **string** | [Required] File name should match exactly one file within the provided zip file. 1000 Characters. | [optional] 
**Success** | Pointer to **bool** |  | [optional] 
**SystemId** | Pointer to **int64** |  | [optional] 
**Errors** | Pointer to **[]interface{}** |  | [optional] 

## Methods

### NewArtifactsResponsePutPostDataInner

`func NewArtifactsResponsePutPostDataInner() *ArtifactsResponsePutPostDataInner`

NewArtifactsResponsePutPostDataInner instantiates a new ArtifactsResponsePutPostDataInner object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewArtifactsResponsePutPostDataInnerWithDefaults

`func NewArtifactsResponsePutPostDataInnerWithDefaults() *ArtifactsResponsePutPostDataInner`

NewArtifactsResponsePutPostDataInnerWithDefaults instantiates a new ArtifactsResponsePutPostDataInner object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetFilename

`func (o *ArtifactsResponsePutPostDataInner) GetFilename() string`

GetFilename returns the Filename field if non-nil, zero value otherwise.

### GetFilenameOk

`func (o *ArtifactsResponsePutPostDataInner) GetFilenameOk() (*string, bool)`

GetFilenameOk returns a tuple with the Filename field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFilename

`func (o *ArtifactsResponsePutPostDataInner) SetFilename(v string)`

SetFilename sets Filename field to given value.

### HasFilename

`func (o *ArtifactsResponsePutPostDataInner) HasFilename() bool`

HasFilename returns a boolean if a field has been set.

### GetSuccess

`func (o *ArtifactsResponsePutPostDataInner) GetSuccess() bool`

GetSuccess returns the Success field if non-nil, zero value otherwise.

### GetSuccessOk

`func (o *ArtifactsResponsePutPostDataInner) GetSuccessOk() (*bool, bool)`

GetSuccessOk returns a tuple with the Success field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSuccess

`func (o *ArtifactsResponsePutPostDataInner) SetSuccess(v bool)`

SetSuccess sets Success field to given value.

### HasSuccess

`func (o *ArtifactsResponsePutPostDataInner) HasSuccess() bool`

HasSuccess returns a boolean if a field has been set.

### GetSystemId

`func (o *ArtifactsResponsePutPostDataInner) GetSystemId() int64`

GetSystemId returns the SystemId field if non-nil, zero value otherwise.

### GetSystemIdOk

`func (o *ArtifactsResponsePutPostDataInner) GetSystemIdOk() (*int64, bool)`

GetSystemIdOk returns a tuple with the SystemId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSystemId

`func (o *ArtifactsResponsePutPostDataInner) SetSystemId(v int64)`

SetSystemId sets SystemId field to given value.

### HasSystemId

`func (o *ArtifactsResponsePutPostDataInner) HasSystemId() bool`

HasSystemId returns a boolean if a field has been set.

### GetErrors

`func (o *ArtifactsResponsePutPostDataInner) GetErrors() []interface{}`

GetErrors returns the Errors field if non-nil, zero value otherwise.

### GetErrorsOk

`func (o *ArtifactsResponsePutPostDataInner) GetErrorsOk() (*[]interface{}, bool)`

GetErrorsOk returns a tuple with the Errors field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetErrors

`func (o *ArtifactsResponsePutPostDataInner) SetErrors(v []interface{})`

SetErrors sets Errors field to given value.

### HasErrors

`func (o *ArtifactsResponsePutPostDataInner) HasErrors() bool`

HasErrors returns a boolean if a field has been set.

### SetErrorsNil

`func (o *ArtifactsResponsePutPostDataInner) SetErrorsNil(b bool)`

 SetErrorsNil sets the value for Errors to be an explicit nil

### UnsetErrors
`func (o *ArtifactsResponsePutPostDataInner) UnsetErrors()`

UnsetErrors ensures that no value is present for Errors, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


