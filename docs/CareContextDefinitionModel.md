# CareContextDefinitionModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**patient_reference** | **str** |  | 
**care_context_reference** | **str** |  | 

## Example

```python
from abdm.abdm.model.care_context_definition_model import CareContextDefinitionModel

# TODO update the JSON string below
json = "{}"
# create an instance of CareContextDefinitionModel from a JSON string
care_context_definition_model_instance = CareContextDefinitionModel.from_json(json)
# print the JSON string representation of the object
print(CareContextDefinitionModel.to_json())

# convert the object into a dict
care_context_definition_model_dict = care_context_definition_model_instance.to_dict()
# create an instance of CareContextDefinitionModel from a dict
care_context_definition_model_from_dict = CareContextDefinitionModel.from_dict(care_context_definition_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


