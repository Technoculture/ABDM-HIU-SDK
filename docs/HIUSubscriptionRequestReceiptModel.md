# HIUSubscriptionRequestReceiptModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | a nonce, unique for each HTTP request | 
**timestamp** | **datetime** | Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ | 
**subscription_request** | [**ConsentRequestInitResponseConsentRequestModelModel**](ConsentRequestInitResponseConsentRequestModel.md) |  | [optional] 
**error** | [**ErrorModelModel**](ErrorModel.md) |  | [optional] 
**resp** | [**RequestReferenceModelModel**](RequestReferenceModel.md) |  | 

## Example

```python
from abdm.abdm.model.hiu_subscription_request_receipt_model import HIUSubscriptionRequestReceiptModel

# TODO update the JSON string below
json = "{}"
# create an instance of HIUSubscriptionRequestReceiptModel from a JSON string
hiu_subscription_request_receipt_model_instance = HIUSubscriptionRequestReceiptModel.from_json(json)
# print the JSON string representation of the object
print(HIUSubscriptionRequestReceiptModel.to_json())

# convert the object into a dict
hiu_subscription_request_receipt_model_dict = hiu_subscription_request_receipt_model_instance.to_dict()
# create an instance of HIUSubscriptionRequestReceiptModel from a dict
hiu_subscription_request_receipt_model_from_dict = HIUSubscriptionRequestReceiptModel.from_dict(hiu_subscription_request_receipt_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


