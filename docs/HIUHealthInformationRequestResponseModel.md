# HIUHealthInformationRequestResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** |  | 
**timestamp** | **datetime** | Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ | 
**hi_request** | [**HIUHealthInformationRequestResponseHiRequestModelModel**](HIUHealthInformationRequestResponseHiRequestModel.md) |  | [optional] 
**error** | [**ErrorModelModel**](ErrorModel.md) |  | [optional] 
**resp** | [**RequestReferenceModelModel**](RequestReferenceModel.md) |  | 

## Example

```python
from abdm.abdm.model.hiu_health_information_request_response_model import HIUHealthInformationRequestResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of HIUHealthInformationRequestResponseModel from a JSON string
hiu_health_information_request_response_model_instance = HIUHealthInformationRequestResponseModel.from_json(json)
# print the JSON string representation of the object
print(HIUHealthInformationRequestResponseModel.to_json())

# convert the object into a dict
hiu_health_information_request_response_model_dict = hiu_health_information_request_response_model_instance.to_dict()
# create an instance of HIUHealthInformationRequestResponseModel from a dict
hiu_health_information_request_response_model_from_dict = HIUHealthInformationRequestResponseModel.from_dict(hiu_health_information_request_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


