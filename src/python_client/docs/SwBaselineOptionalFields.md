# SwBaselineOptionalFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**software_type** | **str** | [Optional] Type of the software asset. | [optional] 
**parent_system** | **str** | [Optional] Parent system of the software asset. | [optional] 
**subsystem** | **str** | [Optional] Subsystem of the software asset. | [optional] 
**network** | **str** | [Optional] Network of the software asset. | [optional] 
**hosting_environment** | **str** | [Optional] Hosting environment of the software asset. | [optional] 
**software_dependencies** | **str** | [Optional] Dependencies of the software asset. | [optional] 
**cryptographic_hash** | **str** | [Optional] Cryptographic hash of the software asset. | [optional] 
**in_service_data** | **str** | [Optional] In-service data of the software asset. | [optional] 
**it_budget_uii** | **str** | [Optional] IT budget UII of the software asset. | [optional] 
**fiscal_year** | **str** | [Optional] Fiscal year (FY) of the software asset. | [optional] 
**pop_end_date** | **int** | [Optional] Period of performance (POP) end date of the software asset. | [optional] 
**license_or_contract** | **str** | [Optional] License or contract number of the software asset. | [optional] 
**license_term** | **str** | [Optional] License term of the software asset. | [optional] 
**cost_per_license** | **float** | [Optional] Cost per license of the software asset. Number will be converted to display 2 decimal points. | [optional] 
**total_licenses** | **int** | [Optional] Total licenses of the software asset. | [optional] 
**total_license_cost** | **float** | [Optional] Total license cost of the software asset. Number will be converted to display 2 decimal points. | [optional] 
**licenses_used** | **int** | [Optional] Number of licenses used for the software asset. | [optional] 
**license_poc** | **str** | [Optional] Point of contact (POC) for the software asset. | [optional] 
**license_renewal_date** | **int** | [Optional] License renewal date for the software asset. | [optional] 
**license_expiration_date** | **int** | [Optional] License expiration date for the software asset. | [optional] 
**approval_status** | **str** | [Optional] Approval status of the software asset. | [optional] 
**release_date** | **int** | [Optional] Release date of the software asset. | [optional] 
**maintenance_date** | **int** | [Optional] Maintenance date of the software asset. | [optional] 
**retirement_date** | **int** | [Optional] Retirement date of the software asset. | [optional] 
**end_of_life_support_date** | **int** | [Optional] End of life support date of the software asset. | [optional] 
**extended_end_of_life_support_date** | **int** | [Optional] If set, the Extended End of Life/Support Date cannot occur prior to the End of Life/Support Date. | [optional] 
**critical_asset** | **bool** | [Optional] Indicates whether the asset is a critical information system asset. | [optional] 
**location** | **str** | [Optional] Location of the software asset. | [optional] 
**purpose** | **str** | [Optional] Purpose of the software asset. | [optional] 
**unsupported_operating_system** | **bool** | [Optional] Unsupported operating system. VA only. | [optional] 
**unapproved_software_from_trm** | **bool** | [Optional] Unapproved software from TRM. VA only | [optional] 
**approved_waiver** | **bool** | [Optional] Approved waiver. VA only | [optional] 

## Example

```python
from emass_client.models.sw_baseline_optional_fields import SwBaselineOptionalFields

# TODO update the JSON string below
json = "{}"
# create an instance of SwBaselineOptionalFields from a JSON string
sw_baseline_optional_fields_instance = SwBaselineOptionalFields.from_json(json)
# print the JSON string representation of the object
print(SwBaselineOptionalFields.to_json())

# convert the object into a dict
sw_baseline_optional_fields_dict = sw_baseline_optional_fields_instance.to_dict()
# create an instance of SwBaselineOptionalFields from a dict
sw_baseline_optional_fields_from_dict = SwBaselineOptionalFields.from_dict(sw_baseline_optional_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


