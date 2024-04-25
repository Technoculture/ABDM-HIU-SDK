# abdm.SubscriptionsApi

All URIs are relative to *https://dev.abdm.gov.in/gateway*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v05_subscription_requests_hiu_notify_post**](SubscriptionsApi.md#v05_subscription_requests_hiu_notify_post) | **POST** /v0.5/subscription-requests/hiu/notify | Notification for subscription grant/deny/revoke
[**v05_subscription_requests_hiu_on_init_post**](SubscriptionsApi.md#v05_subscription_requests_hiu_on_init_post) | **POST** /v0.5/subscription-requests/hiu/on-init | callback API for the /subscription-requests/cm/init to notify a HIU on acceptance/acknowledgement of the request for subscription.
[**v05_subscriptions_hiu_notify_post**](SubscriptionsApi.md#v05_subscriptions_hiu_notify_post) | **POST** /v0.5/subscriptions/hiu/notify | Notification to HIU on basis of a granted subscription


# **v05_subscription_requests_hiu_notify_post**
> v05_subscription_requests_hiu_notify_post(authorization, x_hiu_id, subscription_approval_notification)

Notification for subscription grant/deny/revoke

This API is used by CM to notify a HIU to grant or deny a request for subscription, and also to notify that in case an existing subscription is revoked or expired. For notifying that a particular subscription request was GRANTED or DENIED, the **subscriptionRequestId** is passed.  

### Example


```python
import abdm
from abdm.models.subscription_approval_notification import SubscriptionApprovalNotification
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
    api_instance = abdm.SubscriptionsApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge.
    x_hiu_id = 'x_hiu_id_example' # str | Identifier of the health information user to which the request was intended.
    subscription_approval_notification = abdm.SubscriptionApprovalNotification() # SubscriptionApprovalNotification | 

    try:
        # Notification for subscription grant/deny/revoke
        api_instance.v05_subscription_requests_hiu_notify_post(authorization, x_hiu_id, subscription_approval_notification)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->v05_subscription_requests_hiu_notify_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge. | 
 **x_hiu_id** | **str**| Identifier of the health information user to which the request was intended. | 
 **subscription_approval_notification** | [**SubscriptionApprovalNotification**](SubscriptionApprovalNotification.md)|  | 

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
**400** | **Causes:**   * Invalid data sent    * Required attributes not mentioned  |  -  |
**401** | **Causes:**   * Expired/Invalid token.  |  -  |
**500** | **Causes:**   * Downstream system(s) is down.   * Unhandled exceptions.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v05_subscription_requests_hiu_on_init_post**
> v05_subscription_requests_hiu_on_init_post(authorization, x_hiu_id, hiu_subscription_request_receipt)

callback API for the /subscription-requests/cm/init to notify a HIU on acceptance/acknowledgement of the request for subscription.

This callback API acknowledges the request for subscription from a HIU, and sends back a \"id\" that will be used when the patient/user approves or denies the subscription.  

### Example


```python
import abdm
from abdm.models.hiu_subscription_request_receipt import HIUSubscriptionRequestReceipt
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
    api_instance = abdm.SubscriptionsApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge.
    x_hiu_id = 'x_hiu_id_example' # str | Identifier of the health information user to which the request was intended.
    hiu_subscription_request_receipt = abdm.HIUSubscriptionRequestReceipt() # HIUSubscriptionRequestReceipt | 

    try:
        # callback API for the /subscription-requests/cm/init to notify a HIU on acceptance/acknowledgement of the request for subscription.
        api_instance.v05_subscription_requests_hiu_on_init_post(authorization, x_hiu_id, hiu_subscription_request_receipt)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->v05_subscription_requests_hiu_on_init_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge. | 
 **x_hiu_id** | **str**| Identifier of the health information user to which the request was intended. | 
 **hiu_subscription_request_receipt** | [**HIUSubscriptionRequestReceipt**](HIUSubscriptionRequestReceipt.md)|  | 

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

# **v05_subscriptions_hiu_notify_post**
> v05_subscriptions_hiu_notify_post(authorization, x_hiu_id, hiu_subscription_notification)

Notification to HIU on basis of a granted subscription

This API is used by CM to notify a HIU for notification relevant to subscription. Notifications are sent to subscribed HIUs whenever a new care-context is linked or new data is available on an existing linked care-context.  1. if event.category = LINK, then only care-contexts are passed when new care-contexts are linked for patient.  2. If event.category = DATA, then hiTypes are passed. Care-context is passed only if the subscribed HIU has any valid consent for that care-context 

### Example


```python
import abdm
from abdm.models.hiu_subscription_notification import HIUSubscriptionNotification
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
    api_instance = abdm.SubscriptionsApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge.
    x_hiu_id = 'x_hiu_id_example' # str | Identifier of the health information user to which the request was intended.
    hiu_subscription_notification = abdm.HIUSubscriptionNotification() # HIUSubscriptionNotification | 

    try:
        # Notification to HIU on basis of a granted subscription
        api_instance.v05_subscriptions_hiu_notify_post(authorization, x_hiu_id, hiu_subscription_notification)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->v05_subscriptions_hiu_notify_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge. | 
 **x_hiu_id** | **str**| Identifier of the health information user to which the request was intended. | 
 **hiu_subscription_notification** | [**HIUSubscriptionNotification**](HIUSubscriptionNotification.md)|  | 

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
**400** | **Causes:**   * Invalid data sent    * Required attributes not mentioned  |  -  |
**401** | **Causes:**   * Expired/Invalid token.  |  -  |
**500** | **Causes:**   * Downstream system(s) is down.   * Unhandled exceptions.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

