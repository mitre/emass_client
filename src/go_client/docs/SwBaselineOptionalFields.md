# SwBaselineOptionalFields

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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

### NewSwBaselineOptionalFields

`func NewSwBaselineOptionalFields() *SwBaselineOptionalFields`

NewSwBaselineOptionalFields instantiates a new SwBaselineOptionalFields object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSwBaselineOptionalFieldsWithDefaults

`func NewSwBaselineOptionalFieldsWithDefaults() *SwBaselineOptionalFields`

NewSwBaselineOptionalFieldsWithDefaults instantiates a new SwBaselineOptionalFields object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetSoftwareType

`func (o *SwBaselineOptionalFields) GetSoftwareType() string`

GetSoftwareType returns the SoftwareType field if non-nil, zero value otherwise.

### GetSoftwareTypeOk

`func (o *SwBaselineOptionalFields) GetSoftwareTypeOk() (*string, bool)`

GetSoftwareTypeOk returns a tuple with the SoftwareType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSoftwareType

`func (o *SwBaselineOptionalFields) SetSoftwareType(v string)`

SetSoftwareType sets SoftwareType field to given value.

### HasSoftwareType

`func (o *SwBaselineOptionalFields) HasSoftwareType() bool`

HasSoftwareType returns a boolean if a field has been set.

### SetSoftwareTypeNil

`func (o *SwBaselineOptionalFields) SetSoftwareTypeNil(b bool)`

 SetSoftwareTypeNil sets the value for SoftwareType to be an explicit nil

### UnsetSoftwareType
`func (o *SwBaselineOptionalFields) UnsetSoftwareType()`

UnsetSoftwareType ensures that no value is present for SoftwareType, not even an explicit nil
### GetParentSystem

`func (o *SwBaselineOptionalFields) GetParentSystem() string`

GetParentSystem returns the ParentSystem field if non-nil, zero value otherwise.

### GetParentSystemOk

`func (o *SwBaselineOptionalFields) GetParentSystemOk() (*string, bool)`

GetParentSystemOk returns a tuple with the ParentSystem field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetParentSystem

`func (o *SwBaselineOptionalFields) SetParentSystem(v string)`

SetParentSystem sets ParentSystem field to given value.

### HasParentSystem

`func (o *SwBaselineOptionalFields) HasParentSystem() bool`

HasParentSystem returns a boolean if a field has been set.

### SetParentSystemNil

`func (o *SwBaselineOptionalFields) SetParentSystemNil(b bool)`

 SetParentSystemNil sets the value for ParentSystem to be an explicit nil

### UnsetParentSystem
`func (o *SwBaselineOptionalFields) UnsetParentSystem()`

UnsetParentSystem ensures that no value is present for ParentSystem, not even an explicit nil
### GetSubsystem

`func (o *SwBaselineOptionalFields) GetSubsystem() string`

GetSubsystem returns the Subsystem field if non-nil, zero value otherwise.

### GetSubsystemOk

`func (o *SwBaselineOptionalFields) GetSubsystemOk() (*string, bool)`

GetSubsystemOk returns a tuple with the Subsystem field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSubsystem

`func (o *SwBaselineOptionalFields) SetSubsystem(v string)`

SetSubsystem sets Subsystem field to given value.

### HasSubsystem

`func (o *SwBaselineOptionalFields) HasSubsystem() bool`

HasSubsystem returns a boolean if a field has been set.

### SetSubsystemNil

`func (o *SwBaselineOptionalFields) SetSubsystemNil(b bool)`

 SetSubsystemNil sets the value for Subsystem to be an explicit nil

### UnsetSubsystem
`func (o *SwBaselineOptionalFields) UnsetSubsystem()`

UnsetSubsystem ensures that no value is present for Subsystem, not even an explicit nil
### GetNetwork

`func (o *SwBaselineOptionalFields) GetNetwork() string`

GetNetwork returns the Network field if non-nil, zero value otherwise.

### GetNetworkOk

`func (o *SwBaselineOptionalFields) GetNetworkOk() (*string, bool)`

GetNetworkOk returns a tuple with the Network field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNetwork

`func (o *SwBaselineOptionalFields) SetNetwork(v string)`

SetNetwork sets Network field to given value.

### HasNetwork

`func (o *SwBaselineOptionalFields) HasNetwork() bool`

HasNetwork returns a boolean if a field has been set.

### SetNetworkNil

`func (o *SwBaselineOptionalFields) SetNetworkNil(b bool)`

 SetNetworkNil sets the value for Network to be an explicit nil

### UnsetNetwork
`func (o *SwBaselineOptionalFields) UnsetNetwork()`

UnsetNetwork ensures that no value is present for Network, not even an explicit nil
### GetHostingEnvironment

`func (o *SwBaselineOptionalFields) GetHostingEnvironment() string`

