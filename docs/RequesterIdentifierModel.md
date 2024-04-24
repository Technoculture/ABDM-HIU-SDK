# RequesterIdentifierModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**value** | **str** |  | 
**system** | **str** |  | [optional] 

## Example

```python
from abdm.abdm.model.requester_identifier_model import RequesterIdentifierModel

# TODO update the JSON string below
json = "{}"
# create an instance of RequesterIdentifierModel from a JSON string
requester_identifier_model_instance = RequesterIdentifierModel.from_json(json)
# print the JSON string representation of the object
print(RequesterIdentifierModel.to_json())

# convert the object into a dict
requester_identifier_model_dict = requester_identifier_model_instance.to_dict()
# create an instance of RequesterIdentifierModel from a dict
requester_identifier_model_from_dict = RequesterIdentifierModel.from_dict(requester_identifier_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


