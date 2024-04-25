# abdm.DataFlowApi

All URIs are relative to *https://dev.abdm.gov.in/gateway*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v05_health_information_hiu_on_request_post**](DataFlowApi.md#v05_health_information_hiu_on_request_post) | **POST** /v0.5/health-information/hiu/on-request | Health information data request
[**v05_health_information_transfer_post**](DataFlowApi.md#v05_health_information_transfer_post) | **POST** /v0.5/health-information/transfer | health information transfer API


# **v05_health_information_hiu_on_request_post**
> v05_health_information_hiu_on_request_post(authorization, x_hiu_id, hiu_health_information_request_response)

Health information data request

Callback API for acknowledgement of Health information request made by HIU. Gateway calls this API when request has validated for the specified  consent id. Either the **hiRequest** or **error** would be specified. If the health info request was valid, then the ***hiRequest.transactionId*** specifies the transaction context against which HIP would send over the data.  Possible cases of errors are   1. **Invalid consent artefact id**   2. **Consent has expired**   3. **Date ranges are invalid** 

### Example


```python
import abdm
from abdm.models.hiu_health_information_request_response import HIUHealthInformationRequestResponse
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
    api_instance = abdm.DataFlowApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge.
    x_hiu_id = 'x_hiu_id_example' # str | Identifier of the health information user to which the request was intended.
    hiu_health_information_request_response = abdm.HIUHealthInformationRequestResponse() # HIUHealthInformationRequestResponse | 

    try:
        # Health information data request
        api_instance.v05_health_information_hiu_on_request_post(authorization, x_hiu_id, hiu_health_information_request_response)
    except Exception as e:
        print("Exception when calling DataFlowApi->v05_health_information_hiu_on_request_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge. | 
 **x_hiu_id** | **str**| Identifier of the health information user to which the request was intended. | 
 **hiu_health_information_request_response** | [**HIUHealthInformationRequestResponse**](HIUHealthInformationRequestResponse.md)|  | 

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
**400** | **Causes:**   * Bad request  |  -  |
**401** | **Causes:**   * Token is invalid or Link has expired  |  -  |
**500** | **Causes:**   * Downstream system(s) is down.   * Unhandled exceptions.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v05_health_information_transfer_post**
> v05_health_information_transfer_post(authorization, data_notification)

health information transfer API

**NOTE**: This API is actually the callback URL that is passed as **dataPushUrl** in the data request API - /v0.5/health-information/hip/request. This API is directly called by HIP Data Bridge and is not mediated via CM, and hence not routed through the Gateway.    1. This API should be implemented at HIU side. It maybe implemented by the Data Bridge representing the HIU.    2. Entry elements maybe ***content*** or ***link***, although for version 1, entry ***content*** is preferred.    3. Entry ***content*** (or even link reference content) must be encrypted by means of Elliptic-curve Diffie–Hellman Key Exchange, utilizing the HIU keymaterials that are passed through the data request API - /v0.5/health-information/hip/request.    4. Media contains the mimetype of content, and for v1, it is \"application/fhir+json\"   5. checksum is Md5 checksum of the data conent, before encryption   6. Please refer to the ABDM Sandbox documentation for the format of FHIR bundle that is passed through content 

### Example


```python
import abdm
from abdm.models.data_notification import DataNotification
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
    api_instance = abdm.DataFlowApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge.
    data_notification = abdm.DataNotification() # DataNotification | 

    try:
        # health information transfer API
        api_instance.v05_health_information_transfer_post(authorization, data_notification)
    except Exception as e:
        print("Exception when calling DataFlowApi->v05_health_information_transfer_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge. | 
 **data_notification** | [**DataNotification**](DataNotification.md)|  | 

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
**202** | Data accepted. |  -  |
**401** | **Causes:**   * Invalid/Expired/Empty token.  |  -  |
**500** | **Causes:**   * Downstream services are down  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

