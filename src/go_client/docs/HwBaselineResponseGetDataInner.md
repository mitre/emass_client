# HwBaselineResponseGetDataInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**SystemId** | Pointer to **int64** | [Required] Unique eMASS system identifier. | [optional] 
**HardwareId** | Pointer to **NullableString** | [Read-Only] GUID identifying the specific hardware asset. Required for a PUT call. | [optional] 
**AssetName** | Pointer to **string** | [Required] Name of the hardware asset. | [optional] 
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
**PublicFacingFqdn** | Pointer to **NullableString** | [Conditional] Public facing FQDN. Only applicable if Public Facing is set to true. | [optional] 
**PublicFacingIpAddress** | Pointer to **NullableString** | [Conditional] Public facing IP address. Only applicable if Public Facing is set to true. | [optional] 
**PublicFacingUrls** | Pointer to **NullableString** | [Conditional] Public facing URLs. Only applicable if Public Facing is set to true. | [optional] 

## Methods

### NewHwBaselineResponseGetDataInner

`func NewHwBaselineResponseGetDataInner() *HwBaselineResponseGetDataInner`

NewHwBaselineResponseGetDataInner instantiates a new HwBaselineResponseGetDataInner object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewHwBaselineResponseGetDataInnerWithDefaults

`func NewHwBaselineResponseGetDataInnerWithDefaults() *HwBaselineResponseGetDataInner`

NewHwBaselineResponseGetDataInnerWithDefaults instantiates a new HwBaselineResponseGetDataInner object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetSystemId

`func (o *HwBaselineResponseGetDataInner) GetSystemId() int64`

GetSystemId returns the SystemId field if non-nil, zero value otherwise.

### GetSystemIdOk

`func (o *HwBaselineResponseGetDataInner) GetSystemIdOk() (*int64, bool)`

GetSystemIdOk returns a tuple with the SystemId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSystemId

`func (o *HwBaselineResponseGetDataInner) SetSystemId(v int64)`

SetSystemId sets SystemId field to given value.

### HasSystemId

`func (o *HwBaselineResponseGetDataInner) HasSystemId() bool`

HasSystemId returns a boolean if a field has been set.

### GetHardwareId

`func (o *HwBaselineResponseGetDataInner) GetHardwareId() string`

GetHardwareId returns the HardwareId field if non-nil, zero value otherwise.

### GetHardwareIdOk

`func (o *HwBaselineResponseGetDataInner) GetHardwareIdOk() (*string, bool)`

GetHardwareIdOk returns a tuple with the HardwareId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHardwareId

`func (o *HwBaselineResponseGetDataInner) SetHardwareId(v string)`

SetHardwareId sets HardwareId field to given value.

### HasHardwareId

`func (o *HwBaselineResponseGetDataInner) HasHardwareId() bool`

HasHardwareId returns a boolean if a field has been set.

### SetHardwareIdNil

`func (o *HwBaselineResponseGetDataInner) SetHardwareIdNil(b bool)`

 SetHardwareIdNil sets the value for HardwareId to be an explicit nil

### UnsetHardwareId
`func (o *HwBaselineResponseGetDataInner) UnsetHardwareId()`

UnsetHardwareId ensures that no value is present for HardwareId, not even an explicit nil
### GetAssetName

`func (o *HwBaselineResponseGetDataInner) GetAssetName() string`

GetAssetName returns the AssetName field if non-nil, zero value otherwise.

### GetAssetNameOk

`func (o *HwBaselineResponseGetDataInner) GetAssetNameOk() (*string, bool)`

GetAssetNameOk returns a tuple with the AssetName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAssetName

`func (o *HwBaselineResponseGetDataInner) SetAssetName(v string)`

SetAssetName sets AssetName field to given value.

### HasAssetName

`func (o *HwBaselineResponseGetDataInner) HasAssetName() bool`

HasAssetName returns a boolean if a field has been set.

### GetComponentType

`func (o *HwBaselineResponseGetDataInner) GetComponentType() string`

GetComponentType returns the ComponentType field if non-nil, zero value otherwise.

### GetComponentTypeOk

`func (o *HwBaselineResponseGetDataInner) GetComponentTypeOk() (*string, bool)`

GetComponentTypeOk returns a tuple with the ComponentType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetComponentType

`func (o *HwBaselineResponseGetDataInner) SetComponentType(v string)`

SetComponentType sets ComponentType field to given value.

### HasComponentType

`func (o *HwBaselineResponseGetDataInner) HasComponentType() bool`

HasComponentType returns a boolean if a field has been set.

