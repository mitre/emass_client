# StaticCodeRequestPostBodyApplication

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ApplicationName** | Pointer to **string** | [Required] Name of the software application that was assessed. | [optional] 
**Version** | Pointer to **string** | [Required] The version of the application. | [optional] 

## Methods

### NewStaticCodeRequestPostBodyApplication

`func NewStaticCodeRequestPostBodyApplication() *StaticCodeRequestPostBodyApplication`

NewStaticCodeRequestPostBodyApplication instantiates a new StaticCodeRequestPostBodyApplication object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewStaticCodeRequestPostBodyApplicationWithDefaults

`func NewStaticCodeRequestPostBodyApplicationWithDefaults() *StaticCodeRequestPostBodyApplication`

NewStaticCodeRequestPostBodyApplicationWithDefaults instantiates a new StaticCodeRequestPostBodyApplication object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetApplicationName

`func (o *StaticCodeRequestPostBodyApplication) GetApplicationName() string`

GetApplicationName returns the ApplicationName field if non-nil, zero value otherwise.

### GetApplicationNameOk

`func (o *StaticCodeRequestPostBodyApplication) GetApplicationNameOk() (*string, bool)`

GetApplicationNameOk returns a tuple with the ApplicationName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetApplicationName

`func (o *StaticCodeRequestPostBodyApplication) SetApplicationName(v string)`

SetApplicationName sets ApplicationName field to given value.

### HasApplicationName

`func (o *StaticCodeRequestPostBodyApplication) HasApplicationName() bool`

HasApplicationName returns a boolean if a field has been set.

### GetVersion

`func (o *StaticCodeRequestPostBodyApplication) GetVersion() string`

GetVersion returns the Version field if non-nil, zero value otherwise.

### GetVersionOk

`func (o *StaticCodeRequestPostBodyApplication) GetVersionOk() (*string, bool)`

GetVersionOk returns a tuple with the Version field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVersion

`func (o *StaticCodeRequestPostBodyApplication) SetVersion(v string)`

SetVersion sets Version field to given value.

### HasVersion

`func (o *StaticCodeRequestPostBodyApplication) HasVersion() bool`

HasVersion returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


