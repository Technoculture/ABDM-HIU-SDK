# EventCategoryDetailModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**care_context** | [**CareContextDefinitionModelModel**](CareContextDefinitionModel.md) |  | 
**hi_types** | [**List[HITypeEnumModelModel]**](HITypeEnumModel.md) |  | 

## Example

```python
from abdm.abdm.model.event_category_detail_model import EventCategoryDetailModel

# TODO update the JSON string below
json = "{}"
# create an instance of EventCategoryDetailModel from a JSON string
event_category_detail_model_instance = EventCategoryDetailModel.from_json(json)
# print the JSON string representation of the object
print(EventCategoryDetailModel.to_json())

# convert the object into a dict
event_category_detail_model_dict = event_category_detail_model_instance.to_dict()
# create an instance of EventCategoryDetailModel from a dict
event_category_detail_model_from_dict = EventCategoryDetailModel.from_dict(event_category_detail_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


