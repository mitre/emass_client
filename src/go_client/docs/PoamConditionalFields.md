# PoamConditionalFields

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**PocFirstName** | Pointer to **string** | [Conditional] First name of POC. 100 Characters. | [optional] 
**PocLastName** | Pointer to **string** | [Conditional] Last name of POC. 100 Characters. | [optional] 
**PocEmail** | Pointer to **string** | [Conditional] Email address of POC. 100 Characters. | [optional] 
**PocPhoneNumber** | Pointer to **string** | [Conditional] Phone number of POC (area code) ***-**** format. 100 Characters. | [optional] 
**Severity** | Pointer to **string** | [Conditional] Required for approved items. Values include the following options: (Very Low, Low, Moderate,High,Very High) | [optional] 
**ScheduledCompletionDate** | Pointer to **NullableInt64** | [Conditional] Required for ongoing and completed POA&amp;M items. Unix time format. | [optional] 
**CompletionDate** | Pointer to **int64** | [Conditional] Field is required for completed POA&amp;M items. Unix time format. | [optional] 
**Comments** | Pointer to **string** | [Conditional] Field is required for completed and risk accepted POA&amp;M items. 2000 Characters | [optional] 
**PersonnelResourcesFundedBaseHours** | Pointer to **NullableFloat32** | [Conditional] At least one of the following is required and must be completed for each POA&amp;M Item:   Personnel Resources-&gt; Funded Base Hours   Personnel Resources-&gt; Unfunded Base Hours   Non-Personnel Resources-&gt; Funded Amount   Non-Personnel Resources-&gt; Unfunded Amount Displays numbers to the second decimal point (e.g., 100.00). VA only.  | [optional] 
**PersonnelResourcesCostCode** | Pointer to **NullableString** | [Conditional] Required if Personnel Resources: Funded Base Hours is populated. Only accepts values present in the field&#39;s lookup table (modifiable by eMASS System Admins). VA only.  | [optional] 
**PersonnelResourcesUnfundedBaseHours** | Pointer to **NullableFloat32** | [Conditional] At least one of the following is required and must be completed for each POA&amp;M Item:   Personnel Resources-&gt; Funded Base Hours   Personnel Resources-&gt; Unfunded Base Hours   Non-Personnel Resources-&gt; Funded Amount   Non-Personnel Resources-&gt; Unfunded Amount Displays numbers to the second decimal point (e.g., 100.00). VA only.  | [optional] 
**PersonnelResourcesNonfundingObstacle** | Pointer to **NullableString** | [Conditional] Required if Personnel Resources: Unfunded Base Hours is populated. Only accepts values present in the field&#39;s lookup table (modifiable by eMASS System Admins). VA only.  | [optional] 
**PersonnelResourcesNonfundingObstacleOtherReason** | Pointer to **NullableString** | [Conditional] Required if the value \&quot;Other\&quot; is populated for the field Personnel Resources: Non-Funding Obstacle. VA only. | [optional] 
**NonPersonnelResourcesFundedAmount** | Pointer to **NullableFloat32** | [Conditional] At least one of the following is required and must be completed for each POA&amp;M Item:   Personnel Resources-&gt; Funded Base Hours   Personnel Resources-&gt; Unfunded Base Hours   Non-Personnel Resources-&gt; Funded Amount   Non-Personnel Resources-&gt; Unfunded Amount Displays numbers to the second decimal point (e.g., 100.00). VA only.  | [optional] 
**NonPersonnelResourcesCostCode** | Pointer to **NullableString** | [Conditional] Required if Non-Personnel Resources: Funded Amount is populated. Only accepts values present in the field&#39;s lookup table (modifiable by eMASS System Admins). VA only.  | [optional] 
**NonPersonnelResourcesUnfundedAmount** | Pointer to **NullableFloat32** | [Conditional] At least one of the following is required and must be completed for each POA&amp;M Item:   Personnel Resources-&gt; Funded Base Hours   Personnel Resources-&gt; Unfunded Base Hours   Non-Personnel Resources-&gt; Funded Amount   Non-Personnel Resources-&gt; Unfunded Amount Displays numbers to the second decimal point (e.g., 100.00). VA only.  | [optional] 
**NonPersonnelResourcesNonfundingObstacle** | Pointer to **NullableString** | [Conditional] Required if Non-Personnel Resources: Unfunded Amount is populated. Only accepts values present in the field&#39;s lookup table (modifiable by eMASS System Admins). VA only.  | [optional] 
**NonPersonnelResourcesNonfundingObstacleOtherReason** | Pointer to **NullableString** | [Conditional] Required if the value \&quot;Other\&quot; is populated for the field Non-Personnel Resources: Non-Funding Obstacle. VA only. | [optional] 

