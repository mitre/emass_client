# TestResultsPost

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Cci** | Pointer to **string** | CCI associated with test result. | [optional] 
**Success** | Pointer to **bool** | Indicates if operations result (success/fail) | [optional] 
**SystemId** | Pointer to **int64** | The system identifier for the system being updated. | [optional] 
**Errors** | Pointer to **[]interface{}** |  | [optional] 

## Methods

### NewTestResultsPost

`func NewTestResultsPost() *TestResultsPost`

NewTestResultsPost instantiates a new TestResultsPost object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewTestResultsPostWithDefaults

`func NewTestResultsPostWithDefaults() *TestResultsPost`

NewTestResultsPostWithDefaults instantiates a new TestResultsPost object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCci

`func (o *TestResultsPost) GetCci() string`

GetCci returns the Cci field if non-nil, zero value otherwise.

### GetCciOk

`func (o *TestResultsPost) GetCciOk() (*string, bool)`

GetCciOk returns a tuple with the Cci field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCci

`func (o *TestResultsPost) SetCci(v string)`

SetCci sets Cci field to given value.

### HasCci

`func (o *TestResultsPost) HasCci() bool`

HasCci returns a boolean if a field has been set.

### GetSuccess

`func (o *TestResultsPost) GetSuccess() bool`

GetSuccess returns the Success field if non-nil, zero value otherwise.

### GetSuccessOk

`func (o *TestResultsPost) GetSuccessOk() (*bool, bool)`

GetSuccessOk returns a tuple with the Success field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSuccess

`func (o *TestResultsPost) SetSuccess(v bool)`

SetSuccess sets Success field to given value.

### HasSuccess

`func (o *TestResultsPost) HasSuccess() bool`

HasSuccess returns a boolean if a field has been set.

### GetSystemId

`func (o *TestResultsPost) GetSystemId() int64`

GetSystemId returns the SystemId field if non-nil, zero value otherwise.

### GetSystemIdOk

`func (o *TestResultsPost) GetSystemIdOk() (*int64, bool)`

GetSystemIdOk returns a tuple with the SystemId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSystemId

`func (o *TestResultsPost) SetSystemId(v int64)`

SetSystemId sets SystemId field to given value.

### HasSystemId

`func (o *TestResultsPost) HasSystemId() bool`

HasSystemId returns a boolean if a field has been set.

### GetErrors

`func (o *TestResultsPost) GetErrors() []interface{}`

GetErrors returns the Errors field if non-nil, zero value otherwise.

### GetErrorsOk

`func (o *TestResultsPost) GetErrorsOk() (*[]interface{}, bool)`

GetErrorsOk returns a tuple with the Errors field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetErrors

`func (o *TestResultsPost) SetErrors(v []interface{})`

SetErrors sets Errors field to given value.

### HasErrors

`func (o *TestResultsPost) HasErrors() bool`

HasErrors returns a boolean if a field has been set.

### SetErrorsNil

`func (o *TestResultsPost) SetErrorsNil(b bool)`

 SetErrorsNil sets the value for Errors to be an explicit nil

### UnsetErrors
`func (o *TestResultsPost) UnsetErrors()`

UnsetErrors ensures that no value is present for Errors, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


