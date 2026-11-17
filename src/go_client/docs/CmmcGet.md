# CmmcGet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Operation** | Pointer to **NullableString** | [Read-Only] Indicates the action that should be taken on the assessment record since the provided sinceDate. | [optional] 
**HqOrganizationName** | Pointer to **NullableString** | [Read-Only] The name of the DIB Company. | [optional] 
**Uei** | Pointer to **NullableString** | [Read-Only] The Unique Entity Identifier assigned to the DIB Company. | [optional] 
**OscName** | Pointer to **NullableString** | [Read-Only] The name of the Organization Seeking Certification. | [optional] 
**HighestLevelOwnerCageCode** | Pointer to **NullableString** | [Read-Only] Identifies the highest-level CAGE Code associated with a given organization. | [optional] 
**CageCodesInScope** | Pointer to **NullableString** | [Read-Only] The five position code(s) associated with the Organization Seeking Certification (OSC). | [optional] 
**NumberOfEmployees** | Pointer to **NullableInt64** | [Read-Only] The number of employees affiliated with the Organization Seeking Certification. | [optional] 
**Scope** | Pointer to **NullableString** | [Read-Only] The scope of the OSC assessment. | [optional] 
**ScopeDescription** | Pointer to **NullableString** | [Read-Only] Brief description of the scope of the OSC assessment | [optional] 
**AssessmentStandard** | Pointer to **NullableString** | [Read-Only] Version of the CMMC Model used as part of the assessment. | [optional] 
**AssessmentId** | Pointer to **NullableString** | [Read-Only] Unique identifier for the assessment/certificate. | [optional] 
**CmmcUid** | Pointer to **NullableString** | [Read-Only] Identifies the unique ID that is associated with a given CMMC certification for an organization. | [optional] 
**OverallScore** | Pointer to **int64** | [Read-Only] Identifies the overall calculated score for the assessment based on the assigned values to each applicable security requirement. | [optional] 
**CmmcStatus** | Pointer to **NullableString** | [Read-Only] The status of the CMMC certification. | [optional] 
**CmmcStatusDate** | Pointer to **NullableInt64** | [Read-Only] Date of the CMMC status. | [optional] 
**CmmcStatusExpirationDate** | Pointer to **NullableInt64** | [Read-Only] Expiration date of the CMMC status. | [optional] 

## Methods

### NewCmmcGet

`func NewCmmcGet() *CmmcGet`

NewCmmcGet instantiates a new CmmcGet object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCmmcGetWithDefaults

`func NewCmmcGetWithDefaults() *CmmcGet`

NewCmmcGetWithDefaults instantiates a new CmmcGet object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetOperation

`func (o *CmmcGet) GetOperation() string`

GetOperation returns the Operation field if non-nil, zero value otherwise.

### GetOperationOk

`func (o *CmmcGet) GetOperationOk() (*string, bool)`

GetOperationOk returns a tuple with the Operation field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOperation

`func (o *CmmcGet) SetOperation(v string)`

SetOperation sets Operation field to given value.

### HasOperation

`func (o *CmmcGet) HasOperation() bool`

HasOperation returns a boolean if a field has been set.

### SetOperationNil

`func (o *CmmcGet) SetOperationNil(b bool)`

 SetOperationNil sets the value for Operation to be an explicit nil

### UnsetOperation
`func (o *CmmcGet) UnsetOperation()`

UnsetOperation ensures that no value is present for Operation, not even an explicit nil
### GetHqOrganizationName

`func (o *CmmcGet) GetHqOrganizationName() string`

GetHqOrganizationName returns the HqOrganizationName field if non-nil, zero value otherwise.

### GetHqOrganizationNameOk

`func (o *CmmcGet) GetHqOrganizationNameOk() (*string, bool)`

GetHqOrganizationNameOk returns a tuple with the HqOrganizationName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHqOrganizationName

`func (o *CmmcGet) SetHqOrganizationName(v string)`

SetHqOrganizationName sets HqOrganizationName field to given value.

### HasHqOrganizationName

`func (o *CmmcGet) HasHqOrganizationName() bool`

HasHqOrganizationName returns a boolean if a field has been set.

### SetHqOrganizationNameNil

`func (o *CmmcGet) SetHqOrganizationNameNil(b bool)`

 SetHqOrganizationNameNil sets the value for HqOrganizationName to be an explicit nil

### UnsetHqOrganizationName
`func (o *CmmcGet) UnsetHqOrganizationName()`

UnsetHqOrganizationName ensures that no value is present for HqOrganizationName, not even an explicit nil
### GetUei

`func (o *CmmcGet) GetUei() string`

GetUei returns the Uei field if non-nil, zero value otherwise.

### GetUeiOk

`func (o *CmmcGet) GetUeiOk() (*string, bool)`

