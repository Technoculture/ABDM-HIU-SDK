# SessionResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** |  | [optional] 
**expires_in** | **int** | In Minutes | [optional] 
**refresh_expires_in** | **int** | In Minutes | [optional] 
**refresh_token** | **str** |  | [optional] 
**token_type** | **str** |  | [optional] 

## Example

```python
from abdm.abdm.model.session_response_model import SessionResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of SessionResponseModel from a JSON string
session_response_model_instance = SessionResponseModel.from_json(json)
# print the JSON string representation of the object
print(SessionResponseModel.to_json())

# convert the object into a dict
session_response_model_dict = session_response_model_instance.to_dict()
# create an instance of SessionResponseModel from a dict
session_response_model_from_dict = SessionResponseModel.from_dict(session_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


