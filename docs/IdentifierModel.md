# IdentifierModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**IdentifierTypeModelModel**](IdentifierTypeModel.md) |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from abdm.abdm.model.identifier_model import IdentifierModel

# TODO update the JSON string below
json = "{}"
# create an instance of IdentifierModel from a JSON string
identifier_model_instance = IdentifierModel.from_json(json)
# print the JSON string representation of the object
print(IdentifierModel.to_json())

# convert the object into a dict
identifier_model_dict = identifier_model_instance.to_dict()
# create an instance of IdentifierModel from a dict
identifier_model_from_dict = IdentifierModel.from_dict(identifier_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


