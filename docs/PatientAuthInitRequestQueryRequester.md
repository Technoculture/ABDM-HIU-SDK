# PatientAuthInitRequestQueryRequester

identification of requester

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**id** | **str** |  | 

## Example

```python
from abdm.models.patient_auth_init_request_query_requester import PatientAuthInitRequestQueryRequester

# TODO update the JSON string below
json = "{}"
# create an instance of PatientAuthInitRequestQueryRequester from a JSON string
patient_auth_init_request_query_requester_instance = PatientAuthInitRequestQueryRequester.from_json(json)
# print the JSON string representation of the object
print(PatientAuthInitRequestQueryRequester.to_json())

# convert the object into a dict
patient_auth_init_request_query_requester_dict = patient_auth_init_request_query_requester_instance.to_dict()
# create an instance of PatientAuthInitRequestQueryRequester from a dict
patient_auth_init_request_query_requester_from_dict = PatientAuthInitRequestQueryRequester.from_dict(patient_auth_init_request_query_requester_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


