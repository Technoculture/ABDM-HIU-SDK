import abdm
from abdm.rest import ApiException
from pprint import pprint

# Configuration for the API client, using default URL for demonstration
configuration = abdm.Configuration(host="https://dev.abdm.gov.in/gateway")

# Creating an API client instance
with abdm.ApiClient(configuration) as api_client:
    # Instance of the DefaultAPI class
    api_instance = abdm.DefaultAPI(api_client)

    # Example to generate a new consent request
    try:
        consent_request_payload = {
            "patient_id": "12345",
            "consent_template_id": "template123",
            "permissions": ["read", "write"],
            "expiry_date": "2024-12-31",
        }
        generate_response = api_instance.generate_consent_request(
            consent_request_payload
        )
        pprint("Generated Consent Request:")
        pprint(generate_response)
    except ApiException as e:
        print(f"Exception when calling DefaultAPI->generate_consent_request: {e}\n")
