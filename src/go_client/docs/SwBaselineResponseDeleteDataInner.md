# SwBaselineResponseDeleteDataInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**SystemId** | Pointer to **int64** |  | [optional] 
**SoftwareId** | Pointer to **string** |  | [optional] 
**Success** | Pointer to **bool** |  | [optional] 
**Errors** | Pointer to **[]interface{}** |  | [optional] 

## Methods

### NewSwBaselineResponseDeleteDataInner

`func NewSwBaselineResponseDeleteDataInner() *SwBaselineResponseDeleteDataInner`

NewSwBaselineResponseDeleteDataInner instantiates a new SwBaselineResponseDeleteDataInner object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSwBaselineResponseDeleteDataInnerWithDefaults

`func NewSwBaselineResponseDeleteDataInnerWithDefaults() *SwBaselineResponseDeleteDataInner`

NewSwBaselineResponseDeleteDataInnerWithDefaults instantiates a new SwBaselineResponseDeleteDataInner object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetSystemId

`func (o *SwBaselineResponseDeleteDataInner) GetSystemId() int64`

GetSystemId returns the SystemId field if non-nil, zero value otherwise.

### GetSystemIdOk

`func (o *SwBaselineResponseDeleteDataInner) GetSystemIdOk() (*int64, bool)`

GetSystemIdOk returns a tuple with the SystemId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSystemId

`func (o *SwBaselineResponseDeleteDataInner) SetSystemId(v int64)`

SetSystemId sets SystemId field to given value.

### HasSystemId

`func (o *SwBaselineResponseDeleteDataInner) HasSystemId() bool`

HasSystemId returns a boolean if a field has been set.

### GetSoftwareId

`func (o *SwBaselineResponseDeleteDataInner) GetSoftwareId() string`

GetSoftwareId returns the SoftwareId field if non-nil, zero value otherwise.

### GetSoftwareIdOk

`func (o *SwBaselineResponseDeleteDataInner) GetSoftwareIdOk() (*string, bool)`

GetSoftwareIdOk returns a tuple with the SoftwareId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSoftwareId

`func (o *SwBaselineResponseDeleteDataInner) SetSoftwareId(v string)`

SetSoftwareId sets SoftwareId field to given value.

### HasSoftwareId

`func (o *SwBaselineResponseDeleteDataInner) HasSoftwareId() bool`

HasSoftwareId returns a boolean if a field has been set.

### GetSuccess

`func (o *SwBaselineResponseDeleteDataInner) GetSuccess() bool`

GetSuccess returns the Success field if non-nil, zero value otherwise.

### GetSuccessOk

`func (o *SwBaselineResponseDeleteDataInner) GetSuccessOk() (*bool, bool)`

GetSuccessOk returns a tuple with the Success field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSuccess

`func (o *SwBaselineResponseDeleteDataInner) SetSuccess(v bool)`

SetSuccess sets Success field to given value.

### HasSuccess

`func (o *SwBaselineResponseDeleteDataInner) HasSuccess() bool`

HasSuccess returns a boolean if a field has been set.

### GetErrors

`func (o *SwBaselineResponseDeleteDataInner) GetErrors() []interface{}`

GetErrors returns the Errors field if non-nil, zero value otherwise.

### GetErrorsOk

`func (o *SwBaselineResponseDeleteDataInner) GetErrorsOk() (*[]interface{}, bool)`

GetErrorsOk returns a tuple with the Errors field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetErrors

`func (o *SwBaselineResponseDeleteDataInner) SetErrors(v []interface{})`

SetErrors sets Errors field to given value.

### HasErrors

`func (o *SwBaselineResponseDeleteDataInner) HasErrors() bool`

HasErrors returns a boolean if a field has been set.

### SetErrorsNil

`func (o *SwBaselineResponseDeleteDataInner) SetErrorsNil(b bool)`

 SetErrorsNil sets the value for Errors to be an explicit nil

### UnsetErrors
`func (o *SwBaselineResponseDeleteDataInner) UnsetErrors()`

UnsetErrors ensures that no value is present for Errors, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