## Methods

### NewPoamConditionalFields

`func NewPoamConditionalFields() *PoamConditionalFields`

NewPoamConditionalFields instantiates a new PoamConditionalFields object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPoamConditionalFieldsWithDefaults

`func NewPoamConditionalFieldsWithDefaults() *PoamConditionalFields`

NewPoamConditionalFieldsWithDefaults instantiates a new PoamConditionalFields object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetPocFirstName

`func (o *PoamConditionalFields) GetPocFirstName() string`

GetPocFirstName returns the PocFirstName field if non-nil, zero value otherwise.

### GetPocFirstNameOk

`func (o *PoamConditionalFields) GetPocFirstNameOk() (*string, bool)`

GetPocFirstNameOk returns a tuple with the PocFirstName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPocFirstName

`func (o *PoamConditionalFields) SetPocFirstName(v string)`

SetPocFirstName sets PocFirstName field to given value.

### HasPocFirstName

`func (o *PoamConditionalFields) HasPocFirstName() bool`

HasPocFirstName returns a boolean if a field has been set.

### GetPocLastName

`func (o *PoamConditionalFields) GetPocLastName() string`

GetPocLastName returns the PocLastName field if non-nil, zero value otherwise.

### GetPocLastNameOk

`func (o *PoamConditionalFields) GetPocLastNameOk() (*string, bool)`

GetPocLastNameOk returns a tuple with the PocLastName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPocLastName

`func (o *PoamConditionalFields) SetPocLastName(v string)`

SetPocLastName sets PocLastName field to given value.

### HasPocLastName

`func (o *PoamConditionalFields) HasPocLastName() bool`

HasPocLastName returns a boolean if a field has been set.

### GetPocEmail

`func (o *PoamConditionalFields) GetPocEmail() string`

GetPocEmail returns the PocEmail field if non-nil, zero value otherwise.

### GetPocEmailOk

`func (o *PoamConditionalFields) GetPocEmailOk() (*string, bool)`

GetPocEmailOk returns a tuple with the PocEmail field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPocEmail

`func (o *PoamConditionalFields) SetPocEmail(v string)`

SetPocEmail sets PocEmail field to given value.

### HasPocEmail

`func (o *PoamConditionalFields) HasPocEmail() bool`

HasPocEmail returns a boolean if a field has been set.

### GetPocPhoneNumber

`func (o *PoamConditionalFields) GetPocPhoneNumber() string`

GetPocPhoneNumber returns the PocPhoneNumber field if non-nil, zero value otherwise.

### GetPocPhoneNumberOk

`func (o *PoamConditionalFields) GetPocPhoneNumberOk() (*string, bool)`

GetPocPhoneNumberOk returns a tuple with the PocPhoneNumber field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPocPhoneNumber

`func (o *PoamConditionalFields) SetPocPhoneNumber(v string)`

SetPocPhoneNumber sets PocPhoneNumber field to given value.

### HasPocPhoneNumber

`func (o *PoamConditionalFields) HasPocPhoneNumber() bool`

HasPocPhoneNumber returns a boolean if a field has been set.

### GetSeverity

`func (o *PoamConditionalFields) GetSeverity() string`

GetSeverity returns the Severity field if non-nil, zero value otherwise.

### GetSeverityOk

`func (o *PoamConditionalFields) GetSeverityOk() (*string, bool)`

GetSeverityOk returns a tuple with the Severity field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSeverity

`func (o *PoamConditionalFields) SetSeverity(v string)`

