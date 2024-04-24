# PatientAuthRequesterModel

identification of requester

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**id** | **str** |  | 

## Example

```python
from abdm.abdm.model.patient_auth_requester_model import PatientAuthRequesterModel

# TODO update the JSON string below
json = "{}"
# create an instance of PatientAuthRequesterModel from a JSON string
patient_auth_requester_model_instance = PatientAuthRequesterModel.from_json(json)
# print the JSON string representation of the object
print(PatientAuthRequesterModel.to_json())

# convert the object into a dict
patient_auth_requester_model_dict = patient_auth_requester_model_instance.to_dict()
# create an instance of PatientAuthRequesterModel from a dict
patient_auth_requester_model_from_dict = PatientAuthRequesterModel.from_dict(patient_auth_requester_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


