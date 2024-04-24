# HealthInformationNotificationModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | a nonce, unique for each HTTP request. | 
**timestamp** | **datetime** | Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ | 
**notification** | [**HealthInformationNotificationNotificationModelModel**](HealthInformationNotificationNotificationModel.md) |  | 

## Example

```python
from abdm.abdm.model.health_information_notification_model import HealthInformationNotificationModel

# TODO update the JSON string below
json = "{}"
# create an instance of HealthInformationNotificationModel from a JSON string
health_information_notification_model_instance = HealthInformationNotificationModel.from_json(json)
# print the JSON string representation of the object
print(HealthInformationNotificationModel.to_json())

# convert the object into a dict
health_information_notification_model_dict = health_information_notification_model_instance.to_dict()
# create an instance of HealthInformationNotificationModel from a dict
health_information_notification_model_from_dict = HealthInformationNotificationModel.from_dict(health_information_notification_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


