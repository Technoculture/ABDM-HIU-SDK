# HIUSubscriptionRequestNotificationAcknowledgementModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | a nonce, unique for each HTTP request | 
**timestamp** | **datetime** | Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ | 
**acknowledgement** | [**HIUSubscriptionRequestNotificationAcknowledgementAcknowledgementModelModel**](HIUSubscriptionRequestNotificationAcknowledgementAcknowledgementModel.md) |  | [optional] 
**error** | [**ErrorModelModel**](ErrorModel.md) |  | [optional] 
**resp** | [**RequestReferenceModelModel**](RequestReferenceModel.md) |  | 

## Example

```python
from abdm.abdm.model.hiu_subscription_request_notification_acknowledgement_model import HIUSubscriptionRequestNotificationAcknowledgementModel

# TODO update the JSON string below
json = "{}"
# create an instance of HIUSubscriptionRequestNotificationAcknowledgementModel from a JSON string
hiu_subscription_request_notification_acknowledgement_model_instance = HIUSubscriptionRequestNotificationAcknowledgementModel.from_json(json)
# print the JSON string representation of the object
print(HIUSubscriptionRequestNotificationAcknowledgementModel.to_json())

# convert the object into a dict
hiu_subscription_request_notification_acknowledgement_model_dict = hiu_subscription_request_notification_acknowledgement_model_instance.to_dict()
# create an instance of HIUSubscriptionRequestNotificationAcknowledgementModel from a dict
hiu_subscription_request_notification_acknowledgement_model_from_dict = HIUSubscriptionRequestNotificationAcknowledgementModel.from_dict(hiu_subscription_request_notification_acknowledgement_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


