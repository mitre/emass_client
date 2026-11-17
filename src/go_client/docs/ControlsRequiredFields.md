# ControlsRequiredFields

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Acronym** | Pointer to **string** | [Required] Acronym of the system record. | [optional] 
**ResponsibleEntities** | Pointer to **string** | [Required] Include written description of Responsible Entities that are responsible for the Security Control. Character Limit 2,000. | [optional] 
**ControlDesignation** | Pointer to **string** | [Required] Control designations | [optional] 
**EstimatedCompletionDate** | Pointer to **int64** | [Required] Field is required for Implementation Plan. Unix time format. | [optional] 
**ImplementationNarrative** | Pointer to **string** | [Required] Includes security control comments. Character Limit 2,000. | [optional] 

## Methods

### NewControlsRequiredFields

`func NewControlsRequiredFields() *ControlsRequiredFields`

NewControlsRequiredFields instantiates a new ControlsRequiredFields object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewControlsRequiredFieldsWithDefaults

`func NewControlsRequiredFieldsWithDefaults() *ControlsRequiredFields`

NewControlsRequiredFieldsWithDefaults instantiates a new ControlsRequiredFields object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAcronym

`func (o *ControlsRequiredFields) GetAcronym() string`

GetAcronym returns the Acronym field if non-nil, zero value otherwise.

### GetAcronymOk

`func (o *ControlsRequiredFields) GetAcronymOk() (*string, bool)`

GetAcronymOk returns a tuple with the Acronym field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAcronym

`func (o *ControlsRequiredFields) SetAcronym(v string)`

SetAcronym sets Acronym field to given value.

### HasAcronym

`func (o *ControlsRequiredFields) HasAcronym() bool`

HasAcronym returns a boolean if a field has been set.

### GetResponsibleEntities

`func (o *ControlsRequiredFields) GetResponsibleEntities() string`

GetResponsibleEntities returns the ResponsibleEntities field if non-nil, zero value otherwise.

### GetResponsibleEntitiesOk

`func (o *ControlsRequiredFields) GetResponsibleEntitiesOk() (*string, bool)`

GetResponsibleEntitiesOk returns a tuple with the ResponsibleEntities field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetResponsibleEntities

`func (o *ControlsRequiredFields) SetResponsibleEntities(v string)`

SetResponsibleEntities sets ResponsibleEntities field to given value.

### HasResponsibleEntities

`func (o *ControlsRequiredFields) HasResponsibleEntities() bool`

HasResponsibleEntities returns a boolean if a field has been set.

### GetControlDesignation

`func (o *ControlsRequiredFields) GetControlDesignation() string`

GetControlDesignation returns the ControlDesignation field if non-nil, zero value otherwise.

### GetControlDesignationOk

`func (o *ControlsRequiredFields) GetControlDesignationOk() (*string, bool)`

GetControlDesignationOk returns a tuple with the ControlDesignation field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetControlDesignation

`func (o *ControlsRequiredFields) SetControlDesignation(v string)`

SetControlDesignation sets ControlDesignation field to given value.

### HasControlDesignation

`func (o *ControlsRequiredFields) HasControlDesignation() bool`

HasControlDesignation returns a boolean if a field has been set.

### GetEstimatedCompletionDate

`func (o *ControlsRequiredFields) GetEstimatedCompletionDate() int64`

GetEstimatedCompletionDate returns the EstimatedCompletionDate field if non-nil, zero value otherwise.

### GetEstimatedCompletionDateOk

`func (o *ControlsRequiredFields) GetEstimatedCompletionDateOk() (*int64, bool)`

GetEstimatedCompletionDateOk returns a tuple with the EstimatedCompletionDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEstimatedCompletionDate

`func (o *ControlsRequiredFields) SetEstimatedCompletionDate(v int64)`

SetEstimatedCompletionDate sets EstimatedCompletionDate field to given value.

### HasEstimatedCompletionDate

`func (o *ControlsRequiredFields) HasEstimatedCompletionDate() bool`

HasEstimatedCompletionDate returns a boolean if a field has been set.

### GetImplementationNarrative

`func (o *ControlsRequiredFields) GetImplementationNarrative() string`

GetImplementationNarrative returns the ImplementationNarrative field if non-nil, zero value otherwise.

### GetImplementationNarrativeOk

`func (o *ControlsRequiredFields) GetImplementationNarrativeOk() (*string, bool)`

GetImplementationNarrativeOk returns a tuple with the ImplementationNarrative field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetImplementationNarrative

`func (o *ControlsRequiredFields) SetImplementationNarrative(v string)`

SetImplementationNarrative sets ImplementationNarrative field to given value.

### HasImplementationNarrative

`func (o *ControlsRequiredFields) HasImplementationNarrative() bool`

HasImplementationNarrative returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


