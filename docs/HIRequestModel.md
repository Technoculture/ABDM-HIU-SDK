# HIRequestModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** |  | 
**timestamp** | **datetime** | Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ | 
**hi_request** | [**HIRequestHiRequestModelModel**](HIRequestHiRequestModel.md) |  | 

## Example

```python
from abdm.abdm.model.hi_request_model import HIRequestModel

# TODO update the JSON string below
json = "{}"
# create an instance of HIRequestModel from a JSON string
hi_request_model_instance = HIRequestModel.from_json(json)
# print the JSON string representation of the object
print(HIRequestModel.to_json())

# convert the object into a dict
hi_request_model_dict = hi_request_model_instance.to_dict()
# create an instance of HIRequestModel from a dict
hi_request_model_from_dict = HIRequestModel.from_dict(hi_request_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


