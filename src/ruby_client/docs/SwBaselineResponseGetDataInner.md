# EmassClient::SwBaselineResponseGetDataInner

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **system_id** | **Integer** | [Required] Unique eMASS system identifier. | [optional] |
| **software_id** | **String** | [Read-Only] GUID identifying the specific software asset. | [optional] |
| **software_vendor** | **String** | [Required] Vendor of the software asset. | [optional] |
| **software_name** | **String** | [Required] Name of the software asset. | [optional] |
| **version** | **String** | [Required] Version of the software asset. | [optional] |
| **software_type** | **String** | [Optional] Type of the software asset. | [optional] |
| **parent_system** | **String** | [Optional] Parent system of the software asset. | [optional] |
| **subsystem** | **String** | [Optional] Subsystem of the software asset. | [optional] |
| **network** | **String** | [Optional] Network of the software asset. | [optional] |
| **hosting_environment** | **String** | [Optional] Hosting environment of the software asset. | [optional] |
| **software_dependencies** | **String** | [Optional] Dependencies of the software asset. | [optional] |
| **cryptographic_hash** | **String** | [Optional] Cryptographic hash of the software asset. | [optional] |
| **in_service_data** | **String** | [Optional] In-service data of the software asset. | [optional] |
| **it_budget_uii** | **String** | [Optional] IT budget UII of the software asset. | [optional] |
| **fiscal_year** | **String** | [Optional] Fiscal year (FY) of the software asset. | [optional] |
| **pop_end_date** | **Integer** | [Optional] Period of performance (POP) end date of the software asset. | [optional] |
| **license_or_contract** | **String** | [Optional] License or contract number of the software asset. | [optional] |
| **license_term** | **String** | [Optional] License term of the software asset. | [optional] |
| **cost_per_license** | **Float** | [Optional] Cost per license of the software asset. Number will be converted to display 2 decimal points. | [optional] |
| **total_licenses** | **Integer** | [Optional] Total licenses of the software asset. | [optional] |
| **total_license_cost** | **Float** | [Optional] Total license cost of the software asset. Number will be converted to display 2 decimal points. | [optional] |
| **licenses_used** | **Integer** | [Optional] Number of licenses used for the software asset. | [optional] |
| **license_poc** | **String** | [Optional] Point of contact (POC) for the software asset. | [optional] |
| **license_renewal_date** | **Integer** | [Optional] License renewal date for the software asset. | [optional] |
| **license_expiration_date** | **Integer** | [Optional] License expiration date for the software asset. | [optional] |
| **approval_status** | **String** | [Optional] Approval status of the software asset. | [optional] |
| **release_date** | **Integer** | [Optional] Release date of the software asset. | [optional] |
| **maintenance_date** | **Integer** | [Optional] Maintenance date of the software asset. | [optional] |
| **retirement_date** | **Integer** | [Optional] Retirement date of the software asset. | [optional] |
| **end_of_life_support_date** | **Integer** | [Optional] End of life support date of the software asset. | [optional] |
| **extended_end_of_life_support_date** | **Integer** | [Optional] If set, the Extended End of Life/Support Date cannot occur prior to the End of Life/Support Date. | [optional] |
| **critical_asset** | **Boolean** | [Optional] Indicates whether the asset is a critical information system asset. | [optional] |
| **location** | **String** | [Optional] Location of the software asset. | [optional] |
| **purpose** | **String** | [Optional] Purpose of the software asset. | [optional] |
| **unsupported_operating_system** | **Boolean** | [Optional] Unsupported operating system. VA only. | [optional] |
| **unapproved_software_from_trm** | **Boolean** | [Optional] Unapproved software from TRM. VA only | [optional] |
| **approved_waiver** | **Boolean** | [Optional] Approved waiver. VA only | [optional] |

## Example

```ruby
require 'emass_client'

instance = EmassClient::SwBaselineResponseGetDataInner.new(
  system_id: 85,
  software_id: 171fc7d0-6957-4f54-bd51-3b7cbc6c39d5,
  software_vendor: Test Vendor,
  software_name: Test Software Name 11,
  version: 1.0,
  software_type: COTS Application,
  parent_system: Test Parent System,
  subsystem: Test Subsystem,
  network: Test Network,
  hosting_environment: Test Hosting Environment,
  software_dependencies: Test Dependencies,
  cryptographic_hash: Test Cryptographic Hash 32&quot;,
  in_service_data: Test In-Service Data,
  it_budget_uii: Test IT Budget Uii,
  fiscal_year: 2021,
  pop_end_date: 1715312304,
  license_or_contract: Test License Or Contract 25,
  license_term: Test License Term 25,
  cost_per_license: 250.25,
  total_licenses: 100,
  total_license_cost: 2250.25,
  licenses_used: 100,
  license_poc: Smith, Joe,
  license_renewal_date: 1715312304,
  license_expiration_date: 1715312304,
  approval_status: In Progress,
  release_date: 1715312304,
  maintenance_date: 1715312304,
  retirement_date: 1715312304,
  end_of_life_support_date: 1715312304,
  extended_end_of_life_support_date: 1715312304,
  critical_asset: false,
  location: Test Location,
  purpose: Test Purpose,
  unsupported_operating_system: false,
  unapproved_software_from_trm: false,
  approved_waiver: false
)
```

