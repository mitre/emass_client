# HwBaselineOptionalFields

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ComponentType** | Pointer to **NullableString** | [Optional] Type of the hardware asset. | [optional] 
**Nickname** | Pointer to **NullableString** | [Optional] Nickname of the hardware asset. | [optional] 
**AssetIpAddress** | Pointer to **NullableString** | [Optional] IP address of the hardware asset. | [optional] 
**PublicFacing** | Pointer to **NullableBool** | [Optional] Public facing is defined as any asset that is accessible from a commercial connection. | [optional] 
**VirtualAsset** | Pointer to **NullableBool** | [Optional] Determine if this is a virtual hardware asset. | [optional] 
**Manufacturer** | Pointer to **NullableString** | [Optional] Manufacturer of the hardware asset. Populated with \&quot;Virtual\&quot; by default if Virtual Asset is true, however this can be overridden. | [optional] 
**ModelNumber** | Pointer to **NullableString** | [Optional] Model number of the hardware asset. Populated with \&quot;Virtual\&quot; by default if Virtual Asset is true, however this can be overridden | [optional] 
**SerialNumber** | Pointer to **NullableString** | [Optional] Serial number of the hardware asset. Populated with \&quot;Virtual\&quot; by default if Virtual Asset is true, however this can be overridden. | [optional] 
**OsIosFwVersion** | Pointer to **NullableString** | [Optional] Operating System, IOS, or Firmware version of the hardware asset. | [optional] 
**MemorySizeType** | Pointer to **NullableString** | [Optional] Memory size / type of the hardware asset. | [optional] 
**Location** | Pointer to **NullableString** | [Optional] Location of the hardware asset. | [optional] 
**ApprovalStatus** | Pointer to **NullableString** | [Optional] Approval status of the hardware asset. | [optional] 
**CriticalAsset** | Pointer to **NullableBool** | [Optional] Indicates whether the asset is a critical information system asset. | [optional] 

## Methods

### NewHwBaselineOptionalFields

`func NewHwBaselineOptionalFields() *HwBaselineOptionalFields`

NewHwBaselineOptionalFields instantiates a new HwBaselineOptionalFields object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewHwBaselineOptionalFieldsWithDefaults

`func NewHwBaselineOptionalFieldsWithDefaults() *HwBaselineOptionalFields`

NewHwBaselineOptionalFieldsWithDefaults instantiates a new HwBaselineOptionalFields object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetComponentType

`func (o *HwBaselineOptionalFields) GetComponentType() string`

GetComponentType returns the ComponentType field if non-nil, zero value otherwise.

### GetComponentTypeOk

`func (o *HwBaselineOptionalFields) GetComponentTypeOk() (*string, bool)`

GetComponentTypeOk returns a tuple with the ComponentType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetComponentType

`func (o *HwBaselineOptionalFields) SetComponentType(v string)`

SetComponentType sets ComponentType field to given value.

### HasComponentType

`func (o *HwBaselineOptionalFields) HasComponentType() bool`

HasComponentType returns a boolean if a field has been set.

### SetComponentTypeNil

`func (o *HwBaselineOptionalFields) SetComponentTypeNil(b bool)`

 SetComponentTypeNil sets the value for ComponentType to be an explicit nil

### UnsetComponentType
`func (o *HwBaselineOptionalFields) UnsetComponentType()`

UnsetComponentType ensures that no value is present for ComponentType, not even an explicit nil
### GetNickname

`func (o *HwBaselineOptionalFields) GetNickname() string`

GetNickname returns the Nickname field if non-nil, zero value otherwise.

### GetNicknameOk

`func (o *HwBaselineOptionalFields) GetNicknameOk() (*string, bool)`

GetNicknameOk returns a tuple with the Nickname field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNickname

`func (o *HwBaselineOptionalFields) SetNickname(v string)`

SetNickname sets Nickname field to given value.

### HasNickname

`func (o *HwBaselineOptionalFields) HasNickname() bool`

HasNickname returns a boolean if a field has been set.

### SetNicknameNil

`func (o *HwBaselineOptionalFields) SetNicknameNil(b bool)`

 SetNicknameNil sets the value for Nickname to be an explicit nil

