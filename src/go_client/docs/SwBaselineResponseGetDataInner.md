# SwBaselineResponseGetDataInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**SystemId** | Pointer to **int64** | [Required] Unique eMASS system identifier. | [optional] 
**SoftwareId** | Pointer to **NullableString** | [Read-Only] GUID identifying the specific software asset. | [optional] 
**SoftwareVendor** | Pointer to **string** | [Required] Vendor of the software asset. | [optional] 
**SoftwareName** | Pointer to **string** | [Required] Name of the software asset. | [optional] 
**Version** | Pointer to **string** | [Required] Version of the software asset. | [optional] 
**SoftwareType** | Pointer to **NullableString** | [Optional] Type of the software asset. | [optional] 
**ParentSystem** | Pointer to **NullableString** | [Optional] Parent system of the software asset. | [optional] 
**Subsystem** | Pointer to **NullableString** | [Optional] Subsystem of the software asset. | [optional] 
**Network** | Pointer to **NullableString** | [Optional] Network of the software asset. | [optional] 
**HostingEnvironment** | Pointer to **NullableString** | [Optional] Hosting environment of the software asset. | [optional] 
**SoftwareDependencies** | Pointer to **NullableString** | [Optional] Dependencies of the software asset. | [optional] 
**CryptographicHash** | Pointer to **NullableString** | [Optional] Cryptographic hash of the software asset. | [optional] 
**InServiceData** | Pointer to **NullableString** | [Optional] In-service data of the software asset. | [optional] 
**ItBudgetUii** | Pointer to **NullableString** | [Optional] IT budget UII of the software asset. | [optional] 
**FiscalYear** | Pointer to **NullableString** | [Optional] Fiscal year (FY) of the software asset. | [optional] 
**PopEndDate** | Pointer to **NullableInt64** | [Optional] Period of performance (POP) end date of the software asset. | [optional] 
**LicenseOrContract** | Pointer to **NullableString** | [Optional] License or contract number of the software asset. | [optional] 
**LicenseTerm** | Pointer to **NullableString** | [Optional] License term of the software asset. | [optional] 
**CostPerLicense** | Pointer to **NullableFloat64** | [Optional] Cost per license of the software asset. Number will be converted to display 2 decimal points. | [optional] 
**TotalLicenses** | Pointer to **NullableInt64** | [Optional] Total licenses of the software asset. | [optional] 
**TotalLicenseCost** | Pointer to **NullableFloat64** | [Optional] Total license cost of the software asset. Number will be converted to display 2 decimal points. | [optional] 
**LicensesUsed** | Pointer to **NullableInt64** | [Optional] Number of licenses used for the software asset. | [optional] 
**LicensePoc** | Pointer to **NullableString** | [Optional] Point of contact (POC) for the software asset. | [optional] 
**LicenseRenewalDate** | Pointer to **NullableInt64** | [Optional] License renewal date for the software asset. | [optional] 
**LicenseExpirationDate** | Pointer to **NullableInt64** | [Optional] License expiration date for the software asset. | [optional] 
**ApprovalStatus** | Pointer to **NullableString** | [Optional] Approval status of the software asset. | [optional] 
**ReleaseDate** | Pointer to **NullableInt64** | [Optional] Release date of the software asset. | [optional] 
**MaintenanceDate** | Pointer to **NullableInt64** | [Optional] Maintenance date of the software asset. | [optional] 
**RetirementDate** | Pointer to **NullableInt64** | [Optional] Retirement date of the software asset. | [optional] 
**EndOfLifeSupportDate** | Pointer to **NullableInt64** | [Optional] End of life support date of the software asset. | [optional] 
**ExtendedEndOfLifeSupportDate** | Pointer to **NullableInt64** | [Optional] If set, the Extended End of Life/Support Date cannot occur prior to the End of Life/Support Date. | [optional] 
**CriticalAsset** | Pointer to **NullableBool** | [Optional] Indicates whether the asset is a critical information system asset. | [optional] 
**Location** | Pointer to **NullableString** | [Optional] Location of the software asset. | [optional] 
**Purpose** | Pointer to **NullableString** | [Optional] Purpose of the software asset. | [optional] 
**UnsupportedOperatingSystem** | Pointer to **NullableBool** | [Optional] Unsupported operating system. VA only. | [optional] 
**UnapprovedSoftwareFromTrm** | Pointer to **NullableBool** | [Optional] Unapproved software from TRM. VA only | [optional] 
**ApprovedWaiver** | Pointer to **NullableBool** | [Optional] Approved waiver. VA only | [optional] 

## Methods

### NewSwBaselineResponseGetDataInner

`func NewSwBaselineResponseGetDataInner() *SwBaselineResponseGetDataInner`

NewSwBaselineResponseGetDataInner instantiates a new SwBaselineResponseGetDataInner object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSwBaselineResponseGetDataInnerWithDefaults

`func NewSwBaselineResponseGetDataInnerWithDefaults() *SwBaselineResponseGetDataInner`

NewSwBaselineResponseGetDataInnerWithDefaults instantiates a new SwBaselineResponseGetDataInner object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetSystemId

`func (o *SwBaselineResponseGetDataInner) GetSystemId() int64`

GetSystemId returns the SystemId field if non-nil, zero value otherwise.

### GetSystemIdOk

`func (o *SwBaselineResponseGetDataInner) GetSystemIdOk() (*int64, bool)`

GetSystemIdOk returns a tuple with the SystemId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSystemId

`func (o *SwBaselineResponseGetDataInner) SetSystemId(v int64)`

SetSystemId sets SystemId field to given value.

### HasSystemId

`func (o *SwBaselineResponseGetDataInner) HasSystemId() bool`

HasSystemId returns a boolean if a field has been set.

### GetSoftwareId

`func (o *SwBaselineResponseGetDataInner) GetSoftwareId() string`

GetSoftwareId returns the SoftwareId field if non-nil, zero value otherwise.

### GetSoftwareIdOk

