# HiuPatientStatusNotification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | a nonce, unique for each HTTP request | 
**timestamp** | **datetime** | Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ | 
**notification** | [**HiuPatientStatusNotificationNotification**](HiuPatientStatusNotificationNotification.md) |  | 

## Example

```python
from abdm.models.hiu_patient_status_notification import HiuPatientStatusNotification

# TODO update the JSON string below
json = "{}"
# create an instance of HiuPatientStatusNotification from a JSON string
hiu_patient_status_notification_instance = HiuPatientStatusNotification.from_json(json)
# print the JSON string representation of the object
print(HiuPatientStatusNotification.to_json())

# convert the object into a dict
hiu_patient_status_notification_dict = hiu_patient_status_notification_instance.to_dict()
# create an instance of HiuPatientStatusNotification from a dict
hiu_patient_status_notification_from_dict = HiuPatientStatusNotification.from_dict(hiu_patient_status_notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


