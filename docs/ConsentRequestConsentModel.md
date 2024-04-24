# ConsentRequestConsentModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**purpose** | [**UsePurposeModelModel**](UsePurposeModel.md) |  | 
**patient** | [**ConsentRequestConsentPatientModelModel**](ConsentRequestConsentPatientModel.md) |  | 
**hip** | [**ConsentArtefactResponseConsentConsentDetailHipModelModel**](ConsentArtefactResponseConsentConsentDetailHipModel.md) |  | [optional] 
**care_contexts** | [**List[CareContextDefinitionModelModel]**](CareContextDefinitionModel.md) |  | [optional] 
**hiu** | [**ConsentArtefactResponseConsentConsentDetailHiuModelModel**](ConsentArtefactResponseConsentConsentDetailHiuModel.md) |  | 
**requester** | [**RequesterModelModel**](RequesterModel.md) |  | 
**hi_types** | [**List[HITypeEnumModelModel]**](HITypeEnumModel.md) |  | 
**permission** | [**PermissionModelModel**](PermissionModel.md) |  | 

## Example

```python
from abdm.abdm.model.consent_request_consent_model import ConsentRequestConsentModel

# TODO update the JSON string below
json = "{}"
# create an instance of ConsentRequestConsentModel from a JSON string
consent_request_consent_model_instance = ConsentRequestConsentModel.from_json(json)
# print the JSON string representation of the object
print(ConsentRequestConsentModel.to_json())

# convert the object into a dict
consent_request_consent_model_dict = consent_request_consent_model_instance.to_dict()
# create an instance of ConsentRequestConsentModel from a dict
consent_request_consent_model_from_dict = ConsentRequestConsentModel.from_dict(consent_request_consent_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


