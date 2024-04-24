# HIUConsentNotificationEventNotificationModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consent_request_id** | **str** |  | 
**status** | [**ConsentStatusModelModel**](ConsentStatusModel.md) |  | 
**consent_artefacts** | [**List[ConsentArtefactReferenceModelModel]**](ConsentArtefactReferenceModel.md) | if the status is GRANTED or REVOKED, then the consentArtefact references (Ids) must be specified. | [optional] 

## Example

```python
from abdm.abdm.model.hiu_consent_notification_event_notification_model import HIUConsentNotificationEventNotificationModel

# TODO update the JSON string below
json = "{}"
# create an instance of HIUConsentNotificationEventNotificationModel from a JSON string
hiu_consent_notification_event_notification_model_instance = HIUConsentNotificationEventNotificationModel.from_json(json)
# print the JSON string representation of the object
print(HIUConsentNotificationEventNotificationModel.to_json())

# convert the object into a dict
hiu_consent_notification_event_notification_model_dict = hiu_consent_notification_event_notification_model_instance.to_dict()
# create an instance of HIUConsentNotificationEventNotificationModel from a dict
hiu_consent_notification_event_notification_model_from_dict = HIUConsentNotificationEventNotificationModel.from_dict(hiu_consent_notification_event_notification_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