### SetComponentTypeNil

`func (o *HwBaselineResponseGetDataInner) SetComponentTypeNil(b bool)`

 SetComponentTypeNil sets the value for ComponentType to be an explicit nil

### UnsetComponentType
`func (o *HwBaselineResponseGetDataInner) UnsetComponentType()`

UnsetComponentType ensures that no value is present for ComponentType, not even an explicit nil
### GetNickname

`func (o *HwBaselineResponseGetDataInner) GetNickname() string`

GetNickname returns the Nickname field if non-nil, zero value otherwise.

### GetNicknameOk

`func (o *HwBaselineResponseGetDataInner) GetNicknameOk() (*string, bool)`

GetNicknameOk returns a tuple with the Nickname field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNickname

`func (o *HwBaselineResponseGetDataInner) SetNickname(v string)`

SetNickname sets Nickname field to given value.

### HasNickname

`func (o *HwBaselineResponseGetDataInner) HasNickname() bool`

HasNickname returns a boolean if a field has been set.

### SetNicknameNil

`func (o *HwBaselineResponseGetDataInner) SetNicknameNil(b bool)`

 SetNicknameNil sets the value for Nickname to be an explicit nil

### UnsetNickname
`func (o *HwBaselineResponseGetDataInner) UnsetNickname()`

UnsetNickname ensures that no value is present for Nickname, not even an explicit nil
### GetAssetIpAddress

`func (o *HwBaselineResponseGetDataInner) GetAssetIpAddress() string`

GetAssetIpAddress returns the AssetIpAddress field if non-nil, zero value otherwise.

### GetAssetIpAddressOk

`func (o *HwBaselineResponseGetDataInner) GetAssetIpAddressOk() (*string, bool)`

GetAssetIpAddressOk returns a tuple with the AssetIpAddress field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAssetIpAddress

`func (o *HwBaselineResponseGetDataInner) SetAssetIpAddress(v string)`

SetAssetIpAddress sets AssetIpAddress field to given value.

### HasAssetIpAddress

`func (o *HwBaselineResponseGetDataInner) HasAssetIpAddress() bool`

HasAssetIpAddress returns a boolean if a field has been set.

### SetAssetIpAddressNil

`func (o *HwBaselineResponseGetDataInner) SetAssetIpAddressNil(b bool)`

 SetAssetIpAddressNil sets the value for AssetIpAddress to be an explicit nil

### UnsetAssetIpAddress
`func (o *HwBaselineResponseGetDataInner) UnsetAssetIpAddress()`

UnsetAssetIpAddress ensures that no value is present for AssetIpAddress, not even an explicit nil
### GetPublicFacing

`func (o *HwBaselineResponseGetDataInner) GetPublicFacing() bool`

GetPublicFacing returns the PublicFacing field if non-nil, zero value otherwise.

### GetPublicFacingOk

`func (o *HwBaselineResponseGetDataInner) GetPublicFacingOk() (*bool, bool)`

GetPublicFacingOk returns a tuple with the PublicFacing field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPublicFacing

`func (o *HwBaselineResponseGetDataInner) SetPublicFacing(v bool)`

SetPublicFacing sets PublicFacing field to given value.

### HasPublicFacing

`func (o *HwBaselineResponseGetDataInner) HasPublicFacing() bool`

HasPublicFacing returns a boolean if a field has been set.

### SetPublicFacingNil

`func (o *HwBaselineResponseGetDataInner) SetPublicFacingNil(b bool)`

 SetPublicFacingNil sets the value for PublicFacing to be an explicit nil

### UnsetPublicFacing
`func (o *HwBaselineResponseGetDataInner) UnsetPublicFacing()`

UnsetPublicFacing ensures that no value is present for PublicFacing, not even an explicit nil
### GetVirtualAsset

`func (o *HwBaselineResponseGetDataInner) GetVirtualAsset() bool`

GetVirtualAsset returns the VirtualAsset field if non-nil, zero value otherwise.

### GetVirtualAssetOk

`func (o *HwBaselineResponseGetDataInner) GetVirtualAssetOk() (*bool, bool)`

GetVirtualAssetOk returns a tuple with the VirtualAsset field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVirtualAsset

`func (o *HwBaselineResponseGetDataInner) SetVirtualAsset(v bool)`

SetVirtualAsset sets VirtualAsset field to given value.

### HasVirtualAsset

`func (o *HwBaselineResponseGetDataInner) HasVirtualAsset() bool`

HasVirtualAsset returns a boolean if a field has been set.

