# TestResultsResponsePost

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Meta** | Pointer to [**Response200**](Response200.md) |  | [optional] 
**Data** | Pointer to [**[]TestResultsPost**](TestResultsPost.md) |  | [optional] 

## Methods

### NewTestResultsResponsePost

`func NewTestResultsResponsePost() *TestResultsResponsePost`

NewTestResultsResponsePost instantiates a new TestResultsResponsePost object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewTestResultsResponsePostWithDefaults

`func NewTestResultsResponsePostWithDefaults() *TestResultsResponsePost`

NewTestResultsResponsePostWithDefaults instantiates a new TestResultsResponsePost object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetMeta

`func (o *TestResultsResponsePost) GetMeta() Response200`

GetMeta returns the Meta field if non-nil, zero value otherwise.

### GetMetaOk

`func (o *TestResultsResponsePost) GetMetaOk() (*Response200, bool)`

GetMetaOk returns a tuple with the Meta field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMeta

`func (o *TestResultsResponsePost) SetMeta(v Response200)`

SetMeta sets Meta field to given value.

### HasMeta

`func (o *TestResultsResponsePost) HasMeta() bool`

HasMeta returns a boolean if a field has been set.

### GetData

`func (o *TestResultsResponsePost) GetData() []TestResultsPost`

GetData returns the Data field if non-nil, zero value otherwise.

### GetDataOk

`func (o *TestResultsResponsePost) GetDataOk() (*[]TestResultsPost, bool)`

GetDataOk returns a tuple with the Data field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetData

`func (o *TestResultsResponsePost) SetData(v []TestResultsPost)`

SetData sets Data field to given value.

### HasData

`func (o *TestResultsResponsePost) HasData() bool`

HasData returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