GetHostingEnvironment returns the HostingEnvironment field if non-nil, zero value otherwise.

### GetHostingEnvironmentOk

`func (o *SwBaselineOptionalFields) GetHostingEnvironmentOk() (*string, bool)`

GetHostingEnvironmentOk returns a tuple with the HostingEnvironment field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHostingEnvironment

`func (o *SwBaselineOptionalFields) SetHostingEnvironment(v string)`

SetHostingEnvironment sets HostingEnvironment field to given value.

### HasHostingEnvironment

`func (o *SwBaselineOptionalFields) HasHostingEnvironment() bool`

HasHostingEnvironment returns a boolean if a field has been set.

### SetHostingEnvironmentNil

`func (o *SwBaselineOptionalFields) SetHostingEnvironmentNil(b bool)`

 SetHostingEnvironmentNil sets the value for HostingEnvironment to be an explicit nil

### UnsetHostingEnvironment
`func (o *SwBaselineOptionalFields) UnsetHostingEnvironment()`

UnsetHostingEnvironment ensures that no value is present for HostingEnvironment, not even an explicit nil
### GetSoftwareDependencies

`func (o *SwBaselineOptionalFields) GetSoftwareDependencies() string`

GetSoftwareDependencies returns the SoftwareDependencies field if non-nil, zero value otherwise.

### GetSoftwareDependenciesOk

`func (o *SwBaselineOptionalFields) GetSoftwareDependenciesOk() (*string, bool)`

GetSoftwareDependenciesOk returns a tuple with the SoftwareDependencies field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSoftwareDependencies

`func (o *SwBaselineOptionalFields) SetSoftwareDependencies(v string)`

SetSoftwareDependencies sets SoftwareDependencies field to given value.

### HasSoftwareDependencies

`func (o *SwBaselineOptionalFields) HasSoftwareDependencies() bool`

HasSoftwareDependencies returns a boolean if a field has been set.

### SetSoftwareDependenciesNil

`func (o *SwBaselineOptionalFields) SetSoftwareDependenciesNil(b bool)`

 SetSoftwareDependenciesNil sets the value for SoftwareDependencies to be an explicit nil

### UnsetSoftwareDependencies
`func (o *SwBaselineOptionalFields) UnsetSoftwareDependencies()`

UnsetSoftwareDependencies ensures that no value is present for SoftwareDependencies, not even an explicit nil
### GetCryptographicHash

`func (o *SwBaselineOptionalFields) GetCryptographicHash() string`

GetCryptographicHash returns the CryptographicHash field if non-nil, zero value otherwise.

### GetCryptographicHashOk

`func (o *SwBaselineOptionalFields) GetCryptographicHashOk() (*string, bool)`

GetCryptographicHashOk returns a tuple with the CryptographicHash field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCryptographicHash

`func (o *SwBaselineOptionalFields) SetCryptographicHash(v string)`

SetCryptographicHash sets CryptographicHash field to given value.

### HasCryptographicHash

`func (o *SwBaselineOptionalFields) HasCryptographicHash() bool`

HasCryptographicHash returns a boolean if a field has been set.

### SetCryptographicHashNil

`func (o *SwBaselineOptionalFields) SetCryptographicHashNil(b bool)`

 SetCryptographicHashNil sets the value for CryptographicHash to be an explicit nil

### UnsetCryptographicHash
`func (o *SwBaselineOptionalFields) UnsetCryptographicHash()`

UnsetCryptographicHash ensures that no value is present for CryptographicHash, not even an explicit nil
### GetInServiceData

`func (o *SwBaselineOptionalFields) GetInServiceData() string`

GetInServiceData returns the InServiceData field if non-nil, zero value otherwise.

### GetInServiceDataOk

`func (o *SwBaselineOptionalFields) GetInServiceDataOk() (*string, bool)`

GetInServiceDataOk returns a tuple with the InServiceData field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetInServiceData

`func (o *SwBaselineOptionalFields) SetInServiceData(v string)`

SetInServiceData sets InServiceData field to given value.

### HasInServiceData

`func (o *SwBaselineOptionalFields) HasInServiceData() bool`

HasInServiceData returns a boolean if a field has been set.

### SetInServiceDataNil

`func (o *SwBaselineOptionalFields) SetInServiceDataNil(b bool)`

 SetInServiceDataNil sets the value for InServiceData to be an explicit nil

### UnsetInServiceData
`func (o *SwBaselineOptionalFields) UnsetInServiceData()`

UnsetInServiceData ensures that no value is present for InServiceData, not even an explicit nil
### GetItBudgetUii

`func (o *SwBaselineOptionalFields) GetItBudgetUii() string`

GetItBudgetUii returns the ItBudgetUii field if non-nil, zero value otherwise.

### GetItBudgetUiiOk