GetUeiOk returns a tuple with the Uei field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUei

`func (o *CmmcGet) SetUei(v string)`

SetUei sets Uei field to given value.

### HasUei

`func (o *CmmcGet) HasUei() bool`

HasUei returns a boolean if a field has been set.

### SetUeiNil

`func (o *CmmcGet) SetUeiNil(b bool)`

 SetUeiNil sets the value for Uei to be an explicit nil

### UnsetUei
`func (o *CmmcGet) UnsetUei()`

UnsetUei ensures that no value is present for Uei, not even an explicit nil
### GetOscName

`func (o *CmmcGet) GetOscName() string`

GetOscName returns the OscName field if non-nil, zero value otherwise.

### GetOscNameOk

`func (o *CmmcGet) GetOscNameOk() (*string, bool)`

GetOscNameOk returns a tuple with the OscName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOscName

`func (o *CmmcGet) SetOscName(v string)`

SetOscName sets OscName field to given value.

### HasOscName

`func (o *CmmcGet) HasOscName() bool`

HasOscName returns a boolean if a field has been set.

### SetOscNameNil

`func (o *CmmcGet) SetOscNameNil(b bool)`

 SetOscNameNil sets the value for OscName to be an explicit nil

### UnsetOscName
`func (o *CmmcGet) UnsetOscName()`

UnsetOscName ensures that no value is present for OscName, not even an explicit nil
### GetHighestLevelOwnerCageCode

`func (o *CmmcGet) GetHighestLevelOwnerCageCode() string`

GetHighestLevelOwnerCageCode returns the HighestLevelOwnerCageCode field if non-nil, zero value otherwise.

### GetHighestLevelOwnerCageCodeOk

`func (o *CmmcGet) GetHighestLevelOwnerCageCodeOk() (*string, bool)`

GetHighestLevelOwnerCageCodeOk returns a tuple with the HighestLevelOwnerCageCode field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHighestLevelOwnerCageCode

`func (o *CmmcGet) SetHighestLevelOwnerCageCode(v string)`

SetHighestLevelOwnerCageCode sets HighestLevelOwnerCageCode field to given value.

### HasHighestLevelOwnerCageCode

`func (o *CmmcGet) HasHighestLevelOwnerCageCode() bool`

HasHighestLevelOwnerCageCode returns a boolean if a field has been set.

### SetHighestLevelOwnerCageCodeNil

`func (o *CmmcGet) SetHighestLevelOwnerCageCodeNil(b bool)`

 SetHighestLevelOwnerCageCodeNil sets the value for HighestLevelOwnerCageCode to be an explicit nil

### UnsetHighestLevelOwnerCageCode
`func (o *CmmcGet) UnsetHighestLevelOwnerCageCode()`

UnsetHighestLevelOwnerCageCode ensures that no value is present for HighestLevelOwnerCageCode, not even an explicit nil
### GetCageCodesInScope

`func (o *CmmcGet) GetCageCodesInScope() string`

GetCageCodesInScope returns the CageCodesInScope field if non-nil, zero value otherwise.

### GetCageCodesInScopeOk

`func (o *CmmcGet) GetCageCodesInScopeOk() (*string, bool)`

GetCageCodesInScopeOk returns a tuple with the CageCodesInScope field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCageCodesInScope

`func (o *CmmcGet) SetCageCodesInScope(v string)`

SetCageCodesInScope sets CageCodesInScope field to given value.

### HasCageCodesInScope

`func (o *CmmcGet) HasCageCodesInScope() bool`

HasCageCodesInScope returns a boolean if a field has been set.

### SetCageCodesInScopeNil

`func (o *CmmcGet) SetCageCodesInScopeNil(b bool)`

 SetCageCodesInScopeNil sets the value for CageCodesInScope to be an explicit nil

### UnsetCageCodesInScope
`func (o *CmmcGet) UnsetCageCodesInScope()`

UnsetCageCodesInScope ensures that no value is present for CageCodesInScope, not even an explicit nil
### GetNumberOfEmployees

`func (o *CmmcGet) GetNumberOfEmployees() int64`

GetNumberOfEmployees returns the NumberOfEmployees field if non-nil, zero value otherwise.

### GetNumberOfEmployeesOk

`func (o *CmmcGet) GetNumberOfEmployeesOk() (*int64, bool)`

GetNumberOfEmployeesOk returns a tuple with the NumberOfEmployees field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNumberOfEmployees

`func (o *CmmcGet) SetNumberOfEmployees(v int64)`

SetNumberOfEmployees sets NumberOfEmployees field to given value.

### HasNumberOfEmployees

`func (o *CmmcGet) HasNumberOfEmployees() bool`

HasNumberOfEmployees returns a boolean if a field has been set.

