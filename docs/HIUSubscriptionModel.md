# HIUSubscriptionModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**patient** | [**ConsentManagerPatientIDModelModel**](ConsentManagerPatientIDModel.md) |  | 
**hiu** | [**OrganizationRepresentationModelModel**](OrganizationRepresentationModel.md) |  | 
**sources** | [**List[HIUSubscriptionContextModelModel]**](HIUSubscriptionContextModel.md) |  | 

## Example

```python
from abdm.abdm.model.hiu_subscription_model import HIUSubscriptionModel

# TODO update the JSON string below
json = "{}"
# create an instance of HIUSubscriptionModel from a JSON string
hiu_subscription_model_instance = HIUSubscriptionModel.from_json(json)
# print the JSON string representation of the object
print(HIUSubscriptionModel.to_json())

# convert the object into a dict
hiu_subscription_model_dict = hiu_subscription_model_instance.to_dict()
# create an instance of HIUSubscriptionModel from a dict
hiu_subscription_model_from_dict = HIUSubscriptionModel.from_dict(hiu_subscription_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