`func (o *SwBaselineOptionalFields) GetItBudgetUiiOk() (*string, bool)`

GetItBudgetUiiOk returns a tuple with the ItBudgetUii field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItBudgetUii

`func (o *SwBaselineOptionalFields) SetItBudgetUii(v string)`

SetItBudgetUii sets ItBudgetUii field to given value.

### HasItBudgetUii

`func (o *SwBaselineOptionalFields) HasItBudgetUii() bool`

HasItBudgetUii returns a boolean if a field has been set.

### SetItBudgetUiiNil

`func (o *SwBaselineOptionalFields) SetItBudgetUiiNil(b bool)`

 SetItBudgetUiiNil sets the value for ItBudgetUii to be an explicit nil

### UnsetItBudgetUii
`func (o *SwBaselineOptionalFields) UnsetItBudgetUii()`

UnsetItBudgetUii ensures that no value is present for ItBudgetUii, not even an explicit nil
### GetFiscalYear

`func (o *SwBaselineOptionalFields) GetFiscalYear() string`

GetFiscalYear returns the FiscalYear field if non-nil, zero value otherwise.

### GetFiscalYearOk

`func (o *SwBaselineOptionalFields) GetFiscalYearOk() (*string, bool)`

GetFiscalYearOk returns a tuple with the FiscalYear field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFiscalYear

`func (o *SwBaselineOptionalFields) SetFiscalYear(v string)`

SetFiscalYear sets FiscalYear field to given value.

### HasFiscalYear

`func (o *SwBaselineOptionalFields) HasFiscalYear() bool`

HasFiscalYear returns a boolean if a field has been set.

### SetFiscalYearNil

`func (o *SwBaselineOptionalFields) SetFiscalYearNil(b bool)`

 SetFiscalYearNil sets the value for FiscalYear to be an explicit nil

### UnsetFiscalYear
`func (o *SwBaselineOptionalFields) UnsetFiscalYear()`

UnsetFiscalYear ensures that no value is present for FiscalYear, not even an explicit nil
### GetPopEndDate

`func (o *SwBaselineOptionalFields) GetPopEndDate() int64`

GetPopEndDate returns the PopEndDate field if non-nil, zero value otherwise.

### GetPopEndDateOk

`func (o *SwBaselineOptionalFields) GetPopEndDateOk() (*int64, bool)`

GetPopEndDateOk returns a tuple with the PopEndDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPopEndDate

`func (o *SwBaselineOptionalFields) SetPopEndDate(v int64)`

SetPopEndDate sets PopEndDate field to given value.

### HasPopEndDate

`func (o *SwBaselineOptionalFields) HasPopEndDate() bool`

HasPopEndDate returns a boolean if a field has been set.

### SetPopEndDateNil

`func (o *SwBaselineOptionalFields) SetPopEndDateNil(b bool)`

 SetPopEndDateNil sets the value for PopEndDate to be an explicit nil

### UnsetPopEndDate
`func (o *SwBaselineOptionalFields) UnsetPopEndDate()`

UnsetPopEndDate ensures that no value is present for PopEndDate, not even an explicit nil
### GetLicenseOrContract

`func (o *SwBaselineOptionalFields) GetLicenseOrContract() string`

GetLicenseOrContract returns the LicenseOrContract field if non-nil, zero value otherwise.

### GetLicenseOrContractOk

`func (o *SwBaselineOptionalFields) GetLicenseOrContractOk() (*string, bool)`

GetLicenseOrContractOk returns a tuple with the LicenseOrContract field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLicenseOrContract

`func (o *SwBaselineOptionalFields) SetLicenseOrContract(v string)`

SetLicenseOrContract sets LicenseOrContract field to given value.

### HasLicenseOrContract

`func (o *SwBaselineOptionalFields) HasLicenseOrContract() bool`

HasLicenseOrContract returns a boolean if a field has been set.

### SetLicenseOrContractNil

`func (o *SwBaselineOptionalFields) SetLicenseOrContractNil(b bool)`

 SetLicenseOrContractNil sets the value for LicenseOrContract to be an explicit nil

### UnsetLicenseOrContract
`func (o *SwBaselineOptionalFields) UnsetLicenseOrContract()`

UnsetLicenseOrContract ensures that no value is present for LicenseOrContract, not even an explicit nil
### GetLicenseTerm

`func (o *SwBaselineOptionalFields) GetLicenseTerm() string`

GetLicenseTerm returns the LicenseTerm field if non-nil, zero value otherwise.

### GetLicenseTermOk

`func (o *SwBaselineOptionalFields) GetLicenseTermOk() (*string, bool)`

GetLicenseTermOk returns a tuple with the LicenseTerm field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLicenseTerm

`func (o *SwBaselineOptionalFields) SetLicenseTerm(v string)`

