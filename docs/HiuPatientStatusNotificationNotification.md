# HiuPatientStatusNotificationNotification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**patient** | [**HiuPatientStatusNotificationNotificationPatient**](HiuPatientStatusNotificationNotificationPatient.md) |  | 

## Example

```python
from abdm.models.hiu_patient_status_notification_notification import HiuPatientStatusNotificationNotification

# TODO update the JSON string below
json = "{}"
# create an instance of HiuPatientStatusNotificationNotification from a JSON string
hiu_patient_status_notification_notification_instance = HiuPatientStatusNotificationNotification.from_json(json)
# print the JSON string representation of the object
print(HiuPatientStatusNotificationNotification.to_json())

# convert the object into a dict
hiu_patient_status_notification_notification_dict = hiu_patient_status_notification_notification_instance.to_dict()
# create an instance of HiuPatientStatusNotificationNotification from a dict
hiu_patient_status_notification_notification_from_dict = HiuPatientStatusNotificationNotification.from_dict(hiu_patient_status_notification_notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