### UnsetNickname
`func (o *HwBaselineOptionalFields) UnsetNickname()`

UnsetNickname ensures that no value is present for Nickname, not even an explicit nil
### GetAssetIpAddress

`func (o *HwBaselineOptionalFields) GetAssetIpAddress() string`

GetAssetIpAddress returns the AssetIpAddress field if non-nil, zero value otherwise.

### GetAssetIpAddressOk

`func (o *HwBaselineOptionalFields) GetAssetIpAddressOk() (*string, bool)`

GetAssetIpAddressOk returns a tuple with the AssetIpAddress field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAssetIpAddress

`func (o *HwBaselineOptionalFields) SetAssetIpAddress(v string)`

SetAssetIpAddress sets AssetIpAddress field to given value.

### HasAssetIpAddress

`func (o *HwBaselineOptionalFields) HasAssetIpAddress() bool`

HasAssetIpAddress returns a boolean if a field has been set.

### SetAssetIpAddressNil

`func (o *HwBaselineOptionalFields) SetAssetIpAddressNil(b bool)`

 SetAssetIpAddressNil sets the value for AssetIpAddress to be an explicit nil

### UnsetAssetIpAddress
`func (o *HwBaselineOptionalFields) UnsetAssetIpAddress()`

UnsetAssetIpAddress ensures that no value is present for AssetIpAddress, not even an explicit nil
### GetPublicFacing

`func (o *HwBaselineOptionalFields) GetPublicFacing() bool`

GetPublicFacing returns the PublicFacing field if non-nil, zero value otherwise.

### GetPublicFacingOk

`func (o *HwBaselineOptionalFields) GetPublicFacingOk() (*bool, bool)`

GetPublicFacingOk returns a tuple with the PublicFacing field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPublicFacing

`func (o *HwBaselineOptionalFields) SetPublicFacing(v bool)`

SetPublicFacing sets PublicFacing field to given value.

### HasPublicFacing

`func (o *HwBaselineOptionalFields) HasPublicFacing() bool`

HasPublicFacing returns a boolean if a field has been set.

### SetPublicFacingNil

`func (o *HwBaselineOptionalFields) SetPublicFacingNil(b bool)`

 SetPublicFacingNil sets the value for PublicFacing to be an explicit nil

### UnsetPublicFacing
`func (o *HwBaselineOptionalFields) UnsetPublicFacing()`

UnsetPublicFacing ensures that no value is present for PublicFacing, not even an explicit nil
### GetVirtualAsset

`func (o *HwBaselineOptionalFields) GetVirtualAsset() bool`

GetVirtualAsset returns the VirtualAsset field if non-nil, zero value otherwise.

### GetVirtualAssetOk

`func (o *HwBaselineOptionalFields) GetVirtualAssetOk() (*bool, bool)`

GetVirtualAssetOk returns a tuple with the VirtualAsset field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVirtualAsset

`func (o *HwBaselineOptionalFields) SetVirtualAsset(v bool)`

SetVirtualAsset sets VirtualAsset field to given value.

### HasVirtualAsset

`func (o *HwBaselineOptionalFields) HasVirtualAsset() bool`

HasVirtualAsset returns a boolean if a field has been set.

### SetVirtualAssetNil

`func (o *HwBaselineOptionalFields) SetVirtualAssetNil(b bool)`

 SetVirtualAssetNil sets the value for VirtualAsset to be an explicit nil

### UnsetVirtualAsset
`func (o *HwBaselineOptionalFields) UnsetVirtualAsset()`

UnsetVirtualAsset ensures that no value is present for VirtualAsset, not even an explicit nil
### GetManufacturer

`func (o *HwBaselineOptionalFields) GetManufacturer() string`

GetManufacturer returns the Manufacturer field if non-nil, zero value otherwise.

### GetManufacturerOk

`func (o *HwBaselineOptionalFields) GetManufacturerOk() (*string, bool)`

GetManufacturerOk returns a tuple with the Manufacturer field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetManufacturer

`func (o *HwBaselineOptionalFields) SetManufacturer(v string)`

SetManufacturer sets Manufacturer field to given value.

