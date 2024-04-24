# HIUConsentNotificationResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | a nonce, unique for each HTTP request | 
**timestamp** | **datetime** | Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ | 
**acknowledgement** | [**List[ConsentAcknowledgementModelModel]**](ConsentAcknowledgementModel.md) |  | [optional] 
**error** | [**ErrorModelModel**](ErrorModel.md) |  | [optional] 
**resp** | [**RequestReferenceModelModel**](RequestReferenceModel.md) |  | 

## Example

```python
from abdm.abdm.model.hiu_consent_notification_response_model import HIUConsentNotificationResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of HIUConsentNotificationResponseModel from a JSON string
hiu_consent_notification_response_model_instance = HIUConsentNotificationResponseModel.from_json(json)
# print the JSON string representation of the object
print(HIUConsentNotificationResponseModel.to_json())

# convert the object into a dict
hiu_consent_notification_response_model_dict = hiu_consent_notification_response_model_instance.to_dict()
# create an instance of HIUConsentNotificationResponseModel from a dict
hiu_consent_notification_response_model_from_dict = HIUConsentNotificationResponseModel.from_dict(hiu_consent_notification_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


