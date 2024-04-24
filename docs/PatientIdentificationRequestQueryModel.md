# PatientIdentificationRequestQueryModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**patient** | [**PatientIdentificationRequestQueryPatientModelModel**](PatientIdentificationRequestQueryPatientModel.md) |  | 
**requester** | [**PatientIdentificationRequestQueryRequesterModelModel**](PatientIdentificationRequestQueryRequesterModel.md) |  | 

## Example

```python
from abdm.abdm.model.patient_identification_request_query_model import PatientIdentificationRequestQueryModel

# TODO update the JSON string below
json = "{}"
# create an instance of PatientIdentificationRequestQueryModel from a JSON string
patient_identification_request_query_model_instance = PatientIdentificationRequestQueryModel.from_json(json)
# print the JSON string representation of the object
print(PatientIdentificationRequestQueryModel.to_json())

# convert the object into a dict
patient_identification_request_query_model_dict = patient_identification_request_query_model_instance.to_dict()
# create an instance of PatientIdentificationRequestQueryModel from a dict
patient_identification_request_query_model_from_dict = PatientIdentificationRequestQueryModel.from_dict(patient_identification_request_query_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


