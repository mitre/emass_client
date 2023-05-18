# emass_client.model.test_results_get.TestResultsGet

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**systemId** | decimal.Decimal, int,  | decimal.Decimal,  | [Required] Unique eMASS identifier. Will need to provide correct number | [optional] value must be a 64 bit integer
**control** | None, str,  | NoneClass, str,  | [Read-Only] Control acronym associated with the test result. NIST SP 800-53 Revision 4 defined. | [optional] 
**cci** | str,  | str,  | [Required] CCI associated with test result. | [optional] 
**isInherited** | None, bool,  | NoneClass, BoolClass,  | [Read-only] Indicates whether a test result is inherited. | [optional] 
**testedBy** | str,  | str,  | [Required] Last Name, First Name. 100 Characters. | [optional] 
**testDate** | decimal.Decimal, int,  | decimal.Decimal,  | [Required] Unix time format. | [optional] value must be a 64 bit integer
**description** | str,  | str,  | [Required] Include description of test result. 4000 Characters. | [optional] 
**type** | None, str,  | NoneClass, str,  | [Read-Only] Indicates the location in the Control Approval Chain when the test result is submitted. | [optional] 
**complianceStatus** | str,  | str,  | [Required] Test result compliance status | [optional] must be one of ["Compliant", "Non-Compliant", "Not Applicable", ] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