### SetNumberOfEmployeesNil

`func (o *CmmcGet) SetNumberOfEmployeesNil(b bool)`

 SetNumberOfEmployeesNil sets the value for NumberOfEmployees to be an explicit nil

### UnsetNumberOfEmployees
`func (o *CmmcGet) UnsetNumberOfEmployees()`

UnsetNumberOfEmployees ensures that no value is present for NumberOfEmployees, not even an explicit nil
### GetScope

`func (o *CmmcGet) GetScope() string`

GetScope returns the Scope field if non-nil, zero value otherwise.

### GetScopeOk

`func (o *CmmcGet) GetScopeOk() (*string, bool)`

GetScopeOk returns a tuple with the Scope field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetScope

`func (o *CmmcGet) SetScope(v string)`

SetScope sets Scope field to given value.

### HasScope

`func (o *CmmcGet) HasScope() bool`

HasScope returns a boolean if a field has been set.

### SetScopeNil

`func (o *CmmcGet) SetScopeNil(b bool)`

 SetScopeNil sets the value for Scope to be an explicit nil

### UnsetScope
`func (o *CmmcGet) UnsetScope()`

UnsetScope ensures that no value is present for Scope, not even an explicit nil
### GetScopeDescription

`func (o *CmmcGet) GetScopeDescription() string`

GetScopeDescription returns the ScopeDescription field if non-nil, zero value otherwise.

### GetScopeDescriptionOk

`func (o *CmmcGet) GetScopeDescriptionOk() (*string, bool)`

GetScopeDescriptionOk returns a tuple with the ScopeDescription field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetScopeDescription

`func (o *CmmcGet) SetScopeDescription(v string)`

SetScopeDescription sets ScopeDescription field to given value.

### HasScopeDescription

`func (o *CmmcGet) HasScopeDescription() bool`

HasScopeDescription returns a boolean if a field has been set.

### SetScopeDescriptionNil

`func (o *CmmcGet) SetScopeDescriptionNil(b bool)`

 SetScopeDescriptionNil sets the value for ScopeDescription to be an explicit nil

### UnsetScopeDescription
`func (o *CmmcGet) UnsetScopeDescription()`

UnsetScopeDescription ensures that no value is present for ScopeDescription, not even an explicit nil
### GetAssessmentStandard

`func (o *CmmcGet) GetAssessmentStandard() string`

GetAssessmentStandard returns the AssessmentStandard field if non-nil, zero value otherwise.

### GetAssessmentStandardOk

`func (o *CmmcGet) GetAssessmentStandardOk() (*string, bool)`

GetAssessmentStandardOk returns a tuple with the AssessmentStandard field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAssessmentStandard

`func (o *CmmcGet) SetAssessmentStandard(v string)`

SetAssessmentStandard sets AssessmentStandard field to given value.

### HasAssessmentStandard

`func (o *CmmcGet) HasAssessmentStandard() bool`

HasAssessmentStandard returns a boolean if a field has been set.

### SetAssessmentStandardNil

`func (o *CmmcGet) SetAssessmentStandardNil(b bool)`

 SetAssessmentStandardNil sets the value for AssessmentStandard to be an explicit nil

### UnsetAssessmentStandard
`func (o *CmmcGet) UnsetAssessmentStandard()`

UnsetAssessmentStandard ensures that no value is present for AssessmentStandard, not even an explicit nil
### GetAssessmentId

`func (o *CmmcGet) GetAssessmentId() string`

GetAssessmentId returns the AssessmentId field if non-nil, zero value otherwise.

### GetAssessmentIdOk

`func (o *CmmcGet) GetAssessmentIdOk() (*string, bool)`

GetAssessmentIdOk returns a tuple with the AssessmentId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAssessmentId

`func (o *CmmcGet) SetAssessmentId(v string)`

SetAssessmentId sets AssessmentId field to given value.

### HasAssessmentId

`func (o *CmmcGet) HasAssessmentId() bool`

HasAssessmentId returns a boolean if a field has been set.

### SetAssessmentIdNil

`func (o *CmmcGet) SetAssessmentIdNil(b bool)`

 SetAssessmentIdNil sets the value for AssessmentId to be an explicit nil

### UnsetAssessmentId
`func (o *CmmcGet) UnsetAssessmentId()`

UnsetAssessmentId ensures that no value is present for AssessmentId, not even an explicit nil
### GetCmmcUid

`func (o *CmmcGet) GetCmmcUid() string`

GetCmmcUid returns the CmmcUid field if non-nil, zero value otherwise.

### GetCmmcUidOk

`func (o *CmmcGet) GetCmmcUidOk() (*string, bool)`

GetCmmcUidOk returns a tuple with the CmmcUid field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCmmcUid

`func (o *CmmcGet) SetCmmcUid(v string)`

