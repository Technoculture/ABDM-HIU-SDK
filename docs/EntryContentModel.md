# EntryContentModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** | Encrypted content | 
**media** | **str** | mimetype of the content. | 
**checksum** | **str** | Md5 checksum of the content before encryption | 
**care_context_reference** | **str** | care context reference number. | 

## Example

```python
from abdm.abdm.model.entry_content_model import EntryContentModel

# TODO update the JSON string below
json = "{}"
# create an instance of EntryContentModel from a JSON string
entry_content_model_instance = EntryContentModel.from_json(json)
# print the JSON string representation of the object
print(EntryContentModel.to_json())

# convert the object into a dict
entry_content_model_dict = entry_content_model_instance.to_dict()
# create an instance of EntryContentModel from a dict
entry_content_model_from_dict = EntryContentModel.from_dict(entry_content_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


