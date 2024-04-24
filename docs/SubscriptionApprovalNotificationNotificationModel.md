# SubscriptionApprovalNotificationNotificationModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscription_request_id** | **str** |  | [optional] 
**status** | [**SubscriptionStatusModelModel**](SubscriptionStatusModel.md) |  | 
**subscription** | [**HIUSubscriptionModelModel**](HIUSubscriptionModel.md) |  | [optional] 

## Example

```python
from abdm.abdm.model.subscription_approval_notification_notification_model import SubscriptionApprovalNotificationNotificationModel

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionApprovalNotificationNotificationModel from a JSON string
subscription_approval_notification_notification_model_instance = SubscriptionApprovalNotificationNotificationModel.from_json(json)
# print the JSON string representation of the object
print(SubscriptionApprovalNotificationNotificationModel.to_json())

# convert the object into a dict
subscription_approval_notification_notification_model_dict = subscription_approval_notification_notification_model_instance.to_dict()
# create an instance of SubscriptionApprovalNotificationNotificationModel from a dict
subscription_approval_notification_notification_model_from_dict = SubscriptionApprovalNotificationNotificationModel.from_dict(subscription_approval_notification_notification_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


