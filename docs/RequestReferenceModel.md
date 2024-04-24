# RequestReferenceModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | the requestId that was passed | 

## Example

```python
from abdm.abdm.model.request_reference_model import RequestReferenceModel

# TODO update the JSON string below
json = "{}"
# create an instance of RequestReferenceModel from a JSON string
request_reference_model_instance = RequestReferenceModel.from_json(json)
# print the JSON string representation of the object
print(RequestReferenceModel.to_json())

# convert the object into a dict
request_reference_model_dict = request_reference_model_instance.to_dict()
# create an instance of RequestReferenceModel from a dict
request_reference_model_from_dict = RequestReferenceModel.from_dict(request_reference_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


