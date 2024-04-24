# HIUSubscriptionContextModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hip** | [**OrganizationRepresentationModelModel**](OrganizationRepresentationModel.md) |  | [optional] 
**categories** | [**List[SubscriptionCategoryModelModel]**](SubscriptionCategoryModel.md) |  | 
**period** | [**SubscriptionPeriodModelModel**](SubscriptionPeriodModel.md) |  | 

## Example

```python
from abdm.abdm.model.hiu_subscription_context_model import HIUSubscriptionContextModel

# TODO update the JSON string below
json = "{}"
# create an instance of HIUSubscriptionContextModel from a JSON string
hiu_subscription_context_model_instance = HIUSubscriptionContextModel.from_json(json)
# print the JSON string representation of the object
print(HIUSubscriptionContextModel.to_json())

# convert the object into a dict
hiu_subscription_context_model_dict = hiu_subscription_context_model_instance.to_dict()
# create an instance of HIUSubscriptionContextModel from a dict
hiu_subscription_context_model_from_dict = HIUSubscriptionContextModel.from_dict(hiu_subscription_context_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