SetLicenseTerm sets LicenseTerm field to given value.

### HasLicenseTerm

`func (o *SwBaselineOptionalFields) HasLicenseTerm() bool`

HasLicenseTerm returns a boolean if a field has been set.

### SetLicenseTermNil

`func (o *SwBaselineOptionalFields) SetLicenseTermNil(b bool)`

 SetLicenseTermNil sets the value for LicenseTerm to be an explicit nil

### UnsetLicenseTerm
`func (o *SwBaselineOptionalFields) UnsetLicenseTerm()`

UnsetLicenseTerm ensures that no value is present for LicenseTerm, not even an explicit nil
### GetCostPerLicense

`func (o *SwBaselineOptionalFields) GetCostPerLicense() float64`

GetCostPerLicense returns the CostPerLicense field if non-nil, zero value otherwise.

### GetCostPerLicenseOk

`func (o *SwBaselineOptionalFields) GetCostPerLicenseOk() (*float64, bool)`

GetCostPerLicenseOk returns a tuple with the CostPerLicense field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCostPerLicense

`func (o *SwBaselineOptionalFields) SetCostPerLicense(v float64)`

SetCostPerLicense sets CostPerLicense field to given value.

### HasCostPerLicense

`func (o *SwBaselineOptionalFields) HasCostPerLicense() bool`

HasCostPerLicense returns a boolean if a field has been set.

### SetCostPerLicenseNil

`func (o *SwBaselineOptionalFields) SetCostPerLicenseNil(b bool)`

 SetCostPerLicenseNil sets the value for CostPerLicense to be an explicit nil

### UnsetCostPerLicense
`func (o *SwBaselineOptionalFields) UnsetCostPerLicense()`

UnsetCostPerLicense ensures that no value is present for CostPerLicense, not even an explicit nil
### GetTotalLicenses

`func (o *SwBaselineOptionalFields) GetTotalLicenses() int64`

GetTotalLicenses returns the TotalLicenses field if non-nil, zero value otherwise.

### GetTotalLicensesOk

`func (o *SwBaselineOptionalFields) GetTotalLicensesOk() (*int64, bool)`

GetTotalLicensesOk returns a tuple with the TotalLicenses field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotalLicenses

`func (o *SwBaselineOptionalFields) SetTotalLicenses(v int64)`

SetTotalLicenses sets TotalLicenses field to given value.

### HasTotalLicenses

`func (o *SwBaselineOptionalFields) HasTotalLicenses() bool`

HasTotalLicenses returns a boolean if a field has been set.

### SetTotalLicensesNil

`func (o *SwBaselineOptionalFields) SetTotalLicensesNil(b bool)`

 SetTotalLicensesNil sets the value for TotalLicenses to be an explicit nil

### UnsetTotalLicenses
`func (o *SwBaselineOptionalFields) UnsetTotalLicenses()`

UnsetTotalLicenses ensures that no value is present for TotalLicenses, not even an explicit nil
### GetTotalLicenseCost

`func (o *SwBaselineOptionalFields) GetTotalLicenseCost() float64`

GetTotalLicenseCost returns the TotalLicenseCost field if non-nil, zero value otherwise.

### GetTotalLicenseCostOk

`func (o *SwBaselineOptionalFields) GetTotalLicenseCostOk() (*float64, bool)`

GetTotalLicenseCostOk returns a tuple with the TotalLicenseCost field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotalLicenseCost

`func (o *SwBaselineOptionalFields) SetTotalLicenseCost(v float64)`

SetTotalLicenseCost sets TotalLicenseCost field to given value.

### HasTotalLicenseCost

`func (o *SwBaselineOptionalFields) HasTotalLicenseCost() bool`

HasTotalLicenseCost returns a boolean if a field has been set.

### SetTotalLicenseCostNil

`func (o *SwBaselineOptionalFields) SetTotalLicenseCostNil(b bool)`

 SetTotalLicenseCostNil sets the value for TotalLicenseCost to be an explicit nil

### UnsetTotalLicenseCost
`func (o *SwBaselineOptionalFields) UnsetTotalLicenseCost()`

UnsetTotalLicenseCost ensures that no value is present for TotalLicenseCost, not even an explicit nil
### GetLicensesUsed

`func (o *SwBaselineOptionalFields) GetLicensesUsed() int64`

GetLicensesUsed returns the LicensesUsed field if non-nil, zero value otherwise.

### GetLicensesUsedOk

`func (o *SwBaselineOptionalFields) GetLicensesUsedOk() (*int64, bool)`

GetLicensesUsedOk returns a tuple with the LicensesUsed field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLicensesUsed

`func (o *SwBaselineOptionalFields) SetLicensesUsed(v int64)`

SetLicensesUsed sets LicensesUsed field to given value.

### HasLicensesUsed

