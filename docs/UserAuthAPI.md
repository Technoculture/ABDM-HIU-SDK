# abdm.UserAuthAPI

All URIs are relative to *https://dev.abdm.gov.in/gateway*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v05_users_auth_notify_post**](UserAuthAPI.md#v05_users_auth_notify_post) | **POST** /v0.5/users/auth/notify | notification API in case of DIRECT mode of authentication by the CM
[**v05_users_auth_on_confirm_post**](UserAuthAPI.md#v05_users_auth_on_confirm_post) | **POST** /v0.5/users/auth/on-confirm | callback API for /auth/confirm (in case of MEDIATED auth) to confirm user authentication or not
[**v05_users_auth_on_fetch_modes_post**](UserAuthAPI.md#v05_users_auth_on_fetch_modes_post) | **POST** /v0.5/users/auth/on-fetch-modes | Identification result for a consent-manager user-id
[**v05_users_auth_on_init_post**](UserAuthAPI.md#v05_users_auth_on_init_post) | **POST** /v0.5/users/auth/on-init | Response to user authentication initialization from HIP


# **v05_users_auth_notify_post**
> v05_users_auth_notify_post(authorization, x_hip_id, x_hiu_id, patient_auth_notification_model)

notification API in case of DIRECT mode of authentication by the CM

This API is called by CM to confirm authentication of users. The transactionId returned is same as that passed in /auth/on-init. The \"auth.status\" conveys whether the request was GRANTED or DENIED.    1. **auth.accessToken** - is specific to the purpose mentioned in the /auth/init. This token needs to be used for initiating the intended action. For example for HIP initiated linking of care-contexts   2. **NOTE**, only one of **X-HIP-ID** or **X-HIU-ID** will be sent as part of header, not both.   3. The payload is conditional to the purpose of auth. If purpose specified in /auth/init is KYC or KYC_AND_LINK, then patient details are passed. **auth.accessToken** is passed only if the purpose is LINK or KYC_AND_LINK. 

### Example


```python
import abdm
from abdm.models.patient_auth_notification_model import PatientAuthNotificationModel
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
    api_instance = abdm.UserAuthAPI(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge.
    x_hip_id = 'x_hip_id_example' # str | Identifier of the health information provider to which the request was intended.
    x_hiu_id = 'x_hiu_id_example' # str | Identifier of the health information user to which the request was intended.
    patient_auth_notification_model = abdm.PatientAuthNotificationModel() # PatientAuthNotificationModel | 

    try:
        # notification API in case of DIRECT mode of authentication by the CM
        api_instance.v05_users_auth_notify_post(authorization, x_hip_id, x_hiu_id, patient_auth_notification_model)
    except Exception as e:
        print("Exception when calling UserAuthAPI->v05_users_auth_notify_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge. | 
 **x_hip_id** | **str**| Identifier of the health information provider to which the request was intended. | 
 **x_hiu_id** | **str**| Identifier of the health information user to which the request was intended. | 
 **patient_auth_notification_model** | [**PatientAuthNotificationModel**](PatientAuthNotificationModel.md)|  | 

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
**202** | Request accepted |  -  |
**400** | **Causes:**   * required details not provided   * neither auth nor error specified   |  -  |
**401** | **Causes:**   * Unauthorized request  |  -  |
**500** | **Causes:**   * Downstream system(s) is down.   * Unhandled exceptions.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v05_users_auth_on_confirm_post**
> v05_users_auth_on_confirm_post(authorization, x_hip_id, x_hiu_id, patient_auth_confirm_response_model)

callback API for /auth/confirm (in case of MEDIATED auth) to confirm user authentication or not

This API is called by CM to confirm authentication of users.    1. **auth.accessToken** - is specific to the purpose mentioned in the /auth/init. This token needs to be used for initiating the intended action. For example for HIP initiated linking of care-contexts   2. **NOTE**, only one of **X-HIP-ID** or **X-HIU-ID** will be sent as part of header, not both.      

### Example


```python
import abdm
from abdm.models.patient_auth_confirm_response_model import PatientAuthConfirmResponseModel
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
    api_instance = abdm.UserAuthAPI(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge.
    x_hip_id = 'x_hip_id_example' # str | Identifier of the health information provider to which the request was intended.
    x_hiu_id = 'x_hiu_id_example' # str | Identifier of the health information user to which the request was intended.
    patient_auth_confirm_response_model = abdm.PatientAuthConfirmResponseModel() # PatientAuthConfirmResponseModel | 

    try:
        # callback API for /auth/confirm (in case of MEDIATED auth) to confirm user authentication or not
        api_instance.v05_users_auth_on_confirm_post(authorization, x_hip_id, x_hiu_id, patient_auth_confirm_response_model)
    except Exception as e:
        print("Exception when calling UserAuthAPI->v05_users_auth_on_confirm_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge. | 
 **x_hip_id** | **str**| Identifier of the health information provider to which the request was intended. | 
 **x_hiu_id** | **str**| Identifier of the health information user to which the request was intended. | 
 **patient_auth_confirm_response_model** | [**PatientAuthConfirmResponseModel**](PatientAuthConfirmResponseModel.md)|  | 

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
**202** | Request accepted |  -  |
**400** | **Causes:**   * required details not provided   * neither auth nor error specified   |  -  |
**401** | **Causes:**   * Unauthorized request  |  -  |
**500** | **Causes:**   * Downstream system(s) is down.   * Unhandled exceptions.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v05_users_auth_on_fetch_modes_post**
> v05_users_auth_on_fetch_modes_post(authorization, x_hip_id, x_hiu_id, patient_auth_mode_query_response_model)

Identification result for a consent-manager user-id

If a patient is found then **auth** attribute contains the supported modes for the specified purpose.  Otherwise, error is raised for invalid requests or for non-existent id. Note in addition to the \"Authorization\" header, one of the following headers must be specified 1. **X-HIU-ID** if the requester is HIU (identified from /auth/fetch-modes requester.id) 2. **X-HIP-ID** if the requester is HIP (identified from /auth/fetch-modes requester.id) 

### Example


```python
import abdm
from abdm.models.patient_auth_mode_query_response_model import PatientAuthModeQueryResponseModel
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
    api_instance = abdm.UserAuthAPI(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge.
    x_hip_id = 'x_hip_id_example' # str | Identifier of the health information provider to which the request was intended.
    x_hiu_id = 'x_hiu_id_example' # str | Identifier of the health information user to which the request was intended.
    patient_auth_mode_query_response_model = abdm.PatientAuthModeQueryResponseModel() # PatientAuthModeQueryResponseModel | 

    try:
        # Identification result for a consent-manager user-id
        api_instance.v05_users_auth_on_fetch_modes_post(authorization, x_hip_id, x_hiu_id, patient_auth_mode_query_response_model)
    except Exception as e:
        print("Exception when calling UserAuthAPI->v05_users_auth_on_fetch_modes_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge. | 
 **x_hip_id** | **str**| Identifier of the health information provider to which the request was intended. | 
 **x_hiu_id** | **str**| Identifier of the health information user to which the request was intended. | 
 **patient_auth_mode_query_response_model** | [**PatientAuthModeQueryResponseModel**](PatientAuthModeQueryResponseModel.md)|  | 

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
**400** | Invalid request, required attributes not provided  |  -  |
**401** | **Causes:**   * Unauthorized request  |  -  |
**500** | **Causes:**   * Downstream system(s) is down.   * Unhandled exceptions.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v05_users_auth_on_init_post**
> v05_users_auth_on_init_post(authorization, x_hip_id, x_hiu_id, patient_auth_init_response_model)

Response to user authentication initialization from HIP

If the patient's id is valid, CM will return a transactionId as initialization of user auth. If the request is valid, then 'auth.mode' will convey how the authentication should be done. The authentication can be *mediated* or *direct*. For mediated authentication modes, HIP or HIU is epected to send over relevant code (OTP/token) or demographic info via subsequent API call to /auth/confirm. for direct authentication case, CM will notify requester through/users/auth/notify API.     1. **auth.mode** conveys whats the mode of authentication is, and what is expected from HIP/HIU in the subsequent /auth/confirm API call. Possible values        1. MOBILE_OTP - auth via OTP to registered mobile. Mediated.        2. AADHAAR_OTP - auth initiated with Aadhaar with OTP. Mediated.        3. DEMOGRAPHICS - auth initiated with demographic verification       4. DIRECT - for authentication directly with the patient. e.g. Mobile App, SMS. In this case, the HIP/HIU is not expected to call subsequent /auth/confirm call. CM will do direct authentication with the User (e.g. Mobile App, SMS etc) and will notify requester   2. **meta.expiry** conveys the expiry time of the token and the authentication session   3. **NOTE**, only one of **X-HIP-ID** or **X-HIU-ID** will be sent as part of header, not both.    4. **NOTE**, only KYC purpose is applicable for HIU    The error section in the body, represents the potential errors that may have occurred. Possible reasons:   1. Patient id is invalid 

### Example


```python
import abdm
from abdm.models.patient_auth_init_response_model import PatientAuthInitResponseModel
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
    api_instance = abdm.UserAuthAPI(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge.
    x_hip_id = 'x_hip_id_example' # str | Identifier of the health information provider to which the request was intended.
    x_hiu_id = 'x_hiu_id_example' # str | Identifier of the health information user to which the request was intended.
    patient_auth_init_response_model = abdm.PatientAuthInitResponseModel() # PatientAuthInitResponseModel | 

    try:
        # Response to user authentication initialization from HIP
        api_instance.v05_users_auth_on_init_post(authorization, x_hip_id, x_hiu_id, patient_auth_init_response_model)
    except Exception as e:
        print("Exception when calling UserAuthAPI->v05_users_auth_on_init_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge. | 
 **x_hip_id** | **str**| Identifier of the health information provider to which the request was intended. | 
 **x_hiu_id** | **str**| Identifier of the health information user to which the request was intended. | 
 **patient_auth_init_response_model** | [**PatientAuthInitResponseModel**](PatientAuthInitResponseModel.md)|  | 

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
**202** | Request accepted |  -  |
**400** | **Causes:**   * required information not provided   * neither authInit nor error specified   |  -  |
**401** | **Causes:**   * Unauthorized request  |  -  |
**500** | **Causes:**   * Downstream system(s) is down.   * Unhandled exceptions.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

