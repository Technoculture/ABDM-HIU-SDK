# HIRequestHiRequestModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consent** | [**ConsentModelModel**](ConsentModel.md) |  | 
**date_range** | [**DateRangeModelModel**](DateRangeModel.md) |  | 
**data_push_url** | **str** |  | 
**key_material** | [**KeyMaterialModelModel**](KeyMaterialModel.md) |  | 

## Example

```python
from abdm.abdm.model.hi_request_hi_request_model import HIRequestHiRequestModel

# TODO update the JSON string below
json = "{}"
# create an instance of HIRequestHiRequestModel from a JSON string
hi_request_hi_request_model_instance = HIRequestHiRequestModel.from_json(json)
# print the JSON string representation of the object
print(HIRequestHiRequestModel.to_json())

# convert the object into a dict
hi_request_hi_request_model_dict = hi_request_hi_request_model_instance.to_dict()
# create an instance of HIRequestHiRequestModel from a dict
hi_request_hi_request_model_from_dict = HIRequestHiRequestModel.from_dict(hi_request_hi_request_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