SetSeverity sets Severity field to given value.

### HasSeverity

`func (o *PoamConditionalFields) HasSeverity() bool`

HasSeverity returns a boolean if a field has been set.

### GetScheduledCompletionDate

`func (o *PoamConditionalFields) GetScheduledCompletionDate() int64`

GetScheduledCompletionDate returns the ScheduledCompletionDate field if non-nil, zero value otherwise.

### GetScheduledCompletionDateOk

`func (o *PoamConditionalFields) GetScheduledCompletionDateOk() (*int64, bool)`

GetScheduledCompletionDateOk returns a tuple with the ScheduledCompletionDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetScheduledCompletionDate

`func (o *PoamConditionalFields) SetScheduledCompletionDate(v int64)`

SetScheduledCompletionDate sets ScheduledCompletionDate field to given value.

### HasScheduledCompletionDate

`func (o *PoamConditionalFields) HasScheduledCompletionDate() bool`

HasScheduledCompletionDate returns a boolean if a field has been set.

### SetScheduledCompletionDateNil

`func (o *PoamConditionalFields) SetScheduledCompletionDateNil(b bool)`

 SetScheduledCompletionDateNil sets the value for ScheduledCompletionDate to be an explicit nil

### UnsetScheduledCompletionDate
`func (o *PoamConditionalFields) UnsetScheduledCompletionDate()`

UnsetScheduledCompletionDate ensures that no value is present for ScheduledCompletionDate, not even an explicit nil
### GetCompletionDate

`func (o *PoamConditionalFields) GetCompletionDate() int64`

GetCompletionDate returns the CompletionDate field if non-nil, zero value otherwise.

### GetCompletionDateOk

`func (o *PoamConditionalFields) GetCompletionDateOk() (*int64, bool)`

GetCompletionDateOk returns a tuple with the CompletionDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCompletionDate

`func (o *PoamConditionalFields) SetCompletionDate(v int64)`

SetCompletionDate sets CompletionDate field to given value.

### HasCompletionDate

`func (o *PoamConditionalFields) HasCompletionDate() bool`

HasCompletionDate returns a boolean if a field has been set.

### GetComments

`func (o *PoamConditionalFields) GetComments() string`

GetComments returns the Comments field if non-nil, zero value otherwise.

### GetCommentsOk

`func (o *PoamConditionalFields) GetCommentsOk() (*string, bool)`

GetCommentsOk returns a tuple with the Comments field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetComments

`func (o *PoamConditionalFields) SetComments(v string)`

SetComments sets Comments field to given value.

### HasComments

`func (o *PoamConditionalFields) HasComments() bool`

HasComments returns a boolean if a field has been set.

### GetPersonnelResourcesFundedBaseHours

`func (o *PoamConditionalFields) GetPersonnelResourcesFundedBaseHours() float32`

GetPersonnelResourcesFundedBaseHours returns the PersonnelResourcesFundedBaseHours field if non-nil, zero value otherwise.

### GetPersonnelResourcesFundedBaseHoursOk

`func (o *PoamConditionalFields) GetPersonnelResourcesFundedBaseHoursOk() (*float32, bool)`

GetPersonnelResourcesFundedBaseHoursOk returns a tuple with the PersonnelResourcesFundedBaseHours field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPersonnelResourcesFundedBaseHours

`func (o *PoamConditionalFields) SetPersonnelResourcesFundedBaseHours(v float32)`

SetPersonnelResourcesFundedBaseHours sets PersonnelResourcesFundedBaseHours field to given value.

### HasPersonnelResourcesFundedBaseHours

`func (o *PoamConditionalFields) HasPersonnelResourcesFundedBaseHours() bool`

HasPersonnelResourcesFundedBaseHours returns a boolean if a field has been set.

### SetPersonnelResourcesFundedBaseHoursNil

`func (o *PoamConditionalFields) SetPersonnelResourcesFundedBaseHoursNil(b bool)`

 SetPersonnelResourcesFundedBaseHoursNil sets the value for PersonnelResourcesFundedBaseHours to be an explicit nil

