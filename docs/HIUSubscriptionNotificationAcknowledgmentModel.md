# HIUSubscriptionNotificationAcknowledgmentModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | a nonce, unique for each HTTP request | 
**timestamp** | **datetime** | Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ | 
**acknowledgement** | [**HIUSubscriptionNotificationAcknowledgmentAcknowledgementModelModel**](HIUSubscriptionNotificationAcknowledgmentAcknowledgementModel.md) |  | [optional] 
**error** | [**ErrorModelModel**](ErrorModel.md) |  | [optional] 
**resp** | [**RequestReferenceModelModel**](RequestReferenceModel.md) |  | 

## Example

```python
from abdm.abdm.model.hiu_subscription_notification_acknowledgment_model import HIUSubscriptionNotificationAcknowledgmentModel

# TODO update the JSON string below
json = "{}"
# create an instance of HIUSubscriptionNotificationAcknowledgmentModel from a JSON string
hiu_subscription_notification_acknowledgment_model_instance = HIUSubscriptionNotificationAcknowledgmentModel.from_json(json)
# print the JSON string representation of the object
print(HIUSubscriptionNotificationAcknowledgmentModel.to_json())

# convert the object into a dict
hiu_subscription_notification_acknowledgment_model_dict = hiu_subscription_notification_acknowledgment_model_instance.to_dict()
# create an instance of HIUSubscriptionNotificationAcknowledgmentModel from a dict
hiu_subscription_notification_acknowledgment_model_from_dict = HIUSubscriptionNotificationAcknowledgmentModel.from_dict(hiu_subscription_notification_acknowledgment_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