`func (o *SwBaselineResponseGetDataInner) GetSoftwareIdOk() (*string, bool)`

GetSoftwareIdOk returns a tuple with the SoftwareId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSoftwareId

`func (o *SwBaselineResponseGetDataInner) SetSoftwareId(v string)`

SetSoftwareId sets SoftwareId field to given value.

### HasSoftwareId

`func (o *SwBaselineResponseGetDataInner) HasSoftwareId() bool`

HasSoftwareId returns a boolean if a field has been set.

### SetSoftwareIdNil

`func (o *SwBaselineResponseGetDataInner) SetSoftwareIdNil(b bool)`

 SetSoftwareIdNil sets the value for SoftwareId to be an explicit nil

### UnsetSoftwareId
`func (o *SwBaselineResponseGetDataInner) UnsetSoftwareId()`

UnsetSoftwareId ensures that no value is present for SoftwareId, not even an explicit nil
### GetSoftwareVendor

`func (o *SwBaselineResponseGetDataInner) GetSoftwareVendor() string`

GetSoftwareVendor returns the SoftwareVendor field if non-nil, zero value otherwise.

### GetSoftwareVendorOk

`func (o *SwBaselineResponseGetDataInner) GetSoftwareVendorOk() (*string, bool)`

GetSoftwareVendorOk returns a tuple with the SoftwareVendor field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSoftwareVendor

`func (o *SwBaselineResponseGetDataInner) SetSoftwareVendor(v string)`

SetSoftwareVendor sets SoftwareVendor field to given value.

### HasSoftwareVendor

`func (o *SwBaselineResponseGetDataInner) HasSoftwareVendor() bool`

HasSoftwareVendor returns a boolean if a field has been set.

### GetSoftwareName

`func (o *SwBaselineResponseGetDataInner) GetSoftwareName() string`

GetSoftwareName returns the SoftwareName field if non-nil, zero value otherwise.

### GetSoftwareNameOk

`func (o *SwBaselineResponseGetDataInner) GetSoftwareNameOk() (*string, bool)`

GetSoftwareNameOk returns a tuple with the SoftwareName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSoftwareName

`func (o *SwBaselineResponseGetDataInner) SetSoftwareName(v string)`

SetSoftwareName sets SoftwareName field to given value.

### HasSoftwareName

`func (o *SwBaselineResponseGetDataInner) HasSoftwareName() bool`

HasSoftwareName returns a boolean if a field has been set.

### GetVersion

`func (o *SwBaselineResponseGetDataInner) GetVersion() string`

GetVersion returns the Version field if non-nil, zero value otherwise.

### GetVersionOk

`func (o *SwBaselineResponseGetDataInner) GetVersionOk() (*string, bool)`

GetVersionOk returns a tuple with the Version field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVersion

`func (o *SwBaselineResponseGetDataInner) SetVersion(v string)`

SetVersion sets Version field to given value.

### HasVersion

`func (o *SwBaselineResponseGetDataInner) HasVersion() bool`

HasVersion returns a boolean if a field has been set.

### GetSoftwareType

`func (o *SwBaselineResponseGetDataInner) GetSoftwareType() string`

GetSoftwareType returns the SoftwareType field if non-nil, zero value otherwise.

### GetSoftwareTypeOk

`func (o *SwBaselineResponseGetDataInner) GetSoftwareTypeOk() (*string, bool)`

GetSoftwareTypeOk returns a tuple with the SoftwareType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSoftwareType

`func (o *SwBaselineResponseGetDataInner) SetSoftwareType(v string)`

SetSoftwareType sets SoftwareType field to given value.

### HasSoftwareType

`func (o *SwBaselineResponseGetDataInner) HasSoftwareType() bool`

HasSoftwareType returns a boolean if a field has been set.

### SetSoftwareTypeNil

`func (o *SwBaselineResponseGetDataInner) SetSoftwareTypeNil(b bool)`

 SetSoftwareTypeNil sets the value for SoftwareType to be an explicit nil

### UnsetSoftwareType
`func (o *SwBaselineResponseGetDataInner) UnsetSoftwareType()`

UnsetSoftwareType ensures that no value is present for SoftwareType, not even an explicit nil
### GetParentSystem

`func (o *SwBaselineResponseGetDataInner) GetParentSystem() string`

GetParentSystem returns the ParentSystem field if non-nil, zero value otherwise.

### GetParentSystemOk

`func (o *SwBaselineResponseGetDataInner) GetParentSystemOk() (*string, bool)`

GetParentSystemOk returns a tuple with the ParentSystem field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetParentSystem

`func (o *SwBaselineResponseGetDataInner) SetParentSystem(v string)`

SetParentSystem sets ParentSystem field to given value.

### HasParentSystem

`func (o *SwBaselineResponseGetDataInner) HasParentSystem() bool`

HasParentSystem returns a boolean if a field has been set.

### SetParentSystemNil

`func (o *SwBaselineResponseGetDataInner) SetParentSystemNil(b bool)`

 SetParentSystemNil sets the value for ParentSystem to be an explicit nil

### UnsetParentSystem
`func (o *SwBaselineResponseGetDataInner) UnsetParentSystem()`

UnsetParentSystem ensures that no value is present for ParentSystem, not even an explicit nil
### GetSubsystem

`func (o *SwBaselineResponseGetDataInner) GetSubsystem() string`

GetSubsystem returns the Subsystem field if non-nil, zero value otherwise.

### GetSubsystemOk

`func (o *SwBaselineResponseGetDataInner) GetSubsystemOk() (*string, bool)`

GetSubsystemOk returns a tuple with the Subsystem field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSubsystem

`func (o *SwBaselineResponseGetDataInner) SetSubsystem(v string)`

SetSubsystem sets Subsystem field to given value.

### HasSubsystem

`func (o *SwBaselineResponseGetDataInner) HasSubsystem() bool`

HasSubsystem returns a boolean if a field has been set.

### SetSubsystemNil

`func (o *SwBaselineResponseGetDataInner) SetSubsystemNil(b bool)`

 SetSubsystemNil sets the value for Subsystem to be an explicit nil