### UnsetPersonnelResourcesFundedBaseHours
`func (o *PoamConditionalFields) UnsetPersonnelResourcesFundedBaseHours()`

UnsetPersonnelResourcesFundedBaseHours ensures that no value is present for PersonnelResourcesFundedBaseHours, not even an explicit nil
### GetPersonnelResourcesCostCode

`func (o *PoamConditionalFields) GetPersonnelResourcesCostCode() string`

GetPersonnelResourcesCostCode returns the PersonnelResourcesCostCode field if non-nil, zero value otherwise.

### GetPersonnelResourcesCostCodeOk

`func (o *PoamConditionalFields) GetPersonnelResourcesCostCodeOk() (*string, bool)`

GetPersonnelResourcesCostCodeOk returns a tuple with the PersonnelResourcesCostCode field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPersonnelResourcesCostCode

`func (o *PoamConditionalFields) SetPersonnelResourcesCostCode(v string)`

SetPersonnelResourcesCostCode sets PersonnelResourcesCostCode field to given value.

### HasPersonnelResourcesCostCode

`func (o *PoamConditionalFields) HasPersonnelResourcesCostCode() bool`

HasPersonnelResourcesCostCode returns a boolean if a field has been set.

### SetPersonnelResourcesCostCodeNil

`func (o *PoamConditionalFields) SetPersonnelResourcesCostCodeNil(b bool)`

 SetPersonnelResourcesCostCodeNil sets the value for PersonnelResourcesCostCode to be an explicit nil

### UnsetPersonnelResourcesCostCode
`func (o *PoamConditionalFields) UnsetPersonnelResourcesCostCode()`

UnsetPersonnelResourcesCostCode ensures that no value is present for PersonnelResourcesCostCode, not even an explicit nil
### GetPersonnelResourcesUnfundedBaseHours

`func (o *PoamConditionalFields) GetPersonnelResourcesUnfundedBaseHours() float32`

GetPersonnelResourcesUnfundedBaseHours returns the PersonnelResourcesUnfundedBaseHours field if non-nil, zero value otherwise.

### GetPersonnelResourcesUnfundedBaseHoursOk

`func (o *PoamConditionalFields) GetPersonnelResourcesUnfundedBaseHoursOk() (*float32, bool)`

GetPersonnelResourcesUnfundedBaseHoursOk returns a tuple with the PersonnelResourcesUnfundedBaseHours field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPersonnelResourcesUnfundedBaseHours

`func (o *PoamConditionalFields) SetPersonnelResourcesUnfundedBaseHours(v float32)`

SetPersonnelResourcesUnfundedBaseHours sets PersonnelResourcesUnfundedBaseHours field to given value.

### HasPersonnelResourcesUnfundedBaseHours

`func (o *PoamConditionalFields) HasPersonnelResourcesUnfundedBaseHours() bool`

HasPersonnelResourcesUnfundedBaseHours returns a boolean if a field has been set.

### SetPersonnelResourcesUnfundedBaseHoursNil

`func (o *PoamConditionalFields) SetPersonnelResourcesUnfundedBaseHoursNil(b bool)`

 SetPersonnelResourcesUnfundedBaseHoursNil sets the value for PersonnelResourcesUnfundedBaseHours to be an explicit nil

### UnsetPersonnelResourcesUnfundedBaseHours
`func (o *PoamConditionalFields) UnsetPersonnelResourcesUnfundedBaseHours()`

UnsetPersonnelResourcesUnfundedBaseHours ensures that no value is present for PersonnelResourcesUnfundedBaseHours, not even an explicit nil
### GetPersonnelResourcesNonfundingObstacle

`func (o *PoamConditionalFields) GetPersonnelResourcesNonfundingObstacle() string`

GetPersonnelResourcesNonfundingObstacle returns the PersonnelResourcesNonfundingObstacle field if non-nil, zero value otherwise.

### GetPersonnelResourcesNonfundingObstacleOk

`func (o *PoamConditionalFields) GetPersonnelResourcesNonfundingObstacleOk() (*string, bool)`

