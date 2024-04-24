# PermissionFrequencyModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unit** | **str** |  | 
**value** | **int** |  | 
**repeats** | **int** |  | 

## Example

```python
from abdm.abdm.model.permission_frequency_model import PermissionFrequencyModel

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionFrequencyModel from a JSON string
permission_frequency_model_instance = PermissionFrequencyModel.from_json(json)
# print the JSON string representation of the object
print(PermissionFrequencyModel.to_json())

# convert the object into a dict
permission_frequency_model_dict = permission_frequency_model_instance.to_dict()
# create an instance of PermissionFrequencyModel from a dict
permission_frequency_model_from_dict = PermissionFrequencyModel.from_dict(permission_frequency_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


