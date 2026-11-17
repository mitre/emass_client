# HwBaselineReadOnlyFields

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**HardwareId** | Pointer to **NullableString** | [Read-Only] GUID identifying the specific hardware asset. Required for a PUT call. | [optional] 

## Methods

### NewHwBaselineReadOnlyFields

`func NewHwBaselineReadOnlyFields() *HwBaselineReadOnlyFields`

NewHwBaselineReadOnlyFields instantiates a new HwBaselineReadOnlyFields object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewHwBaselineReadOnlyFieldsWithDefaults

`func NewHwBaselineReadOnlyFieldsWithDefaults() *HwBaselineReadOnlyFields`

NewHwBaselineReadOnlyFieldsWithDefaults instantiates a new HwBaselineReadOnlyFields object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetHardwareId

`func (o *HwBaselineReadOnlyFields) GetHardwareId() string`

GetHardwareId returns the HardwareId field if non-nil, zero value otherwise.

### GetHardwareIdOk

`func (o *HwBaselineReadOnlyFields) GetHardwareIdOk() (*string, bool)`

GetHardwareIdOk returns a tuple with the HardwareId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHardwareId

`func (o *HwBaselineReadOnlyFields) SetHardwareId(v string)`

SetHardwareId sets HardwareId field to given value.

### HasHardwareId

`func (o *HwBaselineReadOnlyFields) HasHardwareId() bool`

HasHardwareId returns a boolean if a field has been set.

### SetHardwareIdNil

`func (o *HwBaselineReadOnlyFields) SetHardwareIdNil(b bool)`

 SetHardwareIdNil sets the value for HardwareId to be an explicit nil

### UnsetHardwareId
`func (o *HwBaselineReadOnlyFields) UnsetHardwareId()`

UnsetHardwareId ensures that no value is present for HardwareId, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