GetPersonnelResourcesNonfundingObstacleOk returns a tuple with the PersonnelResourcesNonfundingObstacle field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPersonnelResourcesNonfundingObstacle

`func (o *PoamConditionalFields) SetPersonnelResourcesNonfundingObstacle(v string)`

SetPersonnelResourcesNonfundingObstacle sets PersonnelResourcesNonfundingObstacle field to given value.

### HasPersonnelResourcesNonfundingObstacle

`func (o *PoamConditionalFields) HasPersonnelResourcesNonfundingObstacle() bool`

HasPersonnelResourcesNonfundingObstacle returns a boolean if a field has been set.

### SetPersonnelResourcesNonfundingObstacleNil

`func (o *PoamConditionalFields) SetPersonnelResourcesNonfundingObstacleNil(b bool)`

 SetPersonnelResourcesNonfundingObstacleNil sets the value for PersonnelResourcesNonfundingObstacle to be an explicit nil

### UnsetPersonnelResourcesNonfundingObstacle
`func (o *PoamConditionalFields) UnsetPersonnelResourcesNonfundingObstacle()`

UnsetPersonnelResourcesNonfundingObstacle ensures that no value is present for PersonnelResourcesNonfundingObstacle, not even an explicit nil
### GetPersonnelResourcesNonfundingObstacleOtherReason

`func (o *PoamConditionalFields) GetPersonnelResourcesNonfundingObstacleOtherReason() string`

GetPersonnelResourcesNonfundingObstacleOtherReason returns the PersonnelResourcesNonfundingObstacleOtherReason field if non-nil, zero value otherwise.

### GetPersonnelResourcesNonfundingObstacleOtherReasonOk

`func (o *PoamConditionalFields) GetPersonnelResourcesNonfundingObstacleOtherReasonOk() (*string, bool)`

GetPersonnelResourcesNonfundingObstacleOtherReasonOk returns a tuple with the PersonnelResourcesNonfundingObstacleOtherReason field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPersonnelResourcesNonfundingObstacleOtherReason

`func (o *PoamConditionalFields) SetPersonnelResourcesNonfundingObstacleOtherReason(v string)`

SetPersonnelResourcesNonfundingObstacleOtherReason sets PersonnelResourcesNonfundingObstacleOtherReason field to given value.

### HasPersonnelResourcesNonfundingObstacleOtherReason

`func (o *PoamConditionalFields) HasPersonnelResourcesNonfundingObstacleOtherReason() bool`

HasPersonnelResourcesNonfundingObstacleOtherReason returns a boolean if a field has been set.

### SetPersonnelResourcesNonfundingObstacleOtherReasonNil

`func (o *PoamConditionalFields) SetPersonnelResourcesNonfundingObstacleOtherReasonNil(b bool)`

 SetPersonnelResourcesNonfundingObstacleOtherReasonNil sets the value for PersonnelResourcesNonfundingObstacleOtherReason to be an explicit nil

### UnsetPersonnelResourcesNonfundingObstacleOtherReason
`func (o *PoamConditionalFields) UnsetPersonnelResourcesNonfundingObstacleOtherReason()`

UnsetPersonnelResourcesNonfundingObstacleOtherReason ensures that no value is present for PersonnelResourcesNonfundingObstacleOtherReason, not even an explicit nil
### GetNonPersonnelResourcesFundedAmount

`func (o *PoamConditionalFields) GetNonPersonnelResourcesFundedAmount() float32`

GetNonPersonnelResourcesFundedAmount returns the NonPersonnelResourcesFundedAmount field if non-nil, zero value otherwise.

### GetNonPersonnelResourcesFundedAmountOk

`func (o *PoamConditionalFields) GetNonPersonnelResourcesFundedAmountOk() (*float32, bool)`

GetNonPersonnelResourcesFundedAmountOk returns a tuple with the NonPersonnelResourcesFundedAmount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNonPersonnelResourcesFundedAmount

`func (o *PoamConditionalFields) SetNonPersonnelResourcesFundedAmount(v float32)`

SetNonPersonnelResourcesFundedAmount sets NonPersonnelResourcesFundedAmount field to given value.

