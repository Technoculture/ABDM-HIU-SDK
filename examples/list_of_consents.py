import abdm
from abdm.rest import ApiException
from pprint import pprint

# Configuration for the API client, using default URL for demonstration
configuration = abdm.Configuration(host="https://dev.abdm.gov.in/gateway")

# Creating an API client instance
with abdm.ApiClient(configuration) as api_client:
    # Instance of the DefaultAPI class
    api_instance = abdm.DefaultAPI(api_client)

    # Example to fetch a list of all consents
    try:
        list_consents_response = api_instance.list_consents()
        pprint("List of Consents:")
        pprint(list_consents_response)
    except ApiException as e:
        print(f"Exception when calling DefaultAPI->list_consents: {e}\n")
