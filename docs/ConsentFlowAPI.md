# abdm.ConsentFlowAPI

All URIs are relative to *https://dev.abdm.gov.in/gateway*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v05_consent_requests_on_init_post**](ConsentFlowAPI.md#v05_consent_requests_on_init_post) | **POST** /v0.5/consent-requests/on-init | Response to consent request
[**v05_consent_requests_on_status_post**](ConsentFlowAPI.md#v05_consent_requests_on_status_post) | **POST** /v0.5/consent-requests/on-status | Result of consent request status
[**v05_consents_hiu_notify_post**](ConsentFlowAPI.md#v05_consents_hiu_notify_post) | **POST** /v0.5/consents/hiu/notify | Consent notification
[**v05_consents_on_fetch_post**](ConsentFlowAPI.md#v05_consents_on_fetch_post) | **POST** /v0.5/consents/on-fetch | Result of fetch request for a consent artefact


# **v05_consent_requests_on_init_post**
> v05_consent_requests_on_init_post(authorization, x_hiu_id, consent_request_init_response_model)

Response to consent request

Result of consent request creation for a patient. **id** represents the consentrequest id created by CM. The result must contain either **id** or the **error** caused. <br/>   Reasons for error may be   * Invalid references (e.g patient id, hiu id), purpose, hiTypes, ranges, persmission 

### Example


```python
import abdm
from abdm.models.consent_request_init_response_model import ConsentRequestInitResponseModel
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
    api_instance = abdm.ConsentFlowAPI(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge.
    x_hiu_id = 'x_hiu_id_example' # str | Identifier of the health information user to which the request was intended.
    consent_request_init_response_model = abdm.ConsentRequestInitResponseModel() # ConsentRequestInitResponseModel | 

    try:
        # Response to consent request
        api_instance.v05_consent_requests_on_init_post(authorization, x_hiu_id, consent_request_init_response_model)
    except Exception as e:
        print("Exception when calling ConsentFlowAPI->v05_consent_requests_on_init_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge. | 
 **x_hiu_id** | **str**| Identifier of the health information user to which the request was intended. | 
 **consent_request_init_response_model** | [**ConsentRequestInitResponseModel**](ConsentRequestInitResponseModel.md)|  | 

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
**400** | **Causes:**   * Invalid data sent  |  -  |
**401** | **Causes:**   * Expired/Invalid token.  |  -  |
**500** | **Causes:**   * Downstream system(s) is down.   * Unhandled exceptions.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v05_consent_requests_on_status_post**
> v05_consent_requests_on_status_post(authorization, x_hiu_id, hiu_consent_request_status_model)

Result of consent request status

Result of consent request done previously. Status of request can be GRANTED,  DENIED, EXPIRED. If the request was GRANTED, then  

### Example


```python
import abdm
from abdm.models.hiu_consent_request_status_model import HIUConsentRequestStatusModel
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
    api_instance = abdm.ConsentFlowAPI(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge.
    x_hiu_id = 'x_hiu_id_example' # str | Identifier of the health information user to which the request was intended.
    hiu_consent_request_status_model = abdm.HIUConsentRequestStatusModel() # HIUConsentRequestStatusModel | 

    try:
        # Result of consent request status
        api_instance.v05_consent_requests_on_status_post(authorization, x_hiu_id, hiu_consent_request_status_model)
    except Exception as e:
        print("Exception when calling ConsentFlowAPI->v05_consent_requests_on_status_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge. | 
 **x_hiu_id** | **str**| Identifier of the health information user to which the request was intended. | 
 **hiu_consent_request_status_model** | [**HIUConsentRequestStatusModel**](HIUConsentRequestStatusModel.md)|  | 

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
**400** | **Causes:**   * Invalid data sent  |  -  |
**401** | **Causes:**   * Expired/Invalid token.  |  -  |
**500** | **Causes:**   * Downstream system(s) is down.   * Unhandled exceptions.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v05_consents_hiu_notify_post**
> v05_consents_hiu_notify_post(authorization, x_hiu_id, hiu_consent_notification_event_model)

Consent notification

Health information user will get notified about the consent request granted or denied, consent revoked, consent expired.  1. For consent request grant, status=GRANTED, consentRequestId=<consent-request-id>, and consentArtefacts is an array of generated consent artefact Ids. 2. For consent request expiry, status=EXPIRED, consentRequestId=<consent-request-id> 3. For consent request denied, status=DENIED, consentRequestId=<consent-request-id> 4. For consent revocation, status=REVOKED, consentArtefacts is an array of revoked consent artefact ids 

### Example


```python
import abdm
from abdm.models.hiu_consent_notification_event_model import HIUConsentNotificationEventModel
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
    api_instance = abdm.ConsentFlowAPI(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge.
    x_hiu_id = 'x_hiu_id_example' # str | Identifier of the health information user to which the request was intended.
    hiu_consent_notification_event_model = abdm.HIUConsentNotificationEventModel() # HIUConsentNotificationEventModel | 

    try:
        # Consent notification
        api_instance.v05_consents_hiu_notify_post(authorization, x_hiu_id, hiu_consent_notification_event_model)
    except Exception as e:
        print("Exception when calling ConsentFlowAPI->v05_consents_hiu_notify_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge. | 
 **x_hiu_id** | **str**| Identifier of the health information user to which the request was intended. | 
 **hiu_consent_notification_event_model** | [**HIUConsentNotificationEventModel**](HIUConsentNotificationEventModel.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Request Accepted. |  -  |
**401** | **Causes:**   * Invalid/Expired/Empty token.  |  -  |
**500** | **Causes:**   * Downstream services are down  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v05_consents_on_fetch_post**
> v05_consents_on_fetch_post(authorization, x_hiu_id, consent_artefact_response_model)

Result of fetch request for a consent artefact

Must contain either consent or error. Possible reason of errors are  1. consentId passed through /fetch is invalid 

### Example


```python
import abdm
from abdm.models.consent_artefact_response_model import ConsentArtefactResponseModel
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
    api_instance = abdm.ConsentFlowAPI(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge.
    x_hiu_id = 'x_hiu_id_example' # str | Identifier of the health information user to which the request was intended.
    consent_artefact_response_model = abdm.ConsentArtefactResponseModel() # ConsentArtefactResponseModel | 

    try:
        # Result of fetch request for a consent artefact
        api_instance.v05_consents_on_fetch_post(authorization, x_hiu_id, consent_artefact_response_model)
    except Exception as e:
        print("Exception when calling ConsentFlowAPI->v05_consents_on_fetch_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge. | 
 **x_hiu_id** | **str**| Identifier of the health information user to which the request was intended. | 
 **consent_artefact_response_model** | [**ConsentArtefactResponseModel**](ConsentArtefactResponseModel.md)|  | 

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
**400** | **Causes:**   * Invalid data sent  |  -  |
**401** | **Causes:**   * Expired/Invalid token.  |  -  |
**500** | **Causes:**   * Downstream system(s) is down.   * Unhandled exceptions.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

