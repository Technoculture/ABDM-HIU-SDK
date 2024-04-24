# PatientDemographicModel

Demographic details are only required for demographic auth at this point. Demographic details must be same as registered

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**gender** | [**PatientGenderModelModel**](PatientGenderModel.md) |  | 
**date_of_birth** | **str** | date of birth in YYYY-MM-DD format. | 
**identifier** | [**AuthConfirmIdentifierModelModel**](AuthConfirmIdentifierModel.md) |  | [optional] 

## Example

```python
from abdm.abdm.model.patient_demographic_model import PatientDemographicModel

# TODO update the JSON string below
json = "{}"
# create an instance of PatientDemographicModel from a JSON string
patient_demographic_model_instance = PatientDemographicModel.from_json(json)
# print the JSON string representation of the object
print(PatientDemographicModel.to_json())

# convert the object into a dict
patient_demographic_model_dict = patient_demographic_model_instance.to_dict()
# create an instance of PatientDemographicModel from a dict
patient_demographic_model_from_dict = PatientDemographicModel.from_dict(patient_demographic_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


