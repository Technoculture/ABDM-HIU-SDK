# PatientStatusNotificationModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | a nonce, unique for each HTTP request | 
**timestamp** | **datetime** | Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ | 
**acknowledgment** | [**PatientAuthNotificationAcknowledgementAcknowledgementModelModel**](PatientAuthNotificationAcknowledgementAcknowledgementModel.md) |  | 
**error** | [**ErrorModelModel**](ErrorModel.md) |  | [optional] 
**resp** | [**RequestReferenceModelModel**](RequestReferenceModel.md) |  | [optional] 

## Example

```python
from abdm.abdm.model.patient_status_notification_model import PatientStatusNotificationModel

# TODO update the JSON string below
json = "{}"
# create an instance of PatientStatusNotificationModel from a JSON string
patient_status_notification_model_instance = PatientStatusNotificationModel.from_json(json)
# print the JSON string representation of the object
print(PatientStatusNotificationModel.to_json())

# convert the object into a dict
patient_status_notification_model_dict = patient_status_notification_model_instance.to_dict()
# create an instance of PatientStatusNotificationModel from a dict
patient_status_notification_model_from_dict = PatientStatusNotificationModel.from_dict(patient_status_notification_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


