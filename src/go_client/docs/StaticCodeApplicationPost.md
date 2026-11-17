# StaticCodeApplicationPost

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**RawSeverity** | Pointer to **string** | [Optional] Scan vulnerability ratting | [optional] 
**CodeCheckName** | Pointer to **string** | [Required] Name of the software vulnerability or weakness. | [optional] 
**Count** | Pointer to **int64** | [Required] Number of instances observed for a specified finding. | [optional] 
**ScanDate** | Pointer to **int64** | [Required] The date of the scan. Unix date format. | [optional] 
**CweId** | Pointer to **string** | [Required] The Common Weakness Enumerator (CWE) identifier. | [optional] 
**ClearFindings** | Pointer to **bool** | [Optional] When used by itself, can clear out all application findings for a single application/version pairing. | [optional] 

## Methods

### NewStaticCodeApplicationPost

`func NewStaticCodeApplicationPost() *StaticCodeApplicationPost`

NewStaticCodeApplicationPost instantiates a new StaticCodeApplicationPost object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewStaticCodeApplicationPostWithDefaults

`func NewStaticCodeApplicationPostWithDefaults() *StaticCodeApplicationPost`

NewStaticCodeApplicationPostWithDefaults instantiates a new StaticCodeApplicationPost object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetRawSeverity

`func (o *StaticCodeApplicationPost) GetRawSeverity() string`

GetRawSeverity returns the RawSeverity field if non-nil, zero value otherwise.

### GetRawSeverityOk

`func (o *StaticCodeApplicationPost) GetRawSeverityOk() (*string, bool)`

GetRawSeverityOk returns a tuple with the RawSeverity field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRawSeverity

`func (o *StaticCodeApplicationPost) SetRawSeverity(v string)`

SetRawSeverity sets RawSeverity field to given value.

### HasRawSeverity

`func (o *StaticCodeApplicationPost) HasRawSeverity() bool`

HasRawSeverity returns a boolean if a field has been set.

### GetCodeCheckName

`func (o *StaticCodeApplicationPost) GetCodeCheckName() string`

GetCodeCheckName returns the CodeCheckName field if non-nil, zero value otherwise.

### GetCodeCheckNameOk

`func (o *StaticCodeApplicationPost) GetCodeCheckNameOk() (*string, bool)`

GetCodeCheckNameOk returns a tuple with the CodeCheckName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCodeCheckName

`func (o *StaticCodeApplicationPost) SetCodeCheckName(v string)`

SetCodeCheckName sets CodeCheckName field to given value.

### HasCodeCheckName

`func (o *StaticCodeApplicationPost) HasCodeCheckName() bool`

HasCodeCheckName returns a boolean if a field has been set.

### GetCount

`func (o *StaticCodeApplicationPost) GetCount() int64`

GetCount returns the Count field if non-nil, zero value otherwise.

### GetCountOk

`func (o *StaticCodeApplicationPost) GetCountOk() (*int64, bool)`

GetCountOk returns a tuple with the Count field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCount

`func (o *StaticCodeApplicationPost) SetCount(v int64)`

SetCount sets Count field to given value.

### HasCount

`func (o *StaticCodeApplicationPost) HasCount() bool`

HasCount returns a boolean if a field has been set.

### GetScanDate

`func (o *StaticCodeApplicationPost) GetScanDate() int64`

GetScanDate returns the ScanDate field if non-nil, zero value otherwise.

### GetScanDateOk

`func (o *StaticCodeApplicationPost) GetScanDateOk() (*int64, bool)`

GetScanDateOk returns a tuple with the ScanDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetScanDate

`func (o *StaticCodeApplicationPost) SetScanDate(v int64)`

SetScanDate sets ScanDate field to given value.

### HasScanDate

`func (o *StaticCodeApplicationPost) HasScanDate() bool`

HasScanDate returns a boolean if a field has been set.

### GetCweId

`func (o *StaticCodeApplicationPost) GetCweId() string`

GetCweId returns the CweId field if non-nil, zero value otherwise.

### GetCweIdOk

`func (o *StaticCodeApplicationPost) GetCweIdOk() (*string, bool)`

GetCweIdOk returns a tuple with the CweId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCweId

`func (o *StaticCodeApplicationPost) SetCweId(v string)`

SetCweId sets CweId field to given value.

### HasCweId

`func (o *StaticCodeApplicationPost) HasCweId() bool`

HasCweId returns a boolean if a field has been set.

### GetClearFindings

`func (o *StaticCodeApplicationPost) GetClearFindings() bool`

GetClearFindings returns the ClearFindings field if non-nil, zero value otherwise.

### GetClearFindingsOk

`func (o *StaticCodeApplicationPost) GetClearFindingsOk() (*bool, bool)`

GetClearFindingsOk returns a tuple with the ClearFindings field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClearFindings

`func (o *StaticCodeApplicationPost) SetClearFindings(v bool)`

SetClearFindings sets ClearFindings field to given value.

### HasClearFindings

`func (o *StaticCodeApplicationPost) HasClearFindings() bool`

HasClearFindings returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


