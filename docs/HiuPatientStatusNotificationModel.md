# HiuPatientStatusNotificationModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | a nonce, unique for each HTTP request | 
**timestamp** | **datetime** | Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ | 
**notification** | [**HiuPatientStatusNotificationNotificationModelModel**](HiuPatientStatusNotificationNotificationModel.md) |  | 

## Example

```python
from abdm.abdm.model.hiu_patient_status_notification_model import HiuPatientStatusNotificationModel

# TODO update the JSON string below
json = "{}"
# create an instance of HiuPatientStatusNotificationModel from a JSON string
hiu_patient_status_notification_model_instance = HiuPatientStatusNotificationModel.from_json(json)
# print the JSON string representation of the object
print(HiuPatientStatusNotificationModel.to_json())

# convert the object into a dict
hiu_patient_status_notification_model_dict = hiu_patient_status_notification_model_instance.to_dict()
# create an instance of HiuPatientStatusNotificationModel from a dict
hiu_patient_status_notification_model_from_dict = HiuPatientStatusNotificationModel.from_dict(hiu_patient_status_notification_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