`func (o *SwBaselineOptionalFields) HasLicensesUsed() bool`

HasLicensesUsed returns a boolean if a field has been set.

### SetLicensesUsedNil

`func (o *SwBaselineOptionalFields) SetLicensesUsedNil(b bool)`

 SetLicensesUsedNil sets the value for LicensesUsed to be an explicit nil

### UnsetLicensesUsed
`func (o *SwBaselineOptionalFields) UnsetLicensesUsed()`

UnsetLicensesUsed ensures that no value is present for LicensesUsed, not even an explicit nil
### GetLicensePoc

`func (o *SwBaselineOptionalFields) GetLicensePoc() string`

GetLicensePoc returns the LicensePoc field if non-nil, zero value otherwise.

### GetLicensePocOk

`func (o *SwBaselineOptionalFields) GetLicensePocOk() (*string, bool)`

GetLicensePocOk returns a tuple with the LicensePoc field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLicensePoc

`func (o *SwBaselineOptionalFields) SetLicensePoc(v string)`

SetLicensePoc sets LicensePoc field to given value.

### HasLicensePoc

`func (o *SwBaselineOptionalFields) HasLicensePoc() bool`

HasLicensePoc returns a boolean if a field has been set.

### SetLicensePocNil

`func (o *SwBaselineOptionalFields) SetLicensePocNil(b bool)`

 SetLicensePocNil sets the value for LicensePoc to be an explicit nil

### UnsetLicensePoc
`func (o *SwBaselineOptionalFields) UnsetLicensePoc()`

UnsetLicensePoc ensures that no value is present for LicensePoc, not even an explicit nil
### GetLicenseRenewalDate

`func (o *SwBaselineOptionalFields) GetLicenseRenewalDate() int64`

GetLicenseRenewalDate returns the LicenseRenewalDate field if non-nil, zero value otherwise.

### GetLicenseRenewalDateOk

`func (o *SwBaselineOptionalFields) GetLicenseRenewalDateOk() (*int64, bool)`

GetLicenseRenewalDateOk returns a tuple with the LicenseRenewalDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLicenseRenewalDate

`func (o *SwBaselineOptionalFields) SetLicenseRenewalDate(v int64)`

SetLicenseRenewalDate sets LicenseRenewalDate field to given value.

### HasLicenseRenewalDate

`func (o *SwBaselineOptionalFields) HasLicenseRenewalDate() bool`

HasLicenseRenewalDate returns a boolean if a field has been set.

### SetLicenseRenewalDateNil

`func (o *SwBaselineOptionalFields) SetLicenseRenewalDateNil(b bool)`

 SetLicenseRenewalDateNil sets the value for LicenseRenewalDate to be an explicit nil

### UnsetLicenseRenewalDate
`func (o *SwBaselineOptionalFields) UnsetLicenseRenewalDate()`

UnsetLicenseRenewalDate ensures that no value is present for LicenseRenewalDate, not even an explicit nil
### GetLicenseExpirationDate

`func (o *SwBaselineOptionalFields) GetLicenseExpirationDate() int64`

GetLicenseExpirationDate returns the LicenseExpirationDate field if non-nil, zero value otherwise.

### GetLicenseExpirationDateOk

`func (o *SwBaselineOptionalFields) GetLicenseExpirationDateOk() (*int64, bool)`

GetLicenseExpirationDateOk returns a tuple with the LicenseExpirationDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLicenseExpirationDate

`func (o *SwBaselineOptionalFields) SetLicenseExpirationDate(v int64)`

SetLicenseExpirationDate sets LicenseExpirationDate field to given value.

### HasLicenseExpirationDate

`func (o *SwBaselineOptionalFields) HasLicenseExpirationDate() bool`

HasLicenseExpirationDate returns a boolean if a field has been set.

### SetLicenseExpirationDateNil

`func (o *SwBaselineOptionalFields) SetLicenseExpirationDateNil(b bool)`

 SetLicenseExpirationDateNil sets the value for LicenseExpirationDate to be an explicit nil

### UnsetLicenseExpirationDate
`func (o *SwBaselineOptionalFields) UnsetLicenseExpirationDate()`

UnsetLicenseExpirationDate ensures that no value is present for LicenseExpirationDate, not even an explicit nil
### GetApprovalStatus

`func (o *SwBaselineOptionalFields) GetApprovalStatus() string`

GetApprovalStatus returns the ApprovalStatus field if non-nil, zero value otherwise.

### GetApprovalStatusOk

`func (o *SwBaselineOptionalFields) GetApprovalStatusOk() (*string, bool)`

GetApprovalStatusOk returns a tuple with the ApprovalStatus field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetApprovalStatus

`func (o *SwBaselineOptionalFields) SetApprovalStatus(v string)`

SetApprovalStatus sets ApprovalStatus field to given value.

### HasApprovalStatus