### UnsetSubsystem
`func (o *SwBaselineResponseGetDataInner) UnsetSubsystem()`

UnsetSubsystem ensures that no value is present for Subsystem, not even an explicit nil
### GetNetwork

`func (o *SwBaselineResponseGetDataInner) GetNetwork() string`

GetNetwork returns the Network field if non-nil, zero value otherwise.

### GetNetworkOk

`func (o *SwBaselineResponseGetDataInner) GetNetworkOk() (*string, bool)`

GetNetworkOk returns a tuple with the Network field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNetwork

`func (o *SwBaselineResponseGetDataInner) SetNetwork(v string)`

SetNetwork sets Network field to given value.

### HasNetwork

`func (o *SwBaselineResponseGetDataInner) HasNetwork() bool`

HasNetwork returns a boolean if a field has been set.

### SetNetworkNil

`func (o *SwBaselineResponseGetDataInner) SetNetworkNil(b bool)`

 SetNetworkNil sets the value for Network to be an explicit nil

### UnsetNetwork
`func (o *SwBaselineResponseGetDataInner) UnsetNetwork()`

UnsetNetwork ensures that no value is present for Network, not even an explicit nil
### GetHostingEnvironment

`func (o *SwBaselineResponseGetDataInner) GetHostingEnvironment() string`

GetHostingEnvironment returns the HostingEnvironment field if non-nil, zero value otherwise.

### GetHostingEnvironmentOk

`func (o *SwBaselineResponseGetDataInner) GetHostingEnvironmentOk() (*string, bool)`

GetHostingEnvironmentOk returns a tuple with the HostingEnvironment field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHostingEnvironment

`func (o *SwBaselineResponseGetDataInner) SetHostingEnvironment(v string)`

SetHostingEnvironment sets HostingEnvironment field to given value.

### HasHostingEnvironment

`func (o *SwBaselineResponseGetDataInner) HasHostingEnvironment() bool`

HasHostingEnvironment returns a boolean if a field has been set.

### SetHostingEnvironmentNil

`func (o *SwBaselineResponseGetDataInner) SetHostingEnvironmentNil(b bool)`

 SetHostingEnvironmentNil sets the value for HostingEnvironment to be an explicit nil

### UnsetHostingEnvironment
`func (o *SwBaselineResponseGetDataInner) UnsetHostingEnvironment()`

UnsetHostingEnvironment ensures that no value is present for HostingEnvironment, not even an explicit nil
### GetSoftwareDependencies

`func (o *SwBaselineResponseGetDataInner) GetSoftwareDependencies() string`

GetSoftwareDependencies returns the SoftwareDependencies field if non-nil, zero value otherwise.

### GetSoftwareDependenciesOk

`func (o *SwBaselineResponseGetDataInner) GetSoftwareDependenciesOk() (*string, bool)`

GetSoftwareDependenciesOk returns a tuple with the SoftwareDependencies field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSoftwareDependencies

`func (o *SwBaselineResponseGetDataInner) SetSoftwareDependencies(v string)`

SetSoftwareDependencies sets SoftwareDependencies field to given value.

### HasSoftwareDependencies

`func (o *SwBaselineResponseGetDataInner) HasSoftwareDependencies() bool`

HasSoftwareDependencies returns a boolean if a field has been set.

### SetSoftwareDependenciesNil

`func (o *SwBaselineResponseGetDataInner) SetSoftwareDependenciesNil(b bool)`

 SetSoftwareDependenciesNil sets the value for SoftwareDependencies to be an explicit nil

### UnsetSoftwareDependencies
`func (o *SwBaselineResponseGetDataInner) UnsetSoftwareDependencies()`

UnsetSoftwareDependencies ensures that no value is present for SoftwareDependencies, not even an explicit nil
### GetCryptographicHash

`func (o *SwBaselineResponseGetDataInner) GetCryptographicHash() string`

GetCryptographicHash returns the CryptographicHash field if non-nil, zero value otherwise.

### GetCryptographicHashOk

`func (o *SwBaselineResponseGetDataInner) GetCryptographicHashOk() (*string, bool)`

GetCryptographicHashOk returns a tuple with the CryptographicHash field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCryptographicHash

`func (o *SwBaselineResponseGetDataInner) SetCryptographicHash(v string)`

SetCryptographicHash sets CryptographicHash field to given value.

### HasCryptographicHash

`func (o *SwBaselineResponseGetDataInner) HasCryptographicHash() bool`

HasCryptographicHash returns a boolean if a field has been set.

### SetCryptographicHashNil

`func (o *SwBaselineResponseGetDataInner) SetCryptographicHashNil(b bool)`

 SetCryptographicHashNil sets the value for CryptographicHash to be an explicit nil

### UnsetCryptographicHash
`func (o *SwBaselineResponseGetDataInner) UnsetCryptographicHash()`

UnsetCryptographicHash ensures that no value is present for CryptographicHash, not even an explicit nil
### GetInServiceData

`func (o *SwBaselineResponseGetDataInner) GetInServiceData() string`

GetInServiceData returns the InServiceData field if non-nil, zero value otherwise.

### GetInServiceDataOk

`func (o *SwBaselineResponseGetDataInner) GetInServiceDataOk() (*string, bool)`

GetInServiceDataOk returns a tuple with the InServiceData field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetInServiceData

`func (o *SwBaselineResponseGetDataInner) SetInServiceData(v string)`

SetInServiceData sets InServiceData field to given value.

### HasInServiceData

`func (o *SwBaselineResponseGetDataInner) HasInServiceData() bool`

HasInServiceData returns a boolean if a field has been set.

### SetInServiceDataNil

`func (o *SwBaselineResponseGetDataInner) SetInServiceDataNil(b bool)`

 SetInServiceDataNil sets the value for InServiceData to be an explicit nil

### UnsetInServiceData
`func (o *SwBaselineResponseGetDataInner) UnsetInServiceData()`

UnsetInServiceData ensures that no value is present for InServiceData, not even an explicit nil
### GetItBudgetUii

