# abdm-hiu-sdk.DefaultAPI

All URIs are relative to *https://example.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**gateway_consent_request_notify**](DefaultAPI.md#gateway_consent_request_notify) | **POST** /your_gateway_callback_url_prefix/consents/hiu/notify | Notify HIU of consent changes via gateway
[**gateway_consent_request_on_fetch**](DefaultAPI.md#gateway_consent_request_on_fetch) | **POST** /your_gateway_callback_url_prefix/consents/on-fetch | Fetch consents from gateway
[**gateway_consent_request_on_init**](DefaultAPI.md#gateway_consent_request_on_init) | **POST** /your_gateway_callback_url_prefix/consent-requests/on-init | Handle gateway consent request initialization
[**gateway_health_information_on_request**](DefaultAPI.md#gateway_health_information_on_request) | **POST** /your_gateway_callback_url_prefix/health-information/hiu/on-request | Handle gateway health information request
[**generate_consent_request**](DefaultAPI.md#generate_consent_request) | **POST** /api/hiu/generate_consent_request | Generate a new consent request
[**list_consent_artefacts**](DefaultAPI.md#list_consent_artefacts) | **GET** /api/hiu/consent_artefacts | List consent artefacts
[**list_consents**](DefaultAPI.md#list_consents) | **GET** /api/hiu/consents | List all consents
[**receive_health_information**](DefaultAPI.md#receive_health_information) | **POST** /api/hiu/health-information/receive | Receive health information
[**request_health_information**](DefaultAPI.md#request_health_information) | **POST** /api/hiu/health-information/request | Request health information
[**retrieve_consent**](DefaultAPI.md#retrieve_consent) | **GET** /api/hiu/consents/{pk} | Retrieve a specific consent
[**retrieve_consent_artefact**](DefaultAPI.md#retrieve_consent_artefact) | **GET** /api/hiu/consent_artefacts/{pk} | Retrieve a specific consent artefact


# **gateway_consent_request_notify**
> GatewayConsentRequestNotify200ResponseModelModel gateway_consent_request_notify()

Notify HIU of consent changes via gateway

### Example


```python
import abdm-hiu-sdk
from abdm-hiu-sdk.models.gateway_consent_request_notify200_response_model_model import GatewayConsentRequestNotify200ResponseModelModel
from abdm-hiu-sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://example.com
# See configuration.py for a list of all supported configuration parameters.
configuration = abdm-hiu-sdk.Configuration(
    host = "https://example.com"
)


# Enter a context with an instance of the API client
with abdm-hiu-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = abdm-hiu-sdk.DefaultAPI(api_client)

    try:
        # Notify HIU of consent changes via gateway
        api_response = api_instance.gateway_consent_request_notify()
        print("The response of DefaultAPI->gateway_consent_request_notify:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultAPI->gateway_consent_request_notify: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GatewayConsentRequestNotify200ResponseModelModel**](GatewayConsentRequestNotify200ResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | HIU notified of consent change |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gateway_consent_request_on_fetch**
> GatewayConsentRequestOnFetch200ResponseModelModel gateway_consent_request_on_fetch()

Fetch consents from gateway

### Example


```python
import abdm-hiu-sdk
from abdm-hiu-sdk.models.gateway_consent_request_on_fetch200_response_model_model import GatewayConsentRequestOnFetch200ResponseModelModel
from abdm-hiu-sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://example.com
# See configuration.py for a list of all supported configuration parameters.
configuration = abdm-hiu-sdk.Configuration(
    host = "https://example.com"
)


# Enter a context with an instance of the API client
with abdm-hiu-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = abdm-hiu-sdk.DefaultAPI(api_client)

    try:
        # Fetch consents from gateway
        api_response = api_instance.gateway_consent_request_on_fetch()
        print("The response of DefaultAPI->gateway_consent_request_on_fetch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultAPI->gateway_consent_request_on_fetch: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GatewayConsentRequestOnFetch200ResponseModelModel**](GatewayConsentRequestOnFetch200ResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Consents fetched from gateway |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gateway_consent_request_on_init**
> GatewayConsentRequestOnInit200ResponseModelModel gateway_consent_request_on_init()

Handle gateway consent request initialization

### Example


```python
import abdm-hiu-sdk
from abdm-hiu-sdk.models.gateway_consent_request_on_init200_response_model_model import GatewayConsentRequestOnInit200ResponseModelModel
from abdm-hiu-sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://example.com
# See configuration.py for a list of all supported configuration parameters.
configuration = abdm-hiu-sdk.Configuration(
    host = "https://example.com"
)


# Enter a context with an instance of the API client
with abdm-hiu-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = abdm-hiu-sdk.DefaultAPI(api_client)

    try:
        # Handle gateway consent request initialization
        api_response = api_instance.gateway_consent_request_on_init()
        print("The response of DefaultAPI->gateway_consent_request_on_init:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultAPI->gateway_consent_request_on_init: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GatewayConsentRequestOnInit200ResponseModelModel**](GatewayConsentRequestOnInit200ResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gateway consent request initialization handled |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gateway_health_information_on_request**
> GatewayHealthInformationOnRequest200ResponseModelModel gateway_health_information_on_request()

Handle gateway health information request

### Example


```python
import abdm-hiu-sdk
from abdm-hiu-sdk.models.gateway_health_information_on_request200_response_model_model import GatewayHealthInformationOnRequest200ResponseModelModel
from abdm-hiu-sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://example.com
# See configuration.py for a list of all supported configuration parameters.
configuration = abdm-hiu-sdk.Configuration(
    host = "https://example.com"
)


# Enter a context with an instance of the API client
with abdm-hiu-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = abdm-hiu-sdk.DefaultAPI(api_client)

    try:
        # Handle gateway health information request
        api_response = api_instance.gateway_health_information_on_request()
        print("The response of DefaultAPI->gateway_health_information_on_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultAPI->gateway_health_information_on_request: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GatewayHealthInformationOnRequest200ResponseModelModel**](GatewayHealthInformationOnRequest200ResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gateway health information request handled |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_consent_request**
> GenerateConsentRequest200ResponseModelModel generate_consent_request()

Generate a new consent request

### Example


```python
import abdm-hiu-sdk
from abdm-hiu-sdk.models.generate_consent_request200_response_model_model import GenerateConsentRequest200ResponseModelModel
from abdm-hiu-sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://example.com
# See configuration.py for a list of all supported configuration parameters.
configuration = abdm-hiu-sdk.Configuration(
    host = "https://example.com"
)


# Enter a context with an instance of the API client
with abdm-hiu-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = abdm-hiu-sdk.DefaultAPI(api_client)

    try:
        # Generate a new consent request
        api_response = api_instance.generate_consent_request()
        print("The response of DefaultAPI->generate_consent_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultAPI->generate_consent_request: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GenerateConsentRequest200ResponseModelModel**](GenerateConsentRequest200ResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Consent request successfully generated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_consent_artefacts**
> ListConsentArtefacts200ResponseModelModel list_consent_artefacts()

List consent artefacts

### Example


```python
import abdm-hiu-sdk
from abdm-hiu-sdk.models.list_consent_artefacts200_response_model_model import ListConsentArtefacts200ResponseModelModel
from abdm-hiu-sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://example.com
# See configuration.py for a list of all supported configuration parameters.
configuration = abdm-hiu-sdk.Configuration(
    host = "https://example.com"
)


# Enter a context with an instance of the API client
with abdm-hiu-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = abdm-hiu-sdk.DefaultAPI(api_client)

    try:
        # List consent artefacts
        api_response = api_instance.list_consent_artefacts()
        print("The response of DefaultAPI->list_consent_artefacts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultAPI->list_consent_artefacts: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ListConsentArtefacts200ResponseModelModel**](ListConsentArtefacts200ResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of consent artefacts |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_consents**
> ListConsents200ResponseModelModel list_consents()

List all consents

### Example


```python
import abdm-hiu-sdk
from abdm-hiu-sdk.models.list_consents200_response_model_model import ListConsents200ResponseModelModel
from abdm-hiu-sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://example.com
# See configuration.py for a list of all supported configuration parameters.
configuration = abdm-hiu-sdk.Configuration(
    host = "https://example.com"
)


# Enter a context with an instance of the API client
with abdm-hiu-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = abdm-hiu-sdk.DefaultAPI(api_client)

    try:
        # List all consents
        api_response = api_instance.list_consents()
        print("The response of DefaultAPI->list_consents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultAPI->list_consents: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ListConsents200ResponseModelModel**](ListConsents200ResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of consents |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **receive_health_information**
> ReceiveHealthInformation200ResponseModelModel receive_health_information()

Receive health information

### Example


```python
import abdm-hiu-sdk
from abdm-hiu-sdk.models.receive_health_information200_response_model_model import ReceiveHealthInformation200ResponseModelModel
from abdm-hiu-sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://example.com
# See configuration.py for a list of all supported configuration parameters.
configuration = abdm-hiu-sdk.Configuration(
    host = "https://example.com"
)


# Enter a context with an instance of the API client
with abdm-hiu-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = abdm-hiu-sdk.DefaultAPI(api_client)

    try:
        # Receive health information
        api_response = api_instance.receive_health_information()
        print("The response of DefaultAPI->receive_health_information:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultAPI->receive_health_information: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ReceiveHealthInformation200ResponseModelModel**](ReceiveHealthInformation200ResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Health information received |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_health_information**
> RequestHealthInformation200ResponseModelModel request_health_information()

Request health information

### Example


```python
import abdm-hiu-sdk
from abdm-hiu-sdk.models.request_health_information200_response_model_model import RequestHealthInformation200ResponseModelModel
from abdm-hiu-sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://example.com
# See configuration.py for a list of all supported configuration parameters.
configuration = abdm-hiu-sdk.Configuration(
    host = "https://example.com"
)


# Enter a context with an instance of the API client
with abdm-hiu-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = abdm-hiu-sdk.DefaultAPI(api_client)

    try:
        # Request health information
        api_response = api_instance.request_health_information()
        print("The response of DefaultAPI->request_health_information:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultAPI->request_health_information: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**RequestHealthInformation200ResponseModelModel**](RequestHealthInformation200ResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Health information request submitted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_consent**
> RetrieveConsent200ResponseModelModel retrieve_consent(pk)

Retrieve a specific consent

### Example


```python
import abdm-hiu-sdk
from abdm-hiu-sdk.models.retrieve_consent200_response_model_model import RetrieveConsent200ResponseModelModel
from abdm-hiu-sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://example.com
# See configuration.py for a list of all supported configuration parameters.
configuration = abdm-hiu-sdk.Configuration(
    host = "https://example.com"
)


# Enter a context with an instance of the API client
with abdm-hiu-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = abdm-hiu-sdk.DefaultAPI(api_client)
    pk = 56 # int | Primary key of the consent

    try:
        # Retrieve a specific consent
        api_response = api_instance.retrieve_consent(pk)
        print("The response of DefaultAPI->retrieve_consent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultAPI->retrieve_consent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pk** | **int**| Primary key of the consent | 

### Return type

[**RetrieveConsent200ResponseModelModel**](RetrieveConsent200ResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Consent retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_consent_artefact**
> RetrieveConsentArtefact200ResponseModelModel retrieve_consent_artefact(pk)

Retrieve a specific consent artefact

### Example


```python
import abdm-hiu-sdk
from abdm-hiu-sdk.models.retrieve_consent_artefact200_response_model_model import RetrieveConsentArtefact200ResponseModelModel
from abdm-hiu-sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://example.com
# See configuration.py for a list of all supported configuration parameters.
configuration = abdm-hiu-sdk.Configuration(
    host = "https://example.com"
)


# Enter a context with an instance of the API client
with abdm-hiu-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = abdm-hiu-sdk.DefaultAPI(api_client)
    pk = 56 # int | Primary key of the consent artefact

    try:
        # Retrieve a specific consent artefact
        api_response = api_instance.retrieve_consent_artefact(pk)
        print("The response of DefaultAPI->retrieve_consent_artefact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultAPI->retrieve_consent_artefact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pk** | **int**| Primary key of the consent artefact | 

### Return type

[**RetrieveConsentArtefact200ResponseModelModel**](RetrieveConsentArtefact200ResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Consent artefact retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

