# ConsentRequestStatusRequestModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | a nonce, unique for each HTTP request | 
**timestamp** | **datetime** | Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ | 
**consent_request_id** | **str** |  | 

## Example

```python
from abdm.abdm.model.consent_request_status_request_model import ConsentRequestStatusRequestModel

# TODO update the JSON string below
json = "{}"
# create an instance of ConsentRequestStatusRequestModel from a JSON string
consent_request_status_request_model_instance = ConsentRequestStatusRequestModel.from_json(json)
# print the JSON string representation of the object
print(ConsentRequestStatusRequestModel.to_json())

# convert the object into a dict
consent_request_status_request_model_dict = consent_request_status_request_model_instance.to_dict()
# create an instance of ConsentRequestStatusRequestModel from a dict
consent_request_status_request_model_from_dict = ConsentRequestStatusRequestModel.from_dict(consent_request_status_request_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


