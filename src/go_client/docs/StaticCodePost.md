# StaticCodePost

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ApplicationName** | Pointer to **string** | [Required] Name of the software application that was assessed. | [optional] 
**Version** | Pointer to **string** | [Required] The version of the application. | [optional] 
**Success** | Pointer to **bool** |  | [optional] 
**SystemId** | Pointer to **int64** |  | [optional] 
**Errors** | Pointer to **[]interface{}** |  | [optional] 

## Methods

### NewStaticCodePost

`func NewStaticCodePost() *StaticCodePost`

NewStaticCodePost instantiates a new StaticCodePost object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewStaticCodePostWithDefaults

`func NewStaticCodePostWithDefaults() *StaticCodePost`

NewStaticCodePostWithDefaults instantiates a new StaticCodePost object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetApplicationName

`func (o *StaticCodePost) GetApplicationName() string`

GetApplicationName returns the ApplicationName field if non-nil, zero value otherwise.

### GetApplicationNameOk

`func (o *StaticCodePost) GetApplicationNameOk() (*string, bool)`

GetApplicationNameOk returns a tuple with the ApplicationName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetApplicationName

`func (o *StaticCodePost) SetApplicationName(v string)`

SetApplicationName sets ApplicationName field to given value.

### HasApplicationName

`func (o *StaticCodePost) HasApplicationName() bool`

HasApplicationName returns a boolean if a field has been set.

### GetVersion

`func (o *StaticCodePost) GetVersion() string`

GetVersion returns the Version field if non-nil, zero value otherwise.

### GetVersionOk

`func (o *StaticCodePost) GetVersionOk() (*string, bool)`

GetVersionOk returns a tuple with the Version field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVersion

`func (o *StaticCodePost) SetVersion(v string)`

SetVersion sets Version field to given value.

### HasVersion

`func (o *StaticCodePost) HasVersion() bool`

HasVersion returns a boolean if a field has been set.

### GetSuccess

`func (o *StaticCodePost) GetSuccess() bool`

GetSuccess returns the Success field if non-nil, zero value otherwise.

### GetSuccessOk

`func (o *StaticCodePost) GetSuccessOk() (*bool, bool)`

GetSuccessOk returns a tuple with the Success field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSuccess

`func (o *StaticCodePost) SetSuccess(v bool)`

SetSuccess sets Success field to given value.

### HasSuccess

`func (o *StaticCodePost) HasSuccess() bool`

HasSuccess returns a boolean if a field has been set.

### GetSystemId

`func (o *StaticCodePost) GetSystemId() int64`

GetSystemId returns the SystemId field if non-nil, zero value otherwise.

### GetSystemIdOk

`func (o *StaticCodePost) GetSystemIdOk() (*int64, bool)`

GetSystemIdOk returns a tuple with the SystemId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSystemId

`func (o *StaticCodePost) SetSystemId(v int64)`

SetSystemId sets SystemId field to given value.

### HasSystemId

`func (o *StaticCodePost) HasSystemId() bool`

HasSystemId returns a boolean if a field has been set.

### GetErrors

`func (o *StaticCodePost) GetErrors() []interface{}`

GetErrors returns the Errors field if non-nil, zero value otherwise.

### GetErrorsOk

`func (o *StaticCodePost) GetErrorsOk() (*[]interface{}, bool)`

GetErrorsOk returns a tuple with the Errors field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetErrors

`func (o *StaticCodePost) SetErrors(v []interface{})`

SetErrors sets Errors field to given value.

### HasErrors

`func (o *StaticCodePost) HasErrors() bool`

HasErrors returns a boolean if a field has been set.

### SetErrorsNil

`func (o *StaticCodePost) SetErrorsNil(b bool)`

 SetErrorsNil sets the value for Errors to be an explicit nil

### UnsetErrors
`func (o *StaticCodePost) UnsetErrors()`

UnsetErrors ensures that no value is present for Errors, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


