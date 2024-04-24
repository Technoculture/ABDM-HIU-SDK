# ConsentArtefactResponseConsentModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**ConsentStatusModelModel**](ConsentStatusModel.md) |  | 
**consent_detail** | [**ConsentArtefactResponseConsentConsentDetailModelModel**](ConsentArtefactResponseConsentConsentDetailModel.md) |  | 
**signature** | **str** |  | 

## Example

```python
from abdm.abdm.model.consent_artefact_response_consent_model import ConsentArtefactResponseConsentModel

# TODO update the JSON string below
json = "{}"
# create an instance of ConsentArtefactResponseConsentModel from a JSON string
consent_artefact_response_consent_model_instance = ConsentArtefactResponseConsentModel.from_json(json)
# print the JSON string representation of the object
print(ConsentArtefactResponseConsentModel.to_json())

# convert the object into a dict
consent_artefact_response_consent_model_dict = consent_artefact_response_consent_model_instance.to_dict()
# create an instance of ConsentArtefactResponseConsentModel from a dict
consent_artefact_response_consent_model_from_dict = ConsentArtefactResponseConsentModel.from_dict(consent_artefact_response_consent_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


