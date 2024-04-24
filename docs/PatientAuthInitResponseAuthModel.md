# PatientAuthInitResponseAuthModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** |  | 
**mode** | [**AuthenticationModeModelModel**](AuthenticationModeModel.md) |  | 
**meta** | [**AuthMetaModelModel**](AuthMetaModel.md) |  | [optional] 

## Example

```python
from abdm.abdm.model.patient_auth_init_response_auth_model import PatientAuthInitResponseAuthModel

# TODO update the JSON string below
json = "{}"
# create an instance of PatientAuthInitResponseAuthModel from a JSON string
patient_auth_init_response_auth_model_instance = PatientAuthInitResponseAuthModel.from_json(json)
# print the JSON string representation of the object
print(PatientAuthInitResponseAuthModel.to_json())

# convert the object into a dict
patient_auth_init_response_auth_model_dict = patient_auth_init_response_auth_model_instance.to_dict()
# create an instance of PatientAuthInitResponseAuthModel from a dict
patient_auth_init_response_auth_model_from_dict = PatientAuthInitResponseAuthModel.from_dict(patient_auth_init_response_auth_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