`func (o *SwBaselineResponseGetDataInner) GetItBudgetUii() string`

GetItBudgetUii returns the ItBudgetUii field if non-nil, zero value otherwise.

### GetItBudgetUiiOk

`func (o *SwBaselineResponseGetDataInner) GetItBudgetUiiOk() (*string, bool)`

GetItBudgetUiiOk returns a tuple with the ItBudgetUii field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItBudgetUii

`func (o *SwBaselineResponseGetDataInner) SetItBudgetUii(v string)`

SetItBudgetUii sets ItBudgetUii field to given value.

### HasItBudgetUii

`func (o *SwBaselineResponseGetDataInner) HasItBudgetUii() bool`

HasItBudgetUii returns a boolean if a field has been set.

### SetItBudgetUiiNil

`func (o *SwBaselineResponseGetDataInner) SetItBudgetUiiNil(b bool)`

 SetItBudgetUiiNil sets the value for ItBudgetUii to be an explicit nil

### UnsetItBudgetUii
`func (o *SwBaselineResponseGetDataInner) UnsetItBudgetUii()`

UnsetItBudgetUii ensures that no value is present for ItBudgetUii, not even an explicit nil
### GetFiscalYear

`func (o *SwBaselineResponseGetDataInner) GetFiscalYear() string`

GetFiscalYear returns the FiscalYear field if non-nil, zero value otherwise.

### GetFiscalYearOk

`func (o *SwBaselineResponseGetDataInner) GetFiscalYearOk() (*string, bool)`

GetFiscalYearOk returns a tuple with the FiscalYear field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFiscalYear

`func (o *SwBaselineResponseGetDataInner) SetFiscalYear(v string)`

SetFiscalYear sets FiscalYear field to given value.

### HasFiscalYear

`func (o *SwBaselineResponseGetDataInner) HasFiscalYear() bool`

HasFiscalYear returns a boolean if a field has been set.

### SetFiscalYearNil

`func (o *SwBaselineResponseGetDataInner) SetFiscalYearNil(b bool)`

 SetFiscalYearNil sets the value for FiscalYear to be an explicit nil

### UnsetFiscalYear
`func (o *SwBaselineResponseGetDataInner) UnsetFiscalYear()`

UnsetFiscalYear ensures that no value is present for FiscalYear, not even an explicit nil
### GetPopEndDate

`func (o *SwBaselineResponseGetDataInner) GetPopEndDate() int64`

GetPopEndDate returns the PopEndDate field if non-nil, zero value otherwise.

### GetPopEndDateOk

`func (o *SwBaselineResponseGetDataInner) GetPopEndDateOk() (*int64, bool)`

GetPopEndDateOk returns a tuple with the PopEndDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPopEndDate

`func (o *SwBaselineResponseGetDataInner) SetPopEndDate(v int64)`

SetPopEndDate sets PopEndDate field to given value.

### HasPopEndDate

`func (o *SwBaselineResponseGetDataInner) HasPopEndDate() bool`

HasPopEndDate returns a boolean if a field has been set.

### SetPopEndDateNil

`func (o *SwBaselineResponseGetDataInner) SetPopEndDateNil(b bool)`

 SetPopEndDateNil sets the value for PopEndDate to be an explicit nil

### UnsetPopEndDate
`func (o *SwBaselineResponseGetDataInner) UnsetPopEndDate()`

UnsetPopEndDate ensures that no value is present for PopEndDate, not even an explicit nil
### GetLicenseOrContract

`func (o *SwBaselineResponseGetDataInner) GetLicenseOrContract() string`

GetLicenseOrContract returns the LicenseOrContract field if non-nil, zero value otherwise.

### GetLicenseOrContractOk

`func (o *SwBaselineResponseGetDataInner) GetLicenseOrContractOk() (*string, bool)`

GetLicenseOrContractOk returns a tuple with the LicenseOrContract field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLicenseOrContract

`func (o *SwBaselineResponseGetDataInner) SetLicenseOrContract(v string)`

SetLicenseOrContract sets LicenseOrContract field to given value.

### HasLicenseOrContract

`func (o *SwBaselineResponseGetDataInner) HasLicenseOrContract() bool`

HasLicenseOrContract returns a boolean if a field has been set.

### SetLicenseOrContractNil

`func (o *SwBaselineResponseGetDataInner) SetLicenseOrContractNil(b bool)`

 SetLicenseOrContractNil sets the value for LicenseOrContract to be an explicit nil

### UnsetLicenseOrContract
`func (o *SwBaselineResponseGetDataInner) UnsetLicenseOrContract()`

UnsetLicenseOrContract ensures that no value is present for LicenseOrContract, not even an explicit nil
### GetLicenseTerm

`func (o *SwBaselineResponseGetDataInner) GetLicenseTerm() string`

GetLicenseTerm returns the LicenseTerm field if non-nil, zero value otherwise.

### GetLicenseTermOk

`func (o *SwBaselineResponseGetDataInner) GetLicenseTermOk() (*string, bool)`

GetLicenseTermOk returns a tuple with the LicenseTerm field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLicenseTerm

`func (o *SwBaselineResponseGetDataInner) SetLicenseTerm(v string)`

SetLicenseTerm sets LicenseTerm field to given value.

### HasLicenseTerm

`func (o *SwBaselineResponseGetDataInner) HasLicenseTerm() bool`

HasLicenseTerm returns a boolean if a field has been set.

### SetLicenseTermNil

`func (o *SwBaselineResponseGetDataInner) SetLicenseTermNil(b bool)`

 SetLicenseTermNil sets the value for LicenseTerm to be an explicit nil

### UnsetLicenseTerm
`func (o *SwBaselineResponseGetDataInner) UnsetLicenseTerm()`

UnsetLicenseTerm ensures that no value is present for LicenseTerm, not even an explicit nil
### GetCostPerLicense

`func (o *SwBaselineResponseGetDataInner) GetCostPerLicense() float64`