`func (o *SwBaselineOptionalFields) HasApprovalStatus() bool`

HasApprovalStatus returns a boolean if a field has been set.

### SetApprovalStatusNil

`func (o *SwBaselineOptionalFields) SetApprovalStatusNil(b bool)`

 SetApprovalStatusNil sets the value for ApprovalStatus to be an explicit nil

### UnsetApprovalStatus
`func (o *SwBaselineOptionalFields) UnsetApprovalStatus()`

UnsetApprovalStatus ensures that no value is present for ApprovalStatus, not even an explicit nil
### GetReleaseDate

`func (o *SwBaselineOptionalFields) GetReleaseDate() int64`

GetReleaseDate returns the ReleaseDate field if non-nil, zero value otherwise.

### GetReleaseDateOk

`func (o *SwBaselineOptionalFields) GetReleaseDateOk() (*int64, bool)`

GetReleaseDateOk returns a tuple with the ReleaseDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetReleaseDate

`func (o *SwBaselineOptionalFields) SetReleaseDate(v int64)`

SetReleaseDate sets ReleaseDate field to given value.

### HasReleaseDate

`func (o *SwBaselineOptionalFields) HasReleaseDate() bool`

HasReleaseDate returns a boolean if a field has been set.

### SetReleaseDateNil

`func (o *SwBaselineOptionalFields) SetReleaseDateNil(b bool)`

 SetReleaseDateNil sets the value for ReleaseDate to be an explicit nil

### UnsetReleaseDate
`func (o *SwBaselineOptionalFields) UnsetReleaseDate()`

UnsetReleaseDate ensures that no value is present for ReleaseDate, not even an explicit nil
### GetMaintenanceDate

`func (o *SwBaselineOptionalFields) GetMaintenanceDate() int64`

GetMaintenanceDate returns the MaintenanceDate field if non-nil, zero value otherwise.

### GetMaintenanceDateOk

`func (o *SwBaselineOptionalFields) GetMaintenanceDateOk() (*int64, bool)`

GetMaintenanceDateOk returns a tuple with the MaintenanceDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMaintenanceDate

`func (o *SwBaselineOptionalFields) SetMaintenanceDate(v int64)`

SetMaintenanceDate sets MaintenanceDate field to given value.

### HasMaintenanceDate

`func (o *SwBaselineOptionalFields) HasMaintenanceDate() bool`

HasMaintenanceDate returns a boolean if a field has been set.

### SetMaintenanceDateNil

`func (o *SwBaselineOptionalFields) SetMaintenanceDateNil(b bool)`

 SetMaintenanceDateNil sets the value for MaintenanceDate to be an explicit nil

### UnsetMaintenanceDate
`func (o *SwBaselineOptionalFields) UnsetMaintenanceDate()`

UnsetMaintenanceDate ensures that no value is present for MaintenanceDate, not even an explicit nil
### GetRetirementDate

`func (o *SwBaselineOptionalFields) GetRetirementDate() int64`

GetRetirementDate returns the RetirementDate field if non-nil, zero value otherwise.

### GetRetirementDateOk

`func (o *SwBaselineOptionalFields) GetRetirementDateOk() (*int64, bool)`

GetRetirementDateOk returns a tuple with the RetirementDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRetirementDate

`func (o *SwBaselineOptionalFields) SetRetirementDate(v int64)`

SetRetirementDate sets RetirementDate field to given value.

### HasRetirementDate

`func (o *SwBaselineOptionalFields) HasRetirementDate() bool`

HasRetirementDate returns a boolean if a field has been set.

### SetRetirementDateNil

`func (o *SwBaselineOptionalFields) SetRetirementDateNil(b bool)`

 SetRetirementDateNil sets the value for RetirementDate to be an explicit nil

### UnsetRetirementDate
`func (o *SwBaselineOptionalFields) UnsetRetirementDate()`

UnsetRetirementDate ensures that no value is present for RetirementDate, not even an explicit nil
### GetEndOfLifeSupportDate

`func (o *SwBaselineOptionalFields) GetEndOfLifeSupportDate() int64`

GetEndOfLifeSupportDate returns the EndOfLifeSupportDate field if non-nil, zero value otherwise.

### GetEndOfLifeSupportDateOk

`func (o *SwBaselineOptionalFields) GetEndOfLifeSupportDateOk() (*int64, bool)`

GetEndOfLifeSupportDateOk returns a tuple with the EndOfLifeSupportDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEndOfLifeSupportDate

`func (o *SwBaselineOptionalFields) SetEndOfLifeSupportDate(v int64)`

SetEndOfLifeSupportDate sets EndOfLifeSupportDate field to given value.

### HasEndOfLifeSupportDate

`func (o *SwBaselineOptionalFields) HasEndOfLifeSupportDate() bool`