### SetVirtualAssetNil

`func (o *HwBaselineResponseGetDataInner) SetVirtualAssetNil(b bool)`

 SetVirtualAssetNil sets the value for VirtualAsset to be an explicit nil

### UnsetVirtualAsset
`func (o *HwBaselineResponseGetDataInner) UnsetVirtualAsset()`

UnsetVirtualAsset ensures that no value is present for VirtualAsset, not even an explicit nil
### GetManufacturer

`func (o *HwBaselineResponseGetDataInner) GetManufacturer() string`

GetManufacturer returns the Manufacturer field if non-nil, zero value otherwise.

### GetManufacturerOk

`func (o *HwBaselineResponseGetDataInner) GetManufacturerOk() (*string, bool)`

GetManufacturerOk returns a tuple with the Manufacturer field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetManufacturer

`func (o *HwBaselineResponseGetDataInner) SetManufacturer(v string)`

SetManufacturer sets Manufacturer field to given value.

### HasManufacturer

`func (o *HwBaselineResponseGetDataInner) HasManufacturer() bool`

HasManufacturer returns a boolean if a field has been set.

### SetManufacturerNil

`func (o *HwBaselineResponseGetDataInner) SetManufacturerNil(b bool)`

 SetManufacturerNil sets the value for Manufacturer to be an explicit nil

### UnsetManufacturer
`func (o *HwBaselineResponseGetDataInner) UnsetManufacturer()`

UnsetManufacturer ensures that no value is present for Manufacturer, not even an explicit nil
### GetModelNumber

`func (o *HwBaselineResponseGetDataInner) GetModelNumber() string`

GetModelNumber returns the ModelNumber field if non-nil, zero value otherwise.

### GetModelNumberOk

`func (o *HwBaselineResponseGetDataInner) GetModelNumberOk() (*string, bool)`

GetModelNumberOk returns a tuple with the ModelNumber field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetModelNumber

`func (o *HwBaselineResponseGetDataInner) SetModelNumber(v string)`

SetModelNumber sets ModelNumber field to given value.

### HasModelNumber

`func (o *HwBaselineResponseGetDataInner) HasModelNumber() bool`

HasModelNumber returns a boolean if a field has been set.

### SetModelNumberNil

`func (o *HwBaselineResponseGetDataInner) SetModelNumberNil(b bool)`

 SetModelNumberNil sets the value for ModelNumber to be an explicit nil

### UnsetModelNumber
`func (o *HwBaselineResponseGetDataInner) UnsetModelNumber()`

UnsetModelNumber ensures that no value is present for ModelNumber, not even an explicit nil
### GetSerialNumber

`func (o *HwBaselineResponseGetDataInner) GetSerialNumber() string`

GetSerialNumber returns the SerialNumber field if non-nil, zero value otherwise.

### GetSerialNumberOk

`func (o *HwBaselineResponseGetDataInner) GetSerialNumberOk() (*string, bool)`

GetSerialNumberOk returns a tuple with the SerialNumber field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSerialNumber

`func (o *HwBaselineResponseGetDataInner) SetSerialNumber(v string)`

SetSerialNumber sets SerialNumber field to given value.

### HasSerialNumber

`func (o *HwBaselineResponseGetDataInner) HasSerialNumber() bool`

HasSerialNumber returns a boolean if a field has been set.

### SetSerialNumberNil

`func (o *HwBaselineResponseGetDataInner) SetSerialNumberNil(b bool)`

 SetSerialNumberNil sets the value for SerialNumber to be an explicit nil

### UnsetSerialNumber
`func (o *HwBaselineResponseGetDataInner) UnsetSerialNumber()`

UnsetSerialNumber ensures that no value is present for SerialNumber, not even an explicit nil
### GetOsIosFwVersion

`func (o *HwBaselineResponseGetDataInner) GetOsIosFwVersion() string`

GetOsIosFwVersion returns the OsIosFwVersion field if non-nil, zero value otherwise.

### GetOsIosFwVersionOk

`func (o *HwBaselineResponseGetDataInner) GetOsIosFwVersionOk() (*string, bool)`

GetOsIosFwVersionOk returns a tuple with the OsIosFwVersion field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOsIosFwVersion

`func (o *HwBaselineResponseGetDataInner) SetOsIosFwVersion(v string)`

SetOsIosFwVersion sets OsIosFwVersion field to given value.

### HasOsIosFwVersion

`func (o *HwBaselineResponseGetDataInner) HasOsIosFwVersion() bool`

HasOsIosFwVersion returns a boolean if a field has been set.

