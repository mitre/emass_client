# StaticCodeRequestPostBody

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Application** | Pointer to [**StaticCodeRequestPostBodyApplication**](StaticCodeRequestPostBodyApplication.md) |  | [optional] 
**ApplicationFindings** | Pointer to [**[]StaticCodeApplicationPost**](StaticCodeApplicationPost.md) |  | [optional] 

## Methods

### NewStaticCodeRequestPostBody

`func NewStaticCodeRequestPostBody() *StaticCodeRequestPostBody`

NewStaticCodeRequestPostBody instantiates a new StaticCodeRequestPostBody object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewStaticCodeRequestPostBodyWithDefaults

`func NewStaticCodeRequestPostBodyWithDefaults() *StaticCodeRequestPostBody`

NewStaticCodeRequestPostBodyWithDefaults instantiates a new StaticCodeRequestPostBody object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetApplication

`func (o *StaticCodeRequestPostBody) GetApplication() StaticCodeRequestPostBodyApplication`

GetApplication returns the Application field if non-nil, zero value otherwise.

### GetApplicationOk

`func (o *StaticCodeRequestPostBody) GetApplicationOk() (*StaticCodeRequestPostBodyApplication, bool)`

GetApplicationOk returns a tuple with the Application field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetApplication

`func (o *StaticCodeRequestPostBody) SetApplication(v StaticCodeRequestPostBodyApplication)`

SetApplication sets Application field to given value.

### HasApplication

`func (o *StaticCodeRequestPostBody) HasApplication() bool`

HasApplication returns a boolean if a field has been set.

### GetApplicationFindings

`func (o *StaticCodeRequestPostBody) GetApplicationFindings() []StaticCodeApplicationPost`

GetApplicationFindings returns the ApplicationFindings field if non-nil, zero value otherwise.

### GetApplicationFindingsOk

`func (o *StaticCodeRequestPostBody) GetApplicationFindingsOk() (*[]StaticCodeApplicationPost, bool)`

GetApplicationFindingsOk returns a tuple with the ApplicationFindings field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetApplicationFindings

`func (o *StaticCodeRequestPostBody) SetApplicationFindings(v []StaticCodeApplicationPost)`

SetApplicationFindings sets ApplicationFindings field to given value.

### HasApplicationFindings

`func (o *StaticCodeRequestPostBody) HasApplicationFindings() bool`

HasApplicationFindings returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