### HasManufacturer

`func (o *HwBaselineOptionalFields) HasManufacturer() bool`

HasManufacturer returns a boolean if a field has been set.

### SetManufacturerNil

`func (o *HwBaselineOptionalFields) SetManufacturerNil(b bool)`

 SetManufacturerNil sets the value for Manufacturer to be an explicit nil

### UnsetManufacturer
`func (o *HwBaselineOptionalFields) UnsetManufacturer()`

UnsetManufacturer ensures that no value is present for Manufacturer, not even an explicit nil
### GetModelNumber

`func (o *HwBaselineOptionalFields) GetModelNumber() string`

GetModelNumber returns the ModelNumber field if non-nil, zero value otherwise.

### GetModelNumberOk

`func (o *HwBaselineOptionalFields) GetModelNumberOk() (*string, bool)`

GetModelNumberOk returns a tuple with the ModelNumber field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetModelNumber

`func (o *HwBaselineOptionalFields) SetModelNumber(v string)`

SetModelNumber sets ModelNumber field to given value.

### HasModelNumber

`func (o *HwBaselineOptionalFields) HasModelNumber() bool`

HasModelNumber returns a boolean if a field has been set.

### SetModelNumberNil

`func (o *HwBaselineOptionalFields) SetModelNumberNil(b bool)`

 SetModelNumberNil sets the value for ModelNumber to be an explicit nil

### UnsetModelNumber
`func (o *HwBaselineOptionalFields) UnsetModelNumber()`

UnsetModelNumber ensures that no value is present for ModelNumber, not even an explicit nil
### GetSerialNumber

`func (o *HwBaselineOptionalFields) GetSerialNumber() string`

GetSerialNumber returns the SerialNumber field if non-nil, zero value otherwise.

### GetSerialNumberOk

`func (o *HwBaselineOptionalFields) GetSerialNumberOk() (*string, bool)`

GetSerialNumberOk returns a tuple with the SerialNumber field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSerialNumber

`func (o *HwBaselineOptionalFields) SetSerialNumber(v string)`

SetSerialNumber sets SerialNumber field to given value.

### HasSerialNumber

`func (o *HwBaselineOptionalFields) HasSerialNumber() bool`

HasSerialNumber returns a boolean if a field has been set.

### SetSerialNumberNil

`func (o *HwBaselineOptionalFields) SetSerialNumberNil(b bool)`

 SetSerialNumberNil sets the value for SerialNumber to be an explicit nil

### UnsetSerialNumber
`func (o *HwBaselineOptionalFields) UnsetSerialNumber()`

UnsetSerialNumber ensures that no value is present for SerialNumber, not even an explicit nil
### GetOsIosFwVersion

`func (o *HwBaselineOptionalFields) GetOsIosFwVersion() string`

GetOsIosFwVersion returns the OsIosFwVersion field if non-nil, zero value otherwise.

### GetOsIosFwVersionOk

`func (o *HwBaselineOptionalFields) GetOsIosFwVersionOk() (*string, bool)`

GetOsIosFwVersionOk returns a tuple with the OsIosFwVersion field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOsIosFwVersion

`func (o *HwBaselineOptionalFields) SetOsIosFwVersion(v string)`

SetOsIosFwVersion sets OsIosFwVersion field to given value.

### HasOsIosFwVersion

`func (o *HwBaselineOptionalFields) HasOsIosFwVersion() bool`

HasOsIosFwVersion returns a boolean if a field has been set.

### SetOsIosFwVersionNil

`func (o *HwBaselineOptionalFields) SetOsIosFwVersionNil(b bool)`

 SetOsIosFwVersionNil sets the value for OsIosFwVersion to be an explicit nil

### UnsetOsIosFwVersion
`func (o *HwBaselineOptionalFields) UnsetOsIosFwVersion()`

UnsetOsIosFwVersion ensures that no value is present for OsIosFwVersion, not even an explicit nil
### GetMemorySizeType

`func (o *HwBaselineOptionalFields) GetMemorySizeType() string`

GetMemorySizeType returns the MemorySizeType field if non-nil, zero value otherwise.

