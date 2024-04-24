# PatientAuthModeQueryRequestModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | a nonce, unique for each HTTP request | 
**timestamp** | **datetime** | Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ | 
**query** | [**PatientAuthModeQueryRequestQueryModelModel**](PatientAuthModeQueryRequestQueryModel.md) |  | 

## Example

```python
from abdm.abdm.model.patient_auth_mode_query_request_model import PatientAuthModeQueryRequestModel

# TODO update the JSON string below
json = "{}"
# create an instance of PatientAuthModeQueryRequestModel from a JSON string
patient_auth_mode_query_request_model_instance = PatientAuthModeQueryRequestModel.from_json(json)
# print the JSON string representation of the object
print(PatientAuthModeQueryRequestModel.to_json())

# convert the object into a dict
patient_auth_mode_query_request_model_dict = patient_auth_mode_query_request_model_instance.to_dict()
# create an instance of PatientAuthModeQueryRequestModel from a dict
patient_auth_mode_query_request_model_from_dict = PatientAuthModeQueryRequestModel.from_dict(patient_auth_mode_query_request_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


