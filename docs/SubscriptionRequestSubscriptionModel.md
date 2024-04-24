# SubscriptionRequestSubscriptionModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**purpose** | [**UsePurposeModelModel**](UsePurposeModel.md) |  | 
**patient** | [**ConsentManagerPatientIDModelModel**](ConsentManagerPatientIDModel.md) |  | 
**hiu** | [**OrganizationRepresentationModelModel**](OrganizationRepresentationModel.md) |  | 
**hips** | [**List[OrganizationRepresentationModelModel]**](OrganizationRepresentationModel.md) |  | [optional] 
**categories** | [**List[SubscriptionCategoryModelModel]**](SubscriptionCategoryModel.md) |  | 
**period** | [**SubscriptionPeriodModelModel**](SubscriptionPeriodModel.md) |  | 

## Example

```python
from abdm.abdm.model.subscription_request_subscription_model import SubscriptionRequestSubscriptionModel

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionRequestSubscriptionModel from a JSON string
subscription_request_subscription_model_instance = SubscriptionRequestSubscriptionModel.from_json(json)
# print the JSON string representation of the object
print(SubscriptionRequestSubscriptionModel.to_json())

# convert the object into a dict
subscription_request_subscription_model_dict = subscription_request_subscription_model_instance.to_dict()
# create an instance of SubscriptionRequestSubscriptionModel from a dict
subscription_request_subscription_model_from_dict = SubscriptionRequestSubscriptionModel.from_dict(subscription_request_subscription_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


