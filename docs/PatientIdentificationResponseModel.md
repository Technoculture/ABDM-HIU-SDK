# PatientIdentificationResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | a nonce, unique for each HTTP request | 
**timestamp** | **datetime** | Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ | 
**patient** | [**PatientIdentificationResponsePatientModelModel**](PatientIdentificationResponsePatientModel.md) |  | [optional] 
**error** | [**ErrorModelModel**](ErrorModel.md) |  | [optional] 
**resp** | [**RequestReferenceModelModel**](RequestReferenceModel.md) |  | 

## Example

```python
from abdm.abdm.model.patient_identification_response_model import PatientIdentificationResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of PatientIdentificationResponseModel from a JSON string
patient_identification_response_model_instance = PatientIdentificationResponseModel.from_json(json)
# print the JSON string representation of the object
print(PatientIdentificationResponseModel.to_json())

# convert the object into a dict
patient_identification_response_model_dict = patient_identification_response_model_instance.to_dict()
# create an instance of PatientIdentificationResponseModel from a dict
patient_identification_response_model_from_dict = PatientIdentificationResponseModel.from_dict(patient_identification_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


