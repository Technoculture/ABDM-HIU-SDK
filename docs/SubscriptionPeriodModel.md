# SubscriptionPeriodModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **datetime** |  | 
**to** | **datetime** |  | 

## Example

```python
from abdm.abdm.model.subscription_period_model import SubscriptionPeriodModel

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionPeriodModel from a JSON string
subscription_period_model_instance = SubscriptionPeriodModel.from_json(json)
# print the JSON string representation of the object
print(SubscriptionPeriodModel.to_json())

# convert the object into a dict
subscription_period_model_dict = subscription_period_model_instance.to_dict()
# create an instance of SubscriptionPeriodModel from a dict
subscription_period_model_from_dict = SubscriptionPeriodModel.from_dict(subscription_period_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


