# EntryContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** | Encrypted content | 
**media** | **str** | mimetype of the content. | 
**checksum** | **str** | Md5 checksum of the content before encryption | 
**care_context_reference** | **str** | care context reference number. | 

## Example

```python
from abdm.models.entry_content import EntryContent

# TODO update the JSON string below
json = "{}"
# create an instance of EntryContent from a JSON string
entry_content_instance = EntryContent.from_json(json)
# print the JSON string representation of the object
print(EntryContent.to_json())

# convert the object into a dict
entry_content_dict = entry_content_instance.to_dict()
# create an instance of EntryContent from a dict
entry_content_from_dict = EntryContent.from_dict(entry_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


