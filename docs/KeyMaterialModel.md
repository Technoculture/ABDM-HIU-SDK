# KeyMaterialModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**crypto_alg** | **str** |  | 
**curve** | **str** |  | 
**dh_public_key** | [**KeyObjectModelModel**](KeyObjectModel.md) |  | 
**nonce** | **str** |  | 

## Example

```python
from abdm.abdm.model.key_material_model import KeyMaterialModel

# TODO update the JSON string below
json = "{}"
# create an instance of KeyMaterialModel from a JSON string
key_material_model_instance = KeyMaterialModel.from_json(json)
# print the JSON string representation of the object
print(KeyMaterialModel.to_json())

# convert the object into a dict
key_material_model_dict = key_material_model_instance.to_dict()
# create an instance of KeyMaterialModel from a dict
key_material_model_from_dict = KeyMaterialModel.from_dict(key_material_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