GetCostPerLicense returns the CostPerLicense field if non-nil, zero value otherwise.

### GetCostPerLicenseOk

`func (o *SwBaselineResponseGetDataInner) GetCostPerLicenseOk() (*float64, bool)`

GetCostPerLicenseOk returns a tuple with the CostPerLicense field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCostPerLicense

`func (o *SwBaselineResponseGetDataInner) SetCostPerLicense(v float64)`

SetCostPerLicense sets CostPerLicense field to given value.

### HasCostPerLicense

`func (o *SwBaselineResponseGetDataInner) HasCostPerLicense() bool`

HasCostPerLicense returns a boolean if a field has been set.

### SetCostPerLicenseNil

`func (o *SwBaselineResponseGetDataInner) SetCostPerLicenseNil(b bool)`

 SetCostPerLicenseNil sets the value for CostPerLicense to be an explicit nil

### UnsetCostPerLicense
`func (o *SwBaselineResponseGetDataInner) UnsetCostPerLicense()`

UnsetCostPerLicense ensures that no value is present for CostPerLicense, not even an explicit nil
### GetTotalLicenses

`func (o *SwBaselineResponseGetDataInner) GetTotalLicenses() int64`

GetTotalLicenses returns the TotalLicenses field if non-nil, zero value otherwise.

### GetTotalLicensesOk

`func (o *SwBaselineResponseGetDataInner) GetTotalLicensesOk() (*int64, bool)`

GetTotalLicensesOk returns a tuple with the TotalLicenses field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotalLicenses

`func (o *SwBaselineResponseGetDataInner) SetTotalLicenses(v int64)`

SetTotalLicenses sets TotalLicenses field to given value.

### HasTotalLicenses

`func (o *SwBaselineResponseGetDataInner) HasTotalLicenses() bool`

HasTotalLicenses returns a boolean if a field has been set.

### SetTotalLicensesNil

`func (o *SwBaselineResponseGetDataInner) SetTotalLicensesNil(b bool)`

 SetTotalLicensesNil sets the value for TotalLicenses to be an explicit nil

### UnsetTotalLicenses
`func (o *SwBaselineResponseGetDataInner) UnsetTotalLicenses()`

UnsetTotalLicenses ensures that no value is present for TotalLicenses, not even an explicit nil
### GetTotalLicenseCost

`func (o *SwBaselineResponseGetDataInner) GetTotalLicenseCost() float64`

GetTotalLicenseCost returns the TotalLicenseCost field if non-nil, zero value otherwise.

### GetTotalLicenseCostOk

`func (o *SwBaselineResponseGetDataInner) GetTotalLicenseCostOk() (*float64, bool)`

GetTotalLicenseCostOk returns a tuple with the TotalLicenseCost field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotalLicenseCost

`func (o *SwBaselineResponseGetDataInner) SetTotalLicenseCost(v float64)`

SetTotalLicenseCost sets TotalLicenseCost field to given value.

### HasTotalLicenseCost

`func (o *SwBaselineResponseGetDataInner) HasTotalLicenseCost() bool`

HasTotalLicenseCost returns a boolean if a field has been set.

### SetTotalLicenseCostNil

`func (o *SwBaselineResponseGetDataInner) SetTotalLicenseCostNil(b bool)`

 SetTotalLicenseCostNil sets the value for TotalLicenseCost to be an explicit nil

### UnsetTotalLicenseCost
`func (o *SwBaselineResponseGetDataInner) UnsetTotalLicenseCost()`

UnsetTotalLicenseCost ensures that no value is present for TotalLicenseCost, not even an explicit nil
### GetLicensesUsed

`func (o *SwBaselineResponseGetDataInner) GetLicensesUsed() int64`

GetLicensesUsed returns the LicensesUsed field if non-nil, zero value otherwise.

### GetLicensesUsedOk

`func (o *SwBaselineResponseGetDataInner) GetLicensesUsedOk() (*int64, bool)`

GetLicensesUsedOk returns a tuple with the LicensesUsed field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLicensesUsed

`func (o *SwBaselineResponseGetDataInner) SetLicensesUsed(v int64)`

SetLicensesUsed sets LicensesUsed field to given value.

### HasLicensesUsed

`func (o *SwBaselineResponseGetDataInner) HasLicensesUsed() bool`

HasLicensesUsed returns a boolean if a field has been set.

### SetLicensesUsedNil

`func (o *SwBaselineResponseGetDataInner) SetLicensesUsedNil(b bool)`

 SetLicensesUsedNil sets the value for LicensesUsed to be an explicit nil

### UnsetLicensesUsed
`func (o *SwBaselineResponseGetDataInner) UnsetLicensesUsed()`

UnsetLicensesUsed ensures that no value is present for LicensesUsed, not even an explicit nil
### GetLicensePoc

`func (o *SwBaselineResponseGetDataInner) GetLicensePoc() string`

GetLicensePoc returns the LicensePoc field if non-nil, zero value otherwise.

### GetLicensePocOk

`func (o *SwBaselineResponseGetDataInner) GetLicensePocOk() (*string, bool)`

GetLicensePocOk returns a tuple with the LicensePoc field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLicensePoc

`func (o *SwBaselineResponseGetDataInner) SetLicensePoc(v string)`

SetLicensePoc sets LicensePoc field to given value.

### HasLicensePoc

`func (o *SwBaselineResponseGetDataInner) HasLicensePoc() bool`

HasLicensePoc returns a boolean if a field has been set.

### SetLicensePocNil

`func (o *SwBaselineResponseGetDataInner) SetLicensePocNil(b bool)`

 SetLicensePocNil sets the value for LicensePoc to be an explicit nil

### UnsetLicensePoc
`func (o *SwBaselineResponseGetDataInner) UnsetLicensePoc()`

UnsetLicensePoc ensures that no value is present for LicensePoc, not even an explicit nil
### GetLicenseRenewalDate

`func (o *SwBaselineResponseGetDataInner) GetLicenseRenewalDate() int64`

