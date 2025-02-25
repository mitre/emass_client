# EmassClient::PoamConditionalFields

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **poc_first_name** | **String** | [Conditional] First name of POC. 100 Characters. | [optional] |
| **poc_last_name** | **String** | [Conditional] Last name of POC. 100 Characters. | [optional] |
| **poc_email** | **String** | [Conditional] Email address of POC. 100 Characters. | [optional] |
| **poc_phone_number** | **String** | [Conditional] Phone number of POC (area code) ***-**** format. 100 Characters. | [optional] |
| **severity** | **String** | [Conditional] Required for approved items. Values include the following options: (Very Low, Low, Moderate,High,Very High) | [optional] |
| **scheduled_completion_date** | **Integer** | [Conditional] Required for ongoing and completed POA&amp;M items. Unix time format. | [optional] |
| **completion_date** | **Integer** | [Conditional] Field is required for completed POA&amp;M items. Unix time format. | [optional] |
| **comments** | **String** | [Conditional] Field is required for completed and risk accepted POA&amp;M items. 2000 Characters | [optional] |
| **personnel_resources_funded_base_hours** | **Float** | [Conditional] At least one of the following is required and must be completed for each POA&amp;M Item:   Personnel Resources-&gt; Funded Base Hours   Personnel Resources-&gt; Unfunded Base Hours   Non-Personnel Resources-&gt; Funded Amount   Non-Personnel Resources-&gt; Unfunded Amount Displays numbers to the second decimal point (e.g., 100.00). VA only.  | [optional] |
| **personnel_resources_cost_code** | **String** | [Conditional] Required if Personnel Resources: Funded Base Hours is populated. Only accepts values present in the field&#39;s lookup table (modifiable by eMASS System Admins). VA only.  | [optional] |
| **personnel_resources_unfunded_base_hours** | **Float** | [Conditional] At least one of the following is required and must be completed for each POA&amp;M Item:   Personnel Resources-&gt; Funded Base Hours   Personnel Resources-&gt; Unfunded Base Hours   Non-Personnel Resources-&gt; Funded Amount   Non-Personnel Resources-&gt; Unfunded Amount Displays numbers to the second decimal point (e.g., 100.00). VA only.  | [optional] |
| **personnel_resources_nonfunding_obstacle** | **String** | [Conditional] Required if Personnel Resources: Unfunded Base Hours is populated. Only accepts values present in the field&#39;s lookup table (modifiable by eMASS System Admins). VA only.  | [optional] |
| **personnel_resources_nonfunding_obstacle_other_reason** | **String** | [Conditional] Required if the value \&quot;Other\&quot; is populated for the field Personnel Resources: Non-Funding Obstacle. VA only. | [optional] |
| **non_personnel_resources_funded_amount** | **Float** | [Conditional] At least one of the following is required and must be completed for each POA&amp;M Item:   Personnel Resources-&gt; Funded Base Hours   Personnel Resources-&gt; Unfunded Base Hours   Non-Personnel Resources-&gt; Funded Amount   Non-Personnel Resources-&gt; Unfunded Amount Displays numbers to the second decimal point (e.g., 100.00). VA only.  | [optional] |
| **non_personnel_resources_cost_code** | **String** | [Conditional] Required if Non-Personnel Resources: Funded Amount is populated. Only accepts values present in the field&#39;s lookup table (modifiable by eMASS System Admins). VA only.  | [optional] |
| **non_personnel_resources_unfunded_amount** | **Float** | [Conditional] At least one of the following is required and must be completed for each POA&amp;M Item:   Personnel Resources-&gt; Funded Base Hours   Personnel Resources-&gt; Unfunded Base Hours   Non-Personnel Resources-&gt; Funded Amount   Non-Personnel Resources-&gt; Unfunded Amount Displays numbers to the second decimal point (e.g., 100.00). VA only.  | [optional] |
| **non_personnel_resources_nonfunding_obstacle** | **String** | [Conditional] Required if Non-Personnel Resources: Unfunded Amount is populated. Only accepts values present in the field&#39;s lookup table (modifiable by eMASS System Admins). VA only.  | [optional] |
| **non_personnel_resources_nonfunding_obstacle_other_reason** | **String** | [Conditional] Required if the value \&quot;Other\&quot; is populated for the field Non-Personnel Resources: Non-Funding Obstacle. VA only. | [optional] |

## Example

```ruby
require 'emass_client'

instance = EmassClient::PoamConditionalFields.new(
  poc_first_name: John,
  poc_last_name: Smith,
  poc_email: smith@ah.com,
  poc_phone_number: 555-555-5555,
  severity: Low,
  scheduled_completion_date: 1799644800,
  completion_date: 1745916276,
  comments: Comments text.,
  personnel_resources_funded_base_hours: 100,
  personnel_resources_cost_code: 123456,
  personnel_resources_unfunded_base_hours: 100,
  personnel_resources_nonfunding_obstacle: Not an system of interest,
  personnel_resources_nonfunding_obstacle_other_reason: Not an system of interest,
  non_personnel_resources_funded_amount: null,
  non_personnel_resources_cost_code: null,
  non_personnel_resources_unfunded_amount: null,
  non_personnel_resources_nonfunding_obstacle: Not an system of interest,
  non_personnel_resources_nonfunding_obstacle_other_reason: Not an system of interest
)
```

