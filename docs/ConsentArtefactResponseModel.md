# ConsentArtefactResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | a nonce, unique for each HTTP request | 
**timestamp** | **datetime** | Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ | 
**consent** | [**ConsentArtefactResponseConsentModelModel**](ConsentArtefactResponseConsentModel.md) |  | [optional] 
**error** | [**ErrorModelModel**](ErrorModel.md) |  | [optional] 
**resp** | [**RequestReferenceModelModel**](RequestReferenceModel.md) |  | 

## Example

```python
from abdm.abdm.model.consent_artefact_response_model import ConsentArtefactResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of ConsentArtefactResponseModel from a JSON string
consent_artefact_response_model_instance = ConsentArtefactResponseModel.from_json(json)
# print the JSON string representation of the object
print(ConsentArtefactResponseModel.to_json())

# convert the object into a dict
consent_artefact_response_model_dict = consent_artefact_response_model_instance.to_dict()
# create an instance of ConsentArtefactResponseModel from a dict
consent_artefact_response_model_from_dict = ConsentArtefactResponseModel.from_dict(consent_artefact_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