GetLicenseRenewalDate returns the LicenseRenewalDate field if non-nil, zero value otherwise.

### GetLicenseRenewalDateOk

`func (o *SwBaselineResponseGetDataInner) GetLicenseRenewalDateOk() (*int64, bool)`

GetLicenseRenewalDateOk returns a tuple with the LicenseRenewalDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLicenseRenewalDate

`func (o *SwBaselineResponseGetDataInner) SetLicenseRenewalDate(v int64)`

SetLicenseRenewalDate sets LicenseRenewalDate field to given value.

### HasLicenseRenewalDate

`func (o *SwBaselineResponseGetDataInner) HasLicenseRenewalDate() bool`

HasLicenseRenewalDate returns a boolean if a field has been set.

### SetLicenseRenewalDateNil

`func (o *SwBaselineResponseGetDataInner) SetLicenseRenewalDateNil(b bool)`

 SetLicenseRenewalDateNil sets the value for LicenseRenewalDate to be an explicit nil

### UnsetLicenseRenewalDate
`func (o *SwBaselineResponseGetDataInner) UnsetLicenseRenewalDate()`

UnsetLicenseRenewalDate ensures that no value is present for LicenseRenewalDate, not even an explicit nil
### GetLicenseExpirationDate

`func (o *SwBaselineResponseGetDataInner) GetLicenseExpirationDate() int64`

GetLicenseExpirationDate returns the LicenseExpirationDate field if non-nil, zero value otherwise.

### GetLicenseExpirationDateOk

`func (o *SwBaselineResponseGetDataInner) GetLicenseExpirationDateOk() (*int64, bool)`

GetLicenseExpirationDateOk returns a tuple with the LicenseExpirationDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLicenseExpirationDate

`func (o *SwBaselineResponseGetDataInner) SetLicenseExpirationDate(v int64)`

SetLicenseExpirationDate sets LicenseExpirationDate field to given value.

### HasLicenseExpirationDate

`func (o *SwBaselineResponseGetDataInner) HasLicenseExpirationDate() bool`

HasLicenseExpirationDate returns a boolean if a field has been set.

### SetLicenseExpirationDateNil

`func (o *SwBaselineResponseGetDataInner) SetLicenseExpirationDateNil(b bool)`

 SetLicenseExpirationDateNil sets the value for LicenseExpirationDate to be an explicit nil

### UnsetLicenseExpirationDate
`func (o *SwBaselineResponseGetDataInner) UnsetLicenseExpirationDate()`

UnsetLicenseExpirationDate ensures that no value is present for LicenseExpirationDate, not even an explicit nil
### GetApprovalStatus

`func (o *SwBaselineResponseGetDataInner) GetApprovalStatus() string`

GetApprovalStatus returns the ApprovalStatus field if non-nil, zero value otherwise.

### GetApprovalStatusOk

`func (o *SwBaselineResponseGetDataInner) GetApprovalStatusOk() (*string, bool)`

GetApprovalStatusOk returns a tuple with the ApprovalStatus field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetApprovalStatus

`func (o *SwBaselineResponseGetDataInner) SetApprovalStatus(v string)`

SetApprovalStatus sets ApprovalStatus field to given value.

### HasApprovalStatus

`func (o *SwBaselineResponseGetDataInner) HasApprovalStatus() bool`

HasApprovalStatus returns a boolean if a field has been set.

### SetApprovalStatusNil

`func (o *SwBaselineResponseGetDataInner) SetApprovalStatusNil(b bool)`

 SetApprovalStatusNil sets the value for ApprovalStatus to be an explicit nil

### UnsetApprovalStatus
`func (o *SwBaselineResponseGetDataInner) UnsetApprovalStatus()`

UnsetApprovalStatus ensures that no value is present for ApprovalStatus, not even an explicit nil
### GetReleaseDate

`func (o *SwBaselineResponseGetDataInner) GetReleaseDate() int64`

GetReleaseDate returns the ReleaseDate field if non-nil, zero value otherwise.

### GetReleaseDateOk

`func (o *SwBaselineResponseGetDataInner) GetReleaseDateOk() (*int64, bool)`

GetReleaseDateOk returns a tuple with the ReleaseDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetReleaseDate

`func (o *SwBaselineResponseGetDataInner) SetReleaseDate(v int64)`

SetReleaseDate sets ReleaseDate field to given value.

### HasReleaseDate

`func (o *SwBaselineResponseGetDataInner) HasReleaseDate() bool`

HasReleaseDate returns a boolean if a field has been set.

### SetReleaseDateNil

`func (o *SwBaselineResponseGetDataInner) SetReleaseDateNil(b bool)`

 SetReleaseDateNil sets the value for ReleaseDate to be an explicit nil

### UnsetReleaseDate
`func (o *SwBaselineResponseGetDataInner) UnsetReleaseDate()`

UnsetReleaseDate ensures that no value is present for ReleaseDate, not even an explicit nil
### GetMaintenanceDate

`func (o *SwBaselineResponseGetDataInner) GetMaintenanceDate() int64`

GetMaintenanceDate returns the MaintenanceDate field if non-nil, zero value otherwise.

### GetMaintenanceDateOk

`func (o *SwBaselineResponseGetDataInner) GetMaintenanceDateOk() (*int64, bool)`

GetMaintenanceDateOk returns a tuple with the MaintenanceDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMaintenanceDate

`func (o *SwBaselineResponseGetDataInner) SetMaintenanceDate(v int64)`

SetMaintenanceDate sets MaintenanceDate field to given value.

### HasMaintenanceDate

`func (o *SwBaselineResponseGetDataInner) HasMaintenanceDate() bool`

HasMaintenanceDate returns a boolean if a field has been set.

### SetMaintenanceDateNil

`func (o *SwBaselineResponseGetDataInner) SetMaintenanceDateNil(b bool)`

 SetMaintenanceDateNil sets the value for MaintenanceDate to be an explicit nil

### UnsetMaintenanceDate
`func (o *SwBaselineResponseGetDataInner) UnsetMaintenanceDate()`

