# SubscriptionRequestModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | a nonce, unique for each HTTP request. | 
**timestamp** | **datetime** | Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ | 
**subscription** | [**SubscriptionRequestSubscriptionModelModel**](SubscriptionRequestSubscriptionModel.md) |  | 

## Example

```python
from abdm.abdm.model.subscription_request_model import SubscriptionRequestModel

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionRequestModel from a JSON string
subscription_request_model_instance = SubscriptionRequestModel.from_json(json)
# print the JSON string representation of the object
print(SubscriptionRequestModel.to_json())

# convert the object into a dict
subscription_request_model_dict = subscription_request_model_instance.to_dict()
# create an instance of SubscriptionRequestModel from a dict
subscription_request_model_from_dict = SubscriptionRequestModel.from_dict(subscription_request_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


