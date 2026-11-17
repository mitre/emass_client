# SwBaselineConditionalFields

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ApprovalDate** | Pointer to **NullableInt64** | [Conditional] Approval date of the software asset. If Approval Status is set to \&quot;Unapproved\&quot; or \&quot;In Progress\&quot;, Approval Date will be set to null. | [optional] 

## Methods

### NewSwBaselineConditionalFields

`func NewSwBaselineConditionalFields() *SwBaselineConditionalFields`

NewSwBaselineConditionalFields instantiates a new SwBaselineConditionalFields object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSwBaselineConditionalFieldsWithDefaults

`func NewSwBaselineConditionalFieldsWithDefaults() *SwBaselineConditionalFields`

NewSwBaselineConditionalFieldsWithDefaults instantiates a new SwBaselineConditionalFields object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetApprovalDate

`func (o *SwBaselineConditionalFields) GetApprovalDate() int64`

GetApprovalDate returns the ApprovalDate field if non-nil, zero value otherwise.

### GetApprovalDateOk

`func (o *SwBaselineConditionalFields) GetApprovalDateOk() (*int64, bool)`

GetApprovalDateOk returns a tuple with the ApprovalDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetApprovalDate

`func (o *SwBaselineConditionalFields) SetApprovalDate(v int64)`

SetApprovalDate sets ApprovalDate field to given value.

### HasApprovalDate

`func (o *SwBaselineConditionalFields) HasApprovalDate() bool`

HasApprovalDate returns a boolean if a field has been set.

### SetApprovalDateNil

`func (o *SwBaselineConditionalFields) SetApprovalDateNil(b bool)`

 SetApprovalDateNil sets the value for ApprovalDate to be an explicit nil

### UnsetApprovalDate
`func (o *SwBaselineConditionalFields) UnsetApprovalDate()`

UnsetApprovalDate ensures that no value is present for ApprovalDate, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


