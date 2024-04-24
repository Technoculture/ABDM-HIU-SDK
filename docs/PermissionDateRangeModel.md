# PermissionDateRangeModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **datetime** |  | 
**to** | **datetime** |  | 

## Example

```python
from abdm.abdm.model.permission_date_range_model import PermissionDateRangeModel

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionDateRangeModel from a JSON string
permission_date_range_model_instance = PermissionDateRangeModel.from_json(json)
# print the JSON string representation of the object
print(PermissionDateRangeModel.to_json())

# convert the object into a dict
permission_date_range_model_dict = permission_date_range_model_instance.to_dict()
# create an instance of PermissionDateRangeModel from a dict
permission_date_range_model_from_dict = PermissionDateRangeModel.from_dict(permission_date_range_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


