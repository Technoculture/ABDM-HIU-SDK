# HealthInformationNotificationNotificationStatusNotificationModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_status** | **str** |  | 
**hip_id** | **str** |  | 
**status_responses** | [**List[HealthInformationNotificationNotificationStatusNotificationStatusResponsesInnerModelModel]**](HealthInformationNotificationNotificationStatusNotificationStatusResponsesInnerModel.md) |  | [optional] 

## Example

```python
from abdm.abdm.model.health_information_notification_notification_status_notification_model import HealthInformationNotificationNotificationStatusNotificationModel

# TODO update the JSON string below
json = "{}"
# create an instance of HealthInformationNotificationNotificationStatusNotificationModel from a JSON string
health_information_notification_notification_status_notification_model_instance = HealthInformationNotificationNotificationStatusNotificationModel.from_json(json)
# print the JSON string representation of the object
print(HealthInformationNotificationNotificationStatusNotificationModel.to_json())

# convert the object into a dict
health_information_notification_notification_status_notification_model_dict = health_information_notification_notification_status_notification_model_instance.to_dict()
# create an instance of HealthInformationNotificationNotificationStatusNotificationModel from a dict
health_information_notification_notification_status_notification_model_from_dict = HealthInformationNotificationNotificationStatusNotificationModel.from_dict(health_information_notification_notification_status_notification_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


