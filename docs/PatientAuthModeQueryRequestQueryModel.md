# PatientAuthModeQueryRequestQueryModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**purpose** | [**PatientAuthPurposeModelModel**](PatientAuthPurposeModel.md) |  | 
**requester** | [**PatientAuthModeQueryRequestQueryRequesterModelModel**](PatientAuthModeQueryRequestQueryRequesterModel.md) |  | 

## Example

```python
from abdm.abdm.model.patient_auth_mode_query_request_query_model import PatientAuthModeQueryRequestQueryModel

# TODO update the JSON string below
json = "{}"
# create an instance of PatientAuthModeQueryRequestQueryModel from a JSON string
patient_auth_mode_query_request_query_model_instance = PatientAuthModeQueryRequestQueryModel.from_json(json)
# print the JSON string representation of the object
print(PatientAuthModeQueryRequestQueryModel.to_json())

# convert the object into a dict
patient_auth_mode_query_request_query_model_dict = patient_auth_mode_query_request_query_model_instance.to_dict()
# create an instance of PatientAuthModeQueryRequestQueryModel from a dict
patient_auth_mode_query_request_query_model_from_dict = PatientAuthModeQueryRequestQueryModel.from_dict(patient_auth_mode_query_request_query_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


