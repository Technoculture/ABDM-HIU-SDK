# abdm.IdentificationApi

All URIs are relative to *https://dev.abdm.gov.in/gateway*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v05_patients_on_find_post**](IdentificationApi.md#v05_patients_on_find_post) | **POST** /v0.5/patients/on-find | Identification result for a consent-manager user-id


# **v05_patients_on_find_post**
> v05_patients_on_find_post(authorization, patient_identification_response)

Identification result for a consent-manager user-id

If a patient is found then patient.name contains the patients name.  Otherwise, patient is not provided, and possibly error is raised for invalid requests Note in addition to the \"Authorization\" header, one of the following headers must be specified 1. specify **X-HIU-ID** if the requester is HIU (identified from /find requester.id) 2. specify **X-HIP-ID** if the requester is HIP (identified from /find requester.id) 

### Example


```python
import abdm
from abdm.models.patient_identification_response import PatientIdentificationResponse
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
    api_instance = abdm.IdentificationApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge.
    patient_identification_response = abdm.PatientIdentificationResponse() # PatientIdentificationResponse | 

    try:
        # Identification result for a consent-manager user-id
        api_instance.v05_patients_on_find_post(authorization, patient_identification_response)
    except Exception as e:
        print("Exception when calling IdentificationApi->v05_patients_on_find_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge. | 
 **patient_identification_response** | [**PatientIdentificationResponse**](PatientIdentificationResponse.md)|  | 

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

