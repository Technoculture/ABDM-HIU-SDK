# KeyObjectModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expiry** | **datetime** |  | 
**parameters** | **str** |  | 
**key_value** | **str** |  | 

## Example

```python
from abdm.abdm.model.key_object_model import KeyObjectModel

# TODO update the JSON string below
json = "{}"
# create an instance of KeyObjectModel from a JSON string
key_object_model_instance = KeyObjectModel.from_json(json)
# print the JSON string representation of the object
print(KeyObjectModel.to_json())

# convert the object into a dict
key_object_model_dict = key_object_model_instance.to_dict()
# create an instance of KeyObjectModel from a dict
key_object_model_from_dict = KeyObjectModel.from_dict(key_object_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


