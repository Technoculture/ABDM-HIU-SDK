# openapi_client.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**gateway_consent_request_notify_your_gateway_callback_url_prefix_consents_hiu_notify_post**](DefaultApi.md#gateway_consent_request_notify_your_gateway_callback_url_prefix_consents_hiu_notify_post) | **POST** /your_gateway_callback_url_prefix/consents/hiu/notify | Gateway Consent Request Notify
[**gateway_consent_request_on_fetch_your_gateway_callback_url_prefix_consents_on_fetch_post**](DefaultApi.md#gateway_consent_request_on_fetch_your_gateway_callback_url_prefix_consents_on_fetch_post) | **POST** /your_gateway_callback_url_prefix/consents/on-fetch | Gateway Consent Request On Fetch
[**gateway_consent_request_on_init_your_gateway_callback_url_prefix_consent_requests_on_init_post**](DefaultApi.md#gateway_consent_request_on_init_your_gateway_callback_url_prefix_consent_requests_on_init_post) | **POST** /your_gateway_callback_url_prefix/consent-requests/on-init | Gateway Consent Request On Init
[**gateway_health_information_on_request_your_gateway_callback_url_prefix_health_information_hiu_on_request_post**](DefaultApi.md#gateway_health_information_on_request_your_gateway_callback_url_prefix_health_information_hiu_on_request_post) | **POST** /your_gateway_callback_url_prefix/health-information/hiu/on-request | Gateway Health Information On Request
[**generate_consent_request_api_hiu_generate_consent_request_post**](DefaultApi.md#generate_consent_request_api_hiu_generate_consent_request_post) | **POST** /api/hiu/generate_consent_request | Generate Consent Request
[**list_consent_artefacts_api_hiu_consent_artefacts_get**](DefaultApi.md#list_consent_artefacts_api_hiu_consent_artefacts_get) | **GET** /api/hiu/consent_artefacts | List Consent Artefacts
[**list_consents_api_hiu_consents_get**](DefaultApi.md#list_consents_api_hiu_consents_get) | **GET** /api/hiu/consents | List Consents
[**receive_health_information_api_hiu_health_information_receive_post**](DefaultApi.md#receive_health_information_api_hiu_health_information_receive_post) | **POST** /api/hiu/health-information/receive | Receive Health Information
[**request_health_information_api_hiu_health_information_request_post**](DefaultApi.md#request_health_information_api_hiu_health_information_request_post) | **POST** /api/hiu/health-information/request | Request Health Information
[**retrieve_consent_api_hiu_consents_pk_get**](DefaultApi.md#retrieve_consent_api_hiu_consents_pk_get) | **GET** /api/hiu/consents/{pk} | Retrieve Consent
[**retrieve_consent_artefact_api_hiu_consent_artefacts_pk_get**](DefaultApi.md#retrieve_consent_artefact_api_hiu_consent_artefacts_pk_get) | **GET** /api/hiu/consent_artefacts/{pk} | Retrieve Consent Artefact


# **gateway_consent_request_notify_your_gateway_callback_url_prefix_consents_hiu_notify_post**
> object gateway_consent_request_notify_your_gateway_callback_url_prefix_consents_hiu_notify_post()

Gateway Consent Request Notify

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
        # Gateway Consent Request Notify
        api_response = api_instance.gateway_consent_request_notify_your_gateway_callback_url_prefix_consents_hiu_notify_post()
        print("The response of DefaultApi->gateway_consent_request_notify_your_gateway_callback_url_prefix_consents_hiu_notify_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->gateway_consent_request_notify_your_gateway_callback_url_prefix_consents_hiu_notify_post: %s\n" % e)
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

# **gateway_consent_request_on_fetch_your_gateway_callback_url_prefix_consents_on_fetch_post**
> object gateway_consent_request_on_fetch_your_gateway_callback_url_prefix_consents_on_fetch_post()

Gateway Consent Request On Fetch

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
        # Gateway Consent Request On Fetch
        api_response = api_instance.gateway_consent_request_on_fetch_your_gateway_callback_url_prefix_consents_on_fetch_post()
        print("The response of DefaultApi->gateway_consent_request_on_fetch_your_gateway_callback_url_prefix_consents_on_fetch_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->gateway_consent_request_on_fetch_your_gateway_callback_url_prefix_consents_on_fetch_post: %s\n" % e)
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

# **gateway_consent_request_on_init_your_gateway_callback_url_prefix_consent_requests_on_init_post**
> object gateway_consent_request_on_init_your_gateway_callback_url_prefix_consent_requests_on_init_post()

Gateway Consent Request On Init

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
        # Gateway Consent Request On Init
        api_response = api_instance.gateway_consent_request_on_init_your_gateway_callback_url_prefix_consent_requests_on_init_post()
        print("The response of DefaultApi->gateway_consent_request_on_init_your_gateway_callback_url_prefix_consent_requests_on_init_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->gateway_consent_request_on_init_your_gateway_callback_url_prefix_consent_requests_on_init_post: %s\n" % e)
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

# **gateway_health_information_on_request_your_gateway_callback_url_prefix_health_information_hiu_on_request_post**
> object gateway_health_information_on_request_your_gateway_callback_url_prefix_health_information_hiu_on_request_post()

Gateway Health Information On Request

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
        # Gateway Health Information On Request
        api_response = api_instance.gateway_health_information_on_request_your_gateway_callback_url_prefix_health_information_hiu_on_request_post()
        print("The response of DefaultApi->gateway_health_information_on_request_your_gateway_callback_url_prefix_health_information_hiu_on_request_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->gateway_health_information_on_request_your_gateway_callback_url_prefix_health_information_hiu_on_request_post: %s\n" % e)
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

# **generate_consent_request_api_hiu_generate_consent_request_post**
> object generate_consent_request_api_hiu_generate_consent_request_post()

Generate Consent Request

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
        # Generate Consent Request
        api_response = api_instance.generate_consent_request_api_hiu_generate_consent_request_post()
        print("The response of DefaultApi->generate_consent_request_api_hiu_generate_consent_request_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->generate_consent_request_api_hiu_generate_consent_request_post: %s\n" % e)
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

# **list_consent_artefacts_api_hiu_consent_artefacts_get**
> object list_consent_artefacts_api_hiu_consent_artefacts_get()

List Consent Artefacts

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
        # List Consent Artefacts
        api_response = api_instance.list_consent_artefacts_api_hiu_consent_artefacts_get()
        print("The response of DefaultApi->list_consent_artefacts_api_hiu_consent_artefacts_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_consent_artefacts_api_hiu_consent_artefacts_get: %s\n" % e)
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

# **list_consents_api_hiu_consents_get**
> object list_consents_api_hiu_consents_get()

List Consents

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
        # List Consents
        api_response = api_instance.list_consents_api_hiu_consents_get()
        print("The response of DefaultApi->list_consents_api_hiu_consents_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_consents_api_hiu_consents_get: %s\n" % e)
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

# **receive_health_information_api_hiu_health_information_receive_post**
> object receive_health_information_api_hiu_health_information_receive_post()

Receive Health Information

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
        # Receive Health Information
        api_response = api_instance.receive_health_information_api_hiu_health_information_receive_post()
        print("The response of DefaultApi->receive_health_information_api_hiu_health_information_receive_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->receive_health_information_api_hiu_health_information_receive_post: %s\n" % e)
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

# **request_health_information_api_hiu_health_information_request_post**
> object request_health_information_api_hiu_health_information_request_post()

Request Health Information

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
        # Request Health Information
        api_response = api_instance.request_health_information_api_hiu_health_information_request_post()
        print("The response of DefaultApi->request_health_information_api_hiu_health_information_request_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->request_health_information_api_hiu_health_information_request_post: %s\n" % e)
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

# **retrieve_consent_api_hiu_consents_pk_get**
> object retrieve_consent_api_hiu_consents_pk_get(pk)

Retrieve Consent

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
    pk = 56 # int | 

    try:
        # Retrieve Consent
        api_response = api_instance.retrieve_consent_api_hiu_consents_pk_get(pk)
        print("The response of DefaultApi->retrieve_consent_api_hiu_consents_pk_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->retrieve_consent_api_hiu_consents_pk_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pk** | **int**|  | 

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
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_consent_artefact_api_hiu_consent_artefacts_pk_get**
> object retrieve_consent_artefact_api_hiu_consent_artefacts_pk_get(pk)

Retrieve Consent Artefact

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
    pk = 56 # int | 

    try:
        # Retrieve Consent Artefact
        api_response = api_instance.retrieve_consent_artefact_api_hiu_consent_artefacts_pk_get(pk)
        print("The response of DefaultApi->retrieve_consent_artefact_api_hiu_consent_artefacts_pk_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->retrieve_consent_artefact_api_hiu_consent_artefacts_pk_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pk** | **int**|  | 

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
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

