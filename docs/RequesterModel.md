# RequesterModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**identifier** | [**RequesterIdentifierModelModel**](RequesterIdentifierModel.md) |  | [optional] 

## Example

```python
from abdm.abdm.model.requester_model import RequesterModel

# TODO update the JSON string below
json = "{}"
# create an instance of RequesterModel from a JSON string
requester_model_instance = RequesterModel.from_json(json)
# print the JSON string representation of the object
print(RequesterModel.to_json())

# convert the object into a dict
requester_model_dict = requester_model_instance.to_dict()
# create an instance of RequesterModel from a dict
requester_model_from_dict = RequesterModel.from_dict(requester_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


