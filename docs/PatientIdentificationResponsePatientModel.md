# PatientIdentificationResponsePatientModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 

## Example

```python
from abdm.abdm.model.patient_identification_response_patient_model import PatientIdentificationResponsePatientModel

# TODO update the JSON string below
json = "{}"
# create an instance of PatientIdentificationResponsePatientModel from a JSON string
patient_identification_response_patient_model_instance = PatientIdentificationResponsePatientModel.from_json(json)
# print the JSON string representation of the object
print(PatientIdentificationResponsePatientModel.to_json())

# convert the object into a dict
patient_identification_response_patient_model_dict = patient_identification_response_patient_model_instance.to_dict()
# create an instance of PatientIdentificationResponsePatientModel from a dict
patient_identification_response_patient_model_from_dict = PatientIdentificationResponsePatientModel.from_dict(patient_identification_response_patient_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


