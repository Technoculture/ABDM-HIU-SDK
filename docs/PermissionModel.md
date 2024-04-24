# PermissionModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_mode** | **str** |  | 
**date_range** | [**PermissionDateRangeModelModel**](PermissionDateRangeModel.md) |  | 
**data_erase_at** | **datetime** |  | 
**frequency** | [**PermissionFrequencyModelModel**](PermissionFrequencyModel.md) |  | 

## Example

```python
from abdm.abdm.model.permission_model import PermissionModel

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionModel from a JSON string
permission_model_instance = PermissionModel.from_json(json)
# print the JSON string representation of the object
print(PermissionModel.to_json())

# convert the object into a dict
permission_model_dict = permission_model_instance.to_dict()
# create an instance of PermissionModel from a dict
permission_model_from_dict = PermissionModel.from_dict(permission_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


