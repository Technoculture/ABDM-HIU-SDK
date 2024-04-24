# ConsentRequestInitResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | a nonce, unique for each HTTP request | 
**timestamp** | **datetime** | Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ | 
**consent_request** | [**ConsentRequestInitResponseConsentRequestModelModel**](ConsentRequestInitResponseConsentRequestModel.md) |  | [optional] 
**error** | [**ErrorModelModel**](ErrorModel.md) |  | [optional] 
**resp** | [**RequestReferenceModelModel**](RequestReferenceModel.md) |  | 

## Example

```python
from abdm.abdm.model.consent_request_init_response_model import ConsentRequestInitResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of ConsentRequestInitResponseModel from a JSON string
consent_request_init_response_model_instance = ConsentRequestInitResponseModel.from_json(json)
# print the JSON string representation of the object
print(ConsentRequestInitResponseModel.to_json())

# convert the object into a dict
consent_request_init_response_model_dict = consent_request_init_response_model_instance.to_dict()
# create an instance of ConsentRequestInitResponseModel from a dict
consent_request_init_response_model_from_dict = ConsentRequestInitResponseModel.from_dict(consent_request_init_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


