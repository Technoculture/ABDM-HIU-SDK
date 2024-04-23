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
    # Receive health information
    try:
        receive_health_info_payload = {
            "health_information": {
                "patient_id": "12345",
                "data": "base64-encoded-data"
            }
        }
        receive_health_info_response = api_instance.receive_health_information(receive_health_info_payload)
        pprint("Received Health Information:")
        pprint(receive_health_info_response)
    except ApiException as e:
        print(f"Exception when calling DefaultAPI->receive_health_information: {e}\n")
