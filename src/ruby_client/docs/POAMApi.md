# EmassClient::POAMApi

All URIs are relative to *http://localhost:4010*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**add_poam_by_system_id**](POAMApi.md#add_poam_by_system_id) | **POST** /api/systems/{systemId}/poams | Add one or many POA&amp;M items in a system |
| [**delete_poam**](POAMApi.md#delete_poam) | **DELETE** /api/systems/{systemId}/poams | Remove one or many POA&amp;M items in a system |
| [**get_system_poams**](POAMApi.md#get_system_poams) | **GET** /api/systems/{systemId}/poams | Get one or many POA&amp;M items in a system |
| [**get_system_poams_by_poam_id**](POAMApi.md#get_system_poams_by_poam_id) | **GET** /api/systems/{systemId}/poams/{poamId} | Get POA&amp;M item by ID in a system |
| [**update_poam_by_system_id**](POAMApi.md#update_poam_by_system_id) | **PUT** /api/systems/{systemId}/poams | Update one or many POA&amp;M items in a system |


## add_poam_by_system_id

> <PoamResponsePostPutDelete> add_poam_by_system_id(system_id, poam_required_fields)

Add one or many POA&M items in a system

Add a POA&M for given `systemId`  **Request Body Required Fields** <table>   <thead>     <tr><th><b>Field</b></th><th><b>Require/Condition</b></th></tr>   </thead>   <tbody>     <tr><td><code>status</code></td><td>Always (every POST)</td></tr>     <tr><td><code>vulnerabilityDescription</code></td><td>Always (every POST)</td></tr>     <tr><td><code>sourceIdentifyingVulnerability</code></td><td>Always (every POST)</td></tr>     <tr><td><code>pocOrganization</code></td><td>Always (every POST)</td></tr>     <tr><td><code>resources</code></td><td>Always (every POST)</td></tr>     <tr><td><code>identifiedInCFOAuditOrOtherReview</code></td><td>Required for VA. Optional for Army and USCG.</td></tr>     <tr><td><code>scheduledCompletionDate</code></td><td>Required for ongoing and completed POA&M items</td></tr>     <tr><td><code>pocFirstName</code></td><td>Only if Last Name, Email, or Phone Number have data</td></tr>     <tr><td><code>pocLastName</code></td><td>Only if First Name, Email, or Phone Number have data</td></tr>     <tr><td><code>pocEmail</code></td><td>Only if First Name, Last Name, or Phone Number have data</td></tr>     <tr><td><code>pocPhoneNumber</code></td><td>Only if First Name, Last Name, or Email have data</td></tr>     <tr><td><code>completionDate</code></td><td>For completed POA&M Item only</td></tr>     <tr><td><code>comments</code></td><td>For completed or Risk Accepted POA&M Items only</td></tr>   </tbody> </table>  **NOTE**: Certain eMASS instances also require the Risk Analysis fields to be populated:   - `severity`   - `relevanceOfThreat`   - `likelihood`   - `impact`   - `residualRiskLevel`   - `mitigations`  </br> **Business Rules**  The following rules apply to the Review Status `status` field value: <table>   <thead><tr><th><b>Value</b></th><th><b>Rule</b></th></tr></thead>   <tbody>     <tr><td><b>Not Approved</b></td><td>POA&M cannot be saved if Milestone Scheduled Completion Date exceeds POA&M Item Scheduled Completion Date</td></tr>     <tr><td><b>Approved</b></td><td>POA&M can only be saved if Milestone Scheduled Completion Date exceeds POA&M Item Scheduled Completion Date</td></tr>     <tr><td></td><td>Are required to have a Severity Value assigned</td></tr>     <tr><td><b>Completed</b> or <b>Ongoing</b></td><td>Cannot be saved without Milestones</td></tr>     <tr><td><b>Risk Accepted</b></td><td>POA&M Item cannot be saved with a Scheduled Completion Date <code>scheduledCompletionDate</code> or have Milestones</td></tr>     <tr><td><b>Approved</b> or <b>Completed</b> or <b>Ongoing</b></td><td>Cannot update Scheduled Completion Date</td></tr>  </tbody> </table>  **Additional Rules** - POA&M Item cannot be saved if associated Security Control or AP is inherited. - Completed POA&M Item cannot be saved if Completion Date (`completionDate`) is in the future. - POA&M Items cannot be updated if they are included in an active package. - Archived POA&M Items cannot be updated. - POA&M Items with a status of \"Not Applicable\" will be updated through test result creation. - If the Security Control or Assessment Procedure does not exist in the system, the POA&M Item maybe imported at the System Level.   **Fields Characters Limitation** - POA&M Item cannot be saved if the Point of Contact (POC) fields exceed 100 characters:   - `pocOrganization` `pocFirstName`, `pocLastName`, `pocEmail`, `pocPhoneNumber` - POA&M Item cannot be saved if Resources (`resource`) field exceeds 250 characters - POA&M Item cannot be saved if the following fields exceeds 2,000 characters:   - `mitigations`, `sourceIdentifyingVulnerability`, `comments`   - Milestones Field: `description` - POA&M Items cannot be saved if Milestone Description (`description`) exceeds 2,000 characters.

### Examples

```ruby
require 'time'
require 'emass_client'
# setup authorization
EmassClient.configure do |config|
  # Configure API key authorization: apiKey
  config.api_key['api-key'] = 'YOUR API KEY'
  # Uncomment the following line to set a prefix for the API key, e.g. 'Bearer' (defaults to nil)
  # config.api_key_prefix['api-key'] = 'Bearer'

  # Configure API key authorization: mockType
  config.api_key['Prefer'] = 'YOUR API KEY'
  # Uncomment the following line to set a prefix for the API key, e.g. 'Bearer' (defaults to nil)
  # config.api_key_prefix['Prefer'] = 'Bearer'

  # Configure API key authorization: userId
  config.api_key['user-uid'] = 'YOUR API KEY'
  # Uncomment the following line to set a prefix for the API key, e.g. 'Bearer' (defaults to nil)
  # config.api_key_prefix['user-uid'] = 'Bearer'
end

api_instance = EmassClient::POAMApi.new
system_id = 35 # Integer | **System Id**: The unique system record identifier.
poam_required_fields = [EmassClient::PoamRequiredFields.new] # Array<PoamRequiredFields> | Example request body to add POA&M(s) to a system (systemId)

begin
  # Add one or many POA&M items in a system
  result = api_instance.add_poam_by_system_id(system_id, poam_required_fields)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling POAMApi->add_poam_by_system_id: #{e}"
end
```

#### Using the add_poam_by_system_id_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PoamResponsePostPutDelete>, Integer, Hash)> add_poam_by_system_id_with_http_info(system_id, poam_required_fields)

```ruby
begin
  # Add one or many POA&M items in a system
  data, status_code, headers = api_instance.add_poam_by_system_id_with_http_info(system_id, poam_required_fields)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PoamResponsePostPutDelete>
rescue EmassClient::ApiError => e
  puts "Error when calling POAMApi->add_poam_by_system_id_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **system_id** | **Integer** | **System Id**: The unique system record identifier. |  |
| **poam_required_fields** | [**Array&lt;PoamRequiredFields&gt;**](PoamRequiredFields.md) | Example request body to add POA&amp;M(s) to a system (systemId) |  |

### Return type

[**PoamResponsePostPutDelete**](PoamResponsePostPutDelete.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## delete_poam

> <PoamResponsePostPutDelete> delete_poam(system_id, poam_request_delete_body_inner)

Remove one or many POA&M items in a system

Remove the POA&M matching `systemId` path parameter and `poamId` Request Body<br>

### Examples

```ruby
require 'time'
require 'emass_client'
# setup authorization
EmassClient.configure do |config|
  # Configure API key authorization: apiKey
  config.api_key['api-key'] = 'YOUR API KEY'
  # Uncomment the following line to set a prefix for the API key, e.g. 'Bearer' (defaults to nil)
  # config.api_key_prefix['api-key'] = 'Bearer'

  # Configure API key authorization: mockType
  config.api_key['Prefer'] = 'YOUR API KEY'
  # Uncomment the following line to set a prefix for the API key, e.g. 'Bearer' (defaults to nil)
  # config.api_key_prefix['Prefer'] = 'Bearer'

  # Configure API key authorization: userId
  config.api_key['user-uid'] = 'YOUR API KEY'
  # Uncomment the following line to set a prefix for the API key, e.g. 'Bearer' (defaults to nil)
  # config.api_key_prefix['user-uid'] = 'Bearer'
end

api_instance = EmassClient::POAMApi.new
system_id = 35 # Integer | **System Id**: The unique system record identifier.
poam_request_delete_body_inner = [EmassClient::PoamRequestDeleteBodyInner.new] # Array<PoamRequestDeleteBodyInner> | Delete the given POA&M Id

begin
  # Remove one or many POA&M items in a system
  result = api_instance.delete_poam(system_id, poam_request_delete_body_inner)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling POAMApi->delete_poam: #{e}"
end
```

#### Using the delete_poam_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PoamResponsePostPutDelete>, Integer, Hash)> delete_poam_with_http_info(system_id, poam_request_delete_body_inner)

```ruby
begin
  # Remove one or many POA&M items in a system
  data, status_code, headers = api_instance.delete_poam_with_http_info(system_id, poam_request_delete_body_inner)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PoamResponsePostPutDelete>
rescue EmassClient::ApiError => e
  puts "Error when calling POAMApi->delete_poam_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **system_id** | **Integer** | **System Id**: The unique system record identifier. |  |
| **poam_request_delete_body_inner** | [**Array&lt;PoamRequestDeleteBodyInner&gt;**](PoamRequestDeleteBodyInner.md) | Delete the given POA&amp;M Id |  |

### Return type

[**PoamResponsePostPutDelete**](PoamResponsePostPutDelete.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## get_system_poams

> <PoamResponseGetSystems> get_system_poams(system_id, opts)

Get one or many POA&M items in a system

Returns system(s) containing POA&M items for matching parameters.

### Examples

```ruby
require 'time'
require 'emass_client'
# setup authorization
EmassClient.configure do |config|
  # Configure API key authorization: apiKey
  config.api_key['api-key'] = 'YOUR API KEY'
  # Uncomment the following line to set a prefix for the API key, e.g. 'Bearer' (defaults to nil)
  # config.api_key_prefix['api-key'] = 'Bearer'

  # Configure API key authorization: mockType
  config.api_key['Prefer'] = 'YOUR API KEY'
  # Uncomment the following line to set a prefix for the API key, e.g. 'Bearer' (defaults to nil)
  # config.api_key_prefix['Prefer'] = 'Bearer'

  # Configure API key authorization: userId
  config.api_key['user-uid'] = 'YOUR API KEY'
  # Uncomment the following line to set a prefix for the API key, e.g. 'Bearer' (defaults to nil)
  # config.api_key_prefix['user-uid'] = 'Bearer'
end

api_instance = EmassClient::POAMApi.new
system_id = 35 # Integer | **System Id**: The unique system record identifier.
opts = {
  scheduled_completion_date_start: 'scheduled_completion_date_start_example', # String | **Date Started**: Filter query by the scheduled completion start date (Unix date format).
  scheduled_completion_date_end: 'scheduled_completion_date_end_example', # String | **Date Ended**: Filter query by the scheduled completion start date (Unix date format).
  control_acronyms: 'control_acronyms_example', # String | **Control Acronym**: Filter query by given system acronym (single value or comma separated).
  assessment_procedures: 'assessment_procedures_example', # String | **Assessment Procedure**: Filter query by given Security Control Assessment Procedure (single value or comma separated).
  ccis: 'ccis_example', # String | **CCI System**: Filter query by Control Correlation Identifiers (CCIs) (single value or comma separated).
  system_only: true # Boolean | **Systems Only**: Indicates that only system(s) information is retrieved.
}

begin
  # Get one or many POA&M items in a system
  result = api_instance.get_system_poams(system_id, opts)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling POAMApi->get_system_poams: #{e}"
end
```

#### Using the get_system_poams_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PoamResponseGetSystems>, Integer, Hash)> get_system_poams_with_http_info(system_id, opts)

```ruby
begin
  # Get one or many POA&M items in a system
  data, status_code, headers = api_instance.get_system_poams_with_http_info(system_id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PoamResponseGetSystems>
rescue EmassClient::ApiError => e
  puts "Error when calling POAMApi->get_system_poams_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **system_id** | **Integer** | **System Id**: The unique system record identifier. |  |
| **scheduled_completion_date_start** | **String** | **Date Started**: Filter query by the scheduled completion start date (Unix date format). | [optional] |
| **scheduled_completion_date_end** | **String** | **Date Ended**: Filter query by the scheduled completion start date (Unix date format). | [optional] |
| **control_acronyms** | **String** | **Control Acronym**: Filter query by given system acronym (single value or comma separated). | [optional] |
| **assessment_procedures** | **String** | **Assessment Procedure**: Filter query by given Security Control Assessment Procedure (single value or comma separated). | [optional] |
| **ccis** | **String** | **CCI System**: Filter query by Control Correlation Identifiers (CCIs) (single value or comma separated). | [optional] |
| **system_only** | **Boolean** | **Systems Only**: Indicates that only system(s) information is retrieved. | [optional][default to true] |

### Return type

[**PoamResponseGetSystems**](PoamResponseGetSystems.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## get_system_poams_by_poam_id

> <PoamResponseGetPoams> get_system_poams_by_poam_id(system_id, poam_id)

Get POA&M item by ID in a system

Returns system(s) containing POA&M items for matching parameters.

### Examples

```ruby
require 'time'
require 'emass_client'
# setup authorization
EmassClient.configure do |config|
  # Configure API key authorization: apiKey
  config.api_key['api-key'] = 'YOUR API KEY'
  # Uncomment the following line to set a prefix for the API key, e.g. 'Bearer' (defaults to nil)
  # config.api_key_prefix['api-key'] = 'Bearer'

  # Configure API key authorization: mockType
  config.api_key['Prefer'] = 'YOUR API KEY'
  # Uncomment the following line to set a prefix for the API key, e.g. 'Bearer' (defaults to nil)
  # config.api_key_prefix['Prefer'] = 'Bearer'

  # Configure API key authorization: userId
  config.api_key['user-uid'] = 'YOUR API KEY'
  # Uncomment the following line to set a prefix for the API key, e.g. 'Bearer' (defaults to nil)
  # config.api_key_prefix['user-uid'] = 'Bearer'
end

api_instance = EmassClient::POAMApi.new
system_id = 35 # Integer | **System Id**: The unique system record identifier.
poam_id = 45 # Integer | **POA&M Id**: The unique POA&M record identifier.

begin
  # Get POA&M item by ID in a system
  result = api_instance.get_system_poams_by_poam_id(system_id, poam_id)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling POAMApi->get_system_poams_by_poam_id: #{e}"
end
```

#### Using the get_system_poams_by_poam_id_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PoamResponseGetPoams>, Integer, Hash)> get_system_poams_by_poam_id_with_http_info(system_id, poam_id)

```ruby
begin
  # Get POA&M item by ID in a system
  data, status_code, headers = api_instance.get_system_poams_by_poam_id_with_http_info(system_id, poam_id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PoamResponseGetPoams>
rescue EmassClient::ApiError => e
  puts "Error when calling POAMApi->get_system_poams_by_poam_id_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **system_id** | **Integer** | **System Id**: The unique system record identifier. |  |
| **poam_id** | **Integer** | **POA&amp;M Id**: The unique POA&amp;M record identifier. |  |

### Return type

[**PoamResponseGetPoams**](PoamResponseGetPoams.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## update_poam_by_system_id

> <PoamResponsePostPutDelete> update_poam_by_system_id(system_id, poam_ids)

Update one or many POA&M items in a system

Update a POA&M for given `systemId`<br>  **Request Body Required Fields** <table>   <thead>     <tr><th><b>Field</b></th><th><b>Require/Condition</b></th></tr>   </thead>   <tbody>     <tr><td><code>poamId</code></td><td>Always (every PUT)</td></tr>     <tr><td><code>displayPoamId</code></td><td>Always (every PUT)</td></tr>     <tr><td><code>status</code></td><td>Always (every PUT)</td></tr>     <tr><td><code>vulnerabilityDescription</code></td><td>Always (every PUT)</td></tr>     <tr><td><code>sourceIdentifyingVulnerability</code></td><td>Always (every PUT)</td></tr>     <tr><td><code>pocOrganization</code></td><td>Always (every PUT)</td></tr>     <tr><td><code>resources</code></td><td>Always (every PUT)</td></tr>     <tr><td><code>identifiedInCFOAuditOrOtherReview</code></td><td>Required for VA. Optional for Army and USCG.</td></tr>     <tr><td><code>scheduledCompletionDate</code></td><td>Required for ongoing and completed POA&M items</td></tr>     <tr><td><code>pocFirstName</code></td><td>Only if Last Name, Email, or Phone Number have data</td></tr>     <tr><td><code>pocLastName</code></td><td>Only if First Name, Email, or Phone Number have data</td></tr>     <tr><td><code>pocEmail</code></td><td>Only if First Name, Last Name, or Phone Number have data</td></tr>     <tr><td><code>pocPhoneNumber</code></td><td>Only if First Name, Last Name, or Email have data</td></tr>     <tr><td><code>completionDate</code></td><td>For completed POA&M Item only</td></tr>     <tr><td><code>comments</code></td><td>For completed or Risk Accepted POA&M Items only</td></tr>   </tbody> </table>  **NOTES**: - Certain eMASS instances also require the Risk Analysis fields to be populated:   - `severity`   - `relevanceOfThreat`   - `likelihood`   - `impact`   - `residualRiskLevel`   - `mitigations` - To prevent uploading duplicate/undesired milestones through the POA&M PUT include an `isActive` field for the milestone and set it to equal to false `(isActive=false)`. </br>  **Business Rules:** See business rules for the POST endpoint

### Examples

```ruby
require 'time'
require 'emass_client'
# setup authorization
EmassClient.configure do |config|
  # Configure API key authorization: apiKey
  config.api_key['api-key'] = 'YOUR API KEY'
  # Uncomment the following line to set a prefix for the API key, e.g. 'Bearer' (defaults to nil)
  # config.api_key_prefix['api-key'] = 'Bearer'

  # Configure API key authorization: mockType
  config.api_key['Prefer'] = 'YOUR API KEY'
  # Uncomment the following line to set a prefix for the API key, e.g. 'Bearer' (defaults to nil)
  # config.api_key_prefix['Prefer'] = 'Bearer'

  # Configure API key authorization: userId
  config.api_key['user-uid'] = 'YOUR API KEY'
  # Uncomment the following line to set a prefix for the API key, e.g. 'Bearer' (defaults to nil)
  # config.api_key_prefix['user-uid'] = 'Bearer'
end

api_instance = EmassClient::POAMApi.new
system_id = 35 # Integer | **System Id**: The unique system record identifier.
poam_ids = [EmassClient::PoamIds.new] # Array<PoamIds> | Example request body for updating a POA&M for a system (systemId)

begin
  # Update one or many POA&M items in a system
  result = api_instance.update_poam_by_system_id(system_id, poam_ids)
  p result
rescue EmassClient::ApiError => e
  puts "Error when calling POAMApi->update_poam_by_system_id: #{e}"
end
```

#### Using the update_poam_by_system_id_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PoamResponsePostPutDelete>, Integer, Hash)> update_poam_by_system_id_with_http_info(system_id, poam_ids)

```ruby
begin
  # Update one or many POA&M items in a system
  data, status_code, headers = api_instance.update_poam_by_system_id_with_http_info(system_id, poam_ids)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PoamResponsePostPutDelete>
rescue EmassClient::ApiError => e
  puts "Error when calling POAMApi->update_poam_by_system_id_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **system_id** | **Integer** | **System Id**: The unique system record identifier. |  |
| **poam_ids** | [**Array&lt;PoamIds&gt;**](PoamIds.md) | Example request body for updating a POA&amp;M for a system (systemId) |  |

### Return type

[**PoamResponsePostPutDelete**](PoamResponsePostPutDelete.md)

### Authorization

[apiKey](../README.md#apiKey), [mockType](../README.md#mockType), [userId](../README.md#userId)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

