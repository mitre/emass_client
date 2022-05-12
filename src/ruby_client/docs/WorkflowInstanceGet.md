# EmassClient::WorkflowInstanceGet

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **workflow_uid** | **String** | [Read-Only] Unique workflow definition identifier. | [optional] |
| **system_name** | **String** | [Read-Only] The system name. | [optional] |
| **workflow_instance_id** | **Integer** | [Read-Only] Unique workflow instance identifier. | [optional] |
| **package_name** | **String** | [Read-Only] The package name. | [optional] |
| **created_date** | **Integer** | [Read-Only] Date the workflow instance or the workflow transition was created. | [optional] |
| **last_edited_date** | **Integer** | [Read-Only] Date the workflow was last acted on. | [optional] |
| **last_edited_by** | **String** | [Read-Only] User that last acted on the workflow. | [optional] |
| **workflow** | **String** | [Read-Only] The workflow type. | [optional] |
| **version** | **String** | [Read-Only] Version of the workflow definition. | [optional] |
| **current_stage** | **String** | [Read-Only] Name of the current stage. | [optional] |
| **transitions** | [**Array&lt;InstancesTransitions&gt;**](InstancesTransitions.md) |  | [optional] |

## Example

```ruby
require 'emass_client'

instance = EmassClient::WorkflowInstanceGet.new(
  workflow_uid: 6f810301-5b3b-4f89-81e7-587fef9142a9,
  system_name: Test system 1,
  workflow_instance_id: 35,
  package_name: Test RMF Step 1 package,
  created_date: 1636124623,
  last_edited_date: 1631130837,
  last_edited_by: john.doe.ctr@mail.mil,
  workflow: RMF Step 1: Security Category,
  version: 4,
  current_stage: Echelon II,
  transitions: null
)
```