SetCmmcUid sets CmmcUid field to given value.

### HasCmmcUid

`func (o *CmmcGet) HasCmmcUid() bool`

HasCmmcUid returns a boolean if a field has been set.

### SetCmmcUidNil

`func (o *CmmcGet) SetCmmcUidNil(b bool)`

 SetCmmcUidNil sets the value for CmmcUid to be an explicit nil

### UnsetCmmcUid
`func (o *CmmcGet) UnsetCmmcUid()`

UnsetCmmcUid ensures that no value is present for CmmcUid, not even an explicit nil
### GetOverallScore

`func (o *CmmcGet) GetOverallScore() int64`

GetOverallScore returns the OverallScore field if non-nil, zero value otherwise.

### GetOverallScoreOk

`func (o *CmmcGet) GetOverallScoreOk() (*int64, bool)`

GetOverallScoreOk returns a tuple with the OverallScore field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOverallScore

`func (o *CmmcGet) SetOverallScore(v int64)`

SetOverallScore sets OverallScore field to given value.

### HasOverallScore

`func (o *CmmcGet) HasOverallScore() bool`

HasOverallScore returns a boolean if a field has been set.

### GetCmmcStatus

`func (o *CmmcGet) GetCmmcStatus() string`

GetCmmcStatus returns the CmmcStatus field if non-nil, zero value otherwise.

### GetCmmcStatusOk

`func (o *CmmcGet) GetCmmcStatusOk() (*string, bool)`

GetCmmcStatusOk returns a tuple with the CmmcStatus field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCmmcStatus

`func (o *CmmcGet) SetCmmcStatus(v string)`

SetCmmcStatus sets CmmcStatus field to given value.

### HasCmmcStatus

`func (o *CmmcGet) HasCmmcStatus() bool`

HasCmmcStatus returns a boolean if a field has been set.

### SetCmmcStatusNil

`func (o *CmmcGet) SetCmmcStatusNil(b bool)`

 SetCmmcStatusNil sets the value for CmmcStatus to be an explicit nil

### UnsetCmmcStatus
`func (o *CmmcGet) UnsetCmmcStatus()`

UnsetCmmcStatus ensures that no value is present for CmmcStatus, not even an explicit nil
### GetCmmcStatusDate

`func (o *CmmcGet) GetCmmcStatusDate() int64`

GetCmmcStatusDate returns the CmmcStatusDate field if non-nil, zero value otherwise.

### GetCmmcStatusDateOk

`func (o *CmmcGet) GetCmmcStatusDateOk() (*int64, bool)`

GetCmmcStatusDateOk returns a tuple with the CmmcStatusDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCmmcStatusDate

`func (o *CmmcGet) SetCmmcStatusDate(v int64)`

SetCmmcStatusDate sets CmmcStatusDate field to given value.

### HasCmmcStatusDate

`func (o *CmmcGet) HasCmmcStatusDate() bool`

HasCmmcStatusDate returns a boolean if a field has been set.

### SetCmmcStatusDateNil

`func (o *CmmcGet) SetCmmcStatusDateNil(b bool)`

 SetCmmcStatusDateNil sets the value for CmmcStatusDate to be an explicit nil

### UnsetCmmcStatusDate
`func (o *CmmcGet) UnsetCmmcStatusDate()`

UnsetCmmcStatusDate ensures that no value is present for CmmcStatusDate, not even an explicit nil
### GetCmmcStatusExpirationDate

`func (o *CmmcGet) GetCmmcStatusExpirationDate() int64`

GetCmmcStatusExpirationDate returns the CmmcStatusExpirationDate field if non-nil, zero value otherwise.

### GetCmmcStatusExpirationDateOk

`func (o *CmmcGet) GetCmmcStatusExpirationDateOk() (*int64, bool)`

GetCmmcStatusExpirationDateOk returns a tuple with the CmmcStatusExpirationDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCmmcStatusExpirationDate

`func (o *CmmcGet) SetCmmcStatusExpirationDate(v int64)`

SetCmmcStatusExpirationDate sets CmmcStatusExpirationDate field to given value.

### HasCmmcStatusExpirationDate

`func (o *CmmcGet) HasCmmcStatusExpirationDate() bool`

HasCmmcStatusExpirationDate returns a boolean if a field has been set.

### SetCmmcStatusExpirationDateNil

`func (o *CmmcGet) SetCmmcStatusExpirationDateNil(b bool)`

 SetCmmcStatusExpirationDateNil sets the value for CmmcStatusExpirationDate to be an explicit nil

### UnsetCmmcStatusExpirationDate
`func (o *CmmcGet) UnsetCmmcStatusExpirationDate()`

UnsetCmmcStatusExpirationDate ensures that no value is present for CmmcStatusExpirationDate, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


