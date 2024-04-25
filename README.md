# Ayushman Bharat Digital Mission: Health Information User SDK
[![PyPI version](https://badge.fury.io/py/ABDM-HIU-SDK.svg)](https://badge.fury.io/py/ABDM-HIU-SDK)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Check and Tests](https://github.com/Technoculture/ABDM-HIU-SDK/actions/workflows/abdm.yml/badge.svg)](https://github.com/Technoculture/ABDM-HIU-SDK/actions/workflows/abdm.yml)

The following are the specifications for the APIs to be implemented at the Health Repository end if an entity is only serving the role of a HIU. The specs are essentially duplicates from the Gateway and Bridge, but put together so as to make it clear to *HIUs* which set of APIs they should implement to participate in the network. 

  1. The APIs are organized by the flows - **identification**, **consent flow**, **data flow** and **monitoring**. They represent the APIs that are expected to be available at the HIU end by the Gateway. 
  2. For majority of the APIs, if Gateway has initiated a call, there are corresponding callback APIs on the Gateway. e.g for **/consents/hiu/notify** API on HIU end, its expected that a corresponding callback API **/consents/hiu/on-notify** on Gateway is called. Such APIs are organized under the **Gateway** label. 
  3. Gateway relevant APIs for HIUs are grouped under **Gateway** label. These include the APIs that HIPs are required to call on the Gateway. For example, to request a CM for consent, HIU would call **/consent-requests/init** API on gateway. 
  4. **NOTE**, in some of the API documentations below, **X-HIP-ID** is mentioned in header (for example in /auth/on-init). These are the cases, when a particular API is applicable for both HIU and HIP (e.g an entity is playing the role of HRP representing both HIU and HIP). If you are only playing the role of HIP, then only X-HIU-ID header will be sent 


This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.5
- Package version: 1.0.0
- Generator version: 7.5.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import abdm
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import abdm
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import abdm
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
    api_instance = abdm.GatewayApi(api_client)

    try:
        # Get certs for JWT verification
        api_response = api_instance.v05_certs_get()
        print("The response of GatewayApi->v05_certs_get:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GatewayApi->v05_certs_get: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://dev.abdm.gov.in/gateway*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*GatewayApi* | [**v05_certs_get**](docs/GatewayApi.md#v05_certs_get) | **GET** /v0.5/certs | Get certs for JWT verification
*GatewayApi* | [**v05_consent_requests_init_post**](docs/GatewayApi.md#v05_consent_requests_init_post) | **POST** /v0.5/consent-requests/init | Create consent request
*GatewayApi* | [**v05_consent_requests_status_post**](docs/GatewayApi.md#v05_consent_requests_status_post) | **POST** /v0.5/consent-requests/status | Get consent request status
*GatewayApi* | [**v05_consents_fetch_post**](docs/GatewayApi.md#v05_consents_fetch_post) | **POST** /v0.5/consents/fetch | Get consent artefact
*GatewayApi* | [**v05_consents_hiu_on_notify_post**](docs/GatewayApi.md#v05_consents_hiu_on_notify_post) | **POST** /v0.5/consents/hiu/on-notify | Consent notification
*GatewayApi* | [**v05_health_information_cm_request_post**](docs/GatewayApi.md#v05_health_information_cm_request_post) | **POST** /v0.5/health-information/cm/request | Health information data request
*GatewayApi* | [**v05_health_information_notify_post**](docs/GatewayApi.md#v05_health_information_notify_post) | **POST** /v0.5/health-information/notify | Notifications corresponding to events during data flow
*GatewayApi* | [**v05_patients_find_post**](docs/GatewayApi.md#v05_patients_find_post) | **POST** /v0.5/patients/find | Identify a patient by her consent-manager user-id
*GatewayApi* | [**v05_patients_status_on_notify_post**](docs/GatewayApi.md#v05_patients_status_on_notify_post) | **POST** /v0.5/patients/status/on-notify | Acknowledgment by HIU
*GatewayApi* | [**v05_sessions_post**](docs/GatewayApi.md#v05_sessions_post) | **POST** /v0.5/sessions | Get access token
*GatewayApi* | [**v05_subscription_requests_cm_init_post**](docs/GatewayApi.md#v05_subscription_requests_cm_init_post) | **POST** /v0.5/subscription-requests/cm/init | Request for subscription
*GatewayApi* | [**v05_subscription_requests_hiu_on_notify_post**](docs/GatewayApi.md#v05_subscription_requests_hiu_on_notify_post) | **POST** /v0.5/subscription-requests/hiu/on-notify | Callback API for /subscription-requests/hiu/notify to acknowledge receipt of notification.
*GatewayApi* | [**v05_subscriptions_hiu_on_notify_post**](docs/GatewayApi.md#v05_subscriptions_hiu_on_notify_post) | **POST** /v0.5/subscriptions/hiu/on-notify | Callback API for /subscriptions/hiu/notify to acknowledge receipt of notification.
*GatewayApi* | [**v05_users_auth_confirm_post**](docs/GatewayApi.md#v05_users_auth_confirm_post) | **POST** /v0.5/users/auth/confirm | Confirmation request sending token, otp or other authentication details from HIP/HIU for confirmation
*GatewayApi* | [**v05_users_auth_fetch_modes_post**](docs/GatewayApi.md#v05_users_auth_fetch_modes_post) | **POST** /v0.5/users/auth/fetch-modes | Get a patient&#39;s authentication modes relevant to specified purpose
*GatewayApi* | [**v05_users_auth_init_post**](docs/GatewayApi.md#v05_users_auth_init_post) | **POST** /v0.5/users/auth/init | Initialize authentication from HIP
*GatewayApi* | [**v05_users_auth_on_notify_post**](docs/GatewayApi.md#v05_users_auth_on_notify_post) | **POST** /v0.5/users/auth/on-notify | callback API by HIU/HIPs as acknowledgement of auth notification
*GatewayApi* | [**v05_well_known_openid_configuration_get**](docs/GatewayApi.md#v05_well_known_openid_configuration_get) | **GET** /v0.5/.well-known/openid-configuration | Get openid configuration
*ConsentFlowApi* | [**v05_consent_requests_on_init_post**](docs/ConsentFlowApi.md#v05_consent_requests_on_init_post) | **POST** /v0.5/consent-requests/on-init | Response to consent request
*ConsentFlowApi* | [**v05_consent_requests_on_status_post**](docs/ConsentFlowApi.md#v05_consent_requests_on_status_post) | **POST** /v0.5/consent-requests/on-status | Result of consent request status
*ConsentFlowApi* | [**v05_consents_hiu_notify_post**](docs/ConsentFlowApi.md#v05_consents_hiu_notify_post) | **POST** /v0.5/consents/hiu/notify | Consent notification
*ConsentFlowApi* | [**v05_consents_on_fetch_post**](docs/ConsentFlowApi.md#v05_consents_on_fetch_post) | **POST** /v0.5/consents/on-fetch | Result of fetch request for a consent artefact
*DataFlowApi* | [**v05_health_information_hiu_on_request_post**](docs/DataFlowApi.md#v05_health_information_hiu_on_request_post) | **POST** /v0.5/health-information/hiu/on-request | Health information data request
*DataFlowApi* | [**v05_health_information_transfer_post**](docs/DataFlowApi.md#v05_health_information_transfer_post) | **POST** /v0.5/health-information/transfer | health information transfer API
*IdentificationApi* | [**v05_patients_on_find_post**](docs/IdentificationApi.md#v05_patients_on_find_post) | **POST** /v0.5/patients/on-find | Identification result for a consent-manager user-id
*MonitoringApi* | [**v05_heartbeat_get**](docs/MonitoringApi.md#v05_heartbeat_get) | **GET** /v0.5/heartbeat | Informs about server status
*PatientNotificationApi* | [**v05_patients_status_notify_post**](docs/PatientNotificationApi.md#v05_patients_status_notify_post) | **POST** /v0.5/patients/status/notify | Notification sent by Consent Manager
*PatientNotificationApi* | [**v05_patients_status_on_notify_post**](docs/PatientNotificationApi.md#v05_patients_status_on_notify_post) | **POST** /v0.5/patients/status/on-notify | Acknowledgment by HIU
*SubscriptionsApi* | [**v05_subscription_requests_hiu_notify_post**](docs/SubscriptionsApi.md#v05_subscription_requests_hiu_notify_post) | **POST** /v0.5/subscription-requests/hiu/notify | Notification for subscription grant/deny/revoke
*SubscriptionsApi* | [**v05_subscription_requests_hiu_on_init_post**](docs/SubscriptionsApi.md#v05_subscription_requests_hiu_on_init_post) | **POST** /v0.5/subscription-requests/hiu/on-init | callback API for the /subscription-requests/cm/init to notify a HIU on acceptance/acknowledgement of the request for subscription.
*SubscriptionsApi* | [**v05_subscriptions_hiu_notify_post**](docs/SubscriptionsApi.md#v05_subscriptions_hiu_notify_post) | **POST** /v0.5/subscriptions/hiu/notify | Notification to HIU on basis of a granted subscription
*UserAuthApi* | [**v05_users_auth_notify_post**](docs/UserAuthApi.md#v05_users_auth_notify_post) | **POST** /v0.5/users/auth/notify | notification API in case of DIRECT mode of authentication by the CM
*UserAuthApi* | [**v05_users_auth_on_confirm_post**](docs/UserAuthApi.md#v05_users_auth_on_confirm_post) | **POST** /v0.5/users/auth/on-confirm | callback API for /auth/confirm (in case of MEDIATED auth) to confirm user authentication or not
*UserAuthApi* | [**v05_users_auth_on_fetch_modes_post**](docs/UserAuthApi.md#v05_users_auth_on_fetch_modes_post) | **POST** /v0.5/users/auth/on-fetch-modes | Identification result for a consent-manager user-id
*UserAuthApi* | [**v05_users_auth_on_init_post**](docs/UserAuthApi.md#v05_users_auth_on_init_post) | **POST** /v0.5/users/auth/on-init | Response to user authentication initialization from HIP


## Documentation For Models

 - [AccessTokenValidity](docs/AccessTokenValidity.md)
 - [AuthConfirmIdentifier](docs/AuthConfirmIdentifier.md)
 - [AuthConfirmIdentifierType](docs/AuthConfirmIdentifierType.md)
 - [AuthMeta](docs/AuthMeta.md)
 - [AuthenticationMode](docs/AuthenticationMode.md)
 - [CareContextDefinition](docs/CareContextDefinition.md)
 - [CertificateOrKeyGetSchema](docs/CertificateOrKeyGetSchema.md)
 - [Certs](docs/Certs.md)
 - [Consent](docs/Consent.md)
 - [ConsentAcknowledgement](docs/ConsentAcknowledgement.md)
 - [ConsentArtefactReference](docs/ConsentArtefactReference.md)
 - [ConsentArtefactResponse](docs/ConsentArtefactResponse.md)
 - [ConsentArtefactResponseConsent](docs/ConsentArtefactResponseConsent.md)
 - [ConsentArtefactResponseConsentConsentDetail](docs/ConsentArtefactResponseConsentConsentDetail.md)
 - [ConsentArtefactResponseConsentConsentDetailCareContextsInner](docs/ConsentArtefactResponseConsentConsentDetailCareContextsInner.md)
 - [ConsentArtefactResponseConsentConsentDetailConsentManager](docs/ConsentArtefactResponseConsentConsentDetailConsentManager.md)
 - [ConsentArtefactResponseConsentConsentDetailHip](docs/ConsentArtefactResponseConsentConsentDetailHip.md)
 - [ConsentArtefactResponseConsentConsentDetailHiu](docs/ConsentArtefactResponseConsentConsentDetailHiu.md)
 - [ConsentFetchRequest](docs/ConsentFetchRequest.md)
 - [ConsentManagerPatientID](docs/ConsentManagerPatientID.md)
 - [ConsentRequest](docs/ConsentRequest.md)
 - [ConsentRequestConsent](docs/ConsentRequestConsent.md)
 - [ConsentRequestConsentPatient](docs/ConsentRequestConsentPatient.md)
 - [ConsentRequestInitResponse](docs/ConsentRequestInitResponse.md)
 - [ConsentRequestInitResponseConsentRequest](docs/ConsentRequestInitResponseConsentRequest.md)
 - [ConsentRequestStatusRequest](docs/ConsentRequestStatusRequest.md)
 - [ConsentStatus](docs/ConsentStatus.md)
 - [DataNotification](docs/DataNotification.md)
 - [DataNotificationEntriesInner](docs/DataNotificationEntriesInner.md)
 - [DateRange](docs/DateRange.md)
 - [EntryContent](docs/EntryContent.md)
 - [EntryLink](docs/EntryLink.md)
 - [Error](docs/Error.md)
 - [ErrorResponse](docs/ErrorResponse.md)
 - [EventCategoryDetail](docs/EventCategoryDetail.md)
 - [HIRequest](docs/HIRequest.md)
 - [HIRequestHiRequest](docs/HIRequestHiRequest.md)
 - [HITypeEnum](docs/HITypeEnum.md)
 - [HIUConsentNotificationEvent](docs/HIUConsentNotificationEvent.md)
 - [HIUConsentNotificationEventNotification](docs/HIUConsentNotificationEventNotification.md)
 - [HIUConsentNotificationResponse](docs/HIUConsentNotificationResponse.md)
 - [HIUConsentRequestStatus](docs/HIUConsentRequestStatus.md)
 - [HIUConsentRequestStatusConsentRequest](docs/HIUConsentRequestStatusConsentRequest.md)
 - [HIUHealthInformationRequestResponse](docs/HIUHealthInformationRequestResponse.md)
 - [HIUHealthInformationRequestResponseHiRequest](docs/HIUHealthInformationRequestResponseHiRequest.md)
 - [HIUSubscription](docs/HIUSubscription.md)
 - [HIUSubscriptionContext](docs/HIUSubscriptionContext.md)
 - [HIUSubscriptionEventContent](docs/HIUSubscriptionEventContent.md)
 - [HIUSubscriptionNotification](docs/HIUSubscriptionNotification.md)
 - [HIUSubscriptionNotificationAcknowledgment](docs/HIUSubscriptionNotificationAcknowledgment.md)
 - [HIUSubscriptionNotificationAcknowledgmentAcknowledgement](docs/HIUSubscriptionNotificationAcknowledgmentAcknowledgement.md)
 - [HIUSubscriptionNotificationEvent](docs/HIUSubscriptionNotificationEvent.md)
 - [HIUSubscriptionRequestNotificationAcknowledgement](docs/HIUSubscriptionRequestNotificationAcknowledgement.md)
 - [HIUSubscriptionRequestNotificationAcknowledgementAcknowledgement](docs/HIUSubscriptionRequestNotificationAcknowledgementAcknowledgement.md)
 - [HIUSubscriptionRequestReceipt](docs/HIUSubscriptionRequestReceipt.md)
 - [HealthInformationNotification](docs/HealthInformationNotification.md)
 - [HealthInformationNotificationNotification](docs/HealthInformationNotificationNotification.md)
 - [HealthInformationNotificationNotificationNotifier](docs/HealthInformationNotificationNotificationNotifier.md)
 - [HealthInformationNotificationNotificationStatusNotification](docs/HealthInformationNotificationNotificationStatusNotification.md)
 - [HealthInformationNotificationNotificationStatusNotificationStatusResponsesInner](docs/HealthInformationNotificationNotificationStatusNotificationStatusResponsesInner.md)
 - [HeartbeatResponse](docs/HeartbeatResponse.md)
 - [HiuPatientStatusNotification](docs/HiuPatientStatusNotification.md)
 - [HiuPatientStatusNotificationNotification](docs/HiuPatientStatusNotificationNotification.md)
 - [HiuPatientStatusNotificationNotificationPatient](docs/HiuPatientStatusNotificationNotificationPatient.md)
 - [Identifier](docs/Identifier.md)
 - [IdentifierType](docs/IdentifierType.md)
 - [KeyMaterial](docs/KeyMaterial.md)
 - [KeyObject](docs/KeyObject.md)
 - [OpenIdConfiguration](docs/OpenIdConfiguration.md)
 - [OrganizationRepresentation](docs/OrganizationRepresentation.md)
 - [PatientAddress](docs/PatientAddress.md)
 - [PatientAuthConfirmRequest](docs/PatientAuthConfirmRequest.md)
 - [PatientAuthConfirmRequestCredential](docs/PatientAuthConfirmRequestCredential.md)
 - [PatientAuthConfirmResponse](docs/PatientAuthConfirmResponse.md)
 - [PatientAuthConfirmResponseAuth](docs/PatientAuthConfirmResponseAuth.md)
 - [PatientAuthInitRequest](docs/PatientAuthInitRequest.md)
 - [PatientAuthInitRequestQuery](docs/PatientAuthInitRequestQuery.md)
 - [PatientAuthInitRequestQueryRequester](docs/PatientAuthInitRequestQueryRequester.md)
 - [PatientAuthInitResponse](docs/PatientAuthInitResponse.md)
 - [PatientAuthInitResponseAuth](docs/PatientAuthInitResponseAuth.md)
 - [PatientAuthModeQueryRequest](docs/PatientAuthModeQueryRequest.md)
 - [PatientAuthModeQueryRequestQuery](docs/PatientAuthModeQueryRequestQuery.md)
 - [PatientAuthModeQueryRequestQueryRequester](docs/PatientAuthModeQueryRequestQueryRequester.md)
 - [PatientAuthModeQueryResponse](docs/PatientAuthModeQueryResponse.md)
 - [PatientAuthModeQueryResponseAuth](docs/PatientAuthModeQueryResponseAuth.md)
 - [PatientAuthNotification](docs/PatientAuthNotification.md)
 - [PatientAuthNotificationAcknowledgement](docs/PatientAuthNotificationAcknowledgement.md)
 - [PatientAuthNotificationAcknowledgementAcknowledgement](docs/PatientAuthNotificationAcknowledgementAcknowledgement.md)
 - [PatientAuthNotificationAuth](docs/PatientAuthNotificationAuth.md)
 - [PatientAuthPurpose](docs/PatientAuthPurpose.md)
 - [PatientAuthRequester](docs/PatientAuthRequester.md)
 - [PatientDemographic](docs/PatientDemographic.md)
 - [PatientDemographicResponse](docs/PatientDemographicResponse.md)
 - [PatientGender](docs/PatientGender.md)
 - [PatientIdentificationRequest](docs/PatientIdentificationRequest.md)
 - [PatientIdentificationRequestQuery](docs/PatientIdentificationRequestQuery.md)
 - [PatientIdentificationRequestQueryPatient](docs/PatientIdentificationRequestQueryPatient.md)
 - [PatientIdentificationRequestQueryRequester](docs/PatientIdentificationRequestQueryRequester.md)
 - [PatientIdentificationResponse](docs/PatientIdentificationResponse.md)
 - [PatientIdentificationResponsePatient](docs/PatientIdentificationResponsePatient.md)
 - [PatientStatusNotification](docs/PatientStatusNotification.md)
 - [Permission](docs/Permission.md)
 - [PermissionDateRange](docs/PermissionDateRange.md)
 - [PermissionFrequency](docs/PermissionFrequency.md)
 - [RequestReference](docs/RequestReference.md)
 - [Requester](docs/Requester.md)
 - [RequesterIdentifier](docs/RequesterIdentifier.md)
 - [SessionRequest](docs/SessionRequest.md)
 - [SessionResponse](docs/SessionResponse.md)
 - [SubscriptionApprovalNotification](docs/SubscriptionApprovalNotification.md)
 - [SubscriptionApprovalNotificationNotification](docs/SubscriptionApprovalNotificationNotification.md)
 - [SubscriptionCategory](docs/SubscriptionCategory.md)
 - [SubscriptionPeriod](docs/SubscriptionPeriod.md)
 - [SubscriptionRequest](docs/SubscriptionRequest.md)
 - [SubscriptionRequestSubscription](docs/SubscriptionRequestSubscription.md)
 - [SubscriptionStatus](docs/SubscriptionStatus.md)
 - [UsePurpose](docs/UsePurpose.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization

Endpoints do not require authorization.


## Author




