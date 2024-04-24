# HIUConsentRequestStatusModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | a nonce, unique for each HTTP request | 
**timestamp** | **datetime** | Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ | 
**consent_request** | [**HIUConsentRequestStatusConsentRequestModelModel**](HIUConsentRequestStatusConsentRequestModel.md) |  | [optional] 
**error** | [**ErrorModelModel**](ErrorModel.md) |  | [optional] 
**resp** | [**RequestReferenceModelModel**](RequestReferenceModel.md) |  | 

## Example

```python
from abdm.abdm.model.hiu_consent_request_status_model import HIUConsentRequestStatusModel

# TODO update the JSON string below
json = "{}"
# create an instance of HIUConsentRequestStatusModel from a JSON string
hiu_consent_request_status_model_instance = HIUConsentRequestStatusModel.from_json(json)
# print the JSON string representation of the object
print(HIUConsentRequestStatusModel.to_json())

# convert the object into a dict
hiu_consent_request_status_model_dict = hiu_consent_request_status_model_instance.to_dict()
# create an instance of HIUConsentRequestStatusModel from a dict
hiu_consent_request_status_model_from_dict = HIUConsentRequestStatusModel.from_dict(hiu_consent_request_status_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


