# HealthInformationNotificationNotificationModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consent_id** | **str** |  | 
**transaction_id** | **str** |  | 
**done_at** | **datetime** |  | 
**notifier** | [**HealthInformationNotificationNotificationNotifierModelModel**](HealthInformationNotificationNotificationNotifierModel.md) |  | 
**status_notification** | [**HealthInformationNotificationNotificationStatusNotificationModelModel**](HealthInformationNotificationNotificationStatusNotificationModel.md) |  | 

## Example

```python
from abdm.abdm.model.health_information_notification_notification_model import HealthInformationNotificationNotificationModel

# TODO update the JSON string below
json = "{}"
# create an instance of HealthInformationNotificationNotificationModel from a JSON string
health_information_notification_notification_model_instance = HealthInformationNotificationNotificationModel.from_json(json)
# print the JSON string representation of the object
print(HealthInformationNotificationNotificationModel.to_json())

# convert the object into a dict
health_information_notification_notification_model_dict = health_information_notification_notification_model_instance.to_dict()
# create an instance of HealthInformationNotificationNotificationModel from a dict
health_information_notification_notification_model_from_dict = HealthInformationNotificationNotificationModel.from_dict(health_information_notification_notification_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


