# HwBaselineResponseDeleteDataInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**SystemId** | Pointer to **int64** |  | [optional] 
**HardwareId** | Pointer to **string** |  | [optional] 
**Success** | Pointer to **bool** |  | [optional] 
**Errors** | Pointer to **[]interface{}** |  | [optional] 

## Methods

### NewHwBaselineResponseDeleteDataInner

`func NewHwBaselineResponseDeleteDataInner() *HwBaselineResponseDeleteDataInner`

NewHwBaselineResponseDeleteDataInner instantiates a new HwBaselineResponseDeleteDataInner object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewHwBaselineResponseDeleteDataInnerWithDefaults

`func NewHwBaselineResponseDeleteDataInnerWithDefaults() *HwBaselineResponseDeleteDataInner`

NewHwBaselineResponseDeleteDataInnerWithDefaults instantiates a new HwBaselineResponseDeleteDataInner object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetSystemId

`func (o *HwBaselineResponseDeleteDataInner) GetSystemId() int64`

GetSystemId returns the SystemId field if non-nil, zero value otherwise.

### GetSystemIdOk

`func (o *HwBaselineResponseDeleteDataInner) GetSystemIdOk() (*int64, bool)`

GetSystemIdOk returns a tuple with the SystemId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSystemId

`func (o *HwBaselineResponseDeleteDataInner) SetSystemId(v int64)`

SetSystemId sets SystemId field to given value.

### HasSystemId

`func (o *HwBaselineResponseDeleteDataInner) HasSystemId() bool`

HasSystemId returns a boolean if a field has been set.

### GetHardwareId

`func (o *HwBaselineResponseDeleteDataInner) GetHardwareId() string`

GetHardwareId returns the HardwareId field if non-nil, zero value otherwise.

### GetHardwareIdOk

`func (o *HwBaselineResponseDeleteDataInner) GetHardwareIdOk() (*string, bool)`

GetHardwareIdOk returns a tuple with the HardwareId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHardwareId

`func (o *HwBaselineResponseDeleteDataInner) SetHardwareId(v string)`

SetHardwareId sets HardwareId field to given value.

### HasHardwareId

`func (o *HwBaselineResponseDeleteDataInner) HasHardwareId() bool`

HasHardwareId returns a boolean if a field has been set.

### GetSuccess

`func (o *HwBaselineResponseDeleteDataInner) GetSuccess() bool`

GetSuccess returns the Success field if non-nil, zero value otherwise.

### GetSuccessOk

`func (o *HwBaselineResponseDeleteDataInner) GetSuccessOk() (*bool, bool)`

GetSuccessOk returns a tuple with the Success field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSuccess

`func (o *HwBaselineResponseDeleteDataInner) SetSuccess(v bool)`

SetSuccess sets Success field to given value.

### HasSuccess

`func (o *HwBaselineResponseDeleteDataInner) HasSuccess() bool`

HasSuccess returns a boolean if a field has been set.

### GetErrors

`func (o *HwBaselineResponseDeleteDataInner) GetErrors() []interface{}`

GetErrors returns the Errors field if non-nil, zero value otherwise.

### GetErrorsOk

`func (o *HwBaselineResponseDeleteDataInner) GetErrorsOk() (*[]interface{}, bool)`

GetErrorsOk returns a tuple with the Errors field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetErrors

`func (o *HwBaselineResponseDeleteDataInner) SetErrors(v []interface{})`

SetErrors sets Errors field to given value.

### HasErrors

`func (o *HwBaselineResponseDeleteDataInner) HasErrors() bool`

HasErrors returns a boolean if a field has been set.

### SetErrorsNil

`func (o *HwBaselineResponseDeleteDataInner) SetErrorsNil(b bool)`

 SetErrorsNil sets the value for Errors to be an explicit nil

### UnsetErrors
`func (o *HwBaselineResponseDeleteDataInner) UnsetErrors()`

UnsetErrors ensures that no value is present for Errors, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