UnsetMaintenanceDate ensures that no value is present for MaintenanceDate, not even an explicit nil
### GetRetirementDate

`func (o *SwBaselineResponseGetDataInner) GetRetirementDate() int64`

GetRetirementDate returns the RetirementDate field if non-nil, zero value otherwise.

### GetRetirementDateOk

`func (o *SwBaselineResponseGetDataInner) GetRetirementDateOk() (*int64, bool)`

GetRetirementDateOk returns a tuple with the RetirementDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRetirementDate

`func (o *SwBaselineResponseGetDataInner) SetRetirementDate(v int64)`

SetRetirementDate sets RetirementDate field to given value.

### HasRetirementDate

`func (o *SwBaselineResponseGetDataInner) HasRetirementDate() bool`

HasRetirementDate returns a boolean if a field has been set.

### SetRetirementDateNil

`func (o *SwBaselineResponseGetDataInner) SetRetirementDateNil(b bool)`

 SetRetirementDateNil sets the value for RetirementDate to be an explicit nil

### UnsetRetirementDate
`func (o *SwBaselineResponseGetDataInner) UnsetRetirementDate()`

UnsetRetirementDate ensures that no value is present for RetirementDate, not even an explicit nil
### GetEndOfLifeSupportDate

`func (o *SwBaselineResponseGetDataInner) GetEndOfLifeSupportDate() int64`

GetEndOfLifeSupportDate returns the EndOfLifeSupportDate field if non-nil, zero value otherwise.

### GetEndOfLifeSupportDateOk

`func (o *SwBaselineResponseGetDataInner) GetEndOfLifeSupportDateOk() (*int64, bool)`

GetEndOfLifeSupportDateOk returns a tuple with the EndOfLifeSupportDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEndOfLifeSupportDate

`func (o *SwBaselineResponseGetDataInner) SetEndOfLifeSupportDate(v int64)`

SetEndOfLifeSupportDate sets EndOfLifeSupportDate field to given value.

### HasEndOfLifeSupportDate

`func (o *SwBaselineResponseGetDataInner) HasEndOfLifeSupportDate() bool`

HasEndOfLifeSupportDate returns a boolean if a field has been set.

### SetEndOfLifeSupportDateNil

`func (o *SwBaselineResponseGetDataInner) SetEndOfLifeSupportDateNil(b bool)`

 SetEndOfLifeSupportDateNil sets the value for EndOfLifeSupportDate to be an explicit nil

### UnsetEndOfLifeSupportDate
`func (o *SwBaselineResponseGetDataInner) UnsetEndOfLifeSupportDate()`

UnsetEndOfLifeSupportDate ensures that no value is present for EndOfLifeSupportDate, not even an explicit nil
### GetExtendedEndOfLifeSupportDate

`func (o *SwBaselineResponseGetDataInner) GetExtendedEndOfLifeSupportDate() int64`

GetExtendedEndOfLifeSupportDate returns the ExtendedEndOfLifeSupportDate field if non-nil, zero value otherwise.

### GetExtendedEndOfLifeSupportDateOk

`func (o *SwBaselineResponseGetDataInner) GetExtendedEndOfLifeSupportDateOk() (*int64, bool)`

GetExtendedEndOfLifeSupportDateOk returns a tuple with the ExtendedEndOfLifeSupportDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExtendedEndOfLifeSupportDate

`func (o *SwBaselineResponseGetDataInner) SetExtendedEndOfLifeSupportDate(v int64)`

SetExtendedEndOfLifeSupportDate sets ExtendedEndOfLifeSupportDate field to given value.

### HasExtendedEndOfLifeSupportDate

`func (o *SwBaselineResponseGetDataInner) HasExtendedEndOfLifeSupportDate() bool`

HasExtendedEndOfLifeSupportDate returns a boolean if a field has been set.

### SetExtendedEndOfLifeSupportDateNil

`func (o *SwBaselineResponseGetDataInner) SetExtendedEndOfLifeSupportDateNil(b bool)`

 SetExtendedEndOfLifeSupportDateNil sets the value for ExtendedEndOfLifeSupportDate to be an explicit nil

### UnsetExtendedEndOfLifeSupportDate
`func (o *SwBaselineResponseGetDataInner) UnsetExtendedEndOfLifeSupportDate()`

UnsetExtendedEndOfLifeSupportDate ensures that no value is present for ExtendedEndOfLifeSupportDate, not even an explicit nil
### GetCriticalAsset

`func (o *SwBaselineResponseGetDataInner) GetCriticalAsset() bool`

GetCriticalAsset returns the CriticalAsset field if non-nil, zero value otherwise.

### GetCriticalAssetOk

`func (o *SwBaselineResponseGetDataInner) GetCriticalAssetOk() (*bool, bool)`

GetCriticalAssetOk returns a tuple with the CriticalAsset field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCriticalAsset

`func (o *SwBaselineResponseGetDataInner) SetCriticalAsset(v bool)`

SetCriticalAsset sets CriticalAsset field to given value.

### HasCriticalAsset

`func (o *SwBaselineResponseGetDataInner) HasCriticalAsset() bool`

HasCriticalAsset returns a boolean if a field has been set.

### SetCriticalAssetNil

`func (o *SwBaselineResponseGetDataInner) SetCriticalAssetNil(b bool)`

 SetCriticalAssetNil sets the value for CriticalAsset to be an explicit nil

### UnsetCriticalAsset
`func (o *SwBaselineResponseGetDataInner) UnsetCriticalAsset()`

UnsetCriticalAsset ensures that no value is present for CriticalAsset, not even an explicit nil
### GetLocation

`func (o *SwBaselineResponseGetDataInner) GetLocation() string`

GetLocation returns the Location field if non-nil, zero value otherwise.

### GetLocationOk

`func (o *SwBaselineResponseGetDataInner) GetLocationOk() (*string, bool)`

GetLocationOk returns a tuple with the Location field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLocation

`func (o *SwBaselineResponseGetDataInner) SetLocation(v string)`

