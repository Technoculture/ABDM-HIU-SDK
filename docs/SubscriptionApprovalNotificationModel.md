# SubscriptionApprovalNotificationModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | a nonce, unique for each HTTP request | 
**timestamp** | **datetime** | Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ | 
**notification** | [**SubscriptionApprovalNotificationNotificationModelModel**](SubscriptionApprovalNotificationNotificationModel.md) |  | 

## Example

```python
from abdm.abdm.model.subscription_approval_notification_model import SubscriptionApprovalNotificationModel

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionApprovalNotificationModel from a JSON string
subscription_approval_notification_model_instance = SubscriptionApprovalNotificationModel.from_json(json)
# print the JSON string representation of the object
print(SubscriptionApprovalNotificationModel.to_json())

# convert the object into a dict
subscription_approval_notification_model_dict = subscription_approval_notification_model_instance.to_dict()
# create an instance of SubscriptionApprovalNotificationModel from a dict
subscription_approval_notification_model_from_dict = SubscriptionApprovalNotificationModel.from_dict(subscription_approval_notification_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


