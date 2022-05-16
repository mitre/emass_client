# EmassClient::WorkflowDefinitionGet

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **workflow_uid** | **String** | [Read-Only] Unique workflow definition identifier. | [optional] |
| **workflow** | **String** | [Read-Only] The workflow type. | [optional] |
| **version** | **String** | [Read-Only] Version of the workflow definition. | [optional] |
| **description** | **String** | [Read-Only] Description of the workflow or the stage transition. | [optional] |
| **is_active** | **Boolean** | [Read-Only] Returns true if the workflow is available to the site. | [optional] |
| **stages** | [**Array&lt;Stage&gt;**](Stage.md) |  | [optional] |

## Example

```ruby
require 'emass_client'

instance = EmassClient::WorkflowDefinitionGet.new(
  workflow_uid: 6f810301-5b3b-4f89-81e7-587fef9142a9,
  workflow: RMF Step 1: Security Category,
  version: 4,
  description: The workflow description,
  is_active: false,
  stages: null
)
```