### SetOsIosFwVersionNil

`func (o *HwBaselineResponseGetDataInner) SetOsIosFwVersionNil(b bool)`

 SetOsIosFwVersionNil sets the value for OsIosFwVersion to be an explicit nil

### UnsetOsIosFwVersion
`func (o *HwBaselineResponseGetDataInner) UnsetOsIosFwVersion()`

UnsetOsIosFwVersion ensures that no value is present for OsIosFwVersion, not even an explicit nil
### GetMemorySizeType

`func (o *HwBaselineResponseGetDataInner) GetMemorySizeType() string`

GetMemorySizeType returns the MemorySizeType field if non-nil, zero value otherwise.

### GetMemorySizeTypeOk

`func (o *HwBaselineResponseGetDataInner) GetMemorySizeTypeOk() (*string, bool)`

GetMemorySizeTypeOk returns a tuple with the MemorySizeType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMemorySizeType

`func (o *HwBaselineResponseGetDataInner) SetMemorySizeType(v string)`

SetMemorySizeType sets MemorySizeType field to given value.

### HasMemorySizeType

`func (o *HwBaselineResponseGetDataInner) HasMemorySizeType() bool`

HasMemorySizeType returns a boolean if a field has been set.

### SetMemorySizeTypeNil

`func (o *HwBaselineResponseGetDataInner) SetMemorySizeTypeNil(b bool)`

 SetMemorySizeTypeNil sets the value for MemorySizeType to be an explicit nil

### UnsetMemorySizeType
`func (o *HwBaselineResponseGetDataInner) UnsetMemorySizeType()`

UnsetMemorySizeType ensures that no value is present for MemorySizeType, not even an explicit nil
### GetLocation

`func (o *HwBaselineResponseGetDataInner) GetLocation() string`

GetLocation returns the Location field if non-nil, zero value otherwise.

### GetLocationOk

`func (o *HwBaselineResponseGetDataInner) GetLocationOk() (*string, bool)`

GetLocationOk returns a tuple with the Location field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLocation

`func (o *HwBaselineResponseGetDataInner) SetLocation(v string)`

SetLocation sets Location field to given value.

### HasLocation

`func (o *HwBaselineResponseGetDataInner) HasLocation() bool`

HasLocation returns a boolean if a field has been set.

### SetLocationNil

`func (o *HwBaselineResponseGetDataInner) SetLocationNil(b bool)`

 SetLocationNil sets the value for Location to be an explicit nil

### UnsetLocation
`func (o *HwBaselineResponseGetDataInner) UnsetLocation()`

UnsetLocation ensures that no value is present for Location, not even an explicit nil
### GetApprovalStatus

`func (o *HwBaselineResponseGetDataInner) GetApprovalStatus() string`

GetApprovalStatus returns the ApprovalStatus field if non-nil, zero value otherwise.

### GetApprovalStatusOk

`func (o *HwBaselineResponseGetDataInner) GetApprovalStatusOk() (*string, bool)`

GetApprovalStatusOk returns a tuple with the ApprovalStatus field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetApprovalStatus

`func (o *HwBaselineResponseGetDataInner) SetApprovalStatus(v string)`

SetApprovalStatus sets ApprovalStatus field to given value.

### HasApprovalStatus

`func (o *HwBaselineResponseGetDataInner) HasApprovalStatus() bool`

HasApprovalStatus returns a boolean if a field has been set.

### SetApprovalStatusNil

`func (o *HwBaselineResponseGetDataInner) SetApprovalStatusNil(b bool)`

 SetApprovalStatusNil sets the value for ApprovalStatus to be an explicit nil

### UnsetApprovalStatus
`func (o *HwBaselineResponseGetDataInner) UnsetApprovalStatus()`

UnsetApprovalStatus ensures that no value is present for ApprovalStatus, not even an explicit nil
### GetCriticalAsset

`func (o *HwBaselineResponseGetDataInner) GetCriticalAsset() bool`

GetCriticalAsset returns the CriticalAsset field if non-nil, zero value otherwise.

### GetCriticalAssetOk

`func (o *HwBaselineResponseGetDataInner) GetCriticalAssetOk() (*bool, bool)`

GetCriticalAssetOk returns a tuple with the CriticalAsset field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCriticalAsset

`func (o *HwBaselineResponseGetDataInner) SetCriticalAsset(v bool)`

SetCriticalAsset sets CriticalAsset field to given value.

### HasCriticalAsset

`func (o *HwBaselineResponseGetDataInner) HasCriticalAsset() bool`