SetLocation sets Location field to given value.

### HasLocation

`func (o *SwBaselineResponseGetDataInner) HasLocation() bool`

HasLocation returns a boolean if a field has been set.

### SetLocationNil

`func (o *SwBaselineResponseGetDataInner) SetLocationNil(b bool)`

 SetLocationNil sets the value for Location to be an explicit nil

### UnsetLocation
`func (o *SwBaselineResponseGetDataInner) UnsetLocation()`

UnsetLocation ensures that no value is present for Location, not even an explicit nil
### GetPurpose

`func (o *SwBaselineResponseGetDataInner) GetPurpose() string`

GetPurpose returns the Purpose field if non-nil, zero value otherwise.

### GetPurposeOk

`func (o *SwBaselineResponseGetDataInner) GetPurposeOk() (*string, bool)`

GetPurposeOk returns a tuple with the Purpose field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPurpose

`func (o *SwBaselineResponseGetDataInner) SetPurpose(v string)`

SetPurpose sets Purpose field to given value.

### HasPurpose

`func (o *SwBaselineResponseGetDataInner) HasPurpose() bool`

HasPurpose returns a boolean if a field has been set.

### SetPurposeNil

`func (o *SwBaselineResponseGetDataInner) SetPurposeNil(b bool)`

 SetPurposeNil sets the value for Purpose to be an explicit nil

### UnsetPurpose
`func (o *SwBaselineResponseGetDataInner) UnsetPurpose()`

UnsetPurpose ensures that no value is present for Purpose, not even an explicit nil
### GetUnsupportedOperatingSystem

`func (o *SwBaselineResponseGetDataInner) GetUnsupportedOperatingSystem() bool`

GetUnsupportedOperatingSystem returns the UnsupportedOperatingSystem field if non-nil, zero value otherwise.

### GetUnsupportedOperatingSystemOk

`func (o *SwBaselineResponseGetDataInner) GetUnsupportedOperatingSystemOk() (*bool, bool)`

GetUnsupportedOperatingSystemOk returns a tuple with the UnsupportedOperatingSystem field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUnsupportedOperatingSystem

`func (o *SwBaselineResponseGetDataInner) SetUnsupportedOperatingSystem(v bool)`

SetUnsupportedOperatingSystem sets UnsupportedOperatingSystem field to given value.

### HasUnsupportedOperatingSystem

`func (o *SwBaselineResponseGetDataInner) HasUnsupportedOperatingSystem() bool`

HasUnsupportedOperatingSystem returns a boolean if a field has been set.

### SetUnsupportedOperatingSystemNil

`func (o *SwBaselineResponseGetDataInner) SetUnsupportedOperatingSystemNil(b bool)`

 SetUnsupportedOperatingSystemNil sets the value for UnsupportedOperatingSystem to be an explicit nil

### UnsetUnsupportedOperatingSystem
`func (o *SwBaselineResponseGetDataInner) UnsetUnsupportedOperatingSystem()`

UnsetUnsupportedOperatingSystem ensures that no value is present for UnsupportedOperatingSystem, not even an explicit nil
### GetUnapprovedSoftwareFromTrm

`func (o *SwBaselineResponseGetDataInner) GetUnapprovedSoftwareFromTrm() bool`

GetUnapprovedSoftwareFromTrm returns the UnapprovedSoftwareFromTrm field if non-nil, zero value otherwise.

### GetUnapprovedSoftwareFromTrmOk

`func (o *SwBaselineResponseGetDataInner) GetUnapprovedSoftwareFromTrmOk() (*bool, bool)`

GetUnapprovedSoftwareFromTrmOk returns a tuple with the UnapprovedSoftwareFromTrm field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUnapprovedSoftwareFromTrm

`func (o *SwBaselineResponseGetDataInner) SetUnapprovedSoftwareFromTrm(v bool)`

SetUnapprovedSoftwareFromTrm sets UnapprovedSoftwareFromTrm field to given value.

### HasUnapprovedSoftwareFromTrm

`func (o *SwBaselineResponseGetDataInner) HasUnapprovedSoftwareFromTrm() bool`

HasUnapprovedSoftwareFromTrm returns a boolean if a field has been set.

### SetUnapprovedSoftwareFromTrmNil

`func (o *SwBaselineResponseGetDataInner) SetUnapprovedSoftwareFromTrmNil(b bool)`

 SetUnapprovedSoftwareFromTrmNil sets the value for UnapprovedSoftwareFromTrm to be an explicit nil

### UnsetUnapprovedSoftwareFromTrm
`func (o *SwBaselineResponseGetDataInner) UnsetUnapprovedSoftwareFromTrm()`

UnsetUnapprovedSoftwareFromTrm ensures that no value is present for UnapprovedSoftwareFromTrm, not even an explicit nil
### GetApprovedWaiver

`func (o *SwBaselineResponseGetDataInner) GetApprovedWaiver() bool`

GetApprovedWaiver returns the ApprovedWaiver field if non-nil, zero value otherwise.

### GetApprovedWaiverOk

`func (o *SwBaselineResponseGetDataInner) GetApprovedWaiverOk() (*bool, bool)`

GetApprovedWaiverOk returns a tuple with the ApprovedWaiver field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetApprovedWaiver

`func (o *SwBaselineResponseGetDataInner) SetApprovedWaiver(v bool)`

SetApprovedWaiver sets ApprovedWaiver field to given value.

### HasApprovedWaiver

`func (o *SwBaselineResponseGetDataInner) HasApprovedWaiver() bool`

HasApprovedWaiver returns a boolean if a field has been set.

### SetApprovedWaiverNil

`func (o *SwBaselineResponseGetDataInner) SetApprovedWaiverNil(b bool)`

 SetApprovedWaiverNil sets the value for ApprovedWaiver to be an explicit nil

### UnsetApprovedWaiver
`func (o *SwBaselineResponseGetDataInner) UnsetApprovedWaiver()`

UnsetApprovedWaiver ensures that no value is present for ApprovedWaiver, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


