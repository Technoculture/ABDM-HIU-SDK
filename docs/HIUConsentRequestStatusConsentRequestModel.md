# HIUConsentRequestStatusConsentRequestModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**status** | [**ConsentStatusModelModel**](ConsentStatusModel.md) |  | 
**consent_artefacts** | [**List[ConsentArtefactReferenceModelModel]**](ConsentArtefactReferenceModel.md) |  | 

## Example

```python
from abdm.abdm.model.hiu_consent_request_status_consent_request_model import HIUConsentRequestStatusConsentRequestModel

# TODO update the JSON string below
json = "{}"
# create an instance of HIUConsentRequestStatusConsentRequestModel from a JSON string
hiu_consent_request_status_consent_request_model_instance = HIUConsentRequestStatusConsentRequestModel.from_json(json)
# print the JSON string representation of the object
print(HIUConsentRequestStatusConsentRequestModel.to_json())

# convert the object into a dict
hiu_consent_request_status_consent_request_model_dict = hiu_consent_request_status_consent_request_model_instance.to_dict()
# create an instance of HIUConsentRequestStatusConsentRequestModel from a dict
hiu_consent_request_status_consent_request_model_from_dict = HIUConsentRequestStatusConsentRequestModel.from_dict(hiu_consent_request_status_consent_request_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


