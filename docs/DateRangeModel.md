# DateRangeModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **datetime** |  | 
**to** | **datetime** |  | 

## Example

```python
from abdm.abdm.model.date_range_model import DateRangeModel

# TODO update the JSON string below
json = "{}"
# create an instance of DateRangeModel from a JSON string
date_range_model_instance = DateRangeModel.from_json(json)
# print the JSON string representation of the object
print(DateRangeModel.to_json())

# convert the object into a dict
date_range_model_dict = date_range_model_instance.to_dict()
# create an instance of DateRangeModel from a dict
date_range_model_from_dict = DateRangeModel.from_dict(date_range_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


