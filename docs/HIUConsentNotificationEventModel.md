# HIUConsentNotificationEventModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | a nonce, unique for each HTTP request | 
**timestamp** | **datetime** | Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ | 
**notification** | [**HIUConsentNotificationEventNotificationModelModel**](HIUConsentNotificationEventNotificationModel.md) |  | 

## Example

```python
from abdm.abdm.model.hiu_consent_notification_event_model import HIUConsentNotificationEventModel

# TODO update the JSON string below
json = "{}"
# create an instance of HIUConsentNotificationEventModel from a JSON string
hiu_consent_notification_event_model_instance = HIUConsentNotificationEventModel.from_json(json)
# print the JSON string representation of the object
print(HIUConsentNotificationEventModel.to_json())

# convert the object into a dict
hiu_consent_notification_event_model_dict = hiu_consent_notification_event_model_instance.to_dict()
# create an instance of HIUConsentNotificationEventModel from a dict
hiu_consent_notification_event_model_from_dict = HIUConsentNotificationEventModel.from_dict(hiu_consent_notification_event_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


