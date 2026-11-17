# PoamRequiredFields

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Status** | Pointer to **string** | [Required] The POA&amp;M status | [optional] 
**VulnerabilityDescription** | Pointer to **string** | [Required] Provide a description of the POA&amp;M Item. 2000 Characters. | [optional] 
**SourceIdentifyingVulnerability** | Pointer to **string** | [Required] Include Source Identifying Vulnerability text. 2000 Characters. | [optional] 
**PocOrganization** | Pointer to **string** | [Required] Organization/Office represented. 100 Characters. | [optional] 
**Resources** | Pointer to **string** | [Required] List of resources used. 250 Characters. | [optional] 
**IdentifiedInCFOAuditOrOtherReview** | Pointer to **bool** | [Required] If not specified, this field will be set to false because it does not accept a null value. VA only | [optional] 

## Methods

### NewPoamRequiredFields

`func NewPoamRequiredFields() *PoamRequiredFields`

NewPoamRequiredFields instantiates a new PoamRequiredFields object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPoamRequiredFieldsWithDefaults

`func NewPoamRequiredFieldsWithDefaults() *PoamRequiredFields`

NewPoamRequiredFieldsWithDefaults instantiates a new PoamRequiredFields object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetStatus

`func (o *PoamRequiredFields) GetStatus() string`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *PoamRequiredFields) GetStatusOk() (*string, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *PoamRequiredFields) SetStatus(v string)`

SetStatus sets Status field to given value.

### HasStatus

`func (o *PoamRequiredFields) HasStatus() bool`

HasStatus returns a boolean if a field has been set.

### GetVulnerabilityDescription

`func (o *PoamRequiredFields) GetVulnerabilityDescription() string`

GetVulnerabilityDescription returns the VulnerabilityDescription field if non-nil, zero value otherwise.

### GetVulnerabilityDescriptionOk

`func (o *PoamRequiredFields) GetVulnerabilityDescriptionOk() (*string, bool)`

GetVulnerabilityDescriptionOk returns a tuple with the VulnerabilityDescription field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVulnerabilityDescription

`func (o *PoamRequiredFields) SetVulnerabilityDescription(v string)`

SetVulnerabilityDescription sets VulnerabilityDescription field to given value.

### HasVulnerabilityDescription

`func (o *PoamRequiredFields) HasVulnerabilityDescription() bool`

HasVulnerabilityDescription returns a boolean if a field has been set.

### GetSourceIdentifyingVulnerability

`func (o *PoamRequiredFields) GetSourceIdentifyingVulnerability() string`

GetSourceIdentifyingVulnerability returns the SourceIdentifyingVulnerability field if non-nil, zero value otherwise.

### GetSourceIdentifyingVulnerabilityOk

`func (o *PoamRequiredFields) GetSourceIdentifyingVulnerabilityOk() (*string, bool)`

GetSourceIdentifyingVulnerabilityOk returns a tuple with the SourceIdentifyingVulnerability field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSourceIdentifyingVulnerability

`func (o *PoamRequiredFields) SetSourceIdentifyingVulnerability(v string)`

SetSourceIdentifyingVulnerability sets SourceIdentifyingVulnerability field to given value.

### HasSourceIdentifyingVulnerability

`func (o *PoamRequiredFields) HasSourceIdentifyingVulnerability() bool`

HasSourceIdentifyingVulnerability returns a boolean if a field has been set.

### GetPocOrganization

`func (o *PoamRequiredFields) GetPocOrganization() string`

GetPocOrganization returns the PocOrganization field if non-nil, zero value otherwise.

### GetPocOrganizationOk

`func (o *PoamRequiredFields) GetPocOrganizationOk() (*string, bool)`

GetPocOrganizationOk returns a tuple with the PocOrganization field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPocOrganization

`func (o *PoamRequiredFields) SetPocOrganization(v string)`

SetPocOrganization sets PocOrganization field to given value.

### HasPocOrganization

`func (o *PoamRequiredFields) HasPocOrganization() bool`

HasPocOrganization returns a boolean if a field has been set.

### GetResources

`func (o *PoamRequiredFields) GetResources() string`

GetResources returns the Resources field if non-nil, zero value otherwise.

### GetResourcesOk

`func (o *PoamRequiredFields) GetResourcesOk() (*string, bool)`

GetResourcesOk returns a tuple with the Resources field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetResources

`func (o *PoamRequiredFields) SetResources(v string)`

SetResources sets Resources field to given value.

### HasResources

`func (o *PoamRequiredFields) HasResources() bool`

HasResources returns a boolean if a field has been set.

### GetIdentifiedInCFOAuditOrOtherReview

`func (o *PoamRequiredFields) GetIdentifiedInCFOAuditOrOtherReview() bool`

GetIdentifiedInCFOAuditOrOtherReview returns the IdentifiedInCFOAuditOrOtherReview field if non-nil, zero value otherwise.

### GetIdentifiedInCFOAuditOrOtherReviewOk

`func (o *PoamRequiredFields) GetIdentifiedInCFOAuditOrOtherReviewOk() (*bool, bool)`

GetIdentifiedInCFOAuditOrOtherReviewOk returns a tuple with the IdentifiedInCFOAuditOrOtherReview field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIdentifiedInCFOAuditOrOtherReview

`func (o *PoamRequiredFields) SetIdentifiedInCFOAuditOrOtherReview(v bool)`

SetIdentifiedInCFOAuditOrOtherReview sets IdentifiedInCFOAuditOrOtherReview field to given value.

### HasIdentifiedInCFOAuditOrOtherReview

`func (o *PoamRequiredFields) HasIdentifiedInCFOAuditOrOtherReview() bool`

HasIdentifiedInCFOAuditOrOtherReview returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