HasEndOfLifeSupportDate returns a boolean if a field has been set.

### SetEndOfLifeSupportDateNil

`func (o *SwBaselineOptionalFields) SetEndOfLifeSupportDateNil(b bool)`

 SetEndOfLifeSupportDateNil sets the value for EndOfLifeSupportDate to be an explicit nil

### UnsetEndOfLifeSupportDate
`func (o *SwBaselineOptionalFields) UnsetEndOfLifeSupportDate()`

UnsetEndOfLifeSupportDate ensures that no value is present for EndOfLifeSupportDate, not even an explicit nil
### GetExtendedEndOfLifeSupportDate

`func (o *SwBaselineOptionalFields) GetExtendedEndOfLifeSupportDate() int64`

GetExtendedEndOfLifeSupportDate returns the ExtendedEndOfLifeSupportDate field if non-nil, zero value otherwise.

### GetExtendedEndOfLifeSupportDateOk

`func (o *SwBaselineOptionalFields) GetExtendedEndOfLifeSupportDateOk() (*int64, bool)`

GetExtendedEndOfLifeSupportDateOk returns a tuple with the ExtendedEndOfLifeSupportDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExtendedEndOfLifeSupportDate

`func (o *SwBaselineOptionalFields) SetExtendedEndOfLifeSupportDate(v int64)`

SetExtendedEndOfLifeSupportDate sets ExtendedEndOfLifeSupportDate field to given value.

### HasExtendedEndOfLifeSupportDate

`func (o *SwBaselineOptionalFields) HasExtendedEndOfLifeSupportDate() bool`

HasExtendedEndOfLifeSupportDate returns a boolean if a field has been set.

### SetExtendedEndOfLifeSupportDateNil

`func (o *SwBaselineOptionalFields) SetExtendedEndOfLifeSupportDateNil(b bool)`

 SetExtendedEndOfLifeSupportDateNil sets the value for ExtendedEndOfLifeSupportDate to be an explicit nil

### UnsetExtendedEndOfLifeSupportDate
`func (o *SwBaselineOptionalFields) UnsetExtendedEndOfLifeSupportDate()`

UnsetExtendedEndOfLifeSupportDate ensures that no value is present for ExtendedEndOfLifeSupportDate, not even an explicit nil
### GetCriticalAsset

`func (o *SwBaselineOptionalFields) GetCriticalAsset() bool`

GetCriticalAsset returns the CriticalAsset field if non-nil, zero value otherwise.

### GetCriticalAssetOk

`func (o *SwBaselineOptionalFields) GetCriticalAssetOk() (*bool, bool)`

GetCriticalAssetOk returns a tuple with the CriticalAsset field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCriticalAsset

`func (o *SwBaselineOptionalFields) SetCriticalAsset(v bool)`

SetCriticalAsset sets CriticalAsset field to given value.

### HasCriticalAsset

`func (o *SwBaselineOptionalFields) HasCriticalAsset() bool`

HasCriticalAsset returns a boolean if a field has been set.

### SetCriticalAssetNil

`func (o *SwBaselineOptionalFields) SetCriticalAssetNil(b bool)`

 SetCriticalAssetNil sets the value for CriticalAsset to be an explicit nil

### UnsetCriticalAsset
`func (o *SwBaselineOptionalFields) UnsetCriticalAsset()`

UnsetCriticalAsset ensures that no value is present for CriticalAsset, not even an explicit nil
### GetLocation

`func (o *SwBaselineOptionalFields) GetLocation() string`

GetLocation returns the Location field if non-nil, zero value otherwise.

### GetLocationOk

`func (o *SwBaselineOptionalFields) GetLocationOk() (*string, bool)`

GetLocationOk returns a tuple with the Location field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLocation

`func (o *SwBaselineOptionalFields) SetLocation(v string)`

SetLocation sets Location field to given value.

### HasLocation

`func (o *SwBaselineOptionalFields) HasLocation() bool`

HasLocation returns a boolean if a field has been set.

### SetLocationNil

`func (o *SwBaselineOptionalFields) SetLocationNil(b bool)`

 SetLocationNil sets the value for Location to be an explicit nil

### UnsetLocation
`func (o *SwBaselineOptionalFields) UnsetLocation()`

UnsetLocation ensures that no value is present for Location, not even an explicit nil
### GetPurpose

`func (o *SwBaselineOptionalFields) GetPurpose() string`

GetPurpose returns the Purpose field if non-nil, zero value otherwise.

### GetPurposeOk

`func (o *SwBaselineOptionalFields) GetPurposeOk() (*string, bool)`

GetPurposeOk returns a tuple with the Purpose field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPurpose

`func (o *SwBaselineOptionalFields) SetPurpose(v string)`

SetPurpose sets Purpose field to given value.

### HasPurpose

