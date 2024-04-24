# EntryLinkModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** | Encrypted content | 
**media** | **str** | mimetype of the content. | 
**checksum** | **str** | Md5 checksum of the content before encryption | 
**care_context_reference** | **str** | care context reference number. | 

## Example

```python
from abdm.abdm.model.entry_link_model import EntryLinkModel

# TODO update the JSON string below
json = "{}"
# create an instance of EntryLinkModel from a JSON string
entry_link_model_instance = EntryLinkModel.from_json(json)
# print the JSON string representation of the object
print(EntryLinkModel.to_json())

# convert the object into a dict
entry_link_model_dict = entry_link_model_instance.to_dict()
# create an instance of EntryLinkModel from a dict
entry_link_model_from_dict = EntryLinkModel.from_dict(entry_link_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


