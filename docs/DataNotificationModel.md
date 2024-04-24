# DataNotificationModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_number** | **int** | Current page number. | 
**page_count** | **int** | Total number of pages. | 
**transaction_id** | **str** | Transaction Id issued when data requested. | 
**entries** | [**List[DataNotificationEntriesInnerModelModel]**](DataNotificationEntriesInnerModel.md) |  | 
**key_material** | [**KeyMaterialModelModel**](KeyMaterialModel.md) |  | 

## Example

```python
from abdm.abdm.model.data_notification_model import DataNotificationModel

# TODO update the JSON string below
json = "{}"
# create an instance of DataNotificationModel from a JSON string
data_notification_model_instance = DataNotificationModel.from_json(json)
# print the JSON string representation of the object
print(DataNotificationModel.to_json())

# convert the object into a dict
data_notification_model_dict = data_notification_model_instance.to_dict()
# create an instance of DataNotificationModel from a dict
data_notification_model_from_dict = DataNotificationModel.from_dict(data_notification_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


