import abdm
from abdm.rest import ApiException
from pprint import pprint

# Configuration for the API client, using default URL for demonstration
configuration = abdm.Configuration(host="https://sandbox.abdm.gov.in")

# Creating an API client instance
with abdm.ApiClient(configuration) as api_client:
    # Instance of the DefaultAPI class
    api_instance = abdm.DefaultAPI(api_client)
    # Retrieve a specific consent by its primary key (pk)
    try:
        consent_pk = "consent123"
        retrieve_consent_response = api_instance.retrieve_consent(consent_pk)
        pprint("Retrieved Consent Details:")
        pprint(retrieve_consent_response)
    except ApiException as e:
        print(f"Exception when calling DefaultAPI->retrieve_consent: {e}\n")
