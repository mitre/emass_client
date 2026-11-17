# DeviceScanResultsResponsePostDataInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Filename** | Pointer to **string** | [Required] single binary file. Specific file extensions are expected depending upon the scanType parameter. | [optional] 
**AssetsImported** | Pointer to **int64** | Number of assets imported from the scan file. | [optional] 
**Success** | Pointer to **bool** |  | [optional] 
**SystemId** | Pointer to **int64** |  | [optional] 
**Errors** | Pointer to **[]interface{}** |  | [optional] 

## Methods

### NewDeviceScanResultsResponsePostDataInner

`func NewDeviceScanResultsResponsePostDataInner() *DeviceScanResultsResponsePostDataInner`

NewDeviceScanResultsResponsePostDataInner instantiates a new DeviceScanResultsResponsePostDataInner object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewDeviceScanResultsResponsePostDataInnerWithDefaults

`func NewDeviceScanResultsResponsePostDataInnerWithDefaults() *DeviceScanResultsResponsePostDataInner`

NewDeviceScanResultsResponsePostDataInnerWithDefaults instantiates a new DeviceScanResultsResponsePostDataInner object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetFilename

`func (o *DeviceScanResultsResponsePostDataInner) GetFilename() string`

GetFilename returns the Filename field if non-nil, zero value otherwise.

### GetFilenameOk

`func (o *DeviceScanResultsResponsePostDataInner) GetFilenameOk() (*string, bool)`

GetFilenameOk returns a tuple with the Filename field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFilename

`func (o *DeviceScanResultsResponsePostDataInner) SetFilename(v string)`

SetFilename sets Filename field to given value.

### HasFilename

`func (o *DeviceScanResultsResponsePostDataInner) HasFilename() bool`

HasFilename returns a boolean if a field has been set.

### GetAssetsImported

`func (o *DeviceScanResultsResponsePostDataInner) GetAssetsImported() int64`

GetAssetsImported returns the AssetsImported field if non-nil, zero value otherwise.

### GetAssetsImportedOk

`func (o *DeviceScanResultsResponsePostDataInner) GetAssetsImportedOk() (*int64, bool)`

GetAssetsImportedOk returns a tuple with the AssetsImported field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAssetsImported

`func (o *DeviceScanResultsResponsePostDataInner) SetAssetsImported(v int64)`

SetAssetsImported sets AssetsImported field to given value.

### HasAssetsImported

`func (o *DeviceScanResultsResponsePostDataInner) HasAssetsImported() bool`

HasAssetsImported returns a boolean if a field has been set.

### GetSuccess

`func (o *DeviceScanResultsResponsePostDataInner) GetSuccess() bool`

GetSuccess returns the Success field if non-nil, zero value otherwise.

### GetSuccessOk

`func (o *DeviceScanResultsResponsePostDataInner) GetSuccessOk() (*bool, bool)`

GetSuccessOk returns a tuple with the Success field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSuccess

`func (o *DeviceScanResultsResponsePostDataInner) SetSuccess(v bool)`

SetSuccess sets Success field to given value.

### HasSuccess

`func (o *DeviceScanResultsResponsePostDataInner) HasSuccess() bool`

HasSuccess returns a boolean if a field has been set.

### GetSystemId

`func (o *DeviceScanResultsResponsePostDataInner) GetSystemId() int64`

GetSystemId returns the SystemId field if non-nil, zero value otherwise.

### GetSystemIdOk

`func (o *DeviceScanResultsResponsePostDataInner) GetSystemIdOk() (*int64, bool)`

GetSystemIdOk returns a tuple with the SystemId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSystemId

`func (o *DeviceScanResultsResponsePostDataInner) SetSystemId(v int64)`

SetSystemId sets SystemId field to given value.

### HasSystemId

`func (o *DeviceScanResultsResponsePostDataInner) HasSystemId() bool`

HasSystemId returns a boolean if a field has been set.

### GetErrors

`func (o *DeviceScanResultsResponsePostDataInner) GetErrors() []interface{}`

GetErrors returns the Errors field if non-nil, zero value otherwise.

### GetErrorsOk

`func (o *DeviceScanResultsResponsePostDataInner) GetErrorsOk() (*[]interface{}, bool)`

GetErrorsOk returns a tuple with the Errors field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetErrors

`func (o *DeviceScanResultsResponsePostDataInner) SetErrors(v []interface{})`

SetErrors sets Errors field to given value.

### HasErrors

`func (o *DeviceScanResultsResponsePostDataInner) HasErrors() bool`

HasErrors returns a boolean if a field has been set.

### SetErrorsNil

`func (o *DeviceScanResultsResponsePostDataInner) SetErrorsNil(b bool)`

 SetErrorsNil sets the value for Errors to be an explicit nil

### UnsetErrors
`func (o *DeviceScanResultsResponsePostDataInner) UnsetErrors()`

UnsetErrors ensures that no value is present for Errors, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


