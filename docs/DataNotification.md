# DataNotification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_number** | **int** | Current page number. | 
**page_count** | **int** | Total number of pages. | 
**transaction_id** | **str** | Transaction Id issued when data requested. | 
**entries** | [**List[DataNotificationEntriesInner]**](DataNotificationEntriesInner.md) |  | 
**key_material** | [**KeyMaterial**](KeyMaterial.md) |  | 

## Example

```python
from abdm.models.data_notification import DataNotification

# TODO update the JSON string below
json = "{}"
# create an instance of DataNotification from a JSON string
data_notification_instance = DataNotification.from_json(json)
# print the JSON string representation of the object
print(DataNotification.to_json())

# convert the object into a dict
data_notification_dict = data_notification_instance.to_dict()
# create an instance of DataNotification from a dict
data_notification_from_dict = DataNotification.from_dict(data_notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


