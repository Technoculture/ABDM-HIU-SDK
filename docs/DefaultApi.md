# openapi_client.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_notify_v05_users_auth_notify_post**](DefaultApi.md#auth_notify_v05_users_auth_notify_post) | **POST** /v0.5/users/auth/notify | Auth Notify
[**confirm_auth_v05_users_auth_confirm_post**](DefaultApi.md#confirm_auth_v05_users_auth_confirm_post) | **POST** /v0.5/users/auth/confirm | Confirm Auth
[**consent_hiu_notify_v05_consents_hiu_notify_post**](DefaultApi.md#consent_hiu_notify_v05_consents_hiu_notify_post) | **POST** /v0.5/consents/hiu/notify | Consent Hiu Notify
[**fetch_auth_modes_v05_users_auth_fetch_modes_post**](DefaultApi.md#fetch_auth_modes_v05_users_auth_fetch_modes_post) | **POST** /v0.5/users/auth/fetch-modes | Fetch Auth Modes
[**fetch_consent_artefact_v05_consents_on_fetch_post**](DefaultApi.md#fetch_consent_artefact_v05_consents_on_fetch_post) | **POST** /v0.5/consents/on-fetch | Fetch Consent Artefact
[**health_info_hiu_request_v05_health_information_hiu_on_request_post**](DefaultApi.md#health_info_hiu_request_v05_health_information_hiu_on_request_post) | **POST** /v0.5/health-information/hiu/on-request | Health Info Hiu Request
[**health_info_transfer_v05_health_information_transfer_post**](DefaultApi.md#health_info_transfer_v05_health_information_transfer_post) | **POST** /v0.5/health-information/transfer | Health Info Transfer
[**heartbeat_v05_heartbeat_get**](DefaultApi.md#heartbeat_v05_heartbeat_get) | **GET** /v0.5/heartbeat | Heartbeat
[**init_auth_v05_users_auth_init_post**](DefaultApi.md#init_auth_v05_users_auth_init_post) | **POST** /v0.5/users/auth/init | Init Auth
[**init_consent_request_v05_consent_requests_init_post**](DefaultApi.md#init_consent_request_v05_consent_requests_init_post) | **POST** /v0.5/consent-requests/init | Init Consent Request
[**on_confirm_auth_v05_users_auth_on_confirm_post**](DefaultApi.md#on_confirm_auth_v05_users_auth_on_confirm_post) | **POST** /v0.5/users/auth/on-confirm | On Confirm Auth
[**on_consent_request_status_v05_consent_requests_on_status_post**](DefaultApi.md#on_consent_request_status_v05_consent_requests_on_status_post) | **POST** /v0.5/consent-requests/on-status | On Consent Request Status
[**on_fetch_modes_v05_users_auth_on_fetch_modes_post**](DefaultApi.md#on_fetch_modes_v05_users_auth_on_fetch_modes_post) | **POST** /v0.5/users/auth/on-fetch-modes | On Fetch Modes
[**on_find_patient_v05_patients_on_find_post**](DefaultApi.md#on_find_patient_v05_patients_on_find_post) | **POST** /v0.5/patients/on-find | On Find Patient
[**on_init_auth_v05_users_auth_on_init_post**](DefaultApi.md#on_init_auth_v05_users_auth_on_init_post) | **POST** /v0.5/users/auth/on-init | On Init Auth
[**on_init_consent_request_v05_consent_requests_on_init_post**](DefaultApi.md#on_init_consent_request_v05_consent_requests_on_init_post) | **POST** /v0.5/consent-requests/on-init | On Init Consent Request
[**on_init_subscription_v05_subscription_requests_hiu_on_init_post**](DefaultApi.md#on_init_subscription_v05_subscription_requests_hiu_on_init_post) | **POST** /v0.5/subscription-requests/hiu/on-init | On Init Subscription
[**patient_status_notify_v05_patients_status_notify_post**](DefaultApi.md#patient_status_notify_v05_patients_status_notify_post) | **POST** /v0.5/patients/status/notify | Patient Status Notify
[**patient_status_on_notify_v05_patients_status_on_notify_post**](DefaultApi.md#patient_status_on_notify_v05_patients_status_on_notify_post) | **POST** /v0.5/patients/status/on-notify | Patient Status On Notify
[**subscription_hiu_notify_v05_subscriptions_hiu_notify_post**](DefaultApi.md#subscription_hiu_notify_v05_subscriptions_hiu_notify_post) | **POST** /v0.5/subscriptions/hiu/notify | Subscription Hiu Notify
[**subscription_notify_v05_subscription_requests_hiu_notify_post**](DefaultApi.md#subscription_notify_v05_subscription_requests_hiu_notify_post) | **POST** /v0.5/subscription-requests/hiu/notify | Subscription Notify


# **auth_notify_v05_users_auth_notify_post**
> object auth_notify_v05_users_auth_notify_post()

Auth Notify

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # Auth Notify
        api_response = api_instance.auth_notify_v05_users_auth_notify_post()
        print("The response of DefaultApi->auth_notify_v05_users_auth_notify_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->auth_notify_v05_users_auth_notify_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **confirm_auth_v05_users_auth_confirm_post**
> object confirm_auth_v05_users_auth_confirm_post()

Confirm Auth

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # Confirm Auth
        api_response = api_instance.confirm_auth_v05_users_auth_confirm_post()
        print("The response of DefaultApi->confirm_auth_v05_users_auth_confirm_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->confirm_auth_v05_users_auth_confirm_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **consent_hiu_notify_v05_consents_hiu_notify_post**
> object consent_hiu_notify_v05_consents_hiu_notify_post()

Consent Hiu Notify

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # Consent Hiu Notify
        api_response = api_instance.consent_hiu_notify_v05_consents_hiu_notify_post()
        print("The response of DefaultApi->consent_hiu_notify_v05_consents_hiu_notify_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->consent_hiu_notify_v05_consents_hiu_notify_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_auth_modes_v05_users_auth_fetch_modes_post**
> object fetch_auth_modes_v05_users_auth_fetch_modes_post()

Fetch Auth Modes

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # Fetch Auth Modes
        api_response = api_instance.fetch_auth_modes_v05_users_auth_fetch_modes_post()
        print("The response of DefaultApi->fetch_auth_modes_v05_users_auth_fetch_modes_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->fetch_auth_modes_v05_users_auth_fetch_modes_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_consent_artefact_v05_consents_on_fetch_post**
> object fetch_consent_artefact_v05_consents_on_fetch_post()

Fetch Consent Artefact

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # Fetch Consent Artefact
        api_response = api_instance.fetch_consent_artefact_v05_consents_on_fetch_post()
        print("The response of DefaultApi->fetch_consent_artefact_v05_consents_on_fetch_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->fetch_consent_artefact_v05_consents_on_fetch_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **health_info_hiu_request_v05_health_information_hiu_on_request_post**
> object health_info_hiu_request_v05_health_information_hiu_on_request_post()

Health Info Hiu Request

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # Health Info Hiu Request
        api_response = api_instance.health_info_hiu_request_v05_health_information_hiu_on_request_post()
        print("The response of DefaultApi->health_info_hiu_request_v05_health_information_hiu_on_request_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->health_info_hiu_request_v05_health_information_hiu_on_request_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **health_info_transfer_v05_health_information_transfer_post**
> object health_info_transfer_v05_health_information_transfer_post()

Health Info Transfer

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # Health Info Transfer
        api_response = api_instance.health_info_transfer_v05_health_information_transfer_post()
        print("The response of DefaultApi->health_info_transfer_v05_health_information_transfer_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->health_info_transfer_v05_health_information_transfer_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **heartbeat_v05_heartbeat_get**
> object heartbeat_v05_heartbeat_get()

Heartbeat

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # Heartbeat
        api_response = api_instance.heartbeat_v05_heartbeat_get()
        print("The response of DefaultApi->heartbeat_v05_heartbeat_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->heartbeat_v05_heartbeat_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **init_auth_v05_users_auth_init_post**
> object init_auth_v05_users_auth_init_post()

Init Auth

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # Init Auth
        api_response = api_instance.init_auth_v05_users_auth_init_post()
        print("The response of DefaultApi->init_auth_v05_users_auth_init_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->init_auth_v05_users_auth_init_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **init_consent_request_v05_consent_requests_init_post**
> object init_consent_request_v05_consent_requests_init_post()

Init Consent Request

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # Init Consent Request
        api_response = api_instance.init_consent_request_v05_consent_requests_init_post()
        print("The response of DefaultApi->init_consent_request_v05_consent_requests_init_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->init_consent_request_v05_consent_requests_init_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **on_confirm_auth_v05_users_auth_on_confirm_post**
> object on_confirm_auth_v05_users_auth_on_confirm_post()

On Confirm Auth

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # On Confirm Auth
        api_response = api_instance.on_confirm_auth_v05_users_auth_on_confirm_post()
        print("The response of DefaultApi->on_confirm_auth_v05_users_auth_on_confirm_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->on_confirm_auth_v05_users_auth_on_confirm_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **on_consent_request_status_v05_consent_requests_on_status_post**
> object on_consent_request_status_v05_consent_requests_on_status_post()

On Consent Request Status

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # On Consent Request Status
        api_response = api_instance.on_consent_request_status_v05_consent_requests_on_status_post()
        print("The response of DefaultApi->on_consent_request_status_v05_consent_requests_on_status_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->on_consent_request_status_v05_consent_requests_on_status_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **on_fetch_modes_v05_users_auth_on_fetch_modes_post**
> object on_fetch_modes_v05_users_auth_on_fetch_modes_post()

On Fetch Modes

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # On Fetch Modes
        api_response = api_instance.on_fetch_modes_v05_users_auth_on_fetch_modes_post()
        print("The response of DefaultApi->on_fetch_modes_v05_users_auth_on_fetch_modes_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->on_fetch_modes_v05_users_auth_on_fetch_modes_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **on_find_patient_v05_patients_on_find_post**
> object on_find_patient_v05_patients_on_find_post()

On Find Patient

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # On Find Patient
        api_response = api_instance.on_find_patient_v05_patients_on_find_post()
        print("The response of DefaultApi->on_find_patient_v05_patients_on_find_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->on_find_patient_v05_patients_on_find_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **on_init_auth_v05_users_auth_on_init_post**
> object on_init_auth_v05_users_auth_on_init_post()

On Init Auth

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # On Init Auth
        api_response = api_instance.on_init_auth_v05_users_auth_on_init_post()
        print("The response of DefaultApi->on_init_auth_v05_users_auth_on_init_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->on_init_auth_v05_users_auth_on_init_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **on_init_consent_request_v05_consent_requests_on_init_post**
> object on_init_consent_request_v05_consent_requests_on_init_post()

On Init Consent Request

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # On Init Consent Request
        api_response = api_instance.on_init_consent_request_v05_consent_requests_on_init_post()
        print("The response of DefaultApi->on_init_consent_request_v05_consent_requests_on_init_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->on_init_consent_request_v05_consent_requests_on_init_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **on_init_subscription_v05_subscription_requests_hiu_on_init_post**
> object on_init_subscription_v05_subscription_requests_hiu_on_init_post()

On Init Subscription

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # On Init Subscription
        api_response = api_instance.on_init_subscription_v05_subscription_requests_hiu_on_init_post()
        print("The response of DefaultApi->on_init_subscription_v05_subscription_requests_hiu_on_init_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->on_init_subscription_v05_subscription_requests_hiu_on_init_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patient_status_notify_v05_patients_status_notify_post**
> object patient_status_notify_v05_patients_status_notify_post()

Patient Status Notify

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # Patient Status Notify
        api_response = api_instance.patient_status_notify_v05_patients_status_notify_post()
        print("The response of DefaultApi->patient_status_notify_v05_patients_status_notify_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->patient_status_notify_v05_patients_status_notify_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patient_status_on_notify_v05_patients_status_on_notify_post**
> object patient_status_on_notify_v05_patients_status_on_notify_post()

Patient Status On Notify

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # Patient Status On Notify
        api_response = api_instance.patient_status_on_notify_v05_patients_status_on_notify_post()
        print("The response of DefaultApi->patient_status_on_notify_v05_patients_status_on_notify_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->patient_status_on_notify_v05_patients_status_on_notify_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscription_hiu_notify_v05_subscriptions_hiu_notify_post**
> object subscription_hiu_notify_v05_subscriptions_hiu_notify_post()

Subscription Hiu Notify

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # Subscription Hiu Notify
        api_response = api_instance.subscription_hiu_notify_v05_subscriptions_hiu_notify_post()
        print("The response of DefaultApi->subscription_hiu_notify_v05_subscriptions_hiu_notify_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->subscription_hiu_notify_v05_subscriptions_hiu_notify_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscription_notify_v05_subscription_requests_hiu_notify_post**
> object subscription_notify_v05_subscription_requests_hiu_notify_post()

Subscription Notify

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # Subscription Notify
        api_response = api_instance.subscription_notify_v05_subscription_requests_hiu_notify_post()
        print("The response of DefaultApi->subscription_notify_v05_subscription_requests_hiu_notify_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->subscription_notify_v05_subscription_requests_hiu_notify_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

