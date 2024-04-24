# abdm.PatientNotificationAPI

All URIs are relative to *https://dev.abdm.gov.in/gateway*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v05_patients_status_notify_post**](PatientNotificationAPI.md#v05_patients_status_notify_post) | **POST** /v0.5/patients/status/notify | Notification sent by Consent Manager
[**v05_patients_status_on_notify_post**](PatientNotificationAPI.md#v05_patients_status_on_notify_post) | **POST** /v0.5/patients/status/on-notify | Acknowledgment by HIU


# **v05_patients_status_notify_post**
> v05_patients_status_notify_post(authorization, x_hiu_id, hiu_patient_status_notification_model)

Notification sent by Consent Manager

This API is to send patient's status (ACTIVE/DEACTIVATED/DELETED) to the HIU. 

### Example


```python
import abdm
from abdm.models.hiu_patient_status_notification_model import HiuPatientStatusNotificationModel
from abdm.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dev.abdm.gov.in/gateway
# See configuration.py for a list of all supported configuration parameters.
configuration = abdm.Configuration(
    host = "https://dev.abdm.gov.in/gateway"
)


# Enter a context with an instance of the API client
with abdm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = abdm.PatientNotificationAPI(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge.
    x_hiu_id = 'x_hiu_id_example' # str | Identifier of the health information user to which the request was intended.
    hiu_patient_status_notification_model = abdm.HiuPatientStatusNotificationModel() # HiuPatientStatusNotificationModel | 

    try:
        # Notification sent by Consent Manager
        api_instance.v05_patients_status_notify_post(authorization, x_hiu_id, hiu_patient_status_notification_model)
    except Exception as e:
        print("Exception when calling PatientNotificationAPI->v05_patients_status_notify_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge. | 
 **x_hiu_id** | **str**| Identifier of the health information user to which the request was intended. | 
 **hiu_patient_status_notification_model** | [**HiuPatientStatusNotificationModel**](HiuPatientStatusNotificationModel.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Request Accepted |  -  |
**500** | **Causes:**   * Downstream system(s) is down.   * Unhandled exceptions.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v05_patients_status_on_notify_post**
> v05_patients_status_on_notify_post(authorization, x_cm_id, patient_status_notification_model)

Acknowledgment by HIU

This  API is to check if the Status is successfully sent for patient (Active/Deactivate/DELETED) to HIU and then \"status\" will be \"OK\" with no error. 

### Example


```python
import abdm
from abdm.models.patient_status_notification_model import PatientStatusNotificationModel
from abdm.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dev.abdm.gov.in/gateway
# See configuration.py for a list of all supported configuration parameters.
configuration = abdm.Configuration(
    host = "https://dev.abdm.gov.in/gateway"
)


# Enter a context with an instance of the API client
with abdm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = abdm.PatientNotificationAPI(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge.
    x_cm_id = 'x_cm_id_example' # str | Suffix of the consent manager to which the request was intended.
    patient_status_notification_model = abdm.PatientStatusNotificationModel() # PatientStatusNotificationModel | 

    try:
        # Acknowledgment by HIU
        api_instance.v05_patients_status_on_notify_post(authorization, x_cm_id, patient_status_notification_model)
    except Exception as e:
        print("Exception when calling PatientNotificationAPI->v05_patients_status_on_notify_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge. | 
 **x_cm_id** | **str**| Suffix of the consent manager to which the request was intended. | 
 **patient_status_notification_model** | [**PatientStatusNotificationModel**](PatientStatusNotificationModel.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Request Accepted |  -  |
**500** | **Causes:**   * Downstream system(s) is down.   * Unhandled exceptions.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

