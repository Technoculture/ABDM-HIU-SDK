# EntryLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** | Encrypted content | 
**media** | **str** | mimetype of the content. | 
**checksum** | **str** | Md5 checksum of the content before encryption | 
**care_context_reference** | **str** | care context reference number. | 

## Example

```python
from abdm.models.entry_link import EntryLink

# TODO update the JSON string below
json = "{}"
# create an instance of EntryLink from a JSON string
entry_link_instance = EntryLink.from_json(json)
# print the JSON string representation of the object
print(EntryLink.to_json())

# convert the object into a dict
entry_link_dict = entry_link_instance.to_dict()
# create an instance of EntryLink from a dict
entry_link_from_dict = EntryLink.from_dict(entry_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


