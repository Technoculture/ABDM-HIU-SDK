# PatientDemographicResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | PHR Identifier of patient at consent manager | 
**name** | **str** |  | 
**gender** | [**PatientGenderModelModel**](PatientGenderModel.md) |  | 
**year_of_birth** | **int** |  | 
**address** | [**PatientAddressModelModel**](PatientAddressModel.md) |  | [optional] 
**identifiers** | [**List[IdentifierModelModel]**](IdentifierModel.md) |  | [optional] 

## Example

```python
from abdm.abdm.model.patient_demographic_response_model import PatientDemographicResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of PatientDemographicResponseModel from a JSON string
patient_demographic_response_model_instance = PatientDemographicResponseModel.from_json(json)
# print the JSON string representation of the object
print(PatientDemographicResponseModel.to_json())

# convert the object into a dict
patient_demographic_response_model_dict = patient_demographic_response_model_instance.to_dict()
# create an instance of PatientDemographicResponseModel from a dict
patient_demographic_response_model_from_dict = PatientDemographicResponseModel.from_dict(patient_demographic_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


