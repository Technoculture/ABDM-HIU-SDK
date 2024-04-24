# PatientAuthNotificationModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | a nonce, unique for each HTTP request | 
**timestamp** | **datetime** | Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ | 
**auth** | [**PatientAuthNotificationAuthModelModel**](PatientAuthNotificationAuthModel.md) |  | [optional] 

## Example

```python
from abdm.abdm.model.patient_auth_notification_model import PatientAuthNotificationModel

# TODO update the JSON string below
json = "{}"
# create an instance of PatientAuthNotificationModel from a JSON string
patient_auth_notification_model_instance = PatientAuthNotificationModel.from_json(json)
# print the JSON string representation of the object
print(PatientAuthNotificationModel.to_json())

# convert the object into a dict
patient_auth_notification_model_dict = patient_auth_notification_model_instance.to_dict()
# create an instance of PatientAuthNotificationModel from a dict
patient_auth_notification_model_from_dict = PatientAuthNotificationModel.from_dict(patient_auth_notification_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


