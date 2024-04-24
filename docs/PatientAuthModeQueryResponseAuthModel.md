# PatientAuthModeQueryResponseAuthModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**purpose** | [**PatientAuthPurposeModelModel**](PatientAuthPurposeModel.md) |  | 
**modes** | [**List[AuthenticationModeModelModel]**](AuthenticationModeModel.md) |  | 

## Example

```python
from abdm.abdm.model.patient_auth_mode_query_response_auth_model import PatientAuthModeQueryResponseAuthModel

# TODO update the JSON string below
json = "{}"
# create an instance of PatientAuthModeQueryResponseAuthModel from a JSON string
patient_auth_mode_query_response_auth_model_instance = PatientAuthModeQueryResponseAuthModel.from_json(json)
# print the JSON string representation of the object
print(PatientAuthModeQueryResponseAuthModel.to_json())

# convert the object into a dict
patient_auth_mode_query_response_auth_model_dict = patient_auth_mode_query_response_auth_model_instance.to_dict()
# create an instance of PatientAuthModeQueryResponseAuthModel from a dict
patient_auth_mode_query_response_auth_model_from_dict = PatientAuthModeQueryResponseAuthModel.from_dict(patient_auth_mode_query_response_auth_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


