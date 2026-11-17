# PoamResponseGetSystemsDataInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**SystemId** | Pointer to **int64** | [Required] Unique eMASS system identifier. | [optional] 
**PoamId** | Pointer to **int64** | [Required] Unique item identifier | [optional] 
**DisplayPoamId** | Pointer to **int64** | [Required] Globally unique identifier for individual POA&amp;M Items, seen on the front-end as ID. | [optional] 
**Status** | Pointer to **string** | [Required] The POA&amp;M status | [optional] 
**VulnerabilityDescription** | Pointer to **string** | [Required] Provide a description of the POA&amp;M Item. 2000 Characters. | [optional] 
**SourceIdentifyingVulnerability** | Pointer to **string** | [Required] Include Source Identifying Vulnerability text. 2000 Characters. | [optional] 
**PocOrganization** | Pointer to **string** | [Required] Organization/Office represented. 100 Characters. | [optional] 
**Resources** | Pointer to **string** | [Required] List of resources used. 250 Characters. | [optional] 
**IdentifiedInCFOAuditOrOtherReview** | Pointer to **bool** | [Required] If not specified, this field will be set to false because it does not accept a null value. VA only | [optional] 
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
**Milestones** | Pointer to [**[]MilestonesGet**](MilestonesGet.md) |  | [optional] 
**ExternalUid** | Pointer to **string** | [Optional] Unique identifier external to the eMASS application for use with associating POA&amp;Ms. 100 Characters. | [optional] 
**ControlAcronym** | Pointer to **string** | [Optional] Control acronym associated with the POA&amp;M Item. NIST SP 800-53 Revision 4 defined. | [optional] 
**AssessmentProcedure** | Pointer to **string** | [Optional] The Security Control Assessment Procedure being associated with the POA&amp;M Item. | [optional] 
**SecurityChecks** | Pointer to **string** | [Optional] Security Checks that are associated with the POA&amp;M. | [optional] 
**RawSeverity** | Pointer to **string** | [Optional] Scan vulnerability ratting Values include the following options: (Very Low, Low, Moderate,High,Very High) | [optional] 
**RelevanceOfThreat** | Pointer to **string** | [Optional] Values include the following options (Very Low, Low, Moderate,High,Very High) | [optional] 
**Likelihood** | Pointer to **string** | [Optional] Values include the following options (Very Low, Low, Moderate,High,Very High) | [optional] 
**Impact** | Pointer to **string** | [Optional] Values include the following options (Very Low, Low, Moderate,High,Very High) | [optional] 
**ImpactDescription** | Pointer to **string** | [Optional] Include description of Security Control&#39;s impact. | [optional] 
**ResidualRiskLevel** | Pointer to **string** | [Optional] Values include the following options (Very Low, Low, Moderate,High,Very High) | [optional] 
**Recommendations** | Pointer to **string** | [Optional] Include recommendations. Character Limit &#x3D; 2,000. | [optional] 
**Mitigations** | Pointer to **string** | [Optional] Include mitigation explanation. 2000 Characters. | [optional] 
**ResultingResidualRiskLevelAfterProposedMitigations** | Pointer to **NullableString** | [Optional] Indicate the risk level expected after any proposed mitigations are implemented. Proposed mitigations should be appropriately documented as POA&amp;M milestones. Navy only. | [optional] 
**PredisposingConditions** | Pointer to **NullableString** | [Optional] A predisposing condition is a condition existing within an organization, a mission or business process, enterprise architecture, information system/PIT, or environment of operation, which affects (i.e., increases or decreases) the likelihood that threat events, once initiated, result in adverse impacts. Navy only. | [optional] 
**ThreatDescription** | Pointer to **NullableString** | [Optional] Describe the identified threat(s) and relevance to the information system. Navy only. | [optional] 
**DevicesAffected** | Pointer to **NullableString** | [Optional] List any affected devices by hostname. If all devices in the information system are affected, state &#39;system&#39; or &#39;all&#39;. Navy only | [optional] 
**ConditionId** | Pointer to **NullableString** | [Read-Only] Unique identifier of the authorization term/condition linked to the POA&amp;M Item. | [optional] 
**IsInherited** | Pointer to **NullableBool** | [Read-only] Indicates whether a test result is inherited. | [optional] 
**Cci** | Pointer to **NullableString** | [Read-Only] CCI associated with POA&amp;M Item. | [optional] 
**ReviewStatus** | Pointer to **NullableString** | [Read-Only] Values include the following options: (Not Approved,Under Review,Approved) | [optional] 
**CreatedDate** | Pointer to **int64** | [Read-Only] Timestamp representing when the POA&amp;M Item was entered into the database. | [optional] 
**ExtensionDate** | Pointer to **NullableInt64** | [Read-Only] Value returned for a POA&amp;M Item with review status \&quot;Approved\&quot; and has a milestone with a scheduled completion date that extends beyond the POA&amp;M Item&#39;s scheduled completion date.  | [optional] 
**PendingExtensionDate** | Pointer to **NullableInt64** | [Read-Only] Value returned for a POA&amp;M Item with a review status of \&quot;Approved\&quot; and an unapproved milestone with a scheduled completion date that extends beyond the POA&amp;M Item&#39;s scheduled completion date.  | [optional] 
**Artifacts** | Pointer to **NullableString** | [Read-Only] Lists the filenames of any artifact files attached to the POA&amp;M Item. Multiple values are separated by “; ”. | [optional] 

## Methods

### NewPoamResponseGetSystemsDataInner

`func NewPoamResponseGetSystemsDataInner() *PoamResponseGetSystemsDataInner`

NewPoamResponseGetSystemsDataInner instantiates a new PoamResponseGetSystemsDataInner object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPoamResponseGetSystemsDataInnerWithDefaults

`func NewPoamResponseGetSystemsDataInnerWithDefaults() *PoamResponseGetSystemsDataInner`

NewPoamResponseGetSystemsDataInnerWithDefaults instantiates a new PoamResponseGetSystemsDataInner object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetSystemId

`func (o *PoamResponseGetSystemsDataInner) GetSystemId() int64`

GetSystemId returns the SystemId field if non-nil, zero value otherwise.

### GetSystemIdOk

`func (o *PoamResponseGetSystemsDataInner) GetSystemIdOk() (*int64, bool)`

GetSystemIdOk returns a tuple with the SystemId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSystemId

`func (o *PoamResponseGetSystemsDataInner) SetSystemId(v int64)`

SetSystemId sets SystemId field to given value.

### HasSystemId

`func (o *PoamResponseGetSystemsDataInner) HasSystemId() bool`

HasSystemId returns a boolean if a field has been set.

### GetPoamId

`func (o *PoamResponseGetSystemsDataInner) GetPoamId() int64`

GetPoamId returns the PoamId field if non-nil, zero value otherwise.

### GetPoamIdOk

`func (o *PoamResponseGetSystemsDataInner) GetPoamIdOk() (*int64, bool)`

GetPoamIdOk returns a tuple with the PoamId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPoamId

`func (o *PoamResponseGetSystemsDataInner) SetPoamId(v int64)`

SetPoamId sets PoamId field to given value.

### HasPoamId

`func (o *PoamResponseGetSystemsDataInner) HasPoamId() bool`

HasPoamId returns a boolean if a field has been set.

### GetDisplayPoamId

`func (o *PoamResponseGetSystemsDataInner) GetDisplayPoamId() int64`

GetDisplayPoamId returns the DisplayPoamId field if non-nil, zero value otherwise.

### GetDisplayPoamIdOk

`func (o *PoamResponseGetSystemsDataInner) GetDisplayPoamIdOk() (*int64, bool)`

GetDisplayPoamIdOk returns a tuple with the DisplayPoamId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDisplayPoamId

