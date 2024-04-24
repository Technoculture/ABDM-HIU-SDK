# ConsentArtefactResponseConsentConsentDetailModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_version** | **str** |  | [optional] 
**consent_id** | **str** |  | 
**created_at** | **datetime** |  | 
**patient** | [**ConsentManagerPatientIDModelModel**](ConsentManagerPatientIDModel.md) |  | 
**care_contexts** | [**List[ConsentArtefactResponseConsentConsentDetailCareContextsInnerModelModel]**](ConsentArtefactResponseConsentConsentDetailCareContextsInnerModel.md) |  | 
**purpose** | [**UsePurposeModelModel**](UsePurposeModel.md) |  | 
**hip** | [**ConsentArtefactResponseConsentConsentDetailHipModelModel**](ConsentArtefactResponseConsentConsentDetailHipModel.md) |  | 
**hiu** | [**ConsentArtefactResponseConsentConsentDetailHiuModelModel**](ConsentArtefactResponseConsentConsentDetailHiuModel.md) |  | 
**consent_manager** | [**ConsentArtefactResponseConsentConsentDetailConsentManagerModelModel**](ConsentArtefactResponseConsentConsentDetailConsentManagerModel.md) |  | 
**requester** | [**RequesterModelModel**](RequesterModel.md) |  | 
**hi_types** | [**List[HITypeEnumModelModel]**](HITypeEnumModel.md) |  | 
**permission** | [**PermissionModelModel**](PermissionModel.md) |  | 

## Example

```python
from abdm.abdm.model.consent_artefact_response_consent_consent_detail_model import ConsentArtefactResponseConsentConsentDetailModel

# TODO update the JSON string below
json = "{}"
# create an instance of ConsentArtefactResponseConsentConsentDetailModel from a JSON string
consent_artefact_response_consent_consent_detail_model_instance = ConsentArtefactResponseConsentConsentDetailModel.from_json(json)
# print the JSON string representation of the object
print(ConsentArtefactResponseConsentConsentDetailModel.to_json())

# convert the object into a dict
consent_artefact_response_consent_consent_detail_model_dict = consent_artefact_response_consent_consent_detail_model_instance.to_dict()
# create an instance of ConsentArtefactResponseConsentConsentDetailModel from a dict
consent_artefact_response_consent_consent_detail_model_from_dict = ConsentArtefactResponseConsentConsentDetailModel.from_dict(consent_artefact_response_consent_consent_detail_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


