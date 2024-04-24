# PatientAuthInitRequestQueryModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | id  of the patient understood by the CM | 
**purpose** | [**PatientAuthPurposeModelModel**](PatientAuthPurposeModel.md) |  | 
**auth_mode** | [**AuthenticationModeModelModel**](AuthenticationModeModel.md) |  | [optional] 
**requester** | [**PatientAuthInitRequestQueryRequesterModelModel**](PatientAuthInitRequestQueryRequesterModel.md) |  | 

## Example

```python
from abdm.abdm.model.patient_auth_init_request_query_model import PatientAuthInitRequestQueryModel

# TODO update the JSON string below
json = "{}"
# create an instance of PatientAuthInitRequestQueryModel from a JSON string
patient_auth_init_request_query_model_instance = PatientAuthInitRequestQueryModel.from_json(json)
# print the JSON string representation of the object
print(PatientAuthInitRequestQueryModel.to_json())

# convert the object into a dict
patient_auth_init_request_query_model_dict = patient_auth_init_request_query_model_instance.to_dict()
# create an instance of PatientAuthInitRequestQueryModel from a dict
patient_auth_init_request_query_model_from_dict = PatientAuthInitRequestQueryModel.from_dict(patient_auth_init_request_query_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


