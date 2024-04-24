# AuthConfirmIdentifierModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**AuthConfirmIdentifierTypeModelModel**](AuthConfirmIdentifierTypeModel.md) |  | 
**value** | **str** |  | 

## Example

```python
from abdm.abdm.model.auth_confirm_identifier_model import AuthConfirmIdentifierModel

# TODO update the JSON string below
json = "{}"
# create an instance of AuthConfirmIdentifierModel from a JSON string
auth_confirm_identifier_model_instance = AuthConfirmIdentifierModel.from_json(json)
# print the JSON string representation of the object
print(AuthConfirmIdentifierModel.to_json())

# convert the object into a dict
auth_confirm_identifier_model_dict = auth_confirm_identifier_model_instance.to_dict()
# create an instance of AuthConfirmIdentifierModel from a dict
auth_confirm_identifier_model_from_dict = AuthConfirmIdentifierModel.from_dict(auth_confirm_identifier_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


