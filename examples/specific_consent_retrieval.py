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
    # Retrieve a specific consent by its primary key (pk)
    try:
        consent_pk = "consent123"
        retrieve_consent_response = api_instance.retrieve_consent(consent_pk)
        pprint("Retrieved Consent Details:")
        pprint(retrieve_consent_response)
    except ApiException as e:
        print(f"Exception when calling DefaultAPI->retrieve_consent: {e}\n")

