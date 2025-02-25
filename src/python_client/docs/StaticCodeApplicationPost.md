# StaticCodeApplicationPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**raw_severity** | **str** | [Optional] Scan vulnerability ratting | [optional] 
**code_check_name** | **str** | [Required] Name of the software vulnerability or weakness. | [optional] 
**count** | **int** | [Required] Number of instances observed for a specified finding. | [optional] 
**scan_date** | **int** | [Required] The date of the scan. Unix date format. | [optional] 
**cwe_id** | **str** | [Required] The Common Weakness Enumerator (CWE) identifier. | [optional] 
**clear_findings** | **bool** | [Optional] When used by itself, can clear out all application findings for a single application/version pairing. | [optional] 

## Example

```python
from emass_client.models.static_code_application_post import StaticCodeApplicationPost

# TODO update the JSON string below
json = "{}"
# create an instance of StaticCodeApplicationPost from a JSON string
static_code_application_post_instance = StaticCodeApplicationPost.from_json(json)
# print the JSON string representation of the object
print(StaticCodeApplicationPost.to_json())

# convert the object into a dict
static_code_application_post_dict = static_code_application_post_instance.to_dict()
# create an instance of StaticCodeApplicationPost from a dict
static_code_application_post_from_dict = StaticCodeApplicationPost.from_dict(static_code_application_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


