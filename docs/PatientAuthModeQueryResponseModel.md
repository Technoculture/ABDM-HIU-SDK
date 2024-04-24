# PatientAuthModeQueryResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | a nonce, unique for each HTTP request | 
**timestamp** | **datetime** | Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ | 
**auth** | [**PatientAuthModeQueryResponseAuthModelModel**](PatientAuthModeQueryResponseAuthModel.md) |  | [optional] 
**error** | [**ErrorModelModel**](ErrorModel.md) |  | [optional] 
**resp** | [**RequestReferenceModelModel**](RequestReferenceModel.md) |  | 

## Example

```python
from abdm.abdm.model.patient_auth_mode_query_response_model import PatientAuthModeQueryResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of PatientAuthModeQueryResponseModel from a JSON string
patient_auth_mode_query_response_model_instance = PatientAuthModeQueryResponseModel.from_json(json)
# print the JSON string representation of the object
print(PatientAuthModeQueryResponseModel.to_json())

# convert the object into a dict
patient_auth_mode_query_response_model_dict = patient_auth_mode_query_response_model_instance.to_dict()
# create an instance of PatientAuthModeQueryResponseModel from a dict
patient_auth_mode_query_response_model_from_dict = PatientAuthModeQueryResponseModel.from_dict(patient_auth_mode_query_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