`func (o *SwBaselineOptionalFields) HasPurpose() bool`

HasPurpose returns a boolean if a field has been set.

### SetPurposeNil

`func (o *SwBaselineOptionalFields) SetPurposeNil(b bool)`

 SetPurposeNil sets the value for Purpose to be an explicit nil

### UnsetPurpose
`func (o *SwBaselineOptionalFields) UnsetPurpose()`

UnsetPurpose ensures that no value is present for Purpose, not even an explicit nil
### GetUnsupportedOperatingSystem

`func (o *SwBaselineOptionalFields) GetUnsupportedOperatingSystem() bool`

GetUnsupportedOperatingSystem returns the UnsupportedOperatingSystem field if non-nil, zero value otherwise.

### GetUnsupportedOperatingSystemOk

`func (o *SwBaselineOptionalFields) GetUnsupportedOperatingSystemOk() (*bool, bool)`

GetUnsupportedOperatingSystemOk returns a tuple with the UnsupportedOperatingSystem field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUnsupportedOperatingSystem

`func (o *SwBaselineOptionalFields) SetUnsupportedOperatingSystem(v bool)`

SetUnsupportedOperatingSystem sets UnsupportedOperatingSystem field to given value.

### HasUnsupportedOperatingSystem

`func (o *SwBaselineOptionalFields) HasUnsupportedOperatingSystem() bool`

HasUnsupportedOperatingSystem returns a boolean if a field has been set.

### SetUnsupportedOperatingSystemNil

`func (o *SwBaselineOptionalFields) SetUnsupportedOperatingSystemNil(b bool)`

 SetUnsupportedOperatingSystemNil sets the value for UnsupportedOperatingSystem to be an explicit nil

### UnsetUnsupportedOperatingSystem
`func (o *SwBaselineOptionalFields) UnsetUnsupportedOperatingSystem()`

UnsetUnsupportedOperatingSystem ensures that no value is present for UnsupportedOperatingSystem, not even an explicit nil
### GetUnapprovedSoftwareFromTrm

`func (o *SwBaselineOptionalFields) GetUnapprovedSoftwareFromTrm() bool`

GetUnapprovedSoftwareFromTrm returns the UnapprovedSoftwareFromTrm field if non-nil, zero value otherwise.

### GetUnapprovedSoftwareFromTrmOk

`func (o *SwBaselineOptionalFields) GetUnapprovedSoftwareFromTrmOk() (*bool, bool)`

GetUnapprovedSoftwareFromTrmOk returns a tuple with the UnapprovedSoftwareFromTrm field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUnapprovedSoftwareFromTrm

`func (o *SwBaselineOptionalFields) SetUnapprovedSoftwareFromTrm(v bool)`

SetUnapprovedSoftwareFromTrm sets UnapprovedSoftwareFromTrm field to given value.

### HasUnapprovedSoftwareFromTrm

`func (o *SwBaselineOptionalFields) HasUnapprovedSoftwareFromTrm() bool`

HasUnapprovedSoftwareFromTrm returns a boolean if a field has been set.

### SetUnapprovedSoftwareFromTrmNil

`func (o *SwBaselineOptionalFields) SetUnapprovedSoftwareFromTrmNil(b bool)`

 SetUnapprovedSoftwareFromTrmNil sets the value for UnapprovedSoftwareFromTrm to be an explicit nil

### UnsetUnapprovedSoftwareFromTrm
`func (o *SwBaselineOptionalFields) UnsetUnapprovedSoftwareFromTrm()`

UnsetUnapprovedSoftwareFromTrm ensures that no value is present for UnapprovedSoftwareFromTrm, not even an explicit nil
### GetApprovedWaiver

`func (o *SwBaselineOptionalFields) GetApprovedWaiver() bool`

GetApprovedWaiver returns the ApprovedWaiver field if non-nil, zero value otherwise.

### GetApprovedWaiverOk

`func (o *SwBaselineOptionalFields) GetApprovedWaiverOk() (*bool, bool)`

GetApprovedWaiverOk returns a tuple with the ApprovedWaiver field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetApprovedWaiver

`func (o *SwBaselineOptionalFields) SetApprovedWaiver(v bool)`

SetApprovedWaiver sets ApprovedWaiver field to given value.

### HasApprovedWaiver

`func (o *SwBaselineOptionalFields) HasApprovedWaiver() bool`

HasApprovedWaiver returns a boolean if a field has been set.

### SetApprovedWaiverNil

`func (o *SwBaselineOptionalFields) SetApprovedWaiverNil(b bool)`

 SetApprovedWaiverNil sets the value for ApprovedWaiver to be an explicit nil

### UnsetApprovedWaiver
`func (o *SwBaselineOptionalFields) UnsetApprovedWaiver()`

UnsetApprovedWaiver ensures that no value is present for ApprovedWaiver, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


