# DataNotificationEntriesInnerModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** | Encrypted content | 
**media** | **str** | mimetype of the content. | 
**checksum** | **str** | Md5 checksum of the content before encryption | 
**care_context_reference** | **str** | care context reference number. | 
**link** | **str** | Encrypted content | 

## Example

```python
from abdm.abdm.model.data_notification_entries_inner_model import DataNotificationEntriesInnerModel

# TODO update the JSON string below
json = "{}"
# create an instance of DataNotificationEntriesInnerModel from a JSON string
data_notification_entries_inner_model_instance = DataNotificationEntriesInnerModel.from_json(json)
# print the JSON string representation of the object
print(DataNotificationEntriesInnerModel.to_json())

# convert the object into a dict
data_notification_entries_inner_model_dict = data_notification_entries_inner_model_instance.to_dict()
# create an instance of DataNotificationEntriesInnerModel from a dict
data_notification_entries_inner_model_from_dict = DataNotificationEntriesInnerModel.from_dict(data_notification_entries_inner_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


