# HIUSubscriptionNotificationEventModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**published** | **datetime** | Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ | 
**subscription_id** | **str** |  | 
**category** | [**SubscriptionCategoryModelModel**](SubscriptionCategoryModel.md) |  | 
**content** | [**HIUSubscriptionEventContentModelModel**](HIUSubscriptionEventContentModel.md) |  | 

## Example

```python
from abdm.abdm.model.hiu_subscription_notification_event_model import HIUSubscriptionNotificationEventModel

# TODO update the JSON string below
json = "{}"
# create an instance of HIUSubscriptionNotificationEventModel from a JSON string
hiu_subscription_notification_event_model_instance = HIUSubscriptionNotificationEventModel.from_json(json)
# print the JSON string representation of the object
print(HIUSubscriptionNotificationEventModel.to_json())

# convert the object into a dict
hiu_subscription_notification_event_model_dict = hiu_subscription_notification_event_model_instance.to_dict()
# create an instance of HIUSubscriptionNotificationEventModel from a dict
hiu_subscription_notification_event_model_from_dict = HIUSubscriptionNotificationEventModel.from_dict(hiu_subscription_notification_event_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


