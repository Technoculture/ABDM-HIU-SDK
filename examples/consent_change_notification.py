import abdm_hiu_sdk
from abdm_hiu_sdk.rest import ApiException
from pprint import pprint

# Configuration for the API client, using default URL for demonstration
configuration = abdm_hiu_sdk.Configuration(
    host="https://sandbox.abdm.gov.in"
)

# Creating an API client instance
with abdm_hiu_sdk.ApiClient(configuration) as api_client:
    # Instance of the DefaultAPI class
    api_instance = abdm_hiu_sdk.DefaultAPI(api_client)
    # Notify HIU of consent changes via gateway
    try:
        notify_payload = {
            "consent_id": "consent123",
            "status": "updated"
        }
        notify_response = api_instance.gateway_consent_request_notify(notify_payload)
        pprint("Notification Response for Consent Change:")
        pprint(notify_response)
    except ApiException as e:
        print(f"Exception when calling DefaultAPI->gateway_consent_request_notify: {e}\n")