### HasNonPersonnelResourcesFundedAmount

`func (o *PoamConditionalFields) HasNonPersonnelResourcesFundedAmount() bool`

HasNonPersonnelResourcesFundedAmount returns a boolean if a field has been set.

### SetNonPersonnelResourcesFundedAmountNil

`func (o *PoamConditionalFields) SetNonPersonnelResourcesFundedAmountNil(b bool)`

 SetNonPersonnelResourcesFundedAmountNil sets the value for NonPersonnelResourcesFundedAmount to be an explicit nil

### UnsetNonPersonnelResourcesFundedAmount
`func (o *PoamConditionalFields) UnsetNonPersonnelResourcesFundedAmount()`

UnsetNonPersonnelResourcesFundedAmount ensures that no value is present for NonPersonnelResourcesFundedAmount, not even an explicit nil
### GetNonPersonnelResourcesCostCode

`func (o *PoamConditionalFields) GetNonPersonnelResourcesCostCode() string`

GetNonPersonnelResourcesCostCode returns the NonPersonnelResourcesCostCode field if non-nil, zero value otherwise.

### GetNonPersonnelResourcesCostCodeOk

`func (o *PoamConditionalFields) GetNonPersonnelResourcesCostCodeOk() (*string, bool)`

GetNonPersonnelResourcesCostCodeOk returns a tuple with the NonPersonnelResourcesCostCode field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNonPersonnelResourcesCostCode

`func (o *PoamConditionalFields) SetNonPersonnelResourcesCostCode(v string)`

SetNonPersonnelResourcesCostCode sets NonPersonnelResourcesCostCode field to given value.

### HasNonPersonnelResourcesCostCode

`func (o *PoamConditionalFields) HasNonPersonnelResourcesCostCode() bool`

HasNonPersonnelResourcesCostCode returns a boolean if a field has been set.

### SetNonPersonnelResourcesCostCodeNil

`func (o *PoamConditionalFields) SetNonPersonnelResourcesCostCodeNil(b bool)`

 SetNonPersonnelResourcesCostCodeNil sets the value for NonPersonnelResourcesCostCode to be an explicit nil

### UnsetNonPersonnelResourcesCostCode
`func (o *PoamConditionalFields) UnsetNonPersonnelResourcesCostCode()`

UnsetNonPersonnelResourcesCostCode ensures that no value is present for NonPersonnelResourcesCostCode, not even an explicit nil
### GetNonPersonnelResourcesUnfundedAmount

`func (o *PoamConditionalFields) GetNonPersonnelResourcesUnfundedAmount() float32`

GetNonPersonnelResourcesUnfundedAmount returns the NonPersonnelResourcesUnfundedAmount field if non-nil, zero value otherwise.

### GetNonPersonnelResourcesUnfundedAmountOk

`func (o *PoamConditionalFields) GetNonPersonnelResourcesUnfundedAmountOk() (*float32, bool)`

GetNonPersonnelResourcesUnfundedAmountOk returns a tuple with the NonPersonnelResourcesUnfundedAmount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNonPersonnelResourcesUnfundedAmount

`func (o *PoamConditionalFields) SetNonPersonnelResourcesUnfundedAmount(v float32)`

SetNonPersonnelResourcesUnfundedAmount sets NonPersonnelResourcesUnfundedAmount field to given value.

### HasNonPersonnelResourcesUnfundedAmount

`func (o *PoamConditionalFields) HasNonPersonnelResourcesUnfundedAmount() bool`

HasNonPersonnelResourcesUnfundedAmount returns a boolean if a field has been set.

### SetNonPersonnelResourcesUnfundedAmountNil

`func (o *PoamConditionalFields) SetNonPersonnelResourcesUnfundedAmountNil(b bool)`

 SetNonPersonnelResourcesUnfundedAmountNil sets the value for NonPersonnelResourcesUnfundedAmount to be an explicit nil

### UnsetNonPersonnelResourcesUnfundedAmount
`func (o *PoamConditionalFields) UnsetNonPersonnelResourcesUnfundedAmount()`

