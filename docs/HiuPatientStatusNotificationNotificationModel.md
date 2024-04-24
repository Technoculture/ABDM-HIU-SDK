# HiuPatientStatusNotificationNotificationModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**patient** | [**HiuPatientStatusNotificationNotificationPatientModelModel**](HiuPatientStatusNotificationNotificationPatientModel.md) |  | 

## Example

```python
from abdm.abdm.model.hiu_patient_status_notification_notification_model import HiuPatientStatusNotificationNotificationModel

# TODO update the JSON string below
json = "{}"
# create an instance of HiuPatientStatusNotificationNotificationModel from a JSON string
hiu_patient_status_notification_notification_model_instance = HiuPatientStatusNotificationNotificationModel.from_json(json)
# print the JSON string representation of the object
print(HiuPatientStatusNotificationNotificationModel.to_json())

# convert the object into a dict
hiu_patient_status_notification_notification_model_dict = hiu_patient_status_notification_notification_model_instance.to_dict()
# create an instance of HiuPatientStatusNotificationNotificationModel from a dict
hiu_patient_status_notification_notification_model_from_dict = HiuPatientStatusNotificationNotificationModel.from_dict(hiu_patient_status_notification_notification_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


