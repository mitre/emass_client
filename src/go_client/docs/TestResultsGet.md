# TestResultsGet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**SystemId** | Pointer to **int64** | [Required] Unique eMASS identifier. Will need to provide correct number | [optional] 
**Control** | Pointer to **NullableString** | [Read-Only] Control acronym associated with the test result. NIST SP 800-53 Revision 4 defined. | [optional] 
**Cci** | Pointer to **string** | [Required] CCI associated with test result. | [optional] 
**AssessmentProcedure** | Pointer to **string** | [Required] The Security Control Assessment Procedure being assessed. | [optional] 
**IsInherited** | Pointer to **NullableBool** | [Read-only] Indicates whether a test result is inherited. | [optional] 
**TestedBy** | Pointer to **string** | [Required] Last Name, First Name. 100 Characters. | [optional] 
**TestDate** | Pointer to **int64** | [Required] Unix time format. | [optional] 
**Description** | Pointer to **string** | [Required] Include description of test result. 4000 Characters. | [optional] 
**Type** | Pointer to **NullableString** | [Read-Only] Indicates the location in the Control Approval Chain when the test result is submitted. | [optional] 
**ComplianceStatus** | Pointer to **string** | [Required] Test result compliance status | [optional] 

## Methods

### NewTestResultsGet

`func NewTestResultsGet() *TestResultsGet`

NewTestResultsGet instantiates a new TestResultsGet object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewTestResultsGetWithDefaults

`func NewTestResultsGetWithDefaults() *TestResultsGet`

NewTestResultsGetWithDefaults instantiates a new TestResultsGet object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetSystemId

`func (o *TestResultsGet) GetSystemId() int64`

GetSystemId returns the SystemId field if non-nil, zero value otherwise.

### GetSystemIdOk

`func (o *TestResultsGet) GetSystemIdOk() (*int64, bool)`

GetSystemIdOk returns a tuple with the SystemId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSystemId

`func (o *TestResultsGet) SetSystemId(v int64)`

SetSystemId sets SystemId field to given value.

### HasSystemId

`func (o *TestResultsGet) HasSystemId() bool`

HasSystemId returns a boolean if a field has been set.

### GetControl

`func (o *TestResultsGet) GetControl() string`

GetControl returns the Control field if non-nil, zero value otherwise.

### GetControlOk

`func (o *TestResultsGet) GetControlOk() (*string, bool)`

GetControlOk returns a tuple with the Control field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetControl

`func (o *TestResultsGet) SetControl(v string)`

SetControl sets Control field to given value.

### HasControl

`func (o *TestResultsGet) HasControl() bool`

HasControl returns a boolean if a field has been set.

### SetControlNil

`func (o *TestResultsGet) SetControlNil(b bool)`

 SetControlNil sets the value for Control to be an explicit nil

### UnsetControl
`func (o *TestResultsGet) UnsetControl()`

UnsetControl ensures that no value is present for Control, not even an explicit nil
### GetCci

`func (o *TestResultsGet) GetCci() string`

GetCci returns the Cci field if non-nil, zero value otherwise.

### GetCciOk

`func (o *TestResultsGet) GetCciOk() (*string, bool)`

GetCciOk returns a tuple with the Cci field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCci

`func (o *TestResultsGet) SetCci(v string)`

SetCci sets Cci field to given value.

### HasCci

`func (o *TestResultsGet) HasCci() bool`

HasCci returns a boolean if a field has been set.

### GetAssessmentProcedure

`func (o *TestResultsGet) GetAssessmentProcedure() string`

GetAssessmentProcedure returns the AssessmentProcedure field if non-nil, zero value otherwise.

### GetAssessmentProcedureOk

`func (o *TestResultsGet) GetAssessmentProcedureOk() (*string, bool)`

GetAssessmentProcedureOk returns a tuple with the AssessmentProcedure field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAssessmentProcedure

`func (o *TestResultsGet) SetAssessmentProcedure(v string)`

SetAssessmentProcedure sets AssessmentProcedure field to given value.

### HasAssessmentProcedure

`func (o *TestResultsGet) HasAssessmentProcedure() bool`

HasAssessmentProcedure returns a boolean if a field has been set.

### GetIsInherited

`func (o *TestResultsGet) GetIsInherited() bool`

GetIsInherited returns the IsInherited field if non-nil, zero value otherwise.

### GetIsInheritedOk

`func (o *TestResultsGet) GetIsInheritedOk() (*bool, bool)`

GetIsInheritedOk returns a tuple with the IsInherited field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsInherited

`func (o *TestResultsGet) SetIsInherited(v bool)`

SetIsInherited sets IsInherited field to given value.

### HasIsInherited

`func (o *TestResultsGet) HasIsInherited() bool`

HasIsInherited returns a boolean if a field has been set.

### SetIsInheritedNil

`func (o *TestResultsGet) SetIsInheritedNil(b bool)`

 SetIsInheritedNil sets the value for IsInherited to be an explicit nil

### UnsetIsInherited
`func (o *TestResultsGet) UnsetIsInherited()`

UnsetIsInherited ensures that no value is present for IsInherited, not even an explicit nil
### GetTestedBy

`func (o *TestResultsGet) GetTestedBy() string`

GetTestedBy returns the TestedBy field if non-nil, zero value otherwise.

### GetTestedByOk

`func (o *TestResultsGet) GetTestedByOk() (*string, bool)`

GetTestedByOk returns a tuple with the TestedBy field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTestedBy

`func (o *TestResultsGet) SetTestedBy(v string)`

SetTestedBy sets TestedBy field to given value.

### HasTestedBy

`func (o *TestResultsGet) HasTestedBy() bool`

HasTestedBy returns a boolean if a field has been set.

### GetTestDate

`func (o *TestResultsGet) GetTestDate() int64`

GetTestDate returns the TestDate field if non-nil, zero value otherwise.

### GetTestDateOk

`func (o *TestResultsGet) GetTestDateOk() (*int64, bool)`

GetTestDateOk returns a tuple with the TestDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTestDate

`func (o *TestResultsGet) SetTestDate(v int64)`

SetTestDate sets TestDate field to given value.

### HasTestDate

`func (o *TestResultsGet) HasTestDate() bool`

HasTestDate returns a boolean if a field has been set.

### GetDescription

`func (o *TestResultsGet) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *TestResultsGet) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *TestResultsGet) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *TestResultsGet) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### GetType

`func (o *TestResultsGet) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *TestResultsGet) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *TestResultsGet) SetType(v string)`

SetType sets Type field to given value.

### HasType

`func (o *TestResultsGet) HasType() bool`

HasType returns a boolean if a field has been set.

### SetTypeNil

`func (o *TestResultsGet) SetTypeNil(b bool)`

 SetTypeNil sets the value for Type to be an explicit nil

### UnsetType
`func (o *TestResultsGet) UnsetType()`

UnsetType ensures that no value is present for Type, not even an explicit nil
### GetComplianceStatus

`func (o *TestResultsGet) GetComplianceStatus() string`

GetComplianceStatus returns the ComplianceStatus field if non-nil, zero value otherwise.

### GetComplianceStatusOk

`func (o *TestResultsGet) GetComplianceStatusOk() (*string, bool)`

GetComplianceStatusOk returns a tuple with the ComplianceStatus field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetComplianceStatus

`func (o *TestResultsGet) SetComplianceStatus(v string)`

SetComplianceStatus sets ComplianceStatus field to given value.

### HasComplianceStatus

`func (o *TestResultsGet) HasComplianceStatus() bool`

HasComplianceStatus returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


