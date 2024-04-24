# SessionRequestModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** |  | 
**client_secret** | **str** |  | 

## Example

```python
from abdm.abdm.model.session_request_model import SessionRequestModel

# TODO update the JSON string below
json = "{}"
# create an instance of SessionRequestModel from a JSON string
session_request_model_instance = SessionRequestModel.from_json(json)
# print the JSON string representation of the object
print(SessionRequestModel.to_json())

# convert the object into a dict
session_request_model_dict = session_request_model_instance.to_dict()
# create an instance of SessionRequestModel from a dict
session_request_model_from_dict = SessionRequestModel.from_dict(session_request_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