### GetMemorySizeTypeOk

`func (o *HwBaselineOptionalFields) GetMemorySizeTypeOk() (*string, bool)`

GetMemorySizeTypeOk returns a tuple with the MemorySizeType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMemorySizeType

`func (o *HwBaselineOptionalFields) SetMemorySizeType(v string)`

SetMemorySizeType sets MemorySizeType field to given value.

### HasMemorySizeType

`func (o *HwBaselineOptionalFields) HasMemorySizeType() bool`

HasMemorySizeType returns a boolean if a field has been set.

### SetMemorySizeTypeNil

`func (o *HwBaselineOptionalFields) SetMemorySizeTypeNil(b bool)`

 SetMemorySizeTypeNil sets the value for MemorySizeType to be an explicit nil

### UnsetMemorySizeType
`func (o *HwBaselineOptionalFields) UnsetMemorySizeType()`

UnsetMemorySizeType ensures that no value is present for MemorySizeType, not even an explicit nil
### GetLocation

`func (o *HwBaselineOptionalFields) GetLocation() string`

GetLocation returns the Location field if non-nil, zero value otherwise.

### GetLocationOk

`func (o *HwBaselineOptionalFields) GetLocationOk() (*string, bool)`

GetLocationOk returns a tuple with the Location field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLocation

`func (o *HwBaselineOptionalFields) SetLocation(v string)`

SetLocation sets Location field to given value.

### HasLocation

`func (o *HwBaselineOptionalFields) HasLocation() bool`

HasLocation returns a boolean if a field has been set.

### SetLocationNil

`func (o *HwBaselineOptionalFields) SetLocationNil(b bool)`

 SetLocationNil sets the value for Location to be an explicit nil

### UnsetLocation
`func (o *HwBaselineOptionalFields) UnsetLocation()`

UnsetLocation ensures that no value is present for Location, not even an explicit nil
### GetApprovalStatus

`func (o *HwBaselineOptionalFields) GetApprovalStatus() string`

GetApprovalStatus returns the ApprovalStatus field if non-nil, zero value otherwise.

### GetApprovalStatusOk

`func (o *HwBaselineOptionalFields) GetApprovalStatusOk() (*string, bool)`

GetApprovalStatusOk returns a tuple with the ApprovalStatus field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetApprovalStatus

`func (o *HwBaselineOptionalFields) SetApprovalStatus(v string)`

SetApprovalStatus sets ApprovalStatus field to given value.

### HasApprovalStatus

`func (o *HwBaselineOptionalFields) HasApprovalStatus() bool`

HasApprovalStatus returns a boolean if a field has been set.

### SetApprovalStatusNil

`func (o *HwBaselineOptionalFields) SetApprovalStatusNil(b bool)`

 SetApprovalStatusNil sets the value for ApprovalStatus to be an explicit nil

### UnsetApprovalStatus
`func (o *HwBaselineOptionalFields) UnsetApprovalStatus()`

UnsetApprovalStatus ensures that no value is present for ApprovalStatus, not even an explicit nil
### GetCriticalAsset

`func (o *HwBaselineOptionalFields) GetCriticalAsset() bool`

GetCriticalAsset returns the CriticalAsset field if non-nil, zero value otherwise.

### GetCriticalAssetOk

`func (o *HwBaselineOptionalFields) GetCriticalAssetOk() (*bool, bool)`

GetCriticalAssetOk returns a tuple with the CriticalAsset field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCriticalAsset

`func (o *HwBaselineOptionalFields) SetCriticalAsset(v bool)`

SetCriticalAsset sets CriticalAsset field to given value.

### HasCriticalAsset

`func (o *HwBaselineOptionalFields) HasCriticalAsset() bool`

HasCriticalAsset returns a boolean if a field has been set.

### SetCriticalAssetNil

`func (o *HwBaselineOptionalFields) SetCriticalAssetNil(b bool)`

 SetCriticalAssetNil sets the value for CriticalAsset to be an explicit nil

### UnsetCriticalAsset
`func (o *HwBaselineOptionalFields) UnsetCriticalAsset()`

UnsetCriticalAsset ensures that no value is present for CriticalAsset, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


