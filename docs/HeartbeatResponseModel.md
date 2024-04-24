# HeartbeatResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **datetime** | Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ | 
**status** | **str** |  | 
**error** | [**ErrorModelModel**](ErrorModel.md) |  | [optional] 

## Example

```python
from abdm.abdm.model.heartbeat_response_model import HeartbeatResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of HeartbeatResponseModel from a JSON string
heartbeat_response_model_instance = HeartbeatResponseModel.from_json(json)
# print the JSON string representation of the object
print(HeartbeatResponseModel.to_json())

# convert the object into a dict
heartbeat_response_model_dict = heartbeat_response_model_instance.to_dict()
# create an instance of HeartbeatResponseModel from a dict
heartbeat_response_model_from_dict = HeartbeatResponseModel.from_dict(heartbeat_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


