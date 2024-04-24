# PatientAuthConfirmRequestCredentialModel

note, demographic details are only required for demographic auth at this point.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_code** | **str** |  | [optional] 
**demographic** | [**PatientDemographicModelModel**](PatientDemographicModel.md) |  | [optional] 

## Example

```python
from abdm.abdm.model.patient_auth_confirm_request_credential_model import PatientAuthConfirmRequestCredentialModel

# TODO update the JSON string below
json = "{}"
# create an instance of PatientAuthConfirmRequestCredentialModel from a JSON string
patient_auth_confirm_request_credential_model_instance = PatientAuthConfirmRequestCredentialModel.from_json(json)
# print the JSON string representation of the object
print(PatientAuthConfirmRequestCredentialModel.to_json())

# convert the object into a dict
patient_auth_confirm_request_credential_model_dict = patient_auth_confirm_request_credential_model_instance.to_dict()
# create an instance of PatientAuthConfirmRequestCredentialModel from a dict
patient_auth_confirm_request_credential_model_from_dict = PatientAuthConfirmRequestCredentialModel.from_dict(patient_auth_confirm_request_credential_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