HasCriticalAsset returns a boolean if a field has been set.

### SetCriticalAssetNil

`func (o *HwBaselineResponseGetDataInner) SetCriticalAssetNil(b bool)`

 SetCriticalAssetNil sets the value for CriticalAsset to be an explicit nil

### UnsetCriticalAsset
`func (o *HwBaselineResponseGetDataInner) UnsetCriticalAsset()`

UnsetCriticalAsset ensures that no value is present for CriticalAsset, not even an explicit nil
### GetPublicFacingFqdn

`func (o *HwBaselineResponseGetDataInner) GetPublicFacingFqdn() string`

GetPublicFacingFqdn returns the PublicFacingFqdn field if non-nil, zero value otherwise.

### GetPublicFacingFqdnOk

`func (o *HwBaselineResponseGetDataInner) GetPublicFacingFqdnOk() (*string, bool)`

GetPublicFacingFqdnOk returns a tuple with the PublicFacingFqdn field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPublicFacingFqdn

`func (o *HwBaselineResponseGetDataInner) SetPublicFacingFqdn(v string)`

SetPublicFacingFqdn sets PublicFacingFqdn field to given value.

### HasPublicFacingFqdn

`func (o *HwBaselineResponseGetDataInner) HasPublicFacingFqdn() bool`

HasPublicFacingFqdn returns a boolean if a field has been set.

### SetPublicFacingFqdnNil

`func (o *HwBaselineResponseGetDataInner) SetPublicFacingFqdnNil(b bool)`

 SetPublicFacingFqdnNil sets the value for PublicFacingFqdn to be an explicit nil

### UnsetPublicFacingFqdn
`func (o *HwBaselineResponseGetDataInner) UnsetPublicFacingFqdn()`

UnsetPublicFacingFqdn ensures that no value is present for PublicFacingFqdn, not even an explicit nil
### GetPublicFacingIpAddress

`func (o *HwBaselineResponseGetDataInner) GetPublicFacingIpAddress() string`

GetPublicFacingIpAddress returns the PublicFacingIpAddress field if non-nil, zero value otherwise.

### GetPublicFacingIpAddressOk

`func (o *HwBaselineResponseGetDataInner) GetPublicFacingIpAddressOk() (*string, bool)`

GetPublicFacingIpAddressOk returns a tuple with the PublicFacingIpAddress field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPublicFacingIpAddress

`func (o *HwBaselineResponseGetDataInner) SetPublicFacingIpAddress(v string)`

SetPublicFacingIpAddress sets PublicFacingIpAddress field to given value.

### HasPublicFacingIpAddress

`func (o *HwBaselineResponseGetDataInner) HasPublicFacingIpAddress() bool`

HasPublicFacingIpAddress returns a boolean if a field has been set.

### SetPublicFacingIpAddressNil

`func (o *HwBaselineResponseGetDataInner) SetPublicFacingIpAddressNil(b bool)`

 SetPublicFacingIpAddressNil sets the value for PublicFacingIpAddress to be an explicit nil

### UnsetPublicFacingIpAddress
`func (o *HwBaselineResponseGetDataInner) UnsetPublicFacingIpAddress()`

UnsetPublicFacingIpAddress ensures that no value is present for PublicFacingIpAddress, not even an explicit nil
### GetPublicFacingUrls

`func (o *HwBaselineResponseGetDataInner) GetPublicFacingUrls() string`

GetPublicFacingUrls returns the PublicFacingUrls field if non-nil, zero value otherwise.

### GetPublicFacingUrlsOk

`func (o *HwBaselineResponseGetDataInner) GetPublicFacingUrlsOk() (*string, bool)`

GetPublicFacingUrlsOk returns a tuple with the PublicFacingUrls field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPublicFacingUrls

`func (o *HwBaselineResponseGetDataInner) SetPublicFacingUrls(v string)`

SetPublicFacingUrls sets PublicFacingUrls field to given value.

### HasPublicFacingUrls

`func (o *HwBaselineResponseGetDataInner) HasPublicFacingUrls() bool`

HasPublicFacingUrls returns a boolean if a field has been set.

### SetPublicFacingUrlsNil

`func (o *HwBaselineResponseGetDataInner) SetPublicFacingUrlsNil(b bool)`

 SetPublicFacingUrlsNil sets the value for PublicFacingUrls to be an explicit nil

### UnsetPublicFacingUrls
`func (o *HwBaselineResponseGetDataInner) UnsetPublicFacingUrls()`

UnsetPublicFacingUrls ensures that no value is present for PublicFacingUrls, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