`func (o *PoamResponseGetSystemsDataInner) SetDisplayPoamId(v int64)`

SetDisplayPoamId sets DisplayPoamId field to given value.

### HasDisplayPoamId

`func (o *PoamResponseGetSystemsDataInner) HasDisplayPoamId() bool`

HasDisplayPoamId returns a boolean if a field has been set.

### GetStatus

`func (o *PoamResponseGetSystemsDataInner) GetStatus() string`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *PoamResponseGetSystemsDataInner) GetStatusOk() (*string, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *PoamResponseGetSystemsDataInner) SetStatus(v string)`

SetStatus sets Status field to given value.

### HasStatus

`func (o *PoamResponseGetSystemsDataInner) HasStatus() bool`

HasStatus returns a boolean if a field has been set.

### GetVulnerabilityDescription

`func (o *PoamResponseGetSystemsDataInner) GetVulnerabilityDescription() string`

GetVulnerabilityDescription returns the VulnerabilityDescription field if non-nil, zero value otherwise.

### GetVulnerabilityDescriptionOk

`func (o *PoamResponseGetSystemsDataInner) GetVulnerabilityDescriptionOk() (*string, bool)`

GetVulnerabilityDescriptionOk returns a tuple with the VulnerabilityDescription field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVulnerabilityDescription

`func (o *PoamResponseGetSystemsDataInner) SetVulnerabilityDescription(v string)`

SetVulnerabilityDescription sets VulnerabilityDescription field to given value.

### HasVulnerabilityDescription

`func (o *PoamResponseGetSystemsDataInner) HasVulnerabilityDescription() bool`

HasVulnerabilityDescription returns a boolean if a field has been set.

### GetSourceIdentifyingVulnerability

`func (o *PoamResponseGetSystemsDataInner) GetSourceIdentifyingVulnerability() string`

GetSourceIdentifyingVulnerability returns the SourceIdentifyingVulnerability field if non-nil, zero value otherwise.

### GetSourceIdentifyingVulnerabilityOk

`func (o *PoamResponseGetSystemsDataInner) GetSourceIdentifyingVulnerabilityOk() (*string, bool)`

GetSourceIdentifyingVulnerabilityOk returns a tuple with the SourceIdentifyingVulnerability field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSourceIdentifyingVulnerability

`func (o *PoamResponseGetSystemsDataInner) SetSourceIdentifyingVulnerability(v string)`

SetSourceIdentifyingVulnerability sets SourceIdentifyingVulnerability field to given value.

### HasSourceIdentifyingVulnerability

`func (o *PoamResponseGetSystemsDataInner) HasSourceIdentifyingVulnerability() bool`

HasSourceIdentifyingVulnerability returns a boolean if a field has been set.

### GetPocOrganization

`func (o *PoamResponseGetSystemsDataInner) GetPocOrganization() string`

GetPocOrganization returns the PocOrganization field if non-nil, zero value otherwise.

### GetPocOrganizationOk

`func (o *PoamResponseGetSystemsDataInner) GetPocOrganizationOk() (*string, bool)`

GetPocOrganizationOk returns a tuple with the PocOrganization field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPocOrganization

`func (o *PoamResponseGetSystemsDataInner) SetPocOrganization(v string)`

SetPocOrganization sets PocOrganization field to given value.

### HasPocOrganization

`func (o *PoamResponseGetSystemsDataInner) HasPocOrganization() bool`

HasPocOrganization returns a boolean if a field has been set.

### GetResources

`func (o *PoamResponseGetSystemsDataInner) GetResources() string`

GetResources returns the Resources field if non-nil, zero value otherwise.

### GetResourcesOk

`func (o *PoamResponseGetSystemsDataInner) GetResourcesOk() (*string, bool)`

GetResourcesOk returns a tuple with the Resources field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetResources

`func (o *PoamResponseGetSystemsDataInner) SetResources(v string)`

SetResources sets Resources field to given value.

### HasResources

`func (o *PoamResponseGetSystemsDataInner) HasResources() bool`

HasResources returns a boolean if a field has been set.

### GetIdentifiedInCFOAuditOrOtherReview

`func (o *PoamResponseGetSystemsDataInner) GetIdentifiedInCFOAuditOrOtherReview() bool`

GetIdentifiedInCFOAuditOrOtherReview returns the IdentifiedInCFOAuditOrOtherReview field if non-nil, zero value otherwise.

### GetIdentifiedInCFOAuditOrOtherReviewOk

`func (o *PoamResponseGetSystemsDataInner) GetIdentifiedInCFOAuditOrOtherReviewOk() (*bool, bool)`

GetIdentifiedInCFOAuditOrOtherReviewOk returns a tuple with the IdentifiedInCFOAuditOrOtherReview field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIdentifiedInCFOAuditOrOtherReview

`func (o *PoamResponseGetSystemsDataInner) SetIdentifiedInCFOAuditOrOtherReview(v bool)`

SetIdentifiedInCFOAuditOrOtherReview sets IdentifiedInCFOAuditOrOtherReview field to given value.

### HasIdentifiedInCFOAuditOrOtherReview

`func (o *PoamResponseGetSystemsDataInner) HasIdentifiedInCFOAuditOrOtherReview() bool`

HasIdentifiedInCFOAuditOrOtherReview returns a boolean if a field has been set.

### GetPocFirstName

`func (o *PoamResponseGetSystemsDataInner) GetPocFirstName() string`

GetPocFirstName returns the PocFirstName field if non-nil, zero value otherwise.

### GetPocFirstNameOk

`func (o *PoamResponseGetSystemsDataInner) GetPocFirstNameOk() (*string, bool)`

GetPocFirstNameOk returns a tuple with the PocFirstName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPocFirstName

`func (o *PoamResponseGetSystemsDataInner) SetPocFirstName(v string)`

SetPocFirstName sets PocFirstName field to given value.

### HasPocFirstName

`func (o *PoamResponseGetSystemsDataInner) HasPocFirstName() bool`

HasPocFirstName returns a boolean if a field has been set.

### GetPocLastName

`func (o *PoamResponseGetSystemsDataInner) GetPocLastName() string`

GetPocLastName returns the PocLastName field if non-nil, zero value otherwise.

### GetPocLastNameOk

`func (o *PoamResponseGetSystemsDataInner) GetPocLastNameOk() (*string, bool)`

GetPocLastNameOk returns a tuple with the PocLastName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPocLastName

`func (o *PoamResponseGetSystemsDataInner) SetPocLastName(v string)`

SetPocLastName sets PocLastName field to given value.

### HasPocLastName

`func (o *PoamResponseGetSystemsDataInner) HasPocLastName() bool`

HasPocLastName returns a boolean if a field has been set.

### GetPocEmail

`func (o *PoamResponseGetSystemsDataInner) GetPocEmail() string`

GetPocEmail returns the PocEmail field if non-nil, zero value otherwise.

### GetPocEmailOk

`func (o *PoamResponseGetSystemsDataInner) GetPocEmailOk() (*string, bool)`

GetPocEmailOk returns a tuple with the PocEmail field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPocEmail

`func (o *PoamResponseGetSystemsDataInner) SetPocEmail(v string)`

SetPocEmail sets PocEmail field to given value.

### HasPocEmail

`func (o *PoamResponseGetSystemsDataInner) HasPocEmail() bool`

HasPocEmail returns a boolean if a field has been set.

### GetPocPhoneNumber

`func (o *PoamResponseGetSystemsDataInner) GetPocPhoneNumber() string`

GetPocPhoneNumber returns the PocPhoneNumber field if non-nil, zero value otherwise.

### GetPocPhoneNumberOk

`func (o *PoamResponseGetSystemsDataInner) GetPocPhoneNumberOk() (*string, bool)`

GetPocPhoneNumberOk returns a tuple with the PocPhoneNumber field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPocPhoneNumber

`func (o *PoamResponseGetSystemsDataInner) SetPocPhoneNumber(v string)`

SetPocPhoneNumber sets PocPhoneNumber field to given value.

### HasPocPhoneNumber

`func (o *PoamResponseGetSystemsDataInner) HasPocPhoneNumber() bool`

HasPocPhoneNumber returns a boolean if a field has been set.

### GetSeverity

`func (o *PoamResponseGetSystemsDataInner) GetSeverity() string`

GetSeverity returns the Severity field if non-nil, zero value otherwise.

### GetSeverityOk

`func (o *PoamResponseGetSystemsDataInner) GetSeverityOk() (*string, bool)`

GetSeverityOk returns a tuple with the Severity field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSeverity

`func (o *PoamResponseGetSystemsDataInner) SetSeverity(v string)`

SetSeverity sets Severity field to given value.

### HasSeverity

`func (o *PoamResponseGetSystemsDataInner) HasSeverity() bool`

HasSeverity returns a boolean if a field has been set.

### GetScheduledCompletionDate

`func (o *PoamResponseGetSystemsDataInner) GetScheduledCompletionDate() int64`

GetScheduledCompletionDate returns the ScheduledCompletionDate field if non-nil, zero value otherwise.

### GetScheduledCompletionDateOk

`func (o *PoamResponseGetSystemsDataInner) GetScheduledCompletionDateOk() (*int64, bool)`

GetScheduledCompletionDateOk returns a tuple with the ScheduledCompletionDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetScheduledCompletionDate

`func (o *PoamResponseGetSystemsDataInner) SetScheduledCompletionDate(v int64)`

SetScheduledCompletionDate sets ScheduledCompletionDate field to given value.

### HasScheduledCompletionDate

`func (o *PoamResponseGetSystemsDataInner) HasScheduledCompletionDate() bool`

HasScheduledCompletionDate returns a boolean if a field has been set.

### SetScheduledCompletionDateNil

`func (o *PoamResponseGetSystemsDataInner) SetScheduledCompletionDateNil(b bool)`

 SetScheduledCompletionDateNil sets the value for ScheduledCompletionDate to be an explicit nil

### UnsetScheduledCompletionDate
`func (o *PoamResponseGetSystemsDataInner) UnsetScheduledCompletionDate()`

UnsetScheduledCompletionDate ensures that no value is present for ScheduledCompletionDate, not even an explicit nil
### GetCompletionDate

`func (o *PoamResponseGetSystemsDataInner) GetCompletionDate() int64`

GetCompletionDate returns the CompletionDate field if non-nil, zero value otherwise.

### GetCompletionDateOk

`func (o *PoamResponseGetSystemsDataInner) GetCompletionDateOk() (*int64, bool)`

GetCompletionDateOk returns a tuple with the CompletionDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCompletionDate

`func (o *PoamResponseGetSystemsDataInner) SetCompletionDate(v int64)`

SetCompletionDate sets CompletionDate field to given value.

### HasCompletionDate

`func (o *PoamResponseGetSystemsDataInner) HasCompletionDate() bool`

HasCompletionDate returns a boolean if a field has been set.

### GetComments

`func (o *PoamResponseGetSystemsDataInner) GetComments() string`

GetComments returns the Comments field if non-nil, zero value otherwise.

### GetCommentsOk

`func (o *PoamResponseGetSystemsDataInner) GetCommentsOk() (*string, bool)`

GetCommentsOk returns a tuple with the Comments field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetComments

`func (o *PoamResponseGetSystemsDataInner) SetComments(v string)`

SetComments sets Comments field to given value.

### HasComments

`func (o *PoamResponseGetSystemsDataInner) HasComments() bool`

HasComments returns a boolean if a field has been set.

### GetPersonnelResourcesFundedBaseHours

`func (o *PoamResponseGetSystemsDataInner) GetPersonnelResourcesFundedBaseHours() float32`

GetPersonnelResourcesFundedBaseHours returns the PersonnelResourcesFundedBaseHours field if non-nil, zero value otherwise.

### GetPersonnelResourcesFundedBaseHoursOk

`func (o *PoamResponseGetSystemsDataInner) GetPersonnelResourcesFundedBaseHoursOk() (*float32, bool)`

GetPersonnelResourcesFundedBaseHoursOk returns a tuple with the PersonnelResourcesFundedBaseHours field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPersonnelResourcesFundedBaseHours

`func (o *PoamResponseGetSystemsDataInner) SetPersonnelResourcesFundedBaseHours(v float32)`

SetPersonnelResourcesFundedBaseHours sets PersonnelResourcesFundedBaseHours field to given value.

### HasPersonnelResourcesFundedBaseHours

`func (o *PoamResponseGetSystemsDataInner) HasPersonnelResourcesFundedBaseHours() bool`

HasPersonnelResourcesFundedBaseHours returns a boolean if a field has been set.

### SetPersonnelResourcesFundedBaseHoursNil

`func (o *PoamResponseGetSystemsDataInner) SetPersonnelResourcesFundedBaseHoursNil(b bool)`

 SetPersonnelResourcesFundedBaseHoursNil sets the value for PersonnelResourcesFundedBaseHours to be an explicit nil

### UnsetPersonnelResourcesFundedBaseHours
`func (o *PoamResponseGetSystemsDataInner) UnsetPersonnelResourcesFundedBaseHours()`

UnsetPersonnelResourcesFundedBaseHours ensures that no value is present for PersonnelResourcesFundedBaseHours, not even an explicit nil
### GetPersonnelResourcesCostCode

`func (o *PoamResponseGetSystemsDataInner) GetPersonnelResourcesCostCode() string`

GetPersonnelResourcesCostCode returns the PersonnelResourcesCostCode field if non-nil, zero value otherwise.

### GetPersonnelResourcesCostCodeOk

`func (o *PoamResponseGetSystemsDataInner) GetPersonnelResourcesCostCodeOk() (*string, bool)`

GetPersonnelResourcesCostCodeOk returns a tuple with the PersonnelResourcesCostCode field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPersonnelResourcesCostCode

`func (o *PoamResponseGetSystemsDataInner) SetPersonnelResourcesCostCode(v string)`

SetPersonnelResourcesCostCode sets PersonnelResourcesCostCode field to given value.

### HasPersonnelResourcesCostCode

`func (o *PoamResponseGetSystemsDataInner) HasPersonnelResourcesCostCode() bool`

HasPersonnelResourcesCostCode returns a boolean if a field has been set.

### SetPersonnelResourcesCostCodeNil

`func (o *PoamResponseGetSystemsDataInner) SetPersonnelResourcesCostCodeNil(b bool)`

 SetPersonnelResourcesCostCodeNil sets the value for PersonnelResourcesCostCode to be an explicit nil

### UnsetPersonnelResourcesCostCode
`func (o *PoamResponseGetSystemsDataInner) UnsetPersonnelResourcesCostCode()`

UnsetPersonnelResourcesCostCode ensures that no value is present for PersonnelResourcesCostCode, not even an explicit nil
### GetPersonnelResourcesUnfundedBaseHours

`func (o *PoamResponseGetSystemsDataInner) GetPersonnelResourcesUnfundedBaseHours() float32`

GetPersonnelResourcesUnfundedBaseHours returns the PersonnelResourcesUnfundedBaseHours field if non-nil, zero value otherwise.

### GetPersonnelResourcesUnfundedBaseHoursOk

`func (o *PoamResponseGetSystemsDataInner) GetPersonnelResourcesUnfundedBaseHoursOk() (*float32, bool)`

GetPersonnelResourcesUnfundedBaseHoursOk returns a tuple with the PersonnelResourcesUnfundedBaseHours field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPersonnelResourcesUnfundedBaseHours

`func (o *PoamResponseGetSystemsDataInner) SetPersonnelResourcesUnfundedBaseHours(v float32)`

SetPersonnelResourcesUnfundedBaseHours sets PersonnelResourcesUnfundedBaseHours field to given value.

### HasPersonnelResourcesUnfundedBaseHours

`func (o *PoamResponseGetSystemsDataInner) HasPersonnelResourcesUnfundedBaseHours() bool`

HasPersonnelResourcesUnfundedBaseHours returns a boolean if a field has been set.

### SetPersonnelResourcesUnfundedBaseHoursNil

`func (o *PoamResponseGetSystemsDataInner) SetPersonnelResourcesUnfundedBaseHoursNil(b bool)`

 SetPersonnelResourcesUnfundedBaseHoursNil sets the value for PersonnelResourcesUnfundedBaseHours to be an explicit nil

### UnsetPersonnelResourcesUnfundedBaseHours
`func (o *PoamResponseGetSystemsDataInner) UnsetPersonnelResourcesUnfundedBaseHours()`

UnsetPersonnelResourcesUnfundedBaseHours ensures that no value is present for PersonnelResourcesUnfundedBaseHours, not even an explicit nil
### GetPersonnelResourcesNonfundingObstacle

`func (o *PoamResponseGetSystemsDataInner) GetPersonnelResourcesNonfundingObstacle() string`

GetPersonnelResourcesNonfundingObstacle returns the PersonnelResourcesNonfundingObstacle field if non-nil, zero value otherwise.

### GetPersonnelResourcesNonfundingObstacleOk

`func (o *PoamResponseGetSystemsDataInner) GetPersonnelResourcesNonfundingObstacleOk() (*string, bool)`

GetPersonnelResourcesNonfundingObstacleOk returns a tuple with the PersonnelResourcesNonfundingObstacle field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPersonnelResourcesNonfundingObstacle

`func (o *PoamResponseGetSystemsDataInner) SetPersonnelResourcesNonfundingObstacle(v string)`

SetPersonnelResourcesNonfundingObstacle sets PersonnelResourcesNonfundingObstacle field to given value.

### HasPersonnelResourcesNonfundingObstacle

`func (o *PoamResponseGetSystemsDataInner) HasPersonnelResourcesNonfundingObstacle() bool`

HasPersonnelResourcesNonfundingObstacle returns a boolean if a field has been set.

### SetPersonnelResourcesNonfundingObstacleNil

`func (o *PoamResponseGetSystemsDataInner) SetPersonnelResourcesNonfundingObstacleNil(b bool)`

 SetPersonnelResourcesNonfundingObstacleNil sets the value for PersonnelResourcesNonfundingObstacle to be an explicit nil

### UnsetPersonnelResourcesNonfundingObstacle
`func (o *PoamResponseGetSystemsDataInner) UnsetPersonnelResourcesNonfundingObstacle()`

UnsetPersonnelResourcesNonfundingObstacle ensures that no value is present for PersonnelResourcesNonfundingObstacle, not even an explicit nil
### GetPersonnelResourcesNonfundingObstacleOtherReason

`func (o *PoamResponseGetSystemsDataInner) GetPersonnelResourcesNonfundingObstacleOtherReason() string`

GetPersonnelResourcesNonfundingObstacleOtherReason returns the PersonnelResourcesNonfundingObstacleOtherReason field if non-nil, zero value otherwise.

### GetPersonnelResourcesNonfundingObstacleOtherReasonOk

`func (o *PoamResponseGetSystemsDataInner) GetPersonnelResourcesNonfundingObstacleOtherReasonOk() (*string, bool)`

GetPersonnelResourcesNonfundingObstacleOtherReasonOk returns a tuple with the PersonnelResourcesNonfundingObstacleOtherReason field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPersonnelResourcesNonfundingObstacleOtherReason

`func (o *PoamResponseGetSystemsDataInner) SetPersonnelResourcesNonfundingObstacleOtherReason(v string)`

SetPersonnelResourcesNonfundingObstacleOtherReason sets PersonnelResourcesNonfundingObstacleOtherReason field to given value.

### HasPersonnelResourcesNonfundingObstacleOtherReason

`func (o *PoamResponseGetSystemsDataInner) HasPersonnelResourcesNonfundingObstacleOtherReason() bool`

HasPersonnelResourcesNonfundingObstacleOtherReason returns a boolean if a field has been set.

### SetPersonnelResourcesNonfundingObstacleOtherReasonNil

`func (o *PoamResponseGetSystemsDataInner) SetPersonnelResourcesNonfundingObstacleOtherReasonNil(b bool)`

 SetPersonnelResourcesNonfundingObstacleOtherReasonNil sets the value for PersonnelResourcesNonfundingObstacleOtherReason to be an explicit nil

### UnsetPersonnelResourcesNonfundingObstacleOtherReason
`func (o *PoamResponseGetSystemsDataInner) UnsetPersonnelResourcesNonfundingObstacleOtherReason()`

UnsetPersonnelResourcesNonfundingObstacleOtherReason ensures that no value is present for PersonnelResourcesNonfundingObstacleOtherReason, not even an explicit nil
### GetNonPersonnelResourcesFundedAmount

`func (o *PoamResponseGetSystemsDataInner) GetNonPersonnelResourcesFundedAmount() float32`

GetNonPersonnelResourcesFundedAmount returns the NonPersonnelResourcesFundedAmount field if non-nil, zero value otherwise.

### GetNonPersonnelResourcesFundedAmountOk

`func (o *PoamResponseGetSystemsDataInner) GetNonPersonnelResourcesFundedAmountOk() (*float32, bool)`

GetNonPersonnelResourcesFundedAmountOk returns a tuple with the NonPersonnelResourcesFundedAmount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNonPersonnelResourcesFundedAmount

`func (o *PoamResponseGetSystemsDataInner) SetNonPersonnelResourcesFundedAmount(v float32)`

SetNonPersonnelResourcesFundedAmount sets NonPersonnelResourcesFundedAmount field to given value.

### HasNonPersonnelResourcesFundedAmount

`func (o *PoamResponseGetSystemsDataInner) HasNonPersonnelResourcesFundedAmount() bool`

HasNonPersonnelResourcesFundedAmount returns a boolean if a field has been set.

### SetNonPersonnelResourcesFundedAmountNil

`func (o *PoamResponseGetSystemsDataInner) SetNonPersonnelResourcesFundedAmountNil(b bool)`

 SetNonPersonnelResourcesFundedAmountNil sets the value for NonPersonnelResourcesFundedAmount to be an explicit nil

### UnsetNonPersonnelResourcesFundedAmount
`func (o *PoamResponseGetSystemsDataInner) UnsetNonPersonnelResourcesFundedAmount()`

UnsetNonPersonnelResourcesFundedAmount ensures that no value is present for NonPersonnelResourcesFundedAmount, not even an explicit nil
### GetNonPersonnelResourcesCostCode

`func (o *PoamResponseGetSystemsDataInner) GetNonPersonnelResourcesCostCode() string`

GetNonPersonnelResourcesCostCode returns the NonPersonnelResourcesCostCode field if non-nil, zero value otherwise.

### GetNonPersonnelResourcesCostCodeOk

`func (o *PoamResponseGetSystemsDataInner) GetNonPersonnelResourcesCostCodeOk() (*string, bool)`

GetNonPersonnelResourcesCostCodeOk returns a tuple with the NonPersonnelResourcesCostCode field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNonPersonnelResourcesCostCode

`func (o *PoamResponseGetSystemsDataInner) SetNonPersonnelResourcesCostCode(v string)`

SetNonPersonnelResourcesCostCode sets NonPersonnelResourcesCostCode field to given value.

### HasNonPersonnelResourcesCostCode

`func (o *PoamResponseGetSystemsDataInner) HasNonPersonnelResourcesCostCode() bool`

HasNonPersonnelResourcesCostCode returns a boolean if a field has been set.

### SetNonPersonnelResourcesCostCodeNil

`func (o *PoamResponseGetSystemsDataInner) SetNonPersonnelResourcesCostCodeNil(b bool)`

 SetNonPersonnelResourcesCostCodeNil sets the value for NonPersonnelResourcesCostCode to be an explicit nil

### UnsetNonPersonnelResourcesCostCode
`func (o *PoamResponseGetSystemsDataInner) UnsetNonPersonnelResourcesCostCode()`

UnsetNonPersonnelResourcesCostCode ensures that no value is present for NonPersonnelResourcesCostCode, not even an explicit nil
### GetNonPersonnelResourcesUnfundedAmount

`func (o *PoamResponseGetSystemsDataInner) GetNonPersonnelResourcesUnfundedAmount() float32`

GetNonPersonnelResourcesUnfundedAmount returns the NonPersonnelResourcesUnfundedAmount field if non-nil, zero value otherwise.

### GetNonPersonnelResourcesUnfundedAmountOk

`func (o *PoamResponseGetSystemsDataInner) GetNonPersonnelResourcesUnfundedAmountOk() (*float32, bool)`

GetNonPersonnelResourcesUnfundedAmountOk returns a tuple with the NonPersonnelResourcesUnfundedAmount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNonPersonnelResourcesUnfundedAmount

`func (o *PoamResponseGetSystemsDataInner) SetNonPersonnelResourcesUnfundedAmount(v float32)`

SetNonPersonnelResourcesUnfundedAmount sets NonPersonnelResourcesUnfundedAmount field to given value.

### HasNonPersonnelResourcesUnfundedAmount

`func (o *PoamResponseGetSystemsDataInner) HasNonPersonnelResourcesUnfundedAmount() bool`

HasNonPersonnelResourcesUnfundedAmount returns a boolean if a field has been set.

### SetNonPersonnelResourcesUnfundedAmountNil

`func (o *PoamResponseGetSystemsDataInner) SetNonPersonnelResourcesUnfundedAmountNil(b bool)`

 SetNonPersonnelResourcesUnfundedAmountNil sets the value for NonPersonnelResourcesUnfundedAmount to be an explicit nil

### UnsetNonPersonnelResourcesUnfundedAmount
`func (o *PoamResponseGetSystemsDataInner) UnsetNonPersonnelResourcesUnfundedAmount()`

UnsetNonPersonnelResourcesUnfundedAmount ensures that no value is present for NonPersonnelResourcesUnfundedAmount, not even an explicit nil
### GetNonPersonnelResourcesNonfundingObstacle

`func (o *PoamResponseGetSystemsDataInner) GetNonPersonnelResourcesNonfundingObstacle() string`

GetNonPersonnelResourcesNonfundingObstacle returns the NonPersonnelResourcesNonfundingObstacle field if non-nil, zero value otherwise.

### GetNonPersonnelResourcesNonfundingObstacleOk

`func (o *PoamResponseGetSystemsDataInner) GetNonPersonnelResourcesNonfundingObstacleOk() (*string, bool)`

GetNonPersonnelResourcesNonfundingObstacleOk returns a tuple with the NonPersonnelResourcesNonfundingObstacle field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNonPersonnelResourcesNonfundingObstacle

`func (o *PoamResponseGetSystemsDataInner) SetNonPersonnelResourcesNonfundingObstacle(v string)`

SetNonPersonnelResourcesNonfundingObstacle sets NonPersonnelResourcesNonfundingObstacle field to given value.

### HasNonPersonnelResourcesNonfundingObstacle

`func (o *PoamResponseGetSystemsDataInner) HasNonPersonnelResourcesNonfundingObstacle() bool`

HasNonPersonnelResourcesNonfundingObstacle returns a boolean if a field has been set.

### SetNonPersonnelResourcesNonfundingObstacleNil

`func (o *PoamResponseGetSystemsDataInner) SetNonPersonnelResourcesNonfundingObstacleNil(b bool)`

 SetNonPersonnelResourcesNonfundingObstacleNil sets the value for NonPersonnelResourcesNonfundingObstacle to be an explicit nil

### UnsetNonPersonnelResourcesNonfundingObstacle
`func (o *PoamResponseGetSystemsDataInner) UnsetNonPersonnelResourcesNonfundingObstacle()`

UnsetNonPersonnelResourcesNonfundingObstacle ensures that no value is present for NonPersonnelResourcesNonfundingObstacle, not even an explicit nil
### GetNonPersonnelResourcesNonfundingObstacleOtherReason

`func (o *PoamResponseGetSystemsDataInner) GetNonPersonnelResourcesNonfundingObstacleOtherReason() string`

GetNonPersonnelResourcesNonfundingObstacleOtherReason returns the NonPersonnelResourcesNonfundingObstacleOtherReason field if non-nil, zero value otherwise.

### GetNonPersonnelResourcesNonfundingObstacleOtherReasonOk

`func (o *PoamResponseGetSystemsDataInner) GetNonPersonnelResourcesNonfundingObstacleOtherReasonOk() (*string, bool)`

GetNonPersonnelResourcesNonfundingObstacleOtherReasonOk returns a tuple with the NonPersonnelResourcesNonfundingObstacleOtherReason field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNonPersonnelResourcesNonfundingObstacleOtherReason

`func (o *PoamResponseGetSystemsDataInner) SetNonPersonnelResourcesNonfundingObstacleOtherReason(v string)`

SetNonPersonnelResourcesNonfundingObstacleOtherReason sets NonPersonnelResourcesNonfundingObstacleOtherReason field to given value.

### HasNonPersonnelResourcesNonfundingObstacleOtherReason

`func (o *PoamResponseGetSystemsDataInner) HasNonPersonnelResourcesNonfundingObstacleOtherReason() bool`

HasNonPersonnelResourcesNonfundingObstacleOtherReason returns a boolean if a field has been set.

### SetNonPersonnelResourcesNonfundingObstacleOtherReasonNil

`func (o *PoamResponseGetSystemsDataInner) SetNonPersonnelResourcesNonfundingObstacleOtherReasonNil(b bool)`

 SetNonPersonnelResourcesNonfundingObstacleOtherReasonNil sets the value for NonPersonnelResourcesNonfundingObstacleOtherReason to be an explicit nil

### UnsetNonPersonnelResourcesNonfundingObstacleOtherReason
`func (o *PoamResponseGetSystemsDataInner) UnsetNonPersonnelResourcesNonfundingObstacleOtherReason()`

UnsetNonPersonnelResourcesNonfundingObstacleOtherReason ensures that no value is present for NonPersonnelResourcesNonfundingObstacleOtherReason, not even an explicit nil
### GetMilestones

`func (o *PoamResponseGetSystemsDataInner) GetMilestones() []MilestonesGet`

GetMilestones returns the Milestones field if non-nil, zero value otherwise.

### GetMilestonesOk

`func (o *PoamResponseGetSystemsDataInner) GetMilestonesOk() (*[]MilestonesGet, bool)`

GetMilestonesOk returns a tuple with the Milestones field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMilestones

`func (o *PoamResponseGetSystemsDataInner) SetMilestones(v []MilestonesGet)`

SetMilestones sets Milestones field to given value.

### HasMilestones

`func (o *PoamResponseGetSystemsDataInner) HasMilestones() bool`

HasMilestones returns a boolean if a field has been set.

### GetExternalUid

`func (o *PoamResponseGetSystemsDataInner) GetExternalUid() string`

GetExternalUid returns the ExternalUid field if non-nil, zero value otherwise.

### GetExternalUidOk

`func (o *PoamResponseGetSystemsDataInner) GetExternalUidOk() (*string, bool)`

GetExternalUidOk returns a tuple with the ExternalUid field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExternalUid

`func (o *PoamResponseGetSystemsDataInner) SetExternalUid(v string)`

SetExternalUid sets ExternalUid field to given value.

### HasExternalUid

`func (o *PoamResponseGetSystemsDataInner) HasExternalUid() bool`

HasExternalUid returns a boolean if a field has been set.

### GetControlAcronym

`func (o *PoamResponseGetSystemsDataInner) GetControlAcronym() string`

GetControlAcronym returns the ControlAcronym field if non-nil, zero value otherwise.

### GetControlAcronymOk

`func (o *PoamResponseGetSystemsDataInner) GetControlAcronymOk() (*string, bool)`

GetControlAcronymOk returns a tuple with the ControlAcronym field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetControlAcronym

`func (o *PoamResponseGetSystemsDataInner) SetControlAcronym(v string)`

SetControlAcronym sets ControlAcronym field to given value.

### HasControlAcronym

`func (o *PoamResponseGetSystemsDataInner) HasControlAcronym() bool`

HasControlAcronym returns a boolean if a field has been set.

### GetAssessmentProcedure

`func (o *PoamResponseGetSystemsDataInner) GetAssessmentProcedure() string`

GetAssessmentProcedure returns the AssessmentProcedure field if non-nil, zero value otherwise.

### GetAssessmentProcedureOk

`func (o *PoamResponseGetSystemsDataInner) GetAssessmentProcedureOk() (*string, bool)`

GetAssessmentProcedureOk returns a tuple with the AssessmentProcedure field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAssessmentProcedure

`func (o *PoamResponseGetSystemsDataInner) SetAssessmentProcedure(v string)`

SetAssessmentProcedure sets AssessmentProcedure field to given value.

### HasAssessmentProcedure

`func (o *PoamResponseGetSystemsDataInner) HasAssessmentProcedure() bool`

HasAssessmentProcedure returns a boolean if a field has been set.

### GetSecurityChecks

`func (o *PoamResponseGetSystemsDataInner) GetSecurityChecks() string`

GetSecurityChecks returns the SecurityChecks field if non-nil, zero value otherwise.

### GetSecurityChecksOk

`func (o *PoamResponseGetSystemsDataInner) GetSecurityChecksOk() (*string, bool)`

GetSecurityChecksOk returns a tuple with the SecurityChecks field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSecurityChecks

`func (o *PoamResponseGetSystemsDataInner) SetSecurityChecks(v string)`

SetSecurityChecks sets SecurityChecks field to given value.

### HasSecurityChecks

`func (o *PoamResponseGetSystemsDataInner) HasSecurityChecks() bool`

HasSecurityChecks returns a boolean if a field has been set.

### GetRawSeverity

`func (o *PoamResponseGetSystemsDataInner) GetRawSeverity() string`

GetRawSeverity returns the RawSeverity field if non-nil, zero value otherwise.

### GetRawSeverityOk

`func (o *PoamResponseGetSystemsDataInner) GetRawSeverityOk() (*string, bool)`

GetRawSeverityOk returns a tuple with the RawSeverity field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRawSeverity

`func (o *PoamResponseGetSystemsDataInner) SetRawSeverity(v string)`

SetRawSeverity sets RawSeverity field to given value.

### HasRawSeverity

`func (o *PoamResponseGetSystemsDataInner) HasRawSeverity() bool`

HasRawSeverity returns a boolean if a field has been set.

### GetRelevanceOfThreat

`func (o *PoamResponseGetSystemsDataInner) GetRelevanceOfThreat() string`

GetRelevanceOfThreat returns the RelevanceOfThreat field if non-nil, zero value otherwise.

### GetRelevanceOfThreatOk

`func (o *PoamResponseGetSystemsDataInner) GetRelevanceOfThreatOk() (*string, bool)`

GetRelevanceOfThreatOk returns a tuple with the RelevanceOfThreat field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRelevanceOfThreat

`func (o *PoamResponseGetSystemsDataInner) SetRelevanceOfThreat(v string)`

SetRelevanceOfThreat sets RelevanceOfThreat field to given value.

### HasRelevanceOfThreat

`func (o *PoamResponseGetSystemsDataInner) HasRelevanceOfThreat() bool`

HasRelevanceOfThreat returns a boolean if a field has been set.

### GetLikelihood

`func (o *PoamResponseGetSystemsDataInner) GetLikelihood() string`

GetLikelihood returns the Likelihood field if non-nil, zero value otherwise.

### GetLikelihoodOk

`func (o *PoamResponseGetSystemsDataInner) GetLikelihoodOk() (*string, bool)`

GetLikelihoodOk returns a tuple with the Likelihood field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLikelihood

`func (o *PoamResponseGetSystemsDataInner) SetLikelihood(v string)`

SetLikelihood sets Likelihood field to given value.

### HasLikelihood

`func (o *PoamResponseGetSystemsDataInner) HasLikelihood() bool`

HasLikelihood returns a boolean if a field has been set.

### GetImpact

`func (o *PoamResponseGetSystemsDataInner) GetImpact() string`

GetImpact returns the Impact field if non-nil, zero value otherwise.

### GetImpactOk

`func (o *PoamResponseGetSystemsDataInner) GetImpactOk() (*string, bool)`

GetImpactOk returns a tuple with the Impact field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetImpact

`func (o *PoamResponseGetSystemsDataInner) SetImpact(v string)`

SetImpact sets Impact field to given value.

### HasImpact

`func (o *PoamResponseGetSystemsDataInner) HasImpact() bool`

HasImpact returns a boolean if a field has been set.

### GetImpactDescription

`func (o *PoamResponseGetSystemsDataInner) GetImpactDescription() string`

GetImpactDescription returns the ImpactDescription field if non-nil, zero value otherwise.

### GetImpactDescriptionOk

`func (o *PoamResponseGetSystemsDataInner) GetImpactDescriptionOk() (*string, bool)`

GetImpactDescriptionOk returns a tuple with the ImpactDescription field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetImpactDescription

`func (o *PoamResponseGetSystemsDataInner) SetImpactDescription(v string)`

SetImpactDescription sets ImpactDescription field to given value.

### HasImpactDescription

`func (o *PoamResponseGetSystemsDataInner) HasImpactDescription() bool`

HasImpactDescription returns a boolean if a field has been set.

### GetResidualRiskLevel

`func (o *PoamResponseGetSystemsDataInner) GetResidualRiskLevel() string`

GetResidualRiskLevel returns the ResidualRiskLevel field if non-nil, zero value otherwise.

### GetResidualRiskLevelOk

`func (o *PoamResponseGetSystemsDataInner) GetResidualRiskLevelOk() (*string, bool)`

GetResidualRiskLevelOk returns a tuple with the ResidualRiskLevel field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetResidualRiskLevel

`func (o *PoamResponseGetSystemsDataInner) SetResidualRiskLevel(v string)`

SetResidualRiskLevel sets ResidualRiskLevel field to given value.

### HasResidualRiskLevel

`func (o *PoamResponseGetSystemsDataInner) HasResidualRiskLevel() bool`

HasResidualRiskLevel returns a boolean if a field has been set.

### GetRecommendations

`func (o *PoamResponseGetSystemsDataInner) GetRecommendations() string`

GetRecommendations returns the Recommendations field if non-nil, zero value otherwise.

### GetRecommendationsOk

`func (o *PoamResponseGetSystemsDataInner) GetRecommendationsOk() (*string, bool)`

GetRecommendationsOk returns a tuple with the Recommendations field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRecommendations

`func (o *PoamResponseGetSystemsDataInner) SetRecommendations(v string)`

SetRecommendations sets Recommendations field to given value.

### HasRecommendations

`func (o *PoamResponseGetSystemsDataInner) HasRecommendations() bool`

HasRecommendations returns a boolean if a field has been set.

### GetMitigations

`func (o *PoamResponseGetSystemsDataInner) GetMitigations() string`

GetMitigations returns the Mitigations field if non-nil, zero value otherwise.

### GetMitigationsOk

`func (o *PoamResponseGetSystemsDataInner) GetMitigationsOk() (*string, bool)`

GetMitigationsOk returns a tuple with the Mitigations field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMitigations

`func (o *PoamResponseGetSystemsDataInner) SetMitigations(v string)`

SetMitigations sets Mitigations field to given value.

### HasMitigations

`func (o *PoamResponseGetSystemsDataInner) HasMitigations() bool`

HasMitigations returns a boolean if a field has been set.

### GetResultingResidualRiskLevelAfterProposedMitigations

`func (o *PoamResponseGetSystemsDataInner) GetResultingResidualRiskLevelAfterProposedMitigations() string`

GetResultingResidualRiskLevelAfterProposedMitigations returns the ResultingResidualRiskLevelAfterProposedMitigations field if non-nil, zero value otherwise.

### GetResultingResidualRiskLevelAfterProposedMitigationsOk

`func (o *PoamResponseGetSystemsDataInner) GetResultingResidualRiskLevelAfterProposedMitigationsOk() (*string, bool)`

GetResultingResidualRiskLevelAfterProposedMitigationsOk returns a tuple with the ResultingResidualRiskLevelAfterProposedMitigations field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetResultingResidualRiskLevelAfterProposedMitigations

`func (o *PoamResponseGetSystemsDataInner) SetResultingResidualRiskLevelAfterProposedMitigations(v string)`

SetResultingResidualRiskLevelAfterProposedMitigations sets ResultingResidualRiskLevelAfterProposedMitigations field to given value.

### HasResultingResidualRiskLevelAfterProposedMitigations

`func (o *PoamResponseGetSystemsDataInner) HasResultingResidualRiskLevelAfterProposedMitigations() bool`

HasResultingResidualRiskLevelAfterProposedMitigations returns a boolean if a field has been set.

### SetResultingResidualRiskLevelAfterProposedMitigationsNil

`func (o *PoamResponseGetSystemsDataInner) SetResultingResidualRiskLevelAfterProposedMitigationsNil(b bool)`

 SetResultingResidualRiskLevelAfterProposedMitigationsNil sets the value for ResultingResidualRiskLevelAfterProposedMitigations to be an explicit nil

### UnsetResultingResidualRiskLevelAfterProposedMitigations
`func (o *PoamResponseGetSystemsDataInner) UnsetResultingResidualRiskLevelAfterProposedMitigations()`

UnsetResultingResidualRiskLevelAfterProposedMitigations ensures that no value is present for ResultingResidualRiskLevelAfterProposedMitigations, not even an explicit nil
### GetPredisposingConditions

`func (o *PoamResponseGetSystemsDataInner) GetPredisposingConditions() string`

GetPredisposingConditions returns the PredisposingConditions field if non-nil, zero value otherwise.

### GetPredisposingConditionsOk

`func (o *PoamResponseGetSystemsDataInner) GetPredisposingConditionsOk() (*string, bool)`

GetPredisposingConditionsOk returns a tuple with the PredisposingConditions field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPredisposingConditions

`func (o *PoamResponseGetSystemsDataInner) SetPredisposingConditions(v string)`

SetPredisposingConditions sets PredisposingConditions field to given value.

### HasPredisposingConditions

`func (o *PoamResponseGetSystemsDataInner) HasPredisposingConditions() bool`

HasPredisposingConditions returns a boolean if a field has been set.

### SetPredisposingConditionsNil

`func (o *PoamResponseGetSystemsDataInner) SetPredisposingConditionsNil(b bool)`

 SetPredisposingConditionsNil sets the value for PredisposingConditions to be an explicit nil

### UnsetPredisposingConditions
`func (o *PoamResponseGetSystemsDataInner) UnsetPredisposingConditions()`

UnsetPredisposingConditions ensures that no value is present for PredisposingConditions, not even an explicit nil
### GetThreatDescription

`func (o *PoamResponseGetSystemsDataInner) GetThreatDescription() string`

GetThreatDescription returns the ThreatDescription field if non-nil, zero value otherwise.

### GetThreatDescriptionOk

`func (o *PoamResponseGetSystemsDataInner) GetThreatDescriptionOk() (*string, bool)`

GetThreatDescriptionOk returns a tuple with the ThreatDescription field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetThreatDescription

`func (o *PoamResponseGetSystemsDataInner) SetThreatDescription(v string)`

SetThreatDescription sets ThreatDescription field to given value.

### HasThreatDescription

`func (o *PoamResponseGetSystemsDataInner) HasThreatDescription() bool`

HasThreatDescription returns a boolean if a field has been set.

### SetThreatDescriptionNil

`func (o *PoamResponseGetSystemsDataInner) SetThreatDescriptionNil(b bool)`

 SetThreatDescriptionNil sets the value for ThreatDescription to be an explicit nil

### UnsetThreatDescription
`func (o *PoamResponseGetSystemsDataInner) UnsetThreatDescription()`

UnsetThreatDescription ensures that no value is present for ThreatDescription, not even an explicit nil
### GetDevicesAffected

`func (o *PoamResponseGetSystemsDataInner) GetDevicesAffected() string`

GetDevicesAffected returns the DevicesAffected field if non-nil, zero value otherwise.

### GetDevicesAffectedOk

`func (o *PoamResponseGetSystemsDataInner) GetDevicesAffectedOk() (*string, bool)`

GetDevicesAffectedOk returns a tuple with the DevicesAffected field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDevicesAffected

`func (o *PoamResponseGetSystemsDataInner) SetDevicesAffected(v string)`

SetDevicesAffected sets DevicesAffected field to given value.

### HasDevicesAffected

`func (o *PoamResponseGetSystemsDataInner) HasDevicesAffected() bool`

HasDevicesAffected returns a boolean if a field has been set.

### SetDevicesAffectedNil

`func (o *PoamResponseGetSystemsDataInner) SetDevicesAffectedNil(b bool)`

 SetDevicesAffectedNil sets the value for DevicesAffected to be an explicit nil

### UnsetDevicesAffected
`func (o *PoamResponseGetSystemsDataInner) UnsetDevicesAffected()`

UnsetDevicesAffected ensures that no value is present for DevicesAffected, not even an explicit nil
### GetConditionId

`func (o *PoamResponseGetSystemsDataInner) GetConditionId() string`

GetConditionId returns the ConditionId field if non-nil, zero value otherwise.

### GetConditionIdOk

`func (o *PoamResponseGetSystemsDataInner) GetConditionIdOk() (*string, bool)`

GetConditionIdOk returns a tuple with the ConditionId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetConditionId

`func (o *PoamResponseGetSystemsDataInner) SetConditionId(v string)`

SetConditionId sets ConditionId field to given value.

### HasConditionId

`func (o *PoamResponseGetSystemsDataInner) HasConditionId() bool`

HasConditionId returns a boolean if a field has been set.

### SetConditionIdNil

`func (o *PoamResponseGetSystemsDataInner) SetConditionIdNil(b bool)`

 SetConditionIdNil sets the value for ConditionId to be an explicit nil

### UnsetConditionId
`func (o *PoamResponseGetSystemsDataInner) UnsetConditionId()`

UnsetConditionId ensures that no value is present for ConditionId, not even an explicit nil
### GetIsInherited

`func (o *PoamResponseGetSystemsDataInner) GetIsInherited() bool`

GetIsInherited returns the IsInherited field if non-nil, zero value otherwise.

### GetIsInheritedOk

`func (o *PoamResponseGetSystemsDataInner) GetIsInheritedOk() (*bool, bool)`

GetIsInheritedOk returns a tuple with the IsInherited field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsInherited

`func (o *PoamResponseGetSystemsDataInner) SetIsInherited(v bool)`

SetIsInherited sets IsInherited field to given value.

### HasIsInherited

`func (o *PoamResponseGetSystemsDataInner) HasIsInherited() bool`

HasIsInherited returns a boolean if a field has been set.

### SetIsInheritedNil

`func (o *PoamResponseGetSystemsDataInner) SetIsInheritedNil(b bool)`

 SetIsInheritedNil sets the value for IsInherited to be an explicit nil

### UnsetIsInherited
`func (o *PoamResponseGetSystemsDataInner) UnsetIsInherited()`

UnsetIsInherited ensures that no value is present for IsInherited, not even an explicit nil
### GetCci

`func (o *PoamResponseGetSystemsDataInner) GetCci() string`

GetCci returns the Cci field if non-nil, zero value otherwise.

### GetCciOk

`func (o *PoamResponseGetSystemsDataInner) GetCciOk() (*string, bool)`

GetCciOk returns a tuple with the Cci field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCci

`func (o *PoamResponseGetSystemsDataInner) SetCci(v string)`

SetCci sets Cci field to given value.

### HasCci

`func (o *PoamResponseGetSystemsDataInner) HasCci() bool`

HasCci returns a boolean if a field has been set.

### SetCciNil

`func (o *PoamResponseGetSystemsDataInner) SetCciNil(b bool)`

 SetCciNil sets the value for Cci to be an explicit nil

### UnsetCci
`func (o *PoamResponseGetSystemsDataInner) UnsetCci()`

UnsetCci ensures that no value is present for Cci, not even an explicit nil
### GetReviewStatus

`func (o *PoamResponseGetSystemsDataInner) GetReviewStatus() string`

GetReviewStatus returns the ReviewStatus field if non-nil, zero value otherwise.

### GetReviewStatusOk

`func (o *PoamResponseGetSystemsDataInner) GetReviewStatusOk() (*string, bool)`

GetReviewStatusOk returns a tuple with the ReviewStatus field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetReviewStatus

`func (o *PoamResponseGetSystemsDataInner) SetReviewStatus(v string)`

SetReviewStatus sets ReviewStatus field to given value.

### HasReviewStatus

`func (o *PoamResponseGetSystemsDataInner) HasReviewStatus() bool`

HasReviewStatus returns a boolean if a field has been set.

### SetReviewStatusNil

`func (o *PoamResponseGetSystemsDataInner) SetReviewStatusNil(b bool)`

 SetReviewStatusNil sets the value for ReviewStatus to be an explicit nil

### UnsetReviewStatus
`func (o *PoamResponseGetSystemsDataInner) UnsetReviewStatus()`

UnsetReviewStatus ensures that no value is present for ReviewStatus, not even an explicit nil
### GetCreatedDate

`func (o *PoamResponseGetSystemsDataInner) GetCreatedDate() int64`

GetCreatedDate returns the CreatedDate field if non-nil, zero value otherwise.

### GetCreatedDateOk

`func (o *PoamResponseGetSystemsDataInner) GetCreatedDateOk() (*int64, bool)`

GetCreatedDateOk returns a tuple with the CreatedDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedDate

`func (o *PoamResponseGetSystemsDataInner) SetCreatedDate(v int64)`

SetCreatedDate sets CreatedDate field to given value.

### HasCreatedDate

`func (o *PoamResponseGetSystemsDataInner) HasCreatedDate() bool`

HasCreatedDate returns a boolean if a field has been set.

### GetExtensionDate

`func (o *PoamResponseGetSystemsDataInner) GetExtensionDate() int64`

GetExtensionDate returns the ExtensionDate field if non-nil, zero value otherwise.

### GetExtensionDateOk

`func (o *PoamResponseGetSystemsDataInner) GetExtensionDateOk() (*int64, bool)`

GetExtensionDateOk returns a tuple with the ExtensionDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExtensionDate

`func (o *PoamResponseGetSystemsDataInner) SetExtensionDate(v int64)`

SetExtensionDate sets ExtensionDate field to given value.

### HasExtensionDate

`func (o *PoamResponseGetSystemsDataInner) HasExtensionDate() bool`

HasExtensionDate returns a boolean if a field has been set.

### SetExtensionDateNil

`func (o *PoamResponseGetSystemsDataInner) SetExtensionDateNil(b bool)`

 SetExtensionDateNil sets the value for ExtensionDate to be an explicit nil

### UnsetExtensionDate
`func (o *PoamResponseGetSystemsDataInner) UnsetExtensionDate()`

UnsetExtensionDate ensures that no value is present for ExtensionDate, not even an explicit nil
### GetPendingExtensionDate

`func (o *PoamResponseGetSystemsDataInner) GetPendingExtensionDate() int64`

GetPendingExtensionDate returns the PendingExtensionDate field if non-nil, zero value otherwise.

### GetPendingExtensionDateOk

`func (o *PoamResponseGetSystemsDataInner) GetPendingExtensionDateOk() (*int64, bool)`

GetPendingExtensionDateOk returns a tuple with the PendingExtensionDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPendingExtensionDate

`func (o *PoamResponseGetSystemsDataInner) SetPendingExtensionDate(v int64)`

SetPendingExtensionDate sets PendingExtensionDate field to given value.

### HasPendingExtensionDate

`func (o *PoamResponseGetSystemsDataInner) HasPendingExtensionDate() bool`

HasPendingExtensionDate returns a boolean if a field has been set.

### SetPendingExtensionDateNil

`func (o *PoamResponseGetSystemsDataInner) SetPendingExtensionDateNil(b bool)`

 SetPendingExtensionDateNil sets the value for PendingExtensionDate to be an explicit nil

### UnsetPendingExtensionDate
`func (o *PoamResponseGetSystemsDataInner) UnsetPendingExtensionDate()`

UnsetPendingExtensionDate ensures that no value is present for PendingExtensionDate, not even an explicit nil
### GetArtifacts

`func (o *PoamResponseGetSystemsDataInner) GetArtifacts() string`

GetArtifacts returns the Artifacts field if non-nil, zero value otherwise.

### GetArtifactsOk

`func (o *PoamResponseGetSystemsDataInner) GetArtifactsOk() (*string, bool)`

GetArtifactsOk returns a tuple with the Artifacts field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetArtifacts

`func (o *PoamResponseGetSystemsDataInner) SetArtifacts(v string)`

SetArtifacts sets Artifacts field to given value.

### HasArtifacts

`func (o *PoamResponseGetSystemsDataInner) HasArtifacts() bool`

HasArtifacts returns a boolean if a field has been set.

### SetArtifactsNil

`func (o *PoamResponseGetSystemsDataInner) SetArtifactsNil(b bool)`

 SetArtifactsNil sets the value for Artifacts to be an explicit nil

### UnsetArtifacts
`func (o *PoamResponseGetSystemsDataInner) UnsetArtifacts()`

UnsetArtifacts ensures that no value is present for Artifacts, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