UnsetNonPersonnelResourcesUnfundedAmount ensures that no value is present for NonPersonnelResourcesUnfundedAmount, not even an explicit nil
### GetNonPersonnelResourcesNonfundingObstacle

`func (o *PoamConditionalFields) GetNonPersonnelResourcesNonfundingObstacle() string`

GetNonPersonnelResourcesNonfundingObstacle returns the NonPersonnelResourcesNonfundingObstacle field if non-nil, zero value otherwise.

### GetNonPersonnelResourcesNonfundingObstacleOk

`func (o *PoamConditionalFields) GetNonPersonnelResourcesNonfundingObstacleOk() (*string, bool)`

GetNonPersonnelResourcesNonfundingObstacleOk returns a tuple with the NonPersonnelResourcesNonfundingObstacle field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNonPersonnelResourcesNonfundingObstacle

`func (o *PoamConditionalFields) SetNonPersonnelResourcesNonfundingObstacle(v string)`

SetNonPersonnelResourcesNonfundingObstacle sets NonPersonnelResourcesNonfundingObstacle field to given value.

### HasNonPersonnelResourcesNonfundingObstacle

`func (o *PoamConditionalFields) HasNonPersonnelResourcesNonfundingObstacle() bool`

HasNonPersonnelResourcesNonfundingObstacle returns a boolean if a field has been set.

### SetNonPersonnelResourcesNonfundingObstacleNil

`func (o *PoamConditionalFields) SetNonPersonnelResourcesNonfundingObstacleNil(b bool)`

 SetNonPersonnelResourcesNonfundingObstacleNil sets the value for NonPersonnelResourcesNonfundingObstacle to be an explicit nil

### UnsetNonPersonnelResourcesNonfundingObstacle
`func (o *PoamConditionalFields) UnsetNonPersonnelResourcesNonfundingObstacle()`

UnsetNonPersonnelResourcesNonfundingObstacle ensures that no value is present for NonPersonnelResourcesNonfundingObstacle, not even an explicit nil
### GetNonPersonnelResourcesNonfundingObstacleOtherReason

`func (o *PoamConditionalFields) GetNonPersonnelResourcesNonfundingObstacleOtherReason() string`

GetNonPersonnelResourcesNonfundingObstacleOtherReason returns the NonPersonnelResourcesNonfundingObstacleOtherReason field if non-nil, zero value otherwise.

### GetNonPersonnelResourcesNonfundingObstacleOtherReasonOk

`func (o *PoamConditionalFields) GetNonPersonnelResourcesNonfundingObstacleOtherReasonOk() (*string, bool)`

GetNonPersonnelResourcesNonfundingObstacleOtherReasonOk returns a tuple with the NonPersonnelResourcesNonfundingObstacleOtherReason field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNonPersonnelResourcesNonfundingObstacleOtherReason

`func (o *PoamConditionalFields) SetNonPersonnelResourcesNonfundingObstacleOtherReason(v string)`

SetNonPersonnelResourcesNonfundingObstacleOtherReason sets NonPersonnelResourcesNonfundingObstacleOtherReason field to given value.

### HasNonPersonnelResourcesNonfundingObstacleOtherReason

`func (o *PoamConditionalFields) HasNonPersonnelResourcesNonfundingObstacleOtherReason() bool`

HasNonPersonnelResourcesNonfundingObstacleOtherReason returns a boolean if a field has been set.

### SetNonPersonnelResourcesNonfundingObstacleOtherReasonNil

`func (o *PoamConditionalFields) SetNonPersonnelResourcesNonfundingObstacleOtherReasonNil(b bool)`

 SetNonPersonnelResourcesNonfundingObstacleOtherReasonNil sets the value for NonPersonnelResourcesNonfundingObstacleOtherReason to be an explicit nil

### UnsetNonPersonnelResourcesNonfundingObstacleOtherReason
`func (o *PoamConditionalFields) UnsetNonPersonnelResourcesNonfundingObstacleOtherReason()`

UnsetNonPersonnelResourcesNonfundingObstacleOtherReason ensures that no value is present for NonPersonnelResourcesNonfundingObstacleOtherReason, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


