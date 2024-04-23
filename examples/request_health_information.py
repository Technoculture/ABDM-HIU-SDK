import abdm_hiu_sdk
from abdm_hiu_sdk.rest import ApiException
from pprint import pprint

# Configuration for the API client, using default URL for demonstration
configuration = abdm_hiu_sdk.Configuration(
    host="https://sandbox.abdm.gov.in"
)

# Creating an API client instance
with abdm_hiu_sdk.ApiClient(configuration) as api_client:
    
    api_instance = abdm_hiu_sdk.DefaultAPI(api_client)  
        
    # Example to request health information
    try:
        health_info_request_payload = {
            "patient_id": "12345",
            "requester_id": "req123",
            "requested_data": {
                "type": "lab_reports",
                "date_range": {
                    "from": "2023-01-01",
                    "to": "2023-12-31"
                }
            }
        }
        request_health_info_response = api_instance.request_health_information(health_info_request_payload)
        pprint("Requested Health Information:")
        pprint(request_health_info_response)
    except ApiException as e:
        print(f"Exception when calling DefaultAPI->request_health_information: {e}\n")